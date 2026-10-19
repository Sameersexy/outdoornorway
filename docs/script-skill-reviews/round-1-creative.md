# Round 1 creative review: scriptcraft

Reviewer: Tomas Reyes-Hale, Creative Director (composite persona, `adquill/agents/creative-director.md`).
Subject: `.claude/skills/scriptcraft/` (SKILL.md, references, assets, examples, scripts) and `.claude/agents/script-writer.md`, `.claude/agents/script-reviewer.md`.
Question: can this method produce a distinctive, thumb-stopping 25 s script and a gripping 3 minute script inside the limits, without every script sounding the same?

## Creative review

Verdict: REVISE
Overall: 7/10

| Dimension | Score | One-line reason |
|---|---|---|
| Idea | 8 | "One idea in a short, one question in a long" is enforced in structure, loops and fact budgets, and it works. |
| Thumb-stop | 6 | Hook rules are sound, but the hook formulas and the visual hook library are tame and almost all lone-skier ski touring shots. |
| Distinctiveness | 5 | Nothing in the method builds a brand asset. Cover the logo on either example and it could be any ski school. |
| Picture and words | 8 | Visual column written first, O03 redundancy check, "voice adds what the picture cannot". Best part of the skill. |
| Platform fit | 7 | Muted-first overlay, safe zones, send CTA. But V01 blocks a one-take POV shot, one of the most native formats on Reels. |
| Shareability | 7 | "Send this to the one friend who overdresses" is a real share line, and the CTA guidance points there. |
| Range of variants | 4 | One beat grid per tier, one canned line per device. My test scripts landed on the examples' exact grid and near-verbatim lines. |

### Blocking issues

1. [assets/script-template-short.md, references/short-form.md "Beat template", assets/script-template-long.md, references/long-form.md "Progress markers" and "Partial answer"] Fixed grid plus single canned lines produce sameness. The short template hard-codes times `0-3, 3-7, 7-12, 12-17, 17-21, 21-25` and words per beat; the short example uses that exact grid; my applied test used it too, because the template is what a writer copies. The long docs give one example line per device: "That's the kit, sorted. Now the question people ask us" and "You're halfway up the mountain, and here's half the answer". Following the skill honestly, I wrote "That's the skiers sorted. Now the hard one." and "You're halfway there, and here's half the answer". Ten scripts from this skill will share a skeleton and a voice tic. That is the exact failure the persona brief asked about. Direction: give each tier 3 or 4 named structures with different beat grids (short: outcome first then rewind, one scene in real time, two-voice question and answer, loop-back; long: day as scenes, misconception test, three people one trip, decision walk-through). Give 4 or 5 alternative phrasings per device (progress, partial, re-engage) and a written rule: never reuse an example line verbatim. Add a "distinct from the examples" check to script-reviewer.md.

2. [references/visuals-and-text.md "Visual hook library", references/short-form.md "Visual hooks for beat 1"] The hook library is narrow. Ten entries, nine of them a skier, skis, skins or a binding; one snowshoe shot; no face with an emotion, no group, no family, no child, no humour, no food or cabin, no "picture argues with the words" pairing. The brief I tested (families and friend groups, a non-skier) had no entry to start from, so I invented one. The real catalogue includes mixed-group products (3-Day Ski and Snowshoe, 6 Day Fresh and Cruisers), so this gap hits real work. A library this narrow pulls every reel toward the same POV-on-skins opener. Direction: grow it to 15 to 20 entries grouped by what the frame does (contrast of two people, reaction face, mid-action mishap, sound-first frame, overhead group, close detail), each paired with a hook formula and with one line where the words contradict the picture. Include snowshoe, family and non-skier frames.

