#!/usr/bin/env python3
"""Tests for script_check.py. Run: python3 -I test_script_check.py"""

import contextlib
import io
import json
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import script_check as sc  # noqa: E402

FIX = os.path.join(HERE, "fixtures")
CFG = sc.load_json(os.path.join(HERE, "tiers.json"))
BRAND = sc.load_json(os.path.join(HERE, "brand_rules.json"))

# Each failing fixture is named after the rule it breaks (RULE or RULE-case); value is the expected severity.
EXPECT = {
    "T01": "block", "T02": "warn", "T03": "block", "T04": "block",
    "W01": "block", "W02": "warn", "W03": "warn", "B01": "warn", "B02": "warn",
    "H01": "block", "H02": "block", "H03": "warn",
    "F01": "block", "F02": "block", "F03": "block", "F04": "block", "F05": "block",
    "F06": "block", "F07": "warn", "S01": "block",
    "V01": "block", "V02": "block", "V03": "warn",
    "O01": "block", "O02": "warn", "O03": "warn", "O04": "warn",
    "C01": "block", "C02": "block", "C03": "block", "C04": "block", "C05": "warn",
    "L01": "block", "R02": "warn", "R03": "warn",
    "BR01": "block", "BR03": "block", "BR09": "block", "BR10": "block",
    "BR11": "block", "BR13": "block", "BR14": "warn",
    # Reviewer false negatives, one fixture each.
    "BR09-not-a-chance": "block", "BR09-no-question": "block", "BR09-certain": "block",
    "BR09-every-morning": "block", "BR09-every-night": "block", "BR10-chance-of-cloud": "block",
    "BR04-going-fast": "block", "BR11-world-class": "block", "BR11-uncited-row": "block",
    "F04-spelled": "block", "F04-uncited": "warn", "F07-brand-part": "warn", "F07-sentence-initial": "warn",
    "H01-hyphen-chain": "block", "C01-untagged": "warn", "C03-stacked": "warn", "C01-two-hard": "block",
    "C02-soft-early": "block", "V01-one-take-static": "warn",
}

SHORT_15 = """---
tier: short
platform: shorts
seconds: 15
title: Skins in fifteen seconds
core_takeaway: Skins let your skis climb.
---
## Facts
| id | fact | source | verified |
|---|---|---|---|
## Script
| beat | time | voiceover | visual | text | role | facts |
|---|---|---|---|---|---|---|
| 1 | 0-3 | Can your skis really climb a hill? | POV: skis gliding up a snowy slope | Skis that climb? | hook, open:A | - |
| 2 | 3-7 | A fabric skin under each ski grips the snow. | Guide fits a skin / close-up of the fibres | - | explain | - |
| 3 | 7-11 | At the top, skins come off. You ski down. | Hands rip the skins off / skier turns downhill | - | payoff, close:A | - |
| 4 | 11-15 | Ask us about a guided ski tour. | Skier glides past the camera / group at the trailhead | Guided ski tours | cta | - |
"""


def read(name):
    with open(os.path.join(FIX, name), encoding="utf-8") as fh:
        return fh.read()


def check(text, final=False, tier=None):
    return sc.run(sc.parse_document(text, CFG, tier), CFG, BRAND, final)


def found(ctx, rid, sev=None):
    return [f for f in ctx.findings if f["id"] == rid and (sev is None or f["severity"] == sev)]


def cli(*args):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = sc.main(list(args))
    return code, buf.getvalue()


def blocking(ctx):
    return [f for f in ctx.findings if f["severity"] == "block"]


