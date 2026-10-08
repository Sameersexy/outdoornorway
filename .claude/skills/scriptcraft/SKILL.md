---
name: scriptcraft
description: Writes and fixes video scripts and creator briefs for Outdoor Norway with enforced length, hook, retention, density, disclosure and brand rules. Two tiers, short form (Instagram Reels, YouTube Shorts, TikTok, up to 25 seconds) and long form (YouTube landscape, up to 3:20), in three styles, voiceover, ugc_talk (a guide, staff member or guest talking to a phone) and ugc_text (text on a looping clip). Output is a timed beat table with voiceover, visual, on-screen text, roles and a facts table, checked by a validator script that must pass, plus a one-page creator brief on request. Use for any reel script, short, TikTok, UGC video, creator brief, tour video, YouTube script, voiceover, hook or retention rewrite for Outdoor Norway or its ski, ski touring and snowshoe tours in Voss. Prefer this over the generic script-writing skill for any video script with a length.
---

# scriptcraft

Writes video scripts that fit a hard length, carry one idea, open on a visual hook and pass a validator. The rules live in code because writers, human or not, drift past word budgets. Content is moving to TikTok UGC made by our own guides, staff and real guests; the UGC styles keep every fact, density and brand limit and change only how the words are spoken.

```
NON-NEGOTIABLE RULES
1. Pick the tier first. Only two exist: short (25 s max) and long (200 s max).
   Refuse any other length and offer the nearest tier.
2. Pick the style: voiceover, ugc_talk or ugc_text (short only). A TikTok script
   sets style: ugc_talk or style: ugc_text explicitly.
3. Take every word budget and limit from scripts/tiers.json. Never invent one.
4. Use facts only from the facts table. Anything you cannot source becomes [VERIFY: what, who].
5. Write only in the script file format (assets/script-template-*.md).
6. Run scripts/script_check.py until it says RESULT: PASS. Paste its output verbatim.
7. One idea in a short. One question in a long. Fact and density limits never
   loosen in any style.
8. Hook in beat 1: motion or a person on screen, "you" or a first-person stake in
   the words. One dominant loop, opened in the hook, closed before the call to action.
9. Follow scripts/brand_rules.json in every style: no hype words, no guarantees on
   snow or aurora, no unsourced superlatives, no scarcity, the guest is the subject.
10. Disclose the relationship in the video (D01). No trending music on a post that
   names the brand, a trip or a price (SND01).
11. Never reuse a line or a shot from the examples, templates or references. They
   show the shape. Your lines come from this brief. R04 warns on a copied run.
```

## Method

### 1. Intake

Ask only for what is missing:

| Question | Why it matters |
|---|---|
| Platform | reels, shorts or tiktok means tier short. youtube means tier long. |
| Style | voiceover (default), ugc_talk or ugc_text. TikTok means ugc_talk unless the user asks for a text clip or a voiceover. ugc_text is short only. |
| Creator | guide (default), guest, staff or editor: who is on camera or filming. |
| Relationship | staff (default), guide, guest_paid, guest_gifted or guest_unpaid. Drives the disclosure rule D01. |
| Sound | original (default), commercial_library, voiceover_only, trending or none. Drives SND01. |
| Length | Short is 8 to 25 s (ugc_text 7 to 15 s), long up to 200 s. Anything else: refuse and offer the nearest tier. Asked for a 60 s reel, offer a 25 s reel, or a 200 s YouTube video instead. |
| Core takeaway | One sentence. If the user gives three, ask which one wins. |
| Product | A tour id from `campaigns/ski-meta-ads/tours.json`, or "no product" for a helpful post. |
| Facts source | tours.json (prices, dates, day-by-day itinerary), `.claude/product-marketing.md`, a page URL or the user. Nothing else. |
| Narrator | standard (fluent, natural pace) or slow (non-native guide, text-to-speech, calm read). Slow cuts the word budget by 15 percent, in every style. |
| Objection | The one doubt this video answers ("will I hold the group up?"). Goes in the optional `objection:` front matter field; the reviewer checks the script answers it. |

