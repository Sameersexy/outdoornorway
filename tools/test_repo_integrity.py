"""Repo integrity checks for the commands, agents, plugin manifests and docs.

Run: python3 -I tools/test_repo_integrity.py
Stdlib only. These catch the mistakes that broke installs before: a command that
only works in a clone, a licence file that went missing, a guide that drifted
from /howto.
"""
import contextlib
import functools
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
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
TEXT_SUFFIXES = {".md", ".json", ".py", ".txt", ".js", ".mjs", ".cjs", ".yml", ".yaml", ".sh"}
SKIP_FOLDERS = {".git", "__pycache__", "node_modules"}


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


@functools.lru_cache(maxsize=None)
def tracked_texts():
    """Every text file in the repo except this one, as (path, skill folder or None, text).

    Built once per run. The folder walk skips .git and the other SKIP_FOLDERS instead of
    listing them first, and the five scans below share one read of each file."""
    third = third_party_skill_names()
    paths = []
    for folder, names, files in os.walk(ROOT):
        names[:] = [name for name in names if name not in SKIP_FOLDERS]
        for name in files:
            path = Path(folder, name)
            if name in SKIP_FOLDERS or path == SELF or path.suffix not in TEXT_SUFFIXES or not path.is_file():
                continue
            paths.append(path)
    found = []
    for path in sorted(paths):
        rel = path.relative_to(ROOT).parts
        skill = rel[2] if len(rel) > 3 and rel[:2] == (".claude", "skills") and rel[2] in third else None
        found.append((path, skill, read(path)))
    return tuple(found)


class Hygiene(unittest.TestCase):
    def test_no_dashes_or_emoji_in_our_own_files(self):
        # Third-party skill files keep quoted examples (lists of AI tells), see THIRD_PARTY_SKILLS.md.
        bad = []
        for path, skill, text in tracked_texts():
            if skill is not None:
                continue
            if DASHES.search(text) or EMOJI.search(text):
                bad.append(str(path.relative_to(ROOT)))
        self.assertEqual(bad, [], "em or en dash, or emoji, in: " + ", ".join(bad))

    def test_no_local_scratch_paths(self):
        scratch = "/tmp/" + "claude"
        bad = [str(p.relative_to(ROOT)) for p, _, text in tracked_texts() if scratch in text]
        self.assertEqual(bad, [], "local scratch path in: " + ", ".join(bad))

    def test_no_claude_model_names_anywhere(self):
        bad = [str(p.relative_to(ROOT)) for p, _, text in tracked_texts() if MODEL_NAMES.search(text)]
        self.assertEqual(bad, [], "model name in: " + ", ".join(bad))

    def test_no_gpt_model_names_in_our_own_files(self):
        # Third-party skill files keep upstream text, so they are skipped like the dash check.
        pattern = re.compile(r"\bGPT[- ]?[0-9]")
        bad = [str(p.relative_to(ROOT)) for p, skill, text in tracked_texts() if skill is None and pattern.search(text)]
        self.assertEqual(bad, [], "GPT model name in: " + ", ".join(bad))

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


def tracked_paths():
    """Repo-relative paths that git tracks. Without a git checkout (a plugin copy) it lists every file instead."""
    try:
        out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True, timeout=30).stdout
        names = [name for name in out.decode("utf-8").split("\0") if name]
        if names:
            return names
    except (OSError, subprocess.SubprocessError, UnicodeDecodeError):
        pass
    return [
        str(path.relative_to(ROOT))
        for path in ROOT.rglob("*")
        if path.is_file() and not SKIP_FOLDERS.intersection(path.relative_to(ROOT).parts)
    ]