class ValidFixtures(unittest.TestCase):
    def test_valid_short_passes_clean(self):
        ctx = check(read("valid-short.md"))
        self.assertEqual(ctx.findings, [])

    def test_valid_long_passes_clean(self):
        ctx = check(read("valid-long.md"))
        self.assertEqual(ctx.findings, [])

    def test_valid_short_cli_strict_exit_0(self):
        code, out = cli(os.path.join(FIX, "valid-short.md"), "--strict")
        self.assertEqual(code, 0)
        self.assertEqual(out.strip().splitlines()[-1], "RESULT: PASS")

    def test_valid_long_cli_json(self):
        code, out = cli(os.path.join(FIX, "valid-long.md"), "--json")
        data = json.loads(out)
        self.assertEqual((code, data["result"], data["blocking"], data["warnings"]), (0, "PASS", 0, 0))
        self.assertEqual(len(data["beats"]), 16)

    def test_output_has_header_table_and_rule_lines(self):
        _, out = cli(os.path.join(FIX, "valid-short.md"))
        lines = out.strip().splitlines()
        self.assertIn("tier short", lines[0])
        self.assertIn("narrator standard", lines[0])
        self.assertIn("seconds 25", lines[0])
        self.assertTrue(lines[1].startswith("beat"))
        self.assertTrue(any(x.startswith("TOTAL words 51") for x in lines))
        self.assertTrue(any(x.startswith("[PASS] T01") for x in lines))
        self.assertTrue(any(x.startswith("[PASS] BR14") for x in lines))


class FailingFixtures(unittest.TestCase):
    def test_at_least_25_failing_fixtures(self):
        names = [f[:-3] for f in os.listdir(FIX) if f.endswith(".md") and not f.startswith("valid")]
        self.assertGreaterEqual(len(names), 25)
        self.assertEqual(sorted(set(names) - {"PARSE"}), sorted(EXPECT))

    def test_parse_fixture_exits_2_with_line(self):
        code, out = cli(os.path.join(FIX, "PARSE.md"))
        self.assertEqual(code, 2)
        self.assertIn("PARSE ERROR line 18", out)

    def test_fail_final_line_format(self):
        code, out = cli(os.path.join(FIX, "C03.md"))
        self.assertEqual(code, 1)
        self.assertEqual(out.strip().splitlines()[-1], "RESULT: FAIL (1 blocking, 0 warnings)")


def make_fixture_test(name, sev):
    rid = name.split("-")[0]

    def test(self):
        final = rid == "BR13"
        ctx = check(read(name + ".md"), final=final)
        self.assertTrue(found(ctx, rid, sev), "%s expected %s, got %s" % (name, sev, ctx.findings))
        args = [os.path.join(FIX, name + ".md")] + (["--final"] if final else [])
        code, out = cli(*args)
        line = "[FAIL] " + rid if sev == "block" else "[WARN] " + rid
        self.assertIn(line, out)
        if sev == "block":
            self.assertEqual(code, 1)
        else:
            self.assertEqual(code, 0)
            self.assertEqual(cli(*(args + ["--strict"]))[0], 1)
    return test


for _rid, _sev in EXPECT.items():
    setattr(FailingFixtures, "test_fixture_%s" % _rid.replace("-", "_"), make_fixture_test(_rid, _sev))


