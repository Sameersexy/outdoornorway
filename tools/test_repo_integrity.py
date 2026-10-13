"""Repo integrity checks for the commands, agents, plugin manifests and docs.

Run: python3 -I tools/test_repo_integrity.py
Stdlib only. These catch the mistakes that broke installs before: a command that
only works in a clone, a licence file that went missing, a guide that drifted
from /howto.
"""
import contextlib
import importlib.util
import io
import json
import re
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMMANDS = sorted((ROOT / ".claude" / "commands").glob("*.md"))
AGENTS = sorted((ROOT / ".claude" / "agents").glob("*.md"))
DASHES = re.compile("[" + chr(0x2013) + chr(0x2014) + "]")
EMOJI = re.compile("[" + chr(0x1F300) + "-" + chr(0x1FAFF) + chr(0x2600) + "-" + chr(0x27BF) + "]")
MODEL_NAMES = re.compile(r"claude[- ]?(?:opus|sonnet|haiku|fable)|\b(?:opus|sonnet|haiku|fable) ?[0-9]", re.I)
SELF = Path(__file__).resolve()
TEXT_SUFFIXES = {".md", ".json", ".py", ".txt"}


def read(path):
    return Path(path).read_text(encoding="utf-8")


def frontmatter(text):
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    return match.group(1) if match else ""


class Manifests(unittest.TestCase):
    def setUp(self):
        self.plugin = json.loads(read(ROOT / ".claude-plugin" / "plugin.json"))
        self.market = json.loads(read(ROOT / ".claude-plugin" / "marketplace.json"))

    def test_versions_match(self):
        listed = self.market["plugins"][0]
        self.assertEqual(self.plugin["version"], listed["version"])
        self.assertEqual(self.plugin["name"], listed["name"])

    def test_licence_is_mit_everywhere(self):
        self.assertEqual(self.plugin["license"], "MIT")
        licence = read(ROOT / "LICENSE")
        self.assertTrue(licence.startswith("MIT License"))
        self.assertIn("Copyright (c)", licence)

    def test_paths_exist(self):
        self.assertTrue((ROOT / self.plugin["commands"]).is_dir())
        self.assertTrue((ROOT / self.plugin["skills"]).is_dir())
        for agent in self.plugin["agents"]:
            self.assertTrue((ROOT / agent).is_file(), agent)


class Commands(unittest.TestCase):
    def test_commands_exist(self):
        names = {path.stem for path in COMMANDS}
        self.assertTrue({"script", "review-script", "validate", "open-items", "tour-data", "tokens", "howto"} <= names)

    def test_frontmatter(self):
        for path in COMMANDS:
            head = frontmatter(read(path))
            self.assertIn("description:", head, path.name)
            self.assertIn("disable-model-invocation: true", head, path.name)

    def test_no_shell_lines_with_braces(self):
        # A "!`...${VAR}...`" line is refused when the variable is not substituted
        # (a clone has no plugin root), so commands must not use them.
        for path in COMMANDS:
            for line in read(path).splitlines():
                if line.lstrip().startswith("!`") or "!`" in line:
                    self.assertNotIn("${", line, f"{path.name}: {line[:60]}")

    def test_root_note_present_when_root_used(self):
        for path in COMMANDS:
            text = read(path)
            if "ROOT/" in text:
                self.assertIn("${CLAUDE_PLUGIN_ROOT}", text, path.name)
                self.assertIn("If that text does not start with a slash", text, path.name)

    def test_script_commands_do_not_use_bare_repo_paths(self):
        # Paths under the repo must go through ROOT so the plugin install works.
        bare = re.compile(r"(?<![/\w])(?:\.claude/skills|campaigns/ski-meta-ads|tools/)")
        for path in COMMANDS:
            if path.stem == "howto":
                continue
            for number, line in enumerate(read(path).splitlines(), 1):
                if line.startswith(("description:", "argument-hint:", "allowed-tools:")):
                    continue
                for match in bare.finditer(line):
                    self.fail(f"{path.name}:{number} bare repo path: {line[:80]}")

    def test_howto_matches_the_guide(self):
        guide = read(ROOT / "docs" / "getting-started.md")
        start = guide.index("## Quick start")
        end = guide.index("## Set up (once)")
        quick = guide[start:end].rstrip() + "\n"
        self.assertTrue(read(ROOT / ".claude" / "commands" / "howto.md").endswith(quick))

    def test_commands_listed_in_guide_and_readme(self):
        guide = read(ROOT / "docs" / "getting-started.md")
        readme = read(ROOT / "README.md")
        for path in COMMANDS:
            if path.stem != "tokens":
                self.assertIn(f"`/{path.stem}", guide, f"guide: {path.stem}")
            self.assertIn(f"`/{path.stem}", readme, f"README: {path.stem}")


class Agents(unittest.TestCase):
    def test_root_note_and_no_model_pin(self):
        for path in AGENTS:
            text = read(path)
            self.assertIn("## Where files live", text, path.name)
            self.assertIn("${CLAUDE_PLUGIN_ROOT}", text, path.name)
            self.assertNotRegex(frontmatter(text), r"(?m)^model:", path.name)


