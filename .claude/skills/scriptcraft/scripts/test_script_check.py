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
import attack_cases  # noqa: E402

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
    "F04-other-claim": "block",
    # 0.3.0 styles: ugc_talk and ugc_text rules, disclosure and sound.
    "U01": "block", "U01-text": "block", "U02": "block", "U02-stock": "block", "U03": "warn", "U04": "warn",
    "U05": "warn", "U05-not-soft": "warn", "U06": "warn", "U06-contractions": "warn", "U07": "warn",
    "D01": "block", "D01-gifted-no-beat": "block", "D01-staff": "warn", "SND01": "block",
    "H01-first-word": "block", "H01-first-sentence": "block", "W01-ugc-text": "block", "O01-ugc-text": "block",
    "O04-ugc-text": "block", "L01-ugc-text": "block", "T03-ugc-text": "block",
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


TALK = "valid-ugc-talk.md"
TEXT = "valid-ugc-text.md"


def with_meta(text, key, value):
    """Set or add a front matter field (value None removes it)."""
    return attack_cases.set_meta(text, key, value)


def beat(text, n, **cells):
    return attack_cases.set_beat(text, n, **cells)


class StyleDefaults(unittest.TestCase):
    def test_no_style_field_defaults_to_voiceover(self):
        m = check(read("valid-short.md")).doc.meta
        self.assertEqual((m["style"], m["creator"], m["relationship"], m["sound"]),
                         ("voiceover", "guide", "staff", "original"))

    def test_voiceover_report_keeps_the_020_layout(self):
        _, out = cli(os.path.join(FIX, "valid-short.md"))
        self.assertNotIn("style", out.splitlines()[0])
        for rid in sc.NEW_RULES:
            self.assertNotIn(" %s " % rid, out)
        self.assertIn("[PASS] H02", out)

    def test_explicit_style_voiceover_gives_the_same_findings(self):
        text = read("valid-short.md")
        self.assertEqual(check(with_meta(text, "style", "voiceover")).findings, check(text).findings)

    def test_ugc_report_lists_style_fields_and_skips(self):
        _, out = cli(os.path.join(FIX, TALK))
        self.assertIn("style ugc_talk | creator guide | relationship guide | sound original", out.splitlines()[0])
        self.assertIn("[SKIP] H02", out)
        self.assertIn("[PASS] U01", out)
        self.assertIn("[PASS] D01", out)

    def test_json_has_style_fields(self):
        _, out = cli(os.path.join(FIX, TEXT), "--json")
        d = json.loads(out)
        self.assertEqual((d["style"], d["relationship"], d["sound"], d["max_seconds"]), ("ugc_text", "staff", "original", 15))

    def test_valid_style_fixtures_pass_clean_and_strict(self):
        for name in (TALK, TEXT, "valid-voiceover-loop.md"):
            self.assertEqual(check(read(name)).findings, [], name)
            self.assertEqual(cli(os.path.join(FIX, name), "--strict", "--final", "--no-example-copy")[0], 0, name)

    def test_ugc_talk_short_overrides(self):
        t = sc.tier_limits(CFG, "short", "ugc_talk")
        self.assertEqual((t["wps"], t["words"]["hard_max"], t["words_per_beat"]["hard_max"], t["sentence"]["hard_max_words"]),
                         (3.0, 75, 24, 16))
        self.assertEqual((t["hook"]["max_seconds_with_overlay"], t["hook"]["hard_max_words"], t["cta"]["min"], t["cta"]["max_words"]),
                         (4, 15, 0, 10))
        self.assertEqual(t["platforms"], CFG["tiers"]["short"]["platforms"])  # untouched keys come from the tier

    def test_ugc_talk_long_overrides(self):
        t = sc.tier_limits(CFG, "long", "ugc_talk")
        self.assertEqual((t["wps"], t["words"]["hard_max"], t["words"]["target_min"], t["sentence"]["hard_max_words"]),
                         (2.8, 560, 420, 20))
        self.assertEqual(t["sentence"]["avg_max"], CFG["tiers"]["long"]["sentence"]["avg_max"])
        self.assertEqual(t["hook"], CFG["tiers"]["long"]["hook"])

    def test_voiceover_has_no_overrides(self):
        for tier in CFG["tiers"]:
            self.assertEqual(sc.tier_limits(CFG, tier, "voiceover"), CFG["tiers"][tier])

    def test_facts_limits_never_loosen_in_any_style(self):
        for style in CFG["styles"]["allowed"]:
            for tier in CFG["tiers"]:
                base, t = CFG["tiers"][tier]["facts"], sc.tier_limits(CFG, tier, style)["facts"]
                for k, v in base.items():
                    self.assertLessEqual(t[k], v, "%s %s %s" % (style, tier, k))

    def test_style_numbers_come_from_tiers_json(self):
        cfg = json.loads(json.dumps(CFG))
        cfg["styles"]["ugc_talk"]["short"]["wps"] = 2.0
        text = read(TALK)
        fast = sc.run(sc.parse_document(text, CFG), CFG, BRAND).total_est
        slow = sc.run(sc.parse_document(text, cfg), cfg, BRAND).total_est
        self.assertGreater(slow, fast * 1.4)

    def test_every_rule_has_help_and_explain(self):
        for rid in sc.RULES:
            self.assertIn(rid, sc.HELP, rid)
        for rid in sc.NEW_RULES:
            code, out = cli("--explain", rid)
            self.assertEqual(code, 0, rid)
            self.assertIn("counts:", out)
            self.assertIn("caption_chapters" if rid == "C06" else "styles.", out)

    def test_explain_shows_style_overrides(self):
        _, out = cli("--explain", "H01")
        self.assertIn("short, style ugc_talk override", out)
        self.assertIn("first_word_by_seconds", out)
        _, out = cli("--explain", "U03")
        self.assertIn("runs for: style ugc_talk only", out)


