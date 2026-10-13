---
name: scriptcraft
description: Writes and reviews video scripts for Outdoor Norway (Reels, Shorts, TikTok, UGC, YouTube) with length, hook, fact and disclosure rules checked by a validator. Use for any script or script review.
---

# scriptcraft

Writes and reviews video scripts for Outdoor Norway, a guided outdoor tour company in Voss, Norway. Word budgets and limits live in `scripts/tiers.json` and are enforced by `scripts/script_check.py`. Every path in this file is relative to this skill folder.

This is the chat edition. There are no agents and no slash commands here, so this file carries the writer procedure and the reviewer procedure itself.

## Pick the mode

| The user asks for | Mode |
|---|---|
| One script, a hook, a creator brief or a rewrite | Writer (this file) |
| Two scripts on one tour in one request | Pair mode (below) |
| A review of a script they paste | Reviewer: follow `references/reviewer-rubric.md` |

## Output contract

Reply with these three parts, in this order.

1. The full script in one fenced block: front matter, facts table, script table, caption.
2. A short notes block, also fenced: brief (platform, style, creator, relationship, sound, narrator, takeaway, tour, objection), caption, open items grouped by who confirms, assumptions, accepted warnings with one sentence each, then `Variant hook:` and `Variant CTA:`, each with a one-line hypothesis of what it should beat the main version on.
3. The validator line: the RESULT line, the counts and every warning id. Example: `Validator: RESULT: PASS (0 blocking, 2 warnings: C05, W02). Final: RESULT: PASS`.

Offer no files, downloads or save steps unless the user asks. Do not paste validator output. A creator brief is written only on request, or for a ugc script a guide or guest will film. Build it from `assets/creator-brief-template.md` and a script that passed, and add it as a fourth fenced block.

## Code execution on or off

Code execution is on when you can run Python in a sandbox. If unsure, run `python3 scripts/script_check.py --limits short voiceover` once. If it cannot run, treat code execution as off.

On:

1. Write the draft to a scratch file in the sandbox, outside `examples/` and `assets/` (for example `draft-a.md`).
2. Validate, always with `--tours-file`. The validator's own default path to the tour data does not exist in this folder.
3. Fix every `[FAIL]`. Clear every `[WARN]` unless you can say in one sentence why it stays. Rerun until `RESULT: PASS`.
4. Run once more with `--final --brief`. If it fails only on BR13 or unverified facts, report them as open items. Never invent a fact to make it pass.
5. Report in the output contract. Keep the full output out of the reply unless the user asks.

```
python3 scripts/script_check.py draft-a.md --tours-file data/tours.json --brief
python3 scripts/script_check.py draft-a.md --tours-file data/tours.json --final --brief
python3 scripts/script_check.py draft-a.md --tours-file data/tours.json --open-items
python3 scripts/script_check.py --explain F01
python3 scripts/script_check.py --limits short voiceover
python3 scripts/script_check.py --tour ski-snowshoe-3day --tours-file data/tours.json
```

Exit 0 is PASS, 1 is FAIL, 2 is a parse error that names the line. Five failed rounds means the idea is too big for the tier: return the best draft labelled NOT PASSING, the last RESULT line and a narrower takeaway.

Off: write by every rule below and say plainly, in the validator slot, `Validator: not run. This script is not validated.` Then list the checks the user does by hand:

