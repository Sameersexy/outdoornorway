"""Repo integrity checks for the commands, agents, plugin manifests and docs.

Run: python3 -I tools/test_repo_integrity.py
Stdlib only. These catch the mistakes that broke installs before: a command that
only works in a clone, a licence file that went missing, a guide that drifted
from /howto.
"""
import contextlib
import functools
import hashlib
import importlib.util
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
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


def is_umbrella(entry):
    """True for a marketplace entry whose source is the repo root, the plugin.json plugin."""
    return os.path.normpath(entry["source"]) == "."


def entry_skill_folders(entry):
    """Repo-relative posix paths of the skill folders a marketplace entry lists."""
    return [os.path.normpath(os.path.join(entry["source"], path)).replace(os.sep, "/") for path in entry.get("skills", [])]


class Manifests(unittest.TestCase):
    def setUp(self):
        self.plugin = json.loads(read(ROOT / ".claude-plugin" / "plugin.json"))
        self.market = json.loads(read(ROOT / ".claude-plugin" / "marketplace.json"))

    def test_versions_match(self):
        # The umbrella entry is the one named like plugin.json. Every entry carries the same version.
        names = [entry["name"] for entry in self.market["plugins"]]
        self.assertIn(self.plugin["name"], names)
        for entry in self.market["plugins"]:
            self.assertEqual(self.plugin["version"], entry["version"], entry["name"])

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


class Marketplace(unittest.TestCase):
    """The entries in .claude-plugin/marketplace.json and the skill folders they list."""

    REQUIRED = ("name", "source", "description", "version", "category", "license")
    SKILL_BASES = (".claude/skills", "account-skills")

    def setUp(self):
        self.market = json.loads(read(ROOT / ".claude-plugin" / "marketplace.json"))
        self.plugin = json.loads(read(ROOT / ".claude-plugin" / "plugin.json"))
        self.package = json.loads(read(ROOT / "package.json"))
        self.entries = self.market["plugins"]

    def entry(self, name):
        found = [entry for entry in self.entries if entry["name"] == name]
        self.assertEqual(len(found), 1, name)
        return found[0]

    def folder_names(self, base):
        return sorted(path.name for path in (ROOT / base).iterdir() if path.is_dir())

    def test_marketplace_name_and_owner(self):
        # Every install line ends in @outdoornorway.
        self.assertEqual(self.market["name"], "outdoornorway")
        self.assertTrue(self.market["owner"]["name"].strip())
        self.assertTrue(self.entries)

    def test_entry_names_are_unique(self):
        names = [entry["name"] for entry in self.entries]
        self.assertEqual(len(names), len(set(names)), names)

    def test_entries_have_the_required_fields(self):
        for entry in self.entries:
            for field in self.REQUIRED:
                value = entry.get(field)
                self.assertTrue(isinstance(value, str) and value.strip(), f"{entry.get('name')}: {field}")

    def test_every_version_equals_package_json(self):
        for entry in self.entries:
            self.assertEqual(self.package["version"], entry["version"], entry["name"])

    def test_the_umbrella_entry_is_the_root_plugin(self):
        umbrella = self.entry(self.plugin["name"])
        self.assertTrue(is_umbrella(umbrella))
        self.assertEqual([entry["name"] for entry in self.entries if is_umbrella(entry)], [self.plugin["name"]])

    def test_no_entry_combines_the_root_source_with_strict_false(self):
        # Claude Code refuses it ("conflicting manifests") although claude plugin validate passes.
        for entry in self.entries:
            if is_umbrella(entry):
                self.assertIsNot(entry.get("strict"), False, entry["name"])

    def test_sources_are_folders_inside_the_repo(self):
        for entry in self.entries:
            self.assertTrue(entry["source"].startswith("./"), entry["name"])
            folder = (ROOT / entry["source"]).resolve()
            self.assertTrue(folder == ROOT or ROOT in folder.parents, entry["name"])
            self.assertTrue(folder.is_dir(), f"{entry['name']}: {entry['source']}")

    def test_every_listed_skill_has_a_skill_md_whose_name_matches_its_folder(self):
        for entry in self.entries:
            source = (ROOT / entry["source"]).resolve()
            for path in entry.get("skills", []):
                label = f"{entry['name']}: {path}"
                self.assertTrue(path.startswith("./"), label)
                folder = (source / path).resolve()
                self.assertIn(source, folder.parents, label)
                self.assertTrue((folder / "SKILL.md").is_file(), label)
                meta = frontmatter(read(folder / "SKILL.md"))
                self.assertRegex(meta, rf"(?m)^name: {re.escape(folder.name)}$", label)

    def test_copy_skills_lists_the_skill_folders_except_scriptcraft(self):
        want = [name for name in self.folder_names(".claude/skills") if name != "scriptcraft"]
        listed = sorted(Path(path).name for path in self.entry("outdoornorway-copy-skills")["skills"])
        self.assertEqual(listed, want)

    def test_account_skills_lists_the_account_skills_folders(self):
        listed = sorted(Path(path).name for path in self.entry("outdoornorway-account-skills")["skills"])
        self.assertEqual(listed, self.folder_names("account-skills"))

    def test_every_skill_folder_is_in_exactly_one_non_umbrella_entry(self):
        owners = {}
        for entry in self.entries:
            if not is_umbrella(entry):
                for folder in entry_skill_folders(entry):
                    owners.setdefault(folder, []).append(entry["name"])
        for base in self.SKILL_BASES:
            for name in self.folder_names(base):
                found = owners.pop(f"{base}/{name}", [])
                if name == "scriptcraft":
                    # It needs the validator and tours.json, so it ships in the umbrella plugin only.
                    self.assertEqual(found, [], "scriptcraft is plugin only")
                else:
                    self.assertEqual(len(found), 1, f"{base}/{name} is listed by {found}")
        self.assertEqual(owners, {}, "entries list folders that are not skill folders")


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
            # /howto is skipped by name. It copies the guide's Quick start and cites docs/getting-started.md.
            # The exemption is also written in CONTRIBUTING.md under Commands and agents.
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


