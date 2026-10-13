# Tiers: every limit, its reason and its grade

The numbers below mirror `scripts/tiers.json` (version 0.3.0, verified 2026-10-07). The JSON is the source of truth. Change a number there and the validator changes with it. Then update this page.

Grades: A platform official or peer reviewed. B documented creator process or large dataset. C practitioner lore. J judgement derived from A and B inputs. Almost every limit is J: the inputs (speech rate, reading rate, working memory, platform windows) are A or B, the cut-off is ours.

## Two tiers only, three styles

The tier table and the Limits table below are the tier values, which are also the `voiceover` values. The `ugc_talk` and `ugc_text` styles override some of them; see Styles.

| | Short | Long |
|---|---|---|
| Label | Short form: Instagram Reels, YouTube Shorts, TikTok | Long form: YouTube landscape |
| platform values | reels, shorts, tiktok | youtube |
| max_seconds (block) | 25 | 200 |
| warn_seconds | 23 | 190 |
| wps (effective words per second) | 2.4 | 2.2 |
| number_penalty_seconds (per number) | 0.4 | 0.4 |

Any other length is refused. Asked for a 60 s reel, offer a 25 s reel, or a 200 s YouTube video instead. The optional `seconds` field (8 to the tier max; ugc_text 7 to 15) scales the word budget by seconds / max_seconds.

Estimated seconds = words / (wps x narrator pace) + 0.4 per number + [PAUSE n] seconds.

The budgets interact. A short hook of 9 words is allowed by H01 but needs 3.8 s at 2.4 words per second, so beat 1 (3 s) gets a T04 warning. In practice a short hook is 4 to 7 words (6 with narrator slow) and a long hook about 17 words in 8 s.

## Limits

| Limit | Short | Long | Grade | Why |
|---|---|---|---|---|
| Words, hard max | 60 | 440 | J | wps x max_seconds. Natural pace minus breaths, music and holds |
| Words, target | 40 to 55 | 320 to 400 | J | Leaves room for a breath beat and landscape holds |
| Beats, min | 4 | 14 | J | Mayer segmenting (A) |
| Beats, warn above | 6 | 22 | J | Cowan: about 4 chunks in focus (A) |
| Beats, hard max | 7 | 24 | J | |
| Seconds per beat | 3 to 6 | 6 to 15 | J | One sentence or two per beat |
| Words per beat, target | 8 to 15 | 20 to 35 | J | wps x beat length |
| Words per beat, hard max | 18 | 45 | J | |
| Hook | Beat 1 ends by 3 s, 4 to 9 words, hard max 10 | Verbal hook by 8 s, max 22 words | B | TikTok: proposition in the first 3 s (A). YouTube intro metric is the first 30 s (A) |
| Promise (long) | n/a | Promise beat ends by 30 s, max 70 words up to its end | A/J | YouTube intro: did the first 30 s match the title |
| Facts per beat | 1 | 2, of which 1 number | J | Cowan 3 to 5 chunks (A) |
| Facts per script | 3 | 14 | J | |
| Numbers per script | 2 | 6 | J | Spoken numbers are hard to hold |
| Sentence average | 6 to 9 words | 8 to 12 words | C/J | Broadcast style: one idea per sentence |
| Sentence hard max | 12 words | 18 words | C/J | |
| Overlay words | 6 | 8 | B/J | |
| Overlay characters per line | 32 | 42 | B/J | Netflix 42 per line (A). Vertical safe box fits fewer |
| Overlay lines | 2 | 2 | B | Netflix |
| Overlay min on screen | 1.5 s | 2 s | J | |
| Overlay reading speed | 15 characters per second | 15 characters per second | J | Netflix 20, slowed for footage plus voice |
| CTA count | exactly 1 cta beat | exactly 1 cta beat plus at most 1 soft-cta beat (2 asks max) | J | TikTok asks for a clear call to action (A). One primary ask |
| CTA words | 8 | 25 | J | |
| CTA position | starts in the last 4 s | starts in the last 20 s; soft-cta after 30 s and after the first mini-payoff | J | Measured back from the declared end of the last beat, not from the tier maximum |
| Seconds per shot | 3 | 6 | C | Editors cut every 1 to 3 s (short), 3 to 6 s (long) |
| Static shot hard max | 4 s | n/a | C | |
| Pattern interrupt | n/a | every 40 s | C/J | MrBeast re-engagement marks, scaled from a 13 min video |
| Chapters | n/a | 4 to 6, one mini-payoff each | J | Blackman: set up, tension, payoff every 1 to 2 min (B) |
| Dominant loop opens by | 3 s | 8 s | J | |
| Dominant loop closes by | last or second-last beat | 185 s | J | Leaves room for the call to action |
| Supporting loops | not allowed | allowed | J | 25 s has no time to close two loops |
| Loops open at once | 1 | 2 | J | Cowan |
| Partial answer window | n/a | 80 to 120 s | J | |
| Re-engagement windows | n/a | 55 to 80 s and 120 to 145 s | J/B | Where a 200 s curve usually dips |

