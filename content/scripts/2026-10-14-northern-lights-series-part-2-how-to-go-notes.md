# Northern lights basics, part two of two: how to go (Instagram Reel): notes

Script: `content/scripts/2026-10-14-northern-lights-series-part-2-how-to-go.md`
Sibling: `content/scripts/2026-10-14-northern-lights-series-part-1-when-to-go.md` and its notes. The series-level material (ideas weighed, connection devices, general Instagram pointers, posting order, Possible Part 3) is in the Part 1 notes.

Do not post this part yet. Three things must clear first: the bio page is named and lists the tours, day 6 of the 7 day trip is confirmed, and the blog-sourced aurora timing is checked against the live post. The series name in beat 6 also needs an owner answer.

## Brief

- Platform: Instagram Reel, 9:16. Front matter `reels`. Tier short, style voiceover, creator staff, relationship staff, sound original, narrator standard. Declared 23 s (tier cap 25 s).
- Series: "Northern lights basics", part 2 of 2, "How to go". Series name: [VERIFY: series name, owner].
- Objection answered: "Do you have to stay up late to see the northern lights?"
- Takeaway: "Check the sky first; aurora is often strongest between about 20:00 and 02:00." The front matter carries this wording. It is advice drawn from the B8 window, and the owner decides whether it stays (see Open items).
- Tour: the 7 day trip (`ski-aurora-7day`) appears once, as one worked example in beat 3, with its night aurora hunt (F8). The voice calls it "the week trip". The caption names no tour, price or date. No day tour and no multi-day tour appears in the text.
- Loop: opens in beat 1 ("Do you have to stay up late?") and closes in beat 5 ("Check the sky first. Aurora is often strongest at night."). The CTA is in beat 6, from 20 s: "See the bio for details."
- Voice facts: F7 in beat 5 only, F8 in beat 3, F3 in beat 4. Beat 2 is the disclosure and cites no fact. Three distinct facts, the cap (F02).
- Facts sources: `campaigns/ski-meta-ads/tours.json` through `script_check.py --tour ski-aurora-7day`; `.claude/product-marketing.md` (do-not-claim list); the blog summary for B8 and B9 (page not fetched).
- Launch reel: `content/scripts/2026-10-14-northern-lights-launch-reel.md` and its notes are replaced by this series. The owner's round 2 feedback asks for a broader, educational series with a theme, not a launch ad. Those two files are not edited here; the main thread removes them in the same commit as this series. This part reuses none of the reel's hook, takeaway, objection, closing line, CTA or shots. Beat 1 (boots stamping snow off a wooden step) is a different shot from reel beat 2 (boots pressing into packed snow). The one shared phrase is "No tour can promise", four words from the brand rule. It is a rule, not a copied line.

## Caption

Do you have to stay up late for the northern lights? Aurora is often strongest between about 20:00 and 02:00. Check the sky first. Clear skies matter more than the calendar month, and no tour can promise a sighting. Part one covers when to go. The details are in the bio [VERIFY: owner names the page the link in bio opens]. We're Outdoor Norway. #northernlights #norway

Caption facts: F7 (the window in B8, about 20:00 to 02:00, and clear skies over the calendar month) and F3 (no promise). The caption has no price, no dates and no tour name. It has two numbers, "20:00" and "02:00", both from F7 and both flagged until F7 is verified. It has two hashtags, the validator's limit (C05). Its bio line is a VERIFY placeholder, so the final run has a BR13 line for it until the owner names the page.

## Open items

Owner (fact)
- Day 6 of the 7 day trip (F8). Beat 3 says the trip includes a night aurora hunt. tours.json day 6 says so, but the file's itinerary note says the itinerary is not yet confirmed. Not an accepted warning: the line stays out of posting until the owner confirms. [VERIFY: day 6 aurora hunt at night, owner confirms]
- Aurora timing (F7). Beat 5 and the caption rest on the blog summary (B8 and B9), not on the live page. The caption's window, about 20:00 to 02:00, is B8's wording, and the beat 5 clock shot reads 20:00. [VERIFY: B8, B9 and the 20:00 start of the window against the live post, owner confirms]
- Takeaway wording. The front matter takeaway, "Check the sky first; aurora is often strongest between about 20:00 and 02:00.", carries the B8 window, and "check the sky first" is advice, not a fact. The owner decides whether it stays as the takeaway. (kind: decision)
- Product name. tours.json names the trip "7 Day Ski in Fjord Norway & Aurora in Tromsø". The voice says "the week trip". [VERIFY: how the trip is named in public, owner confirms]
- No-promise row (F3). Recorded yes from two repo sources (see Source lines). The owner may set it to no; that adds an F04 warning on beat 4. [VERIFY: F3 wording, owner confirms]
- One trip example. Beat 3 names the 7 day trip as the one worked example, and it is the only tour named in the text. The owner decides whether a trip example stays in this part at all. (kind: decision)

