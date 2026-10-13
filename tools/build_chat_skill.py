"""Build the claude.ai chat edition of the scriptcraft skill as a zip.

Run: python3 -I tools/build_chat_skill.py [--out PATH]
Writes dist/scriptcraft.zip (or PATH) and prints the path, the size and the
file count. Python 3 standard library only, no network.

Upload the zip in claude.ai under the skills settings. The zip holds one top
level folder, scriptcraft/, laid out like this:

    scriptcraft/SKILL.md                      tools/chat_skill/SKILL.md (chat text)
    scriptcraft/references/*.md               the 8 references, plus reviewer-rubric.md
                                              (tools/chat_skill/references/) and
                                              product-marketing.md (.claude/product-marketing.md)
    scriptcraft/assets/*, examples/*          copied from the skill folder
    scriptcraft/scripts/                      script_check.py, brand_rules.json, tiers.json
    scriptcraft/data/tours.json               campaigns/ski-meta-ads/tours.json

Left out on purpose: the validator's tests (test_script_check.py,
attack_cases.py), fixtures/, __pycache__ and *.pyc. The scripts folder is an
allowlist, so a new helper there never ships by accident. The copied folders
hold text files only (.md, .json, .py, .txt): any other type stops the build,
because the leak scan could not read it.

Source references are never edited. The built copies get the exact-string
replacements in REPLACEMENTS, then every built text file is scanned for
FORBIDDEN strings. If one survives, the build stops with a non-zero exit and
names the file, so an edit to a reference cannot leak a repo path.

script_check.py is copied byte for byte. It holds no forbidden string: its one
repo path (TOURS_FILE, near line 33) is assembled from separate path segments,
so it never matches. That default does not exist inside a zip, and only
--tour reads it, so the chat SKILL.md and the tour card command in the
references pass --tours-file data/tours.json. The builder rewrites nothing in
Python code.

The zip is deterministic: entries sorted by name, fixed timestamp, fixed
permissions. Two builds of the same sources are byte-identical.
"""

import argparse
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_SRC = ROOT / ".claude" / "skills" / "scriptcraft"
CHAT_SRC = ROOT / "tools" / "chat_skill"
TOURS_SRC = ROOT / "campaigns" / "ski-meta-ads" / "tours.json"
PRODUCT_SRC = ROOT / ".claude" / "product-marketing.md"
DEFAULT_OUT = ROOT / "dist" / "scriptcraft.zip"

TOP = "scriptcraft"
FIXED_TIME = (1980, 1, 1, 0, 0, 0)
SCRIPT_FILES = ("script_check.py", "brand_rules.json", "tiers.json")
COPIED_DIRS = ("references", "assets", "examples")
SKIP_NAMES = {"__pycache__", "fixtures", "test_script_check.py", "attack_cases.py"}
SKIP_SUFFIXES = (".pyc",)
TEXT_SUFFIXES = (".md", ".json", ".py", ".txt")

# Exact-string replacements for the built copies, applied longest first. Each
# entry is (old, new). The tour card command gets --tours-file because the
# validator's built-in tours path does not exist inside a zip. The three after
# it are the path forms the sources use. The two sentence removals drop a
# mention of a repo-only checker that does not ship.
REPLACEMENTS = [
    ("`python3 -I .claude/skills/scriptcraft/scripts/script_check.py --tour TOUR_ID`",
     "`python3 -I scripts/script_check.py --tour TOUR_ID --tours-file data/tours.json`"),
    (" Re-check with `python3 -I campaigns/ski-meta-ads/verify_tours.py`.", ""),
    (".claude/skills/scriptcraft/scripts/script_check.py", "scripts/script_check.py"),
    ("campaigns/ski-meta-ads/tours.json", "data/tours.json"),
    (".claude/product-marketing.md", "references/product-marketing.md"),
    (" and verify_tours.py checks it", ""),
]

# A built text file may hold none of these. "verify_tours" and "ski-meta-ads"
# catch a repo-only checker or folder named without the full path.
FORBIDDEN = [".claude/", "campaigns/", "tools/", "${CLAUDE_PLUGIN_ROOT}", "CLAUDE_PLUGIN_ROOT",
             "verify_tours", "ski-meta-ads"]

# Entries exempt from one needle, with the reason. script_check.py builds its
# unused default tours path from the segments "campaigns", "ski-meta-ads",
# "tours.json" (code, never rewritten). Every other needle still applies to it.
EXEMPT = {("scripts/script_check.py", "ski-meta-ads")}

DESCRIPTION_MAX = 200
SKILL_LINES_MAX = 500


class BuildError(Exception):
    pass


def apply_replacements(text):
    for old, new in sorted(REPLACEMENTS, key=lambda pair: -len(pair[0])):
        text = text.replace(old, new)
    return text


def read_source(path):
    try:
        return Path(path).read_bytes()
    except OSError as exc:
        raise BuildError("cannot read %s: %s" % (path, exc))


def is_text(name):
    return name.endswith(TEXT_SUFFIXES)