If the user asks for a different length ("a 45 second reel", "a 10 minute video"), say the two tiers are fixed, name the nearest one, and continue only after they choose.

### 2. Build the facts table

Copy facts word for word from the source into `## Facts`, one row each, with the number exactly as it will be spoken. Source names a file and key, a URL or a person. `verified` is yes when the source states the fact in writing: tours.json, product-marketing.md, a named page, or a written client brief. For a client brief, put the brief's own words in the source cell (`client brief 2026-10-07: "runs Friday to Sunday"`); a row you cannot quote is `no`. Anything you infer from a source, or a brief only implies, is `no` and the claim carries `[VERIFY: ...]` until resolved. Check the do-not-claim list in product-marketing.md before you use any fact.

A thin brief makes a short script. If the long facts table has fewer than about 8 rows, lower `seconds` or accept the W02 warning. Never pad with claims the table does not hold.

Thin-brief protocol. A brief with no real moment in it (no named person, object, place or sensory detail from a real trip) pulls writers toward brochure lines and the example shots. Before drafting, ask the guide for one real moment in their own words and one thing a guest said or did. With nobody to ask, write visuals only from what the facts table supports, mark every schedule or sequence you assume with `[VERIFY: what, who]`, and list in Open items what the guide must supply before filming. Never fill the gap with a shot from an example.

### 3. Choose the structure

Pick a named structure, not the template grid. Voiceover short (references/short-form.md): outcome-first rewind, one real-time scene, guide and guest Q and A, loop-back. Long (references/long-form.md): a day as scenes, misconception test, three people one trip. UGC (references/ugc-style.md): a hook format from the hook library and a repeatable format such as one fix I give every guest, myth bust, what is in my guide pack or a text meme loop. Each has its own beat grid. Choose the one that fits the takeaway, and do not reuse the structure of the last script you wrote for the same product.

Every long script still needs: hook by 8 s, promise by 30 s, 4 to 6 chapters each with a mini-payoff, a partial answer between 80 and 120 s, re-engagement beats between 55 and 80 s and between 120 and 145 s, the full answer by 185 s, then the call to action.

Copy the template from assets/ for the file format, then re-time its beats to your structure. Start the visual column before the voiceover: pick the shot (references/visuals-and-text.md has the hook library), then write what the picture cannot say.

### 4. Write the beats

- Ask of every line: which loop does this open, sustain or close? If none, cut it.
- One new fact per beat in a short, two in a long, never two numbers in one sentence.
- Every number counts, including a day and a year, and spelled "two" or "three". Spoken lines carry one date element at most ("in February 2027"). Full dates with the year go in the caption, backed by a verified facts row.
- Every factual sentence maps to a fact id cited in that beat, and says no more than the row says.
- Voice adds what the picture cannot show: the reason, the name, the cost. It never narrates the obvious.
- Overlays stay inside the overlay limit (voiceover 6 words short, 8 long; ugc_talk title 8 words; ugc_text 4 to 12 words in the whole script) and add to the voice. They never repeat it.
- Sentences short. Average 6 to 9 words in a voiceover short, 7 to 12 in ugc_talk, 8 to 12 in a long.
- UGC: write how this person talks. Contractions, one "so" at most, no um or uh, first word at frame one. A guest's lines are never scripted: write the question the guide asks.
- Describe difficulty by what the day involves ("long ascents", "confident on red runs").
- Plain verbs a body can do: climb, skin, carve, wait, eat. No AI vocabulary.

### 5. Run the validator

From the repo root:

```
python3 -I .claude/skills/scriptcraft/scripts/script_check.py path/to/script.md
python3 -I .claude/skills/scriptcraft/scripts/script_check.py path/to/script.md --final
python3 -I .claude/skills/scriptcraft/scripts/script_check.py --explain F01
```