Owner (permission, link)
- Bio page. "See the bio for details." and the caption's bio line need a page that lists the tours. The owner names the page and checks that it lists them before posting. [VERIFY: which page the bio link opens, owner names it]
- Bio page contents. Once the page is named, the owner says what it holds, so the CTA and the caption can say what the page holds. [VERIFY: what the bio page holds, owner confirms]

Owner (held for the bio page, not in the script)
- Price basis for "From NOK 41,181". The per-person basis is not stated anywhere. [VERIFY: confirm per person with the owner before the price goes on the bio page or in an ad]
- Day tour tense. The owner's brief quote is "we launch northern lights day tour as well". [VERIFY: owner confirms the launch and the tense]
- Multi-day tours tense. The owner's brief quote is "and multi day tours". [VERIFY: owner confirms the launch and the tense]
Held material is in its own section below. Do not write either tour as launched until the owner confirms the tense.

Editor (kind: footage)
- Real clips for every shot in the beat map. Confirm each exists in the library. No composited, generated or stock sky. [VERIFY: which clips exist in the library, editor confirms]
- The paper wall calendar and a phone clock on a snowy step are props. The calendar is filmed for beat 1 and shared with the Part 1 shoot. [VERIFY: calendar and clock prop shoot, editor confirms]
- The valley in beat 3 is not claimed as the 7 day trip's location. Do not name a place in the post. [VERIFY: editor confirms no place is named]
- Night shots (beats 1 to 6, most of them) need a guide on the shoot. See Filming safety.
- Burned-in captions from the final voiceover once the audio is recorded.

Release (kind: release)
- Beat 1 shows boots and a hand, and beat 5 shows a bare finger. No face is in shot. Each person whose hands or boots show needs a written release, with guardian consent for anyone under 18, or recorded staff consent for staff. [VERIFY with counsel: Norwegian image right and GDPR, owner confirms who checks]

Designer (kind: footage)
- The cover frame "How", the pair of Part 1's "When", and the shared series title card, inside the safe zone. [VERIFY: designer confirms the cover and the grid crop]

Music (kind: permission)
- Sound is original. If music is added, the licence has to cover business use on Instagram. [VERIFY: music licence, owner confirms]

Series (kind: decision)
- Series name, posting order, gap and a possible Part 3 are in the Part 1 notes. [VERIFY: series plan and name, owner decides]
- Marker wording. The overlay is spelled "Part two of two", not "Part 2 of 2", because digits in an overlay trip F01, F02 and F04 (see the Part 1 notes). The owner decides which form ships.

Narrator (kind: decision)
- Slow pace fails. At narrator slow the script is 47 words and estimated 23.0 s. T01 fails at 23.0 s against the 23 s maximum, and W01 fails at 47 words against the slow maximum of 47 (see Validator). Standard pace passes. The script is not cut for a slow voice in this pass. [VERIFY: narrator pace, owner decides]

## Assumptions

- Relationship staff, sound original and narrator standard, the conservative choice where nobody could be asked.
- The voice names no price, departure, date or day tour. The 7 day trip appears once, as a worked example in beat 3.
- The no-promise line in beat 4 says "No tour can promise you a sighting tonight." It names no company product, so it reads as a general caveat, not a pivot to a pitch. Beat 3 names the trip, and beat 4 follows it with the caveat.
- F3 is recorded yes, from the two repo sources. The line says no more than they do.
- The rule in beat 5 is "check the sky first", and "often strongest at night" in the voice covers the window. The caption gives the window in B8's words, about 20:00 to 02:00. The clock shot reads 20:00, the start of that window. The owner confirms the window and its start.
- Number budget: the voice and overlays carry one number, the spelled "two" in the beat 6 overlay "Part two of two". The validator counts 1, under the F03 limit of 2. The digits 20:00 and 02:00 sit in the caption and the beat 5 clock shot, not in the voice or an overlay.
- Overlays restate the voice in short form, or add a label, so a sound-off viewer gets the point. The beat 2 overlay "Staff at Outdoor Norway." names the disclosure. The beat 5 overlay "Clear skies outrank the month." gives the B9 comparison that the voice does not say. The overlay-repeat check (O03) passes.
- Beat 1 meets the hook rule: motion (boots stamp snow), an overlay ("Northern lights: stay up late?"), and "you" in the words ("Do you have to stay up late?"). It starts inside 3 s.
- The disclosure is in beat 2 at 3 s, before the 5 s limit: "I work at Outdoor Norway, and here's the answer." The beat 2 overlay names it too.
- The caption has two hashtags, the validator's limit (C05).

