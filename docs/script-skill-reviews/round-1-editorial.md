# scriptcraft, round 1: editorial review

Reviewer: Edith Marlow, Editorial Director (composite persona, `adquill/agents/editorial-director.md`).
Subject: `.claude/skills/scriptcraft/` (SKILL.md, references, assets, examples, scripts) and `.claude/agents/script-writer.md`, `.claude/agents/script-reviewer.md`.
Date: 2026-10-07.

## Editorial review

Verdict: REVISE
Overall: 7/10

| Dimension | Score | One-line reason |
|---|---|---|
| Clarity | 7 | The method is easy to follow, but three counting rules the validator enforces are written down nowhere, and they cost me two rounds. |
| Voice | 8 | Plain, specific and local. The docs read like an editor wrote them and the short example sounds like a guide talking. |
| Rhythm | 7 | The docs vary well. The long example drifts into a slogan cadence in its last three beats. |
| Precision | 6 | Almost every number matches tiers.json, but one documented date format is blocked by the validator, and "2 to 6 keywords" is a limit that does not exist. |
| Honesty | 9 | Zeigarnik and dopamine are handled correctly and graded. One grade is a notch too generous. |
| AI tells | 7 | The examples are clean on the linter, but a reference teaches a colon reveal and the long example closes on a tricolon. |

### Blocking issues

1. [references/brand-and-claims.md, "Facts and [VERIFY]"; agents/script-writer.md, "Style in everything you write"] "Dates in full with the year: \"30 Jan to 7 Feb 2027\"" and "Dates with the year." This instruction contradicts the validator. That example date holds 3 numbers. A short allows 2 numbers in the whole script (F03), and a long allows 1 number per beat (F01). So a writer who follows the rule fails. I did, in round 1 of the long script: "12 Feb and 19 Feb 2027" was blocked under F01. Fix: say that every numeral counts, including the day and the year. Spoken lines carry one date element per beat ("in February 2027"). Full dates with the year go in the caption, plus a facts row. Make the writer agent's style line match.

2. [SKILL.md, "Information diet"; references/tiers.md, "Limits"; `--explain` output] The writer is never told how the validator counts. Three rules bit me, and no document states any of them:
   - Spelled numbers count toward F01 and F03. "three" and "two" each took a number slot: "beat 13 has 2 numbers, maximum 1: 4900, three". The skill also says "Numerals for numbers", which reads as if spelled numbers are a safe way out. They are not, and only "one" is exempt.
   - Digits in the caption must also sit in a verified facts row (F04). The short failed on the caption alone: "number not in the facts table: 12 / 19 / 2027". Meanwhile the docs send dates to the caption ("Where the rest goes: Caption"). visuals-and-text.md only says "Digits on screen count as facts".
   - A facts row that no beat references does not count toward F02. That is useful, and nobody says it.

   `--explain F01` prints only the JSON limits, not what gets counted. Fix: add a short "How the validator counts" box to tiers.md, covering words, numbers (digits, spelled two to twenty, "one" exempt), names, caption digits and unreferenced rows. Link it from SKILL.md step 5 and the writer agent. Have `--explain` print one plain sentence on what it counts (owner V).

### Non-blocking suggestions

