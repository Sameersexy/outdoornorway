# e-MTB one way tour short: notes

Script: `content/scripts/emtb-9-day-traverse-short.md`. Source: Sameer's original 42 s script (pasted in session; the saved copy was deleted on request and stays in git history, commit 34f57d9). Status: passes the validator in draft mode (63 words, 21.0 s estimated, 6 beats, 3 facts, narrator brisk). `--final` fails on the placeholders (BR13) and the three unverified fact rows (F04). Nothing can be filmed or published until F1 is confirmed. If F1 cannot be confirmed in writing, drop the script.

## Brief

- Platform: reels (the same cut can go to Shorts; TikTok needs a music and style recheck).
- Style: voiceover. Tier: short, 25 s cap, declared 25 s. Narrator: brisk (3.0 words per second, 75 word hard maximum), see "Pace" below.
- Voice: guest facing, "you", "our local guides". This is Sameer's own voice from the original script.
- Tour: no tour id. `tours.json` holds winter tours only and `.claude/product-marketing.md` lists winter products only. Every e-MTB fact comes from the original script and is marked unverified.
- Objection: is this a loop, or does the route go somewhere? Hook raises it, beat 2 answers it, beat 5 pays it off with the fjord picture.
- Audience: assumed to be adult riders who read English and are weighing a guided multi-day e-MTB trip. The original script does not say. [VERIFY: Sameer]
- Relationship and creator are left out of the front matter on purpose, so the validator skips the disclosure rule. See open item 7.

## Pace (edit round 3)

Sameer's note: in 23 seconds people can say a lot more words, and the script was slow.

- The standard short voiceover limit is 2.4 words per second, 60 words hard maximum. The old script (55 words) read at that pace.
- A new opt-in narrator, `brisk`, is in `.claude/skills/scriptcraft/scripts/tiers.json` (commit 6fbcd61). It reads at 3.0 words per second, the pace the `ugc_talk` short tier already uses, with a 75 word hard maximum and a 50 to 69 word target. Facts, hook words, sentence length and overlay limits do not change.
- The script went from 55 to 63 words (up 15 percent) and from 2.4 to 3.0 words per second (up 25 percent). The validator estimate is 21.0 s.
- A first round 3 draft had 68 words (22.7 s estimated). A read-aloud check that adds a 0.4 s breath after every sentence put it at 26.8 s, over the 25 s cap, and the same check called beats 1, 3 and 5 rushed. The draft was cut to 63 words. On the same strict count (breath after every sentence, 0.5 s tail) that version ends at about 23.9 to 24.7 s, inside the 25 s cap. Treat 63 as the practical top. The 68 word draft is in commit eee3e5b if the narrator turns out to be fast.
- The 3.0 pace is a choice, not a measurement of Sameer's narrator. It matches the repo's own talking-clip evidence. If the narrator is faster, raise `pace` for `brisk` in `tiers.json` (one number) and the budget grows with it.
- Brisk is for a fluent narrator reading a punchy, spoken-style short. A non-native speaker or a text-to-speech voice should use the standard or slow narrator, and then this script is too long: 63 words is over the standard 60 word hard maximum. See "Fallback cuts" below.

## Edit round 3: faster and more words

11 of the 63 spoken words are new (17 percent), all from the original script. Three words were dropped ("You ride from" in beat 2).

