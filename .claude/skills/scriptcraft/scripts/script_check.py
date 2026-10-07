#!/usr/bin/env python3
"""scriptcraft validator.

Checks a voiceover video script (the markdown format in ../SKILL.md) against
the limits in tiers.json and the claims rules in brand_rules.json.

    python3 -I script_check.py FILE [--tier short|long] [--json] [--final]
        [--strict] [--tiers PATH] [--brand PATH] [--explain RULE_ID]

Exit codes: 0 pass, 1 fail, 2 parse error.
Standard library only, no network, deterministic. Every length or density
limit is read from tiers.json; only the contract tolerances below live here.
To add a rule: write a check_* function that calls ctx.add(), describe the
id in RULES and HELP and append the function to CHECKS.

Styles. The optional front matter field 'style' is voiceover, ugc_talk or
ugc_text (default voiceover; ugc_text is short tier only). Optional fields
'creator', 'relationship' and 'sound' have defaults in tiers.json
styles.fields. A style's tier overrides (styles.<style>.<tier>) replace tier
values for that style. STYLE_ONLY lists the rules that run in some styles
only; the report prints [SKIP] for a rule the style does not check. A
voiceover script that sets none of the new fields gets the 0.2.0 report.
Every ugc word list and number lives in tiers.json styles.
"""

import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EM_DASH, EN_DASH = chr(0x2014), chr(0x2013)

# Tolerances fixed by the validator contract (they are not tier limits).
BEAT_OVER_BLOCK = 1.25    # T04 and H01: estimate over the declared seconds
BEAT_OVER_WARN = 1.10     # T04
OVERLAY_REPEAT_MAX = 0.6  # O03
CAPTION_HASHTAGS_MAX = 2  # C05
HOLD_INFO_SECONDS = 3     # info line: declared time this far above the estimate is a silent hold
MIN_SECONDS = 8           # lowest 'seconds:' value unless the style tier sets min_seconds
PLACEHOLDER_WORDS = " tbd "  # a [VERIFY] or [TODO] note counts as one spoken word

# Spelled two to nineteen count toward density only; "one" never counts.
# Twenty and up are claims: they count toward density and need a facts row (F04).
SPELLED_SMALL = {"two", "three", "four", "five", "six", "seven", "eight", "nine",
                 "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
                 "sixteen", "seventeen", "eighteen", "nineteen"}
UNITS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
        "eighty": 80, "ninety": 90}
BIG = dict(TENS, dozen=12, hundred=100, thousand=1000, million=1000000)
SPELLED_BIG_RE = re.compile(r"\b(%s)(?:[- ](%s))?\b|\b(dozen|hundred|thousand|million)\b"
                            % ("|".join(TENS), "|".join(UNITS)), re.I)
H02_BANNED = re.compile(r"\b(logo|title card|intro(duction)?|fade[ -]in|black screen|"
                        r"talking[ -]head|greeting|waves? hello|says? hi)\b", re.I)
H02_MOTION = re.compile(r"\b(person|people|skier|guide|hands|pov|drop|skis|walk|hike|"
                        r"hiking|pan|drone|glide|gliding|snow|boots)", re.I)
ONE_TAKE_RE = re.compile(r"^one take:", re.I)
TAKE_MOTION = re.compile(r"\b(pov|drone|pan|push|pull|track|tracking|follow|follows|orbit|tilt|walk|walks|"
                         r"step|steps|climb|climbs|ski|skis|glide|glides|slide|slides|rise|rises|drop|drops|"
                         r"hike|hikes|run|runs|turn|turns|selfie|handheld|hand held|swing|swings|pans|tilts|"
                         r"walking|climbing|skiing|gliding)\b", re.I)  # a handheld or selfie take is never static

# Hyphens split words, so "a-b-c" is three words. Digits keep their separators.
WORD_RE = re.compile(r"\d+(?:[.,:]\d+)+|[A-Za-z0-9\u00c0-\u024f]+(?:['\u2019][A-Za-z0-9\u00c0-\u024f]+)*")
NUM_RE = re.compile(r"\d+(?:[.,:]\d+)*")
SPACED_THOUSANDS = re.compile(r"(?<![\d.,])\d{1,3}(?:[ \u00a0]\d{3})+(?!\d)")
PAUSE_RE = re.compile(r"\[\s*PAUSE\s+(\d+(?:\.\d+)?)\s*s?\s*\]", re.I)
BRACKET_RE = re.compile(r"\[[^\]]*\]")
TIME_RE = re.compile(r"^(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)$")
LOOP_RE = re.compile(r"^(open|close):([a-z])$", re.I)
CHAPTER_RE = re.compile(r"^(ch|mini):(\d+)$", re.I)
SEP_RE = re.compile(r"^:?-+:?$")
EMOJI_RE = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27bf\u2b00-\u2bff\ufe0f\u200d]")

# F04 claim matching: the word after a number names what it counts ("10 minutes",
# "10 guides"). These words do not, so the next word is tried instead.
UNIT_SKIP = {"a", "an", "the", "and", "or", "but", "to", "in", "into", "on", "at", "of", "for", "from", "per",
             "by", "with", "about", "around", "over", "under", "up", "down", "out", "off", "than", "more",
             "less", "is", "are", "was", "were", "be", "it", "its", "this", "that", "these", "those", "you",
             "your", "we", "our", "i", "my", "they", "their", "he", "she", "his", "her", "so", "then", "just",
             "only", "each", "every", "plus", "if", "when", "as", "all"}
UNIT_ALIASES = {"m": "metre", "meter": "metre", "km": "kilometre", "kilometer": "kilometre", "min": "minute",
                "mins": "minute", "hr": "hour", "hrs": "hour", "h": "hour", "kr": "nok", "kroner": "nok", "pct": "percent",
                "cent": "percent"}
UNIT_LOOKAHEAD_BEAT = 2   # words after a number in the script searched for its unit
UNIT_LOOKAHEAD_ROW = 3    # words after the same number in the facts row that may hold that unit
UNIT_LOOKBEHIND_ROW = 3   # words before it in the row that may hold the unit ("day tours from NOK 1,950")
CURRENCY_UNITS = {"nok", "eur", "euro", "usd", "dollar", "gbp", "pound"}  # NOK is stripped from rows, so a currency is no unit

# Rules that run in some styles only; the others print [SKIP].
UGC = ("ugc_talk", "ugc_text")
STYLE_ONLY = {"H02": ("voiceover",), "H03": ("voiceover",), "U01": UGC, "U02": UGC, "U03": ("ugc_talk",),
              "U04": UGC, "U05": UGC, "U06": ("ugc_talk",), "U07": UGC}
STYLE_SKIP_NOTE = {"H02": "see U01", "H03": "see U03"}
# Rules added in 0.3.0. A voiceover script with no new front matter field does not list them.
NEW_RULES = ("U01", "U02", "U03", "U04", "U05", "U06", "U07", "D01", "SND01")
NEW_FIELDS = ("creator", "relationship", "sound")