class RunsLauncher:
    """Mixin: run tools/outdoornorway-cli.js with node, or skip the test when node is missing."""

    def run_cli(self, *args, env=None, cwd=None, root=None):
        node = shutil.which("node")
        if node is None:
            self.skipTest("node is not installed")
        script = (root or ROOT) / json.loads(read(ROOT / "package.json"))["bin"]["outdoornorway"]
        # A marketplace source set in the shell must not change what the tests expect.
        merged = {key: value for key, value in os.environ.items() if key != "OUTDOORNORWAY_MARKETPLACE"}
        merged.update(env or {})
        return subprocess.run([node, str(script), *args], capture_output=True, text=True, timeout=120, cwd=cwd, env=merged)


class Packaging(RunsLauncher, unittest.TestCase):
    """package.json and the npx launcher (tools/outdoornorway-cli.js)."""

    def setUp(self):
        self.package = json.loads(read(ROOT / "package.json"))
        self.plugin = json.loads(read(ROOT / ".claude-plugin" / "plugin.json"))
        self.market = json.loads(read(ROOT / ".claude-plugin" / "marketplace.json"))

    def test_package_version_and_name_match_the_plugin(self):
        self.assertEqual(self.package["version"], self.plugin["version"])
        for entry in self.market["plugins"]:
            self.assertEqual(self.package["version"], entry["version"], entry["name"])
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

    def test_files_list_ships_the_folders_every_marketplace_source_needs(self):
        shipped = [entry.rstrip("/") for entry in self.package["files"] if not entry.startswith("!")]
        self.assertIn("account-skills", shipped)
        self.assertIn("tools", shipped)
        for entry in self.market["plugins"]:
            top = os.path.normpath(entry["source"]).split(os.sep)[0]
            if top != ".":
                self.assertIn(top, shipped, entry["name"])

    def test_gitignore_keeps_the_skill_zips_out_of_git(self):
        if not (ROOT / ".gitignore").exists():
            self.skipTest("no .gitignore here (an npm pack or npx copy does not ship one)")
        lines = [line.strip() for line in read(ROOT / ".gitignore").splitlines()]
        self.assertIn("dist/", lines)

    def test_npm_scripts_call_the_launcher(self):
        for script, tail in (("doctor", "doctor"), ("list", "list"), ("pack", "skills pack"), ("test", "test")):
            self.assertEqual(self.package["scripts"][script], f"node {self.package['bin']['outdoornorway']} {tail}", script)

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


