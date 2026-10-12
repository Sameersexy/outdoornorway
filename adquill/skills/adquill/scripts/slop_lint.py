#!/usr/bin/env python3
"""adquill slop_lint: flag stock-phrase patterns, policy risks and slot overruns in ad copy.

Run it like this:

    python3 -I skills/adquill/scripts/slop_lint.py FILE_OR_TEXT
    python3 -I skills/adquill/scripts/slop_lint.py --text "Ski touring day, NOK 4,900" --slot meta_headline
    cat draft.txt | python3 -I skills/adquill/scripts/slop_lint.py --json

What it is: a deterministic pattern checker. The same text always gets the same score.
What it is not: an AI detector. It never claims to know who or what wrote a text. It flags
patterns (stock words, empty structure, risky claims, over-long slots) that make ad copy read
as automated or that platforms and regulators treat as risky. Humans write these patterns too.

Standard library only. No network. Writes no files. Python 3.9 or newer.
All rules live in rules.json next to this file, so a contributor adds a pattern in one place.
"""

import argparse
import json
import os
import re
import statistics
import sys

VERSION = "1.0.0"
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_RULES = os.path.join(HERE, "rules.json")

EXIT_OK = 0
EXIT_BELOW_THRESHOLD = 1
EXIT_USAGE = 2
EXIT_RULES = 3

SEVERITIES = ("block", "warn", "note")
CATEGORIES = (
    "lexical", "structural", "tonal", "rhythmic", "formatting", "semantic",
    "ad-specific", "travel-specific", "policy", "platform",
)
PROFILES = ("ad", "doc", "code")
REQUIRED_KEYS = ("id", "category", "severity", "weight", "pattern", "flags", "message", "suggestion")
MAX_INPUT_BYTES = 2 * 1024 * 1024

DISCLAIMER = (
    "slop_lint flags patterns. It cannot tell who or what wrote a text, it is not an AI "
    "detector, and a clean score does not mean the copy is good or true."
)

APOS_CLASS = "['’]"
MARK_RE = re.compile(r"<!--\s*adquill-lint:\s*(ignore-start|ignore-end|ignore-line)\s*-->")
FENCE_RE = re.compile(r"(?ms)^[ \t]*(```|~~~).*?^[ \t]*\1[^\n]*$")
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
URL_RE = re.compile(r"https?://[^\s)>\]]+")
QUOTE_RE = re.compile(r"\"[^\"\n]{2,300}\"|“[^”\n]{2,300}”")
WORD_RE = re.compile(r"\d[\d,.:]*\d|\d|[A-Za-zÀ-ɏ]+(?:['’\-][A-Za-zÀ-ɏ]+)*")
SENT_SPLIT_RE = re.compile(r"(?<=[.!?])[\"”)\]]*\s+(?=[\"“(\[]?[A-Z0-9À-Þ])")
NUMBER_WORDS = {
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven",
    "twelve", "twenty", "thirty", "forty", "fifty", "hundred", "thousand", "dozen", "half",
}
STARTERS = {
    "the", "a", "an", "we", "you", "it", "this", "that", "these", "those", "our", "your", "my",
    "if", "in", "on", "at", "for", "to", "and", "but", "or", "so", "no", "not", "there", "here",
    "when", "what", "why", "how", "who", "with", "from", "by", "as", "is", "are", "was", "be",
    "do", "can", "will", "all", "every", "each", "some", "most", "then", "now", "just", "only",
    "also", "pick", "book", "bring", "check", "see", "add", "ski", "skin", "come", "get", "go",
    "join", "learn", "meet", "take", "try", "use", "wear", "pack", "ask", "call", "choose",
    "start", "stop", "wait", "walk", "climb", "carry", "keep", "let", "make", "read", "send",
    "tell", "think", "look", "find", "give", "bring", "expect", "remember", "plan", "mark",
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "i", "he",
    "she", "they", "his", "her", "their", "its", "these", "after", "before", "once", "while",
    "until", "since", "because", "though", "although", "both", "either", "neither", "many",
    "much", "more", "less", "any", "own", "same", "such", "very", "too", "yes", "ok", "okay",
}


class RulesError(Exception):
    """Raised when rules.json is missing, unreadable or invalid."""


# ---------------------------------------------------------------------------
# Rules
# ---------------------------------------------------------------------------

def _flags_from_string(flag_string):
    value = 0
    for ch in flag_string or "":
        if ch == "i":
            value |= re.IGNORECASE
        elif ch == "m":
            value |= re.MULTILINE
        elif ch == "s":
            value |= re.DOTALL
        elif ch == "x":
            value |= re.VERBOSE
        else:
            raise RulesError("unknown regex flag %r" % ch)
    return value


