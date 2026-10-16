# Northern lights basics, part two of two: how to go (Instagram Reel): notes

Script file: `content/scripts/2026-10-14-northern-lights-series-part-2-how-to-go.md`
Sibling: `content/scripts/2026-10-14-northern-lights-series-part-1-when-to-go.md` and its notes. The series-level material (ideas weighed, connection devices, Instagram pointers, Possible Part 3, blog conflict on months) is in the Part 1 notes.

Launch reel retired: `content/scripts/2026-10-14-northern-lights-launch-reel.md` and its notes are retired on the owner's instruction. They are not edited here; the main thread removes them. This part reuses none of the reel's takeaway, objection, closing line or shots. Two near overlaps were reworded: the no-promise wording and the pointer to the bio. R04 compares only against examples and assets, so this was checked by hand.

Do not post this part yet. "See the details in the bio." needs the page the bio link opens to list the tours, and the owner has not named that page (see Open items).

## Brief

- Platform: Instagram Reel, 9:16, front matter `reels`. Tier short, style voiceover, creator staff, relationship staff, sound original, narrator standard. Declared 23 s (tier cap 25 s).
- Series: "Northern lights basics", part 2 of 2, "How to go".
- Objection answered: do you have to stay up late to see the northern lights?
- Takeaway: choose how you go by the evenings you can spare.
- Tour: the 7 day trip (`ski-aurora-7day`) is named once, in the beat 4 voice, with its aurora hunt at night (F8). The caption names no tour, price or date. No day tour or multi-day tour appears in the text.
- Loop: opens in beat 1 ("Do you have to stay up late?"), closes in beat 5 ("Pick your trip by evenings you can spare."). One CTA, in the last 4 s (from 19 s): "See the details in the bio."
- Voice facts: F7 (beat 2), F3 (beat 3), F8 (beat 4). Three, the cap. F1, F4, F5 and F6 are not used in the text. They stay in the facts table for the bio page and do not block this part.
- Facts sources: `campaigns/ski-meta-ads/tours.json` through `script_check.py --tour ski-aurora-7day`; `.claude/product-marketing.md` (do-not-claim list); the blog summary for B8 (page not fetched); the owner's written brief of 14 Oct 2026 for F1 and F4 (not used in the text).

## Caption

How do you go for the northern lights? Pick the trip that fits the evenings you have. Aurora often peaks at night, and no departure can promise a sighting, ours included. Part one covers when to go. We're Outdoor Norway. #northernlights #norway

Caption facts: F7 (aurora often peaks at night) and F3 (no promise). The caption has no digits, no price, no dates, no tour name and no VERIFY placeholder, so the final run has no BR13 line.

## Open items

Owner (fact)
- Aurora timing (F7). The wording "aurora often peaks at night" paraphrases B8 from the blog summary. Owner checks it against the live post. [VERIFY: B8 paraphrase against the live post, owner confirms]
- Day 6 of the 7 day trip (F8). The beat 4 voice says the trip includes a night aurora hunt, which is day 6 in tours.json. The itinerary note says it is not yet confirmed. Owner confirms before the line is posted. [VERIFY: day 6 aurora hunt at night, owner confirms]
- Product naming. tours.json names the trip "7 Day Ski in Fjord Norway & Aurora in Tromsø". The voice says "the 7 day trip". Owner confirms how the trip is named in public. [VERIFY: product naming, owner confirms]
- Payoff line (kind: decision). "Pick your trip by evenings you can spare." is advice, not a fact. Owner decides whether it stays.

Owner (permission, link)
- Bio page. "See the details in the bio." needs a page that lists the tours. Owner names the page; it is checked before posting. [VERIFY: which page the bio link opens, owner names it]

Editor (kind: footage)
- Real clips for each shot in the beat map. Confirm each exists in the library. No composited or generated sky. [VERIFY: which clips exist in the library, editor confirms]
- The paper wall calendar prop has to be filmed for beats 1 and 5. [VERIFY: calendar prop shoot, editor confirms]
- The valley in beat 4 is not claimed as the 7 day trip's location. Do not add a place name. [VERIFY: editor confirms no place is named in the post]
- Night shots (beats 2, 4 and 6) need a guide on the shoot. See Filming safety.
- Burned-in captions from the final voiceover once the audio is recorded.

Release (kind: release)
- Beat 1 shows a hand and boots, and beat 5 shows a finger. No face is in shot. Each person whose hands or boots show needs a written release, with guardian consent for anyone under 18, or staff consent recorded for staff. [VERIFY with counsel: Norwegian image right and GDPR, owner confirms who checks]

