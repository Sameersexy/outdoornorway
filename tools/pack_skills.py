#!/usr/bin/env python3
"""Package Outdoor Norway skills as one zip per skill.

Run from the repo root:

    python3 -I tools/pack_skills.py [--out DIR] [--list] [NAME ...]

Sources are every folder with a SKILL.md under account-skills/ and .claude/skills/,
except scriptcraft, which needs the validator and tours.json and ships only in the plugin.
Each zip holds one top folder named after the skill. Two runs give identical bytes on the
same Python and zlib build: entries are sorted, timestamps are fixed at 1980-01-01 and
modes are fixed at 0644. The skill text is never changed.

Python standard library only. Output goes only to --out (default dist/skills, resolved
against the current folder).
"""

import argparse
import hashlib
import io
import json
import os
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ("account-skills", ".claude/skills")
PLUGIN_ONLY = {"scriptcraft"}
DEFAULT_OUT = "dist/skills"
SKIP_DIRS = {"__pycache__"}
SKIP_FILES = {".DS_Store"}
SKIP_SUFFIXES = (".pyc",)
FIXED_TIME = (1980, 1, 1, 0, 0, 0)
FILE_MODE = (0o100644 & 0xFFFF) << 16
UNIX = 3
# claude.ai upload limit for a skill description. [VERIFY] not confirmed, so it is a note, not an error.
DESCRIPTION_NOTE_LIMIT = 200
DESCRIPTION_NOTE = "description over %d characters" % DESCRIPTION_NOTE_LIMIT


class Parser(argparse.ArgumentParser):
    """Bad usage exits 1, to match the exit codes of the launcher."""

    def error(self, message):
        self.print_usage(sys.stderr)
        sys.stderr.write("pack_skills.py: error: %s\n" % message)
        sys.exit(1)


def find_skills():
    """Return {name: folder} for every packable skill. Exit 1 on a name clash."""
    found = {}
    for source in SOURCES:
        base = ROOT / source
        if not base.is_dir():
            continue
        for folder in sorted(base.iterdir()):
            if not folder.is_dir() or not (folder / "SKILL.md").is_file():
                continue
            if folder.name in PLUGIN_ONLY:
                continue
            if folder.name in found:
                sys.exit("Two skill folders are named %s: %s and %s" % (folder.name, found[folder.name], folder))
            found[folder.name] = folder
    return found


def relative(folder):
    return folder.relative_to(ROOT).as_posix()


def frontmatter_lines(text):
    lines = text.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    if not lines or lines[0].strip() != "---":
        return []
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return lines[1:index]
    return []


def unquote(value):
    value = value.strip()
    if len(value) >= 2 and value[0] == '"' and value[-1] == '"':
        try:
            return json.loads(value)
        except ValueError:
            return value[1:-1]
    if len(value) >= 2 and value[0] == "'" and value[-1] == "'":
        return value[1:-1].replace("''", "'")
    return value


def read_description(skill_md):
    """Return the description from the SKILL.md front matter, or None.

    Handles plain, quoted, folded (>) and literal (|) values, which is all this repo uses.
    """
    lines = frontmatter_lines(skill_md.read_text(encoding="utf-8"))
    for index, line in enumerate(lines):
        if not line.startswith("description:"):
            continue
        rest = line[len("description:"):].strip()
        block = []
        for follow in lines[index + 1:]:
            if follow.strip() == "" or follow[:1] in (" ", "\t"):
                block.append(follow.strip())
            else:
                break
        while block and block[-1] == "":
            block.pop()
        if rest[:1] in ("|", ">"):
            joiner = "\n" if rest[0] == "|" else " "
            return joiner.join(block).strip()
        if block:
            return " ".join([rest] + [piece for piece in block if piece]).strip()
        return unquote(rest)
    return None


def skill_files(folder):
    """Yield (archive name, path) for each file to pack, sorted by archive name."""
    entries = []
    for current, dirs, files in os.walk(str(folder)):
        dirs[:] = sorted(name for name in dirs if name not in SKIP_DIRS)
        for name in dirs:
            if (Path(current) / name).is_symlink():
                sys.exit("Symbolic links are not packed: %s" % (Path(current) / name))
        for name in files:
            if name in SKIP_FILES or name.endswith(SKIP_SUFFIXES):
                continue
            path = Path(current) / name
            if path.is_symlink():
                sys.exit("Symbolic links are not packed: %s" % path)
            arcname = folder.name + "/" + path.relative_to(folder).as_posix()
            entries.append((arcname, path))
    entries.sort(key=lambda pair: pair[0])
    return entries


def build_zip(folder):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        for arcname, path in skill_files(folder):
            info = zipfile.ZipInfo(arcname, date_time=FIXED_TIME)
            info.create_system = UNIX
            info.external_attr = FILE_MODE
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    return buffer.getvalue()


def out_dir_is_a_source(out):
    for source in SOURCES:
        base = (ROOT / source).resolve()
        if out == base or base in out.parents:
            return source
    return None


def main(argv):
    parser = Parser(
        prog="pack_skills.py",
        description="Package skills as one zip each. scriptcraft is plugin only and is never packed.",
    )
    parser.add_argument("names", nargs="*", metavar="NAME", help="skills to pack (default: all)")
    parser.add_argument("--out", default=DEFAULT_OUT, help="output folder (default: %s)" % DEFAULT_OUT)
    parser.add_argument("--list", action="store_true", help="print the skill names and folders, write nothing")
    args = parser.parse_args(argv)

    skills = find_skills()
    if not skills:
        sys.stderr.write("No skills found under %s.\n" % ", ".join(SOURCES))
        return 1

    unknown = [name for name in args.names if name not in skills]
    if unknown:
        for name in unknown:
            reason = "plugin only, it needs the validator and tours.json" if name in PLUGIN_ONLY else "unknown skill"
            sys.stderr.write("%s: %s\n" % (name, reason))
        sys.stderr.write("Valid names: %s\n" % ", ".join(sorted(skills)))
        return 1
    chosen = []
    for name in args.names or sorted(skills):
        if name not in chosen:
            chosen.append(name)

    if args.list:
        width = max(len(name) for name in chosen)
        for name in chosen:
            print("%s  %s" % (name.ljust(width), relative(skills[name])))
        return 0

    out = Path(args.out).expanduser().resolve()
    inside = out_dir_is_a_source(out)
    if inside:
        sys.stderr.write("--out must not be inside %s: the zips would be packed into the next run.\n" % inside)
        return 1
    if out.exists() and not out.is_dir():
        sys.stderr.write("--out is not a folder: %s\n" % out)
        return 1
    out.mkdir(parents=True, exist_ok=True)

    width = max(len(name) for name in chosen)
    over = False
    for name in chosen:
        data = build_zip(skills[name])
        (out / (name + ".zip")).write_bytes(data)
        description = read_description(skills[name] / "SKILL.md")
        if description is None:
            note = "no description found"
            length = 0
        else:
            length = len(description)
            note = DESCRIPTION_NOTE if length > DESCRIPTION_NOTE_LIMIT else ""
            over = over or bool(note)
        line = "%s  %d bytes  sha256 %s  description %d characters" % (
            name.ljust(width),
            len(data),
            hashlib.sha256(data).hexdigest()[:12],
            length,
        )
        print(line + ("  " + note if note else ""))
    print("Wrote %d zip file%s to %s" % (len(chosen), "" if len(chosen) == 1 else "s", out))
    if over:
        print("The %d character description limit for claude.ai uploads is not confirmed. Check it before you upload." % DESCRIPTION_NOTE_LIMIT)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