def _expand(pattern):
    return pattern.replace("~", APOS_CLASS)


def _compile_optional(rule, key):
    raw = rule.get(key)
    if not raw:
        return None
    try:
        return re.compile(_expand(raw), re.IGNORECASE)
    except re.error as exc:
        raise RulesError("rule %s: bad %s regex: %s" % (rule.get("id"), key, exc))


def load_rules(path=DEFAULT_RULES):
    """Load and validate rules.json. Returns a dict with compiled rules, slots and lists."""
    try:
        with open(path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, ValueError) as exc:
        raise RulesError("cannot read rules file %s: %s" % (path, exc))
    if not isinstance(data, dict) or not isinstance(data.get("rules"), list):
        raise RulesError("rules file must be an object with a 'rules' list")
    slots = data.get("slots", {})
    seen = set()
    compiled = []
    for rule in data["rules"]:
        for key in REQUIRED_KEYS:
            if key not in rule:
                raise RulesError("rule %r is missing key %r" % (rule.get("id", "?"), key))
        rid = rule["id"]
        if rid in seen:
            raise RulesError("duplicate rule id %s" % rid)
        seen.add(rid)
        if rule["severity"] not in SEVERITIES:
            raise RulesError("rule %s: severity must be one of %s" % (rid, ", ".join(SEVERITIES)))
        if rule["category"] not in CATEGORIES:
            raise RulesError("rule %s: unknown category %r" % (rid, rule["category"]))
        if not isinstance(rule["weight"], (int, float)) or rule["weight"] < 0:
            raise RulesError("rule %s: weight must be a number of zero or more" % rid)
        rtype = rule.get("type", "regex")
        if rtype not in ("regex", "caps", "metric", "slot_limit", "builtin"):
            raise RulesError("rule %s: unknown type %r" % (rid, rtype))
        profiles = rule.get("profiles", ["ad", "doc"])
        for prof in profiles:
            if prof not in PROFILES:
                raise RulesError("rule %s: unknown profile %r" % (rid, prof))
        for slot_key in ("slots", "not_slots"):
            for slot in rule.get(slot_key, []):
                if slot not in slots:
                    raise RulesError("rule %s: unknown slot %r" % (rid, slot))
        entry = dict(rule)
        entry["type"] = rtype
        entry["profiles"] = profiles
        entry["regex"] = None
        if rtype in ("regex",):
            if not rule["pattern"]:
                raise RulesError("rule %s: regex rules need a pattern" % rid)
            try:
                entry["regex"] = re.compile(_expand(rule["pattern"]), _flags_from_string(rule["flags"]))
            except re.error as exc:
                raise RulesError("rule %s: bad pattern: %s" % (rid, exc))
        entry["sup_ctx"] = _compile_optional(rule, "suppress_if_context")
        entry["sup_before"] = _compile_optional(rule, "suppress_if_before")
        entry["sup_after"] = _compile_optional(rule, "suppress_if_after")
        compiled.append(entry)
    return {
        "rules": compiled,
        "slots": slots,
        "caps_allowlist": set(data.get("caps_allowlist", [])),
        "allowlist": list(data.get("allowlist", [])),
        "version": data.get("version", "unknown"),
    }


# ---------------------------------------------------------------------------
# Text preparation
# ---------------------------------------------------------------------------

def _line_of(text, index):
    return text.count("\n", 0, index) + 1


def mask_spans(text, spans):
    """Blank out spans with spaces. Newlines stay, so line numbers and offsets hold."""
    if not spans:
        return text
    chars = list(text)
    for start, end in spans:
        for i in range(start, min(end, len(chars))):
            if chars[i] != "\n":
                chars[i] = " "
    return "".join(chars)


def ignore_spans(text):
    """Return (spans, problems) for lint-ignore markers."""
    spans = []
    problems = []
    open_at = None
    for match in MARK_RE.finditer(text):
        kind = match.group(1)
        if kind == "ignore-start":
            if open_at is None:
                open_at = match.start()
            else:
                problems.append(("nested", _line_of(text, match.start())))
        elif kind == "ignore-end":
            if open_at is None:
                problems.append(("stray_end", _line_of(text, match.start())))
            else:
                spans.append((open_at, match.end()))
                open_at = None
        else:
            line_start = text.rfind("\n", 0, match.start()) + 1
            line_end = text.find("\n", match.end())
            spans.append((line_start, len(text) if line_end == -1 else line_end))
    if open_at is not None:
        spans.append((open_at, len(text)))
        problems.append(("unclosed", _line_of(text, open_at)))
    return spans, problems


def find_spans(regex, text):
    return [(m.start(), m.end()) for m in regex.finditer(text)]


