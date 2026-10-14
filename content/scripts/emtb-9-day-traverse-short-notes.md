# e-MTB one way tour short: notes

Script: `content/scripts/emtb-9-day-traverse-short.md`. Source idea: `content/scripts/emtb-9-day-traverse-draft.md` (left untouched; the git log labels it unreviewed facts, REJECT). Status: passes the validator in draft mode. `--final` fails only on the intentional placeholders (BR13) and the three unverified rows (F04). Nothing can be filmed or published until F1 is confirmed. If F1 cannot be confirmed in writing, drop the script.

## Brief

- Platform: reels (the same cut can go to Shorts; TikTok needs a style and music recheck).
- Style: voiceover. Tier: short, 25 s cap, declared 25 s as asked (the word target scales with the length: 40 to 55 words at 25 s).
- Creator: staff. Relationship: staff. Sound: original (natural ride sound under a calm read).
- Narrator: standard.
- Takeaway: the tour runs one way and finishes at the Sognefjord.
- Tour: no tour id. `tours.json` holds 7 ski, snowshoe, aurora and backcountry tours and no bike tour; `product-marketing.md` lists winter products only. The e-MTB tour comes only from the rejected draft.
- Objection: where do I end up, and how do I get back? Where: beat 4 and its overlay. Getting back: a placeholder sentence in the caption, waiting on the client. Both halves are the writer's reading of the likelier doubt, not a client brief.
- Structure: outcome-first rewind. The hook asks where the tour finishes, the same handlebar framing returns at the answer, one ask.
- Size as validated: 5 beats, 30 spoken words (each placeholder counts as 1 word), 12.5 s estimated. With the guide's line at 14 words in beat 3, 40 words and about 17 s.

## Caption

Where do you finish this bike tour? The e-MTB tour page is linked in the bio. [VERIFY: one sentence on how guests get back from the finish, Sameer or the client] #emtb #norway

## Open items, grouped by who confirms

Sameer or the client, facts (kind: fact):
1. F1, first and blocking: the tour exists, its name as sold, it is on sale, and a page sells it (with its URL). Put the client's own words in quotes in the source cell. Beat 5 and the caption rest on it. The CTA and caption now say only that a page sells the tour, not that it shows the full route.
2. F3: where the tour finishes, in the client's own words, and whether a boat follows the riding. The draft says "Voss to the Sognefjord" and "Six riding days later, a boat carries you down Norway's longest fjord". "You finish at the Sognefjord" in beat 4 and its overlay rest on this. If the finish is somewhere else, change the voice, the overlay and the hook together.
3. Getting back: how guests get back from the finish. Not in the draft. It fills the caption placeholder.
4. Tour name as sold. The voice says "electric mountain bike tour page" because "e-MTB" in the voice trips the capitals rule and no name is sourced.

Sameer, decision (kind: other):
5. Link placement. Reels captions do not make links clickable, so the overlay says "Link in bio" and the caption says the page is linked in the bio. Confirm the link goes in the bio, or change the overlay and the caption.
6. Who films and who is on camera. The disclosure is spoken and on screen at 3 s as "Outdoor Norway staff filmed all of this" and "Filmed by Outdoor Norway staff". "All of this" and "staff" are unconfirmed. If a guide appears, use the guide's own role words in both places.

The guide who has ridden the route (kind: fact, footage):
7. Hand over `.claude/skills/scriptcraft/assets/guide-moment-intake.md`. Answer 3 is the one moment for beat 3, 14 words or fewer, quoted in row F6. Answers 5 and 9 give the rider benefit and the doubt; ask the guide to choose a moment that shows what the rider gets from a route that does not loop back. Answer 1 gives the role words for beat 2. Without a real moment the hook, loop and visuals stay at about 5 to 6 out of 10, and the viewer still has no reason why a one way route matters.
8. Footage (kind: footage): the shot of the guide's moment, filmed where it happens; the finish, filmed at the same handlebar framing as beat 1. No clip is assumed to exist.

Sameer, permission and release (kind: permission, release):
9. Filming permission at the places on the route. A written release from every identifiable rider in beats 2, 3, 4 and 5, with separate boxes for organic posting and ads. [VERIFY with counsel: Norwegian image right and GDPR]

Sameer, other:
10. Repo hygiene: the rejected draft fails `tools/test_repo_integrity.py` (arrow glyphs and a middle dot in its table). It was left untouched. Decide whether to edit or archive it.

## Parked fact rows

Removed from the script's facts table because no beat cites them. Each stays a claim from the rejected draft until the client confirms it.