## Styles

Front matter `style:` picks one of voiceover, ugc_talk or ugc_text. Left out, it is voiceover. A TikTok script sets it explicitly. ugc_text is short only; in a long script it is a parse error. Each style overrides tier values for that style only; nested values merge key by key. Facts limits are never raised by a style. Brand rules run in every style.

Rendered from `styles` in tiers.json. Tier value is the voiceover value; n/a means the key exists only for the style.

| Style | Tier | Key | Tier value | Style value |
|---|---|---|---|---|
| voiceover | short | none | | no overrides |
| voiceover | long | none | | no overrides |
| ugc_talk | short | wps | 2.4 | 3.0 |
| ugc_talk | short | words.hard_max | 60 | 75 |
| ugc_talk | short | words.target_min | 40 | 55 |
| ugc_talk | short | words.target_max | 55 | 68 |
| ugc_talk | short | words_per_beat.target_min | 8 | 10 |
| ugc_talk | short | words_per_beat.target_max | 15 | 20 |
| ugc_talk | short | words_per_beat.hard_max | 18 | 24 |
| ugc_talk | short | sentence.avg_min | 6 | 7 |
| ugc_talk | short | sentence.avg_max | 9 | 12 |
| ugc_talk | short | sentence.hard_max_words | 12 | 16 |
| ugc_talk | short | hook.max_seconds | 3 | 3 |
| ugc_talk | short | hook.max_seconds_with_overlay | n/a | 4 |
| ugc_talk | short | hook.min_words | 4 | 4 |
| ugc_talk | short | hook.max_words | 9 | 15 |
| ugc_talk | short | hook.hard_max_words | 10 | 15 |
| ugc_talk | short | hook.first_word_by_seconds | n/a | 0.5 |
| ugc_talk | short | hook.first_sentence_min_words | n/a | 6 |
| ugc_talk | short | hook.first_sentence_max_words | n/a | 15 |
| ugc_talk | short | overlay.max_words | 6 | 8 |
| ugc_talk | short | overlay.max_chars_per_line | 32 | 40 |
| ugc_talk | short | cta.min | 1 | 0 |
| ugc_talk | short | cta.max | 1 | 1 |
| ugc_talk | short | cta.hard_max | 1 | 1 |
| ugc_talk | short | cta.max_words | 8 | 10 |
| ugc_talk | short | cta.last_seconds | 4 | 5 |
| ugc_talk | short | casual.markers_max_per_100_words | n/a | 2 |
| ugc_talk | short | casual.contractions_min_per_100_words | n/a | 1 |
| ugc_talk | long | wps | 2.2 | 2.8 |
| ugc_talk | long | words.hard_max | 440 | 560 |
| ugc_talk | long | words.target_min | 320 | 420 |
| ugc_talk | long | words.target_max | 400 | 520 |
| ugc_talk | long | sentence.hard_max_words | 18 | 20 |
| ugc_talk | long | casual.markers_max_per_100_words | n/a | 2 |
| ugc_talk | long | casual.contractions_min_per_100_words | n/a | 1 |
| ugc_text | short | max_seconds | 25 | 15 |
| ugc_text | short | min_seconds | n/a | 7 |
| ugc_text | short | warn_seconds | 23 | 15 |
| ugc_text | short | words.hard_max | 60 | 12 |
| ugc_text | short | words.target_min | 40 | 0 |
| ugc_text | short | words.target_max | 55 | 12 |
| ugc_text | short | words.scale_with_seconds | n/a | false |
| ugc_text | short | words_per_beat.target_min | 8 | 0 |
| ugc_text | short | words_per_beat.target_max | 15 | 12 |
| ugc_text | short | words_per_beat.hard_max | 18 | 12 |
| ugc_text | short | beats.min | 4 | 1 |
| ugc_text | short | beats.target_max | 6 | 3 |
| ugc_text | short | beats.hard_max | 7 | 3 |
| ugc_text | short | seconds_per_beat.min | 3 | 2 |
| ugc_text | short | seconds_per_beat.max | 6 | 15 |
| ugc_text | short | hook.max_seconds | 3 | 15 |
| ugc_text | short | hook.min_words | 4 | 0 |
| ugc_text | short | hook.max_words | 9 | 12 |
| ugc_text | short | hook.hard_max_words | 10 | 12 |
| ugc_text | short | facts.per_beat_max | 1 | 1 |
| ugc_text | short | facts.per_script_max | 3 | 1 |
| ugc_text | short | facts.numbers_per_script_max | 2 | 2 |
| ugc_text | short | sentence.avg_min | 6 | 1 |
| ugc_text | short | sentence.avg_max | 9 | 12 |
| ugc_text | short | sentence.hard_max_words | 12 | 12 |
| ugc_text | short | overlay.max_words | 6 | 12 |
| ugc_text | short | overlay.max_chars_per_line | 32 | 40 |
| ugc_text | short | overlay.max_lines | 2 | 2 |
| ugc_text | short | overlay.min_seconds | 1.5 | 2 |
| ugc_text | short | overlay.chars_per_second | 15 | 15 |
| ugc_text | short | overlay.persistent | n/a | true |
| ugc_text | short | overlay.script_min_words | n/a | 4 |
| ugc_text | short | overlay.script_max_words | n/a | 12 |
| ugc_text | short | overlay.script_max_lines | n/a | 2 |
| ugc_text | short | overlay.required_in_first_beat | n/a | true |
| ugc_text | short | cta.min | 1 | 0 |
| ugc_text | short | cta.max | 1 | 1 |
| ugc_text | short | cta.hard_max | 1 | 1 |
| ugc_text | short | cta.max_words | 8 | 8 |
| ugc_text | short | cta.last_seconds | 4 | 4 |
| ugc_text | short | visual.max_seconds_per_shot | 3 | 8 |
| ugc_text | short | visual.hard_max_static_seconds | 4 | 15 |
| ugc_text | short | loops.close_in_last_beat | n/a | true |