3. [scripts/tiers.json short.visual.hard_max_static_seconds, enforced as V01 block; references/visuals-and-text.md "How to write the visual column"] V01 counts shots, not motion. A single unbroken POV take of snowshoes stepping into forest for 5 s blocks ("[FAIL] V01 beat 4 holds one shot for 5 s, maximum 4"). One-take POV and drone pushes are some of the most native, thumb-stopping short formats, and the motion is the point. A writer will dodge it by splitting one shot into a fake "a / b", which teaches the crew the wrong thing. Direction: let a beat mark a continuous moving take (for example a visual cell starting "one take:") and downgrade the static block to a warning when the shot names motion, or count camera moves as shots. Say so in visuals-and-text.md.

### Non-blocking suggestions

- Distinctiveness: add a short section on brand assets that survive a covered logo: a recurring named guide as narrator (the Rent a Finn and Ask Gudmundur lesson already in creator-patterns.md, but never turned into a script pattern), a recurring sound (skins squeak, thermos lid), a fixed one-line local detail. Right now the method guarantees clean scripts, not ownable ones.
- Hooks: the old skill's line "The goal is not clarity. The goal is interruption" was the one thing it had right about the hook. Scriptcraft's formulas lean polite ("Frame as discovery, never 'you are wrong'"). Keep the brand guard, but add one or two sharper formulas: a mild confession from the guide, a visual contradiction, a funny honest downside.
- Dates and price in a short: a full date with a year counts as 2 numbers, so "12 Feb 2027 / From NOK 4,900" on a short CTA overlay fails F01, F02 and F03 at once. Tested: 4 blocking. short-form.md still says "Book only when the overlay or caption carries the real date and price", which a writer reads as "overlay". Say plainly that in a short the date goes in the caption, or count a full date as one fact.
- Caption digits: F04 checks digits in the caption, which is correct, but no document says so. My first short failed 3 times on caption dates. One line in SKILL.md step 2 fixes it.
- Loop-back ending (short-form.md): "put the CTA in the overlay and caption only, and make the final spoken beat still carry the cta role with at most 8 words" reads as a contradiction. Show one worked loop-back beat 6 so writers see what a spoken cta-role line that is also the loop line looks like.
- Fact fidelity: my first short draft said "Then one day, nobody skis. You all strap on snowshoes." The brief says the snowshoe day is for non-skiers. It passed the validator because F2 was tagged. The reviewer agent catches this in step 2, but the writer agent should have its own step: reread each beat against its fact row; the line may not say more than the row.
- "Small groups": the brief claims it; product-marketing.md bans any group size number. Say in brand-and-claims.md whether the words "small groups" (no number) are allowed for Outdoor Norway.
- S01 average floor: short fragments ("Bring her anyway.") pulled the average to 5.6 and drew a warning. Punchy fragments are the native voice of a reel. Keep it a warning and say in short-form.md that one fragment pair in the hook is fine.
- `--explain`: it prints the limits but not the fix. "F07: every proper noun appears in the facts table" with nothing else. Add one line of "how to fix" per rule.
- Long example: "Now you find out what the climb was for" followed by "This is what the climb was for" in the next chapter reads as a repeat. Vary one.
- Both examples are ski touring with a lone guide voice. Make the long example a different product or audience (families, mixed group, snowshoe) so the examples show range rather than one recipe.

### The line to protect

"Send this to the one friend who overdresses." (examples/short-fictional.md, beat 6) - a share line built on a specific, slightly teasing truth about a friend. It is the model for every short CTA in this skill. And in the same example, "Your guide wants you a little cold." is the best hook in the package: specific, counterintuitive, paid off.

### Cliches found

- "This is what the climb was for." (long example, beat 14) close to the stock "this is why we do it" travel closer.
- "By the end, you'll know if it's for you." (long-form.md and long example promise) a sound promise line, but it is now the house default; it will appear in every long script.
- "The fjord sits below your ski tips." appears in the short-form.md weak versus strong table and again in the long example. Writers will copy it; it is a house line already.
- None of the BR03 tourism-board cliches got through in either example or my test scripts. That part works.

## Mandatory applied test

Brief (fictional): Brekke Ski Guides, 3-day ski and snowshoe weekend, NOK 4,900 from, departures 12 Feb and 19 Feb 2027, small groups, a lesson on each ski day, one snowshoe day for non-skiers. Audience: families and friend groups.