## Warnings and why each stays

The plain run has four warnings. None is accepted for posting.

- F04 caption "20:00" and F04 caption "02:00": the window numbers come from F7, which rests on the blog summary (B8). They stay until the owner verifies F7 against the live post. This is the accepted class (blog-sourced rows the owner checks). The voice and overlays carry no digits, so the beat 5 line is clear.
- F04 F7: the blog page was not fetched, so B8 and B9 are verified no. It stays until the owner checks both sentences against the live post. This is the accepted class.
- F04 F8: the day 6 row comes from tours.json, not the blog, and the file says the itinerary is not yet confirmed. This is outside the accepted class, so it is reported, not accepted. It stays until the owner confirms day 6.

Marking F7 or F8 yes without the owner's confirmation would invent a verification, so both rows stay no.

## Variant

- Variant: hook. "How many nights for your northern lights?" Hypothesis: it names the trip-length doubt a cold viewer already has, so it should hold beat 1 better than the stay-up-late question. Risk: it reads as the trip theme of the retired launch reel.
- Variant: CTA. "Send this to a friend." Hypothesis: a send prompt should beat "See the bio for details." on shares per view. The cost is bio taps, and the caption still points to the bio page.

## Beat map

Footage is a real clip. A title card is plain text on a night-sky frame with no logo. Hands, boots and fingers are people in shot (see Release).