- F2: a descent that starts with glaciers in view and ends at a fjord edge (draft, beat 1). Needed only if a version brings the glacier hook back.
- F4: a boat down the fjord after six riding days. Folded into the F3 question above.
- F5: a bike is provided to each guest (draft: "A full-suspension e-MTB is waiting in Voss, set up for you"). Not in any beat. Never write "all gear included" (do-not-claim list in `product-marketing.md`).
- F7: what a one way route gives the rider, in the guide's words. A short allows 3 facts per script (`tiers.json`, short, facts.per_script_max) and the script cites F1, F3 and F6, so F7 has no fourth beat. Once the guide answers, pick one: the guide's moment carries the benefit (F6 and F7 become one row), F7 replaces F6, or F7 goes in a second short.
- Not in the table at all: trip length, riding days, price, departures, Bergen arrival and "Norway's longest fjord" (a superlative needs a named source, BR11). Confirm only for a longer version.

## Assumptions

- Nobody was available to ask, so the conservative defaults apply: creator and relationship staff, disclosure spoken and on screen, sound original, standard narrator, link in the bio. None is confirmed.
- The draft is a claim to check, not a source. Its words are quoted in the facts rows and every row is verified no.
- Spoken claims carry a `[VERIFY]` in their voiceover cell: beats 2, 3, 4 and 5. Beat 1 is a question.
- "Finish" is the one word for where the tour stops, in beats 1 and 4 and both overlays. "End" appears nowhere in the voice or the overlays.
- Visuals come only from filming that is possible on any guided ride: a mounted camera, a fixed camera beside the trail, a camera operator standing still, stops on level ground. No scenery, place or weather is shown except where a `[VERIFY]` says so. Shot timing is stated.

## Accepted warnings

- F04 on F1, F3 and F6 (fact used but not verified yes): they stay until the client or the guide confirms the rows. `--final` blocks on them by design.
- W02 (30 words, target 40 to 55): each placeholder counts as one word, so the count reads low. It clears once the guide's line is in (about 40 words). Padding now would add claims.
- W03 on beat 3 (1 word) and beat 4 (6 words): beat 3 is a placeholder for the guide's line; beat 4 is the answer to the hook and says no more than row F3. Adding words now would add unsourced claims.
- INFO on beats 3 and 4 (about 6 s and 4 s with no voice): the guide's line fills beat 3. Beat 4 leaves room for the finish picture to play.

## Variant

- Hook: "Your bike tour starts in Voss. Where does it finish?" Hypothesis: naming the start gives the viewer a map to anchor the question, so it should beat "Where do you finish this bike tour?" on hold through the first 3 s; the main hook keeps the edge on a muted first frame because it has one place name fewer. It needs F3 confirmed and spends a second place name.
- Call to action: "Send this to your riding partner." Hypothesis: a send ask should beat the tour page line on shares per reach, while the main line should win on tour page visits. It still needs F1, because the whole script does.

## What changed against the review findings

| Finding | Change | Still waits on |
|---|---|---|
| 1 F1 unconfirmed, CTA and caption overreach | F1 kept as no with a note to quote the client; CTA and caption say a page sells the tour and name it as the e-MTB tour page; link placement is a decision for Sameer | Sameer or the client |
| 2 rows and uncited lines | Beat 2 "different landscape" shots and the staff overlay claim now carry a placeholder or are cut; F2, F4, F5, F7 moved to Parked fact rows; F3 reworded to the draft's route line, "point to point" dropped | F3, who films |
| 3 loop not closed, "end" shifts | Hook asks where the tour finishes, beat 4 names the Sognefjord from the draft, both overlays carry the question and the answer, "finish" is the only word used | F3 |
| 4 two beats empty | Beat 3 is a slot for the guide's moment with a word budget; the benefit cannot have its own beat under the 3 fact cap, so the guide is asked for a moment that shows it | the guide |
| 5 brief not from the client | Objection now names both halves of the likelier doubt; defaults listed as unconfirmed | Sameer or the client |
| 6 and 10 disclosure | Spoken and on screen at 3 s with the same role words; who films and who is in shot is open item 6; releases are item 9 | Sameer or the guide |
| 7 confirm F1 and F3 in writing | Open items 1 and 2 | Sameer or the client |
| 8 payoff answers the hook | Beat 4 answers with the place; beat 1 overlay carries the question | F3 |
| 9 guide intake, cut two lines | Intake is open item 7; "Watch what's behind the bikes." and "It doesn't end where it began." are cut | the guide |
| 11 tidy | Uncited rows parked; the helmet strap hands shot replaced by boots stepping off pedals; beat 5 is an ask ("Open ... page") and its overlay says where, not what | footage |

## Safety line for riding shots

- Every riding shot shows helmets on and a guide riding ahead of the group.
- Helmets come off only once the group has stopped, on level ground away from edges and the water.
- Nobody films while riding. Use a handlebar-mounted camera or a camera operator standing still beside the trail.
- No jumps, drops or speed shots for the camera. The group rides at the guide's pace.
- No "send it" or "no risk" wording in captions or overlays.
