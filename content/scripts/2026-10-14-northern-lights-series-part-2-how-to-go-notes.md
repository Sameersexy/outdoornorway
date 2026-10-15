# Northern lights basics, part two of two: how to go (Instagram Reel): notes

Script file: `content/scripts/2026-10-14-northern-lights-series-part-2-how-to-go.md`
Sibling: `content/scripts/2026-10-14-northern-lights-series-part-1-when-to-go.md` and its notes. The series-level material (ideas weighed, connection devices, Instagram pointers, Part 3, the blog conflict) is in the Part 1 notes.

## Brief

- Platform: Instagram Reel, 9:16, front matter `reels`. Tier short, style voiceover, creator staff, relationship staff, sound original, narrator standard. Declared length 24 s (tier cap 25 s).
- Series: "Northern lights basics", part 2 of 2, "How to go".
- Takeaway: you can go on a day tour or a longer trip, so pick the length that fits your time.
- Tour: ski-aurora-7day (the 7 day trip), plus the Northern Lights day tour and other multi-day tours, which are named in the owner's brief only.
- Objection answered: do you need a full week to try for the northern lights?
- Facts source: tours.json through `script_check.py --tour ski-aurora-7day` (name, days, price, departures), `.claude/product-marketing.md` (do-not-claim list), and the owner's written brief of 14 Oct 2026 for the launches.
- Loop: opens in beat 1 (choose how you go), closes in beat 5 (pick the length that fits your time). One CTA, in the last 4 s: the link in bio.
- Shape: no itinerary and no price in the voice. The voice holds one number ("7"). Price and the 2027 departures sit in the caption only.

## Caption

How do you go for the northern lights? You can take a northern lights day tour, or go longer. The 7 day trip pairs skiing in fjord Norway with aurora in Tromsø and is from NOK 41,181. Other multi-day tours have launched too. The 2027 departures of the 7 day trip start on 23 Jan, 30 Jan, 6 Feb, 13 Feb and 27 Feb. No tour can promise the northern lights. Part one covers when to go. Details at the link in bio. We're Outdoor Norway. #northernlights #norway

## Open items

Owner (facts and decisions)
- Fact: the day tour. Price, length, start point, departure dates, inclusions and booking page are all unknown. The scripts say only that it has launched (the brief gives no more). [VERIFY: day tour facts, owner confirms]
- Fact: the other multi-day tours. Which ones are in the launch, and anything about them. The caption says only that they have launched. [VERIFY: multi-day tours in this launch, owner confirms]
- Fact: the 7 day trip. tours.json says its itinerary is not yet confirmed, so no itinerary is used. Confirm the price basis behind "from NOK 41,181" (per person is not stated) and the five 2027 departures against the hub page, which is the price source of truth. [VERIFY: price basis and departures against the hub page, owner confirms]
- Fact: naming. The tours.json name is "7 Day Ski in Fjord Norway & Aurora in Tromsø". The voice says "7 days" and "fjord skiing and aurora in Tromsø", and the caption says "the 7 day trip". Confirm how the trip and the day tour are named in public. [VERIFY: product naming, owner confirms]
- Fact: F1 and F4 quote the owner's brief of 14 Oct 2026 ("we launch northern lights day tour as well" and "and multi day tours"). The brief file is not in the repo. [VERIFY: both quotes are the owner's own words, owner confirms]
- Decision: series name, posting order and gap, and a possible Part 3. See the Part 1 notes. [VERIFY: series plan, owner decides]

Editor (footage, kind: footage)
- Real clips for every visual: a hand lifting a circled calendar page with a snowy track behind, guests with headlamps walking at dusk, a guide talking to a group on a snowy field after dark, boots on packed snow, a skier carving a turn above a fjord in daylight, a wide shot of a dark sky over a snowy landscape, cloud thickening over a dark ridge then thinning, guests looking up with breath steaming, a finger tapping calendar squares, the group laughing on snow after dark, a slow pan over a snowy ridge. No composited or generated sky. [VERIFY: which of these clips exist in the library, editor confirms]
- Day tour footage: beat 2 uses generic night-group shots because no day tour footage is known. A real day tour clip is wanted. [VERIFY: day tour footage, editor confirms]
- Fjord skiing: if no clip shows a skier above a fjord, drop "above a fjord" from the beat 3 visual. The voice line stays, because it rests on the tour name.
- Burned-in captions from the final voiceover once the audio is recorded.

Guests in shot (kind: release)
- A written release from every guest in shot, with guardian consent for anyone under 18. [VERIFY with counsel: Norwegian image right and GDPR, owner confirms who checks]

Designer (kind: footage)
- The paired cover frames ("When" in Part 1, "How" here) and the shared end card, inside the safe box.

Link and music (kind: permission)
- The bio link has to open a page that lists the tours before this part goes live. [VERIFY: which page the bio link opens, owner confirms]
- If music is added, the licence has to cover business use on Instagram. [VERIFY: music licence, owner confirms]

Voice recorder
- Standard narrator is assumed. A test copy at slow pace fails: 52 words against a maximum of 49 (W01) and T01 estimated 25.9 s against a maximum of 24. A slow voice needs a shorter cut.

## Assumptions

