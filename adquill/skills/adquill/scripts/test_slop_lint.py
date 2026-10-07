#!/usr/bin/env python3
"""Tests for slop_lint.py. Run them with:

    python3 -I skills/adquill/scripts/test_slop_lint.py

Standard library only (unittest). No network. The CLI tests run the script in a child
process with python3 -I, the same way the skill does, and write nothing to disk except in
a temporary directory that the test removes.

Every example in this file is a fictional brief for the invented brand Brekke Ski Guides.
Prices and dates are invented.
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import slop_lint as sl  # noqa: E402

SCRIPT = os.path.join(HERE, "slop_lint.py")
RULES_PATH = os.path.join(HERE, "rules.json")
FIXTURES = os.path.join(HERE, "fixtures")

EM = chr(0x2014)
EN = chr(0x2013)
RULES = sl.load_rules(RULES_PATH)


def lint(text, **kwargs):
    return sl.lint_text(text, RULES, **kwargs)


def ids(text, **kwargs):
    return {hit["id"] for hit in lint(text, **kwargs)["hits"]}


def severities(text, rule_id, **kwargs):
    return {hit["severity"] for hit in lint(text, **kwargs)["hits"] if hit["id"] == rule_id}


def run_cli(*args, stdin=None):
    proc = subprocess.run(
        [sys.executable, "-I", SCRIPT] + list(args),
        input=stdin, capture_output=True, text=True, timeout=60,
    )
    return proc.returncode, proc.stdout, proc.stderr


def read_fixture(name):
    with open(os.path.join(FIXTURES, name), "r", encoding="utf-8") as handle:
        return handle.read()


class RulesFileTests(unittest.TestCase):
    def test_at_least_80_rules(self):
        self.assertGreaterEqual(len(RULES["rules"]), 80)

    def test_rule_ids_are_unique(self):
        found = [r["id"] for r in RULES["rules"]]
        self.assertEqual(len(found), len(set(found)))

    def test_every_rule_has_required_keys(self):
        for rule in RULES["rules"]:
            for key in sl.REQUIRED_KEYS:
                self.assertIn(key, rule, "%s lacks %s" % (rule.get("id"), key))

    def test_every_category_is_used(self):
        used = {r["category"] for r in RULES["rules"]}
        self.assertEqual(used, set(sl.CATEGORIES))

    def test_all_three_severities_are_used(self):
        used = {r["severity"] for r in RULES["rules"]}
        self.assertEqual(used, set(sl.SEVERITIES))

    def test_block_rules_weigh_more_than_note_rules(self):
        block = min(r["weight"] for r in RULES["rules"] if r["severity"] == "block")
        note = max(r["weight"] for r in RULES["rules"] if r["severity"] == "note")
        self.assertGreater(block, note)

    def test_selftest_passes(self):
        self.assertEqual(sl.selftest(RULES), [])

    def test_most_rules_carry_examples(self):
        with_examples = [r for r in RULES["rules"] if r.get("examples_bad")]
        self.assertGreaterEqual(len(with_examples), 70)

    def test_all_slots_have_a_limit_and_a_source(self):
        for name, slot in RULES["slots"].items():
            self.assertIsInstance(slot["limit"], int, name)
            self.assertTrue(slot["source"], name)
            self.assertTrue(slot["status"], name)

    def test_source_files_contain_no_dash_characters_or_emoji(self):
        banned = {EM, EN}
        for path in (SCRIPT, RULES_PATH, os.path.abspath(__file__)):
            with open(path, "r", encoding="utf-8") as handle:
                body = handle.read()
            for ch in body:
                self.assertNotIn(ch, banned, path)
                self.assertFalse(0x1F300 <= ord(ch) <= 0x1FAFF, path)
                self.assertFalse(0x2600 <= ord(ch) <= 0x27BF, path)

    def test_rules_file_error_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = os.path.join(tmp, "bad.json")
            with open(bad, "w", encoding="utf-8") as handle:
                handle.write("{not json")
            with self.assertRaises(sl.RulesError):
                sl.load_rules(bad)

    def test_rule_without_required_key_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = os.path.join(tmp, "bad.json")
            with open(bad, "w", encoding="utf-8") as handle:
                json.dump({"rules": [{"id": "X-1", "category": "lexical"}]}, handle)
            with self.assertRaises(sl.RulesError):
                sl.load_rules(bad)


class DetectionTests(unittest.TestCase):
    def test_negative_parallelism(self):
        self.assertIn("STR-001", ids("It's not just a ski trip, it's a way of life."))

    def test_negative_parallelism_second_form(self):
        self.assertTrue({"STR-001", "STR-002"} & ids("This isn't about skiing. It's about freedom."))

    def test_countdown(self):
        self.assertIn("STR-003", ids("No queues. No crowds. Just snow."))

    def test_whether_you_are(self):
        self.assertIn("STR-004", ids("Whether you're a first-timer or a seasoned pro, we have a tour."))

    def test_tier_one_vocabulary(self):
        self.assertIn("LEX-010", ids("We delve into the fjords."))
        self.assertIn("LEX-010", ids("Embark on a ski week."))

    def test_ad_slop_verb(self):
        self.assertIn("LEX-011", ids("Elevate your ski season."))

    def test_scenery_adjective(self):
        self.assertIn("TRV-001", ids("Stunning, breathtaking fjords."))

    def test_filler_transition(self):
        self.assertIn("LEX-035", ids("Furthermore, the tour is good."))

    def test_question_opener(self):
        self.assertIn("AD-001", ids("Ready to ski the fjords?"))

    def test_chatbot_residue_blocks(self):
        result = lint("Certainly! Here is a revised caption for your post: Ski Saturday.")
        self.assertIn("LEX-001", {h["id"] for h in result["hits"]})
        self.assertEqual(result["verdict"], "BLOCK")

    def test_placeholder_blocks(self):
        self.assertIn("LEX-002", ids("Book the [insert tour name] today."))

    def test_guarantee_blocks(self):
        result = lint("Guaranteed fresh snow on every tour.")
        self.assertIn("POL-001", {h["id"] for h in result["hits"]})
        self.assertEqual(result["verdict"], "BLOCK")

    def test_false_scarcity_blocks(self):
        self.assertEqual(severities("Only 3 spots left, book now.", "POL-003"), {"block"})

    def test_personal_attribute_opener_blocks(self):
        self.assertEqual(severities("Are you over 50 and still skiing?", "POL-005"), {"block"})

    def test_invented_rating_blocks(self):
        self.assertEqual(severities("Rated 4.9 by thousands of happy skiers.", "POL-008"), {"block"})

    def test_before_after_price_blocks(self):
        self.assertIn("POL-011", ids("Was NOK 6,900, now NOK 4,900."))

    def test_certainty_about_aurora(self):
        self.assertIn("TRV-007", ids("You will see the northern lights."))

    def test_emoji_flagged(self):
        self.assertIn("FMT-005", ids("Ski the fjord " + chr(0x2744) + " today."))

    def test_em_dash_flagged(self):
        self.assertIn("FMT-001", ids("Ski the fjord " + EM + " then rest."))

    def test_en_dash_flagged(self):
        self.assertIn("FMT-002", ids("Ski 9" + EN + "10 days."))

    def test_double_hyphen_flagged(self):
        self.assertIn("FMT-003", ids("Ski the fjord -- then rest."))

    def test_caps_emphasis_flagged(self):
        self.assertIn("FMT-007", ids("Ski the fjord on SATURDAY with a guide."))

    def test_stacked_punctuation_flagged(self):
        self.assertIn("FMT-008", ids("Book today!!"))

    def test_markdown_bold_and_heading_flagged(self):
        self.assertIn("FMT-010", ids("Ski with **real guides** on Saturday."))
        self.assertIn("FMT-009", ids("# Ski Brekke\nSaturday, NOK 4,900."))

    def test_hashtag_stack_flagged(self):
        self.assertIn("FMT-013", ids("Ski Saturday. #ski #norway #brekke #fjords #powder"))

    def test_abstract_filler_is_flagged_in_travel_copy(self):
        self.assertTrue({"TRV-004", "TRV-002", "LEX-032"} & ids("Nestled in the heart of the mountains, a hidden gem."))


class FalsePositiveTests(unittest.TestCase):
    def test_robust_software_is_not_flagged(self):
        self.assertNotIn("LEX-013", ids("The booking API is robust under load."))

    def test_robust_about_ideas_is_a_warn_at_most(self):
        result = lint("A robust approach to winter adventure.")
        for hit in result["hits"]:
            self.assertNotEqual(hit["severity"], "block")
        self.assertIn("LEX-013", {h["id"] for h in result["hits"]})

    def test_leverage_as_a_noun_is_suppressed(self):
        self.assertNotIn("LEX-012", ids("Leverage on a pole plant comes from the hip."))
        self.assertNotIn("LEX-012", ids("The fund runs at a leverage of three to one."))

    def test_leverage_as_a_verb_is_flagged(self):
        self.assertIn("LEX-012", ids("Our guides leverage local knowledge."))

    def test_harness_on_a_glacier(self):
        self.assertEqual(ids("You wear a harness on the glacier section."), set())

    def test_unlock_a_cabin_door(self):
        self.assertEqual(ids("Unlock the cabin door with the brass key."), set())

    def test_navigate_in_a_whiteout(self):
        self.assertEqual(ids("We navigate by compass in a whiteout."), set())

    def test_elevation_is_a_measurement(self):
        self.assertEqual(ids("Elevation gain is 900 m."), set())

    def test_allowlisted_names(self):
        self.assertEqual(ids("Our guests also hold an Epic Pass."), set())
        self.assertEqual(ids("Dinner at the Majestic Hotel."), set())

    def test_negated_guarantee_is_fine(self):
        self.assertNotIn("POL-001", ids("We cannot guarantee snow."))
        self.assertNotIn("POL-001", ids("Snow is not guaranteed in February."))

    def test_currency_and_vat_are_not_caps_emphasis(self):
        self.assertNotIn("FMT-007", ids("Price in NOK, VAT included, paid by CTA link."))

    def test_train_journey_is_literal(self):
        self.assertNotIn("LEX-016", ids("The train journey to Voss takes 80 minutes."))

    def test_plain_factual_copy_scores_clean(self):
        text = "Six skiers per guide. Saturdays 9 Jan to 27 Feb, NOK 4,900 per person."
        self.assertEqual(lint(text)["score"], 100)


class IgnoreBlockTests(unittest.TestCase):
    def test_ignore_block_hides_hits(self):
        text = ("Meet at 08:30.\n<!-- adquill-lint: ignore-start -->\n"
                "Embark on a stunning journey. Guaranteed.\n"
                "<!-- adquill-lint: ignore-end -->\nSkins on at 09:15.")
        result = lint(text)
        self.assertEqual(result["hits"], [])
        self.assertEqual(result["score"], 100)

    def test_text_outside_the_block_is_still_checked(self):
        text = ("<!-- adquill-lint: ignore-start -->\nEmbark.\n<!-- adquill-lint: ignore-end -->\n"
                "We delve into the fjords.")
        self.assertIn("LEX-010", ids(text))

    def test_ignore_line(self):
        text = "Embark on a ski week. <!-- adquill-lint: ignore-line -->\nSaturday, NOK 4,900."
        self.assertNotIn("LEX-010", ids(text))

    def test_unclosed_block_is_reported(self):
        text = "<!-- adquill-lint: ignore-start -->\nEmbark on a ski week."
        self.assertIn("FMT-017", ids(text))

    def test_stray_end_is_reported(self):
        self.assertIn("FMT-018", ids("Saturday.\n<!-- adquill-lint: ignore-end -->"))

    def test_line_numbers_survive_masking(self):
        text = ("Line one.\n<!-- adquill-lint: ignore-start -->\nignored\n"
                "<!-- adquill-lint: ignore-end -->\nWe delve into it.")
        hits = [h for h in lint(text)["hits"] if h["id"] == "LEX-010"]
        self.assertEqual(hits[0]["line"], 5)

    def test_doc_profile_skips_code_fences(self):
        text = "Meet at 08:30 at the car park.\n\n```\nEmbark on a stunning journey\n```\n"
        self.assertNotIn("LEX-010", ids(text, profile="doc"))

    def test_skip_quotes_option(self):
        text = 'A guest wrote "stunning views, a real gem" after the trip.'
        self.assertIn("TRV-001", ids(text))
        self.assertNotIn("TRV-001", ids(text, skip_quotes=True))

    def test_allow_phrase_option(self):
        self.assertIn("TRV-001", ids("The Stunning Lodge opens at 09:00."))
        self.assertNotIn("TRV-001", ids("The Stunning Lodge opens at 09:00.", extra_allow=["Stunning Lodge"]))

    def test_ignore_rule_option(self):
        self.assertNotIn("LEX-010", ids("We delve into it.", ignore_rules=["LEX-010"]))


class SlotTests(unittest.TestCase):
    def test_headline_at_budget_passes(self):
        self.assertNotIn("PLT-003", ids("x" * 27, slot="meta_headline"))

    def test_headline_over_budget_warns(self):
        self.assertIn("PLT-003", ids("x" * 28, slot="meta_headline"))

    def test_headline_over_widest_field_blocks(self):
        self.assertEqual(severities("x" * 41, "PLT-004", slot="meta_headline"), {"block"})

    def test_primary_text_over_visible_part(self):
        self.assertIn("PLT-002", ids("a" * 126, slot="meta_primary"))
        self.assertNotIn("PLT-002", ids("a" * 125, slot="meta_primary"))

    def test_description_budget(self):
        self.assertIn("PLT-005", ids("a" * 31, slot="meta_description"))

    def test_image_line_budgets(self):
        self.assertIn("PLT-007", ids("a" * 26, slot="meta_image_line_1"))
        self.assertIn("PLT-008", ids("a" * 31, slot="meta_image_line_2"))
        self.assertIn("PLT-009", ids("a" * 21, slot="meta_image_line_3"))
        self.assertNotIn("PLT-009", ids("a" * 20, slot="meta_image_line_3"))

    def test_three_image_lines_with_a_fourth_is_flagged(self):
        text = "Ski touring day\nSaturdays 9 Jan to 27 Feb\nNOK 4,900\nBook now"
        self.assertIn("PLT-006", ids(text, slot="meta_image_line"))

    def test_reels_line_budget(self):
        self.assertIn("PLT-010", ids("a" * 41, slot="reels_line"))

    def test_x_post_budget(self):
        ok = ("Intro to ski touring above Brekke. Saturdays 9 Jan to 27 Feb, NOK 4,900 per person. "
              "Six per guide.")
        self.assertNotIn("PLT-001", ids(ok, slot="x_post"))
        self.assertEqual(severities("a " * 141, "PLT-001", slot="x_post"), {"block"})

    def test_x_link_counts_as_23(self):
        link = "https://example.com/" + "a" * 200
        self.assertEqual(sl.count_slot_chars("x_post", "Ski " + link), 4 + 23)

    def test_x_card_budgets(self):
        self.assertIn("PLT-011", ids("a" * 71, slot="x_card_headline"))
        self.assertIn("PLT-013", ids("a" * 201, slot="x_card_description"))

    def test_x_hashtags(self):
        self.assertIn("PLT-015", ids("Ski Brekke on Saturday #ski #norway #fjords", slot="x_post"))

    def test_limit_override(self):
        self.assertIn("PLT-003", ids("x" * 20, slot="meta_headline", limit_override=10))

    def test_slot_info_in_result(self):
        result = lint("Ski touring day, NOK 4,900", slot="meta_headline")
        self.assertEqual(result["slot"]["name"], "meta_headline")
        self.assertEqual(result["slot"]["chars"], 26)
        self.assertEqual(result["slot"]["limit"], 27)


class ScoreTests(unittest.TestCase):
    def test_clean_text_scores_100(self):
        self.assertEqual(lint("Meet at 08:30. Skins on at 09:15.")["score"], 100)

    def test_score_is_deterministic(self):
        text = "It's not just a ski trip, it's a way of life. Embark now!"
        self.assertEqual(lint(text)["score"], lint(text)["score"])
        self.assertEqual(json.dumps(lint(text), sort_keys=True), json.dumps(lint(text), sort_keys=True))

    def test_score_stays_in_range(self):
        for text in (read_fixture("bad-1-meta-primary.txt"), read_fixture("bad-3-chatbot-residue.txt"), "x"):
            score = lint(text)["score"]
            self.assertGreaterEqual(score, 0)
            self.assertLessEqual(score, 100)

    def test_block_hit_caps_score_at_59(self):
        result = lint("Guaranteed. Saturday 9 Jan, NOK 4,900, six per guide, meet 08:30.")
        self.assertLessEqual(result["score"], 59)
        self.assertEqual(result["verdict"], "BLOCK")

    def test_more_hits_never_raise_the_score(self):
        one = lint("We delve into the fjords.")["score"]
        two = lint("We delve into the fjords. Embark on a stunning journey.")["score"]
        self.assertLessEqual(two, one)

    def test_verdict_levels(self):
        self.assertEqual(lint("Saturday 9 Jan, NOK 4,900.")["verdict"], "PASS")
        self.assertEqual(lint("We delve into the fjords.")["verdict"], "REVISE")
        self.assertEqual(lint("Guaranteed snow.")["verdict"], "BLOCK")

    def test_open_verify_tokens_are_counted(self):
        result = lint("Saturday 9 Jan. Price NOK 4,900 [VERIFY: basis not given].")
        self.assertEqual(result["open_verify"], 1)

    def test_disclaimer_is_present_in_json(self):
        self.assertIn("not an AI detector", lint("Saturday.")["disclaimer"])

    def test_density_scaling_for_long_text(self):
        hit = {"id": "LEX-010", "severity": "warn", "weight": 10, "category": "lexical"}
        short_score, _ = sl.compute_score([hit], 100)
        long_score, _ = sl.compute_score([hit], 600)
        self.assertEqual(short_score, 90)
        self.assertGreater(long_score, short_score)

    def test_repeat_hits_cost_half_and_are_capped(self):
        hit = {"id": "LEX-010", "severity": "warn", "weight": 10, "category": "lexical"}
        one, _ = sl.compute_score([hit], 50)
        two, _ = sl.compute_score([hit, hit], 50)
        many, _ = sl.compute_score([hit] * 20, 50)
        self.assertEqual(one, 90)
        self.assertEqual(two, 85)
        self.assertEqual(many, 75)


class SeparationTests(unittest.TestCase):
    BAD = ("bad-1-meta-primary.txt", "bad-2-policy-risks.txt", "bad-3-chatbot-residue.txt")
    GOOD = ("good-1-meta-primary.txt", "good-2-meta-long.txt", "good-3-x-post.txt")

    def test_fixture_files_exist(self):
        for name in self.BAD + self.GOOD:
            self.assertTrue(os.path.isfile(os.path.join(FIXTURES, name)), name)

    def test_bad_ads_score_low(self):
        for name in self.BAD:
            self.assertLess(lint(read_fixture(name))["score"], 50, name)

    def test_good_ads_score_high(self):
        for name in self.GOOD:
            result = lint(read_fixture(name))
            self.assertGreaterEqual(result["score"], 90, name)
            self.assertEqual(result["counts"]["block"], 0, name)
            self.assertEqual(result["counts"]["warn"], 0, name)

    def test_scores_separate_with_a_wide_gap(self):
        bad = max(lint(read_fixture(n))["score"] for n in self.BAD)
        good = min(lint(read_fixture(n))["score"] for n in self.GOOD)
        self.assertGreaterEqual(good - bad, 40)

    def test_policy_fixture_blocks(self):
        self.assertEqual(lint(read_fixture("bad-2-policy-risks.txt"))["verdict"], "BLOCK")

    def test_good_x_post_fits_the_x_budget(self):
        result = lint(read_fixture("good-3-x-post.txt"), slot="x_post")
        self.assertEqual(result["counts"]["block"], 0)
        self.assertLessEqual(result["slot"]["chars"], 280)

    def test_good_primary_text_fits_visible_budget(self):
        result = lint(read_fixture("good-1-meta-primary.txt"), slot="meta_primary")
        self.assertLessEqual(result["slot"]["chars"], 125)
        self.assertNotIn("PLT-002", {h["id"] for h in result["hits"]})


class CliTests(unittest.TestCase):
    def test_clean_text_exits_zero(self):
        code, out, _ = run_cli("--text", "Saturday 9 Jan, NOK 4,900, six per guide.")
        self.assertEqual(code, 0)
        self.assertIn("Score 100/100", out)

    def test_bad_text_exits_one(self):
        code, out, _ = run_cli("--text", "Guaranteed fresh snow. Embark on an unforgettable adventure!")
        self.assertEqual(code, 1)
        self.assertIn("BLOCK", out)

    def test_fail_under_threshold(self):
        text = "We delve into the fjords on Saturday 9 Jan for NOK 4,900."
        code_low, _, _ = run_cli("--text", text, "--fail-under", "50")
        code_high, _, _ = run_cli("--text", text, "--fail-under", "99")
        self.assertEqual(code_low, 0)
        self.assertEqual(code_high, 1)

    def test_json_output_parses(self):
        code, out, _ = run_cli("--text", "We delve into the fjords. Embark on an unforgettable adventure!", "--json")
        data = json.loads(out)
        self.assertEqual(data["tool"], "adquill slop_lint")
        self.assertIn("score", data)
        self.assertIn("hits", data)
        self.assertIn("disclaimer", data)
        self.assertEqual(code, 1)

    def test_explain_shows_fixes(self):
        _, out, _ = run_cli("--text", "We delve into the fjords.", "--explain")
        self.assertIn("Fix:", out)
        self.assertIn("Score breakdown", out)

    def test_stdin_input(self):
        code, out, _ = run_cli("-", stdin="Saturday 9 Jan, NOK 4,900.")
        self.assertEqual(code, 0)
        self.assertIn("Score 100/100", out)

    def test_stdin_without_dash(self):
        code, out, _ = run_cli(stdin="We delve into the fjords. Embark on an unforgettable adventure!")
        self.assertIn("LEX-010", out)
        self.assertEqual(code, 1)

    def test_file_input_and_profile_detection(self):
        path = os.path.join(FIXTURES, "good-1-meta-primary.txt")
        code, out, _ = run_cli(path)
        self.assertEqual(code, 0)
        self.assertIn("profile ad", out)

    def test_markdown_file_uses_doc_profile(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "note.md")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write("# Notes\n\nMeet at 08:30 at the Brekke car park.\n")
            code, out, _ = run_cli(path)
        self.assertIn("profile doc", out)
        self.assertEqual(code, 0)

    def test_slot_flag(self):
        code, out, _ = run_cli("--text", "x" * 45, "--slot", "meta_headline")
        self.assertIn("PLT-003", out)
        self.assertIn("slot meta_headline: 45 characters of 27", out)
        self.assertEqual(code, 1)

    def test_empty_input_is_a_usage_error(self):
        code, _, err = run_cli("--text", "   ")
        self.assertEqual(code, 2)
        self.assertIn("empty", err)

    def test_unknown_rule_id_is_a_usage_error(self):
        code, _, err = run_cli("--text", "Saturday.", "--ignore-rule", "NOPE-1")
        self.assertEqual(code, 2)
        self.assertIn("unknown rule id", err)

    def test_broken_rules_file_exits_three(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = os.path.join(tmp, "bad.json")
            with open(bad, "w", encoding="utf-8") as handle:
                handle.write("[]")
            code, _, err = run_cli("--text", "Saturday.", "--rules", bad)
        self.assertEqual(code, 3)
        self.assertIn("rules error", err)

    def test_help_says_it_is_not_a_detector(self):
        code, out, _ = run_cli("--help")
        self.assertEqual(code, 0)
        self.assertIn("does not detect AI authorship", out)

    def test_list_rules(self):
        code, out, _ = run_cli("--list-rules")
        self.assertEqual(code, 0)
        self.assertIn("POL-001", out)

    def test_selftest_command(self):
        code, out, _ = run_cli("--selftest")
        self.assertEqual(code, 0)
        self.assertIn("0 failures", out)

    def test_cli_writes_no_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            before = set(os.listdir(tmp))
            run_cli(os.path.join(FIXTURES, "bad-1-meta-primary.txt"), "--json")
            self.assertEqual(set(os.listdir(tmp)), before)

    def test_source_has_no_network_or_write_calls(self):
        with open(SCRIPT, "r", encoding="utf-8") as handle:
            body = handle.read()
        for needle in ("import socket", "import urllib", "import requests", "import http",
                       "import subprocess", "import ftplib", "os.system", "'w')", '"w")', "'a')", '"a")'):
            self.assertNotIn(needle, body, needle)


if __name__ == "__main__":
    unittest.main(verbosity=1)
