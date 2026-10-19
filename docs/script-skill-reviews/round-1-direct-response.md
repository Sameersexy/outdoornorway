# Round 1 review: scriptcraft, direct response and validator attack

Reviewer: Dana Whitfield, direct-response chief (composite persona, `adquill/agents/direct-response-chief.md`).
Subject: `.claude/skills/scriptcraft/` (SKILL.md, references, assets, examples, scripts) and `.claude/agents/script-writer.md`, `.claude/agents/script-reviewer.md`.
Date: 2026-10-07.

## Direct-response review

Verdict: REVISE
Overall: 7/10

| Dimension | Score | One-line reason |
|---|---|---|
| Offer clarity | 7 | Templates push price to the CTA overlay and dates to the caption; the buyer gets the offer, but late and partly off-screen |
| Specificity | 8 | Facts table, numbers exactly as spoken, and "describe difficulty by what the day involves" all force concrete lines |
| Is-it-for-me signal | 8 | "You" in the hook window is checked (H03), personal-attribute address is caught (BR08), anxieties table is good |
| Objection handling | 7 | Anxiety table is strong; nothing in code or the writer workflow requires the top objection to be answered |
| CTA and message match | 5 | Doc says one primary CTA, soft CTA never before 30 s, no stacked asks. Code allows 4 asks in a long and a mid-script "book" in a short |
| Proof and honesty | 6 | F04 is a good idea with three holes: spelled numbers, reused digits, and superlatives whitelisted by any row that contains the word |
| Policy risk | 6 | The aurora guarantee rule can be passed with a one-line rewrite. That is the client's top claims rule |
| Testability | 7 | Beat table makes variants easy to cut; the skill never asks for a variant or a hypothesis |

### Blocking issues

1. [`scripts/brand_rules.json` BR09 and BR10, and `scripts/script_check.py` `check_brand` with `NEGATION_RE`] The aurora and snow guarantee rules can be passed. Exact inputs that returned `RESULT: PASS` (beat 5 of the short example, everything else unchanged):
   - "Not a chance you miss the northern lights." BR09 has no guarantee word to match, and BR10's `requires_regex` accepts "a chance" inside "not a chance". Zero findings.
   - "The aurora shows up, no question, guaranteed." with the CTA changed to "Send this. There's a chance of cloud." BR09 skips the match because "no" sits inside the 25 character negation window; BR10 is satisfied by "chance of" anywhere in the script.
   - "Snow is certain, and you ski down warm." The second alternation of BR09 lacks `certain`, and the first needs the guarantee word before the noun.
   - "Fresh powder every morning. You ski down warm." `every (night|time|trip)` misses morning, day, week, weekend.
   Fix direction: treat negation as safe only when it governs the guarantee verb directly ("can't promise", "no guarantee", "not guaranteed"), never "no question", "no doubt", "not a chance", "no exceptions"; drop bare "a chance" from BR10 or exclude "not a chance|no chance"; add `certain\w*`, `sure thing` and `every (day|morning|week|weekend|winter)` to the phenomenon-first alternation. Add each input above as a fixture. brand_rules.json is owned elsewhere, so the owner must make the regex change; the negation logic is in script_check.py.

2. [`scripts/script_check.py` `check_facts` F04 and `SPELLED`; `references/brand-and-claims.md` "Facts and [VERIFY]"] Invented numbers pass F04. Exact inputs that returned `RESULT: PASS`:
   - "Ninety percent of guests overdress. So you peel one off." Spelled numbers above twenty are not counted at all, so an invented statistic has no density cost and no facts check.
   - "Wet layers chill fast. Ninety seconds and you peel one off." Same hole.
   - "10 guides watch your group. You peel one off." with that beat's facts cell set to "-". The digit 10 exists in F1 ("10 minutes into every climb"), so F04 is satisfied by a row about a different claim.
   Fix direction: count every spelled cardinal (twenty-one to ninety-nine, "a hundred", "percent", "half" optional) as a number for F03 and F04; for F04 require the digit to appear in a row the beat declares in its facts column (block in `--final`, warn in draft), so a reused number in a new claim is caught. The docs then say "a number is tied to the row you cite in that beat".