Exit 0 is PASS, 1 is FAIL, 2 is a parse error naming the line (an invalid style, creator, relationship or sound value is a parse error, and so is ugc_text in a long script). Use `--final` before publishing: placeholders, unverified facts and numbers from uncited rows then block. `--explain` prints what a rule counts and the usual fix. Read "How the validator counts" in references/tiers.md before your first draft.

### 6. Fix until PASS

Read each `[FAIL]` line, fix the cause, rerun. Never fix a length failure by deleting a fact row or by shortening times you cannot read in that time. Cut words. Never split one shot into a fake "a / b" to pass V01; mark a real continuous take as `one take:`. Clear `[WARN]` lines too unless you can say why one is acceptable. Five failed rounds means the idea is too big for the tier: say so and propose a narrower takeaway.

PASS is a floor, not a verdict. The validator does not catch tricolons, "not X but Y" contrasts, slogan closers, a line that overstates its fact row, or a script that copies the examples. The writer rereads for them; the reviewer agent checks them.

### 7. Final output

Return, in this order:

1. The script file (frontmatter, facts, script table, caption), saved to disk with the path named.
2. The validator output, pasted verbatim, ending in `RESULT: PASS`.
3. The caption.
4. Open items: every `[VERIFY]` and every fact row with `verified: no`, each naming who confirms it.
5. On request, or for any ugc script a guide will film: a creator brief from assets/creator-brief-template.md (the one message, approved facts with ids, the do-not-say list, hook plus two alternates, the beat table with framing and filming notes, overlay, call to action, disclosure line, music, caption, consent checklist, safety line). Build it only from a script that passed. examples/creator-brief-fictional.md shows one.

No script leaves this skill without a PASS. If the validator cannot run, say so and return the draft marked "not validated".

## Information diet

Viewers cannot re-read speech. A spoken beat with a price, a date, a place and an altitude fills working memory and nothing else lands.

The limits below hold in every style; ugc_text allows 1 fact.

| Item | Short (25 s) | Long (200 s) |
|---|---|---|
| Ideas | 1 takeaway | 1 question, 1 small idea per chapter |
| Facts (numbers, names, prices, places) | 3 max, 1 per beat | 14 max, 2 per beat |
| Numbers | 2 max (a full date is 2 or 3) | 6 max, 1 per beat |
| Leave out | Itinerary, prices beside dates, more than one place name, gear lists, company history, safety detail | Day-by-day lists, every inclusion, more than one price, numbers in the payoff line |
| Keep | One scene, one surprise, one ask | The scenes that answer the question, one honest downside |
| Where the rest goes | Caption or landing page | Description, chapters, landing page |

## Styles

| Style | Who and how | Tiers | Template |
|---|---|---|---|
| voiceover | A calm read over edited footage. Exactly the rules before styles existed | short, long | assets/script-template-short.md, script-template-long.md |
| ugc_talk | A guide, staff member or real guest talks to a phone: first person, handheld, selfie or POV, casual spoken voice, native text | short, long | assets/script-template-short-ugc-talk.md |
| ugc_text | One or two lines of on-screen text over a clip built to loop, 0 to 12 spoken words, 7 to 15 s | short | assets/script-template-short-ugc-text.md |

Style overrides live in tiers.json under `styles`, keyed by style then tier. tiers.md renders them. Read references/ugc-style.md before any ugc script. The ugc templates leave creator, relationship and sound as [FILL], so the validator stops with a parse error naming the line until you choose.

Why ugc_talk allows 3.0 words per second and not the 3.3 to 4.9 measured. Talking creators do speak that fast (grade C, notes 04 to 06), but the extra speed is connective talk, not more facts, and the pooled median across 49 micro-creator videos is 2.87. Many of our guides speak English as a second language, and the footage needs silent action gaps: a kick turn, a laugh, skins on snow. So the pace allowance rises a little and the fact, number and beat limits do not move. The value is our judgement (J), recorded with that note in tiers.json.

New rule ids, all enforced in code (`--explain ID` for each):