class FalsePositives(unittest.TestCase):
    def test_your_first_tour_does_not_flag(self):
        text = read("valid-short.md").replace("You walk up, not back.", "Your first tour feels easy.")
        ctx = check(text)
        self.assertFalse(found(ctx, "BR14"))
        self.assertFalse(blocking(ctx))

    def test_the_first_is_only_a_warning(self):
        text = read("valid-short.md").replace("You walk up, not back.", "The first skins were fur.")
        ctx = check(text)
        self.assertTrue(found(ctx, "BR14", "warn"))
        self.assertFalse(blocking(ctx))

    def test_only_warns_never_blocks(self):
        ctx = check(read("BR14.md"))
        self.assertTrue(found(ctx, "BR14", "warn"))
        self.assertFalse(blocking(ctx))

    def test_superlative_allowed_when_fact_row_has_it(self):
        text = read("BR11.md").replace("| fixture data, guide estimate | yes |",
                                       "| fixture data, guide estimate | yes |\n| F3 | Skins are the best way up on skis | guide manual | yes |")
        self.assertTrue(found(check(text), "BR11", "block"))  # row exists but the beat does not cite it
        self.assertFalse(found(check(text.replace("| build | - |", "| build | F3 |")), "BR11"))

    def test_number_in_facts_table_not_double_counted(self):
        ctx = check(read("valid-short.md"))
        beat4 = ctx.doc.beats[3]
        self.assertEqual(beat4.units, {"F2"})
        self.assertEqual(beat4.number_values, {"2"})

    def test_thousands_separator_matches_spaced_fact(self):
        text = read("valid-short.md").replace("The guided climb takes about 2 hours", "A day costs NOK 1 500 and the climb takes 2 hours")
        text = text.replace("| Guided tours from Voss | cta | F1 |", "| From NOK 1,500 | cta | F2 |")
        ctx = check(text)
        self.assertFalse(found(ctx, "F04"))

    def test_spelled_one_never_counts(self):
        text = read("valid-short.md").replace("You walk up, not back.", "One step, then one more.")
        self.assertEqual(check(text).doc.beats[2].number_values, set())

    def test_spelled_number_counts_for_density_not_verification(self):
        text = read("valid-short.md").replace("You walk up, not back.", "You walk up in three steps.")
        ctx = check(text)
        self.assertEqual(ctx.doc.beats[2].number_values, {"three"})
        self.assertFalse(found(ctx, "F04"))

    def test_pause_marker_is_time_not_words(self):
        text = read("valid-short.md").replace("You ski down.", "[PAUSE 1] You ski down.")
        b = check(text).doc.beats[4]
        self.assertEqual(b.words, 8)
        self.assertAlmostEqual(b.est, 8 / 2.4 + 1, places=3)

    def test_sentence_initial_and_i_are_not_names(self):
        names = sc.proper_nouns("Voss is near. I think Bergen works. Then I'll go.", set())
        self.assertEqual(names, ["Bergen"])

    def test_adjacent_capitals_form_one_name(self):
        self.assertEqual(sc.proper_nouns("Book with Outdoor Norway today.", set()), ["Outdoor Norway"])

    def test_allowlisted_acronym_no_r02(self):
        text = read("valid-short.md").replace("| Climbing skins |", "| Prices in NOK |")
        self.assertFalse(found(check(text), "R02"))

    def test_negated_guarantee_is_not_br09(self):
        text = read("valid-short.md").replace(
            "How climbing skins work, from a guide in Voss.",
            "Stay for the northern lights. No tour can guarantee the northern lights.")
        ctx = check(text)
        self.assertFalse(found(ctx, "BR09"))
        self.assertFalse(found(ctx, "BR10"))

    def test_br09_still_catches_guarantee(self):
        text = read("valid-short.md").replace("How climbing skins work", "Snow is guaranteed")
        self.assertTrue(found(check(text), "BR09", "block"))

    def test_spaced_thousands_in_script_match_comma_row(self):
        text = read("valid-short.md").replace("| Guided tours from Voss | cta | F1 |", "| From NOK 1 950 | cta | F3 |")
        text = text.replace("Book a guided ski tour from Voss.", "Book a guided ski touring day.")
        text = text.replace("| fixture data, guide estimate | yes |",
                            "| fixture data, guide estimate | yes |\n| F3 | Day tours from NOK 1,950 per adult | fixture price list | yes |")
        ctx = check(text)
        self.assertEqual(ctx.doc.beats[5].number_values, {"1950"})
        self.assertFalse(blocking(ctx))
        self.assertFalse(found(ctx, "F04"))

    def test_placeholder_counts_as_one_word(self):
        text = read("valid-short.md").replace(
            "Slide forward and it holds.", "[VERIFY: which ski levels the lessons suit, ask the head guide] It holds.")
        ctx = check(text)
        self.assertFalse(found(ctx, "S01", "block"))
        self.assertEqual(ctx.doc.beats[2].words, 1 + 2 + 5)
        self.assertTrue(found(check(text, final=True), "BR13", "block"))

    def test_governed_negations_are_safe(self):
        for line in ("No guide can guarantee snow. You ski down.", "It doesn't always snow. You ski down.",
                     "We can't promise the aurora. You ski down.", "The aurora is never guaranteed here."):
            ctx = check(read("valid-short.md").replace("At the top, skins off. You ski down.", line))
            self.assertFalse(found(ctx, "BR09"), line)
            self.assertFalse(found(ctx, "BR10"), line)

    def test_snowshoes_every_day_is_not_a_snow_guarantee(self):
        ctx = check(read("valid-short.md").replace("You walk up, not back.", "Snowshoes every day, uncertain weather."))
        self.assertFalse(found(ctx, "BR09"))

    def test_possibility_line_satisfies_br10(self):
        ctx = check(read("valid-short.md").replace(
            "At the top, skins off. You ski down.", "There's a chance of seeing the northern lights."))
        self.assertFalse(found(ctx, "BR10"))

    def test_lesson_first_is_not_a_claim(self):
        ctx = check(read("valid-short.md").replace("| Climbing skins |", "| Lesson first |"))
        self.assertFalse(found(ctx, "BR14"))

    def test_one_take_with_motion_is_not_static(self):
        text = read("valid-short.md").replace(
            "Hands rip the skins off / first turn down the slope", "one take: POV, skins off and the first turn down")
        self.assertFalse(found(check(text), "V01"))
        self.assertTrue(found(check(text.replace("one take: POV, ", "")), "V01", "block"))

    def test_hyphens_split_words(self):
        self.assertEqual(len(sc.words("a little-bit-cold day, NOK 1,950")), 7)

    def test_spelled_compound_is_one_number(self):
        ctx = check(read("valid-short.md").replace("You walk up, not back.", "You walk up for twenty-five steps."))
        self.assertEqual(ctx.doc.beats[2].number_values, {"twenty-five"})
        self.assertTrue(found(ctx, "F04", "block"))

    def test_spelled_number_matches_digit_row(self):
        text = read("valid-short.md").replace("You walk up, not back.", "Ninety skiers walk up.")
        text = text.replace("| build | - |", "| build | F3 |").replace(
            "| fixture data, guide estimate | yes |", "| fixture data, guide estimate | yes |\n| F3 | 90 skiers a day | fixture | yes |")
        self.assertFalse(found(check(text), "F04"))

    def test_uncited_number_blocks_in_final(self):
        self.assertTrue(found(check(read("F04-uncited.md"), final=True), "F04", "block"))

    def test_caption_number_needs_a_row(self):
        ctx = check(read("valid-short.md").replace("#skitouring #voss", "Dates 12 Feb 2027. #skitouring"))
        self.assertTrue(found(ctx, "F04", "block"))

    def test_soft_cta_after_first_mini_passes(self):
        ctx = check(read("valid-long.md").replace("| ch:2, mini:2, proof |", "| ch:2, mini:2, proof, soft-cta |"))
        self.assertFalse(found(ctx, "C01"))
        self.assertFalse(found(ctx, "C02"))

    def test_silent_hold_info_line(self):
        ctx = check(read("valid-short.md").replace("A strip of fabric under each ski grips the snow.", "Skins grip."))
        self.assertTrue(any(x.startswith("beat 2:") for x in ctx.info))
        self.assertIn("[INFO] beat 2", sc.render(ctx, "x.md"))

    def test_two_hashtags_are_fine(self):
        self.assertFalse(found(check(read("valid-short.md")), "C05"))