class StyleParsing(unittest.TestCase):
    def assertParseError(self, text, key=None, tier=None):
        with self.assertRaises(sc.ParseError) as cm:
            check(text, tier=tier)
        if key:
            line = [i + 1 for i, x in enumerate(text.splitlines()) if x.startswith(key + ":")][0]
            self.assertEqual(cm.exception.line, line)
        return cm.exception

    def test_invalid_style_names_the_line(self):
        e = self.assertParseError(with_meta(read("valid-short.md"), "style", "cinematic"), "style")
        self.assertIn("voiceover, ugc_talk, ugc_text", e.msg)

    def test_superseded_style_names_are_errors(self):
        for old in ("ugc", "polished"):
            self.assertParseError(with_meta(read("valid-short.md"), "style", old), "style")

    def test_ugc_text_is_short_only(self):
        e = self.assertParseError(with_meta(read("valid-long.md"), "style", "ugc_text"), "style")
        self.assertIn("only valid for tier short", e.msg)

    def test_invalid_creator_relationship_sound(self):
        for key, bad in (("creator", "influencer"), ("relationship", "friend"), ("sound", "viral")):
            self.assertParseError(with_meta(read(TALK), key, bad), key)

    def test_ugc_text_seconds_range(self):
        self.assertEqual(check(with_meta(read(TEXT), "seconds", "7")).secs, 7)
        self.assertParseError(with_meta(read(TEXT), "seconds", "6"), "seconds")
        self.assertParseError(with_meta(read(TEXT), "seconds", "16"), "seconds")

    def test_disclosure_role_token(self):
        self.assertIn("disclosure", check(read(TALK)).doc.beats[1].roles)
        self.assertParseError(read(TALK).replace("setup, disclosure", "setup, disclose"))

    def test_cli_style_parse_error_exits_2(self):
        path = os.path.join(FIX, "PARSE.md")
        self.assertEqual(cli(path)[0], 2)
        code, out = cli("--explain", "SND01")
        self.assertEqual(code, 0)