def extract_prose(text):
    """Keep prose lines of a markdown document for rhythm metrics."""
    lines = text.split("\n")
    kept = []
    in_front = bool(lines) and lines[0].strip() == "---"
    for index, line in enumerate(lines):
        stripped = line.strip()
        if in_front:
            if index > 0 and stripped == "---":
                in_front = False
            continue
        if not stripped:
            kept.append("")
            continue
        if stripped.startswith(("|", "#", ">", "<!--")) or re.match(r"^[-*_]{3,}$", stripped):
            continue
        stripped = re.sub(r"^(?:[-*+]|\d+[.)])\s+", "", stripped)
        kept.append(stripped)
    return "\n".join(kept)


def split_sentences(text):
    out = []
    for line in re.split(r"\n+", text):
        line = line.strip()
        if not line:
            continue
        for part in SENT_SPLIT_RE.split(line):
            part = part.strip()
            if part:
                out.append(part)
    return out


def tokenize(text):
    return WORD_RE.findall(text)


def count_slot_chars(slot, text):
    """Character count for a slot. On X a link counts as 23 (reported, see rules.json)."""
    value = text.strip()
    if slot in ("x_post", "x_card_description", "x_card_headline"):
        value = URL_RE.sub("x" * 23, value)
    return len(value)


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def _specifics(sentences):
    digits = 0
    names = 0
    for sentence in sentences:
        tokens = tokenize(sentence)
        for index, tok in enumerate(tokens):
            if tok[0].isdigit() or tok.lower() in NUMBER_WORDS:
                digits += 1
            elif tok[0].isupper() and tok != "I":
                if index > 0:
                    names += 1
                elif tok.lower() not in STARTERS:
                    names += 1
    return digits, names


def metric_sentence_cv(ctx, params):
    lens = ctx["lens"]
    if len(lens) < params.get("min_sentences", 6):
        return None
    mean = statistics.mean(lens)
    if mean <= 0:
        return None
    cv = statistics.pstdev(lens) / mean
    if cv < params.get("max_cv", 0.35):
        return "sentence lengths barely vary (variation %.2f, mean %.1f words)" % (cv, mean)
    return None


def metric_no_short_sentence(ctx, params):
    lens = ctx["lens"]
    if len(lens) < params.get("min_sentences", 6):
        return None
    if min(lens) > params.get("short", 6):
        return "the shortest sentence has %d words" % min(lens)
    return None


def metric_repeated_opener(ctx, params):
    sents = ctx["sentences"]
    if len(sents) < params.get("min_sentences", 4):
        return None
    skip = set(params.get("ignore", ["the", "a", "an", "and", "but", "or", "so"]))
    firsts = []
    for sentence in sents:
        toks = tokenize(sentence)
        if toks:
            firsts.append(toks[0].lower())
    worst = None
    for word in sorted(set(firsts)):
        if word in skip:
            continue
        n = firsts.count(word)
        if n >= params.get("min_count", 3) and (worst is None or n > worst[1]):
            worst = (word, n)
    if worst:
        return "%d sentences start with '%s'" % (worst[1], worst[0])
    return None


def metric_drumbeat(ctx, params):
    lens = ctx["lens"]
    run = params.get("run", 4)
    tol = params.get("tolerance", 2)
    floor = params.get("min_words", 5)
    for i in range(0, len(lens) - run + 1):
        window = lens[i:i + run]
        if min(window) >= floor and max(window) - min(window) <= tol:
            return "%d sentences in a row run %d to %d words" % (run, min(window), max(window))
    return None


def metric_long_sentence(ctx, params):
    limit = params.get("max_words", 35)
    longest = max(ctx["lens"]) if ctx["lens"] else 0
    if longest > limit:
        return "one sentence runs %d words" % longest
    return None


def metric_paragraph_uniform(ctx, params):
    paras = [p for p in re.split(r"\n\s*\n", ctx["text"]) if p.strip()]
    counts = [len(split_sentences(p)) for p in paras]
    if len(counts) >= params.get("min_paragraphs", 4) and min(counts) >= 2 and len(set(counts)) == 1:
        return "%d paragraphs of %d sentences each" % (len(counts), counts[0])
    return None


def metric_specificity(ctx, params):
    words = ctx["n_words"]
    if words < params.get("min_words", 40):
        return None
    digits, names = _specifics(ctx["sentences"])
    per_100 = (digits + names) * 100.0 / words
    if per_100 < params.get("min_per_100", 3):
        return "%d numbers and %d names in %d words" % (digits, names, words)
    return None


def metric_no_specifics_short(ctx, params):
    words = ctx["n_words"]
    if words < params.get("min_words", 20) or words >= params.get("max_words", 40):
        return None
    digits, names = _specifics(ctx["sentences"])
    if digits + names == 0:
        return "no number, date, place or name in %d words" % words
    return None