class Budgets(unittest.TestCase):
    def test_short_15_second_script_passes_clean(self):
        ctx = check(SHORT_15)
        self.assertEqual(ctx.findings, [])
        self.assertEqual(ctx.secs, 15)

    def test_15_second_script_without_seconds_field_is_short_on_words(self):
        ctx = check(SHORT_15.replace("seconds: 15\n", ""))
        self.assertTrue(found(ctx, "W02", "warn"))

    def test_seconds_field_scales_word_budget(self):
        ctx = check(read("valid-short.md").replace("narrator: standard", "narrator: standard\nseconds: 15"))
        msg = found(ctx, "W01", "block")[0]["message"]
        self.assertIn("maximum 36", msg)
        self.assertTrue(found(ctx, "T01", "block"))

    def test_narrator_slow_scales_word_budget(self):
        text = read("valid-short.md").replace("narrator: standard", "narrator: slow")
        ctx = check(text)
        self.assertFalse(found(ctx, "W01"))
        self.assertIn("target 34 to 47", found(ctx, "W02")[0]["message"])
        ctx = check(text.replace("You ski down.", "You ski down fast."))
        self.assertIn("maximum 51", found(ctx, "W01", "block")[0]["message"])

    def test_narrator_slow_slows_estimate(self):
        fast = check(read("valid-short.md")).total_est
        slow = check(read("valid-short.md").replace("narrator: standard", "narrator: slow")).total_est
        self.assertGreater(slow, fast * 1.15)

    def test_t04_warn_band(self):
        text = read("valid-short.md").replace("grips the snow.", "grips the snow well.")
        self.assertTrue(found(check(text), "T04", "warn"))

    def test_long_hook_word_limit(self):
        text = read("valid-long.md").replace("Your skis can climb a mountain.", "Your skis can climb a whole mountain, today, slowly, and safely.")
        self.assertTrue(found(check(text), "H01", "block"))

    def test_h02_heuristic_is_a_warning(self):
        text = read("valid-short.md").replace("POV: skis gliding uphill through fresh snow", "Mountain view at dawn")
        self.assertTrue(found(check(text), "H02", "warn"))