class UgcRules(unittest.TestCase):
    def test_u01_selfie_passes_and_greeting_blocks(self):
        self.assertFalse(found(check(read(TALK)), "U01"))
        ctx = check(beat(read(TALK), 1, visual="guide waves hello to the camera / group behind"))
        self.assertTrue(found(ctx, "U01", "block"))

    def test_h02_and_h03_do_not_run_in_ugc(self):
        ctx = check(beat(read(TALK), 1, visual="logo over the snow, guide in front"))
        self.assertFalse(found(ctx, "H02"))
        self.assertTrue(found(ctx, "U02", "block"))

    def test_u02_slide_noun_blocks_verb_passes(self):
        self.assertTrue(found(check(beat(read(TALK), 5, visual="the end slide with dates / guide grins")), "U02", "block"))
        self.assertFalse(found(check(beat(read(TALK), 5, visual="skis slide down the ridge / guide grins")), "U02"))
        self.assertFalse(found(check(beat(read(TALK), 5, visual="the guest copies the slide / guide grins")), "U02"))
        self.assertTrue(found(check(beat(read(TALK), 5, visual="a slide with the dates / guide grins")), "U02", "block"))

    def test_handheld_one_take_is_motion(self):
        ctx = check(beat(read(TALK), 6, visual="one take: selfie, guide laughs and swings the phone to the group"))
        self.assertFalse(found(ctx, "V01"))

    def test_u02_does_not_run_in_voiceover(self):
        self.assertFalse(found(check(read("valid-voiceover-loop.md")), "U02"))

    def test_u03_first_person_stake_and_we_pass(self):
        for line in ("I make every guest start a little cold.", "We start every climb a little cold."):
            ctx = check(beat(read(TALK), 1, vo=line, overlay="cold on purpose"))
            self.assertFalse(found(ctx, "U03"), line)

    def test_u04_allowlisted_acronym_passes(self):
        self.assertFalse(found(check(beat(read(TALK), 5, overlay="POV: start cold")), "U04"))
        ctx = check(beat(read(TALK), 5, overlay="start COLD"))
        self.assertTrue(found(ctx, "U04", "warn"))
        self.assertFalse(found(ctx, "R02"))  # ugc overlays are U04's, not R02's

    def test_u05_logistics_line_is_soft(self):
        ctx = check(beat(read(TALK), 6, vo="Dates and prices in the caption, come ski."))
        self.assertFalse(found(ctx, "U05"))

    def test_u05_bare_question_is_not_soft(self):
        self.assertTrue(found(check(beat(read(TALK), 6, vo="Would you start cold or warm?")), "U05", "warn"))

    def test_u05_skips_when_there_is_no_cta(self):
        text = read(TALK).replace("| cta | - |", "| build | - |").replace("Send this to the friend", "This goes to the friend")
        ctx = check(text)
        self.assertFalse(found(ctx, "U05"))
        self.assertFalse(found(ctx, "C01"))  # ugc_talk cta min is 0

    def test_u06_honestly_once_passes(self):
        ctx = check(beat(read(TALK), 5, vo="Honestly, stay dry on the way up, and you ski down warm."))
        self.assertFalse(found(ctx, "U06"))
        self.assertEqual(sc.casual_markers(ctx), ["honestly"])

    def test_u06_filler_like_counts(self):
        ctx = check(beat(read(TALK), 5, vo="Like, stay dry, like, and you ski down warm."))
        self.assertEqual(sc.casual_markers(ctx), ["like", "like"])

    def test_u06_contractions_skip_possessives(self):
        ctx = check(beat(read(TALK), 5, vo="The guide's rule: it's dry up, don't stop, you ski warm."))
        self.assertEqual(sorted(sc.contraction_list(ctx)), ["don't", "it's", "you're", "you've"])

    def test_u07_one_take_prefix_not_counted(self):
        self.assertTrue(found(check(beat(read(TALK), 3, visual="one take: guide")), "U07", "warn"))

    def test_r03_counts_i_on_the_guest_side_in_ugc(self):
        text = beat(read(TALK), 4, vo="We stop, we rest, we eat, our break, our call. I love it, I swear, my rule.")
        self.assertFalse(found(check(text), "R03"))
        self.assertTrue(found(check(with_meta(text, "style", "voiceover")), "R03", "warn"))