3. [`scripts/script_check.py` `superlative_hits`] Superlatives are whitelisted by any facts row anywhere. Exact input: add the row `| F3 | Guests say the best part is the waffle | fictional: guest review | yes |` and set beat 5 to "The best ski guides in Norway keep you warm." Result: `RESULT: PASS` with zero findings ("Norway" also escapes F07 because it is part of the brand name "Outdoor Norway"). Fix direction: allow a BR11 word only in a beat whose facts column cites a row containing that word, and exempt only the full brand string from F07, not its parts.

4. [`scripts/script_check.py` `check_cta` C01 and C02; `references/long-form.md` "Call to action"; `SKILL.md` "What changed" row "No call to action"] The CTA rules in the docs are not the CTA rules in code. long-form.md says "One primary CTA", soft CTA "Never in the first 30 s", "No stacked asks". tiers.json `cta.max` is 2 and the validator counts `soft-cta` separately, so a long can carry 2 hard plus 1 soft. Exact input: the long example with `promise, soft-cta` on beat 2 (8 to 19 s), beat 16 "Book a date from the link below. Follow for the next tour." (cta) and beat 17 "Subscribe, and send this to the friend who rides lifts." (cta). Four asks, one inside the promise: `RESULT: PASS`. In the short tier, "Save this, follow, and book your seat." as the single CTA passes, and "10 minutes in, you sweat. Book from the link below." in a `build` beat passes with no warning. Fix direction: make C01 count hard plus soft against `cta.max` and hard alone against 1 (or document that `max` 2 means one hard plus one soft and enforce exactly that); add a check that `soft-cta` starts after `hook.promise_by_seconds` and after the first `mini:` beat; warn when a cta beat holds more than one CTA verb (send, save, follow, subscribe, book, comment, like) and when a non-cta beat contains "link below", "book", "subscribe" as an imperative.

### Number and fact check

Research claims in the skill (checked against `docs/research/video-scripts/03-hook-retention-pacing.md` and `docs/research/video-scripts/01-educational-voiceover.md`):
- Zeigarnik meta-analysis, 59 studies, recall ratio 0.99, Ghibellini and Meier 2025: pass, matches 03 section 9.
- Ovsiankina resumption tendency from the same meta-analysis: pass.
- Gruber, Gelman and Ranganath 2014, curiosity and memory: pass.
- TikTok "Introduce your content proposition in the first 3 seconds": pass, 01 N6 and 02 line 51.
- Netflix 42 characters per line, 2 lines: pass.
- "Sends per reach" named by Mosseri: pass, graded B in research and B in short-form.md. Correctly not overstated.
- Real Outdoor Norway facts quoted in short-form.md and brand-and-claims.md (NOK 1,948, NOK 42,126, Bergen to Voss about an hour, do-not-claim list): consistent with the brief; not every tours.json key was reopened in this round.

Applied test scripts (fictional brief): every number is in a facts row copied from the brief. 4,900 (F3 short, F5 long), 3 (F3, F1), 12 and 19 Feb 2027 (caption only, F4 short, F6 long), February 2027 (F6 long). Pass. "Small groups" stays a phrase, no number. One open item: ski levels the lessons suit (`[VERIFY]` in beat 11 of the long, so `--final` fails by design).

## Validator attack

Base files: the passing examples, copied to a short and a long base script, one change per test. Command: `python3 -I .claude/skills/scriptcraft/scripts/script_check.py FILE`.

### Should FAIL (all caught)