RULES = {
    "T01": "estimated total speaking time at or under the maximum",
    "T02": "estimated total under the warning line",
    "T03": "beat times contiguous from 0 and inside the maximum",
    "T04": "each beat can be spoken in its declared time",
    "W01": "total words at or under the hard maximum",
    "W02": "total words inside the target range",
    "W03": "words per beat inside the limits",
    "B01": "beat count inside the limits",
    "B02": "seconds per beat inside the range",
    "H01": "hook length and timing (long: promise timing)",
    "H02": "first shot shows motion or a person, not a logo or greeting",
    "H03": "hook window addresses the viewer (you, your)",
    "F01": "facts and numbers per beat",
    "F02": "facts per script",
    "F03": "numbers per script",
    "F04": "every number is in a verified facts row the beat cites, counting the same thing",
    "F05": "every referenced fact id exists",
    "F06": "every facts row has a source and verified yes or no",
    "F07": "every proper noun appears in the facts table",
    "S01": "sentence length",
    "V01": "seconds per shot",
    "V02": "every beat has a visual",
    "V03": "a cut or shift inside every pattern interrupt window (long)",
    "O01": "overlay words, characters and lines",
    "O02": "overlay readable in its time",
    "O03": "overlay does not repeat the voiceover",
    "O04": "first beat has an overlay for sound-off viewers",
    "C01": "call to action count",
    "C02": "call to action starts near the end",
    "C03": "call to action length",
    "C04": "call to action comes after the payoff",
    "C05": "caption hashtags",
    "L01": "loop and chapter structure",
    "R01": "no em dash, en dash or emoji",
    "R02": "no capitals for emphasis",
    "R03": "speaks to you more than about the company",
    "U01": "first beat shows a person, selfie, POV, handheld shot or hands in action",
    "U02": "no end card, logo, title card, stock footage, animation, slide or lower third in any visual",
    "U03": "hook addresses the viewer (you, your) or opens on a first-person stake (I, my, we)",
    "U04": "overlay text uses no capital letters for emphasis",
    "U05": "call to action is a soft prompt, not only a link",
    "U06": "casual markers and contractions per 100 words",
    "U07": "every visual names who or what is on camera",
    "D01": "disclosure: Ad label and an early disclosure beat when the relationship needs one",
    "SND01": "no trending song when the script names the brand, a trip or a price",
}
# --explain: what each rule counts, and the usual fix.
HELP = {
    "T01": ("Sum of beat estimates: words / (wps x narrator pace) + penalty per spoken digit number + [PAUSE n].",
            "Cut words. Spoken digits cost extra time, so cut numbers first."),
    "T02": ("The same estimate against the warning line.", "Cut a sentence or accept the warning."),
    "T03": ("Declared start-end times: contiguous, from 0, ending inside the maximum (or the seconds field), and at "
            "or after min_seconds when the style tier sets one (ugc_text: 7 s).",
            "Make each beat start where the last one ended."),
    "T04": ("Per beat: estimated speaking time against declared time. Over 10 percent warns, over 25 percent blocks.",
            "Cut words in that beat or give it more seconds from a quieter beat."),
    "W01": ("Spoken words, hyphenated parts counted separately, [PAUSE] excluded, a placeholder counts as 1 word.",
            "Cut words. Budget scales with narrator word_scale and seconds / max_seconds, unless the style tier sets "
            "words.scale_with_seconds false (ugc_text: 12 spoken words at any length)."),
    "W02": ("Same count against the target range.", "Add or cut a line; do not pad with filler."),
    "W03": ("Words per beat. Hook, cta and disclosure beats are exempt from the target range, not from the hard max.",
            "Move a sentence to a neighbouring beat or cut it."),
    "B01": ("Rows in the Script table.", "Merge or split beats."),
    "B02": ("Declared seconds per beat.", "Re-time beats inside the range."),
    "H01": ("Short: beat 1 end time and words. Long: words before verbal_by_seconds, and the promise beat timing and "
            "words. ugc_talk short: beat 1 may end at max_seconds_with_overlay (4 s) when it has an overlay; the first "
            "word must come by first_word_by_seconds (a leading [PAUSE n] counts, an empty beat 1 blocks); the first "
            "sentence of the voiceover over first_sentence_max_words blocks, under first_sentence_min_words warns.",
            "Cut the hook to one question. With narrator slow, keep a short hook to 6 words."),
    "H02": ("Voiceover style only (ugc styles use U01). Beat 1 visual cell text: banned openers block; no motion or "
            "person word warns.", "Open on a moving subject: skis, a guide, hands, boots, a drone move."),
    "H03": ("Voiceover style only (ugc_talk uses U03). you, your and similar words in voiceover and overlay inside "
            "the hook window.", "Put the guest in the first line."),
    "F01": ("Per beat: cited fact ids, plus digit numbers and names not covered by a cited row. Long also counts numbers: "
            "digits, spelled two and up (one never counts), a full date is 2 or 3 numbers.",
            "Move one fact to another beat, the caption or the description."),
    "F02": ("Distinct facts across all beats. Facts rows that no beat cites do not count.", "Cut facts the takeaway does not need."),
    "F03": ("Distinct numbers across all beats: digits and spelled numbers from two up, voiceover and overlay.",
            "Say one number per idea. Put dates and prices in the caption."),
    "F04": ("Every digit and every spelled number from twenty up, in voiceover, overlay and caption, must be in a "
            "verified facts row. In a beat it must be in a row that beat declares in its facts column, counting the "
            "same thing: one of the words in the 2 words after the number that names a unit (10 minutes, 10 guides, "
            "400 vertical metres; small words such as of, per, the and currencies are skipped, plurals and m, km, "
            "min, h are matched) must be one of the 3 words before or after that number in the row. A row number "
            "that ends its clause (lunch at 12:30) matches any unit. A number in no row blocks. A number reused for "
            "a claim no row makes (beat says 10 guides, rows only say 10 minutes) blocks. A number whose claim is "
            "only in a row the beat does not declare, or only in an unverified row, warns in a draft and blocks "
            "with --final. Commas, spaces and NOK are ignored; % is read as percent.",
            "Cite the row that says this exact claim in the beat's facts column, add a sourced row for the new "
            "claim, or cut the number."),
    "F05": ("Ids in the facts column against the facts table.", "Fix the id or add the row."),
    "F06": ("Facts rows: a source and verified yes or no.", "Name the file, page or person, and set verified."),
    "F07": ("Capitalized words not at a sentence start (plus known place names anywhere), not found in the facts table.",
            "Add a sourced row for the name or cut it. The full brand name is exempt."),
    "S01": ("Words per sentence across the voiceover. Hard max blocks; the average warns.",
            "Split long sentences. A deliberate fragment pair may keep the average warning."),
    "V01": ("Beat seconds divided by shots. A short single shot over the static maximum blocks unless it is a "
            "'one take:' shot that names a camera or subject move.", "Add a shot, or mark a real continuous take as 'one take:'."),
    "V02": ("An empty visual cell.", "Name a subject and an action."),
    "V03": ("Long: windows with no beat of 2 or more shots and no shift or reengage role.", "Add a cut or a reengage beat."),
    "O01": ("Overlay words, characters per line and lines per beat. With overlay.persistent (ugc_text) also the "
            "distinct lines across the script: over script_max_lines or script_max_words blocks, under "
            "script_min_words warns.", "Cut the overlay to keywords."),
    "O02": ("Overlay characters per second of the beat, and the beat's minimum seconds. With overlay.persistent "
            "(ugc_text) the distinct lines over the time from their first beat to the end.",
            "Shorten the overlay or lengthen the beat."),
    "O03": ("Share of the beat's voiceover words repeated in its overlay.", "Make the overlay add a keyword the voice does not say."),
    "O04": ("Beat 1 overlay cell. Warns; blocks when the style tier sets overlay.required_in_first_beat (ugc_text).",
            "Give muted viewers the question on screen."),
    "C01": ("cta beats (hard_max), cta plus soft-cta beats (max), soft-cta beats (soft_mid_max); and a booking or "
            "link ask in a beat without a cta role (warn).", "Keep one primary ask. Move asks out of story beats."),
    "C02": ("cta start against the declared end of the script minus last_seconds. Long: a soft-cta must start after "
            "promise_by_seconds and after the first mini beat.", "Move the ask later."),
    "C03": ("Spoken words in the cta beat; more than one ask verb in it warns.", "One verb, one destination."),
    "C04": ("cta beat position against the payoff or close of the dominant loop.", "Pay off first, then ask."),
    "C05": ("Hashtags in the caption.", "Keep 2 at most."),
    "L01": ("Role column loop and chapter tokens. ugc_text (loops.close_in_last_beat): close:A in the last beat.",
            "Short: open:A in beat 1, close:A in one of the last 2 beats (ugc_text: the last beat; one beat may "
            "hold both). Long: see references/long-form.md."),
    "R01": ("Em dash, en dash or emoji in any cell or the caption.", "Use a comma, colon or full stop."),
    "R02": ("Words of 3 or more capitals not in the acronym allowlist, in voiceover and overlay. In the ugc styles "
            "the voiceover only, because U04 checks overlays.", "Use sentence case."),
    "R03": ("Company words (brand_rules.json guest_subject.company_words: we, our, us, the brand) against you words. "
            "In the ugc styles the you side also counts styles.ugc_rules.first_person_words (I, I'm, my, me): a "
            "creator speaking for themselves is not company-speak.", "Make the guest or the creator the subject."),
    "U01": ("Styles ugc_talk and ugc_text, block. Beat 1 visual cell: blocks when it names none of "
            "styles.ugc_rules.first_frame_person_cues (a person, selfie, POV, handheld, hands), or when it opens on "
            "one of first_frame_banned (intro, fade in, black screen, a wave hello). A product or landscape shot "
            "alone blocks. Voiceover keeps the H02 warning.",
            "Open on the creator or a guest mid-action: 'selfie: guide on the skin track', 'POV: skis on skins'."),
    "U02": ("Styles ugc_talk and ugc_text, block. Every visual cell, against styles.ugc_rules.visual_disallowed "
            "(end card, logo, title card, stock footage, animation, slideshow, lower third) and "
            "visual_disallowed_regex (slide as a noun, stock drone footage, animated map, closing card, price graphic). "
            "The verb 'slide' is allowed (skis slide uphill), and so is an animated guest.",
            "Shoot it on the phone. Put the brand in the caption or the creator's own disclosure line."),
    "U03": ("Style ugc_talk, warn. Voiceover and overlay of the beats that start inside the hook window (short: "
            "hook.max_seconds, or max_seconds_with_overlay when beat 1 has an overlay; long: verbal_by_seconds): "
            "warns when they hold no you word and no styles.ugc_rules.hook_first_person_stakes word (I, I'm, my, we).",
            "Address the viewer ('your skis') or open on your own stake ('I make every guest...')."),
    "U04": ("Styles ugc_talk and ugc_text, warn. Overlay cells: words of styles.ugc_rules.overlay_caps_min_letters or "
            "more capitals that are not in the acronym allowlist.", "Write native text in sentence case or lower case."),
    "U05": ("Styles ugc_talk and ugc_text, warn. Each cta beat's voiceover and overlay: warns when they hold no "
            "styles.ugc_rules.cta_soft_prompts phrase (save this, send this to, which one, follow along, one "
            "logistics line on how to book, or any line matching cta_soft_regex such as dates are in the caption), with "
            "its own message when the only ask is a cta_link_only phrase such as link in bio or comment for the link. "
            "A link_only phrase in a beat without the cta role also warns when no cta beat holds a soft prompt.",
            "Ask a soft prompt and put the booking link in the caption."),
    "U06": ("Style ugc_talk, warn. Per 100 spoken words: casual markers (styles.ugc_rules.casual_markers plus 'like' "
            "as filler) above the tier's casual.markers_max_per_100_words warn; contractions (contraction_suffixes, "
            "contraction_s_words) below casual.contractions_min_per_100_words warn.",
            "Keep the one marker that sounds like the creator and cut the rest. Say it the way you talk: you're, "
            "it's, don't."),
    "U07": ("Styles ugc_talk and ugc_text, warn. Words in each visual cell against styles.ugc_rules.visual_min_words.",
            "Name who or what is on camera and what they do: 'guide zips a shell at the top'."),
    "D01": ("Front matter relationship, rules in styles.disclosure. guest_paid or guest_gifted: the caption must start "
            "with an ad label: Ad, #ad, Advert, Advertisement, Reklame or Annonse (caption_label_regex), and a beat that "
            "starts inside within_seconds with the role token disclosure must say so in its voiceover or overlay "
            "(paid_words; a paid word right after a negation, as in 'not an ad', does not count); each missing part blocks. staff or "
            "guide: a disclosure beat inside within_seconds whose voiceover or overlay names the role (role_words or "
            "the brand name), else warn. guest_unpaid: no requirement. Runs in the ugc styles; in voiceover only "
            "when relationship is written in the front matter.",
            "Start the caption with 'Ad'. Add a beat in the first 5 s with the disclosure role: 'I guide for "
            "Outdoor Norway' or 'Ad: Outdoor Norway paid for my trip'."),
    "SND01": ("Front matter sound, rules in styles.sound. sound: trending blocks when the voiceover, overlay or "
              "caption names the brand (brand_rules.json brand), a trip (trip_words) or a price (price_regex). "
              "Other sound values pass.",
              "Use a Commercial Music Library track (sound: commercial_library) or original sound."),
}
LIMIT_KEYS = {
    "T01": ["max_seconds"], "T02": ["warn_seconds"], "T03": ["max_seconds"], "O04": ["overlay"],
    "T04": ["wps", "number_penalty_seconds"], "W01": ["words"], "W02": ["words"],
    "W03": ["words_per_beat"], "B01": ["beats"], "B02": ["seconds_per_beat"],
    "H01": ["hook"], "F01": ["facts"], "F02": ["facts"], "F03": ["facts"],
    "S01": ["sentence"], "V01": ["visual"], "V03": ["visual"], "O01": ["overlay"],
    "O02": ["overlay"], "C01": ["cta"], "C02": ["cta"], "C03": ["cta"],
    "L01": ["loops", "chapters"],
}
# --explain: the tiers.json styles keys each new rule reads, as (section, key).
STYLE_KEYS = {
    "U01": [("ugc_rules", "first_frame_person_cues"), ("ugc_rules", "first_frame_banned")],
    "U02": [("ugc_rules", "visual_disallowed"), ("ugc_rules", "visual_disallowed_regex")],
    "U03": [("ugc_rules", "hook_first_person_stakes")], "U04": [("ugc_rules", "overlay_caps_min_letters")],
    "U05": [("ugc_rules", "cta_soft_prompts"), ("ugc_rules", "cta_soft_regex"), ("ugc_rules", "cta_link_only")],
    "U06": [("ugc_rules", "casual_markers"), ("ugc_rules", "casual_filler_like_regex"),
            ("ugc_rules", "contraction_suffixes"), ("ugc_rules", "contraction_s_words")],
    "U07": [("ugc_rules", "visual_min_words")], "R03": [("ugc_rules", "first_person_words")],
    "D01": [("disclosure", k) for k in ("within_seconds", "role_token", "ad_label_required", "role_line_expected",
                                        "caption_label_regex", "paid_words", "paid_negation_regex",
                                        "role_words")],
    "SND01": [("sound", k) for k in ("blocked_value", "trip_words", "price_regex")],
}
# --explain: style tier keys each rule reads (besides LIMIT_KEYS).
STYLE_LIMIT_KEYS = {"U06": ["casual"], "T03": ["min_seconds"]}


class ParseError(Exception):
    def __init__(self, line, msg):
        super().__init__("line %s: %s" % (line, msg))
        self.line, self.msg = line, msg