class UgcLimits(unittest.TestCase):
    def test_hook_gets_4_s_only_with_an_overlay(self):
        text = read(TALK)
        self.assertFalse(found(check(text), "H01"))
        self.assertTrue(found(check(beat(text, 1, overlay="-")), "H01", "block"))

    def test_first_sentence_under_6_words_warns(self):
        ctx = check(beat(read(TALK), 1, vo="Start cold. I make every guest."))
        self.assertTrue(found(ctx, "H01", "warn"))

    def test_hook_with_no_spoken_word_blocks(self):
        self.assertTrue(found(check(beat(read(TALK), 1, vo="-")), "H01", "block"))

    def test_disclosure_beat_exempt_from_beat_target(self):
        ctx = check(beat(read(TALK), 2, vo="I guide for Outdoor Norway."))
        self.assertFalse(found(ctx, "W03"))

    def test_ugc_talk_overlay_title_8_words(self):
        title = "why I make you start cold now"
        self.assertFalse(found(check(beat(read(TALK), 1, overlay=title)), "O01"))
        self.assertTrue(found(check(beat(read("valid-voiceover-loop.md"), 1, overlay=title)), "O01", "block"))

    def test_ugc_talk_word_budget_75(self):
        ctx = check(read(TALK))
        self.assertEqual(ctx.total_words, 66)
        self.assertFalse(found(ctx, "W01"))
        self.assertFalse(found(ctx, "W02"))

    def test_ugc_text_single_beat_loop_passes(self):
        text = read(TEXT).split("| 2 | 5-10 |")[0].rstrip("\n") + "\n## Caption\nStart cold. #skitouring\n"
        text = text.replace("| 1 | 0-5 |", "| 1 | 0-10 |").replace("hook, open:A, disclosure", "hook, open:A, close:A, disclosure")
        ctx = check(text)
        self.assertFalse(found(ctx, "L01"))
        self.assertFalse(blocking(ctx))

    def test_ugc_text_overlay_repeat_counts_once(self):
        text = beat(read(TEXT), 2, overlay="the layer rule every guide uses")
        self.assertFalse(found(check(text), "O01"))

    def test_ugc_text_overlay_under_4_words_warns(self):
        text = beat(beat(read(TEXT), 1, overlay="cold"), 2, overlay="cold")
        self.assertTrue(found(check(text), "O01", "warn"))

    def test_ugc_text_words_do_not_scale_with_seconds(self):
        text = beat(read(TEXT), 2, vo="Start a little cold, ski down warm.")
        self.assertFalse(found(check(text), "W01"))  # 12 words in a 10 s clip

    def test_ugc_text_facts_at_most_1(self):
        text = attack_cases.add_fact(attack_cases.add_fact(read(TEXT), "| F1 | Guides call a layer check | fixture | yes |"),
                                     "| F2 | Wet layers chill fast | fixture | yes |")
        text = beat(beat(text, 1, facts="F1"), 2, facts="F2")
        self.assertTrue(found(check(text), "F02", "block"))


class Disclosure(unittest.TestCase):
    def test_guest_unpaid_needs_nothing(self):
        text = with_meta(beat(read(TALK), 2, role="setup"), "relationship", "guest_unpaid")
        self.assertFalse(found(check(text), "D01"))

    def test_paid_guest_done_right_passes(self):
        text = with_meta(beat(read(TALK), 2, vo="Quick one: they paid for this trip, so this is an ad."), "relationship", "guest_paid")
        text = text.replace("The layer rule I use", "#ad The layer rule my guide uses")
        self.assertFalse(found(check(text), "D01"))

    def test_disclosure_must_start_before_5_s(self):
        text = read(TALK).replace("| 1 | 0-4 |", "| 1 | 0-5 |").replace("| 2 | 4-8 |", "| 2 | 5-8 |")
        self.assertTrue(found(check(text), "D01", "warn"))

    def test_staff_role_line_must_name_the_role(self):
        ctx = check(beat(read(TALK), 2, vo="Quick one from me, this is my favourite rule.", overlay="the layer rule"))
        self.assertTrue(found(ctx, "D01", "warn"))

    def test_voiceover_runs_d01_only_when_relationship_is_written(self):
        self.assertFalse(found(check(read("valid-short.md")), "D01"))
        self.assertTrue(found(check(with_meta(read("valid-short.md"), "relationship", "staff")), "D01", "warn"))
        self.assertTrue(found(check(with_meta(read("valid-short.md"), "relationship", "guest_paid")), "D01", "block"))


class Sound(unittest.TestCase):
    def test_trending_with_a_trip_word_blocks(self):
        ctx = check(with_meta(read(TALK), "sound", "trending"))
        self.assertIn("Outdoor Norway", found(ctx, "SND01", "block")[0]["quote"])

    def test_other_sound_values_pass(self):
        for value in ("original", "commercial_library", "voiceover_only", "none"):
            self.assertFalse(found(check(with_meta(read(TALK), "sound", value)), "SND01"), value)

    def test_trending_runs_in_voiceover_too(self):
        self.assertTrue(found(check(with_meta(read("valid-short.md"), "sound", "trending")), "SND01", "block"))


