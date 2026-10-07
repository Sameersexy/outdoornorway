# Tiers: every limit, its reason and its grade

The numbers below mirror `scripts/tiers.json` (version 0.1.0, verified 2026-10-07). The JSON is the source of truth. Change a number there and the validator changes with it. Then update this page.

Grades: A platform official or peer reviewed. B documented creator process or large dataset. C practitioner lore. J judgement derived from A and B inputs. Almost every limit is J: the inputs (speech rate, reading rate, working memory, platform windows) are A or B, the cut-off is ours.

## Two tiers only

| | Short | Long |
|---|---|---|
| Label | Short form: Instagram Reels, YouTube Shorts, TikTok | Long form: YouTube landscape |
| platform values | reels, shorts, tiktok | youtube |
| max_seconds (block) | 25 | 200 |
| warn_seconds | 23 | 190 |
| wps (effective words per second) | 2.4 | 2.2 |
| number_penalty_seconds (per number) | 0.4 | 0.4 |

Any other length is refused. A 60 s reel is either a 25 s short or a 200 s long. The optional `seconds` field (8 to the tier max) scales the word budget by seconds / max_seconds.

Estimated seconds = words / (wps x narrator pace) + 0.4 per number + [PAUSE n] seconds.

The budgets interact. A short hook of 9 words is allowed by H01 but needs 3.8 s at 2.4 words per second, so beat 1 (3 s) gets a T04 warning. In practice a short hook is 4 to 7 words and a long hook about 17 words in 8 s.

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
| CTA count | exactly 1 | 1 or 2, of which soft mid-roll max 1 | J | TikTok asks for a clear call to action (A) |
| CTA words | 8 | 25 | J | |
| CTA position | starts in the last 4 s | starts in the last 20 s | J | |
| Seconds per shot | 3 | 6 | C | Editors cut every 1 to 3 s (short), 3 to 6 s (long) |
| Static shot hard max | 4 s | n/a | C | |
| Pattern interrupt | n/a | every 40 s | B/J | MrBeast re-engagement marks, scaled |
| Chapters | n/a | 4 to 6, one mini-payoff each | J | Blackman: set up, tension, payoff every 1 to 2 min (B) |
| Dominant loop opens by | 3 s | 8 s | J | |
| Dominant loop closes by | last or second-last beat | 185 s | J | Leaves room for the call to action |
| Supporting loops | not allowed | allowed | J | 25 s has no time to close two loops |
| Loops open at once | 1 | 2 | J | Cowan |
| Partial answer window | n/a | 80 to 120 s | J | |
| Re-engagement windows | n/a | 55 to 80 s and 120 to 145 s | J/B | Where a 200 s curve usually dips |

## Narrators

| Profile | pace | word_scale | Use for |
|---|---|---|---|
| standard | 1.0 | 1.0 | Native or fluent English voiceover at a natural, not rushed, pace |
| slow | 0.85 | 0.85 | Non-native narrator, text-to-speech, or a deliberately calm read. Cuts the word budget by 15 percent |

With `slow`, the hard max becomes 51 words (short) and 374 words (long), before any `seconds` scaling.

## Roles

Common: hook, setup, build, shift, explain, proof, payoff, cta. Long only: promise, partial, progress, reengage, soft-cta. Chapters: ch:1 to ch:6, with mini:1 to mini:6 on the beat that answers that chapter's small question. Loops: open:A and close:A, any single capital letter.

## Acronym allowlist

CTA, POV, UGC, NOK, USD, EUR, UK, EU, US, FAQ, DM, GPS, SOS, TV, AM, PM, OK, HQ, RV. Any other word of 3 or more capitals is treated as shouting (R02).

## Where the numbers come from

- Speech: edX data, mean 156 wpm, 2.6 words per second (Guo, Kim, Rubin 2014, A). Voiceover guides about 2.5 (C). Creator videos measured at a median 2.75 (C, n=14). Effective rates are lower once breaths and holds are counted.
- Hook: TikTok creative best practices, "Introduce your content proposition in the first 3 seconds" (A). YouTube Help: intro is "after the first 30 seconds" (A).
- Density: Cowan 2001 and 2010, about 4 chunks (A). Mayer redundancy and segmenting principles (A).
- Overlays: Netflix English timed text, 42 characters per line, 2 lines (A).

Open calibration item: time 5 real reads by the Outdoor Norway voice and adjust wps and the number penalty in tiers.json.