- SKILL.md, "Write the beats": "Overlays carry 2 to 6 keywords". No such limit exists. tiers.json allows 6 words in a short and 8 in a long. The templates say "2 to 5 words". Use "a few keywords, within the tier's overlay limit" and drop the invented range everywhere.
- SKILL.md, "Intake": "A 60 s reel becomes a 25 s short or a 200 s long." A long is YouTube landscape, so a reel cannot simply become one. Say: "a 25 s reel, or a 200 s YouTube video instead".
- references/long-form.md, "Partial answer": "Here's half the answer: your legs can do this." This is a colon reveal, and the long example copies it. Writers will reuse the model line word for word. Give a plain version: "Here's half the answer. Your legs can do this."
- examples/long-fictional.md, beat 14: "A quiet slope, your group spread out above you, and the sound of your own skis." This is a tricolon. Beat 15 ends on the slogan pair "Your guide handles the route and the pace. You bring the legs." Beats 12 and 14 also both say "what the climb was for". Cut one and break the triad.
- references/creator-patterns.md, "Who was studied": "Journey as an obstacle". This uses "journey" as a noun, which the house style bans. Write "The trip as an obstacle".
- references/tiers.md, "Limits": "Pattern interrupt every 40 s" is graded B/J. Research note 03 grades "pattern interrupt every 20 to 40 s" C, and MrBeast's 3 and 6 minute marks scale to about 60 s, not 40. Grade it C/J.
- Design question for the tiers.json owner, not for the docs owner: on-screen numbers in the CTA beat use the same budget as spoken ones. The Cowan and Mayer case is about speech that cannot be re-read, while an end-card overlay can be. As it stands, no long beat can show "12 or 19 Feb 2027", and a short cannot show the price and a date together. Consider a separate overlay number allowance for the cta beat.
- Validator: my long script estimates 165 s against a declared 191 s, so 26 s of the timeline has no voice and no [PAUSE]. That is fine for landscape holds, but nothing tells the editor where the holds are. An info line per beat (declared minus estimated, over 3 s) would help.
- The validator, by design, does not catch AI tells. My own long draft passed with "The skiers learn, the walkers explore, and nobody waits in a cafe" (tricolon) and "not a long line of strangers" (contrast). The reviewer agent covers this under "Sounds human", which is correct. Say plainly in SKILL.md step 6 that PASS is a floor, not a verdict on the prose.
- The linter (`adquill/skills/adquill/scripts/slop_lint.py`) flags banned words that the docs only quote ("perfect powder", "guarantee", "elevate"). These are false positives. The only true hit in the skill files is "Journey" above.

### Strongest line

"Then, after 600 metres, the slope runs out of up." (examples/long-fictional.md, beat 12). It has one number, a physical image, no adjective, and you can hear the guide's dry humour. It shows the voice brief better than the four-row table does.

### AI tells found

- colon reveal: "Here's half the answer: your legs can do this." (long-form.md, long example beat 9)
- tricolon: "A quiet slope, your group spread out above you, and the sound of your own skis." (long example beat 14)
- slogan closer: "You bring the legs." (long example beat 15)
- banned noun: "Journey as an obstacle" (creator-patterns.md)
- None in the short example. Both examples score 100 on the repo linter.

## Consistency with tiers.json

I checked every limit in SKILL.md, tiers.md, short-form.md, long-form.md, visuals-and-text.md, both templates and both agents against tiers.json 0.1.0. All of them match: seconds, warn lines, wps, number penalty, words, beats, seconds and words per beat, hook and promise, facts and numbers, sentence lengths, overlays, CTA, shots, chapters, loop windows, narrator scales (51 and 374 words for slow are right) and the acronym list. Two exceptions are the invented "2 to 6 keywords" and the template's "2 to 5 word overlay", both above. Guidance figures such as "4 to 7 hook words" and "17 words fits 8 s" are derived correctly and explained, which is the right way to do it.

The facts quoted in brand-and-claims.md and short-form.md match `campaigns/ski-meta-ads/tours.json` and `.claude/product-marketing.md` (NOK 1,948 per adult, NOK 42,126, NOK 41,181, NOK 28,896, the 2027 departures, about an hour by train). The do-not-claim list is carried over faithfully.

No em dashes, en dashes, emoji or model names appear in any skill or agent file (checked by code point).

## Research honesty

- Zeigarnik: correctly marked not supported. Ghibellini and Meier 2025, 59 studies, recall ratio 0.99, all match research note 03, section 9.
- Ovsiankina resumption as the basis for open loops: matches the same meta-analysis.
- Dopamine: SKILL.md calls "a dopamine hit per cut" pop neuroscience and bans it. psychology-for-scripts.md describes dopamine accurately as reward prediction and learning. Nothing overclaims Gruber 2014.
- Curiosity (Gruber 2014, Kang 2009), Mayer redundancy, signalling and segmenting, Cowan, Guo 2014 (156 wpm, 2.6 wps), Google social proof 28 of 31, Van Boven and Gilovich, Kumar et al: all match the notes, with the grades the notes give.
- Muller misconception-first is graded A. The note grades it "A (peer-reviewed thesis, secondary report)". That is acceptable, but a thesis read through a magazine report is closer to B.
- The creator measurements are correctly graded C and labelled as a small sample.

## Applied test: Brekke Ski Guides (fictional brief)

Brief: a 3-day ski and snowshoe weekend, from NOK 4,900, departures 12 Feb and 19 Feb 2027, small groups, a lesson on each ski day, one snowshoe day for non-skiers, aimed at families and friend groups. All of it is fictional.