| File | Exact change | Result |
|---|---|---|
| f1-words.md | Beats 2 to 5 padded, e.g. "You start the long climb from the van wearing every warm layer you own." | FAIL (8 blocking): T01 30.8 s, W01 73 words, T04, S01 |
| f2-facts.md | "You start the climb in Lindvik wearing every layer.", "So we stop at Myrdal", F2 declared in beat 2 | FAIL (3 blocking): F01 twice, F02 4 facts |
| f3-hook.md | Hook "Your guide wants you a little cold on the climb up today." | FAIL: H01 12 words, T04 |
| f4-twocta.md | Beat 5 role "payoff, close:A, cta" | FAIL: C01 2 cta beats, C02, C03 |
| f5-aurora.md | Beat 5 "Stay dry, and you will see the aurora for sure." | FAIL: BR09, BR10 |
| f6-number.md | Beat 4 "Wet layers chill in 4 minutes. So you peel one off." | FAIL: F04 number 4, F01 |
| f7-loop.md | Beat 5 role "payoff" (close:A removed) | FAIL: L01 |
| f8-longloop.md | Long beat 15 role "payoff" (close:A removed) | FAIL: L01 loop A never closes |
| a17.md | "Northern lights every night. No one can promise more." | FAIL: BR09 (negation is after, so not skipped) |
| a18.md | "You never miss the aurora with us. Never." | FAIL: BR10 |
| a19.md | "The aurora is guaranteed, no doubt about it." | FAIL: BR09 |

### False negatives (should FAIL, returned PASS)

| File | Exact input | Why it passes | Severity |
|---|---|---|---|
| a1.md | "Not a chance you miss the northern lights." | BR10 accepts "a chance"; no guarantee word for BR09 | Blocking 1 |
| a20.md | "The aurora shows up, no question, guaranteed." plus CTA "Send this. There's a chance of cloud." | Negation window sees "no"; BR10 sees "chance of" | Blocking 1 |
| a2.md | "Snow is certain, and you ski down warm." | `certain` missing after the noun | Blocking 1 |
| a2b.md | "Fresh powder every morning. You ski down warm." | `every morning` not in the list | Blocking 1 |
| a3.md | "Ninety percent of guests overdress. So you peel one off." | Spelled numbers over twenty ignored | Blocking 2 |
| a15.md | "Wet layers chill fast. Ninety seconds and you peel one off." | Same | Blocking 2 |
| a7.md | "10 guides watch your group. You peel one off." (facts cell "-") | Digit 10 matched to the unrelated F1 row | Blocking 2 |
| a9.md | Row "Guests say the best part is the waffle", line "The best ski guides in Norway keep you warm." | Any row with "best" whitelists all "best" | Blocking 3 |
| a12.md | Long with soft-cta inside the promise and two hard cta beats, 4 asks | C01 counts hard and soft separately; no soft-cta timing check | Blocking 4 |
| a5.md | CTA "Save this, follow, and book your seat." | Stacked asks not checked | Blocking 4 |
| a6.md | Beat 3 "10 minutes in, you sweat. Book from the link below." | CTA outside the cta beat not checked | Blocking 4 |
| a4.md | Hook "Your guide wants you a little-bit-cold-on-the-first-climb-of-the-day." | `WORD_RE` joins hyphenated chains: 14 spoken words count as 7. Only a BR14 warning | Non-blocking, fix soon |
| a10.md | "Seats are going fast. You ski down warm." | Scarcity list misses "going fast", "filling up" | Non-blocking |
| a11.md | "World-class guides, and you ski down warm." | BR11 misses world-class, unbeatable, leading, premier | Non-blocking |
| a8.md | "Myrdal is where you start, in every warm layer." | Sentence-initial names are not names: no F01 unit, no F07 | Non-blocking |
| a13.md | Row "Brekke has a 100% safety record \| the brief \| yes", line "Our record is 100% safe." | By design: code cannot judge a source. The reviewer agent must open it | Reviewer's job |

### Should PASS

