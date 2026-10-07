---
name: scriptcraft
description: Writes and fixes voiceover-led video scripts for Outdoor Norway with enforced length, hook, retention and density rules. Two tiers only, short form (Instagram Reels, YouTube Shorts, TikTok, up to 25 seconds) and long form (YouTube landscape, up to 3:20). Output is a timed beat table with voiceover, visual, on-screen text, roles and a facts table, checked by a validator script that must pass. Use for any reel script, short, TikTok, tour video, YouTube script, voiceover, hook or retention rewrite for Outdoor Norway or its ski, ski touring and snowshoe tours in Voss. Prefer this over the generic script-writing skill for any video script with a length.
---

# scriptcraft

Writes video scripts that fit a hard length, carry one idea, open on a visual hook and pass a validator. The rules live in code because writers, human or not, drift past word budgets.

```
NON-NEGOTIABLE RULES
1. Pick the tier first. Only two exist: short (25 s max) and long (200 s max).
   Refuse any other length and offer the nearest tier.
2. Take every word budget and limit from scripts/tiers.json. Never invent one.
3. Use facts only from the facts table. Anything you cannot source becomes [VERIFY: what, who].
4. Write only in the script file format (assets/script-template-*.md).
5. Run scripts/script_check.py until it says RESULT: PASS. Paste its output verbatim.
6. One idea in a short. One question in a long.
7. Hook in beat 1 with motion on screen and "you" in the words. One dominant loop,
   opened in the hook, closed before the call to action.
8. Follow scripts/brand_rules.json: no hype words, no guarantees on snow or aurora,
   no unsourced superlatives, no scarcity, the guest is the subject.
```

## Method

### 1. Intake

Ask only for what is missing. Six answers:

| Question | Why it matters |
|---|---|
| Platform | reels, shorts or tiktok means tier short. youtube means tier long. |
| Length | Short is 8 to 25 s, long up to 200 s. Anything else: refuse and offer the nearest tier. A 60 s reel becomes a 25 s short or a 200 s long. |
| Core takeaway | One sentence. If the user gives three, ask which one wins. |
| Product | A tour id from `campaigns/ski-meta-ads/tours.json`, or "no product" for a helpful post. |
| Facts source | tours.json, `.claude/product-marketing.md`, a page URL or the user. Nothing else. |
| Narrator | standard (fluent, natural pace) or slow (non-native guide, text-to-speech, calm read). Slow cuts the word budget by 15 percent. |

If the user asks for a different length ("a 45 second reel", "a 10 minute video"), say the two tiers are fixed, name the nearest one, and continue only after they choose.

### 2. Build the facts table

Copy facts word for word from the source into `## Facts`, one row each, with the number exactly as it will be spoken. Source names a file and key, a URL or a person. `verified` is yes only when the source is confirmed (tours.json counts). Everything else is `no` and the claim carries `[VERIFY: ...]` until resolved. Check the do-not-claim list in product-marketing.md before you use any fact.

### 3. Choose the structure

Short: 5 or 6 beats. Hook, setup, build or shift, payoff that closes the loop, call to action. See references/short-form.md.

Long: hook (by 8 s), promise (by 30 s), 4 to 6 chapters of 2 to 4 beats, each with its own small question and mini-payoff, a partial answer between 80 and 120 s, re-engagement beats between 55 and 80 s and between 120 and 145 s, the full answer by 185 s, then the call to action. See references/long-form.md.

Copy the matching template from assets/ and fill it. Start the visual column before the voiceover: pick the shot, then write what the picture cannot say.

### 4. Write the beats

- Ask of every line: which loop does this open, sustain or close? If none, cut it.
- One new fact per beat in a short, two in a long, never two numbers in one sentence.
- Voice adds what the picture cannot show: the reason, the name, the cost. It never narrates the obvious.
- Overlays carry 2 to 6 keywords that add to the voice. They never repeat it.
- Sentences short. Average 6 to 9 words in a short, 8 to 12 in a long.
- Describe difficulty by what the day involves ("long ascents", "confident on red runs").
- Plain verbs a body can do: climb, skin, carve, wait, eat. No AI vocabulary.

### 5. Run the validator

From the repo root:

```
python3 -I .claude/skills/scriptcraft/scripts/script_check.py path/to/script.md
python3 -I .claude/skills/scriptcraft/scripts/script_check.py path/to/script.md --final
python3 -I .claude/skills/scriptcraft/scripts/script_check.py --explain F01
```