class Structure(unittest.TestCase):
    def test_long_missing_reengage_warns(self):
        ctx = check(read("valid-long.md").replace("ch:2, reengage, open:B", "ch:2, open:B"))
        self.assertTrue(found(ctx, "L01", "warn"))
        self.assertFalse(blocking(ctx))

    def test_long_three_chapters_blocks(self):
        text = read("valid-long.md").replace("ch:4", "ch:3").replace("mini:4", "build")
        self.assertTrue(found(check(text), "L01", "block"))

    def test_long_too_many_open_loops(self):
        text = read("valid-long.md").replace("ch:2, mini:2, proof", "ch:2, mini:2, proof, open:C")
        self.assertTrue(any("loops open" in f["message"] for f in found(check(text), "L01", "block")))

    def test_short_second_loop_blocks(self):
        text = read("valid-short.md").replace("| - | build | - |", "| - | build, open:B | - |")
        self.assertTrue(found(check(text), "L01", "block"))

    def test_unverified_fact_warns_in_draft_blocks_in_final(self):
        text = read("valid-short.md").replace("guide estimate | yes |", "guide estimate | no |")
        self.assertTrue(found(check(text), "F04", "warn"))
        self.assertFalse(found(check(text), "F04", "block"))
        self.assertTrue(found(check(text, final=True), "F04", "block"))

    def test_placeholder_only_blocks_in_final(self):
        self.assertFalse(found(check(read("BR13.md")), "BR13"))
        self.assertTrue(found(check(read("BR13.md"), final=True), "BR13", "block"))

    def test_sales_verb_only_before_cta(self):
        text = read("valid-short.md").replace("Book a guided ski tour from Voss.", "Book today with a guide in Voss.")
        self.assertFalse(found(check(text), "BR07"))
        text = read("valid-short.md").replace("Slide forward and it holds.", "Book today. Slide forward.")
        self.assertTrue(found(check(text), "BR07", "warn"))

    def test_date_without_year_warns(self):
        text = read("valid-short.md").replace("How climbing skins work", "Tours start 2 Jan")
        self.assertTrue(found(check(text), "BR12", "warn"))
        text = text.replace("Tours start 2 Jan", "Tours start 2 Jan 2027")
        self.assertFalse(found(check(text), "BR12"))

    def test_em_dash_en_dash_and_emoji_block(self):
        for bad in (chr(0x2014), chr(0x2013), chr(0x1F3BF)):
            text = read("valid-short.md").replace("not back.", "not back " + bad)
            self.assertTrue(found(check(text), "R01", "block"), repr(bad))

    def test_greeting_in_beat_two_is_not_br01(self):
        text = read("valid-short.md").replace("A strip of fabric", "Welcome to a strip of fabric")
        self.assertFalse(found(check(text), "BR01"))