class Launcher(RunsLauncher, unittest.TestCase):
    """What the npx launcher prints and runs. A fake claude on PATH records calls, so Claude Code never starts."""

    def setUp(self):
        self.market = json.loads(read(ROOT / ".claude-plugin" / "marketplace.json"))
        self.default = json.loads(read(ROOT / ".claude-plugin" / "plugin.json"))["name"]
        self.names = [entry["name"] for entry in self.market["plugins"]]
        self.overlap = "outdoornorway-copy-skills"

    def fake_claude(self, add_message=""):
        """Put a fake claude first on PATH. Returns (env, log file). Each call is appended to the log.

        With add_message set, "claude plugin marketplace add" prints it and exits 1."""
        if os.name == "nt":
            self.skipTest("the fake claude is a shell script")
        folder = tempfile.mkdtemp()
        self.addCleanup(shutil.rmtree, folder, True)
        log = Path(folder) / "calls.log"
        script = Path(folder) / "claude"
        script.write_text(
            "#!/bin/sh\n"
            'echo "$*" >> "$FAKE_CLAUDE_LOG"\n'
            'if [ "$1 $2 $3" = "plugin marketplace add" ] && [ -n "$FAKE_CLAUDE_ADD_MESSAGE" ]; then\n'
            '  echo "$FAKE_CLAUDE_ADD_MESSAGE" >&2\n'
            "  exit 1\n"
            "fi\n"
            "exit 0\n",
            encoding="utf-8",
        )
        script.chmod(0o755)
        env = {
            "PATH": folder + os.pathsep + os.environ.get("PATH", ""),
            "FAKE_CLAUDE_LOG": str(log),
            "FAKE_CLAUDE_ADD_MESSAGE": add_message,
        }
        try:
            subprocess.run([str(script), "--version"], env={**os.environ, **env}, capture_output=True, timeout=30, check=True)
        except (OSError, subprocess.SubprocessError):
            self.skipTest("a script in the temp folder cannot be run here")
        log.unlink()
        return env, log

    def calls(self, log):
        """The fake claude's calls in order, without the --version probe the launcher makes before --run."""
        if not log.exists():
            return []
        return [line for line in log.read_text(encoding="utf-8").splitlines() if line != "--version"]

    def test_list_prints_every_entry_with_its_version_and_install_line(self):
        result = self.run_cli("list")
        self.assertEqual(result.returncode, 0, result.stderr)
        for entry in self.market["plugins"]:
            self.assertIn(f"{entry['name']}  {entry['version']}", result.stdout)
            self.assertIn(entry["description"], result.stdout)
            self.assertIn(f"claude plugin install {entry['name']}@{self.market['name']}", result.stdout)

    def test_install_prints_the_default_steps_and_runs_nothing(self):
        env, log = self.fake_claude()
        result = self.run_cli("install", env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("claude plugin marketplace add Sameersexy/outdoornorway", result.stdout)
        self.assertIn(f"claude plugin install {self.default}@outdoornorway", result.stdout)
        self.assertIn("were not run", result.stdout)
        for name in self.names:
            if name != self.default:
                self.assertNotIn(f"claude plugin install {name}@", result.stdout)
        self.assertFalse(log.exists(), "install without --run called claude")

    def test_install_all_skips_the_plugin_the_umbrella_already_carries(self):
        env, log = self.fake_claude()
        result = self.run_cli("install", "all", env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.count("claude plugin marketplace add"), 1)
        self.assertEqual(len(re.findall(r"^  claude plugin install ", result.stdout, re.M)), len(self.names) - 1)
        for name in self.names:
            if name != self.overlap:
                self.assertIn(f"claude plugin install {name}@outdoornorway", result.stdout)
        self.assertNotIn(f"claude plugin install {self.overlap}@", result.stdout)
        self.assertIn("Left out: " + self.overlap, result.stdout)
        self.assertIn("listed twice", result.stdout)
        self.assertIn("were not run", result.stdout)
        self.assertFalse(log.exists(), "install all without --run called claude")

    def test_update_prints_the_marketplace_refresh_then_one_update_per_entry(self):
        env, log = self.fake_claude()
        result = self.run_cli("update", "all", env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("claude plugin marketplace update outdoornorway", result.stdout)
        for name in self.names:
            self.assertIn(f"claude plugin update {name}@outdoornorway", result.stdout)
        self.assertIn("were not run", result.stdout)
        self.assertFalse(log.exists(), "update without --run called claude")

    def test_an_unknown_name_exits_1_and_lists_the_valid_names(self):
        env, log = self.fake_claude()
        result = self.run_cli("install", "bogus", env=env)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Unknown plugin: bogus", result.stderr)
        for name in self.names + ["all"]:
            self.assertIn(name, result.stderr)
        self.assertFalse(log.exists())

    def test_bad_usage_exits_1_and_runs_nothing(self):
        env, log = self.fake_claude()
        for args in (
            ("install", "all", "bogus"),
            ("install", "--bad"),
            ("update", "bogus"),
            ("skills",),
            ("skills", "bogus"),
            ("no-such-command",),
        ):
            with self.subTest(args=args):
                result = self.run_cli(*args, env=env)
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertFalse(log.exists())

    def test_the_marketplace_source_can_come_from_the_environment(self):
        result = self.run_cli("install", env={"OUTDOORNORWAY_MARKETPLACE": "someone/fork"})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("claude plugin marketplace add someone/fork", result.stdout)
        self.assertIn("OUTDOORNORWAY_MARKETPLACE", result.stdout)
        self.assertNotIn("Sameersexy/outdoornorway", result.stdout)

    def test_run_calls_claude_once_per_step_in_order(self):
        env, log = self.fake_claude()
        result = self.run_cli("install", "all", "--run", env=env)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        want = ["plugin marketplace add Sameersexy/outdoornorway"] + [f"plugin install {name}@outdoornorway" for name in self.names if name != self.overlap]
        self.assertEqual(self.calls(log), want)
        result = self.run_cli("update", self.default, "--run", env=env)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.calls(log)[len(want):], ["plugin marketplace update outdoornorway", f"plugin update {self.default}@outdoornorway"])

    def test_run_treats_an_already_added_marketplace_as_done(self):
        env, log = self.fake_claude(add_message="Marketplace outdoornorway is already added")
        result = self.run_cli("install", "--run", env=env)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.calls(log), ["plugin marketplace add Sameersexy/outdoornorway", f"plugin install {self.default}@outdoornorway"])

    def test_run_stops_at_a_real_failure(self):
        env, log = self.fake_claude(add_message="network unreachable")
        result = self.run_cli("install", "--run", env=env)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertEqual(self.calls(log), ["plugin marketplace add Sameersexy/outdoornorway"])

    def test_skills_list_has_a_row_for_every_skill_folder(self):
        result = self.run_cli("skills", "list")
        self.assertEqual(result.returncode, 0, result.stderr)
        rows = {}
        for line in result.stdout.splitlines():
            if line.startswith("  "):
                columns = re.split(r"\s{2,}", line.strip())
                rows[columns[0]] = columns
        self.assertEqual(rows.pop("skill"), ["skill", "plugins", "folder", "zip"])
        folders = sorted(
            f"{base}/{path.name}"
            for base in (".claude/skills", "account-skills")
            for path in (ROOT / base).iterdir()
            if (path / "SKILL.md").is_file()
        )
        self.assertEqual(sorted(columns[2] for columns in rows.values()), folders)
        for name, columns in rows.items():
            folder = columns[2]
            owners = set()
            for entry in self.market["plugins"]:
                if (is_umbrella(entry) and folder.startswith(".claude/skills/")) or folder in entry_skill_folders(entry):
                    owners.add(entry["name"])
            self.assertEqual(set(columns[1].split(", ")), owners, name)
            self.assertEqual(columns[3], "plugin only" if name == "scriptcraft" else "zip", name)
        self.assertIn(f"can package {len(rows) - 1} of {len(rows)} skills", result.stdout)

    def test_help_names_every_command(self):
        result = self.run_cli("help")
        self.assertEqual(result.returncode, 0, result.stderr)
        for command in ("list", "install", "update", "skills list", "skills pack", "doctor", "test", "version", "OUTDOORNORWAY_MARKETPLACE"):
            self.assertIn(command, result.stdout, command)

    def test_doctor_passes_on_this_repo(self):
        if shutil.which("python3") is None:
            self.skipTest("doctor needs python3 on PATH")
        result = self.run_cli("doctor")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertNotIn("[fail]", result.stdout)
        self.assertIn("All required checks passed", result.stdout)
        for name in self.names:
            self.assertIn(name, result.stdout)

    def fake_repo(self):
        """A small stand-in repo with a copy of the launcher, for doctor runs that must fail."""
        root = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, root, True)
        for name in ("tools/outdoornorway-cli.js", "package.json", ".claude-plugin/plugin.json"):
            (root / name).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(ROOT / name, root / name)
        for name in (".claude/commands", ".claude/agents"):
            (root / name).mkdir(parents=True)
        (root / "campaigns" / "ski-meta-ads").mkdir(parents=True)
        (root / "campaigns" / "ski-meta-ads" / "tours.json").write_text("{}", encoding="utf-8")
        for folder in (".claude/skills/scriptcraft", ".claude/skills/humanizer", "account-skills/script-writing"):
            (root / folder).mkdir(parents=True)
            (root / folder / "SKILL.md").write_text(f"---\nname: {Path(folder).name}\ndescription: Stand-in.\n---\n", encoding="utf-8")
        return root

    def write_market(self, root, plugins):
        (root / ".claude-plugin" / "marketplace.json").write_text(
            json.dumps({"name": "outdoornorway", "owner": {"name": "Test"}, "plugins": plugins}), encoding="utf-8"
        )

    def test_doctor_fails_on_a_broken_marketplace_entry_and_does_not_crash(self):
        if shutil.which("python3") is None:
            self.skipTest("doctor needs python3 on PATH")
        version = json.loads(read(ROOT / "package.json"))["version"]
        umbrella = {"name": self.default, "source": "./", "description": "Umbrella.", "version": version}
        copy = {"name": "copy-skills", "source": "./.claude/skills", "strict": False, "description": "Copy.", "version": version, "skills": ["./humanizer"]}
        cases = {
            "a version that differs from package.json": ({**copy, "version": "9.9.9"}, "does not match package.json"),
            "source ./ with strict false and a skills list": ({**umbrella, "name": "root-copy", "strict": False, "skills": ["./.claude/skills/humanizer"]}, "conflicts"),
            "a source folder that is missing": ({**copy, "source": "./missing"}, "does not exist"),
            "a source outside the repo": ({**copy, "source": "../outside"}, "outside the repo"),
            "a skills path with no SKILL.md": ({**copy, "skills": ["./nothing"]}, "has no SKILL.md"),
            "a skill whose name differs from its folder": ({**copy, "skills": ["./scriptcraft"]}, "not scriptcraft"),
        }
        root = self.fake_repo()
        (root / ".claude" / "skills" / "scriptcraft" / "SKILL.md").write_text("---\nname: other\n---\n", encoding="utf-8")
        self.write_market(root, [umbrella, copy])
        good = self.run_cli("doctor", root=root)
        self.assertEqual(good.returncode, 0, "the stand-in repo must pass first: " + good.stdout)
        for label, (entry, expected) in cases.items():
            with self.subTest(label):
                self.write_market(root, [umbrella, entry])
                result = self.run_cli("doctor", root=root)
                self.assertEqual(result.returncode, 1, result.stdout)
                self.assertRegex(result.stdout, rf"\[fail\].*{expected}")
                self.assertNotIn("at Object", result.stderr)
        with self.subTest("a name used twice"):
            self.write_market(root, [umbrella, umbrella])
            result = self.run_cli("doctor", root=root)
            self.assertEqual(result.returncode, 1, result.stdout)
            self.assertIn("used twice", result.stdout)
        with self.subTest("no marketplace file"):
            (root / ".claude-plugin" / "marketplace.json").unlink()
            result = self.run_cli("doctor", root=root)
            self.assertEqual(result.returncode, 1, result.stdout)
            self.assertIn("could not read .claude-plugin/marketplace.json", result.stdout)
            self.assertNotIn("at Object", result.stderr)