Exit 0 is PASS, 1 is FAIL, 2 is a parse error naming the line. Use `--final` before publishing: placeholders and unverified facts then block.

### 6. Fix until PASS

Read each `[FAIL]` line, fix the cause, rerun. Never fix a length failure by deleting a fact row or by shortening times you cannot read in that time. Cut words. Clear `[WARN]` lines too unless you can say why one is acceptable. Five failed rounds means the idea is too big for the tier: say so and propose a narrower takeaway.

### 7. Final output

Return, in this order:

1. The script file (frontmatter, facts, script table, caption), saved to disk with the path named.
2. The validator output, pasted verbatim, ending in `RESULT: PASS`.
3. The caption.
4. Open items: every `[VERIFY]` and every fact row with `verified: no`, each naming who confirms it.

No script leaves this skill without a PASS. If the validator cannot run, say so and return the draft marked "not validated".

## Information diet

Viewers cannot re-read speech. A spoken beat with a price, a date, a place and an altitude fills working memory and nothing else lands.

| Item | Short (25 s) | Long (200 s) |
|---|---|---|
| Ideas | 1 takeaway | 1 question, 1 small idea per chapter |
| Facts (numbers, names, prices, places) | 3 max, 1 per beat | 14 max, 2 per beat |
| Numbers | 2 max | 6 max, 1 per beat |
| Leave out | Itinerary, prices beside dates, more than one place name, gear lists, company history, safety detail | Day-by-day lists, every inclusion, more than one price, numbers in the payoff line |
| Keep | One scene, one surprise, one ask | The scenes that answer the question, one honest downside |
| Where the rest goes | Caption or landing page | Description, chapters, landing page |

## Loops, with the honest evidence

Keep the old skill's loop discipline. Change the reasons.

- Curiosity gaps work: curiosity improves memory for the answer (Gruber, Gelman and Ranganath 2014; grade A).
- People tend to resume interrupted tasks (Ovsiankina). That is the honest basis for an open loop.
- The Zeigarnik memory claim is not supported. A 2025 meta-analysis of 59 studies found no memory advantage for unfinished tasks.
- "A dopamine hit per cut" is pop neuroscience. Do not use it.
- Holding every answer to the end is fine in 25 s and risky in 200 s. Long scripts pay a mini-answer in every chapter.

Short: one loop, opened in beat 1, closed in the last or second-last beat. No supporting loops. Long: one dominant loop opened by 8 s, closed by 185 s, at most 2 loops open at once.

## What changed from the previous script-writing skill

| Previous skill | scriptcraft |
|---|---|
| No length tiers | Two tiers, 25 s and 200 s, from tiers.json |
| "Every word earns its place", untestable | Word budgets per script and per beat, checked in code |
| Continuous prose output | A timed beat table: voiceover, visual, text, role, facts |
| No visual column | Visual hook in beat 1, shot pace limits |
| No density limit | Facts and numbers per beat and per script |
| No facts or brand rules | Facts table with sources, brand_rules.json, [VERIFY] |
| No call to action | One CTA in a short, one plus one optional soft CTA in a long, placed late |
| Zeigarnik and dopamine framing | Curiosity and resumption, with grades |
| Never resolve the main question early | Short: yes. Long: mini-payoffs, partial answer, re-engagement beats |
| No validator | scripts/script_check.py, rerun by an independent reviewer |

Kept: loops, the "which loop does this line serve" test, word economy, concrete over abstract.

## Agents

- `.claude/agents/script-writer.md` runs this method end to end and returns only a passing script.
- `.claude/agents/script-reviewer.md` reruns the validator and scores what code cannot judge. Use it before anything is published.

## References

| File | Read when |
|---|---|
| references/tiers.md | You need a limit, its reason or its evidence grade. |
| references/short-form.md | Writing or fixing a 25 s script. |
| references/long-form.md | Writing or fixing a 200 s script. |
| references/visuals-and-text.md | Choosing the opening shot, overlays, captions or safe zones. |
| references/psychology-for-scripts.md | Choosing a hook angle or answering a trip anxiety. |
| references/brand-and-claims.md | Any fact, claim, difficulty line, aurora or snow mention. |
| references/creator-patterns.md | You want a proven structure or need to justify one. |
| examples/short-fictional.md, examples/long-fictional.md | You want to see a passing script before writing. |