Grades, from the evidence fields in tiers.json: ugc_talk short wps 3.0 is J, our chosen value, set below the 3.3 to 4.9 measured on purpose (the extra speed is connective talk, not more facts, and many of our guides speak English as a second language). Measured inputs: top five creators 3.3 to 4.9 (note 04, C), talking clips of 45 s or less 3.46 median (note 06, n = 6, C), micro creators 2.87 pooled median (note 05, 49 videos, C). ugc_talk long wps 2.8 is J (long spoken micro videos 2.3 to 3.1, C). Hook timing and length are C inputs with a J cut-off. ugc_text limits come from one creator's eight text posts and another's 528,500-view tips post (C); spoken max 12 and 1 fact are J.

Where each style rule runs: H02 and H03 voiceover only. U01, U02, U04, U05, U07 in ugc_talk and ugc_text. U03 and U06 in ugc_talk only. D01 in the ugc styles, and in voiceover only when `relationship:` is written. SND01 in every style. R04 in every style when the validator is given a file.

### Front matter fields

| Field | Allowed | Default | Read by |
|---|---|---|---|
| style | voiceover, ugc_talk, ugc_text | voiceover | Every limit above |
| creator | guide, guest, staff, editor | guide | The report; changes no limit |
| relationship | staff, guide, guest_paid, guest_gifted, guest_unpaid | staff | D01 |
| sound | original, commercial_library, voiceover_only, trending, none | original | SND01 |

A value outside the list is a parse error (exit 2) naming the line.

### Disclosure (D01) and sound (SND01) settings