class Licences(unittest.TestCase):
    def test_every_listed_third_party_skill_has_its_licence_file(self):
        table = read(ROOT / "THIRD_PARTY_SKILLS.md")
        skills = re.findall(r"^\| ([a-z-]+) \| [^|]+ \| [0-9a-f]{40} \|", table, re.M)
        self.assertGreaterEqual(len(skills), 8)
        for skill in skills:
            folder = ROOT / ".claude" / "skills" / skill
            self.assertTrue(list(folder.glob("LICENSE*")), f"{skill} has no licence file")

    def test_every_skill_folder_is_listed_or_original(self):
        table = read(ROOT / "THIRD_PARTY_SKILLS.md")
        for folder in (ROOT / ".claude" / "skills").iterdir():
            if folder.is_dir() and folder.name != "scriptcraft":
                self.assertIn(f"| {folder.name} |", table, folder.name)


def third_party_skill_names():
    table = read(ROOT / "THIRD_PARTY_SKILLS.md")
    return set(re.findall(r"^\| ([a-z-]+) \| [^|]+ \| [0-9a-f]{40} \|", table, re.M))


def tracked_text_files():
    """Every text file in the repo except this one, with the skill folder it sits in (or None)."""
    third = third_party_skill_names()
    for path in sorted(ROOT.rglob("*")):
        rel = path.relative_to(ROOT).parts
        if not path.is_file() or ".git" in rel or "__pycache__" in rel or path == SELF:
            continue
        if path.suffix not in TEXT_SUFFIXES:
            continue
        skill = rel[2] if len(rel) > 3 and rel[:2] == (".claude", "skills") and rel[2] in third else None
        yield path, skill


class Hygiene(unittest.TestCase):
    def test_no_dashes_or_emoji_in_our_own_files(self):
        # Third-party skill files keep quoted examples (lists of AI tells), see THIRD_PARTY_SKILLS.md.
        bad = []
        for path, skill in tracked_text_files():
            if skill is not None:
                continue
            text = read(path)
            if DASHES.search(text) or EMOJI.search(text):
                bad.append(str(path.relative_to(ROOT)))
        self.assertEqual(bad, [], "em or en dash, or emoji, in: " + ", ".join(bad))

    def test_no_local_scratch_paths(self):
        scratch = "/tmp/" + "claude"
        bad = [str(p.relative_to(ROOT)) for p, _ in tracked_text_files() if scratch in read(p)]
        self.assertEqual(bad, [], "local scratch path in: " + ", ".join(bad))

    def test_no_claude_model_names_anywhere(self):
        bad = [str(p.relative_to(ROOT)) for p, _ in tracked_text_files() if MODEL_NAMES.search(read(p))]
        self.assertEqual(bad, [], "model name in: " + ", ".join(bad))

    def test_no_dangling_session_references(self):
        for name in ("THIRD_PARTY_SKILLS.md", "README.md", "CLAUDE.md"):
            text = read(ROOT / name).lower()
            self.assertNotIn("session notes", text, name)
            self.assertNotIn("session research", text, name)

    def test_quick_start_stands_alone(self):
        # /howto shows only the Quick start, so it must not point at a section it does not show.
        guide = read(ROOT / "docs" / "getting-started.md")
        quick = guide[guide.index("## Quick start"):guide.index("## Set up (once)")]
        self.assertNotIn("below", quick)
        self.assertIn("Set up (once)", quick)

    def test_guide_has_no_link_placeholders_and_names_the_install_pages(self):
        guide = read(ROOT / "docs" / "getting-started.md")
        self.assertNotIn("[link:", guide)
        self.assertIn("https://code.claude.com/docs/en/quickstart", guide)
        self.assertIn("https://www.python.org/downloads/", guide)

    def test_guide_does_not_say_private(self):
        guide = read(ROOT / "docs" / "getting-started.md")
        self.assertNotIn("The repo is private", guide)
        self.assertNotIn("private repo", read(ROOT / "README.md").lower())


class TranscriptReport(unittest.TestCase):
    """tools/transcript_report.py (the /tokens command) on a small made-up session."""

    def load(self):
        spec = importlib.util.spec_from_file_location("transcript_report", ROOT / "tools" / "transcript_report.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    def session(self):
        lines = [
            {"type": "assistant", "message": {"id": "m1", "usage": {"input_tokens": 10, "cache_read_input_tokens": 1000, "cache_creation_input_tokens": 500, "output_tokens": 50}}},
            {"type": "user", "message": {"role": "user", "content": "hello"}},
            {"type": "assistant", "message": {"id": "m2", "usage": {"input_tokens": 5, "cache_read_input_tokens": 1500, "cache_creation_input_tokens": 100, "output_tokens": 20}}},
            {"type": "assistant", "message": {"id": "m2", "usage": {"input_tokens": 5, "cache_read_input_tokens": 1500, "cache_creation_input_tokens": 100, "output_tokens": 20}}},
            "not json at all",
        ]
        handle = tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False, encoding="utf-8")
        for line in lines:
            handle.write((line if isinstance(line, str) else json.dumps(line)) + "\n")
        handle.close()
        return handle.name

    def test_reports_calls_and_cache_hit_ratio_and_skips_junk_lines(self):
        module = self.load()
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            module.main(self.session())
        out = buffer.getvalue()
        self.assertIn("model calls: 2", out)  # the repeated message id counts once
        self.assertIn("hit ratio", out)
        self.assertIn("context above 150k", out)

    def test_an_image_counts_as_a_fixed_cost_not_its_base64_length(self):
        module = self.load()
        image = {"type": "image", "source": {"type": "base64", "data": "A" * 400000}}
        self.assertLess(module.size(image), 10000)


if __name__ == "__main__":
    unittest.main(verbosity=1)
