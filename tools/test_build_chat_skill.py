"""Tests for tools/build_chat_skill.py, the claude.ai chat edition of scriptcraft.

Run: python3 -I tools/test_build_chat_skill.py
Stdlib only. Builds into temp folders, never into the repo's dist/.
"""
import contextlib
import hashlib
import importlib.util
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parent.parent
SKILL_SRC = ROOT / ".claude" / "skills" / "scriptcraft"
TOURS_SRC = ROOT / "campaigns" / "ski-meta-ads" / "tours.json"
TOP = "scriptcraft"

DASHES = re.compile("[" + chr(0x2013) + chr(0x2014) + "]")
EMOJI = re.compile("[" + chr(0x1F300) + "-" + chr(0x1FAFF) + chr(0x2600) + "-" + chr(0x27BF) + "]")
MODEL_WORDS = "|".join(["op" + "us", "son" + "net", "hai" + "ku", "fa" + "ble"])
MODEL_NAMES = re.compile("claude[- ]?(?:" + MODEL_WORDS + r")|\b(?:" + MODEL_WORDS + ") ?[0-9]", re.I)
LEAKS = [".claude/", "campaigns/", "tools/", "${CLAUDE_PLUGIN_ROOT}"]
EXCLUDED = ["test_script_check.py", "attack_cases.py", "fixtures", "__pycache__", ".pyc"]
TEXT_SUFFIXES = (".md", ".json", ".py", ".txt")
SCRIPT_EXAMPLES = ["short-fictional.md", "short-ugc-talk-fictional.md", "short-ugc-text-fictional.md", "long-fictional.md"]