Designer (kind: footage)
- The cover frame "How" (the pair of Part 1's "When") and the shared series title card, inside the safe box. [VERIFY: designer confirms the cover and the grid crop]

Music (kind: permission)
- Sound is original. If music is added, the licence has to cover business use on Instagram. [VERIFY: music licence, owner confirms]

Series (kind: decision)
- Series name, posting order, gap and a possible Part 3 are in the Part 1 notes. [VERIFY: series plan, owner decides]

## Assumptions

- Relationship staff, sound original and narrator standard, because nobody could be asked.
- The voice names no price, date, departure or day tour. The 7 day trip is named once, in beat 4, and its aurora hunt is the worked example.
- F3 is verified yes. Its no-promise half rests on the do-not-claim list in `.claude/product-marketing.md` ("The page says no departure can guarantee one.") and on tours.json, days 5 and 6 ("The aurora can never be promised."). The line "no departure can promise a sighting" says no more than those rows.
- "Ours included" in beat 3 applies the same rule to Outdoor Norway's own departures.
- The number budget is full: the digit "7" in beat 4 and the spelled "two" in the beat 6 overlay. The validator counts 2 numbers.
- The caption has 2 hashtags, the validator's limit (C05).
- Overlays in beats 1, 2, 4 and 5 restate the voice in short form, so a sound-off viewer gets the point. The owner can cut the repeat if a sound-off check shows it is not needed.
- Narrator: standard. Tested this round on a throwaway copy with narrator slow: 48 words, estimated 23.9 s (T01 fails at 23 s), and W01 sets the slow maximum at 47 words. A slow voice needs 47 words or fewer; the script is not changed for it.

## Accepted warnings

Plain run: RESULT: PASS with three F04 warnings. None is accepted for posting. Each stays until the owner confirms the row it cites.
- F04 beat 4: number only in an unverified fact row, "7 day trip". The digit sits in beat 4 with F8. It clears when F8 is verified yes.
- F04 fact used but not verified yes: F7 (aurora often peaks at night). Stays until the owner checks the B8 paraphrase against the live post.
- F04 fact used but not verified yes: F8 (day 6 aurora hunt at night). Stays until the owner confirms day 6.

Strict run: RESULT: FAIL (0 blocking, 3 warnings). The same three F04 lines.

Final run: RESULT: FAIL (3 blocking). The same three F04 lines. No BR13 line, because the script has no VERIFY placeholder in its text.

Marking F7 or F8 yes without the owner's confirmation would invent a verification, so both rows stay no.

## Variant

- Variant: hook. "How many nights for your northern lights?" Hypothesis: it names the trip-length doubt a cold viewer already has, so it should hold beat 1 better than the stay-up-late question. Risk: it reads as the full-week theme of the retired launch reel, and a viewer may hear length rather than evenings.
- Variant: CTA. "Send this to a friend." Hypothesis: a send prompt to a friend who travels should beat "See the details in the bio." on shares per view. The cost is bio taps, and the caption still points to the bio page.

## Beat map

Footage means a real clip. A title card is plain text on a night-sky frame with no logo. Hands and boots are people in shot (see Release).

1. 0 to 3 s, hook, opens loop A. Voice: "Do you have to stay up late?" Visual: a hand lifts a circled page of a paper wall calendar (footage, prop and hand), then boots stamp snow off a wooden step at dusk (footage). Overlay: "Stay up late?"
2. 3 to 7 s, setup and disclosure, F7. Voice: "I work at Outdoor Norway. Aurora often peaks at night." Visual: a snowy field under a dark sky, no people (footage), then a slow tilt from the snow up to the stars (footage). Overlay: "I work at Outdoor Norway."
3. 7 to 11 s, shift and explain, F3. Voice: "No departure can promise a sighting, ours included." Visual: thin cloud moves over a dark ridge (footage, no people), then the cloud thins and stars show above the snow (footage). Overlay: "Bring warm layers."
4. 11 to 15 s, build, F8. Voice: "The 7 day trip includes a night aurora hunt." Visual: a wide shot of a snowy valley in daylight (footage, no place named), then a headlamp beam crosses a field at night, no people in shot (footage). Overlay: "An aurora hunt at night."
5. 15 to 19 s, payoff, closes loop A. Voice: "Pick your trip by evenings you can spare." Visual: a finger taps one square on a paper wall calendar (footage, prop and hand), then the finger slides along one full row (footage). Overlay: "Start with your evenings."
6. 19 to 23 s, call to action. Voice: "See the details in the bio." Visual: a lantern on a snowy bench as the light fades, no people (footage), then the series title card, the same as Part 1 (title card on a night-sky frame). Overlay: "This is part two."

Footage: beats 1 to 5 and the first shot of beat 6. Title card: the second shot of beat 6 only. Do not post until the bio page is named (see Open items).

## Timing

- Beat 4 needs 4.15 s of speech (9 words at 2.4 words a second, plus 0.4 s for the digit "7") in a 4 s slot. That is 4 percent over, inside the 10 percent T04 line. Beat 5 is 8 words in 4 s. Beat 6 starts at 19 s, inside the last 4 s of the 23 s declared length, which is where the CTA must start (C02).

## Validator (final state)

- Plain: RESULT: PASS. 48 words, estimated 20.4 s, declared 23 s, 6 beats, 3 facts, 2 numbers. Three F04 warnings (beat 4 "7", F7, F8).
- Strict: RESULT: FAIL (0 blocking, 3 warnings). The same three F04 lines.
- Final: RESULT: FAIL (3 blocking). The same three F04 lines. No BR13 line.
- `--open-items`: 4 placeholders (VERIFY in F1, F4, F7, F8 rows). F1 and F4 are not used in the text, so they do not block this part.

## Filming safety

Shots at dusk or at night on snow (beats 1, 2, 4 and 6). Before any night shot:
- A guide is present for the whole shoot.
- Marked routes only. No off-trail walking and no unmarked ice.
- Stop when hands are numb, or when the light is too low to walk safely.
- Everyone in shot wears a headlamp and warm layers.
- Nobody is posed on a slope or on ice for a shot.
- Local rules for filming on the chosen site and any permits. [VERIFY: local rules and permits for filming on the site, owner or guide confirms]

## Design changes in round 2

- The launch reel is retired. This part no longer repeats its takeaway, objection, closing line or shots.
- The hook asks the stay-up-late question. The earlier hook "How many nights for your northern lights?" is the variant.
- The caption no longer names the day tour, the multi-day tours, the price, the 2027 dates or the tour. The three caption placeholders from round 1 are gone, and so is the BR13 failure.
- The CTA is "See the details in the bio." (round 1 "Tap the link in bio.").
- The aurora hunt is tied to day 6 only (F8). Round 1 also cited day 5.
- The shot of a night sky over a field and the dolly shot in beat 6 were reworded: the first restated the retired reel's sky shot, and the second restated its pan.
- Length 23 s and 48 words, down from 49.

## Source lines

Read through a search summary only (blog). The page was not fetched. The quotes below are the summary's wording, not the post's text, and every blog row is verified no.
- Blog URL: https://www.outdoornorway.com/blog/best-time-to-see-northern-lights-in-norway
- B8 (summary wording): "The post cites the local tourism authority: activity is often strongest between about 20:00 and 02:00." Behind F7, paraphrased in the voice as "Aurora often peaks at night."
- `.claude/product-marketing.md`, do-not-claim list: "Any aurora sighting or guarantee. The page says no departure can guarantee one." Behind F3.
- `campaigns/ski-meta-ads/tours.json`, only through `script_check.py --tour ski-aurora-7day`: name, days, price (F5), departure starts (F6), and day 6 of the itinerary (F8). Its aurora line for days 5 and 6: "The aurora can never be promised." Behind F3. The itinerary is marked not yet confirmed. The file was not read whole.
- Owner's written brief of 14 Oct 2026, quoted in F1 and F4: "we launch northern lights day tour as well" and "and multi day tours". Not used in the text.
- `.claude/skills/scriptcraft/SKILL.md`, the short voiceover template, `references/short-form.md`, `references/brand-and-claims.md`, `references/tiers.md`, `scripts/brand_rules.json`. Limits from `script_check.py --limits short voiceover`. tiers.json was not read whole and was not edited.

## Instagram pointers for this part

The general pointers (format, safe box, covers, music, caption shape, comments, grouping) are in the Part 1 notes. Only this part's points are here.
- The CTA says "See the details in the bio." Do not post until the bio page is named and lists the tours. [VERIFY: which page the bio link opens, owner names it]
- Price and dates are not in this part. If the owner adds them later, use the "from" qualifier and the year on the dates, and keep them out of overlays.
- In comments, do not state the day tour's price, length or start until the owner has confirmed them. Never answer "will we see them?" with a yes or with odds.