class Packaging(unittest.TestCase):
    """package.json and the npx launcher (tools/outdoornorway-cli.js)."""

    def setUp(self):
        self.package = json.loads(read(ROOT / "package.json"))
        self.plugin = json.loads(read(ROOT / ".claude-plugin" / "plugin.json"))
        self.market = json.loads(read(ROOT / ".claude-plugin" / "marketplace.json"))

    def run_cli(self, *args):
        node = shutil.which("node")
        if node is None:
            self.skipTest("node is not installed")
        script = ROOT / self.package["bin"]["outdoornorway"]
        return subprocess.run([node, str(script), *args], capture_output=True, text=True, timeout=60)

    def test_package_version_and_name_match_the_plugin(self):
        self.assertEqual(self.package["version"], self.plugin["version"])
        self.assertEqual(self.package["version"], self.market["plugins"][0]["version"])
        self.assertEqual(self.package["name"], self.plugin["name"])
        self.assertEqual(self.package["license"], "MIT")

    def test_bin_file_exists_and_starts_with_a_node_shebang(self):
        target = ROOT / self.package["bin"]["outdoornorway"]
        self.assertTrue(target.is_file(), str(target))
        self.assertTrue(read(target).startswith("#!/usr/bin/env node\n"))

    def test_package_has_no_dependencies(self):
        for key in ("dependencies", "devDependencies", "optionalDependencies", "peerDependencies"):
            self.assertFalse(self.package.get(key), key)

    def test_files_list_points_at_real_paths(self):
        for entry in self.package["files"]:
            if entry.startswith("!"):
                continue
            self.assertTrue((ROOT / entry.rstrip("/")).exists(), f"package.json files: {entry}")

    def test_launcher_version_matches_the_package(self):
        result = self.run_cli("version")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), self.package["version"])

    def test_launcher_install_prints_the_marketplace_commands_and_runs_nothing(self):
        result = self.run_cli("install")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("claude plugin marketplace add Sameersexy/outdoornorway", result.stdout)
        self.assertIn("claude plugin install outdoornorway-marketing@outdoornorway", result.stdout)
        self.assertIn("were not run", result.stdout)

    def test_launcher_rejects_an_unknown_command(self):
        self.assertNotEqual(self.run_cli("no-such-command").returncode, 0)


class PublicRepoGuards(unittest.TestCase):
    """The repo is public. Transcripts, archives, secrets and addresses stay out."""

    def test_no_transcripts_archives_env_files_or_node_modules_are_tracked(self):
        bad = []
        for name in tracked_paths():
            parts = Path(name).parts
            base = parts[-1]
            if base.endswith((".jsonl", ".zip", ".tgz")) or base == ".env" or base.startswith(".env.") or "node_modules" in parts:
                bad.append(name)
        self.assertEqual(bad, [], "must not be committed: " + ", ".join(bad))

    def test_gitignore_blocks_the_same_files(self):
        lines = {line.strip() for line in read(ROOT / ".gitignore").splitlines()}
        for pattern in ("*.jsonl", "*.zip", "*.tgz", ".env", ".env.*", "node_modules/"):
            self.assertIn(pattern, lines, pattern)

    def test_no_email_addresses_or_secret_patterns(self):
        email = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,}")
        secrets = re.compile(
            "|".join(
                [
                    "gh" + r"[pousr]_[A-Za-z0-9]{20,}",
                    "github" + r"_pat_[A-Za-z0-9_]{20,}",
                    "sk" + r"-[A-Za-z0-9_-]{20,}",
                    "AK" + r"IA[0-9A-Z]{16}",
                    "xox" + r"[baprs]-[A-Za-z0-9-]{10,}",
                    "npm" + r"_[A-Za-z0-9]{30,}",
                    "-----BEGIN " + r"[A-Z ]*PRIVATE KEY-----",
                ]
            )
        )
        bad = []
        for path, _, text in tracked_texts():
            if email.search(text) or secrets.search(text):
                bad.append(str(path.relative_to(ROOT)))
        self.assertEqual(bad, [], "email address or secret-like text in: " + ", ".join(bad))


NAV_DOCS = [
    "README.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "adquill/README.md",
    "account-skills/README.md",
    "campaigns/ski-meta-ads/README.md",
    "content/scripts/README.md",
    "tools/README.md",
    "docs/README.md",
    "docs/repo-map.md",
    "docs/skills-catalog.md",
    "docs/installation.md",
    "docs/backup-and-restore.md",
    "docs/publishing-to-npm.md",
    "docs/script-skill-reviews/README.md",
]
REPO_PREFIXES = (".claude/", ".claude-plugin/", "docs/", "tools/", "campaigns/", "content/", "adquill/", "account-skills/")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
BACKTICKED = re.compile(r"`([^`\n]+)`")
PLACEHOLDER_CHARS = re.compile(r"[<>*{}$|\s]|\.\.\.|yyyy|slug|NN")