def load_builder():
    spec = importlib.util.spec_from_file_location("build_chat_skill", ROOT / "tools" / "build_chat_skill.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def tree_hash(paths):
    digest = hashlib.sha256()
    for base in paths:
        files = [base] if base.is_file() else sorted(p for p in base.rglob("*") if p.is_file() and "__pycache__" not in p.parts)
        for path in files:
            digest.update(str(path).encode() + path.read_bytes())
    return digest.hexdigest()


def run(args, cwd):
    return subprocess.run([sys.executable, "-I"] + [str(a) for a in args], cwd=str(cwd), capture_output=True, text=True)


class BuiltZip(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.builder = load_builder()
        cls.tmp = tempfile.TemporaryDirectory()
        base = Path(cls.tmp.name)
        cls.zip_path = base / "out" / "scriptcraft.zip"
        cls.sources_before = tree_hash([SKILL_SRC, TOURS_SRC, ROOT / ".claude" / "product-marketing.md"])
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            cls.code = cls.builder.main(["--out", str(cls.zip_path)])
        cls.stdout = buffer.getvalue()
        cls.sources_after = tree_hash([SKILL_SRC, TOURS_SRC, ROOT / ".claude" / "product-marketing.md"])
        cls.zip = zipfile.ZipFile(cls.zip_path)
        cls.names = cls.zip.namelist()
        cls.unzipped = base / "unzipped"
        cls.zip.extractall(cls.unzipped)
        cls.skill = cls.unzipped / TOP

    @classmethod
    def tearDownClass(cls):
        cls.zip.close()
        cls.tmp.cleanup()

    def text(self, name):
        return self.zip.read(TOP + "/" + name).decode("utf-8")

    def text_entries(self):
        return [(n, self.zip.read(n).decode("utf-8")) for n in self.names if n.endswith(TEXT_SUFFIXES)]

    def front_matter(self):
        match = re.match(r"---\n(.*?)\n---\n", self.text("SKILL.md"), re.S)
        self.assertIsNotNone(match, "SKILL.md has no front matter")
        return dict(re.findall(r"(?m)^([a-z-]+): (.*)$", match.group(1)))

    # Build and layout

    def test_builder_exits_zero_and_prints_path_and_size(self):
        self.assertEqual(self.code, 0)
        self.assertIn(str(self.zip_path), self.stdout)
        self.assertIn("%d bytes" % self.zip_path.stat().st_size, self.stdout)
        self.assertIn("%d files" % len(self.names), self.stdout)

    def test_top_level_is_the_skill_folder_only(self):
        self.assertEqual({n.split("/")[0] for n in self.names}, {TOP})

    def test_required_files_are_present(self):
        for name in ["SKILL.md", "data/tours.json", "references/product-marketing.md", "references/reviewer-rubric.md",
                     "scripts/script_check.py", "scripts/brand_rules.json", "scripts/tiers.json"]:
            self.assertIn(TOP + "/" + name, self.names)
        for folder in ["assets", "examples"]:
            self.assertTrue(any(n.startswith("%s/%s/" % (TOP, folder)) for n in self.names), folder)

    def test_all_eight_references_plus_rubric_and_product_context(self):
        built = {n.split("/")[-1] for n in self.names if n.startswith(TOP + "/references/")}
        source = {p.name for p in (SKILL_SRC / "references").glob("*.md")}
        self.assertEqual(len(source), 8)
        self.assertEqual(built, source | {"reviewer-rubric.md", "product-marketing.md"})

    def test_assets_and_examples_match_the_skill_folder(self):
        for folder in ["assets", "examples"]:
            built = {n.split("/")[-1] for n in self.names if n.startswith("%s/%s/" % (TOP, folder))}
            self.assertEqual(built, {p.name for p in (SKILL_SRC / folder).iterdir() if p.is_file()}, folder)

    def test_excluded_files_are_absent(self):
        for name in self.names:
            for part in EXCLUDED:
                self.assertNotIn(part, name, name)

    def test_entries_are_sorted_with_a_fixed_timestamp_and_no_directories(self):
        self.assertEqual(self.names, sorted(self.names))
        for info in self.zip.infolist():
            self.assertEqual(info.date_time, (1980, 1, 1, 0, 0, 0), info.filename)
            self.assertFalse(info.filename.endswith("/"), info.filename)

    def test_builds_are_byte_identical(self):
        again = Path(self.tmp.name) / "again.zip"
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(self.builder.main(["--out", str(again)]), 0)
        self.assertEqual(again.read_bytes(), self.zip_path.read_bytes())

    def test_building_does_not_touch_the_sources(self):
        self.assertEqual(self.sources_before, self.sources_after)

    # SKILL.md

    def test_front_matter_name_matches_the_folder(self):
        name = self.front_matter()["name"]
        self.assertEqual(name, TOP)
        self.assertRegex(name, r"^[a-z0-9-]{1,64}$")

    def test_description_is_at_most_200_characters_and_says_when_and_what(self):
        description = self.front_matter()["description"]
        self.assertTrue(0 < len(description) <= 200, len(description))
        self.assertIn("Use for", description)
        for word in ["Outdoor Norway", "Reels", "Shorts", "TikTok", "UGC", "YouTube", "script"]:
            self.assertIn(word, description)

    def test_skill_md_has_under_500_lines(self):
        self.assertLess(self.text("SKILL.md").count("\n"), 500)

    def test_skill_md_carries_the_chat_behaviour(self):
        text = self.text("SKILL.md")
        for needle in ["Pair mode", "same tour", "Code execution", "Validator: not run. This script is not validated.",
                       "--tours-file data/tours.json", "RESULT: PASS", "Variant hook:", "Variant CTA:",
                       "SHIP, REVISE or REJECT", "[VERIFY: what, who confirms]", "references/reviewer-rubric.md",
                       "--final --brief", "I write up to two scripts per request", "A pair needs one tour"]:
            self.assertIn(needle, text)

    def test_skill_md_has_no_repo_or_agent_wording(self):
        text = self.text("SKILL.md")
        self.assertNotRegex(text, r"\bROOT\b")
        for needle in ["script-writer", "script-reviewer", "CLAUDE_PLUGIN_ROOT", "${", "campaigns", "verify_tours"]:
            self.assertNotIn(needle, text)

    def test_every_path_named_in_skill_md_exists_in_the_zip(self):
        text = self.text("SKILL.md")
        for rel in sorted(set(re.findall(r"`((?:references|assets|examples|scripts|data)/[A-Za-z0-9_./-]+)`", text))):
            if rel.endswith("/"):
                self.assertTrue(any(n.startswith(TOP + "/" + rel) for n in self.names), rel)
            elif rel.count("*") == 0 and not rel.startswith("scripts/script_check.py"):
                self.assertIn(TOP + "/" + rel, self.names, rel)

    def test_limits_table_matches_tiers_json(self):
        text = self.text("SKILL.md")
        for tier, style in [("short", "voiceover"), ("short", "ugc_talk"), ("short", "ugc_text"),
                            ("long", "voiceover"), ("long", "ugc_talk")]:
            card = run(["scripts/script_check.py", "--limits", tier, style], self.skill).stdout
            words = json.loads(re.search(r"(?m)^words: (.*)$", card).group(1))
            wps = re.search(r"(?m)^wps: (.*)$", card).group(1)
            seconds = re.search(r"(?m)^max_seconds: (.*)$", card).group(1)
            row = [l for l in text.splitlines() if l.startswith("| %s %s |" % (tier, style))]
            self.assertEqual(len(row), 1, (tier, style))
            cells = [c.strip() for c in row[0].strip("|").split("|")]
            self.assertEqual(cells[1:], [seconds, wps, "%d to %d" % (words["target_min"], words["target_max"]), str(words["hard_max"])],
                             (tier, style))

    # Reviewer rubric

    def test_rubric_has_the_ten_score_names_and_three_verdicts(self):
        text = self.text("references/reviewer-rubric.md")
        for name in ["Hook strength", "Loop quality", "Overload", "Visual hook", "Guest benefit", "Brand voice", "Facts",
                     "Sounds human", "Distinct", "Objection", "Authenticity"]:
            self.assertIn(name, text)
        for verdict in ["SHIP", "REVISE", "REJECT"]:
            self.assertIn(verdict, text)

    def test_rubric_score_names_match_the_reviewer_agent(self):
        agent = (ROOT / ".claude" / "agents" / "script-reviewer.md").read_text(encoding="utf-8")
        agent_items = re.findall(r"(?m)^\| ([A-Z][A-Za-z ]+?) \| ", agent.split("## Step 3")[1].split("Authenticity, ugc_talk")[0])
        rubric = self.text("references/reviewer-rubric.md")
        rubric_items = re.findall(r"(?m)^\| ([A-Z][A-Za-z ]+?) \| ", rubric.split("## Step 3")[1].split("Authenticity applies")[0])
        agent_items = [i for i in agent_items if i != "Item"]
        rubric_items = [i for i in rubric_items if i != "Item"]
        self.assertEqual(len(agent_items), 10)
        self.assertEqual(rubric_items, agent_items)

    # Leak and hygiene checks on every built text file

    def test_no_repo_paths_survive_in_any_built_text_file(self):
        for name, text in self.text_entries():
            for needle in LEAKS:
                self.assertNotIn(needle, text, "%s holds %s" % (name, needle))

    def test_replacements_reached_the_built_copies(self):
        self.assertIn("data/tours.json", self.text("references/short-form.md"))
        self.assertIn("references/product-marketing.md", self.text("references/short-form.md"))
        self.assertIn("data/tours.json", self.text("references/product-marketing.md"))
        self.assertIn("references/product-marketing.md", self.text("assets/creator-brief-template.md"))
        self.assertIn("references/product-marketing.md", self.text("data/tours.json"))

    def test_no_dashes_emoji_or_model_names_in_built_text_files(self):
        for name, text in self.text_entries():
            self.assertIsNone(DASHES.search(text), name + " has an em or en dash")
            self.assertIsNone(EMOJI.search(text), name + " has an emoji")
            self.assertIsNone(MODEL_NAMES.search(text), name + " names a model")

    def test_no_local_scratch_path_and_no_menu_label_marker_in_the_zip(self):
        scratch = "/tmp/" + "claude"
        for name, text in self.text_entries():
            self.assertNotIn(scratch, text, name)
            self.assertNotIn("menu label", text, name)

    def test_tours_json_is_valid_and_keeps_every_tour(self):
        built = json.loads(self.text("data/tours.json"))
        source = json.loads(TOURS_SRC.read_text(encoding="utf-8"))
        self.assertEqual(built["tours"], source["tours"])
        self.assertEqual([t["id"] for t in built["tours"]], [t["id"] for t in source["tours"]])

    def test_validator_is_byte_identical_to_the_source(self):
        self.assertEqual(self.zip.read(TOP + "/scripts/script_check.py"),
                         (SKILL_SRC / "scripts" / "script_check.py").read_bytes())

    # Commands and copies

    def command_lines(self):
        """Every python3 command the shipped text tells the model to run, as (file, command)."""
        found = []
        for name, text in self.text_entries():
            if name.endswith("scripts/script_check.py") or not name.endswith(".md"):
                continue
            for match in re.finditer(r"python3 [^`\n]*", text):
                found.append((name, match.group(0).strip()))
        return found

    def test_every_command_names_the_validator_by_its_zip_path(self):
        commands = self.command_lines()
        self.assertGreaterEqual(len(commands), 10)
        for name, command in commands:
            self.assertRegex(command, r"^python3 (-I )?scripts/script_check\.py\b", (name, command))
            if "--tour " in command:
                self.assertIn("--tours-file data/tours.json", command, (name, command))
        for name, text in self.text_entries():
            if name.endswith("scripts/script_check.py"):
                continue
            self.assertNotRegex(text, r"(?<!scripts/)script_check\.py", name)

    def test_every_command_runs_from_the_unzipped_folder(self):
        work = Path(tempfile.mkdtemp(dir=self.tmp.name)) / TOP
        shutil.copytree(self.skill, work)
        shutil.copy(self.skill / "examples" / "short-fictional.md", work / "draft-a.md")
        tour_id = json.loads(TOURS_SRC.read_text(encoding="utf-8"))["tours"][0]["id"]
        for name, command in self.command_lines():
            command = re.sub(r"\bFILE\b", "draft-a.md", command)
            command = command.replace("TOUR_ID", tour_id).replace("RULE_ID", "F01")
            args = command.split()[1:]
            if args[0] == "-I":
                args = args[1:]
            result = run(args, work)
            self.assertEqual(result.returncode, 0, (name, command, result.stdout[-300:], result.stderr[-300:]))

    def test_shipped_text_equals_the_source_after_the_replacements(self):
        for folder in ["references", "assets", "examples"]:
            for path in sorted((SKILL_SRC / folder).iterdir()):
                if not path.is_file() or not path.name.endswith(TEXT_SUFFIXES):
                    continue
                expected = self.builder.apply_replacements(path.read_text(encoding="utf-8"))
                self.assertEqual(self.text("%s/%s" % (folder, path.name)), expected, "%s/%s" % (folder, path.name))
        for name in ["tiers.json", "brand_rules.json"]:
            expected = self.builder.apply_replacements((SKILL_SRC / "scripts" / name).read_text(encoding="utf-8"))
            self.assertEqual(self.text("scripts/" + name), expected, name)

    def test_second_limits_table_and_narrator_match_tiers_json(self):
        text = self.text("SKILL.md")
        tiers = json.loads(self.text("scripts/tiers.json"))

        def card(tier, style):
            out = run(["scripts/script_check.py", "--limits", tier, style], self.skill).stdout
            return {key: json.loads(value) for key, value in re.findall(r"(?m)^(overlay|facts): (\{.*\})$", out)}

        short_voice, short_talk, long_voice = card("short", "voiceover"), card("short", "ugc_talk"), card("long", "voiceover")
        self.assertIn("| Overlay words | %d voiceover, %d ugc_talk | %d |" % (
            short_voice["overlay"]["max_words"], short_talk["overlay"]["max_words"], long_voice["overlay"]["max_words"]), text)
        self.assertIn("| Facts (numbers, names, prices, places) | %d max, " % short_voice["facts"]["per_script_max"], text)
        self.assertIn("| %d max, 2 per beat |" % long_voice["facts"]["per_script_max"], text)
        self.assertIn("| Numbers | %d max, " % short_voice["facts"]["numbers_per_script_max"], text)
        self.assertIn("| %d max, 1 per beat |" % long_voice["facts"]["numbers_per_script_max"], text)
        slow = json.dumps(tiers).count('"word_scale": 0.85')
        self.assertEqual(slow, 1)
        self.assertIn("cuts the word budget by 15 percent", text)

    # The validator inside the zip

    def draft_in_empty_folder(self, example):
        folder = Path(tempfile.mkdtemp(dir=self.tmp.name))
        shutil.copy(self.skill / "examples" / example, folder / "draft.md")
        self.assertEqual([p.name for p in folder.iterdir()], ["draft.md"])
        return folder

    def test_validator_passes_every_example_script_from_the_zip(self):
        for example in SCRIPT_EXAMPLES:
            folder = self.draft_in_empty_folder(example)
            result = run(["scripts/script_check.py", folder / "draft.md", "--brief"], self.skill)
            self.assertEqual(result.returncode, 0, example + result.stdout + result.stderr)
            self.assertIn("RESULT: PASS", result.stdout)
            final = run(["scripts/script_check.py", folder / "draft.md", "--final", "--brief"], self.skill)
            self.assertEqual(final.returncode, 0, example + final.stdout + final.stderr)
            self.assertIn("RESULT: PASS", final.stdout)

    def test_validator_runs_with_absolute_paths_from_an_empty_folder(self):
        folder = self.draft_in_empty_folder("short-ugc-text-fictional.md")
        result = run([self.skill / "scripts" / "script_check.py", "draft.md", "--tours-file",
                      self.skill / "data" / "tours.json", "--brief"], folder)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("RESULT: PASS", result.stdout)

    def test_validator_still_fails_a_bad_script(self):
        folder = Path(tempfile.mkdtemp(dir=self.tmp.name))
        shutil.copy(SKILL_SRC / "scripts" / "fixtures" / "D01.md", folder / "draft.md")
        result = run(["scripts/script_check.py", folder / "draft.md", "--tours-file", "data/tours.json", "--brief"], self.skill)
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("RESULT: FAIL", result.stdout)

    def test_tour_card_reads_the_tours_file_from_the_zip(self):
        tour_id = json.loads(TOURS_SRC.read_text(encoding="utf-8"))["tours"][0]["id"]
        result = run(["scripts/script_check.py", "--tour", tour_id, "--tours-file", "data/tours.json"], self.skill)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("card: " + tour_id, result.stdout)
        self.assertIn('"price_nok"', result.stdout)

    def test_unknown_tour_id_lists_the_ids(self):
        result = run(["scripts/script_check.py", "--tour", "no-such-tour", "--tours-file", "data/tours.json"], self.skill)
        self.assertEqual(result.returncode, 2)
        self.assertIn("ski-6day", result.stdout)

    def test_explain_and_limits_run_from_the_zip(self):
        self.assertEqual(run(["scripts/script_check.py", "--explain", "F01"], self.skill).returncode, 0)
        self.assertEqual(run(["scripts/script_check.py", "--limits", "short", "voiceover"], self.skill).returncode, 0)


class LeakCheck(unittest.TestCase):
    """A repo path in a source reference must stop the build, not ship."""

    def setUp(self):
        self.builder = load_builder()
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.skill = Path(self.tmp.name) / "scriptcraft"
        shutil.copytree(SKILL_SRC, self.skill, ignore=shutil.ignore_patterns("__pycache__", "fixtures"))
        self.out = Path(self.tmp.name) / "out" / "scriptcraft.zip"

    def build_with_leak(self, relative, line):
        target = self.skill / relative
        target.write_text(target.read_text(encoding="utf-8") + "\n" + line + "\n", encoding="utf-8")
        err = io.StringIO()
        with mock.patch.object(self.builder, "SKILL_SRC", self.skill), contextlib.redirect_stderr(err):
            code = self.builder.main(["--out", str(self.out)])
        return code, err.getvalue()

    def test_an_unlisted_repo_path_fails_the_build_and_names_the_file(self):
        code, err = self.build_with_leak("references/short-form.md", "See `.claude/other/file.md` for more.")
        self.assertEqual(code, 1)
        self.assertIn("references/short-form.md", err)
        self.assertIn(".claude/", err)
        self.assertFalse(self.out.exists())

    def test_each_forbidden_string_is_caught(self):
        for leak in ["campaigns/x", "tools/y", "${CLAUDE_PLUGIN_ROOT}/z"]:
            code, err = self.build_with_leak("assets/guide-moment-intake.md", "Open " + leak + " now.")
            self.assertEqual(code, 1, leak)
            self.assertIn("guide-moment-intake.md", err)

    def test_a_listed_path_is_rewritten_and_the_build_passes(self):
        code, err = self.build_with_leak("references/short-form.md", "Facts: `campaigns/ski-meta-ads/tours.json`.")
        self.assertEqual(code, 0, err)
        with zipfile.ZipFile(self.out) as archive:
            built = archive.read(TOP + "/references/short-form.md").decode("utf-8")
        self.assertIn("Facts: `data/tours.json`.", built)

    def test_missing_source_stops_the_build_with_a_message(self):
        (self.skill / "scripts" / "tiers.json").unlink()
        err = io.StringIO()
        with mock.patch.object(self.builder, "SKILL_SRC", self.skill), contextlib.redirect_stderr(err):
            self.assertEqual(self.builder.main(["--out", str(self.out)]), 1)
        self.assertIn("tiers.json", err.getvalue())


if __name__ == "__main__":
    unittest.main(verbosity=1)