class F04Claims(unittest.TestCase):
    def test_different_claim_blocks_in_draft(self):
        self.assertTrue(found(check(read("F04-other-claim.md")), "F04", "block"))

    def test_uncited_same_claim_warns_in_draft_blocks_in_final(self):
        self.assertTrue(found(check(read("F04-uncited.md")), "F04", "warn"))
        self.assertFalse(found(check(read("F04-uncited.md")), "F04", "block"))
        self.assertTrue(found(check(read("F04-uncited.md"), final=True), "F04", "block"))

    def test_unit_with_an_adjective_matches(self):
        text = read("valid-short.md").replace("The guided climb takes about 2 hours", "You climb about 400 metres on skins")
        text = text.replace("With a guide, the climb takes about 2 hours.", "With a guide, you climb 400 vertical metres.")
        text = text.replace("| About 2 hours up |", "| 400 m up |")
        self.assertFalse(found(check(text), "F04"))

    def test_unit_before_the_number_in_the_row_matches(self):
        text = read("valid-short.md").replace("The guided climb takes about 2 hours", "Day tours from NOK 1,950 per adult")
        text = text.replace("With a guide, the climb takes about 2 hours.", "With a guide, NOK 1,950 a day.")
        text = text.replace("| About 2 hours up |", "| NOK 1,950 a day |")
        self.assertFalse(found(check(text), "F04"))


class VerifierRound(unittest.TestCase):
    """Gaps found by the independent verification round, one test each."""

    def talk(self):
        return read("valid-ugc-talk.md")

    def test_u02_stock_with_a_word_between(self):
        self.assertTrue(found(check(beat(self.talk(), 3, visual="stock drone footage of the fjord / guest grins")), "U02", "block"))

    def test_u02_animated_map_and_closing_card(self):
        self.assertTrue(found(check(beat(self.talk(), 3, visual="animated route map / guest grins at the lens")), "U02", "block"))
        self.assertTrue(found(check(beat(self.talk(), 6, visual="skier laughs / closing card with the dates")), "U02", "block"))

    def test_u02_animated_guest_and_final_frame_pass(self):
        self.assertFalse(found(check(beat(self.talk(), 3, visual="an animated guest laughs at the lens / birch trees")), "U02"))
        self.assertFalse(found(check(beat(self.talk(), 3, visual="guide skins up / final frame cuts back to the skis")), "U02"))

    def test_d01_negated_paid_word_does_not_disclose(self):
        text = attack_cases.set_caption(beat(with_meta(self.talk(), "relationship", "guest_paid"), 2,
                                             vo="Quick one, I'm not paid to say this."), "Ad. My trip.")
        self.assertTrue(found(check(text), "D01", "block"))
        text = attack_cases.set_caption(beat(with_meta(self.talk(), "relationship", "guest_gifted"), 2,
                                             vo="Quick one from me.", overlay="this isn't sponsored"), "#ad my trip")
        self.assertTrue(found(check(text), "D01", "block"))

    def test_d01_ad_after_negation_elsewhere_still_counts(self):
        text = attack_cases.set_caption(beat(with_meta(self.talk(), "relationship", "guest_paid"), 2,
                                             vo="Not gonna lie, this is an ad, they paid me."), "Ad. My trip.")
        self.assertFalse(found(check(text), "D01"))

    def test_d01_caption_labels_reklame_advert_annonse(self):
        for label in ("Reklame.", "Advert:", "Annonse.", "[Ad]", "#reklame"):
            text = attack_cases.set_caption(beat(with_meta(self.talk(), "relationship", "guest_gifted"), 2,
                                                 vo="Quick one: this trip was gifted, so it's an ad."), label + " My trip.")
            self.assertFalse(found(check(text), "D01"), label)
        text = attack_cases.set_caption(beat(with_meta(self.talk(), "relationship", "guest_gifted"), 2,
                                             vo="Quick one: this trip was gifted, so it's an ad."), "Adventure time. My trip.")
        self.assertTrue(found(check(text), "D01", "block"))

    def test_u05_logistics_line_to_the_caption_is_soft(self):
        for vo in ("Dates are in the caption if you're keen.", "How to book is down in the caption."):
            self.assertFalse(found(check(beat(self.talk(), 6, vo=vo, overlay="-")), "U05"), vo)

    def test_u05_link_only_in_a_story_beat_warns(self):
        text = beat(beat(self.talk(), 6, role="build"), 5, vo="Comment link and I'll send you the dates.", role="payoff, close:A")
        self.assertTrue(found(check(text), "U05", "warn"))

    def test_snd01_weekend_is_a_trip_word(self):
        text = beat(with_meta(self.talk(), "sound", "trending"), 2, vo="Quick one from me, I'm a ski guide on this weekend.")
        self.assertTrue(found(check(text), "SND01", "block"))