| Beat | Before | After |
|---|---|---|
| 1 | Visual: mid-descent, fjord "far below" | Visual: handlebar camera on an easy-pace trail, the guide ahead sets the pace and the gap. No fjord, exposure or speed in the hook shot |
| 2 | "You ride from Voss to the Sognefjord." Overlay "Voss to the Sognefjord" | "Voss to the Sognefjord." (Sameer's own phrase). Overlay "One way". "You ride" would say you ride the whole route, and the original has a boat on the fjord. The camera operator stands still well back from any edge |
| 3 | "The motor takes the climbs your legs would quit on." | Adds "You didn't pack a bike to get here." in front (original line without the "And"). The climbing shot names a handlebar camera, a gentle climb and a helmet on |
| 4 | Overlay "Earn the view. Keep the descent." | Overlay "Local guides. Singletrack." The POV shot is a handlebar camera on a gentle gradient at the guide's pace. Helmets on in both shots |
| 5 | "Light that doesn't want the day to end." Overlay "Glacier to fjord. One ride." | Adds "Earn the view." in front (original line). "Keep the descent." moves to the overlay. The glacier and evening light shot is gone: no fact row backs it, and "One ride" reads as a single ride on a multi-day tour. Shots are the fjord and mountains with the operator well back from any edge, then riders on a gentle downhill with the guide ahead |
| 6 | Helmets off, "the fjord behind them" | Group stopped on level ground well back from the water and any edge, then helmets off |
| Facts | F1 "one way". F2 bike and motor. F3 "guests would not find alone" | Each row now says what the spoken line says. F1 quotes the original in full and marks "no return to the start, no retracing" as a reading to confirm. F2 says the tour provides the bike (not "included") and adds "your legs would quit on". F3 quotes "only our local guides know" and adds that local guides lead |

Beat 3 is the densest: 18 words. On a strict breath count it needs about 6.4 s in a 6 s window, so the voice may run about 0.4 s into beat 4. Fallback cut 1 removes the problem.

## Edit round 2: more fun, within one third

About 31 percent of the spoken words were new at the time (17 of 55). Beats 2 and 4 and the whole structure were untouched.

| Beat | Before | After |
|---|---|---|
| 1 | overlay "Point-to-point across Norway" | overlay "Same hotel. Every night." (brings back "every night" from the original, which the hook word cap would not fit in the voice) |
| 3 | "A full-suspension e-MTB waits for you in Voss." | "The motor takes the climbs your legs would quit on." Overlay "Full-suspension e-MTB" keeps the bike detail. Shots: power button, then a grinning climb |
| 5 | "The mountains hand you to the fjords." | "Light that doesn't want the day to end." Both lines are from the original |
| 6 | "Tap the link for the route and dates." | "Tap the link for the route." Drops a claim about what the page shows and clears a pacing warning |

## Caption

Most bike trips circle back to the same hotel. This one runs from Voss to the Sognefjord. [VERIFY: days, riding days, price and departures from Sameer's original script, Sameer or the client] [LINK: e-MTB tour page] #emtb #singletrack

## Open items, grouped by who confirms

Sameer or the client, facts (kind: fact):
1. F1, first and blocking: the tour runs one way from Voss to the Sognefjord and never returns to the start or retraces its route. Put the client's own words in the source cell.
2. F2: the tour provides a full-suspension e-MTB, guests do not bring a bike, and the motor takes the climbs. Do not write "included" until the price is confirmed.
3. F3: "singletrack only our local guides know" claims exclusivity. Confirm it, or use a softer line such as "singletrack our local guides know well".
4. Beat 5 line "Light that doesn't want the day to end" is Sameer's original wording and implies long evening light. Confirm it fits the season of the departures.
5. Caption placeholder: days, riding days, price and departures. The script states none of them. The original script has figures for them, all unverified, so take the current ones from the client.
6. Tour page URL for the `[LINK: e-MTB tour page]` placeholder. Do not guess it.

Sameer, decision (kind: other):
7. Who films and who is on camera. If staff, a guide or a paid guest film it, the validator asks for a relationship and a disclosure beat. Decide before publishing.
8. Link placement. Reels captions do not make links clickable. "Tap the link" suits an ad or a link sticker; for an organic post, change the CTA to "link in bio".
9. Narrator: who reads it, and at what pace. A fluent speaker can use brisk. Otherwise see "Fallback cuts". If the narrator is faster than 3.0 words per second, change the brisk `pace` in `tiers.json`.

Sameer, permission and release (kind: permission, release):
10. Filming permission along the route and a written release from every identifiable rider, with separate boxes for organic posting and ads. [VERIFY with counsel: Norwegian image right and GDPR]

A guide who has led the route (kind: other):
11. One real moment from a ride on this route: something a guest said or a guide saw, in the guide's own words. The script has no concrete moment yet, and a real one can replace the mood line in beat 5. Do not write it for them.

## Read-aloud notes

- "Sognefjord" in beat 2 and the caption is a name a non-Norwegian narrator may misread. Have a Norwegian speaker say it, or give the narrator a recording of the local pronunciation.
- "singletrack only our local guides know" is a mouthful at 3.0 words per second. Leave a short breath before "singletrack" rather than speeding up.
- Beat 3 has two sentences in 6 s with no spare time. Read the first one quickly and take the breath before "The motor".
- Start the read on the first frame. The hotel line is 9 words in 3 s.

## Fallback cuts

If the read runs long with the real narrator, cut in this order. Each cut keeps all three fact rows. Cuts 1 and 2 shorten Sameer's own lines, so ask him before using them.

1. Beat 3: drop "to get here" (63 words to 60).
2. Beat 5: drop "Earn the view." (60 words to 57). It also removes the clash with "the motor takes the climbs".

- Standard narrator: cuts 1 and 2 together (57 words) were tested with the validator at est 23.8 s, PASS, with warnings T02, T04 (9 word hook) and W02 on top of the ones listed under "Accepted warnings".
- Slow narrator: the word limit is 51, so it needs a further cut to 51 words or fewer. That cut is not written yet.
- Do not fall back to the older 55 word version (commit 1c87e65). It predates the fact and visual fixes in this round, and on the strict count it runs 24.7 to 25.3 s.

## Not used from the original

Bergen arrival, the boat on the Sognefjord, "Norway's longest fjord" (a superlative needs a named source), "past every mountain you just rode", "the only sound is your tyres and the wind" (the best sensory line in the original; 13 words, so it needs a longer cut), the day count, riding days, price and departures. A short allows 3 facts per script, and F1 to F3 use them. A boat line would be a fourth fact, so it belongs in a longer cut.

## Assumptions

- Facts are the original script's claims, not sources. Every row is verified no.
- Visuals use only filming that is possible on any guided ride: a mounted camera, a camera operator standing still well back from any edge, stops on level ground. "Grinning" in beat 3 needs a rider who is actually enjoying the climb, not a staged smile. Film only what the real route shows; the shot list does not promise a glacier or a time of day.
- The fjord is in view in beats 5 and 6. That needs a spot on the route with a safe view of the fjord. The F1 row carries a VERIFY for it. If the route has no such spot, change those shots to the mountains.
- Beat 4 is a POV shot. Cut fast, ride at the guide's pace.
- "Light that doesn't want the day to end" is read as a mood line from the original, not a claim about daylight hours. See open item 4.
- The hook "Most bike trips circle back to the same hotel" and the overlay "Same hotel. Every night." are Sameer's chosen opener and a general market line. They have no fact row, because the short cap is 3 facts and F1 to F3 use them.

## Accepted warnings

- F04 on F1, F2 and F3: stays until the client confirms the rows. `--final` blocks on it by design.
- W03 on beat 2 (9 words, target 10 to 19): "This one never turns back. Voss to the Sognefjord." is Sameer's phrasing. Adding a verb would add a claim.
- H03 (no "you" in the first 3 s): the hotel line is the required opener. "You" arrives in beat 3.
- R02 on "e-MTB" in the beat 3 overlay: the original wording, kept.

## Safety line for riding shots

- A guide leads the group on every take, and every riding shot shows helmets on.
- Helmets come off only once the group has stopped, on level ground away from edges and the water.
- Nobody films while riding. Use a handlebar-mounted camera or a camera operator standing still beside the trail.
- No jumps, drops or speed shots for the camera. The group rides at the guide's pace.
- No "send it" or "no risk" wording in captions or overlays.