class Navigation(unittest.TestCase):
    """The README files and guides that help people find their way around."""

    def test_every_navigation_doc_exists(self):
        missing = [name for name in NAV_DOCS if not (ROOT / name).is_file()]
        self.assertEqual(missing, [], "missing: " + ", ".join(missing))

    def test_relative_markdown_links_resolve(self):
        bad = []
        for name in NAV_DOCS:
            path = ROOT / name
            if not path.is_file():
                continue
            for target in MARKDOWN_LINK.findall(read(path)):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                if not (path.parent / target.split("#")[0]).exists():
                    bad.append(f"{name} -> {target}")
        self.assertEqual(bad, [], "broken links: " + "; ".join(bad))

    def test_backticked_repo_paths_exist(self):
        # CHANGELOG.md records old paths on purpose, so it is skipped here.
        bad = []
        for name in NAV_DOCS:
            path = ROOT / name
            if not path.is_file() or name == "CHANGELOG.md":
                continue
            for token in BACKTICKED.findall(read(path)):
                if not token.startswith(REPO_PREFIXES) or PLACEHOLDER_CHARS.search(token):
                    continue
                if not (ROOT / token.rstrip("/")).exists():
                    bad.append(f"{name}: {token}")
        self.assertEqual(bad, [], "paths that do not exist: " + "; ".join(bad))

    def test_docs_index_lists_every_guide_and_folder(self):
        index = read(ROOT / "docs" / "README.md")
        for path in sorted((ROOT / "docs").iterdir()):
            if path.name == "README.md" or path.name.startswith("."):
                continue
            needle = path.name + "/" if path.is_dir() else path.name
            self.assertIn(needle, index, f"docs/README.md does not mention {needle}")

    def test_root_readme_points_at_the_install_and_map_docs(self):
        readme = read(ROOT / "README.md")
        for target in ("docs/README.md", "docs/installation.md", "docs/repo-map.md", "docs/backup-and-restore.md", "CONTRIBUTING.md"):
            self.assertIn(f"({target})", readme, target)

    def test_readme_has_no_hand_written_test_or_rule_counts(self):
        # Counts drift. The README shows the command that prints the live number instead.
        self.assertIsNone(re.search(r"\b\d+ (?:tests|rules)\b", read(ROOT / "README.md")))

    def test_claude_md_points_at_the_repo_map_and_keeps_its_rules(self):
        text = read(ROOT / "CLAUDE.md")
        self.assertIn("docs/repo-map.md", text)
        self.assertIn("The repo is public and MIT licensed", text)
        self.assertIn("No em or en dashes, no emojis", text)

    def test_the_retired_handoff_note_and_its_archive_are_gone(self):
        self.assertFalse((ROOT / "docs" / "handoff-next-session.md").exists())
        self.assertFalse((ROOT / "docs" / "archive").exists())

    def test_docs_claim_no_privacy_screen_and_no_private_repository(self):
        # The repo holds no record of a privacy screen, and the private backup is kept outside it.
        # CHANGELOG.md is skipped because it names the old wording when it records the removal.
        banned = ("privacy screen", "screened", "private repository")
        bad = []
        for name in NAV_DOCS:
            path = ROOT / name
            if not path.is_file() or name == "CHANGELOG.md":
                continue
            text = read(path).lower()
            bad += [f"{name}: {phrase}" for phrase in banned if phrase in text]
        self.assertEqual(bad, [], "wording the repo cannot back up: " + "; ".join(bad))


class AccountSkills(unittest.TestCase):
    """The skills in account-skills/. The plugin does not load this folder."""

    FOLDER = ROOT / "account-skills"

    def skill_folders(self):
        return sorted(path for path in self.FOLDER.iterdir() if path.is_dir())

    def test_folder_holds_only_skill_folders_and_the_readme(self):
        stray = sorted(path.name for path in self.FOLDER.iterdir() if path.is_file() and path.name != "README.md")
        self.assertEqual(stray, [], "files other than README.md: " + ", ".join(stray))
        for folder in self.skill_folders():
            files = sorted(path.name for path in folder.iterdir())
            self.assertEqual(files, ["SKILL.md"], folder.name)

    def test_each_skill_name_matches_its_folder(self):
        for folder in self.skill_folders():
            meta = frontmatter(read(folder / "SKILL.md"))
            self.assertRegex(meta, rf"(?m)^name: {re.escape(folder.name)}$", folder.name)

    def test_each_skill_has_a_description(self):
        for folder in self.skill_folders():
            meta = frontmatter(read(folder / "SKILL.md"))
            self.assertRegex(meta, r"(?m)^description: \S", folder.name)

    def test_the_plugin_does_not_load_the_folder(self):
        self.assertNotIn("account-skills", read(ROOT / ".claude-plugin" / "plugin.json"))
        self.assertNotIn(ROOT / ".claude", self.FOLDER.parents)
        for folder in self.skill_folders():
            self.assertFalse((ROOT / ".claude" / "skills" / folder.name).exists(), folder.name)

    def test_readme_links_every_skill_and_the_docs_point_here(self):
        readme = read(self.FOLDER / "README.md")
        for folder in self.skill_folders():
            self.assertIn(f"({folder.name}/SKILL.md)", readme, folder.name)
        for name in ("docs/README.md", "docs/repo-map.md", "docs/skills-catalog.md"):
            self.assertIn("account-skills/", read(ROOT / name), name)


if __name__ == "__main__":
    unittest.main(verbosity=1)