def metric_exclamations(ctx, params):
    n = ctx["text"].count("!")
    if n > params.get("max", 1):
        return "%d exclamation marks" % n
    return None


def metric_tricolon(ctx, params):
    if ctx["n_words"] < params.get("min_words", 40):
        return None
    found = re.findall(r"\b[A-Za-z-]{3,}, [A-Za-z-]{3,},? (?:and|&|or) [A-Za-z-]{3,}\b", ctx["text"])
    if len(found) >= params.get("min_lists", 2):
        return "%d three-item lists (%s)" % (len(found), "; ".join(found[:2]))
    return None


def metric_colon_reveals(ctx, params):
    n = len(re.findall(r"[A-Za-z]: [A-Z]", ctx["text"]))
    if n >= params.get("min", 3):
        return "%d colon reveals" % n
    return None


def metric_no_contractions(ctx, params):
    if ctx["n_words"] < params.get("min_words", 40):
        return None
    lowered = ctx["text"].lower()
    if not re.search(r"\b(?:you|we)\b", lowered):
        return None
    if re.search(r"\b\w+['’](?:s|re|ll|ve|d|t|m)\b", lowered):
        return None
    return "no contractions in %d words" % ctx["n_words"]


def metric_duplicate_sentence(ctx, params):
    seen = set()
    for sentence in ctx["sentences"]:
        key = re.sub(r"\W+", " ", sentence.lower()).strip()
        if len(key.split()) < params.get("min_words", 3):
            continue
        if key in seen:
            return "'%s' appears twice" % sentence[:50]
        seen.add(key)
    return None


def metric_open_verify(ctx, params):
    n = len(re.findall(r"\[VERIFY", ctx["raw_text"]))
    if n:
        return "%d open [VERIFY] token%s: status is draft, not ready to publish" % (n, "" if n == 1 else "s")
    return None


def metric_visible_no_number(ctx, params):
    visible = ctx["raw_text"].strip()[:params.get("visible", 125)]
    if visible and not re.search(r"\d", visible):
        return "no number in the first %d characters" % params.get("visible", 125)
    return None


METRICS = {
    "sentence_cv": metric_sentence_cv,
    "no_short_sentence": metric_no_short_sentence,
    "repeated_opener": metric_repeated_opener,
    "drumbeat": metric_drumbeat,
    "long_sentence": metric_long_sentence,
    "paragraph_uniform": metric_paragraph_uniform,
    "specificity": metric_specificity,
    "no_specifics_short": metric_no_specifics_short,
    "exclamations": metric_exclamations,
    "tricolon": metric_tricolon,
    "colon_reveals": metric_colon_reveals,
    "no_contractions": metric_no_contractions,
    "duplicate_sentence": metric_duplicate_sentence,
    "open_verify": metric_open_verify,
    "visible_no_number": metric_visible_no_number,
}


# ---------------------------------------------------------------------------
# Engine
# ---------------------------------------------------------------------------

def detect_profile(source_path, from_stdin_or_text):
    if from_stdin_or_text or not source_path:
        return "ad"
    ext = os.path.splitext(source_path)[1].lower()
    if ext in (".md", ".markdown", ".rst", ".mdx"):
        return "doc"
    if ext in (".py", ".json", ".toml", ".yml", ".yaml", ".cfg", ".ini", ".sh", ".js", ".ts"):
        return "code"
    return "ad"


def _applies(rule, profile, slot):
    if profile not in rule["profiles"]:
        return False
    slots = rule.get("slots")
    if slots is not None and slot not in slots:
        return False
    if slot is not None and slot in rule.get("not_slots", []):
        return False
    return True


def _suppressed(rule, text, match):
    window = rule.get("context_window", 40)
    start, end = match.start(), match.end()
    if rule["sup_ctx"] is not None:
        if rule["sup_ctx"].search(text[max(0, start - window):min(len(text), end + window)]):
            return True
    if rule["sup_before"] is not None:
        if rule["sup_before"].search(text[max(0, start - window):start]):
            return True
    if rule["sup_after"] is not None:
        if rule["sup_after"].search(text[end:end + window]):
            return True
    return False


def _make_hit(rule, text, start, end, detail=None, line_starts=None):
    line = _line_of(text, start)
    line_begin = text.rfind("\n", 0, start) + 1
    shown = text[start:end].replace("\n", " ").strip()
    if len(shown) > 80:
        shown = shown[:77] + "..."
    message = rule["message"]
    if detail:
        message = message.replace("{detail}", detail)
    hit = {
        "id": rule["id"],
        "category": rule["category"],
        "severity": rule["severity"],
        "weight": rule["weight"],
        "line": line,
        "col": start - line_begin + 1,
        "match": shown,
        "message": message,
        "suggestion": rule["suggestion"],
    }
    if rule.get("example_fix"):
        hit["example"] = rule["example_fix"]
    return hit