class Fact:
    def __init__(self, line, cells):
        self.line = line
        self.id = cells["id"]
        self.text = cells["fact"]
        self.source = cells["source"]
        self.verified = cells["verified"].strip().lower()
        self.low = norm(self.text)
        no_nok = re.sub(r"(?i)nok", " ", self.text)
        self.nums = {num_norm(n) for n in NUM_RE.findall(no_nok)}
        self.squeezed = re.sub(r"[,\s]", "", no_nok)
        # number -> the words that follow it, and the unit stems near it (before and after), for F04 claim matching
        self.after, self.near = {}, {}
        for n, follow, before in numbers_with_followers(self.text, UNIT_LOOKAHEAD_ROW, UNIT_LOOKBEHIND_ROW):
            self.after.setdefault(n, []).append(follow)
            self.near.setdefault(n, set()).update(unit_stem(w) for w in follow + before)

    def has_number(self, n):
        """n is a digit string or a spelled number such as 'ninety'."""
        if not n[0].isdigit():
            return self.has_phrase(n) or self.has_number(str(spelled_value(n)))
        return n in self.nums or re.search(r"(?<![\d.])%s(?!\d)" % re.escape(n), self.squeezed)

    def says(self, n, units):
        """True when this row has number n counting the same thing. units is the set of unit stems the
        script puts after the number, or None when the number names no unit."""
        if not self.has_number(n):
            return False
        if not units:
            return True
        keys = [n] if n[0].isdigit() else [n, str(spelled_value(n))]
        follows = [f for k in keys for f in self.after.get(k, [])]
        if not follows or any(not f for f in follows):
            return True  # the row number ends its clause ("lunch at 12:30"), so it names no unit to compare
        near = set().union(*[self.near.get(k, set()) for k in keys])
        return bool(set(units) & near)

    def context(self, n):
        """The row's own words for number n, for messages: '10 minutes into every'."""
        for k in ([n] if n[0].isdigit() else [n, str(spelled_value(n))]):
            if self.after.get(k):
                return " ".join([k] + self.after[k][0][:UNIT_LOOKAHEAD_BEAT])
        return n

    def has_phrase(self, phrase):
        return has_phrase(self.low, phrase)


class Beat:
    def __init__(self, line, cells, roles, start, end):
        self.line = line
        self.n = int(cells["beat"])
        self.start, self.end = start, end
        self.seconds = end - start
        self.vo = cells["voiceover"]
        self.visual = cells["visual"]
        self.text = cells["text"]
        self.roles = roles
        cell = cells["facts"].strip()
        self.facts = [] if cell in ("", "-") else [f.strip() for f in cell.split(",") if f.strip()]
        self.shots = split_list(self.visual)
        self.overlay = split_list(self.text)

    def has(self, role):
        return role in self.roles

    def label(self):
        return "beat %d" % self.n


class Doc:
    def __init__(self, meta, facts, beats, caption):
        self.meta, self.facts, self.beats, self.caption = meta, facts, beats, caption
        self.facts_by_id = {f.id: f for f in facts}


# ---------------------------------------------------------------- text helpers

def norm(text):
    return text.replace("\u2019", "'").lower()


def has_phrase(low_text, phrase):
    return re.search(r"(?<![a-z0-9])%s(?![a-z0-9])" % re.escape(phrase.lower()), low_text) is not None


def split_list(cell):
    cell = cell.strip()
    if cell in ("", "-"):
        return []
    return [p.strip() for p in re.split(r"\s+/\s+", cell) if p.strip() and p.strip() != "-"]


def num_norm(s):
    return s.replace(",", "")


def join_thousands(text):
    """NOK 1 950 is one number, as in the facts row NOK 1,950."""
    return SPACED_THOUSANDS.sub(lambda m: re.sub(r"\s", "", m.group(0)), text)


def digits(text):
    return [num_norm(x) for x in NUM_RE.findall(join_thousands(text))]


def spelled_big(text):
    """Spelled numbers from twenty up, compounds joined: 'twenty-five' -> 'twenty-five'."""
    return [m.group(0).lower().replace(" ", "-") for m in SPELLED_BIG_RE.finditer(text)]


def spelled_value(token):
    parts = token.split("-")
    return BIG[parts[0]] + (UNITS[parts[1]] if len(parts) > 1 else 0)


def unit_stem(word):
    """'minutes' -> 'minute', 'hrs' -> 'hour', 'metres' -> 'metre'; used to compare what a number counts."""
    w = word.lower().replace("’", "'")
    w = w[:-2] if w.endswith("'s") else w
    w = UNIT_ALIASES.get(w, w)
    if len(w) > 4 and w.endswith("ies"):
        w = w[:-3] + "y"
    elif len(w) > 4 and re.search(r"(ss|sh|ch|x|z)es$", w):
        w = w[:-2]
    elif len(w) > 3 and w.endswith("s") and not w.endswith("ss"):
        w = w[:-1]
    return UNIT_ALIASES.get(w, w)


def numbers_with_followers(text, lookahead, lookbehind=0):
    """(number, following words, preceding words) for each digit number and spelled number from twenty up.
    Both stop at the clause edge, so 'lunch at 12:30.' gives ('12:30', [], ['lunch', 'at'])."""
    t = join_thousands(re.sub(r"(?i)\bnok\b", " ", text)).replace("%", " percent")
    found = [(num_norm(m.group(0)), m.start(), m.end()) for m in NUM_RE.finditer(t)]
    found += [(m.group(0).lower().replace(" ", "-"), m.start(), m.end()) for m in SPELLED_BIG_RE.finditer(t)]
    out = []
    for n, start, end in found:
        clause = re.split(r"[.,;:!?/()\[\]|]", t[end:], maxsplit=1)[0]
        prior = re.split(r"[.,;:!?/()\[\]|]", t[:start])[-1]
        before = [w.lower() for w in WORD_RE.findall(prior) if not w[0].isdigit()][-lookbehind:] if lookbehind else []
        out.append((n, [w.lower() for w in WORD_RE.findall(clause)][:lookahead], before))
    return out


def number_claims(text):
    """(number, unit stems or None, words as written) for each number in a script cell:
    '10 guides watch' -> ('10', ('guide', 'watch'), '10 guides watch'). The unit stems are the words
    in the next UNIT_LOOKAHEAD_BEAT words that are not small words (UNIT_SKIP), up to the next number."""
    out = []
    for n, follow, _ in numbers_with_followers(text, UNIT_LOOKAHEAD_BEAT):
        units, last = [], -1
        for i, w in enumerate(follow):
            if w[0].isdigit():
                break
            if w not in UNIT_SKIP and unit_stem(w) not in CURRENCY_UNITS:
                units.append(unit_stem(w))
                last = i
        shown = " ".join([n] + follow[:last + 1])
        out.append((n, tuple(units) or None, shown))
    return out


def phrase_hits(text, phrases):
    """Phrases from a word list found in text as whole words; case, curly quotes and hyphens are ignored."""
    low = re.sub(r"[-‐‑]", " ", norm(text))
    low = re.sub(r"[\"“”]|(?<![a-z])'|'(?![a-z])", " ", low)
    return [p for p in phrases if has_phrase(low, re.sub(r"-", " ", p.lower()))]


def spoken(vo):
    """Voiceover as said: [PAUSE n] removed, any other [note] counted as one word."""
    return BRACKET_RE.sub(PLACEHOLDER_WORDS, PAUSE_RE.sub(" ", vo))


def words(text):
    return WORD_RE.findall(text)


def proper_nouns(text, allow, known=()):
    """Capitalized words that are not sentence-initial and not I; adjacent ones form one name.
    A sentence-initial word counts when it is in known (lowercase place names and names)."""
    names, group, prev_end = [], [], 0

    def flush():
        if group:
            names.append(" ".join(group))
            del group[:]
    for m in WORD_RE.finditer(text):
        w = m.group(0)
        before = text[:m.start()].rstrip(" \t\"'(\u201c\u2018")
        initial = not before or before[-1] in ".!?"
        is_i = w == "I" or re.match(r"^I['\u2019]", w)
        shouting = len(w) > 1 and w.isupper()  # emphasis is R02, not a name
        capital = w[0].isupper() and not is_i and not shouting and w not in allow
        if capital and (not initial or w.lower() in known):
            if group and not text[prev_end:m.start()].strip():
                group.append(w)
            else:
                flush()
                group.append(w)
        else:
            flush()
        prev_end = m.end()
    flush()
    return names


def quote(text, limit=60):
    text = " ".join(text.split())
    return text if len(text) <= limit else text[:limit - 3] + "..."


# ---------------------------------------------------------------- parsing

def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.replace("\\|", "|").strip() for c in re.split(r"(?<!\\)\|", s)]


def parse_table(rows, required, name):
    if not rows:
        return []
    head_no, head_line = rows[0]
    header = [c.lower() for c in split_row(head_line)]
    missing = [c for c in required if c not in header]
    if missing:
        raise ParseError(head_no, "%s table header is missing: %s" % (name, ", ".join(missing)))
    out = []
    for no, line in rows[1:]:
        cells = split_row(line)
        if all(SEP_RE.match(c) for c in cells):
            continue
        if len(cells) != len(header):
            raise ParseError(no, "%s row has %d cells, the header has %d (write a pipe inside a cell as \\|)"
                             % (name, len(cells), len(header)))
        out.append((no, dict(zip(header, cells))))
    return out


def parse_roles(cell, no, tier_name, cfg):
    common, long_only = set(cfg["roles"]["common"]), set(cfg["roles"]["long_only"])
    roles = []
    for tok in [t.strip() for t in cell.split(",")]:
        if tok in ("", "-"):
            continue
        loop, chap = LOOP_RE.match(tok), CHAPTER_RE.match(tok)
        if loop:
            roles.append("%s:%s" % (loop.group(1).lower(), loop.group(2).upper()))
        elif chap:
            if tier_name != "long":
                raise ParseError(no, "role %r is a long form token" % tok)
            if int(chap.group(2)) < 1:
                raise ParseError(no, "chapter numbers start at 1: %r" % tok)
            roles.append("%s:%d" % (chap.group(1).lower(), int(chap.group(2))))
        elif tok.lower() in long_only and tier_name != "long":
            raise ParseError(no, "role %r is a long form token" % tok)
        elif tok.lower() in common | long_only:
            roles.append(tok.lower())
        else:
            raise ParseError(no, "unknown role token %r" % tok)
    return roles


def parse_style(meta, meta_line, cfg, tier):
    """style, creator, relationship and sound: defaults from tiers.json styles, a bad value names its line."""
    styles = cfg.get("styles", {})
    allowed = styles.get("allowed", ["voiceover"])
    meta["explicit"] = {k for k in ("style",) + NEW_FIELDS if meta.get(k)}
    style = meta.get("style", "").lower() or styles.get("default", "voiceover")
    if style not in allowed:
        raise ParseError(meta_line["style"], "style must be one of: %s (got %r)" % (", ".join(allowed), meta["style"]))
    tiers_ok = styles.get(style, {}).get("tiers_allowed", list(cfg["tiers"]))
    if tier not in tiers_ok:
        raise ParseError(meta_line.get("style", meta_line.get("tier", 1)),
                         "style %s is only valid for tier %s (this script is tier %s)" % (style, " or ".join(tiers_ok), tier))
    meta["style"] = style
    fields = styles.get("fields", {})
    for key in NEW_FIELDS:
        spec = fields.get(key, {})
        val = meta.get(key, "").lower()
        if val and val not in spec.get("allowed", []):
            raise ParseError(meta_line[key], "%s must be one of: %s (got %r)"
                             % (key, ", ".join(spec.get("allowed", [])) or "nothing, tiers.json has no styles.fields."
                                + key, meta[key]))
        meta[key] = val or spec.get("default")


