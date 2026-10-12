"""Repo integrity checks for the commands, agents, plugin manifests and docs.

Run: python3 -I tools/test_repo_integrity.py
Stdlib only. These catch the mistakes that broke installs before: a command that
only works in a clone, a licence file that went missing, a guide that drifted
from /howto.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COMMANDS = sorted((ROOT / ".claude" / "commands").glob("*.md"))
AGENTS = sorted((ROOT / ".claude" / "agents").glob("*.md"))
DASHES = re.compile("[–—]")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")


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


class Hygiene(unittest.TestCase):
    FILES = [ROOT / "README.md", ROOT / "CLAUDE.md", ROOT / "docs" / "getting-started.md"] + COMMANDS + AGENTS

    def test_no_dashes_or_emoji(self):
        for path in self.FILES:
            text = read(path)
            self.assertIsNone(DASHES.search(text), f"{path.name} has an em or en dash")
            self.assertIsNone(EMOJI.search(text), f"{path.name} has an emoji")

    def test_no_local_scratch_paths_in_docs(self):
        for path in list((ROOT / "docs").rglob("*.md")) + self.FILES:
            self.assertNotIn("/tmp/claude", read(path), path.name)

    def test_no_model_names_in_tracked_text(self):
        pattern = re.compile(r"claude-(?:opus|sonnet|haiku|fable)-\d", re.I)
        for path in self.FILES:
            self.assertIsNone(pattern.search(read(path)), path.name)

    def test_guide_does_not_say_private(self):
        guide = read(ROOT / "docs" / "getting-started.md")
        self.assertNotIn("The repo is private", guide)
        self.assertNotIn("private repo", read(ROOT / "README.md").lower())


if __name__ == "__main__":
    unittest.main(verbosity=1)