Files:
- `brekke-short.md` (reels, 25 s, 6 beats, 52 words, est 21.7 s)
- `brekke-long.md` (youtube, 191 s, 16 beats, 357 words, est 165.1 s, 4 chapters)

Rounds:
- Short, round 1: FAIL (3 blocking). F04 hit 12, 19 and 2027, which appeared only in the caption. Fix: add a dates row to the facts table.
- Short, round 2: `RESULT: PASS`, 0 warnings. `--final` PASS, `--strict` PASS.
- Long, round 1: FAIL (4 blocking, 2 warnings). F01 hit "4900, three" in one beat and "12, 19, 2027, two" in another. S01 caught two sentences of 20 and 22 words. F07 warned on "February". V01 warned on beat 16.
- Long, round 2: FAIL (1 blocking). F01 hit "2027, two", because the overlay "Two February weekends" counted as a number.
- Long, round 3: `RESULT: PASS`, 0 warnings. `--final` PASS, `--strict` PASS.

Final validator result lines:

```
short: TOTAL words 52 | est 21.7 s | declared end 25 s | beats 6 | facts 3 | numbers 1
short: RESULT: PASS
long:  TOTAL words 357 | est 165.1 s | declared end 191 s | beats 16 | facts 7 | numbers 4
long:  RESULT: PASS
```

### Short script voiceover as it passed

| beat | time | voiceover | text | role |
|---|---|---|---|---|
| 1 | 0-3 | Half your group skis. Half doesn't. | Who skis, who doesn't? | hook, open:A |
| 2 | 3-7 | So someone usually ends up waiting in the cafe. | - | setup |
| 3 | 7-12 | Here, the skiers get a lesson on each ski day. | Skiers | build |
| 4 | 12-17 | The others get a day of their own, on snowshoes. | Non-skiers | shift, explain |
| 5 | 17-21 | Nobody waits in the cafe. Everyone gets a day. | Nobody waits | payoff, close:A |
| 6 | 21-25 | Send this to the friend who never skis. | From NOK 4,900 | cta |

### Judgement

Did the skill make the rules easy to follow? Mostly, yes. The short template's beat sizes (4 to 7, then 8 to 12 words) landed the first draft at 52 words and 21.7 s with no timing failures. The hook rules pushed me to a better opener than I would have written: "Half your group skis. Half doesn't." The facts table made me notice that the brief never says what is included in the price. So the long script says "ask what that price covers" and invents nothing. Every failure I hit was a counting rule, not a craft rule. Blocking issues 1 and 2 above would have saved me three rounds.

Were instructions ambiguous or contradictory? Yes, in three places: the full date format (blocking 1), how numbers and caption digits are counted (blocking 2), and the overlay "2 to 6 keywords" against the tier limits. "Starts in the last 20 s" is also unclear about whether it counts from the declared end or from 200 s. The validator counts from the declared end, which is sensible, but it should say so.

Did the limits force a worse script? Twice they helped and once they hurt. S01 caught two sentences I had let sprawl, and the long script is better for the split. The per-beat number cap hurt. The long CTA cannot show "12 or 19 Feb 2027", so the spoken line became "Departures run in February 2027, a week apart" and the real dates moved to the caption. For a booking video, the date on the end card is the one number a viewer needs. That is a tiers.json design choice worth revisiting (see suggestions), not a docs fault.

Does it beat the old loop-only skill? Clearly, in five ways:
1. Length is enforced. The old skill had no word budget and no timing, so a "25 second" script could not be checked.
2. Pictures come first. The old skill wrote continuous prose with no visual column. Here, beat 1 has to move, which is what stops a scroll.
3. Facts are controlled. The old skill had no facts table, and a brief this thin invites invented inclusions. This one made me write the gap down instead.
4. The CTA has rules. The old skill banned a CTA outright. This one places it, caps it and ties it to the payoff.
5. The evidence is honest. Zeigarnik and dopamine are gone, and the long form pays mini-answers instead of holding everything to 185 s.

It keeps the best of the old skill: "which loop does this line open, sustain or close" still runs through every step.

What it does not do yet: catch prose tells. My long draft passed with a tricolon and a "not X" contrast. The reviewer agent has to carry that, and SKILL.md should say so.