class ExampleCopyAndDisclosureOverlay(unittest.TestCase):
    """R04 (copied example lines) and the on-screen disclosure line of D01."""

    REF = """---
tier: short
---
## Script
| beat | time | voiceover | visual | text | role | facts |
|---|---|---|---|---|---|---|
| 1 | 0-4 | The old fleece trick keeps every guest warm all day long. | selfie: guide holds a damp fleece up to the lens beside a birch tree | - | hook | - |
| 2 | 4-8 | Send this to the friend who overdresses. | guide zips a shell at the top of the track | - | cta | - |
"""

    def setUp(self):
        import tempfile
        self.dir = tempfile.mkdtemp()
        self.ref = os.path.join(self.dir, "ref.md")
        self.out = os.path.join(self.dir, "out")
        os.makedirs(self.out)
        with open(self.ref, "w", encoding="utf-8") as fh:
            fh.write(self.REF)
        self.cfg = json.loads(json.dumps(CFG))
        self.cfg["styles"]["example_copy"]["reference_dirs"] = [self.dir]

    def run_r04(self, text, name="mine.md", source=None):
        path = source or os.path.join(self.out, name)
        if not source:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(text)
        return sc.run(sc.parse_document(text, self.cfg), self.cfg, BRAND, False, source=path)

    def talk(self):
        return read(TALK)

    def test_copied_voiceover_sentence_warns(self):
        text = beat(self.talk(), 3, vo="The old fleece trick keeps every guest warm today.")
        self.assertTrue(found(self.run_r04(text), "R04", "warn"))

    def test_copied_visual_warns(self):
        text = beat(self.talk(), 3, visual="selfie: guide holds a damp fleece up to the lens beside a birch tree / skis")
        self.assertTrue(found(self.run_r04(text), "R04", "warn"))

    def test_one_short_shared_run_does_not_warn(self):
        text = beat(self.talk(), 6, vo="Send this to the friend you ski with.", overlay="-")
        self.assertFalse(found(self.run_r04(text), "R04"))

    def test_script_is_never_compared_with_itself(self):
        self.assertEqual(sc.reference_rows(self.cfg, self.ref), ({}, {}, []))
        self.assertTrue(sc.reference_rows(self.cfg, os.path.join(self.out, "other.md"))[0])

    def test_examples_do_not_trip_r04_on_themselves(self):
        for name in ("short-fictional.md", "short-ugc-talk-fictional.md", "short-ugc-text-fictional.md", "long-fictional.md"):
            code, out = cli(os.path.join(HERE, "..", "examples", name), "--final", "--strict")
            self.assertEqual(code, 0, name + out)
            self.assertNotIn("R04 voiceover", out)

    def test_copy_of_a_whole_example_warns_from_the_cli(self):
        import shutil
        dst = os.path.join(self.out, "copy.md")
        shutil.copy(os.path.join(HERE, "..", "examples", "short-ugc-talk-fictional.md"), dst)
        code, out = cli(dst, "--json")
        data = json.loads(out)
        self.assertTrue([f for f in data["findings"] if f["id"] == "R04" and f["severity"] == "warn"])

    def test_text_only_run_skips_r04(self):
        ctx = check(self.talk())
        self.assertIn("R04", ctx.skipped)
        self.assertFalse(found(ctx, "R04"))

    def test_no_example_copy_flag_prints_skip(self):
        code, out = cli(os.path.join(FIX, TALK), "--no-example-copy")
        self.assertIn("[SKIP] R04", out)

    NEAR_REF = """---
tier: short
---
## Script
| beat | time | voiceover | visual | text | role | facts |
|---|---|---|---|---|---|---|
| 1 | 0-4 | Placeholder line one. | a drone rises over the ridge | - | hook | - |
| 2 | 4-8 | Placeholder line two. | skis and snowshoes stacked / family walks to the van in late light, carrying skis and snowshoes | - | cta | - |
"""

    def near_ctx(self, visuals):
        with open(self.ref, "w", encoding="utf-8") as fh:
            fh.write(self.NEAR_REF)
        text = self.talk()
        for n, v in zip((3, 4, 5), visuals):
            text = beat(text, n, visual=v)
        return self.run_r04(text)

    def test_three_restated_shots_warn(self):
        ctx = self.near_ctx(["one take: drone rises over a ridge",
                             "skis and snowshoes stacked together by a door",
                             "friends walk off the snow in late light, skis on shoulders and snowshoes in hand"])
        self.assertTrue([f for f in found(ctx, "R04", "warn") if "restate shots" in f["message"]], ctx.findings)

    def test_two_restated_shots_do_not_warn(self):
        ctx = self.near_ctx(["one take: drone rises over a ridge",
                             "skis and snowshoes stacked together by a door",
                             "guide kneels to tighten a boot buckle on the track"])
        self.assertFalse([f for f in found(ctx, "R04") if "restate shots" in f["message"]], ctx.findings)

    def test_unrelated_shots_do_not_warn(self):
        ctx = self.near_ctx(["guide kneels to tighten a boot buckle on the track",
                             "guest laughs at the camera and wipes frost off a glove",
                             "skier skids to a stop beside a birch trunk"])
        self.assertFalse(found(ctx, "R04"), ctx.findings)

    def test_caption_placeholder_blocks_final_only(self):
        text = attack_cases.set_caption(self.talk(), "Ad. Book here [LINK: tour page, client confirms]. #skitouring")
        self.assertFalse(found(check(text), "BR13"))
        self.assertTrue(found(check(text, final=True), "BR13", "block"))

    def test_voiceover_without_relationship_gets_an_info_line(self):
        ctx = check(read("valid-short.md"))
        self.assertTrue([i for i in ctx.info if "disclosure rule was not checked" in i])
        self.assertFalse([i for i in check(self.talk()).info if "disclosure rule was not checked" in i])

    def brief_text(self, source):
        text = read(TALK)
        return text.replace("| F1 |", "| F9 | The guide leads the day | %s | yes |\n| F1 |" % source, 1)

    def test_f06_brief_without_a_quote_warns_and_blocks_final(self):
        text = self.brief_text("client brief, 2026-10-08")
        self.assertTrue(found(check(text), "F06", "warn"))
        self.assertTrue(found(check(text, final=True), "F06", "block"))

    def test_f06_brief_with_a_quote_passes(self):
        text = self.brief_text('client brief 2026-10-08: "the guide leads the day"')
        self.assertFalse(found(check(text, final=True), "F06"))

    def test_f06_file_source_needs_no_quote(self):
        text = self.brief_text("campaigns/ski-meta-ads/tours.json")
        self.assertFalse(found(check(text, final=True), "F06"))

    def test_f06_unverified_brief_row_needs_no_quote(self):
        text = self.brief_text("client brief, 2026-10-08").replace("| yes |\n| F1 |", "| no |\n| F1 |", 1)
        self.assertFalse(found(check(text), "F06"))

    def test_br13_placeholder_in_a_visual_blocks_final_only(self):
        text = beat(read(TALK), 3, visual="selfie, the guide on the trail [VERIFY: which trail, guide]")
        self.assertFalse(found(check(text), "BR13"))
        self.assertTrue(found(check(text, final=True), "BR13", "block"))

    def test_u05_logistics_line_to_the_description_is_soft(self):
        for vo in ("The dates and prices are in the description if you're keen.", "Booking details are in the description."):
            self.assertFalse(found(check(beat(self.talk(), 6, vo=vo, overlay="-")), "U05"), vo)

    def test_d01_disclosure_beat_without_overlay_warns(self):
        text = beat(self.talk(), 2, overlay="-")
        self.assertTrue(found(check(text), "D01", "warn"))
        self.assertFalse(found(check(self.talk()), "D01"))

    def test_d01_guest_unpaid_needs_no_overlay(self):
        text = beat(with_meta(self.talk(), "relationship", "guest_unpaid"), 2, overlay="-")
        self.assertFalse(found(check(text), "D01"))

    def test_disclosure_overlay_does_not_use_a_content_line_in_ugc_text(self):
        three = read(TEXT).replace("| 1 | 0-5 | I guide for Outdoor Norway. |", "| 1 | 0-3 | - |").replace(
            "hook, open:A, disclosure", "hook, open:A").replace(
            "| 2 | 5-10 | - |", "| 2 | 3-6 | I guide for Outdoor Norway. |").replace(
            "start cold, ski down warm | payoff, close:A", "ski guide | disclosure")
        three = three.replace("## Caption", "| 3 | 6-10 | - | guide peels off a fleece at the top, grinning / skier drops into "
                              "the descent | start cold, ski down warm | payoff, close:A | - |\n## Caption", 1)
        ctx = check(three)
        self.assertFalse([f for f in found(ctx, "O01", "block") if "different overlay lines" in f["message"]], ctx.findings)
        off = json.loads(json.dumps(CFG))
        del off["styles"]["disclosure"]["overlay_max_words"]
        ctx = sc.run(sc.parse_document(three, off), off, BRAND)
        self.assertTrue([f for f in found(ctx, "O01", "block") if "different overlay lines" in f["message"]])

    def test_disclosure_overlay_over_6_words_blocks(self):
        base = read(TEXT)
        text = base.replace("| 2 | 5-10 | - |", "| 2 | 5-10 | I guide for Outdoor Norway. |").replace(
            "start cold, ski down warm | payoff, close:A", "start cold, ski down warm | payoff, close:A")
        text = text.replace("hook, open:A, disclosure", "hook, open:A")
        text = beat(text, 2, role="disclosure, close:A", overlay="I guide here for the whole winter at Outdoor Norway")
        self.assertTrue([f for f in found(check(text), "O01", "block") if "disclosure overlay" in f["message"]])

    def test_hook_beat_overlay_never_uses_the_disclosure_allowance(self):
        base = read(TEXT)
        text = beat(base, 1, overlay="the layer rule every guide uses on every single winter climb")
        self.assertTrue(found(check(text), "O01", "block"))