| File | Input | Result |
|---|---|---|
| p1.md | "No one can promise you the northern lights." | PASS, correct |
| p2.md | "No guide can guarantee snow. You ski down warm." | PASS, correct |
| p3.md | Slow narrator, `seconds: 20`, 5 beats, 33 words | PASS with 3 warnings (T04 on a 7 word hook, W03, S01 average) |
| p4b.md | CTA overlay "From NOK 1,950", row "Day tours from NOK 1,950 per adult", CTA "Send this before your first tour." | PASS, correct ("your first" is ordinary) |
| brekke-short.md, brekke-long.md | Applied test below | PASS |

### False positives (should PASS, returned FAIL)

| File | Exact input | Result | Fix direction |
|---|---|---|---|
| p4.md | Overlay "From NOK 1 950" (Norwegian thousands space), row says "NOK 1,950" | FAIL (5 blocking): F04 on "1" and "950", F01, F02, F03 | The contract says numbers are compared "after removing commas and spaces and NOK". Join `\d{1,3}( \d{3})+` before `NUM_RE` on the script side, as the fact side already does |
| brekke-long.md draft 1 | "[VERIFY: which ski levels the lessons suit, Brekke Ski Guides] Your guide plans..." | S01 block, sentence of 21 words | Placeholder text is counted as spoken words and sentence length, but stripped for names. Strip `BRACKET_RE` before counting words, or count a placeholder as a fixed 3 words |

## Mandatory applied test: Brekke Ski Guides (fictional)

Files: `brekke-short.md` (Reels, 25 s) and `brekke-long.md` (YouTube, 192 s). These test scripts are not kept in this repo.

Final validator lines:
- brekke-short.md: `TOTAL words 50 | est 20.8 s | declared end 25 s | beats 6 | facts 3 | numbers 2`, `RESULT: PASS`. With `--final`: `RESULT: PASS`. With `--strict`: `RESULT: PASS`.
- brekke-long.md: `TOTAL words 357 | est 163.5 s | declared end 192 s | beats 16 | facts 6 | numbers 3`, `RESULT: PASS`. With `--strict`: `RESULT: PASS`. With `--final`: `RESULT: FAIL (1 blocking, 0 warnings)`, BR13 on `[verify: lesson levels, brekke]`, listed as the open item for the client.

Short script (beats, as validated):

| beat | time | voiceover | text | role |
|---|---|---|---|---|
| 1 | 0-3 | Half your group skis. Half doesn't. | Skiers and non-skiers? | hook, open:A |
| 2 | 3-7 | You still want one weekend away, all of you. | - | setup |
| 3 | 7-12 | Each ski day starts with a lesson from your guide. | A lesson each ski day | build |
| 4 | 12-17 | The ones who don't ski get a snowshoe day. | Snowshoe day | shift, explain |
| 5 | 17-21 | Different days out. One weekend, all of you. | Same weekend | payoff, close:A |
| 6 | 21-25 | Send this to the friend who won't ski. | 3 days from NOK 4,900 | cta |

Caption carries the dates: "Departures 12 Feb and 19 Feb 2027."

Iterations: short passed on the first run. I then changed beat 5 by hand from "One table at night" because it implied a shared dinner the brief never mentions; the validator had passed it. Long needed two runs: run 1 failed F01 ("two departures, both in February 2027" counted "two" and "2027") and S01 (the placeholder sentence). More important, my first long draft contained five invented claims that the validator passed: "The guide watches you ski first, then picks one thing to work on", "That covers the guiding and a lesson", "strap them on over winter boots", "If you can walk on a winter path, you can snowshoe", "works for school holidays". I removed them by reading against the brief. The code cannot catch this; the reviewer agent's Step 2 can, if it reads every sentence and not only the facts rows.

### Honest judgement