class Parsing(unittest.TestCase):
    def assertParseError(self, text, line=None, tier=None):
        with self.assertRaises(sc.ParseError) as cm:
            check(text, tier=tier)
        if line is not None:
            self.assertEqual(cm.exception.line, line)
        return cm.exception

    def test_escaped_pipe_inside_cell(self):
        text = read("valid-short.md").replace("guide checks the map", "sign reads A\\|B")
        ctx = check(text)
        self.assertIn("sign reads A|B", ctx.doc.beats[3].visual)
        self.assertEqual(len(ctx.doc.beats[3].shots), 2)

    def test_aligned_separator_and_spacing(self):
        text = read("valid-short.md").replace("|---|---|---|---|---|---|---|", "| :--- | :---: | --- | --- | --- | --- | ---: |")
        text = text.replace("| 2 | 3-7 |", "|   2   |  3 - 7  |")
        self.assertEqual(check(text).findings, [])

    def test_unknown_role_names_the_line(self):
        text = read("valid-short.md").replace("| build |", "| buildup |")
        line = text.splitlines().index([x for x in text.splitlines() if "| buildup |" in x][0]) + 1
        self.assertParseError(text, line)

    def test_long_only_token_in_short(self):
        self.assertParseError(read("valid-short.md").replace("| build |", "| reengage |"))

    def test_chapter_token_in_short(self):
        self.assertParseError(read("valid-short.md").replace("| build |", "| ch:1 |"))

    def test_seconds_out_of_range(self):
        self.assertParseError(read("valid-short.md").replace("narrator: standard", "seconds: 7"), 4)
        self.assertParseError(read("valid-short.md").replace("narrator: standard", "seconds: 30"))

    def test_tier_flag_mismatch(self):
        self.assertParseError(read("valid-short.md"), tier="long")

    def test_tier_flag_fills_missing_tier(self):
        ctx = check(read("valid-short.md").replace("tier: short\n", ""), tier="short")
        self.assertEqual(ctx.tname, "short")

    def test_platform_must_match_tier(self):
        self.assertParseError(read("valid-short.md").replace("platform: reels", "platform: youtube"))

    def test_text_outside_table(self):
        self.assertParseError(read("valid-short.md").replace("## Caption", "stray note\n## Caption"))

    def test_wrong_cell_count(self):
        self.assertParseError(read("valid-short.md").replace("| proof | F2 |", "| proof |"))

    def test_beats_must_be_numbered_in_order(self):
        self.assertParseError(read("valid-short.md").replace("| 3 | 7-11 |", "| 4 | 7-11 |"))

    def test_missing_front_matter(self):
        self.assertParseError("## Script\n", 1)

    def test_cli_parse_error_json(self):
        code, out = cli(os.path.join(FIX, "PARSE.md"), "--json")
        self.assertEqual(code, 2)
        self.assertEqual(json.loads(out)["result"], "PARSE")

    def test_cli_missing_rules_file_exits_2(self):
        code, _ = cli(os.path.join(FIX, "valid-short.md"), "--tiers", os.path.join(FIX, "nope.json"))
        self.assertEqual(code, 2)

    def test_explain(self):
        code, out = cli("--explain", "T01")
        self.assertEqual(code, 0)
        self.assertIn("max_seconds=25", out)
        self.assertIn("max_seconds=200", out)
        self.assertIn("counts:", out)
        self.assertIn("fix:", out)
        self.assertIn("block", cli("--explain", "BR03")[1])
        self.assertEqual(cli("--explain", "ZZ9")[0], 2)


if __name__ == "__main__":
    unittest.main(verbosity=1)