- Relationship staff and sound original, narrator standard, because nobody could be asked.
- The day tour has no row in tours.json. Its only source is the owner's brief, so F1 says only "has launched" and the voice calls it "a northern lights day tour" in lower case, because the public product name is not known.
- The number budget is full: "7" and the spelled "two" in "part two of two". Series line and part markers are spelled out for that reason (see the Part 1 notes on "Northern Lights 101").
- Beat 3 reads the tour name as "skiing in fjord Norway and aurora in Tromsø". An earlier wording, "skiing and aurora in Tromsø", could be read as skiing in Tromsø, so it now says "fjord skiing and aurora in Tromsø" and F2 states the pairing from the name.
- "Pick the length that fits the time you have" works because a day tour is a day and the trip is 7 days (F2). It says nothing about what the day tour includes.
- F4, F5 and F6 are used in the caption only. A row that no beat cites does not count toward the 3 fact cap, and F5 and F6 hold the caption's digits with verified rows.
- The price is "from" only. The per person basis is not stated in tours.json, so the caption does not say it.
- "No tour can promise the lights" rests on the do-not-claim list. The page FAQ line behind it was not read for this script.
- The hook "Month picked? Now choose how you go." echoes Part 1 for people who saw it. For a cold viewer the overlay "Northern lights / part two of two" names the subject.
- The caption has 2 hashtags. The brief said 1 to 3, and the validator's C05 allows at most 2.
- Part 1 mentions February and March, and the 2027 departures here start between 23 Jan and 27 Feb. The scripts do not link them.

## Accepted warnings

None. Plain, strict and final all print RESULT: PASS with no findings.

What passing does not cover: the day tour line rests on one sentence of the owner's brief, and the 7 day trip rows rest on tours.json, whose itinerary is marked not yet confirmed (not used). The hub page, the price basis and the bio link still need the owner before this goes live.

## Variant

- Hook variant: "Season set? Now choose how you go." Hypothesis: "season" is the broader word, so a cold viewer who never saw Part 1 should feel less that they missed a step, and it should hold the first 3 s better than "Month picked?". A strict run on a throwaway copy passes (52 words, estimated 22.1 s).
- CTA variant: "Send this to whoever you'd go with." Hypothesis: it should beat "Compare the tours at the link in bio." on shares and sends from viewers who travel with someone, at the cost of link taps. The caption still says "Details at the link in bio." A strict run on a throwaway copy passes (51 words, estimated 21.6 s).

## Beat map

1. 0 to 3 s, hook: "Month picked? Now choose how you go." A hand lifts a circled calendar page, a snowy track behind it, guests with headlamps walk along it. Overlay "Northern lights / part two of two". Opens loop A.
2. 3 to 7 s, setup and disclosure: "You can go on a northern lights day tour." A guide talks to a group on a snowy field after dark. Overlay "We work at Outdoor Norway" (starts before 5 s). F1.
3. 7 to 12 s, build: "Or go 7 days, with fjord skiing and aurora in Tromsø." A skier above a fjord by day, a dark sky over snow. F2.
4. 12 to 16 s, shift and explain: "Either way, no tour can promise the lights." Cloud thickens and thins over a ridge. F3.
5. 16 to 20 s, payoff: "Pick the length that fits the time you have." A finger taps a calendar square and slides along a row. Closes loop A.
6. 20 to 24 s, call to action: "Compare the tours at the link in bio." Slow pan, then the end card. Overlay "Northern lights basics".

The 3 facts in the voice are F1, F2 and F3. The 2 numbers are "7" and the spelled "two". Each beat cites at most one fact row.

## Validator (final state)

- Plain: RESULT: PASS. 52 words, estimated 22.1 s, declared 24 s, 6 beats, 3 facts, 2 numbers. 0 findings.
- Strict: RESULT: PASS. 0 findings.
- Final: RESULT: PASS. 0 findings.
- `--open-items`: 0 placeholders, 0 unverified fact rows.

## Sources

- The owner's written brief of 14 Oct 2026, quoted in F1 and F4. The brief file is not in the repo.
- `campaigns/ski-meta-ads/tours.json`, only through `script_check.py --tour ski-aurora-7day`: name, days, price with its "from" qualifier and the 2027 departure starts. The file was not read whole.
- `.claude/product-marketing.md`: the do-not-claim list behind F3.
- `.claude/skills/scriptcraft/SKILL.md`, `assets/script-template-short.md`, `references/short-form.md`, `references/brand-and-claims.md`, `references/tiers.md`, `scripts/brand_rules.json`. Limits from `script_check.py --limits short voiceover`. tiers.json was not read whole and was not edited.

## Extending to 30 to 35 s

The full test is in the Part 1 notes. In short, on a throwaway copy of the skill folder outside the repo with the cap, word and beat limits raised, a 32 s version of this part adds one beat, "Other multi day tours have launched as well." (F4), and the CTA moves to 28 to 32 s. It needs the fact cap raised to 4 as well: with the cap at 3, F02 blocks. With the fact cap at 4 the result is RESULT: PASS in plain and strict (60 words, estimated 25.4 s, 7 beats, 4 facts, 2 numbers). Tiers.json was not changed.

## Instagram pointers for this part

The general pointers (format, safe box, covers, music, caption shape, comments) are in the Part 1 notes. Only this part's points are here. Each feature claim is tagged.

- The CTA says "link in bio", so the bio link has to point at the tours before posting. [VERIFY: confirm current feature set for Instagram, and which page the bio link opens, owner confirms]
- Price and dates are in the caption only, with the "from" qualifier and the year on the dates. Do not add them to the overlay.
- In comments, do not state the day tour's price, length or start until the owner has confirmed them, and never answer "will we see them?" with a yes or with odds.