def _caps_hits(rule, scan, allowlist):
    hits = []
    for run in re.finditer(r"\b[A-Z]{2,}\b(?:[ ][A-Z]{2,}\b)*", scan):
        tokens = [(m.group(0), run.start() + m.start()) for m in re.finditer(r"[A-Z]{2,}", run.group(0))]
        live = [(tok, pos) for tok, pos in tokens if tok not in allowlist]
        if not live:
            continue
        long_ones = [(tok, pos) for tok, pos in live if len(tok) >= 4]
        if long_ones:
            tok, pos = long_ones[0]
            hits.append((pos, pos + len(tok)))
        elif len(live) >= 2:
            first, last = live[0], live[-1]
            hits.append((first[1], last[1] + len(last[0])))
    return hits


def _dedupe(hits):
    """Drop a hit that sits inside a heavier hit of the same category, or has the same span."""
    ordered = sorted(hits, key=lambda h: (-h["weight"], h["_start"], h["id"]))
    kept = []
    for hit in ordered:
        drop = False
        for other in kept:
            same_span = (hit["_start"], hit["_end"]) == (other["_start"], other["_end"])
            inside = (other["_start"] <= hit["_start"] and hit["_end"] <= other["_end"]
                      and other["category"] == hit["category"])
            if hit["id"] != other["id"] and (same_span or inside):
                drop = True
                break
        if not drop:
            kept.append(hit)
    return kept