- Easy to follow? Yes for the short. The template beat word ranges (4 to 7, 8 to 10, 8 to 12) land inside every limit, and the short passed first time. The long template is also accurate: copying its timings passed L01, the reengage windows and the partial window with no fiddling.
- Ambiguous or contradictory instructions:
  1. CTA count: "one plus one optional soft CTA" (SKILL.md), "One primary CTA" (long-form.md) versus `cta.max` 2 plus `soft_mid_max` 1 in code. See blocking 4.
  2. Is a client brief `verified: yes`? SKILL.md step 2 says yes "only when the source is confirmed (tours.json counts)"; brand-and-claims.md lists "the user in writing" as a source. I marked the brief yes. Say it explicitly.
  3. Hook length: SKILL.md and short-form.md say 4 to 7 words; with `narrator: slow` a 7 word hook warns T04 (p3). Say "6 words with slow".
  4. short-form.md checklist "At most ... 1 place name" is not a rule in code, and sentence-initial names escape F01 anyway.
- Did the limits force a worse script? Twice, mildly. In the short, the 2 number cap means price and duration fill the CTA overlay and the departure dates live only in the caption; a booking short would want "12 or 19 Feb 2027" on screen. For a send CTA that is acceptable. In the long, 1 number per beat (with "two" counted) forced "Departures run in February 2027" instead of naming both dates, which is the detail a family needs to decide. The bigger pressure is the other way: the 320 to 400 word target for a 7 fact brief pushed me to fill time, and filling time is where the invented claims came from. The skill should tell the writer to lower `seconds` or accept W02 rather than pad.
- Does it beat the old loop-only skill? Clearly. The old skill had no length, no visual column, no facts, no CTA and "the goal is not clarity". On this brief it would have produced continuous prose with no price, no dates, no check on the level objection and nothing stopping "magical winter wonderland". scriptcraft gave me a timed table, a shot list a crew can film, a checked CTA, a facts table, and a forced `[VERIFY]` on the one claim the brief left open (ski level, which is also on the real do-not-claim list for the 3-day trip). It keeps the old skill's best line ("which loop does this line open, sustain or close?") and replaces Zeigarnik and dopamine with graded sources. What it lost: the old skill's push for an uncomfortable, interrupting hook. The new hook formulas are safe and a little polite.

## Non-blocking suggestions

- Count hyphenated and dotted chains as separate words in `WORD_RE` (a4). "ski-and-snowshoe" is 3 spoken words, not 1. This is the easiest budget cheat a writer agent will find.
- Fix the Norwegian thousands space false positive (p4). Outdoor Norway copy will write "NOK 4 900" sooner or later.
- Strip placeholders before word and sentence counts, or count them as a fixed length.
- Add to the scarcity and superlative lists: "going fast", "filling up", "spaces are limited", "world-class", "unbeatable", "leading", "premier", "top".
- Add a writer workflow step and a reviewer check: "every factual sentence in the voiceover maps to a row id in that beat". Fact rows protect numbers; claims without numbers (what a price covers, what a guide does first) are where the invention happens.
- Long-form.md: add "if the facts table has fewer than about 8 rows, set `seconds` to 120 to 150 or make a short".
- For DR: the CTA guidance should name the destination (link in bio, description, end card) and require it to match the landing page promise. "Book" CTAs should state what the viewer will see on landing.
- Add a "variant" line to the writer output contract: one alternative hook and one alternative CTA, each changing one variable, with a one-line hypothesis. A reel that cannot be A/B tested teaches nothing.
- Name the top objection per script in the frontmatter (`objection:`) and have the reviewer check it is answered with a fact.
- R03 counts "we" in "we stop" as company-speak; fine as a warning, but the brand rule "we for what the team looks after" means some "we" is wanted. Consider a ratio over 1.5.

## Test plan (for the applied Brekke short)

- Variant A tests the CTA verb: "Send this to the friend who won't ski." versus "Pick a February date. Link in bio." (the dates cannot also go on screen: 2 numbers per short, see the judgement above) Hypothesis: the send CTA wins on reach and sends per reach; the book CTA wins on link clicks per view. Same hook, same footage.
- Variant B tests the hook: "Half your group skis. Half doesn't." versus "Your non-skier is coming this time." Hypothesis: the second names the decision-maker's real problem (the reluctant non-skier) and lifts 3 s hold among family accounts.