| Setting | Value |
|---|---|
| disclosure.within_seconds | 5: the `disclosure` beat must start by then |
| disclosure.ad_label_required | guest_paid, guest_gifted: caption starts with Ad, #ad, Advert, Advertisement, Reklame or Annonse, and the disclosure beat says so (block) |
| disclosure.role_line_expected | staff, guide: the disclosure beat names the role or the brand (warn) |
| disclosure.paid_words | ad, advert, advertisement, paid, paid partnership, sponsored, gifted, free trip, for free, invited, hosted, comped, partnership, partnered, reklame. A paid word right after a negation in the same clause (not an ad, I'm not paid) does not count (paid_negation_regex) |
| disclosure.overlay_required | true: the disclosure beat needs on-screen text (warn), because many viewers watch muted |
| disclosure.overlay_max_words | 6: in ugc_text the overlay on a disclosure beat that is not the hook is counted apart from the 2 content lines |
| caption_chapters | C06 (warn): YouTube long. At least 3 chapter lines in the caption, first at 0:00, 10 s apart, each within 1 s of a beat start; timestamps are not numbers for F04 |
| sources.quote_required_regex | `\bbrief\b`: F06 warns (blocks with --final) when a row verified yes names a brief in its source and quotes nothing |
| example_copy | R04 (warn): 5-word runs shared with `examples/` or `assets/`; 2 distinct shared runs (a 6-word copy gives two) in the voiceover, or 2 in the visual and overlay cells, warn. Also 3 shots that restate reference shots (60 percent of a reference shot's content words, 3 content words minimum) |
| disclosure.role_words | guide, guides, guiding, instructor, staff, team, employee, work for, work at, work with, i run, we run, owner, founder, co-founder, plus the brand name |
| sound.blocked_value | trending, when the voiceover, overlay or caption names the brand, a trip word (tour, trip, booking, book, package, holiday, departure, weekend, getaway, excursion, itinerary and plurals) or a price |

Grades: disclosure rests on FTC Disclosures 101 (A), ASA (B) and TikTok Commercial Disclosure (A); sound on the TikTok Commercial Music Library page (A). Legal reading is [VERIFY with counsel]; see references/ugc-style.md.

## How the validator counts

Run `python3 -I .claude/skills/scriptcraft/scripts/script_check.py --explain RULE_ID` for any rule. The short version:

| Thing | Counted as |
|---|---|
| Words | Spoken voiceover words. Hyphenated parts count separately ("a-little-cold" is 3). `[PAUSE n]` is time, not words. A `[VERIFY: ...]` note counts as 1 word |
| Numbers | Every digit group: "12 Feb 2027" is 2 numbers, "NOK 1,950" and "NOK 1 950" are 1. Spelled two and up also count ("two", "twenty-five"). "one" never counts |
| Numbers that need a facts row (F04) | Every digit, and every spelled number from twenty up, in voiceover, overlay and caption. In a beat, the row must be cited in that beat's facts column |
| Names | Capitalized words mid-sentence, plus known place names (brand_rules.json place_names) and names already seen mid-sentence, even at a sentence start. The full brand name is exempt; its parts are not |
| Facts per beat | Cited fact ids, plus any number or name not covered by a cited row |
| Facts per script | The distinct facts the beats carry. Rows no beat cites do not count |
| Caption | Not timed or budgeted, but its digits must be in a verified facts row (F04), and it is checked for dashes, emojis and brand rules |
| Silent holds | An `[INFO]` line marks any beat whose declared time is more than 3 s above its estimate. Fill it with a `[PAUSE n]` for natural sound, or give the time to another beat |

## Narrators

| Profile | pace | word_scale | Use for |
|---|---|---|---|
| standard | 1.0 | 1.0 | Native or fluent English voiceover at a natural, not rushed, pace |
| slow | 0.85 | 0.85 | Non-native narrator, text-to-speech, or a deliberately calm read. Cuts the word budget by 15 percent |

With `slow`, the hard max becomes 51 words (short) and 374 words (long) in voiceover, before any `seconds` scaling. In ugc_talk, 75 becomes 64 (short) and 560 becomes 476 (long).

## Roles

Common: hook, setup, build, shift, explain, proof, payoff, cta, disclosure. `disclosure` marks the beat that says who the creator is to the brand (D01). Long only: promise, partial, progress, reengage, soft-cta. Chapters: ch:1 to ch:6, with mini:1 to mini:6 on the beat that answers that chapter's small question. Loops: open:A and close:A, any single capital letter.

## Acronym allowlist

CTA, POV, UGC, NOK, USD, EUR, UK, EU, US, FAQ, DM, GPS, SOS, TV, AM, PM, OK, HQ, RV. Any other word of 3 or more capitals is treated as shouting (R02).

## Where the numbers come from

- Speech: edX data, mean 156 wpm, 2.6 words per second (Guo, Kim, Rubin 2014, A). Voiceover guides about 2.5 (C). Creator videos measured at a median 2.75 (C, n=14). Effective rates are lower once breaths and holds are counted.
- UGC speech: notes 04 to 06, summarised in references/ugc-style.md and references/creator-patterns.md (C).
- Hook: TikTok creative best practices, "Introduce your content proposition in the first 3 seconds" (A). YouTube Help: intro is "after the first 30 seconds" (A).
- Density: Cowan 2001 and 2010, about 4 chunks (A). Mayer redundancy and segmenting principles (A).
- Overlays: Netflix English timed text, 42 characters per line, 2 lines (A).

Open calibration item: time 5 real reads by the Outdoor Norway voice and adjust wps and the number penalty in tiers.json.