Files: `short.md` (Reels, 25 s) and `long.md` (YouTube, 192 s declared, 178 s estimated).

### Short: final validator result

```
TOTAL words 53 | est 22.1 s | declared end 25 s | beats 6 | facts 3 | numbers 1
RESULT: PASS
```
Zero warnings. `--final --strict`: `RESULT: PASS`.

Rounds: draft 1 failed 3 blocking (F04 on caption dates 12, 19, 2027) with 5 warnings (T02, T04 beat 2, W02, S01 average 5.6, BR14 "most"). Draft 2 passed clean. Draft 3 was my own fact-fidelity fix (see above), still PASS.

The script, in one line per beat:
1. "Your sister doesn't ski. Bring her anyway." over a skier carving past a woman on snowshoes. Overlay "One skis. One doesn't."
2. "Usually she waits in the cafe while you ride lifts."
3. "Here, each ski day starts with a lesson, so she tries."
4. "And one day is all hers, out on snowshoes."
5. "So at dinner, she's the one with stories." Overlay "Nobody sat it out".
6. "Send this to the one who never skis." Overlay "From NOK 4,900".

### Long: final validator result

```
TOTAL words 387 | est 178.3 s | declared end 192 s | beats 16 | facts 5 | numbers 3
RESULT: PASS
```
Zero warnings. `--final --strict`: `RESULT: PASS`.

Rounds: draft 1 failed 3 blocking (F01 beat 16 with 4 numbers from a date and price overlay; S01 two sentences of 19 and 22 words) with 6 warnings (T04 hook +25 percent, W03 beat 12, V01 beats 15 and 16, BR14 twice). Draft 2 left one BR14 warning on the overlay "Lesson first". Draft 3 passed clean.

Shape: hook "One of you skis fast. One of you is nervous. One won't ski at all. Can one weekend work?"; promise by 20 s; four chapters told through three people (the nervous skier, the one who won't ski, small groups, the evening); partial answer at 92 s; re-engagement at 56 s and at 128 s with a 2 s sound break; payoff at 164 s; CTA at 178 s.

### Honest judgement of the skill in use

- Easy to follow: yes. The validator output is the best feature. Every failure named the beat, the number and the quote, and each fix took under a minute. The per-beat table made pacing visible in a way prose never does.
- Ambiguous or contradictory: caption digits are checked but not documented; "Book only when the overlay or caption carries the date and price" invites an overlay that cannot pass in a short; the loop-back CTA paragraph reads as a contradiction; "small groups" sits between the brief and the do-not-claim list with no ruling.
- Did the limits force a worse script: mostly no. They made both scripts better. Cutting the long hook from 22 to 17 words made it punchier, the sentence cap split a limp 22-word payoff into three plain beats, and moving dates off the CTA overlay cleaned the end card. Two places hurt: the one-take POV block, and the sentence-average floor nudging a reel away from fragments. The bigger risk is not the limits, it is the templates: I followed them and produced scripts that share a skeleton and phrasing with the examples.
- Does it beat the old loop-only skill: yes, clearly. The old skill would have returned continuous prose with no shots, no overlay, no timing, no facts and no CTA, and nothing would have caught a 22-word sentence, a 10 s hook in an 8 s window, three dates on one end card or caption numbers with no source. Scriptcraft keeps the old skill's best idea (the "which loop does this line serve" test, which I used on every line) and replaces Zeigarnik and dopamine claims with honest evidence. What it lost: the old skill's appetite for interruption and its emotional relevance section ("things the viewer already believes but has never heard said out loud"). Put that back in short-form.md as a hook source and the creative ceiling rises.

## Score rationale

The engineering is strong and honest. Creatively it is a safe system: it reliably stops bad scripts, and it does not yet push writers toward ownable or varied ones. The three blocking items are cheap to fix and all sit in docs or one validator rule. Fix them and this is an 8.