def tier_limits(cfg, tier, style):
    """The tier's limits with the style's overrides for that tier on top."""
    return merged(cfg["tiers"][tier], cfg.get("styles", {}).get(style, {}).get(tier, {}))


def parse_document(text, cfg, tier_arg=None):
    lines = text.lstrip("\ufeff").splitlines()
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i >= len(lines) or lines[i].strip() != "---":
        raise ParseError(i + 1, "the file must start with a --- front matter block")
    meta, meta_line = {}, {}
    i += 1
    while i < len(lines) and lines[i].strip() != "---":
        raw = lines[i].strip()
        if raw:
            if ":" not in raw:
                raise ParseError(i + 1, "front matter line needs 'key: value'")
            key, val = raw.split(":", 1)
            meta[key.strip().lower()] = val.strip()
            meta_line[key.strip().lower()] = i + 1
        i += 1
    if i >= len(lines):
        raise ParseError(i, "the front matter is not closed with ---")

    sections, current = {"facts": [], "script": [], "caption": []}, None
    seen = set()
    for no in range(i + 2, len(lines) + 1):
        line = lines[no - 1]
        head = re.match(r"^##\s+(.+?)\s*$", line.strip())
        if head:
            current = head.group(1).strip().lower()
            if current in seen and current in sections:
                raise ParseError(no, "duplicate section ## %s" % head.group(1))
            seen.add(current)
        elif current == "caption":
            sections["caption"].append(line)
        elif current in ("facts", "script"):
            if line.strip().startswith("|"):
                sections[current].append((no, line))
            elif line.strip():
                raise ParseError(no, "text outside the %s table" % current)

    tier = meta.get("tier", "").lower()
    if tier_arg and tier and tier_arg != tier:
        raise ParseError(meta_line["tier"], "--tier %s does not match 'tier: %s'" % (tier_arg, tier))
    tier = tier_arg or tier
    if tier not in cfg["tiers"]:
        raise ParseError(meta_line.get("tier", 1), "tier must be one of: %s" % ", ".join(cfg["tiers"]))
    for key in ("platform", "title", "core_takeaway"):
        if not meta.get(key):
            raise ParseError(meta_line.get(key, 1), "front matter is missing '%s'" % key)
    platforms = cfg["tiers"][tier]["platforms"]
    if meta["platform"].lower() not in platforms:
        raise ParseError(meta_line["platform"], "platform for tier %s must be one of: %s" % (tier, ", ".join(platforms)))
    meta["tier"], meta["platform"] = tier, meta["platform"].lower()
    meta["narrator"] = meta.get("narrator", "standard").lower() or "standard"
    if meta["narrator"] not in cfg["narrators"]:
        raise ParseError(meta_line["narrator"], "narrator must be one of: %s" % ", ".join(cfg["narrators"]))
    parse_style(meta, meta_line, cfg, tier)
    t = tier_limits(cfg, tier, meta["style"])
    max_s, min_s = t["max_seconds"], t.get("min_seconds", MIN_SECONDS)
    if meta.get("seconds"):
        try:
            secs = float(meta["seconds"])
        except ValueError:
            raise ParseError(meta_line["seconds"], "seconds must be a number")
        if not min_s <= secs <= max_s:
            raise ParseError(meta_line["seconds"], "seconds must be between %g and %g" % (min_s, max_s))
        meta["seconds"] = secs
    else:
        meta["seconds"] = float(max_s)

    if "script" not in seen:
        raise ParseError(len(lines), "missing ## Script section")
    facts, ids = [], set()
    for no, cells in parse_table(sections["facts"], ["id", "fact", "source", "verified"], "Facts"):
        if not cells["id"]:
            raise ParseError(no, "facts row without an id")
        if cells["id"] in ids:
            raise ParseError(no, "duplicate fact id %s" % cells["id"])
        ids.add(cells["id"])
        facts.append(Fact(no, cells))
    beats = []
    required = ["beat", "time", "voiceover", "visual", "text", "role", "facts"]
    for no, cells in parse_table(sections["script"], required, "Script"):
        if not cells["beat"].isdigit() or int(cells["beat"]) != len(beats) + 1:
            raise ParseError(no, "beat numbers must run 1, 2, 3 in order (got %r)" % cells["beat"])
        tm = TIME_RE.match(cells["time"])
        if not tm:
            raise ParseError(no, "time must be 'start-end' in seconds (got %r)" % cells["time"])
        roles = parse_roles(cells["role"], no, tier, cfg)
        beats.append(Beat(no, cells, roles, float(tm.group(1)), float(tm.group(2))))
    if not beats:
        raise ParseError(len(lines), "the Script table has no beats")
    caption = "\n".join(sections["caption"]).strip()
    return Doc(meta, facts, beats, caption)


# ---------------------------------------------------------------- context and measures

class Context:
    def __init__(self, doc, cfg, brand, final=False):
        self.doc, self.cfg, self.brand, self.final = doc, cfg, brand, final
        self.tname = doc.meta["tier"]
        self.styles = cfg.get("styles", {})
        self.style = doc.meta.get("style") or "voiceover"
        self.ugc = self.style in self.styles.get("ugc_styles", UGC)
        self.ur = self.styles.get("ugc_rules", {})
        self.explicit = doc.meta.get("explicit", set())
        # A voiceover script that sets none of the new fields keeps the 0.2.0 report.
        self.legacy = self.style == "voiceover" and not (self.explicit & set(NEW_FIELDS))
        self.t = tier_limits(cfg, self.tname, self.style)
        self.narrator = cfg["narrators"][doc.meta["narrator"]]
        self.secs = doc.meta["seconds"]
        self.ratio = self.secs / self.t["max_seconds"]
        self.allow = set(cfg.get("acronym_allowlist", []))
        self.findings = []
        self.facts_low = " \n ".join(f.low for f in doc.facts)
        self.cta = [b for b in doc.beats if b.has("cta")]
        self.dominant = next((r.split(":")[1] for b in doc.beats for r in b.roles if r.startswith("open:")), None)
        measure(self)

    def add(self, rule, sev, msg, quote_text=""):
        self.findings.append({"id": rule, "severity": sev, "message": msg, "quote": quote_text})

    def is_long(self):
        return self.tname == "long"

    def checks(self, rid):
        """False for a rule that does not run in this script's style (see STYLE_ONLY)."""
        return self.style in STYLE_ONLY.get(rid, (self.style,))


def merged(base, override):
    """A copy of base with override's values on top; nested objects merge key by key."""
    out = dict(base)
    for k, v in override.items():
        out[k] = merged(out[k], v) if isinstance(v, dict) and isinstance(out.get(k), dict) else v
    return out


def is_brand(ctx, name):
    return norm(name) == norm(ctx.brand.get("brand", ""))


def cited_rows(ctx, b):
    return [ctx.doc.facts_by_id[f] for f in b.facts if f in ctx.doc.facts_by_id]


def fact_units(ctx, b):
    """Facts a beat carries: declared ids, plus numbers and names not covered by them."""
    facts, declared = ctx.doc.facts, cited_rows(ctx, b)
    units = set(b.facts)
    for n in sorted(b.claim_numbers):
        if not any(f.has_number(n) for f in declared):
            row = next((f for f in facts if f.has_number(n)), None)
            units.add(row.id if row else "#" + n)
    for name in b.names:
        if any(f.has_phrase(name) for f in declared) or is_brand(ctx, name):
            continue
        row = next((f for f in facts if f.has_phrase(name)), None)
        units.add(row.id if row else "@" + name)
    return units


def known_names(ctx):
    """Lowercase words that count as names even at a sentence start."""
    known = {norm(n) for n in ctx.brand.get("place_names", {}).get("names", [])}
    texts = [f.text for f in ctx.doc.facts] + [spoken(b.vo) for b in ctx.doc.beats]
    for t in texts:
        for name in proper_nouns(t, ctx.allow):
            known.update(norm(w) for w in name.split())
    return known


def measure(ctx):
    pace = ctx.narrator["pace"]
    known = known_names(ctx)
    for b in ctx.doc.beats:
        said = spoken(b.vo)
        shown = " ".join(b.overlay)
        b.said = said
        b.word_list = words(said)
        b.words = len(b.word_list)
        b.pause = sum(float(x) for x in PAUSE_RE.findall(b.vo))
        b.vo_digits = digits(said)
        b.digit_values = set(b.vo_digits) | set(digits(shown))
        both = said + " " + shown
        big = set(spelled_big(both))
        small = {w.lower() for w in words(SPELLED_BIG_RE.sub(" ", both)) if w.lower() in SPELLED_SMALL}
        b.claim_numbers = b.digit_values | big
        claims = {}
        for n, unit, text in number_claims(said) + number_claims(shown):
            claims.setdefault((n, unit), text)
        b.claims = [(n, unit, claims[(n, unit)]) for n, unit in sorted(claims, key=lambda c: (c[0], c[1] or ""))]
        b.number_values = b.claim_numbers | small
        b.est = (b.words / (ctx.t["wps"] * pace)
                 + ctx.t["number_penalty_seconds"] * len(b.vo_digits) + b.pause)
        b.names = proper_nouns(said, ctx.allow, known)
        b.overlay_words = len(words(shown))
        b.units = fact_units(ctx, b)
    beats = ctx.doc.beats
    ctx.total_words = sum(b.words for b in beats)
    ctx.total_est = sum(b.est for b in beats)
    ctx.end = beats[-1].end
    ctx.info = ["%s: about %.0f s with no voice or [PAUSE] (declared %g s, estimated %.1f s)"
                % (b.label(), b.seconds - b.est, b.seconds, b.est)
                for b in beats if b.seconds - b.est > HOLD_INFO_SECONDS]


# ---------------------------------------------------------------- rule families

def check_time(ctx):
    t, beats = ctx.t, ctx.doc.beats
    if ctx.total_est > ctx.secs:
        ctx.add("T01", "block", "estimated %.1f s, maximum %.0f s" % (ctx.total_est, ctx.secs))
    elif ctx.total_est > t["warn_seconds"] * ctx.ratio:
        ctx.add("T02", "warn", "estimated %.1f s, warning line %.1f s" % (ctx.total_est, t["warn_seconds"] * ctx.ratio))
    if beats[0].start != 0:
        ctx.add("T03", "block", "first beat starts at %g, not 0" % beats[0].start)
    for prev, b in zip(beats, beats[1:]):
        if b.start != prev.end:
            ctx.add("T03", "block", "%s starts at %g but beat %d ends at %g" % (b.label(), b.start, prev.n, prev.end))
    for b in beats:
        if b.end <= b.start:
            ctx.add("T03", "block", "%s ends at or before it starts" % b.label(), "%g-%g" % (b.start, b.end))
    if ctx.end > ctx.secs:
        ctx.add("T03", "block", "last beat ends at %g s, maximum %.0f s" % (ctx.end, ctx.secs))
    if ctx.end < t.get("min_seconds", 0):
        ctx.add("T03", "block", "last beat ends at %g s, minimum %g s for style %s" % (ctx.end, t["min_seconds"], ctx.style))
    for b in beats:
        if b.seconds <= 0:
            continue
        over = b.est / b.seconds
        if over > BEAT_OVER_WARN:
            sev = "block" if over > BEAT_OVER_BLOCK else "warn"
            ctx.add("T04", sev, "%s needs %.1f s for %g s declared (+%d%%)"
                    % (b.label(), b.est, b.seconds, round((over - 1) * 100)), quote(b.vo))


