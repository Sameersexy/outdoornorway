# End-to-end agent tests of scriptcraft

Four scripts written by the script-writer agent and reviewed by a separate script-reviewer agent that reran the validator itself. The aim was to see what the validator catches, what only a reviewer catches, and whether a rewrite loop converges.

Limits of this evidence: four scripts, one reviewer run each, writer and reviewer from the same model family, scores are model judgement and not audience results. Treat the pattern as a finding, not a measurement.

## Scores (1 to 10, reviewer's own)

| Item | Long voiceover (fictional brand) | ugc_talk, first run | ugc_talk, thin brief, round 1 | ugc_talk, thin brief, round 2 |
|---|---|---|---|---|
| Hook strength | 5 | 5 | 6 | 5 |
| Loop quality | 4 | 5 | 5 | 4 |
| Overload | 7 | 7 | 8 | 6 |
| Visual hook | 6 | 5 | 5 | 4 |
| Guest benefit | 5 | 5 | 6 | 4 |
| Brand voice | 4 | 5 | 5 | 5 |
| Facts | 4 | 4 | 5 | 8 |
| Sounds human | 4 | 5 | 6 | 6 |
| Distinct | 4 | 4 | 5 | 6 |
| Objection | 5 | 5 | 4 | 7 |
| Validator, draft | PASS | PASS | PASS | PASS |
| Reviewer verdict | REJECT | REJECT | REVISE | REVISE |

Note on the second column: one of its blocking findings came from a review prompt that left out the audience line the writer had received. It was a false finding, and the other findings stood.

## What the validator caught and what it did not

Every script passed the draft validator. The reviewer found, in each one:

- Overstated facts: lines claiming more than the cited row ("whoever skis gets a lesson on each ski day"), and a facts row marked verified yes against a brief that did not say it.
- Copied shapes: example shots and call-to-action shapes lifted or paraphrased from the examples.
- Bland voice: no sensory detail, brochure lines, a guide calling themself "a guide", a reveal said three times.
- Disclosure said aloud but never shown on screen.

## Validator changes the tests caused

| Gap found | Change |
|---|---|
| Example shots and lines copied | R04 warns on shared word runs, and on 3 shots that restate reference shots by content words |
| Disclosure spoken but not shown | D01 warns when the disclosure beat has no on-screen text; ugc_text counts that line apart from its 2 content lines |
| Placeholder in the caption passed --final | BR13 covers the caption and, after round 2, visual cells |
| Row verified yes from a brief with no quote | F06 warns, and blocks with --final |
| Voiceover script with no relationship line skipped disclosure silently | The report prints an [INFO] line |
| tours.json had no day plans, so the writer could not state that day 2 is a snowshoe hike | `itinerary` list for the five multi-day tours, headings checked against the live pages by verify_tours.py |

In this round the suite grew from 224 to 247 unit tests, and the attack harness stayed at 81 cases with 0 mismatches. Both counts date from this round. The suite has grown since, so run it for the current count.

## The loop

Round 1 to round 2 on the thin brief: facts 5 to 8, objection 4 to 7, distinct 5 to 6. Hook 6 to 5, loop 5 to 4, visual hook 5 to 4, guest benefit 6 to 4. The writer removed the unverified premise (a non-skier can join), which was right, and the hook lost the stake that rested on it. The reviewer's diagnosis: with no real moment from a real trip, the script is a guide alone in a forest reading the day plan.

Conclusion: more rewrite rounds do not fix a thin brief. The input has to come from the guide. The skill now ships `assets/guide-moment-intake.md` (ten short questions) for that, and the writer is told to wait for the answers instead of padding.

## Open questions for the client from these tests

- Can someone who does not ski book the 3-Day Ski and Snowshoe Experience? The tour page says prior hiking and skiing experience is recommended, and days 1 and 3 are ski days. The snowshoe day tour may be the right product for a non-skier video.
- The 3-Day Ski and Snowshoe page still shows NOK 13,462 against the hub's NOK 17,451.
- Which TikTok disclosure toggle a guide's own post should use, and whether "Advertisement" is the right caption label for Norway [VERIFY with counsel].