PACKER = ROOT / "tools" / "pack_skills.py"


class Packer(RunsLauncher, unittest.TestCase):
    """tools/pack_skills.py: one zip per skill, the same bytes every run, nothing written outside --out."""

    BASES = ("account-skills", ".claude/skills")

    def pack(self, *args, cwd=None, packer=PACKER):
        return subprocess.run([sys.executable, "-I", str(packer), *args], capture_output=True, text=True, timeout=120, cwd=cwd)

    def temp(self):
        folder = Path(tempfile.mkdtemp()).resolve()
        self.addCleanup(shutil.rmtree, folder, True)
        return folder

    def packable(self):
        """Names of the skill folders the packer should pick up."""
        return sorted(
            path.name
            for base in self.BASES
            for path in (ROOT / base).iterdir()
            if (path / "SKILL.md").is_file() and path.name != "scriptcraft"
        )

    def repo_snapshot(self):
        """Every path in the repo outside .git, to prove a run created nothing there."""
        found = set()
        for folder, names, files in os.walk(ROOT):
            names[:] = [name for name in names if name != ".git"]
            found.update(os.path.join(folder, name) for name in names + files)
        return found

    def skill_digests(self):
        return {
            str(path): hashlib.sha256(path.read_bytes()).hexdigest()
            for base in self.BASES
            for path in sorted((ROOT / base).rglob("*"))
            if path.is_file()
        }

    def test_two_runs_give_identical_bytes(self):
        first, second = self.temp() / "a", self.temp() / "b"
        for out in (first, second):
            result = self.pack("--out", str(out))
            self.assertEqual(result.returncode, 0, result.stderr)
        zips = sorted(path.name for path in first.iterdir())
        self.assertEqual(zips, [name + ".zip" for name in self.packable()])
        self.assertEqual(zips, sorted(path.name for path in second.iterdir()))
        for name in zips:
            self.assertEqual((first / name).read_bytes(), (second / name).read_bytes(), name)

    def test_each_zip_holds_the_skill_under_one_top_folder_with_fixed_metadata(self):
        out = self.temp() / "zips"
        self.assertEqual(self.pack("--out", str(out)).returncode, 0)
        for name in self.packable():
            source = next(ROOT / base / name for base in self.BASES if (ROOT / base / name).is_dir())
            with zipfile.ZipFile(out / f"{name}.zip") as archive:
                self.assertIsNone(archive.testzip(), name)
                names = archive.namelist()
                self.assertEqual(names, sorted(names), name)
                self.assertIn(f"{name}/SKILL.md", names)
                self.assertEqual(archive.read(f"{name}/SKILL.md"), (source / "SKILL.md").read_bytes(), name)
                for info in archive.infolist():
                    self.assertTrue(info.filename.startswith(f"{name}/"), info.filename)
                    self.assertNotRegex(info.filename, r"__pycache__|\.pyc$|\.DS_Store")
                    self.assertEqual(info.date_time, (1980, 1, 1, 0, 0, 0), info.filename)
                    self.assertEqual((info.external_attr >> 16) & 0o777, 0o644, info.filename)
                    self.assertEqual(info.compress_type, zipfile.ZIP_DEFLATED, info.filename)

    def test_scriptcraft_is_left_out_and_cannot_be_asked_for(self):
        out = self.temp() / "zips"
        self.assertEqual(self.pack("--out", str(out)).returncode, 0)
        self.assertFalse((out / "scriptcraft.zip").exists())
        listing = self.pack("--list")
        self.assertEqual(listing.returncode, 0, listing.stderr)
        self.assertNotIn("scriptcraft", listing.stdout)
        asked = self.pack("--out", str(self.temp() / "other"), "scriptcraft")
        self.assertEqual(asked.returncode, 1)
        self.assertIn("plugin only", asked.stderr)

    def test_an_unknown_name_exits_1_and_writes_nothing(self):
        for names in (["nonesuch"], ["humanizer", "nonesuch"]):
            with self.subTest(names=names):
                out = self.temp() / "zips"
                result = self.pack("--out", str(out), *names)
                self.assertEqual(result.returncode, 1)
                self.assertIn("nonesuch", result.stderr)
                self.assertIn("Valid names", result.stderr)
                self.assertEqual(list(out.glob("*.zip")), [])

    def test_bad_usage_exits_1_not_2(self):
        for args in (["--no-such-option"], ["--out"]):
            with self.subTest(args=args):
                self.assertEqual(self.pack(*args).returncode, 1)

    def test_list_prints_names_and_folders_and_writes_nothing(self):
        out = self.temp() / "zips"
        result = self.pack("--list", "--out", str(out))
        self.assertEqual(result.returncode, 0, result.stderr)
        rows = [line.split() for line in result.stdout.splitlines()]
        self.assertEqual([row[0] for row in rows], self.packable())
        for name, folder in rows:
            self.assertTrue((ROOT / folder / "SKILL.md").is_file(), folder)
            self.assertEqual(Path(folder).name, name)
        self.assertFalse(out.exists())
        one = self.pack("--list", "humanizer")
        self.assertEqual([line.split()[0] for line in one.stdout.splitlines()], ["humanizer"])

    def test_nothing_is_written_outside_the_out_folder(self):
        before, digests = self.repo_snapshot(), self.skill_digests()
        elsewhere = self.temp()
        out = self.temp() / "zips"
        result = self.pack("--out", str(out), cwd=elsewhere)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.repo_snapshot() - before, set(), "the packer wrote inside the repo")
        self.assertEqual(self.skill_digests(), digests, "the packer changed a skill file")
        self.assertEqual(list(elsewhere.iterdir()), [], "the packer wrote into the current folder")

    def test_the_default_out_folder_is_dist_skills_in_the_current_folder(self):
        elsewhere = self.temp()
        had_dist = (ROOT / "dist").exists()
        result = self.pack("humanizer", cwd=elsewhere)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((elsewhere / "dist" / "skills" / "humanizer.zip").is_file())
        self.assertEqual((ROOT / "dist").exists(), had_dist)

    def test_the_report_has_one_line_per_zip_with_a_matching_hash(self):
        out = self.temp() / "zips"
        result = self.pack("--out", str(out))
        self.assertEqual(result.returncode, 0, result.stderr)
        lines = [line for line in result.stdout.splitlines() if " bytes  sha256 " in line]
        self.assertEqual(len(lines), len(self.packable()))
        for line in lines:
            found = re.fullmatch(r"(\S+)\s+(\d+) bytes  sha256 ([0-9a-f]{12})  description (\d+) characters(  description over 200 characters)?", line)
            self.assertIsNotNone(found, line)
            name, size, short, length, note = found.groups()
            data = (out / f"{name}.zip").read_bytes()
            self.assertEqual(int(size), len(data), name)
            self.assertEqual(short, hashlib.sha256(data).hexdigest()[:12], name)
            self.assertEqual(note is not None, int(length) > 200, name)
        self.assertIn(f"Wrote {len(lines)} zip files to {out}", result.stdout)

    def test_the_launcher_passes_its_arguments_to_the_packer(self):
        python = shutil.which("python3")
        if python is None:
            self.skipTest("the launcher needs python3 on PATH")
        direct, through = self.temp() / "direct", self.temp() / "through"
        first = subprocess.run([python, "-I", str(PACKER), "--out", str(direct), "humanizer", "social"], capture_output=True, text=True, timeout=120)
        second = self.run_cli("skills", "pack", "--out", str(through), "humanizer", "social")
        self.assertEqual((first.returncode, second.returncode), (0, 0), second.stderr)
        for name in ("humanizer", "social"):
            self.assertEqual((direct / f"{name}.zip").read_bytes(), (through / f"{name}.zip").read_bytes(), name)
        self.assertEqual(self.run_cli("skills", "pack", "--out", str(self.temp() / "x"), "nonesuch").returncode, 1)

    def stand_in_repo(self):
        """A tiny repo with its own copy of the packer, so guard rails can be tried without touching this one."""
        root = self.temp()
        (root / "tools").mkdir()
        shutil.copy(PACKER, root / "tools" / "pack_skills.py")
        for folder in ("account-skills/alpha", ".claude/skills/beta", ".claude/skills/scriptcraft"):
            (root / folder).mkdir(parents=True)
            (root / folder / "SKILL.md").write_text(f"---\nname: {Path(folder).name}\ndescription: Short.\n---\nBody.\n", encoding="utf-8")
        return root, root / "tools" / "pack_skills.py"

    def test_junk_files_are_skipped_and_nested_files_are_kept(self):
        root, packer = self.stand_in_repo()
        skill = root / "account-skills" / "alpha"
        (skill / "__pycache__").mkdir()
        (skill / "__pycache__" / "x.pyc").write_bytes(b"x")
        (skill / "stray.pyc").write_bytes(b"x")
        (skill / ".DS_Store").write_bytes(b"x")
        (skill / "references").mkdir()
        (skill / "references" / "notes.md").write_text("Notes.\n", encoding="utf-8")
        out = self.temp() / "zips"
        result = self.pack("--out", str(out), cwd=root, packer=packer)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(sorted(path.name for path in out.iterdir()), ["alpha.zip", "beta.zip"])
        with zipfile.ZipFile(out / "alpha.zip") as archive:
            self.assertEqual(archive.namelist(), ["alpha/SKILL.md", "alpha/references/notes.md"])

    def test_a_symlink_inside_a_skill_folder_exits_1(self):
        root, packer = self.stand_in_repo()
        try:
            os.symlink(root / "tools" / "pack_skills.py", root / "account-skills" / "alpha" / "link.py")
        except (OSError, NotImplementedError):
            self.skipTest("symbolic links are not available here")
        result = self.pack("--out", str(self.temp() / "zips"), cwd=root, packer=packer)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Symbolic links", result.stderr)

    def test_a_symlink_to_a_folder_inside_a_skill_folder_exits_1(self):
        root, packer = self.stand_in_repo()
        try:
            os.symlink(root / "tools", root / "account-skills" / "alpha" / "linked", target_is_directory=True)
        except (OSError, NotImplementedError):
            self.skipTest("symbolic links are not available here")
        result = self.pack("--out", str(self.temp() / "zips"), cwd=root, packer=packer)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Symbolic links", result.stderr)

    def test_an_out_folder_inside_a_skill_source_exits_1(self):
        root, packer = self.stand_in_repo()
        for inside in ("account-skills", ".claude/skills/beta/zips"):
            with self.subTest(inside=inside):
                result = self.pack("--out", str(root / inside / "out"), cwd=root, packer=packer)
                self.assertEqual(result.returncode, 1)
                self.assertFalse((root / inside / "out").exists())

    def test_two_skill_folders_with_one_name_exit_1(self):
        root, packer = self.stand_in_repo()
        (root / ".claude" / "skills" / "alpha").mkdir()
        (root / ".claude" / "skills" / "alpha" / "SKILL.md").write_text("---\nname: alpha\n---\n", encoding="utf-8")
        result = self.pack("--out", str(self.temp() / "zips"), cwd=root, packer=packer)
        self.assertEqual(result.returncode, 1)
        self.assertIn("alpha", result.stderr)


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
        if not (ROOT / ".gitignore").exists():
            self.skipTest("no .gitignore here (an npm pack or npx copy does not ship one)")
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
    """The skills in account-skills/. The umbrella plugin does not load this folder. Its own marketplace entry does."""

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

    def test_the_umbrella_plugin_does_not_load_the_folder(self):
        # plugin.json loads .claude/skills only. The folder reaches Claude Code through its own marketplace entry.
        self.assertNotIn("account-skills", read(ROOT / ".claude-plugin" / "plugin.json"))
        self.assertNotIn(ROOT / ".claude", self.FOLDER.parents)
        for folder in self.skill_folders():
            self.assertFalse((ROOT / ".claude" / "skills" / folder.name).exists(), folder.name)

    def test_the_marketplace_entry_loads_the_folder(self):
        market = json.loads(read(ROOT / ".claude-plugin" / "marketplace.json"))
        loaders = [entry for entry in market["plugins"] if entry["source"] == "./account-skills"]
        self.assertEqual([entry["name"] for entry in loaders], ["outdoornorway-account-skills"])
        for entry in market["plugins"]:
            if entry["name"] != "outdoornorway-account-skills":
                self.assertNotIn("account-skills", json.dumps(entry), entry["name"])

    def test_readme_links_every_skill_and_the_docs_point_here(self):
        readme = read(self.FOLDER / "README.md")
        for folder in self.skill_folders():
            self.assertIn(f"({folder.name}/SKILL.md)", readme, folder.name)
        for name in ("docs/README.md", "docs/repo-map.md", "docs/skills-catalog.md"):
            self.assertIn("account-skills/", read(ROOT / name), name)


if __name__ == "__main__":
    unittest.main(verbosity=1)