def check_words(ctx):
    t, scale = ctx.t, ctx.narrator["word_scale"]
    w = t["words"]
    ratio = ctx.ratio if w.get("scale_with_seconds", True) else 1.0
    hard = w["hard_max"] * scale * ratio
    lo, hi = w["target_min"] * scale * ratio, w["target_max"] * scale * ratio
    if ctx.total_words > hard:
        ctx.add("W01", "block", "%d words, maximum %.0f" % (ctx.total_words, hard))
    elif not lo <= ctx.total_words <= hi:
        ctx.add("W02", "warn", "%d words, target %.0f to %.0f" % (ctx.total_words, lo, hi))
    wb = t["words_per_beat"]
    for b in ctx.doc.beats:
        if b.words > wb["hard_max"] * scale:
            ctx.add("W03", "block", "%s has %d words, maximum %.0f" % (b.label(), b.words, wb["hard_max"] * scale), quote(b.vo))
        elif b.has("hook") or b.has("cta") or b.has("disclosure"):
            continue  # hook and cta lengths are governed by H01 and C03; a disclosure line is as long as it must be
        elif not wb["target_min"] * scale <= b.words <= wb["target_max"] * scale:
            ctx.add("W03", "warn", "%s has %d words, target %.0f to %.0f"
                    % (b.label(), b.words, wb["target_min"] * scale, wb["target_max"] * scale), quote(b.vo))


def check_beats(ctx):
    lim, n = ctx.t["beats"], len(ctx.doc.beats)
    if n < lim["min"] or n > lim["hard_max"]:
        ctx.add("B01", "block", "%d beats, allowed %d to %d" % (n, lim["min"], lim["hard_max"]))
    elif n > lim["target_max"]:
        ctx.add("B01", "warn", "%d beats, target at most %d" % (n, lim["target_max"]))
    spb = ctx.t["seconds_per_beat"]
    for b in ctx.doc.beats:
        if not spb["min"] <= b.seconds <= spb["max"]:
            ctx.add("B02", "warn", "%s lasts %g s, range %g to %g" % (b.label(), b.seconds, spb["min"], spb["max"]))


def words_until(beats, second):
    """Spoken words before a time, counting a straddling beat pro rata."""
    total = 0.0
    for b in beats:
        if b.end <= second:
            total += b.words
        elif b.start < second and b.seconds > 0:
            total += b.words * (second - b.start) / b.seconds
    return total


def check_hook(ctx):
    h, beats, first = ctx.t["hook"], ctx.doc.beats, ctx.doc.beats[0]
    if not ctx.is_long():
        # ugc_talk: an overlay hook on screen from frame one buys the first line one more second
        max_s = h.get("max_seconds_with_overlay", h["max_seconds"]) if first.overlay else h["max_seconds"]
        if first.end > max_s:
            ctx.add("H01", "block", "hook beat ends at %g s, maximum %g s" % (first.end, max_s))
        if first.words > h["hard_max_words"]:
            ctx.add("H01", "block", "hook has %d words, maximum %d" % (first.words, h["hard_max_words"]), quote(first.vo))
        elif first.est > max_s * BEAT_OVER_BLOCK:
            ctx.add("H01", "block", "hook needs %.1f s to say, too slow for %g s" % (first.est, max_s), quote(first.vo))
        if first.words < h["min_words"]:
            ctx.add("H01", "warn", "hook has %d words, minimum %d" % (first.words, h["min_words"]), quote(first.vo))
        check_first_words(ctx, h, first)
        window = max_s
    else:
        early = words_until(beats, h["verbal_by_seconds"])
        if early > h["max_words"]:
            ctx.add("H01", "block", "%.0f words before %g s, maximum %d" % (early, h["verbal_by_seconds"], h["max_words"]))
        promise = next((b for b in beats if b.has("promise")), None)
        if not promise:
            ctx.add("H01", "block", "no beat has the promise role")
        else:
            if promise.end > h["promise_by_seconds"]:
                ctx.add("H01", "block", "promise ends at %g s, maximum %g s" % (promise.end, h["promise_by_seconds"]))
            upto = sum(b.words for b in beats if b.n <= promise.n)
            if upto > h["promise_max_words"]:
                ctx.add("H01", "block", "%d words up to the promise, maximum %d" % (upto, h["promise_max_words"]))
        window = h["verbal_by_seconds"]
    ctx.hook_window = window
    if ctx.checks("H02"):
        if H02_BANNED.search(first.visual):
            ctx.add("H02", "block", "beat 1 visual opens on a logo, intro or greeting", quote(first.visual))
        elif not H02_MOTION.search(first.visual):
            ctx.add("H02", "warn", "beat 1 visual names no motion or person", quote(first.visual))
    gs = ctx.brand.get("guest_subject", {})
    if gs.get("hook_must_contain_you", True) and ctx.checks("H03"):
        if not any(has_phrase(hook_text(ctx), w) for w in gs.get("you_words", ["you", "your"])):
            ctx.add("H03", "warn", "no you or your in the first %g s" % window)


def check_first_words(ctx, h, first):
    """ugc_talk short: the first word by first_word_by_seconds, and a first sentence of 6 to 15 words."""
    if "first_word_by_seconds" in h:
        lead = re.match(r"^(\s*\[\s*PAUSE\s+\d+(?:\.\d+)?\s*s?\s*\]\s*)+", first.vo, re.I)
        delay = sum(float(x) for x in PAUSE_RE.findall(lead.group(0))) if lead else 0.0
        if not first.words:
            ctx.add("H01", "block", "beat 1 has no spoken word; the first word must come by %g s" % h["first_word_by_seconds"])
        elif delay > h["first_word_by_seconds"]:
            ctx.add("H01", "block", "first word comes after a %g s pause, it must come by %g s"
                    % (delay, h["first_word_by_seconds"]), quote(first.vo))
    if "first_sentence_max_words" in h and first.words:
        joined = " ".join(spoken(b.vo).strip() for b in ctx.doc.beats if b.vo.strip() not in ("", "-"))
        sentence = next((x for x in re.split(r"(?<=[.!?])\s+", joined) if words(x)), "")
        n = len(words(sentence))
        if n > h["first_sentence_max_words"]:
            ctx.add("H01", "block", "first sentence has %d words, maximum %d" % (n, h["first_sentence_max_words"]),
                    quote(sentence))
        elif n < h["first_sentence_min_words"]:
            ctx.add("H01", "warn", "first sentence has %d words, minimum %d" % (n, h["first_sentence_min_words"]),
                    quote(sentence))


def hook_text(ctx):
    """Lowercase voiceover and overlay of the beats that start inside the hook window."""
    return norm(" ".join(spoken(b.vo) + " " + b.text for b in ctx.doc.beats if b.start < ctx.hook_window))


def check_facts(ctx):
    f, beats, doc = ctx.t["facts"], ctx.doc.beats, ctx.doc
    for b in beats:
        if len(b.units) > f["per_beat_max"]:
            ctx.add("F01", "block", "%s carries %d facts, maximum %d" % (b.label(), len(b.units), f["per_beat_max"]),
                    ", ".join(sorted(b.units)))
        if "numbers_per_beat_max" in f and len(b.number_values) > f["numbers_per_beat_max"]:
            ctx.add("F01", "block", "%s has %d numbers, maximum %d" % (b.label(), len(b.number_values), f["numbers_per_beat_max"]),
                    ", ".join(sorted(b.number_values)))
    units = set().union(*[b.units for b in beats])
    if len(units) > f["per_script_max"]:
        ctx.add("F02", "block", "%d facts in the script, maximum %d" % (len(units), f["per_script_max"]), ", ".join(sorted(units)))
    numbers = set().union(*[b.number_values for b in beats])
    if len(numbers) > f["numbers_per_script_max"]:
        ctx.add("F03", "block", "%d numbers in the script, maximum %d" % (len(numbers), f["numbers_per_script_max"]),
                ", ".join(sorted(numbers)))
    final_sev = "block" if ctx.final else "warn"
    for b in beats:
        check_beat_numbers(ctx, b, final_sev)
    for n in sorted(set(digits(doc.caption)) | set(spelled_big(doc.caption))):
        rows = [r for r in doc.facts if r.has_number(n)]
        if not rows:
            ctx.add("F04", "block", "caption: number not in the facts table", n)
        elif not any(r.verified == "yes" for r in rows):
            ctx.add("F04", final_sev, "caption: number only in an unverified fact row", n)
    used = sorted({fid for b in beats for fid in b.facts})
    for fid in used:
        row = doc.facts_by_id.get(fid)
        if row is None:
            ctx.add("F05", "block", "fact id is not in the facts table", fid)
        elif row.verified != "yes":
            ctx.add("F04", final_sev, "fact used but not verified yes", fid)
    for row in doc.facts:
        if not row.source.strip() or row.source.strip() == "-" or not row.text.strip():
            ctx.add("F06", "block", "fact row %s has no source or no text" % row.id)
        if row.verified not in ("yes", "no"):
            ctx.add("F06", "block", "fact row %s: verified must be yes or no" % row.id, row.verified)
    for name in sorted({n for b in beats for n in b.names}):
        if not has_phrase(ctx.facts_low, name) and not is_brand(ctx, name):
            ctx.add("F07", "warn", "proper noun not in the facts table", name)


def check_beat_numbers(ctx, b, final_sev):
    """F04 for one beat: each number must be in a verified row the beat cites, counting the same thing."""
    cited, facts = cited_rows(ctx, b), ctx.doc.facts
    for n, unit, said in b.claims:
        mine = [r for r in cited if r.says(n, unit)]
        rows = [r for r in facts if r.says(n, unit)]
        other = [r for r in cited if r.has_number(n) and r not in mine]
        if mine:
            if not any(r.verified == "yes" for r in mine):
                ctx.add("F04", final_sev, "%s: number only in an unverified fact row" % b.label(), said)
        elif rows:
            ctx.add("F04", final_sev, "%s: number is in %s, which this beat does not cite"
                    % (b.label(), ", ".join(r.id for r in rows)), said)
        elif other or any(r.has_number(n) for r in facts):
            # The digit is reused for a claim no row makes ("10 guides" against "10 minutes"): an invented claim.
            row = (other or [r for r in facts if r.has_number(n)])[0]
            ctx.add("F04", "block", "%s: '%s' is a different claim from %s, which says '%s'. Add a sourced row "
                    "that says it, or cut the number" % (b.label(), said, row.id, row.context(n)), said)
        else:
            ctx.add("F04", "block", "%s: number not in the facts table" % b.label(), said)


def check_sentences(ctx):
    s = ctx.t["sentence"]
    joined = " ".join(spoken(b.vo).strip() for b in ctx.doc.beats if b.vo.strip() not in ("", "-"))
    sentences = [x for x in re.split(r"(?<=[.!?])\s+", joined) if words(x)]
    for x in sentences:
        if len(words(x)) > s["hard_max_words"]:
            ctx.add("S01", "block", "sentence of %d words, maximum %d" % (len(words(x)), s["hard_max_words"]), quote(x))
    if sentences:
        avg = sum(len(words(x)) for x in sentences) / float(len(sentences))
        if not s["avg_min"] <= avg <= s["avg_max"]:
            ctx.add("S01", "warn", "average sentence %.1f words, range %g to %g" % (avg, s["avg_min"], s["avg_max"]))