def lint_text(text, rules, profile="ad", slot=None, extra_allow=None, skip_quotes=False,
              ignore_rules=None, limit_override=None, dedupe=True):
    """Lint text. Returns a result dict. Never raises on odd input."""
    ignore_rules = set(ignore_rules or [])
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    raw_text = text
    warnings = []

    problems = []
    if profile != "code":
        spans, problems = ignore_spans(text)
        text = mask_spans(text, spans)
    if profile == "doc":
        text = mask_spans(text, find_spans(FENCE_RE, text))
        text = mask_spans(text, find_spans(INLINE_CODE_RE, text))
    scan = text
    scan = mask_spans(scan, find_spans(URL_RE, scan))
    if skip_quotes:
        scan = mask_spans(scan, find_spans(QUOTE_RE, scan))
    allow_phrases = list(rules["allowlist"]) + list(extra_allow or [])
    for phrase in allow_phrases:
        if not phrase:
            continue
        scan = mask_spans(scan, find_spans(re.compile(re.escape(phrase), re.IGNORECASE), scan))

    prose = extract_prose(text) if profile == "doc" else text
    sentences = split_sentences(prose)
    lens = [len(tokenize(s)) for s in sentences]
    n_words = sum(lens)
    ctx = {
        "text": prose, "raw_text": text, "sentences": sentences, "lens": lens,
        "n_words": n_words, "profile": profile, "slot": slot,
    }

    raw_hits = []
    slot_info = None
    chars = None
    if slot is not None:
        chars = count_slot_chars(slot, text)
        slot_info = {"name": slot, "chars": chars, "limit": None}
        meta = rules["slots"].get(slot, {})
        slot_info["limit"] = limit_override if limit_override else meta.get("limit")

    for rule in rules["rules"]:
        if rule["id"] in ignore_rules or not _applies(rule, profile, slot):
            continue
        rtype = rule["type"]
        if rtype == "regex":
            found = []
            for match in rule["regex"].finditer(scan):
                if match.end() == match.start():
                    continue
                if _suppressed(rule, scan, match):
                    continue
                found.append(match)
            if len(found) < rule.get("min_hits", 1):
                continue
            for match in found:
                hit = _make_hit(rule, scan, match.start(), match.end())
                hit["_start"], hit["_end"] = match.start(), match.end()
                raw_hits.append(hit)
        elif rtype == "caps":
            for start, end in _caps_hits(rule, scan, rules["caps_allowlist"]):
                hit = _make_hit(rule, scan, start, end)
                hit["_start"], hit["_end"] = start, end
                raw_hits.append(hit)
        elif rtype == "metric":
            func = METRICS.get(rule.get("metric"))
            if func is None:
                continue
            detail = func(ctx, rule.get("params", {}))
            if detail:
                hit = _make_hit(rule, text, 0, 0, detail=detail)
                hit["line"], hit["col"], hit["match"] = 1, 1, ""
                hit["_start"] = hit["_end"] = -1
                raw_hits.append(hit)
        elif rtype == "slot_limit":
            params = rule.get("params", {})
            over = []
            if "limits_by_line" in params and slot == "meta_image_line":
                lines = [ln.strip() for ln in text.strip().split("\n") if ln.strip()]
                limits = params["limits_by_line"]
                for index, line in enumerate(lines):
                    if index >= len(limits):
                        over.append("line %d: a fourth line is not allowed, three lines only" % (index + 1))
                    elif len(line) > limits[index]:
                        over.append("line %d has %d characters, budget %d" % (index + 1, len(line), limits[index]))
            else:
                limit = limit_override if limit_override else params.get("limit")
                if limit is not None and chars is not None and chars > limit:
                    over.append("%d characters, budget %d (%d over)" % (chars, limit, chars - limit))
            for detail in over:
                hit = _make_hit(rule, text, 0, 0, detail=detail)
                hit["line"], hit["col"], hit["match"] = 1, 1, ""
                hit["_start"] = hit["_end"] = -1
                raw_hits.append(hit)
        elif rtype == "builtin":
            name = rule.get("builtin")
            if name in ("unclosed_ignore", "stray_ignore_end", "nested_ignore"):
                wanted = {"unclosed_ignore": "unclosed", "stray_ignore_end": "stray_end",
                          "nested_ignore": "nested"}[name]
                for kind, line in problems:
                    if kind == wanted:
                        hit = _make_hit(rule, text, 0, 0, detail="line %d" % line)
                        hit["line"], hit["col"], hit["match"] = line, 1, ""
                        hit["_start"] = hit["_end"] = -1
                        raw_hits.append(hit)
            elif name == "url_in_post":
                for match in URL_RE.finditer(text):
                    hit = _make_hit(rule, text, match.start(), match.end())
                    hit["_start"], hit["_end"] = match.start(), match.end()
                    raw_hits.append(hit)

    positioned = [h for h in raw_hits if h["_start"] >= 0]
    unpositioned = [h for h in raw_hits if h["_start"] < 0]
    hits = (_dedupe(positioned) if dedupe else positioned) + unpositioned
    hits.sort(key=lambda h: (h["line"], h["col"], h["id"]))
    for hit in hits:
        hit.pop("_start", None)
        hit.pop("_end", None)

    score, breakdown = compute_score(hits, n_words)
    counts = {s: sum(1 for h in hits if h["severity"] == s) for s in SEVERITIES}
    if counts["block"]:
        verdict = "BLOCK"
    elif counts["warn"]:
        verdict = "REVISE"
    else:
        verdict = "PASS"
    by_category = {}
    for hit in hits:
        by_category[hit["category"]] = by_category.get(hit["category"], 0) + 1
    return {
        "tool": "adquill slop_lint",
        "version": VERSION,
        "disclaimer": DISCLAIMER,
        "profile": profile,
        "slot": slot_info,
        "score": score,
        "verdict": verdict,
        "counts": counts,
        "by_category": by_category,
        "stats": {"words": n_words, "sentences": len(sentences), "characters": len(raw_text.strip())},
        "open_verify": len(re.findall(r"\[VERIFY", text)),
        "ignored_rules": sorted(ignore_rules),
        "warnings": warnings,
        "breakdown": breakdown,
        "hits": hits,
    }


def compute_score(hits, n_words):
    """Score 0 to 100, 100 is clean.

    Each rule deducts its weight for the first hit and half its weight for every further
    hit, capped at 2.5 times the weight. Texts over 150 words are scored by density (the
    deduction is scaled by 150 / words). Any block-tier hit caps the score at 59.
    """
    per_rule = {}
    for hit in hits:
        per_rule.setdefault(hit["id"], []).append(hit)
    breakdown = []
    total = 0.0
    scale = 1.0 if n_words <= 150 else 150.0 / n_words
    for rid in sorted(per_rule):
        group = per_rule[rid]
        weight = group[0]["weight"]
        raw = weight * (1 + 0.5 * (len(group) - 1))
        raw = min(raw, weight * 2.5)
        deduction = raw * scale
        total += deduction
        breakdown.append({
            "id": rid, "severity": group[0]["severity"], "hits": len(group),
            "deduction": round(deduction, 1),
        })
    score = int(round(max(0.0, 100.0 - total)))
    if any(h["severity"] == "block" for h in hits):
        score = min(score, 59)
    return score, breakdown


# ---------------------------------------------------------------------------
# Rule self-test (used by --selftest and by the unit tests)
# ---------------------------------------------------------------------------

