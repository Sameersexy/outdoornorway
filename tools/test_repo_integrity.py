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

    def test_repo_settings_deny_the_artifact_tool_and_keep_the_other_keys(self):
        settings = json.loads(read(ROOT / ".claude" / "settings.json"))
        self.assertEqual(settings["permissions"]["deny"], ["Artifact"])
        self.assertTrue(settings["enabledPlugins"])
        self.assertEqual(settings["autoCompactWindow"], 200000)

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


class TextFirst(unittest.TestCase):
    """/script returns text in the chat. Files only when the request ends with save."""

    def test_script_command_is_text_first(self):
        text = read(ROOT / ".claude" / "commands" / "script.md")
        self.assertIn("[save]", frontmatter(text))
        self.assertIn("Output is text in the chat", text)
        self.assertIn("ends with the word `save`", text)
        self.assertIn("Pair mode", text)

    def test_writer_agent_is_text_first(self):
        text = read(ROOT / ".claude" / "agents" / "script-writer.md")
        for needle in ("SCRATCH", "Pair mode", "### Save", "### Creator brief", "four backticks"):
            self.assertIn(needle, text, needle)
        # The only copy into the user's folder sits in the Save section.
        before_save = text[:text.index("### Save")]
        self.assertNotIn("cp SCRATCH", before_save)
        self.assertNotIn("mkdir -p content/scripts", before_save)

    def test_writer_agent_writes_files_only_on_save(self):
        text = read(ROOT / ".claude" / "agents" / "script-writer.md")
        save = text[text.index("### Save"):text.index("### Creator brief")]
        brief = text[text.index("### Creator brief"):text.index("## Style in everything you write")]
        self.assertIn("Only when the request ends with the word `save`", save)
        self.assertIn("Never overwrite a saved file", save)
        self.assertIn("slug", save)
        self.assertIn("Refuse a third script, or two different tours", text)
        # Collisions: one listing, first free name, never clobber, same name for script, notes and brief.
        self.assertIn("ls <dir>/<yyyy-mm-dd>-*", save)
        self.assertIn("first free name", save)
        self.assertIn("`<base>-2`", save)
        self.assertEqual(save.count("cp -n "), 2)
        self.assertNotRegex(save, r"cp (?!-n)")
        self.assertNotIn("never share a slug", save)
        self.assertIn("unless the request names another relative folder", save)
        self.assertIn("<dir>/<name>-brief.md", brief)
        self.assertNotRegex(brief, r"cp (?!-n)")
        # The brief may name a saved path, but only under `save`.
        self.assertIn("`save`", brief)
        # No sentence outside the Save and Creator brief sections tells the agent to write into content/scripts.
        outside = text.replace(save, "").replace(brief, "")
        self.assertNotRegex(outside, r"(?i)(write|copy|save)[^.\n]*`?content/scripts/<")

    def test_every_edition_gives_the_same_creator_brief_default(self):
        phrase = "a guide or guest will film"
        agent = read(ROOT / ".claude" / "agents" / "script-writer.md")
        skill = read(ROOT / ".claude" / "skills" / "scriptcraft" / "SKILL.md")
        chat = read(ROOT / "tools" / "chat_skill" / "SKILL.md")
        self.assertIn("any ugc script " + phrase, agent[agent.index("### Creator brief"):])
        self.assertIn("On request, or for any ugc script " + phrase, skill)
        self.assertIn("a ugc script " + phrase, chat)
        self.assertNotIn("On request only", skill)

    def test_every_script_template_carries_creator_relationship_and_sound(self):
        # The writer agent and the chat skill both say to write the three fields in every style.
        assets = ROOT / ".claude" / "skills" / "scriptcraft" / "assets"
        templates = sorted(assets.glob("script-template-*.md"))
        self.assertEqual(len(templates), 4)
        for path in templates:
            head = read(path).split("\n---\n")[0]
            for field in ("creator", "relationship", "sound"):
                self.assertRegex(head, r"(?m)^" + field + r": \[FILL", path.name)
        skill = read(ROOT / ".claude" / "skills" / "scriptcraft" / "SKILL.md")
        chat = read(ROOT / "tools" / "chat_skill" / "SKILL.md")
        self.assertIn("Every template leaves creator, relationship and sound as [FILL]", skill)
        self.assertIn("Every template leaves creator, relationship and sound as `[FILL]`", chat)
        self.assertNotIn("voiceover templates leave these three out", chat)

    def test_reviewer_asks_for_five_fixes(self):
        text = read(ROOT / ".claude" / "agents" / "script-reviewer.md")
        self.assertIn("Top five fixes", text)
        self.assertNotIn("Top three fixes", text)
        block = text[text.index("Top five fixes, in order:"):text.index("Verdict: SHIP")]
        self.assertEqual(re.findall(r"(?m)^([0-9]+)\. \.\.\.$", block), ["1", "2", "3", "4", "5"])

    def test_skill_final_output_is_text_first(self):
        text = read(ROOT / ".claude" / "skills" / "scriptcraft" / "SKILL.md")
        final = text[text.index("### 7. Final output"):]
        self.assertIn("`save`", final)

    def test_review_script_takes_pasted_text(self):
        text = read(ROOT / ".claude" / "commands" / "review-script.md")
        self.assertIn("pasted", frontmatter(text))
        self.assertIn("scratch folder", text)
        self.assertIn("without the code fence", text)
        self.assertIn("`test -f`", text)
        self.assertIn("File not found: <path>", text)
        self.assertIn("copied exactly as pasted", text)

    def test_script_command_relays_the_text_exactly_and_names_the_recheck(self):
        # The main model relays the agent's reply, so the command asks for a character-for-character copy
        # and points at /review-script, which validates the exact pasted text.
        text = read(ROOT / ".claude" / "commands" / "script.md")
        self.assertIn("copied character for character", text)
        self.assertIn("re-runs the validator on the exact text the user copied", text)

    def intake_block(self):
        text = read(ROOT / ".claude" / "skills" / "scriptcraft" / "assets" / "guide-moment-intake.md")
        section = text[text.index("## Send-ready text"):text.index("## How the script uses it")]
        blocks = re.findall(r"(?s)```\n(.*?)\n```", section)
        self.assertEqual(len(blocks), 1)
        return blocks[0]

    def test_guide_questions_come_as_one_send_ready_block_with_no_path(self):
        # A user in the chat cannot open a file, so the ten questions are printed inline.
        block = self.intake_block()
        self.assertEqual(re.findall(r"(?m)^([0-9]+)\. ", block), [str(n) for n in range(1, 11)])
        self.assertLessEqual(len(block.splitlines()), 20)
        for needle in ["ROOT", ".md", ".claude", "assets/", "/home/", "${"]:
            self.assertNotIn(needle, block)
        self.assertIn("signed release", block)

    def test_prompts_print_the_questions_and_never_point_to_the_form_file_for_the_user(self):
        command = read(ROOT / ".claude" / "commands" / "script.md")
        self.assertNotIn("guide-moment-intake", command)
        self.assertIn("ten guide questions in one fenced block", command)
        agent = read(ROOT / ".claude" / "agents" / "script-writer.md")
        contract = agent[agent.index("## Output contract"):agent.index("### Save")]
        self.assertIn("`Questions for the guide`", contract)
        self.assertIn("one fenced block", contract)
        self.assertIn("Never print the file name or a path in its place", contract)
        intake = agent[agent.index("2. Intake."):agent.index("3. Facts.")]
        self.assertNotIn("hand the guide", intake)
        chat = read(ROOT / "tools" / "chat_skill" / "SKILL.md")
        self.assertIn("`Questions for the guide`", chat)
        self.assertIn("Never print the file name or a path in its place", chat)
        self.assertNotIn("Send the guide the ten questions in", chat)

    def test_commands_that_print_to_the_user_name_no_repo_path(self):
        # ROOT/ is allowed in shell lines (python3 -I ROOT/...) and in instructions that read a file,
        # not in text the user is told to read.
        for name in ["tour-data", "tokens"]:
            text = read(ROOT / ".claude" / "commands" / (name + ".md"))
            for line in text.splitlines():
                if "ROOT/" in line:
                    self.assertTrue(line.startswith("`python3 -I ROOT/"), (name, line[:80]))
        review = read(ROOT / ".claude" / "commands" / "review-script.md")
        self.assertIn("`Script review: pasted script`", review)
        self.assertIn("never a scratch or temp path", read(ROOT / ".claude" / "agents" / "script-reviewer.md"))

    def test_script_command_does_not_name_a_saved_path_by_default(self):
        # Quick start step 5 must say text first, so /howto does not promise saved files.
        guide = read(ROOT / "docs" / "getting-started.md")
        quick = guide[guide.index("## Quick start"):guide.index("## Set up (once)")]
        self.assertIn("as text in the chat", quick)
        self.assertIn("`save`", quick)


class ResearchNotes(unittest.TestCase):
    def test_note_07_keeps_its_section_numbers_in_order(self):
        # Other notes cite "note 07 section 3", so a removed section leaves a stub and the numbers never shift.
        text = read(ROOT / "docs" / "research" / "ad-copy" / "07-outdoor-norway-voice-and-category.md")
        numbers = [int(n) for n in re.findall(r"(?m)^## ([0-9]+)\. ", text)]
        self.assertEqual(numbers, list(range(0, 13)))


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