def check_visuals(ctx):
    v = ctx.t["visual"]
    for b in ctx.doc.beats:
        if not b.shots:
            ctx.add("V02", "block", "%s has no visual" % b.label())
            continue
        per = b.seconds / len(b.shots)
        takes = [x for x in b.shots if ONE_TAKE_RE.match(x)]
        if takes:
            # A continuous take that names a move is motion, not a static hold.
            for x in takes:
                if not TAKE_MOTION.search(ONE_TAKE_RE.sub("", x)):
                    ctx.add("V01", "warn", "%s: one take names no camera or subject move" % b.label(), quote(x))
            continue
        if "hard_max_static_seconds" in v and len(b.shots) == 1 and b.seconds > v["hard_max_static_seconds"]:
            ctx.add("V01", "block", "%s holds one shot for %g s, maximum %g" % (b.label(), b.seconds, v["hard_max_static_seconds"]),
                    quote(b.visual))
        elif per > v["max_seconds_per_shot"]:
            ctx.add("V01", "warn", "%s: %.1f s per shot, maximum %g" % (b.label(), per, v["max_seconds_per_shot"]), quote(b.visual))
    window = v.get("pattern_interrupt_every_seconds")
    if window:
        marks = [b for b in ctx.doc.beats if len(b.shots) >= 2 or b.has("shift") or b.has("reengage")]
        edges = [(0.0, 0.0)] + [(b.start, b.end) for b in marks] + [(ctx.end, ctx.end)]
        for (_, a), (c, _) in zip(edges, edges[1:]):
            if c - a >= window:
                ctx.add("V03", "warn", "no cut, shift or reengage from %g s to %g s" % (a, c))


def check_overlay(ctx):
    o = ctx.t["overlay"]
    persistent = o.get("persistent")
    for b in ctx.doc.beats:
        if not b.overlay:
            continue
        if b.overlay_words > o["max_words"]:
            ctx.add("O01", "block", "%s overlay has %d words, maximum %d" % (b.label(), b.overlay_words, o["max_words"]), quote(b.text))
        for line in b.overlay:
            if len(line) > o["max_chars_per_line"]:
                ctx.add("O01", "block", "%s overlay line has %d characters, maximum %d"
                        % (b.label(), len(line), o["max_chars_per_line"]), quote(line))
        if len(b.overlay) > o["max_lines"]:
            ctx.add("O01", "block", "%s overlay has %d lines, maximum %d" % (b.label(), len(b.overlay), o["max_lines"]))
        chars = sum(len(x) for x in b.overlay)
        if not persistent and (b.seconds < o["min_seconds"] or (b.seconds > 0 and chars / b.seconds > o["chars_per_second"])):
            ctx.add("O02", "warn", "%s overlay: %d characters in %g s, limit %g per second and %g s minimum"
                    % (b.label(), chars, b.seconds, o["chars_per_second"], o["min_seconds"]), quote(b.text))
        said = {w.lower() for w in b.word_list}
        if said:
            shared = said & {w.lower() for w in words(" ".join(b.overlay))}
            if len(shared) / float(len(said)) > OVERLAY_REPEAT_MAX:
                ctx.add("O03", "warn", "%s overlay repeats %d of %d voiceover words" % (b.label(), len(shared), len(said)), quote(b.text))
    if persistent:
        check_persistent_overlay(ctx, o)
    if not ctx.doc.beats[0].overlay:
        if o.get("required_in_first_beat"):
            ctx.add("O04", "block", "beat 1 has no overlay; style %s needs its text on screen from frame one" % ctx.style)
        else:
            ctx.add("O04", "warn", "beat 1 has no overlay for sound-off viewers")


def check_persistent_overlay(ctx, o):
    """Text that stays on screen (ugc_text): each distinct line counts once across the script."""
    lines, first = [], None
    for b in ctx.doc.beats:
        for line in b.overlay:
            if norm(line).strip() not in [norm(x).strip() for x in lines]:
                lines.append(line)
                first = b if first is None else first
    if not lines:
        return
    n = sum(len(words(x)) for x in lines)
    if len(lines) > o["script_max_lines"]:
        ctx.add("O01", "block", "%d different overlay lines in the script, maximum %d" % (len(lines), o["script_max_lines"]),
                " / ".join(lines))
    if n > o["script_max_words"]:
        ctx.add("O01", "block", "%d overlay words in the script, maximum %d" % (n, o["script_max_words"]), " / ".join(lines))
    elif n < o["script_min_words"]:
        ctx.add("O01", "warn", "%d overlay words in the script, minimum %d" % (n, o["script_min_words"]), " / ".join(lines))
    shown = ctx.end - first.start
    chars = sum(len(x) for x in lines)
    if shown < o["min_seconds"] or (shown > 0 and chars / shown > o["chars_per_second"]):
        ctx.add("O02", "warn", "overlay: %d characters on screen for %g s, limit %g per second and %g s minimum"
                % (chars, shown, o["chars_per_second"], o["min_seconds"]), " / ".join(lines))


def payoff_index(ctx):
    idx = [b.n for b in ctx.doc.beats if b.has("payoff") or (ctx.dominant and b.has("close:" + ctx.dominant))]
    return max(idx) if idx else None


def check_cta(ctx):
    c, cta, beats = ctx.t["cta"], ctx.cta, ctx.doc.beats
    hard_max = c.get("hard_max", c["max"])
    soft = [b for b in beats if b.has("soft-cta")]
    if not c["min"] <= len(cta) <= hard_max:
        ctx.add("C01", "block", "%d cta beats, allowed %d to %d" % (len(cta), c["min"], hard_max))
    if len(cta) + len(soft) > c["max"]:
        ctx.add("C01", "block", "%d asks (cta plus soft-cta beats), maximum %d" % (len(cta) + len(soft), c["max"]))
    if len(soft) > c.get("soft_mid_max", 0):
        ctx.add("C01", "block", "%d soft-cta beats, maximum %d" % (len(soft), c.get("soft_mid_max", 0)))
    cfg = ctx.brand.get("cta", {})
    untagged = cfg.get("untagged_regex")
    for b in beats:
        if untagged and not (b.has("cta") or b.has("soft-cta")):
            m = re.search(untagged, norm(b.said + " / " + b.text))
            if m:
                ctx.add("C01", "warn", "%s asks for an action but has no cta role" % b.label(), m.group(0))
    minis = [b.end for b in beats if any(r.startswith("mini:") for r in b.roles)]
    not_before = max(ctx.t["hook"].get("promise_by_seconds", 0), min(minis) if minis else 0)
    for b in soft:
        if b.start < not_before:
            ctx.add("C02", "block", "%s soft-cta starts at %g s, not before %g s (after the promise and the first mini-payoff)"
                    % (b.label(), b.start, not_before))
    for b in cta:
        low = norm(b.said)
        verbs = [v for v in cfg.get("verbs", []) if has_phrase(low, v)]
        if len(verbs) > 1:
            ctx.add("C03", "warn", "%s stacks %d asks, keep one" % (b.label(), len(verbs)), ", ".join(verbs))
    pay = payoff_index(ctx)
    for b in cta:
        if b.start < ctx.end - c["last_seconds"]:
            ctx.add("C02", "block", "%s cta starts at %g s, must start in the last %g s (from %g s)"
                    % (b.label(), b.start, c["last_seconds"], ctx.end - c["last_seconds"]))
        if b.words > c["max_words"]:
            ctx.add("C03", "block", "%s cta has %d words, maximum %d" % (b.label(), b.words, c["max_words"]), quote(b.vo))
        if pay and b.n < pay:
            ctx.add("C04", "block", "%s cta comes before the payoff in beat %d" % (b.label(), pay))
    tags = re.findall(r"(?<!\w)#\w+", ctx.doc.caption)
    if len(tags) > CAPTION_HASHTAGS_MAX:
        ctx.add("C05", "warn", "caption has %d hashtags, maximum %d" % (len(tags), CAPTION_HASHTAGS_MAX), " ".join(tags))


def loop_tokens(beats):
    return [(b, r.split(":")[0], r.split(":")[1]) for b in beats for r in b.roles if r[:5] in ("open:", "close")]


def check_loops_short(ctx):
    beats = ctx.doc.beats
    first, tokens = beats[0], loop_tokens(beats)
    if not first.has("hook"):
        ctx.add("L01", "block", "beat 1 needs the hook role")
    opens1 = [x for b, k, x in tokens if b is first and k == "open"]
    if len(opens1) != 1:
        ctx.add("L01", "block", "beat 1 needs exactly one open:X token (found %d)" % len(opens1))
        return
    dom = opens1[0]
    closes = [b for b, k, x in tokens if k == "close" and x == dom]
    last_only = ctx.t["loops"].get("close_in_last_beat")
    tail = {beats[-1].n} if last_only else {beats[-1].n, beats[-2].n if len(beats) > 1 else beats[-1].n}
    if len(closes) != 1 or closes[0].n not in tail:
        ctx.add("L01", "block", "close:%s must appear once, in the %s beat"
                % (dom, "final" if last_only else "final or second-last"))
    others = [(b, k, x) for b, k, x in tokens if not (x == dom and ((k == "open" and b is first) or k == "close"))]
    for b, k, x in others:
        ctx.add("L01", "block", "%s: short form allows one loop only" % b.label(), "%s:%s" % (k, x))


def check_loops_long(ctx):
    lp, beats = ctx.t["loops"], ctx.doc.beats
    dom, opened = ctx.dominant, {}
    if not dom:
        ctx.add("L01", "block", "no open:X token for the dominant loop")
    for b in beats:
        for r in b.roles:
            if r.startswith("close:"):
                x = r[6:]
                if x not in opened:
                    ctx.add("L01", "block", "%s closes loop %s that is not open" % (b.label(), x))
                opened.pop(x, None)
        for r in b.roles:
            if r.startswith("open:"):
                x = r[5:]
                if x in opened:
                    ctx.add("L01", "block", "%s opens loop %s twice" % (b.label(), x))
                opened[x] = b
        if len(opened) > lp["max_open"]:
            ctx.add("L01", "block", "%s leaves %d loops open, maximum %d" % (b.label(), len(opened), lp["max_open"]))
    for x, b in sorted(opened.items()):
        sev = "block" if x == dom else "warn"
        ctx.add("L01", sev, "loop %s opened in %s never closes" % (x, b.label()))
    if dom:
        ob = next(b for b in beats if b.has("open:" + dom))
        if ob.end > lp["dominant_open_by_seconds"]:
            ctx.add("L01", "block", "dominant loop opens in a beat ending at %g s, maximum %g s" % (ob.end, lp["dominant_open_by_seconds"]))
        cb = next((b for b in beats if b.has("close:" + dom)), None)
        if cb and cb.end > lp["dominant_close_by_seconds"]:
            ctx.add("L01", "block", "dominant loop closes at %g s, maximum %g s" % (cb.end, lp["dominant_close_by_seconds"]))
        if cb and ctx.cta and cb.n >= ctx.cta[0].n:
            ctx.add("L01", "block", "dominant loop must close before the cta beat")
    chapters = sorted({int(r[3:]) for b in beats for r in b.roles if r.startswith("ch:")})
    ch = ctx.t["chapters"]
    if not ch["min"] <= len(chapters) <= ch["max"]:
        ctx.add("L01", "block", "%d chapters, allowed %d to %d" % (len(chapters), ch["min"], ch["max"]))
    if lp.get("mini_payoff_per_chapter"):
        for n in chapters:
            if not any(b.has("mini:%d" % n) for b in beats):
                ctx.add("L01", "block", "chapter %d has no mini:%d beat" % (n, n))
    for prev, n in zip(chapters, chapters[1:]):
        last = max(b.n for b in beats if b.has("ch:%d" % prev))
        start = min(b.n for b in beats if b.has("ch:%d" % n))
        if not any(b.has("progress") for b in beats if last <= b.n <= start):
            ctx.add("L01", "warn", "no progress beat between chapter %d and chapter %d" % (prev, n))
    for a, z in lp.get("reengage_windows", []):
        if a < ctx.end and not any(b.has("reengage") and b.start < z and b.end > a for b in beats):
            ctx.add("L01", "warn", "no reengage beat between %g s and %g s" % (a, z))
    pa = lp.get("partial_answer_window")
    if pa and pa[0] < ctx.end and not any(b.has("partial") and b.start < pa[1] and b.end > pa[0] for b in beats):
        ctx.add("L01", "warn", "no partial beat between %g s and %g s" % (pa[0], pa[1]))