def selftest(rules):
    """Check each rule's examples. Returns a list of failure strings."""
    failures = []
    for rule in rules["rules"]:
        profiles = rule["profiles"]
        profile = "ad" if "ad" in profiles else profiles[0]
        slots = rule.get("slots")
        slot = slots[0] if slots else None
        for example in rule.get("examples_bad", []):
            res = lint_text(example, rules, profile=profile, slot=rule.get("example_slot", slot), dedupe=False)
            if rule["id"] not in {h["id"] for h in res["hits"]}:
                failures.append("%s did not fire on its bad example: %r" % (rule["id"], example))
        for example in rule.get("examples_ok", []):
            res = lint_text(example, rules, profile=profile, slot=rule.get("example_slot", slot), dedupe=False)
            if rule["id"] in {h["id"] for h in res["hits"]}:
                failures.append("%s fired on its ok example: %r" % (rule["id"], example))
    return failures


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def format_text(result, explain=False, threshold=80):
    lines = []
    head = "adquill slop_lint %s | profile %s" % (VERSION, result["profile"])
    slot = result["slot"]
    if slot:
        limit = slot.get("limit")
        head += " | slot %s: %d characters" % (slot["name"], slot["chars"])
        if limit:
            head += " of %d" % limit
    lines.append(head)
    counts = result["counts"]
    lines.append("Score %d/100  Verdict %s  (block %d, warn %d, note %d)  Pass mark %d" % (
        result["score"], result["verdict"], counts["block"], counts["warn"], counts["note"], threshold))
    if result["open_verify"]:
        lines.append("Open [VERIFY] tokens: %d. Status: draft, not ready to publish." % result["open_verify"])
    for warning in result["warnings"]:
        lines.append("Warning: " + warning)
    if not result["hits"]:
        lines.append("No hits.")
    for hit in result["hits"]:
        where = "%d:%d" % (hit["line"], hit["col"])
        shown = ' "%s"' % hit["match"] if hit["match"] else ""
        lines.append("")
        lines.append("%-5s %-8s %-6s%s" % (hit["severity"].upper(), hit["id"], where, shown))
        lines.append("      " + hit["message"])
        if explain:
            lines.append("      Fix: " + hit["suggestion"])
            if hit.get("example"):
                lines.append("      Example: %s  ->  %s" % (hit["example"]["before"], hit["example"]["after"]))
            lines.append("      Category: %s, weight %s" % (hit["category"], hit["weight"]))
    if explain and result["breakdown"]:
        lines.append("")
        lines.append("Score breakdown (100 minus deductions, block-tier hits cap the score at 59):")
        for row in sorted(result["breakdown"], key=lambda r: -r["deduction"]):
            lines.append("  %-8s %-5s hits %d  deduction %.1f" % (
                row["id"], row["severity"], row["hits"], row["deduction"]))
    if explain:
        lines.append("")
        lines.append(DISCLAIMER)
    return "\n".join(lines)


def format_rules_table(rules):
    rows = ["%-8s %-5s %-4s %-15s %s" % ("id", "tier", "wt", "category", "message")]
    for rule in rules["rules"]:
        rows.append("%-8s %-5s %-4s %-15s %s" % (
            rule["id"], rule["severity"], rule["weight"], rule["category"], rule["message"][:70]))
    rows.append("")
    rows.append("%d rules, rules file version %s" % (len(rules["rules"]), rules["version"]))
    return "\n".join(rows)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser(slot_names):
    parser = argparse.ArgumentParser(
        prog="slop_lint.py",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=(
            "adquill slop_lint: score ad copy from 0 to 100 (100 is clean) for stock-phrase "
            "patterns, risky claims and slot overruns.\n\n"
            "IMPORTANT: this tool flags patterns. It does not detect AI authorship, it cannot "
            "tell who or what wrote a text, and it makes no claim about AI detectors. Humans "
            "write these patterns too. A clean score does not make copy good or true."
        ),
        epilog=(
            "Input: a file path, a literal text argument, --text, or stdin (use - for stdin).\n"
            "Profiles: ad (default for text, stdin, slots and .txt files) applies every rule.\n"
            "  doc (default for .md files) skips the ad formatting rules and ignores code blocks.\n"
            "  code (default for .py and .json files) checks house style characters only.\n"
            "Ignore blocks: wrap text in <!-- adquill-lint: ignore-start --> and\n"
            "  <!-- adquill-lint: ignore-end --> to skip it. One line: <!-- adquill-lint: ignore-line -->.\n"
            "Score: each rule deducts its weight for the first hit and half for each further hit.\n"
            "  Texts over 150 words are scored by density. A block-tier hit caps the score at 59.\n"
            "Verdict: BLOCK if any block-tier hit, REVISE if any warn-tier hit, else PASS.\n"
            "Exit codes: 0 score at or above --fail-under (default 80), 1 score below it,\n"
            "  2 bad usage or unreadable input, 3 invalid rules file.\n"
            "Rules live in rules.json beside this script. Add a rule there, with examples,\n"
            "  then run --selftest."
        ),
    )
    parser.add_argument("input", nargs="?", help="file path, or literal text, or - for stdin")
    parser.add_argument("--text", help="lint this literal text")
    parser.add_argument("--slot", choices=slot_names, help="check a character budget and apply slot rules")
    parser.add_argument("--profile", choices=("auto",) + PROFILES, default="auto",
                        help="rule set to apply (default auto, see below)")
    parser.add_argument("--json", action="store_true", help="print the result as JSON")
    parser.add_argument("--fail-under", type=int, default=80, metavar="N",
                        help="exit 1 when the score is below N (default 80)")
    parser.add_argument("--explain", action="store_true", help="show the fix and the score breakdown for each hit")
    parser.add_argument("--rules", default=DEFAULT_RULES, help="path to a rules file (default rules.json beside this script)")
    parser.add_argument("--allow", action="append", default=[], metavar="PHRASE",
                        help="treat this phrase as fine, for example a proper noun (repeatable)")
    parser.add_argument("--ignore-rule", action="append", default=[], metavar="ID",
                        help="switch off a rule by id. The result lists it, so the choice is visible (repeatable)")
    parser.add_argument("--skip-quotes", action="store_true",
                        help="do not lint text inside double quotes (for verbatim guest quotes)")
    parser.add_argument("--limit", type=int, metavar="N", help="override the slot character budget")
    parser.add_argument("--list-rules", action="store_true", help="print the rule table and exit")
    parser.add_argument("--selftest", action="store_true",
                        help="check every rule against its own examples and exit")
    parser.add_argument("--version", action="version", version="slop_lint " + VERSION)
    return parser