1. 0 to 3 s, hook, opens loop A, no fact. Voice: "Do you have to stay up late?" Visual: boots stamp snow off a wooden step at dusk (footage, person's boots), then a hand lifts a circled page of a paper wall calendar (footage, prop and hand). Overlay: "Northern lights: stay up late?"
2. 3 to 8 s, setup and disclosure, no fact. Voice: "I work at Outdoor Norway, and here's the answer." Visual: a snowy field under a dark sky, no people (footage), then a slow tilt from the snow up to the stars (footage). Overlay: "Staff at Outdoor Norway."
3. 8 to 11.5 s, build and proof, F8. Voice: "The week trip includes a night aurora hunt." Visual: a snowy valley in daylight, no people in shot (footage), then the same valley after dark, no people in shot (footage). Overlay: "Dog sled, then an aurora hunt." No place is named.
4. 11.5 to 15 s, shift and explain, F3. Voice: "No tour can promise you a sighting tonight." Visual: a grey cloud bank rolls over a dark valley, no people (footage), then the cloud fills the frame and the stars are gone (footage). Overlay: "Sightings are not guaranteed."
5. 15 to 20 s, payoff, closes loop A, F7. Voice: "Check the sky first. Aurora is often strongest at night." Visual: a bare finger points up at a clear sky over a snowy ridge (footage, hand in shot), then a phone clock on a snowy step reads 20:00 (footage, prop). Overlay: "Clear skies outrank the month."
6. 20 to 23 s, call to action. Voice: "See the bio for details." Visual: a lantern on a snowy bench as the light fades, no people (footage), then the title card reading "Northern lights basics" [VERIFY: series name, owner] on a dark snow-field frame (title card). Overlay: "Part two of two".

Footage: beats 1 to 5, and the first shot of beat 6. Title card: the second shot of beat 6 only. Do not post until the bio page is named (see Open items).

## Timing

At 2.4 words a second, with 0.4 s for each numeric token:

- Beat 1: 7 words, 2.9 s, in 3 s.
- Beat 2: 9 words, 3.8 s, in 5 s.
- Beat 3: 8 words, 3.3 s, in 3.5 s.
- Beat 4: 8 words, 3.3 s, in 3.5 s.
- Beat 5: 10 words, 4.2 s, in 5 s. The clock shot's 20:00 is visual and adds no spoken time.
- Beat 6: 5 words, 2.1 s, in 3 s. It starts at 20 s, inside the last 4 s of the 23 s declared length, which is where the CTA must start (C02).

Total: 47 words, estimated 19.6 s. Every beat is inside the 10 percent overrun line (T04).

## Validator

Run from the repo root, in the order brief, strict, final:

- `--brief`: RESULT: PASS. 47 words, estimated 19.6 s, declared 23 s, 6 beats, 3 facts, 1 number. Four warnings: F04 caption "02:00", F04 caption "20:00", F04 F7, and F04 F8 (shown as "1 more" in brief mode).
- `--strict --brief`: RESULT: FAIL (0 blocking, 4 warnings). The same four lines.
- `--final --brief`: RESULT: FAIL (6 blocking, 0 warnings). The four F04 lines, plus BR13 for the beat 6 series name and BR13 for the caption's bio page. The BR13 lines clear when the owner names the series and the bio page.

Slow pace, tested on a scratch copy with narrator slow (not in the repo): 47 words, estimated 23.0 s. RESULT: FAIL (2 blocking, 7 warnings). T01 fails (23.0 s against the 23 s maximum) and W01 fails (47 words against the slow maximum of 47). T04 warns on beats 1, 3 and 4. The script is not cut for a slow voice in this pass.

Text check (`check_text.py repo` on the four series files): RESULT: PASS hard=0 warn=21. The warns are house words inside quoted source text, source URLs or negated rules: "guarantee" (the do-not-claim quote and the F3 row), "guaranteed" (the beat 4 overlay "Sightings are not guaranteed."), "best" (the blog URL) and "per person" (the VERIFY lines). None is HARD.

`--open-items` on this script: the bio page (caption), the series name (beat 6), and the F7 and F8 rows.

## Filming safety

Shots at dusk or after dark on snow (beats 1 to 6, most of them). Before any night shot:

- A guide is present for the whole shoot.
- Marked routes only. No off-trail walking and no unmarked ice.
- Stop when hands are numb, or when the light is too low to walk safely.
- Everyone in shot wears a headlamp and warm layers.
- Nobody is posed on a slope or on ice for a shot.
- Local rules for filming on the chosen site and any permits. [VERIFY: local rules and permits for filming on the site, owner or guide confirms]

## Held for the bio page (not in the script or caption)

These are facts the bio page may need. The voice and caption do not use them. Each one is checked before the bio page or any ad uses it.

- Price, 7 day trip (`ski-aurora-7day`): tours.json `price_nok` 41181, qualifier "from". The 7 day tour page says "From NOK 41,181"; the hub shows the bare price. The owner confirmed the price in tours.json on 6 October 2026. Verified yes for the amount; the per-person basis is not stated anywhere. [VERIFY: confirm per person with the owner before it goes on the bio page or in an ad]
- Departures 2027, from tours.json `departures`: 23 January 2027 (page: 23 Jan to 29 Jan), 30 January 2027 (30 Jan to 5 Feb), 6 February 2027 (6 Feb to 12 Feb), 13 February 2027 (13 Feb to 19 Feb), 27 February 2027 (27 Feb to 5 Mar). Verified yes against the file. Every date carries the year on the bio page.
- Day tour, owner's written brief of 14 October 2026: "we launch northern lights day tour as well". The day tour has no row in tours.json, so the brief is its only source. It gives no price, no length and no start point. [VERIFY: owner confirms the launch and the tense]. Do not write it as launched until the owner confirms the tense.
- Multi-day tours, owner's written brief of 14 October 2026: "and multi day tours". [VERIFY: owner confirms the launch and the tense]. Same rule: no "has launched" or "have launched" until the owner confirms.

The earlier fact rows F1 (day tour) and F4 (multi-day tours) were removed from the script. Their wording said "has launched" or "have launched", which the brief quotes do not say. They now live in this section with the quotes as the brief gives them.

## Round 3 changes

- The payoff is a rule: "Not necessarily. Check the sky, then look from about 20:00." The trip is one worked example in beat 3, and the trip does not appear in the payoff, the caption's rule or the takeaway.
- The F1 and F4 rows are removed from the script (see Held for the bio page).
- The overlay "Bring warm layers." is removed. It had no fact row and added a second idea.
- The dusk shot now opens the hook. The calendar moved to second.
- The no-promise line says "No tour", not "ours included", so it no longer reads as a pivot into a pitch.
- The voice says "often strongest at night", the blog's wording, not "peaks".
- The marker is spelled ("Part two of two") and the number budget is two.
- The earlier single launch reel was replaced by this series after the owner's round 2 feedback, and its files are removed in the same commit. This part does not repeat its hook, takeaway, objection, CTA or shots.
- Length 23 s and 49 words.

## Round 4 changes

- The review's blocking finding on beat 5: F7 was overstated by "Not necessarily. Check the sky, then look from about 20:00." The payoff is now "Check the sky first. Aurora is often strongest at night.", the wording F7 supports. The window stays in the caption, in B8's wording.
- The digits 20:00 and 02:00 left the voice and the overlays, so the number budget holds (F03). The caption carries them, flagged under F04 until F7 is verified.
- Beat 2 is one sentence, "I work at Outdoor Norway, and here's the answer." It cites no fact, so F7 is voiced once, in beat 5. Beat times are unchanged.
- Beat 2 overlay is "Staff at Outdoor Norway." (was "I work at Outdoor Norway.", which repeated the voice; O03).
- Beat 5 overlay is "Clear skies outrank the month." (was "Check the sky first.", which repeated the voice).
- The front matter takeaway carries the B8 window. It is advice, and the owner decides (Open items).
- The launch reel files are not edited. The main thread removes them in the same commit as this series.
- Totals: 47 words, estimated 19.6 s (was 49 words, 20.8 s). Slow scratch copy: 47 words, 23.0 s.
- Warnings: four, as before. The beat 5 "20:00" warning is gone. The caption "02:00" warning is new.

## Source lines

Read through a search summary only (blog). The page was not fetched. The quotes below are the summary's wording, not the post's text, and every blog row is verified no.

- Blog URL: https://www.outdoornorway.com/blog/best-time-to-see-northern-lights-in-norway
- B8 (summary wording, verified no): "The post cites the local tourism authority: activity is often strongest between about 20:00 and 02:00." Behind F7. The voice says "Aurora is often strongest at night", which covers the window. The caption gives the window, following B8. The owner confirms it against the live post.
- B9 (summary wording, verified no): "Clear skies and solar activity matter more than the calendar month. No timing guarantees a sighting." Behind F7: the first sentence, in the beat 5 overlay as "Clear skies outrank the month." and in the caption as "Clear skies matter more than the calendar month." The second sentence is not used in the script or the caption.
- `.claude/product-marketing.md`, do-not-claim list (verified yes, see the note below): "Any aurora sighting or guarantee. The page says no departure can guarantee one." Behind F3.
- `campaigns/ski-meta-ads/tours.json`, read only through `script_check.py --tour ski-aurora-7day`: day 6 of the itinerary, "Dog sledding, then an aurora hunting trip at night. The aurora can never be promised." Behind F8 (day 6, verified no) and F3 (days 5 and 6, the no-promise half). The file's itinerary note says the itinerary is not yet confirmed. The file was not read whole, and no person's name from it is used here.
- Owner's written brief of 14 October 2026: the two quotes in Held for the bio page. Not used in the text. Verified no.
- `.claude/skills/scriptcraft/SKILL.md`, the short voiceover template, `references/short-form.md`, `references/brand-and-claims.md`, `references/tiers.md` and `scripts/brand_rules.json`. Limits from `script_check.py --limits short voiceover`. tiers.json was not read whole and was not edited.

Note on F3 (verified yes). Both repo sources state the rule directly: the do-not-claim line says "The page says no departure can guarantee one", and tours.json says "The aurora can never be promised." The F3 row says no more than they say, and it cites no blog text. The owner may hold it at no until the live page is checked. That would add an F04 warning on beat 4 and clear nothing else.

## Instagram pointers for this part

The general pointers (format, safe zone, covers, music, caption shape, comments, grouping) are in the Part 1 notes. Only this part's points are here, each tagged.

- CTA: "See the bio for details." Do not post until the bio page is named and lists the tours. [VERIFY: which page the bio link opens, owner names it]
- Cover: the "How" frame pairs with Part 1's "When" frame. [VERIFY: designer confirms the cover and the grid crop]
- Safe zone: the overlays and the title card sit inside the safe zone. No pixel values are given here. [VERIFY: confirm current Instagram safe zone]
- Price and dates: not in this part. If the owner adds them later, use the "from" qualifier, state the per-person basis, put the year on each date, and keep them out of overlays. [VERIFY: per-person basis, owner confirms]
- Comments: do not state the day tour's price, length or start until the owner confirms them. Never answer "will we see them?" with a yes or with odds. [Rule: brand_rules.json, no guarantees on the aurora]
- Caption: it points to Part 1 ("Part one covers when to go."). Two hashtags, the validator's limit (C05).
- Order: post after Part 1, once this part is cleared. [VERIFY: series plan, owner decides]