def check_loops(ctx):
    (check_loops_long if ctx.is_long() else check_loops_short)(ctx)


def check_style(ctx):
    beats = ctx.doc.beats
    fields = [(b.label(), x) for b in beats for x in (b.vo, b.visual, b.text)] + [("caption", ctx.doc.caption)]
    for where, x in fields:
        for ch, name in ((EM_DASH, "em dash"), (EN_DASH, "en dash")):
            if ch in x:
                ctx.add("R01", "block", "%s contains an %s" % (where, name), quote(x))
        if EMOJI_RE.search(x):
            ctx.add("R01", "block", "%s contains an emoji" % where, quote(x))
    for b in beats:
        cells = b.vo if ctx.ugc else b.vo + " / " + b.text  # ugc overlays are checked by U04
        for w in re.findall(r"\b[A-Z]{3,}\b", BRACKET_RE.sub(" ", cells)):
            if w not in ctx.allow:
                ctx.add("R02", "warn", "%s: capitals for emphasis" % b.label(), w)
    gs = ctx.brand.get("guest_subject", {})
    text = norm(" ".join(spoken(b.vo) + " " + b.text for b in beats))
    count = lambda ws: sum(len(re.findall(r"(?<![a-z0-9'])%s(?![a-z0-9'])" % re.escape(w), text)) for w in ws)
    you, company = count(gs.get("you_words", [])), count(gs.get("company_words", []))
    side = "you"
    if ctx.ugc:  # a creator's I and my are not company words; they sit with you on the guest side
        you += count(ctx.ur.get("first_person_words", []))
        side = "you and I"
    limit = gs.get("max_company_to_you_ratio")
    if limit is not None and company > you * limit:
        ctx.add("R03", "warn", "%d company words against %d %s words, ratio limit %g" % (company, you, side, limit))


# ---------------------------------------------------------------- ugc styles (U01 to U07), D01, SND01

def check_ugc(ctx):
    """Creator-led rules. Every list and number comes from tiers.json styles."""
    if not ctx.ugc:
        return
    u, beats = ctx.ur, ctx.doc.beats
    first = beats[0]
    banned = phrase_hits(first.visual, u["first_frame_banned"])
    if banned:
        ctx.add("U01", "block", "beat 1 visual opens on a greeting or intro; open on the creator mid-action",
                ", ".join(banned))
    elif not phrase_hits(first.visual, u["first_frame_person_cues"]):
        ctx.add("U01", "block", "beat 1 visual shows no person, selfie, POV, handheld shot or hands "
                "(a product or landscape shot alone is not a ugc opening)", quote(first.visual))
    for b in beats:
        hits = phrase_hits(b.visual, u["visual_disallowed"])
        if u.get("visual_disallowed_regex"):
            hits += [m.group(0) for m in re.finditer(u["visual_disallowed_regex"], norm(b.visual))]
        if hits:
            ctx.add("U02", "block", "%s visual uses edited brand graphics or stock; ugc is shot on the phone"
                    % b.label(), ", ".join(hits))
    if ctx.checks("U03"):
        gs = ctx.brand.get("guest_subject", {})
        hook = hook_text(ctx)
        if not any(has_phrase(hook, w) for w in gs.get("you_words", ["you", "your"]) + u["hook_first_person_stakes"]):
            ctx.add("U03", "warn", "hook names no you and no first-person stake (I, my, we) in the first %g s"
                    % ctx.hook_window)
    caps = re.compile(r"\b[A-Z]{%d,}\b" % u["overlay_caps_min_letters"])
    for b in beats:
        shouted = [w for w in caps.findall(BRACKET_RE.sub(" ", b.text)) if w not in ctx.allow]
        if shouted:
            ctx.add("U04", "warn", "%s overlay uses capitals for emphasis, write it in sentence or lower case"
                    % b.label(), ", ".join(shouted))
    soft_re = u.get("cta_soft_regex")
    any_soft = False
    for b in ctx.cta:
        cells = b.said + " / " + b.text
        soft = phrase_hits(cells, u["cta_soft_prompts"])
        if soft_re:
            soft += [m.group(0) for m in re.finditer(soft_re, norm(cells))]
        any_soft = any_soft or bool(soft)
        link = phrase_hits(cells, u["cta_link_only"])
        if link and not soft:
            ctx.add("U05", "warn", "%s: the only ask is a link; ask a soft prompt and put the link in the caption"
                    % b.label(), ", ".join(link))
        elif not soft:
            ctx.add("U05", "warn", "%s cta is not a soft prompt (save this, send this to, which one, follow along, "
                    "or how to book)" % b.label(), quote(b.vo if b.vo.strip() not in ("", "-") else b.text))
    if not any_soft:
        # a link-only ask in a beat without the cta role is still the script's only ask
        for b in beats:
            link = phrase_hits(b.said + " / " + b.text, u["cta_link_only"])
            if link and not b.has("cta"):
                ctx.add("U05", "warn", "%s: the only ask is a link; ask a soft prompt in a cta beat and put the link "
                        "in the caption" % b.label(), ", ".join(link))
    if ctx.checks("U06"):
        check_casual(ctx)
    for b in beats:
        n = len(words(ONE_TAKE_RE.sub("", b.visual.strip())))
        if b.shots and n < u["visual_min_words"]:
            ctx.add("U07", "warn", "%s visual has %d words, minimum %d: name who or what is on camera"
                    % (b.label(), n, u["visual_min_words"]), quote(b.visual))


def check_casual(ctx):
    """U06: casual markers and contractions per 100 spoken words, limits from the style tier's casual object."""
    lim = ctx.t.get("casual")
    if not lim or not ctx.total_words:
        return
    markers, contractions = casual_markers(ctx), contraction_list(ctx)
    per = 100.0 / ctx.total_words
    if len(markers) * per > lim["markers_max_per_100_words"]:
        ctx.add("U06", "warn", "%d casual markers in %d words (%.1f per 100), maximum %g per 100"
                % (len(markers), ctx.total_words, len(markers) * per, lim["markers_max_per_100_words"]),
                ", ".join(markers))
    if len(contractions) * per < lim["contractions_min_per_100_words"]:
        ctx.add("U06", "warn", "%d contractions in %d words (%.1f per 100), minimum %g per 100: write it the way "
                "the creator talks" % (len(contractions), ctx.total_words, len(contractions) * per,
                                        lim["contractions_min_per_100_words"]))


def casual_markers(ctx):
    """Casual markers in the voiceover, each counted once even when two list entries overlap."""
    u, found = ctx.ur, []
    word = r"(?<![a-z0-9']){}(?![a-z0-9'])"
    pats = [(word.format(re.escape(m.lower())), m) for m in sorted(u["casual_markers"], key=len, reverse=True)]
    if u.get("casual_filler_like_regex"):
        pats.append((u["casual_filler_like_regex"], "like"))
    for b in ctx.doc.beats:
        for sentence in re.split(r"(?<=[.!?])\s+", norm(spoken(b.vo)).strip()):
            sentence = sentence.lstrip(" \"'(")
            taken = []
            for pat, m in pats:
                for hit in re.finditer(pat, sentence):
                    if any(hit.start() < e and s < hit.end() for s, e, _ in taken):
                        continue
                    taken.append((hit.start(), hit.end(), m))
            found += [m for _, _, m in sorted(taken)]
    return found


def contraction_list(ctx):
    """Spoken contractions: n't, 're, 've, 'll, 'd, 'm, and 's after the words in contraction_s_words."""
    u, out = ctx.ur, []
    s_words = set(u.get("contraction_s_words", []))
    for b in ctx.doc.beats:
        for w in b.word_list:
            low = norm(w)
            if low in s_words or any(low.endswith(x) for x in u.get("contraction_suffixes", [])):
                out.append(low)
    return out


def check_disclosure(ctx):
    """D01: who the creator is to the brand, said early, and an Ad label on paid or gifted posts."""
    d = ctx.styles.get("disclosure")
    rel = ctx.doc.meta.get("relationship")
    if not d or not (ctx.ugc or "relationship" in ctx.explicit):
        return
    paid, role = rel in d["ad_label_required"], rel in d["role_line_expected"]
    if not (paid or role):
        return
    early = [b for b in ctx.doc.beats if b.has(d["role_token"]) and b.start < d["within_seconds"]]
    cells = lambda b: spoken(b.vo) + " / " + b.text
    if paid:
        if not re.search(d["caption_label_regex"], ctx.doc.caption, re.I):
            ctx.add("D01", "block", "relationship %s: the caption must start with an ad label (Ad, #ad, Advertisement, Reklame)" % rel,
                    quote(ctx.doc.caption, 40))
        if not early:
            ctx.add("D01", "block", "relationship %s: no beat with the %s role starts in the first %g s"
                    % (rel, d["role_token"], d["within_seconds"]))
        elif not any(paid_hits(cells(b), d) for b in early):
            ctx.add("D01", "block", "relationship %s: the disclosure beat does not say the post is paid or gifted "
                    "(ad, paid, gifted, sponsored)" % rel, quote(cells(early[0])))
        return
    brand = ctx.brand.get("brand", "")
    names = d["role_words"] + ([brand] if brand else [])
    if not early:
        ctx.add("D01", "warn", "relationship %s: no beat with the %s role starts in the first %g s; say who you are "
                "to the brand (I guide for %s)" % (rel, d["role_token"], d["within_seconds"], brand or "the brand"))
    elif not any(phrase_hits(cells(b), names) for b in early):
        ctx.add("D01", "warn", "relationship %s: the disclosure beat does not name the role (guide, staff, %s)"
                % (rel, brand or "the brand"), quote(cells(early[0])))


def paid_hits(text, d):
    """paid_words in text, minus those right after a negation in the same clause ('not an ad', 'not paid')."""
    low = re.sub(r"[-‐‑]", " ", norm(text))
    neg = d.get("paid_negation_regex")
    out = []
    for p in d["paid_words"]:
        for m in re.finditer(r"(?<![a-z0-9])%s(?![a-z0-9])" % re.escape(p.lower()), low):
            clause = re.split(r"[.,;:!?/()]", low[:m.start()])[-1]
            if not (neg and re.search(neg, clause)):
                out.append(p)
                break
    return out