class YoutubeChapters(unittest.TestCase):
    """C06 and the F04 exemption for chapter timestamps in a YouTube description."""

    def long(self):
        return read("valid-long.md")

    def with_caption(self, lines):
        return attack_cases.set_caption(self.long(), "\n".join(lines))

    GOOD = ["How a guided ski touring day works. #skitouring", "0:00 Skis that climb", "0:20 The gear", "0:44 The climb",
            "1:20 The turn", "1:56 The ski down"]

    def test_valid_chapters_pass_clean(self):
        ctx = check(self.with_caption(self.GOOD))
        self.assertEqual(ctx.findings, [])

    def test_timestamps_are_not_numbers_for_f04(self):
        self.assertFalse(found(check(self.with_caption(self.GOOD)), "F04"))

    def test_a_real_number_on_a_chapter_line_still_needs_a_facts_row(self):
        lines = list(self.GOOD)
        lines[2] = "0:20 The gear costs 9,999"
        self.assertTrue(found(check(self.with_caption(lines)), "F04", "block"))

    def test_no_chapters_warns_for_youtube_long(self):
        ctx = check(self.with_caption(["How a guided ski touring day works. #skitouring"]))
        self.assertTrue(found(ctx, "C06", "warn"))

    def test_fewer_than_three_chapters_warns(self):
        self.assertTrue(found(check(self.with_caption(self.GOOD[:3])), "C06", "warn"))

    def test_first_chapter_must_be_zero(self):
        lines = list(self.GOOD)
        lines[1] = "0:08 Skis that climb"
        self.assertTrue([f for f in found(check(self.with_caption(lines)), "C06") if "0:00" in f["message"]])

    def test_chapter_off_a_beat_start_warns(self):
        lines = list(self.GOOD)
        lines[3] = "0:50 The climb"
        self.assertTrue([f for f in found(check(self.with_caption(lines)), "C06") if "does not start on a beat" in f["message"]])

    def test_chapters_under_10_seconds_apart_warn(self):
        lines = list(self.GOOD)
        lines[1:3] = ["0:20 Skis that climb", "0:25 The gear"]
        self.assertTrue([f for f in found(check(self.with_caption(lines)), "C06") if "under" in f["message"]])

    def test_chapter_without_a_title_warns(self):
        lines = list(self.GOOD)
        lines[2] = "0:20"
        self.assertTrue([f for f in found(check(self.with_caption(lines)), "C06") if "no title" in f["message"]])

    def test_other_platforms_are_not_checked(self):
        cfg = json.loads(json.dumps(CFG))
        cfg["caption_chapters"]["platform"] = "tiktok"
        text = self.with_caption(["A caption with no chapters. #skitouring"])
        ctx = sc.run(sc.parse_document(text, cfg), cfg, BRAND)
        self.assertFalse(found(ctx, "C06"))

    def test_short_tier_never_needs_chapters(self):
        self.assertFalse(found(check(read(TALK)), "C06"))

    def test_chapter_after_the_script_end_warns(self):
        lines = list(self.GOOD) + ["4:00 Late"]
        self.assertTrue(found(check(self.with_caption(lines)), "C06", "warn"))

    def test_help_for_c06_names_the_config(self):
        code, out = cli("--explain", "C06")
        self.assertEqual(code, 0)
        self.assertIn("caption_chapters", out)


class AttackHarness(unittest.TestCase):
    def test_attack_cases_have_no_mismatch(self):
        self.assertEqual(attack_cases.run_all(verbose=False), [])

    def test_attack_harness_size(self):
        self.assertGreaterEqual(len(attack_cases.CASES), 81)


if __name__ == "__main__":
    unittest.main(verbosity=1)