def _read_input(args):
    """Return (text, source_path, from_text_or_stdin). Raises ValueError with a message."""
    if args.text is not None:
        return args.text, None, True
    value = args.input
    if value is None or value == "-":
        if value is None and sys.stdin.isatty():
            raise ValueError("no input. Pass a file, text, --text, or pipe text on stdin.")
        return sys.stdin.read(), None, True
    if os.path.isdir(value):
        raise ValueError("%s is a directory, pass a file" % value)
    if os.path.isfile(value):
        if os.path.getsize(value) > MAX_INPUT_BYTES:
            raise ValueError("%s is larger than %d bytes" % (value, MAX_INPUT_BYTES))
        with open(value, "r", encoding="utf-8", errors="replace") as handle:
            return handle.read(), value, False
    return value, None, True


def main(argv=None):
    if sys.version_info < (3, 9):
        sys.stderr.write("slop_lint needs Python 3.9 or newer\n")
        return EXIT_USAGE
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass
    pre = argparse.ArgumentParser(add_help=False)
    pre.add_argument("--rules", default=DEFAULT_RULES)
    known, _ = pre.parse_known_args(argv)
    try:
        rules = load_rules(known.rules)
    except RulesError as exc:
        sys.stderr.write("rules error: %s\n" % exc)
        return EXIT_RULES
    parser = build_parser(sorted(rules["slots"]))
    args = parser.parse_args(argv)

    if args.list_rules:
        print(format_rules_table(rules))
        return EXIT_OK
    if args.selftest:
        failures = selftest(rules)
        for failure in failures:
            print("FAIL " + failure)
        print("%d rules checked, %d failures" % (len(rules["rules"]), len(failures)))
        return EXIT_RULES if failures else EXIT_OK

    try:
        text, source_path, from_text = _read_input(args)
    except (ValueError, OSError) as exc:
        sys.stderr.write("input error: %s\n" % exc)
        return EXIT_USAGE
    if not text.strip():
        sys.stderr.write("input error: the text is empty\n")
        return EXIT_USAGE
    profile = args.profile
    if profile == "auto":
        profile = "ad" if args.slot else detect_profile(source_path, from_text)
    if args.slot and profile != "ad":
        profile = "ad"
    unknown = [r for r in args.ignore_rule if r not in {x["id"] for x in rules["rules"]}]
    if unknown:
        sys.stderr.write("input error: unknown rule id %s\n" % ", ".join(unknown))
        return EXIT_USAGE

    result = lint_text(text, rules, profile=profile, slot=args.slot, extra_allow=args.allow,
                       skip_quotes=args.skip_quotes, ignore_rules=args.ignore_rule,
                       limit_override=args.limit)
    result["threshold"] = args.fail_under
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    else:
        print(format_text(result, explain=args.explain, threshold=args.fail_under))
    return EXIT_BELOW_THRESHOLD if result["score"] < args.fail_under else EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