def check_sound(ctx):
    """SND01: a trending song on a post that names the brand, a trip or a price."""
    snd = ctx.styles.get("sound")
    if not snd or ctx.doc.meta.get("sound") != snd["blocked_value"]:
        return
    text = " / ".join([spoken(b.vo) + " / " + b.text for b in ctx.doc.beats] + [ctx.doc.caption])
    brand = ctx.brand.get("brand", "")
    hits = []
    if brand and re.search(r"\s*".join(re.escape(w) for w in norm(brand).split()), norm(text)):
        hits.append(brand)  # also matches the joined handle or hashtag: #outdoornorway
    hits += phrase_hits(text, snd["trip_words"])
    hits += [m.group(0).strip() for m in re.finditer(snd["price_regex"], norm(text))]
    if hits:
        ctx.add("SND01", "block", "sound %s on a post that names the brand, a trip or a price; use the Commercial "
                "Music Library or original sound" % snd["blocked_value"], ", ".join(dict.fromkeys(hits)))


def scope_texts(ctx, scope):
    """(where, lowercase text, beat or None) for a brand rule scope."""
    beats = ctx.doc.beats
    item = lambda b: (b.label(), norm(PAUSE_RE.sub(" ", b.vo) + " / " + b.text), b)
    if scope == "first_beat":
        return [item(beats[0])]
    if scope == "before_cta":
        stop = ctx.cta[0].n if ctx.cta else len(beats) + 1
        return [item(b) for b in beats if b.n < stop and not b.has("soft-cta")]
    if scope == "voiceover_and_text":
        return [item(b) for b in beats]
    texts = [item(b) for b in beats] + [("caption", norm(ctx.doc.caption), None)]
    if scope == "script":
        return [("script", " \n ".join(t for _, t, _ in texts), None)]
    return texts


def negated(rule, text, m):
    """True when every guarantee word in the match is directly governed by a negation."""
    terms = list(re.finditer(rule["guarantee_regex"], m.group(0), re.I))
    neg = rule["negated_when_preceded_by"]
    return bool(terms) and all(re.search(neg, text[:m.start() + g.start()], re.I) for g in terms)


def check_brand(ctx):
    for rule in ctx.brand.get("rules", []):
        if rule.get("mode") == "final_only" and not ctx.final:
            continue
        rid, sev, msg = rule["id"], rule["severity"], rule["message"]
        texts = scope_texts(ctx, rule.get("scope", "any"))
        joined = " \n ".join(t for _, t, _ in texts)
        if "requires_regex" in rule:
            trigger = re.search(rule.get("when_regex") or rule.get("regex"), joined, re.I)
            if trigger and not re.search(rule["requires_regex"], joined, re.I):
                ctx.add(rid, sev, msg, trigger.group(0))
            continue
        for where, text, beat in texts:
            hits = [p for p in rule.get("phrases", []) if has_phrase(text, p)]
            if "regex" in rule:
                for m in re.finditer(rule["regex"], text, re.I):
                    if "guarantee_regex" in rule and negated(rule, text, m):
                        continue
                    hits.append(m.group(0))
            for sup in rule.get("superlatives", []):
                hits += superlative_hits(ctx, text, sup, beat)
            for h in hits:
                ctx.add(rid, sev, "%s: %s" % (where, msg), h)


def superlative_hits(ctx, text, sup, beat):
    """A superlative counts unless the beat cites a facts row with the same word (caption: any row)."""
    pat = r"(?<![a-z0-9#])%s(?![a-z0-9])" % re.escape(sup.lower())
    if not re.search(pat, text):
        return []
    rows = cited_rows(ctx, beat) if beat else ctx.doc.facts
    if any(re.search(pat, r.low) for r in rows):
        return []
    return [sup]


CHECKS = [check_time, check_words, check_beats, check_hook, check_facts, check_sentences,
          check_visuals, check_overlay, check_cta, check_loops, check_style, check_ugc, check_disclosure,
          check_sound, check_brand]


# ---------------------------------------------------------------- run and report

def run(doc, cfg, brand, final=False):
    ctx = Context(doc, cfg, brand, final)
    for check in CHECKS:
        check(ctx)
    return ctx


def rule_order(ctx):
    return list(RULES) + [r["id"] for r in ctx.brand.get("rules", [])]


def summary(ctx, strict=False):
    blocks = sum(1 for f in ctx.findings if f["severity"] == "block")
    warns = sum(1 for f in ctx.findings if f["severity"] == "warn")
    ok = blocks == 0 and not (strict and warns)
    return ok, blocks, warns


def as_dict(ctx, strict=False):
    ok, blocks, warns = summary(ctx, strict)
    m, t = ctx.doc.meta, ctx.t
    return {
        "tier": m["tier"], "platform": m["platform"], "narrator": m["narrator"],
        "style": ctx.style, "creator": m.get("creator"), "relationship": m.get("relationship"),
        "sound": m.get("sound"),
        "seconds": ctx.secs, "max_seconds": t["max_seconds"], "final": ctx.final,
        "beats": [{"beat": b.n, "time": "%g-%g" % (b.start, b.end), "words": b.words,
                   "est_seconds": round(b.est, 2), "numbers": len(b.number_values), "names": len(b.names),
                   "overlay_words": b.overlay_words, "shots": len(b.shots), "facts": sorted(b.units)}
                  for b in ctx.doc.beats],
        "totals": {"words": ctx.total_words, "est_seconds": round(ctx.total_est, 2),
                   "beats": len(ctx.doc.beats), "end_seconds": ctx.end,
                   "facts": len(set().union(*[b.units for b in ctx.doc.beats])),
                   "numbers": len(set().union(*[b.number_values for b in ctx.doc.beats]))},
        "findings": ctx.findings, "info": ctx.info,
        "result": "PASS" if ok else "FAIL", "blocking": blocks, "warnings": warns,
    }


def render(ctx, path, strict=False):
    d = as_dict(ctx, strict)
    style = "" if ctx.legacy else " | style %s | creator %s | relationship %s | sound %s" % (
        d["style"], d["creator"], d["relationship"], d["sound"])
    out = ["scriptcraft check: %s | tier %s | platform %s%s | narrator %s | seconds %g (tier max %g)%s"
           % (os.path.basename(path), d["tier"], d["platform"], style, d["narrator"], d["seconds"],
              d["max_seconds"], " | final" if ctx.final else "")]
    out.append("%-5s %-9s %6s %6s %8s %6s %8s %6s" % ("beat", "time", "words", "est_s", "numbers", "names", "overlay", "shots"))
    for b in d["beats"]:
        out.append("%-5d %-9s %6d %6.1f %8d %6d %8d %6d" % (b["beat"], b["time"], b["words"], b["est_seconds"],
                                                         b["numbers"], b["names"], b["overlay_words"], b["shots"]))
    tt = d["totals"]
    out.append("TOTAL words %d | est %.1f s | declared end %g s | beats %d | facts %d | numbers %d"
               % (tt["words"], tt["est_seconds"], tt["end_seconds"], tt["beats"], tt["facts"], tt["numbers"]))
    out += ["[INFO] %s" % x for x in d["info"]]
    for rid in rule_order(ctx):
        found = [f for f in ctx.findings if f["id"] == rid]
        if ctx.legacy and rid in NEW_RULES and not found:
            continue
        if not ctx.checks(rid):
            extra = STYLE_SKIP_NOTE.get(rid)
            out.append("[SKIP] %s %s (style %s only, this script is %s%s)"
                       % (rid, RULES[rid], " or ".join(STYLE_ONLY[rid]), ctx.style, ", " + extra if extra else ""))
            continue
        if not found:
            note = RULES.get(rid) or brand_note(ctx, rid)
            out.append("[PASS] %s %s" % (rid, note))
        for f in sorted(found, key=lambda f: f["severity"] != "block"):
            tag = "[FAIL]" if f["severity"] == "block" or strict else "[WARN]"
            out.append("%s %s %s%s" % (tag, rid, f["message"], (": " + f["quote"]) if f["quote"] else ""))
    if d["result"] == "PASS":
        out.append("RESULT: PASS")
    else:
        out.append("RESULT: FAIL (%d blocking, %d warnings)" % (d["blocking"], d["warnings"]))
    return "\n".join(out)


def brand_note(ctx, rid):
    if rid == "BR13" and not ctx.final:
        return "skipped (draft mode, use --final)"
    msg = next((r["message"] for r in ctx.brand.get("rules", []) if r["id"] == rid), "")
    return msg.split(". ")[0].rstrip(".").lower()


def explain(rule_id, cfg, brand):
    rid = rule_id.upper()
    for r in brand.get("rules", []):
        if r["id"] == rid:
            return "%s (%s, scope %s): %s" % (rid, r["severity"], r.get("scope", "any"), r["message"])
    if rid not in RULES:
        return None
    lines = ["%s: %s" % (rid, RULES[rid])]
    if rid in STYLE_ONLY:
        lines.append("  runs for: style %s only" % " or ".join(STYLE_ONLY[rid]))
    if rid in HELP:
        lines += ["  counts: %s" % HELP[rid][0], "  fix: %s" % HELP[rid][1]]
    styles = cfg.get("styles", {})
    keys = LIMIT_KEYS.get(rid, []) + STYLE_LIMIT_KEYS.get(rid, [])
    for tname, t in cfg["tiers"].items():
        vals = ["%s=%s" % (k, json.dumps(t[k])) for k in keys if k in t]
        if vals:
            lines.append("  %s: %s" % (tname, "; ".join(vals)))
        for sname in styles.get("allowed", []):
            over = styles.get(sname, {}).get(tname, {})
            vals = ["%s=%s" % (k, json.dumps(over[k])) for k in keys if k in over]
            if vals:
                lines.append("  %s, style %s override: %s" % (tname, sname, "; ".join(vals)))
            notes = styles.get(sname, {}).get("evidence", {})
            for k in keys:
                if k in over and "%s.%s" % (tname, k) in notes:
                    lines.append("    evidence %s.%s: %s" % (tname, k, notes["%s.%s" % (tname, k)]))
    for section, k in STYLE_KEYS.get(rid, []):
        if k in styles.get(section, {}):
            lines.append("  styles.%s.%s=%s" % (section, k, json.dumps(styles[section][k])))
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Check a scriptcraft video script.")
    ap.add_argument("file", nargs="?")
    ap.add_argument("--tier", choices=["short", "long"])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--final", action="store_true", help="placeholders and unverified facts block")
    ap.add_argument("--strict", action="store_true", help="warnings fail")
    ap.add_argument("--tiers", default=os.path.join(HERE, "tiers.json"))
    ap.add_argument("--brand", default=os.path.join(HERE, "brand_rules.json"))
    ap.add_argument("--explain", metavar="RULE_ID")
    args = ap.parse_args(argv)
    try:
        cfg, brand = load_json(args.tiers), load_json(args.brand)
        if args.explain:
            text = explain(args.explain, cfg, brand)
            print(text or "unknown rule id %s" % args.explain)
            return 0 if text else 2
        if not args.file:
            raise ParseError(0, "no script file given")
        try:
            with open(args.file, encoding="utf-8") as fh:
                text = fh.read()
        except (OSError, UnicodeDecodeError) as exc:
            raise ParseError(0, "cannot read %s: %s" % (args.file, exc))
        ctx = run(parse_document(text, cfg, args.tier), cfg, brand, args.final)
    except ParseError as exc:
        if args.json:
            print(json.dumps({"result": "PARSE", "line": exc.line, "error": exc.msg}))
        else:
            print("PARSE ERROR line %s: %s" % (exc.line, exc.msg))
        return 2
    if args.json:
        print(json.dumps(as_dict(ctx, args.strict), indent=2))
    else:
        print(render(ctx, args.file, args.strict))
    return 0 if summary(ctx, args.strict)[0] else 1


def load_json(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError) as exc:
        raise ParseError(0, "cannot read %s: %s" % (path, exc))


if __name__ == "__main__":
    sys.exit(main())
