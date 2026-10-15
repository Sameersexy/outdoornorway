# e-MTB one way tour short: notes

Script: `content/scripts/emtb-9-day-traverse-short.md`. Source: Sameer's original 42 s script (pasted in session; the saved copy was deleted on request and stays in git history, commit 34f57d9). Status: passes the validator in draft mode (68 words, 22.7 s estimated, 6 beats, 3 facts, narrator brisk). `--final` fails on the placeholders (BR13) and the three unverified fact rows (F04). Nothing can be filmed or published until F1 is confirmed. If F1 cannot be confirmed in writing, drop the script.

## Brief

- Platform: reels (the same cut can go to Shorts; TikTok needs a music and style recheck).
- Style: voiceover. Tier: short, 25 s cap, declared 25 s. Narrator: brisk (3.0 words per second, 75 word hard maximum), see "Pace" below.
- Voice: guest facing, "you", "our local guides". This is Sameer's own voice from the original script.
- Tour: no tour id. `tours.json` holds winter tours only and `.claude/product-marketing.md` lists winter products only. Every e-MTB fact comes from the original script and is marked unverified.
- Objection: is this a loop, or does the route go somewhere? Hook raises it, beat 2 answers it, beat 5 pays it off with the fjord picture.
- Relationship and creator are left out of the front matter on purpose, so the validator skips the disclosure rule. See open item 6.

## Pace (edit round 3)

Sameer's note: in 23 seconds people can say a lot more words, and the script was slow.

- The standard short voiceover limit is 2.4 words per second, 60 words hard maximum. The old script (55 words) sat inside it and read slowly.
- A new opt-in narrator, `brisk`, is in `.claude/skills/scriptcraft/scripts/tiers.json` (commit 6fbcd61). It reads at 3.0 words per second, the pace the `ugc_talk` short tier already uses, with a 75 word hard maximum and a 50 to 69 word target. Facts, hook words, sentence length and overlay limits do not change.
- The script went from 55 to 68 words (up 24 percent). The estimate is 22.7 s against the 23 s warning line, so about 69 words is the practical top for a 25 s short.
- The 3.0 pace is a choice, not a measurement of Sameer's narrator. It matches the repo's own talking-clip evidence. If the narrator is faster, raise `pace` for `brisk` in `tiers.json` (one number) and the budget grows with it.
- Brisk is for a fluent narrator reading a punchy, spoken-style short. A non-native speaker or a text-to-speech voice should use the standard or slow narrator, and then this script is too long: 68 words is over the standard 60 word hard maximum. See "Fallback cuts" below.

## Edit round 3: faster and more words

14 of the 68 spoken words are new (21 percent), all taken from the original script. One word was dropped ("from" in beat 2).

| Beat | Before | After |
|---|---|---|
| 2 | "You ride from Voss to the Sognefjord." Overlay "Voss to the Sognefjord" | "You ride Voss to the Sognefjord." Overlay "One way" (the old overlay repeated the voiceover) |
| 3 | "The motor takes the climbs your legs would quit on." | Adds "You didn't pack a bike to get here." in front (original line without the "And"). Helmet on in the climbing shot |
| 4 | Overlay "Earn the view. Keep the descent." | Overlay "Local guides. Singletrack." Helmets on in both shots |
| 5 | "Light that doesn't want the day to end." | Adds "Earn the view. Keep the descent." in front (original line, moved from the overlay into the voice). Helmets on in the riding shot |
| Facts | F2 covered the bike and the motor | F2 widened to include that guests do not pack the bike (beat 3 now says it) |

Beat 3 is the densest: 18 words in a 6 s beat, no slack.

## Edit round 2: more fun, within one third

About 31 percent of the spoken words were new at the time (17 of 55). Beats 2 and 4 and the whole structure were untouched.

| Beat | Before | After |
|---|---|---|
| 1 | overlay "Point-to-point across Norway" | overlay "Same hotel. Every night." (brings back "every night" from the original, which the hook word cap would not fit in the voice) |
| 3 | "A full-suspension e-MTB waits for you in Voss." | "The motor takes the climbs your legs would quit on." Overlay "Full-suspension e-MTB" keeps the bike detail. Shots: power button, then a grinning climb |
| 5 | "The mountains hand you to the fjords." | "Light that doesn't want the day to end." Overlay "Glacier to fjord. One ride." Both lines are from the original |
| 6 | "Tap the link for the route and dates." | "Tap the link for the route." Drops a claim about what the page shows and clears a pacing warning |