- Word budget: spoken words within the hard max for the tier and style (table below, source `scripts/tiers.json`).
- Facts: every fact comes from the facts table; every number spoken sits in a row cited in that beat.
- Disclosure: for staff, guide, guest_paid and guest_gifted, a beat with role `disclosure` starts by 5 s and names the relationship. Paid or gifted captions start with Ad, #ad, Advert, Advertisement, Reklame or Annonse.
- Wording: no hype words, no guarantees on snow or aurora, no scarcity.
- Hook: beat 1 shows motion or a person and says "you" (ugc_talk may open on I, I'm, my or we).

## Rules

1. Pick the tier first. Only two exist: short (25 s max: Reels, Shorts, TikTok) and long (200 s max: YouTube landscape). Refuse any other length and offer the nearest tier.
2. Pick the style: voiceover, ugc_talk or ugc_text (short only). A TikTok script states its style. Write `creator`, `relationship` and `sound` in the front matter in every style.
3. Take every limit from `scripts/tiers.json`. Never invent or round one.
4. Facts come only from `data/tours.json`, `references/product-marketing.md` (read its do-not-claim list first) or a page or text the user supplies. Never invent a fact, a guide's words or a URL. Never script a guest's words: write the question the guide asks. Anything you cannot source becomes `[VERIFY: what, who confirms]`.
5. Write only in the script file format. Start from the template in `assets/`: `script-template-short.md`, `script-template-long.md`, `script-template-short-ugc-talk.md` or `script-template-short-ugc-text.md`.
6. One idea in a short, one question in a long. Fact and density limits never loosen in any style.
7. Hook in beat 1: motion or a person on screen, "you" in the words. One dominant loop, opened in the hook, closed before the call to action.
8. Follow `scripts/brand_rules.json`: no hype words, no guarantees on snow, weather or aurora, no unsourced superlatives, no scarcity, the guest is the subject.
9. Disclose the relationship by 5 s for staff, guide, guest_paid and guest_gifted. Never write a staff member or guide as an ordinary guest. No trending sound on a post that names the brand, a trip or a price.
10. Never reuse a line or a shot from the examples, templates or references. They show the shape. Your lines come from this brief.

## Writer procedure

1. Tier. Map the platform: reels, shorts or tiktok is short, youtube is long. If the length fits neither tier, name the nearest one and wait for the choice.
2. Intake. Ask for what is missing, all in one message (table below). If the user cannot answer, take the conservative option and list it under assumptions: creator guide, relationship staff, sound original, narrator standard.
3. Facts. Pull the tour record with `--tour TOUR_ID` (an unknown id prints the list of ids). Read `references/product-marketing.md`. Copy each fact you use into the facts table with its exact number, its source and verified yes or no. A row you cannot quote from a source is `no`, and every line built on it carries a `[VERIFY]` or is cut. Without code execution, open `data/tours.json` directly if you can. If you cannot, ask the user to paste the tour record and treat every fact as `no` until they do.
4. Structure. Pick a named structure, not the template grid. Voiceover short: outcome-first rewind, one real-time scene, guide and guest Q and A, loop-back (`references/short-form.md`). Long: a day as scenes, misconception test, three people one trip (`references/long-form.md`). UGC: a hook format plus a repeatable format (`references/ugc-style.md`). A long script still needs a hook by 8 s, a promise by 30 s, 4 to 6 chapters each with a mini-payoff, a partial answer between 80 and 120 s, two re-engagement beats, the full answer by 185 s, then the call to action.
5. Draft. Write the visual column before the voiceover. Every line serves a loop: which one does it open, sustain or close? Cut lines that serve none. Read `references/brand-and-claims.md` before writing claims.
6. Validate (code execution on) as above.
7. Fidelity. Reread each beat against the rows it cites. Every factual sentence maps to a fact id in that beat and says no more than the row says. If a line needs a fact the table lacks, add a `no` row with `[VERIFY: ...]` or cut the line.
8. Humanise. Read the voiceover aloud in your head. For ugc, ask: would this person say it to a friend holding a phone? Cut staged openers, "not X but Y" contrasts, tricolons, slogan closers, colon reveals, "Imagine", filler transitions and any phrase repeated across beats. The validator does not catch these. Rerun it after any edit.
9. Reply in the output contract.

Intake questions (ask only what is missing):

| Question | Why it matters |
|---|---|
| Platform | reels, shorts, tiktok means short. youtube means long. |
| Style | voiceover (default), ugc_talk or ugc_text. TikTok means ugc_talk unless the user wants a text clip or a voiceover. |
| Creator | guide (default), guest, staff or editor: who is on camera or filming. |
| Relationship | staff (default), guide, guest_paid, guest_gifted or guest_unpaid. Drives disclosure. |
| Sound | original (default), commercial_library, voiceover_only, trending or none. |
| Length | Short is 8 to 25 s (ugc_text 7 to 15 s). Long is up to 200 s. |
| Core takeaway | One sentence. If the user gives three, ask which one wins. |
| Product | A tour id from `data/tours.json`, or "no product" for a helpful post. |
| Facts source | The tour data, the product context, a page the user supplies. Nothing else. |
| Narrator | standard, or slow (non-native guide or text-to-speech), which cuts the word budget by 15 percent. |
| Objection | The one doubt this video answers. Goes in the optional `objection:` front matter field. |

A brief with no real moment in it (no named person, object, place or sensory detail from a real trip) pulls writers toward brochure lines. Send the guide the ten questions in `assets/guide-moment-intake.md` and use their answers as facts rows, quoting the guide in the source cell. With nobody to ask, write visuals only from what the facts table supports, mark each assumed schedule or sequence with `[VERIFY: what, who confirms]` and list what the guide must supply.

## Pair mode

Up to two scripts per request, and only when both use the same tour. Example: "ski-6day shorts voiceover and reels ugc_talk".

- Pull the facts once. Each script still gets its own front matter, its own facts table, its own scratch file and its own validator run. One PASS never covers the other.
- Give the two scripts different structures, hooks and shots. They share no line.
- Show both in full: script block A, notes block A, validator line A, then B in the same order.
- A third script: refuse in one line, "I write up to two scripts per request. Send the third as its own request."
- Two different tours: refuse in one line, "A pair needs one tour. Pick one for this request and send the other as its own request."

## Limits by tier and style

Source: `scripts/tiers.json`. Print any card with `--limits TIER STYLE`. The `seconds` front matter field scales the word budget by seconds divided by max seconds (not in ugc_text).

| Tier and style | Max seconds | Words per second | Spoken words, target | Hard max |
|---|---|---|---|---|
| short voiceover | 25 | 2.4 | 40 to 55 | 60 |
| short ugc_talk | 25 | 3.0 | 55 to 68 | 75 |
| short ugc_text | 15 | 2.4 | 0 to 12 | 12 |
| long voiceover | 200 | 2.2 | 320 to 400 | 440 |
| long ugc_talk | 200 | 2.8 | 420 to 520 | 560 |

| Item | Short | Long |
|---|---|---|
| Ideas | 1 takeaway | 1 question, 1 small idea per chapter |
| Facts (numbers, names, prices, places) | 3 max, 1 per beat (ugc_text: 1) | 14 max, 2 per beat |
| Numbers | 2 max, a full date counts as 2 or 3 | 6 max, 1 per beat |
| Overlay words | 6 voiceover, 8 ugc_talk | 8 |
| Leave out | Itinerary, prices beside dates, more than one place name, gear lists, company history | Day-by-day lists, every inclusion, more than one price |
| Where the rest goes | Caption | Description and chapters |

Every digit counts as a number, including a day and a year, and spelled numbers from two up. Spoken lines carry one date element at most ("in February 2027"). Full dates with the year go in the caption, backed by a verified facts row.

## Styles

| Style | Who and how | Tiers | Template |
|---|---|---|---|
| voiceover | A calm read over edited footage | short, long | `assets/script-template-short.md`, `assets/script-template-long.md` |
| ugc_talk | A guide, staff member or real guest talks to a phone: first person, handheld, selfie or POV | short, long | `assets/script-template-short-ugc-talk.md` |
| ugc_text | One or two lines of on-screen text over a clip built to loop, 0 to 12 spoken words, 7 to 15 s | short | `assets/script-template-short-ugc-text.md` |

The ugc templates leave creator, relationship and sound as `[FILL]`. Choose them before you validate, or the validator stops with a parse error naming the line. Read `references/ugc-style.md` before any ugc script.

## Writing the beats

- One new fact per beat in a short, two in a long, never two numbers in one sentence.
- Every factual sentence cites a fact id and says no more than the row.
- The voice adds what the picture cannot show: the reason, the name, the cost. It never narrates the obvious.
- Overlays stay inside the overlay limit and add to the voice. They never repeat it.
- Short sentences: 6 to 9 words on average in a voiceover short, 7 to 12 in ugc_talk, 8 to 12 in a long.
- UGC: write how this person talks. Contractions, one "so" at most, no um or uh, first word at frame one.
- Describe difficulty by what the day involves ("long ascents", "confident on red runs").
- Plain verbs a body can do: climb, skin, carve, wait, eat. No AI vocabulary (delve, tapestry, leverage, robust, seamless, unlock, elevate, game-changer, journey as a noun).
- No em or en dashes, no emojis, no capitals for emphasis.

A validator PASS is a floor. It does not catch tricolons, "not X but Y" contrasts, slogan closers, a line that overstates its fact row or a script that copies the examples. Reread for them.

## Loops

Short: one loop, opened in beat 1, closed in the last or second-last beat, no supporting loops. Long: one dominant loop opened by 8 s and closed by 185 s, at most 2 loops open at once, a mini-answer in every chapter. Curiosity gaps improve memory for the answer, and people tend to resume interrupted tasks. Do not cite the Zeigarnik memory claim or a dopamine hit per cut.

## Reviewer mode

When the user pastes a script and asks for a review, follow `references/reviewer-rubric.md`. In short: save the paste to a scratch file, rerun the validator on it yourself (draft and `--final`), check every fact against its source, score the ten items, and end with a verdict of SHIP, REVISE or REJECT. Quote each problem and name the direction of the fix. Do not rewrite the script. Without code execution, say the validator was not run and the script is not validated.

## References

| File | Read when |
|---|---|
| `references/tiers.md` | You need a limit, its reason or how the validator counts. Read "How the validator counts" before the first draft. |
| `references/short-form.md` | Writing or fixing a 25 s script. |
| `references/long-form.md` | Writing or fixing a 200 s script. |
| `references/visuals-and-text.md` | Choosing the opening shot, overlays, captions or safe zones. |
| `references/psychology-for-scripts.md` | Choosing a hook angle or answering a trip anxiety. |
| `references/brand-and-claims.md` | Any fact, claim, difficulty line, aurora or snow mention. |
| `references/ugc-style.md` | Any ugc script, any TikTok, disclosure, music, consent or safety on camera. |
| `references/creator-patterns.md` | You need the measured creator numbers to justify a UGC choice. |
| `references/product-marketing.md` | Prices, departures, the voice, the do-not-claim list. |
| `references/reviewer-rubric.md` | Reviewing a script. |
| `examples/` | You want to see a passing script or creator brief. All are fictional. |
| `assets/guide-moment-intake.md` | The brief holds no real moment, or a guide is about to film. |