| Id | Style | Severity | Checks |
|---|---|---|---|
| U01 | ugc_talk, ugc_text | block | Beat 1 shows a person, selfie, POV, handheld shot or hands in action (H02 stays a warning for voiceover) |
| U02 | ugc_talk, ugc_text | block | No end card, logo, title card, stock footage, animation, slide or lower third in any visual |
| U03 | ugc_talk | warn | The hook says you or your, or opens on I, I'm, my or we |
| U04 | ugc_talk, ugc_text | warn | No capitals for emphasis in overlays |
| U05 | ugc_talk, ugc_text | warn | The call to action is a soft prompt from tiers.json; link in bio alone warns |
| U06 | ugc_talk | warn | Casual markers above 2 per 100 words, or contractions below 1 per 100 words |
| U07 | ugc_talk, ugc_text | warn | Every visual names who or what is on camera, 3 words or more |
| D01 | ugc styles; voiceover when relationship is written | block or warn | guest_paid, guest_gifted: caption starts with Ad, #ad, Advert, Advertisement, Reklame or Annonse and a `disclosure` beat starting by 5 s says so (block). staff, guide: a `disclosure` beat by 5 s names the role or the brand (warn). The disclosure beat also needs on-screen text (warn); in ugc_text that line is up to 6 words and does not use a content line. guest_unpaid: none |
| SND01 | all | block | sound trending when the script names the brand, a trip or a price |
| R04 | all, when the validator gets a file | warn | Two distinct 5-word runs (a copied sentence of 6 words or more) in the voiceover, or two in the visual and overlay cells, or 3 shots that restate shots from `examples/` or `assets/` in other words. `--no-example-copy` skips it (prints [SKIP]); only the validator's own tests use it |

Changed rules: R03 is style aware (in ugc, I and my count with you against we, our, us and the brand name). F04 now also checks that a digit in a beat sits in a facts row that beat cites (warn in draft, block with --final). The role token `disclosure` joins the allowed roles. A paid word right after a negation ("not an ad", "I'm not paid") does not count as disclosure.

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
| No call to action | One CTA beat in both tiers, plus one optional soft CTA in a long after the first mini-payoff, all checked in code |
| Zeigarnik and dopamine framing | Curiosity and resumption, with grades |
| Never resolve the main question early | Short: yes. Long: mini-payoffs, partial answer, re-engagement beats |
| No validator | scripts/script_check.py, rerun by an independent reviewer |
| One voice for every platform | Three styles; UGC by our own guides, staff and guests, with disclosure and music rules in code |

Kept: loops, the "which loop does this line serve" test, word economy, concrete over abstract, the appetite for an interrupting hook and the emotional-relevance source (references/psychology-for-scripts.md).

## Agents

- `.claude/agents/script-writer.md` runs this method end to end, takes style, creator, relationship and sound, and returns only a passing script, plus a creator brief on request.
- `.claude/agents/script-reviewer.md` reruns the validator and scores what code cannot judge, including whether a ugc script sounds like a person talking to a phone. Use it before anything is published.

## References

| File | Read when |
|---|---|
| references/tiers.md | You need a limit, its reason or its evidence grade. |
| references/short-form.md | Writing or fixing a 25 s script. |
| references/long-form.md | Writing or fixing a 200 s script. |
| references/visuals-and-text.md | Choosing the opening shot, overlays, captions or safe zones. |
| references/psychology-for-scripts.md | Choosing a hook angle or answering a trip anxiety. |
| references/brand-and-claims.md | Any fact, claim, difficulty line, aurora or snow mention. |
| references/ugc-style.md | Any ugc_talk or ugc_text script, any TikTok, any creator brief, disclosure, music, consent or safety on camera. |
| references/creator-patterns.md | You want the measured creator numbers or need to justify a UGC choice. |
| examples/short-fictional.md, examples/long-fictional.md | You want to see a passing voiceover script before writing. |
| examples/short-ugc-talk-fictional.md, examples/short-ugc-text-fictional.md | You want to see a passing ugc script before writing. |
| examples/creator-brief-fictional.md | You are writing a creator brief. |