## Caption

Most bike trips circle back to the same hotel. This one runs from Voss to the Sognefjord. [VERIFY: days, riding days, price and departures from Sameer's original script, Sameer or the client] [LINK: e-MTB tour page] #emtb #singletrack

## Open items, grouped by who confirms

Sameer or the client, facts (kind: fact):
1. F1, first and blocking: the tour runs one way from Voss to the Sognefjord. Put the client's own words in the source cell.
2. F2: a full-suspension e-MTB is part of the tour, guests do not bring a bike, and the motor takes the climbs. Confirm "included" and the word "full-suspension".
3. F3: wording the client accepts for "singletrack only our local guides know".
4. Caption placeholder: days, riding days, price and departures. The script states none of them. The original had 9 days, 6 riding days, 40,000 NOK and 3 departures in 2027, unverified.
5. Tour page URL for the `[LINK: e-MTB tour page]` placeholder. Do not guess it.

Sameer, decision (kind: other):
6. Who films and who is on camera. If staff, a guide or a paid guest film it, the validator asks for a relationship and a disclosure beat. Decide before publishing.
7. Link placement. Reels captions do not make links clickable. "Tap the link" suits an ad or a link sticker; for an organic post, change the CTA to "link in bio".
8. Narrator: who reads it. A fluent speaker can use brisk. Otherwise see "Fallback cuts".
9. Pace: is 3.0 words per second right for the narrator? If faster, change the brisk `pace` in `tiers.json`.

Sameer, permission and release (kind: permission, release):
10. Filming permission along the route and a written release from every identifiable rider, with separate boxes for organic posting and ads. [VERIFY with counsel: Norwegian image right and GDPR]

## Read-aloud notes

- "Sognefjord" in beat 2 and the caption is a name a non-Norwegian narrator may misread. Have a Norwegian speaker say it, or give the narrator a recording of the local pronunciation.
- "singletrack only our local guides know" is a mouthful at 3.0 words per second. Leave a short breath before "singletrack" rather than speeding up.
- Beat 3 has two sentences in 6 s with no spare time. Read the first one quickly and the second with a short pause before it.

## Fallback cuts

If the narrator reads slower than 3.0 words per second, cut in this order. Each cut keeps every fact row and the original wording.

1. Beat 3: drop "to get here" (18 words to 15).
2. Beat 5: drop "Keep the descent." (14 words to 11).
3. Beat 2: use "Voss to the Sognefjord." without "You ride" (11 words to 9).

Cutting all three gives 60 words. Under the standard narrator that passes but warns (T02: 25.0 s estimated against the 23 s line, and W02: target 40 to 55 words). For a standard or slow narrator, use the earlier 55 word version instead (22.9 s, no warnings of that kind): `git show 1c87e65:content/scripts/emtb-9-day-traverse-short.md`.

## Not used from the original

Bergen arrival, the boat on the Sognefjord, "Norway's longest fjord" (a superlative needs a named source), "past every mountain you just rode", nine days, six riding days, price and departures. A short allows 3 facts per script, and F1 to F3 use them. A boat line would be a fourth fact, so it belongs in a longer cut.

## Assumptions

- Facts are the original script's claims, not sources. Every row is verified no.
- Visuals use only filming that is possible on any guided ride: a mounted camera, a camera operator standing still, stops on level ground. "Grinning" in beat 3 needs a rider who is actually enjoying the climb, not a staged smile.
- Beat 4 is a POV shot. Cut fast, ride at the guide's pace.
- "Light that doesn't want the day to end" is read as a mood line from the original, not a claim about daylight hours. The glacier and fjord shots in beat 5 should be filmed in evening light, not staged.

## Accepted warnings

- F04 on F1, F2 and F3: stays until the client confirms the rows. `--final` blocks on it by design.
- H03 (no "you" in the first 3 s): the hotel line is the required opener. "You" arrives at 3 s in beat 2.
- R02 on "e-MTB" in the beat 3 overlay: the original wording, kept.

## Safety line for riding shots

- Every riding shot shows helmets on and a guide riding ahead of the group.
- Helmets come off only once the group has stopped, on level ground away from edges and the water.
- Nobody films while riding. Use a handlebar-mounted camera or a camera operator standing still beside the trail.
- No jumps, drops or speed shots for the camera. The group rides at the guide's pace.
- No "send it" or "no risk" wording in captions or overlays.