def prepare(name, data):
    """Apply the replacements to a text entry. Data stays bytes for binary entries."""
    if not is_text(name):
        return data
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise BuildError("%s is not valid UTF-8: %s" % (name, exc))
    if name.endswith("scripts/script_check.py"):
        return data  # code is never rewritten, see the module docstring
    text = apply_replacements(text)
    if name.endswith(".json"):
        try:
            json.loads(text)
        except ValueError as exc:
            raise BuildError("%s is not valid JSON after replacements: %s" % (name, exc))
    return text.encode("utf-8")


def walk(folder):
    """Files under folder as (relative posix path, Path), sorted, minus the skipped names."""
    found = []
    for path in sorted(folder.rglob("*")):
        rel = path.relative_to(folder)
        if not path.is_file():
            continue
        if any(part in SKIP_NAMES for part in rel.parts) or path.name.endswith(SKIP_SUFFIXES) or path.name.startswith("."):
            continue
        found.append((rel.as_posix(), path))
    return found


def collect():
    """The zip contents as {archive name: bytes}, before the leak check."""
    sources = {}
    sources["SKILL.md"] = CHAT_SRC / "SKILL.md"
    sources["references/reviewer-rubric.md"] = CHAT_SRC / "references" / "reviewer-rubric.md"
    sources["references/product-marketing.md"] = PRODUCT_SRC
    sources["data/tours.json"] = TOURS_SRC
    for name in SCRIPT_FILES:
        sources["scripts/" + name] = SKILL_SRC / "scripts" / name
    for folder in COPIED_DIRS:
        base = SKILL_SRC / folder
        if not base.is_dir():
            raise BuildError("missing source folder %s" % base)
        for rel, path in walk(base):
            name = "%s/%s" % (folder, rel)
            if name in sources:
                raise BuildError("duplicate entry %s" % name)
            if not is_text(name):
                raise BuildError("%s is not a text file (%s). The leak scan reads text only, so "
                                 "a binary file cannot ship. Remove it or add its type to TEXT_SUFFIXES "
                                 "in tools/build_chat_skill.py" % (path, ", ".join(TEXT_SUFFIXES)))
            sources[name] = path
    return {"%s/%s" % (TOP, name): prepare(name, read_source(path)) for name, path in sorted(sources.items())}


def check_skill_md(entries):
    data = entries[TOP + "/SKILL.md"].decode("utf-8")
    match = re.match(r"---\n(.*?)\n---\n", data, re.S)
    if not match:
        raise BuildError("SKILL.md has no front matter")
    fields = dict(re.findall(r"(?m)^([a-z-]+): (.*)$", match.group(1)))
    if fields.get("name") != TOP:
        raise BuildError("SKILL.md name must be %s, found %r" % (TOP, fields.get("name")))
    description = fields.get("description", "")
    if re.fullmatch(r"[>|][+-]?", description) or re.search(r"(?m)^description: .*\n[ \t]+\S", match.group(1)):
        raise BuildError("SKILL.md description must be one plain line, not a folded or multi-line value")
    if not description or len(description) > DESCRIPTION_MAX:
        raise BuildError("SKILL.md description must be 1 to %d characters, found %d" % (DESCRIPTION_MAX, len(description)))
    lines = data.count("\n")
    if lines >= SKILL_LINES_MAX:
        raise BuildError("SKILL.md has %d lines, the limit is under %d" % (lines, SKILL_LINES_MAX))


def check_leaks(entries):
    leaks = []
    for name, data in sorted(entries.items()):
        if not is_text(name):
            continue
        text = data.decode("utf-8")
        for needle in FORBIDDEN:
            if (name[len(TOP) + 1:], needle) in EXEMPT:
                continue
            if needle in text:
                line = text.count("\n", 0, text.index(needle)) + 1
                leaks.append("%s line %d holds %r" % (name, line, needle))
    if leaks:
        raise BuildError("a repo path survived in the built files. Add an exact-string "
                         "replacement to REPLACEMENTS in tools/build_chat_skill.py or fix the source:\n  "
                         + "\n  ".join(leaks))


def write_zip(entries, out):
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w") as archive:
        for name in sorted(entries):
            info = zipfile.ZipInfo(name, FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o644 << 16
            archive.writestr(info, entries[name], compresslevel=9)
    return out


def build(out=DEFAULT_OUT):
    """Build the zip. Returns (path, size in bytes, file count). Raises BuildError."""
    entries = collect()
    check_skill_md(entries)
    check_leaks(entries)
    path = write_zip(entries, out)
    return path, path.stat().st_size, len(entries)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build the claude.ai chat edition of scriptcraft.")
    parser.add_argument("--out", default=str(DEFAULT_OUT), help="zip path (default dist/scriptcraft.zip)")
    args = parser.parse_args(argv)
    try:
        path, size, count = build(args.out)
    except (BuildError, OSError) as exc:
        print("build_chat_skill: ERROR: %s" % exc, file=sys.stderr)
        return 1
    print("%s  %d bytes  %d files" % (path, size, count))
    return 0


if __name__ == "__main__":
    sys.exit(main())
