# Fact-Check Report: itinerary download sequences (7-Day Bergen to Tromsø and 6-Day Alta)

Checked on 26 October 2026 against the live pages fetched that day, `campaigns/ski-meta-ads/tours.json` and the terms, flexible booking, insurance, tailor-made and team pages. Method: every checkable claim in the two sequence files was listed, matched against a named source with a text search of the fetched page, and given a level on the 6-level scale in `.claude/skills/fact-check/SKILL.md`. Opinions, mood lines and the sender's offers to help were not scored.

Source keys used below (URLs in the README sources table):

| Key | Source |
|---|---|
| T7 | 7-Day tour page |
| TA | 6-Day Alta tour page |
| TJ | `campaigns/ski-meta-ads/tours.json`, entry `ski-aurora-7day` |
| HUB | Northern lights hub page (not linked from the emails) |
| SG | Season guide blog |
| TB | Tromsø aurora guide blog |
| AB | Alta aurora guide blog |
| WB | Where to see the lights blog |
| CB | Can you see the lights in Norway blog |
| VB | Skiing in Voss blog |
| SB | Snowshoeing for beginners blog |
| BB | Bergen in winter blog |
| PF | 7-Day packing FAQ page |
| FB | Flexible booking page |
| TC | Terms and conditions page |
| TI | Travel insurance page |
| TM | Tailor-made trips page |
| TE | Our team page |

## Summary

- Claims checked: 96
- Verified (levels 1 to 2): 84
- Unverified (level 3, marked `[CONFIRM ...]` in the drafts): 9
- Disputed (level 4, marked `[CONFIRM ...]` in the drafts): 3
- Corrected: 12 (unverified detail removed or wording aligned with the page)
- Wrong (fixed): 0
- Confidence: MEDIUM

Every price and every date is at level 1. The gate passes at MEDIUM. The drafts still cannot be sent with a `[CONFIRM ...]` marker in place; the twelve markers are the nine level 3 and three level 4 items below, and each maps to a numbered decision in the README.

## Corrections applied

1. 7-Day Email 2 said January brings "the longest nights of the trip's season in Tromsø and the shortest days in Voss". No page ranks the weeks. Now "long nights in Tromsø and short days in Voss". Source: SG ("December and January bring exceptionally long Arctic nights").
2. 7-Day Email 3 said you "learn them on the trail" about snowshoe techniques. SB does not say that. Now "needs only a few easy techniques before your first trail". Source: SB.
3. 7-Day Email 3 said "a detailed packing list before the trip". Now "a full packing list before you arrive", the T7 FAQ wording. Source: T7.
4. 7-Day Email 4 Facts line credited Bergen's seven mountains to BB. BB does not mention them. Now credited to the T7 Day 1 heading "A stroll between the seven mountains". Source: T7.
5. 7-Day Email 5 exclusion "lunches, drinks and snacks" is now "lunches, beverages and snacks", the T7 Not Included wording. Source: T7.
6. Alta Email 2 said "November and December sit around the darkest weeks of the year". SG names December and January as the longest nights and says November takes you "much further into the Arctic winter". Now "November takes you well into the Arctic winter. December and January bring the longest nights". Source: SG.
7. Alta Email 2 Facts line now names the SG month lines it rests on.
8. Alta Email 3 said "through the forests around Gargia". TA says "through Gargia Valley". Now "through Gargia Valley", and the Facts line no longer credits "forests surrounding Gargia" to AB. Source: TA.
9. Alta Email 4 said Day 2 has no aurora activity "on purpose, so you have one early night". The purpose is not on the page. Now "Day 2 has no aurora activity in the plan". Source: TA Day 2 block.
10. Alta Email 5 said Gargia Lodge has "a sauna and a fireside lounge". TA says "sauna and evening by the fire". Now "a sauna and evenings by the fire", in the body and the Facts line. Source: TA.
11. Alta Email 5 inclusion "selected warm drinks and snacks" is now "selected warm beverages and snacks during the activities", the TA Included wording. Source: TA.
12. Both Email 6 reply buttons use `mailto:[REPLY ADDRESS]` instead of an address, because the repo integrity test rejects any email address in a tracked file. Source: `tools/test_repo_integrity.py`.

## Needs the client's input

- Deposit amount and balance due date (both Email 5). No page states either. Question: what is the deposit, and when is the balance due?
- Cancellation terms (both Email 5 and Email 7). T7, TA and TC agree on the 60, 45 to 59, 30 to 44 and under 30 day scale. FB promises a 14-day 100 percent refund window after the deposit and a Lifetime Deposit. Question: which policy applies to these two tours, and should the emails state both?
- What the date request does (both Email 7). The emails say sending the request is a question, not a booking. Question: does the form create a booking, a hold, or an inquiry?
- Reply time and calls (both Email 6). Question: can Mate promise a reply within one working day, and is a call offered?
- Sender identity (every email). TE does not list anyone called Mate. Question: keep the name, or sign with a listed team member?
- Alta aurora season (Alta Email 2). TA gives the season as November to April. AB gives the aurora season as September to late March. SG says early April is possible where nights stay dark. Question: should April be offered as an aurora month?
- Whale cruise months (Alta Email 3). TA does not say which months the cruise runs. Question: does Day 2 run in every month of the season, and what replaces it when it does not?
- Single travellers (both Email 7). T7 says twin-share. Neither page mentions a single supplement or a solo option. Question: can a single traveller book, and at what price?
- Tripadvisor review count (both Email 5). Both tour pages show a 4.9/5 badge with the Tripadvisor logo but no review count. Question: how many reviews, so the line can carry the number?
- Alta is not in `tours.json`, so `verify_tours.py` does not re-check the Alta price. Suggestion: add an Alta entry so the next check covers it.

## Claim by claim

### 7-Day Email 2, day 2

[1] CLAIM: Five 2027 departures: 23 to 29 January, 30 January to 5 February, 6 to 12 February, 13 to 19 February, 27 February to 5 March.
    SLOT: body
    STATUS: 1 VERIFIED
    SOURCE: TJ departures; T7 "23 Jan | 30 Jan | 06 Feb | 13 Feb | 27 Feb"
    NOTES: Each pair spans 7 calendar days inclusive. All dates are in the future.

[2] CLAIM: January is deep winter, with long nights in Tromsø and short days in Voss.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: SG "December and January bring exceptionally long Arctic nights"
    NOTES: Corrected, see correction 1.

[3] CLAIM: By February the days are noticeably longer than around the December solstice.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: BB, line "By February, the days are already noticeably longer than around the December solstice"
    NOTES: Bergen blog; applied to Voss, 1 hour by train from Bergen.

[4] CLAIM: Visit Norway notes that spring statistically sees high levels of aurora activity.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: SG "Official tourism information also identifies the spring period around March/April ... as statistically associated with higher Aurora activity"
    NOTES: SG attributes the note to official tourism information and names Visit Norway elsewhere on the page.

[5] CLAIM: The season guide says February and March would be hard to beat.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: SG
    NOTES: Quoted wording confirmed in the fetched text.

[6] CLAIM: The plan is a day in Bergen, the train to Voss (about an hour), a snowshoe day and a ski day, the flight to Tromsø, three evenings of aurora activity.
    SLOT: body
    STATUS: 1 VERIFIED
    SOURCE: TJ itinerary; T7 day headings
    NOTES: TJ Day 2 "Morning train from Bergen to Voss (about an hour)".

### 7-Day Email 3, day 5

[7] CLAIM: Grade easy to intermediate; good general physical condition required.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: T7 "Easy to intermediate", "physical condition"

[8] CLAIM: Snowshoeing needs only a few easy techniques before your first trail and is low-impact exercise.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: SB "requires a few easy techniques before you can hit your first trail", "low-impact exercise"
    NOTES: Corrected, see correction 2.

[9] CLAIM: No previous skiing experience is required.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: T7 "You don't need previous skiing experience"

[10] CLAIM: A 1-day ski pass at Voss Resort is included.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: T7 Included list "1-day ski pass at Voss Resort"

[11] CLAIM: Voss Resort has green slopes for first-timers.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: VB "green slopes for kids and first-timers"

[12] CLAIM: Ski equipment is not included; rentals can be arranged.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: T7 Not Included "Ski equipment - rentals are available and can be arranged"
    NOTES: T7 also carries the summary line "All equipment + guide + transfers + stay", which contradicts its own list. The email follows the list. Decision 9 in the README.

[13] CLAIM: Day 5 is a fjord trip by private boat with lunch; Day 6 is dog sledding.
    SLOT: body
    STATUS: 1 VERIFIED
    SOURCE: TJ Day 5 and Day 6; T7 "onboard chef crafts a delicious lunch"

[14] CLAIM: A guide is with you throughout; every transfer inside Norway and the flight from Bergen to Tromsø are included.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: T7 Included "Professional guide throughout the trip", "All transportation during the trip in Norway", "Flight from Bergen to Tromsø"

[15] CLAIM: A full packing list is sent before you arrive.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: T7 FAQ "we will send you a full packing list before you arrive"
    NOTES: Corrected, see correction 3. PF is the linked page.

[16] CLAIM: The Alta trip has your own dog team and a snowmobile day.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA Included "Drive-your-own-team husky experience", "4-hour snowmobile adventure across Finnmarksvidda"

### 7-Day Email 4, day 9

[17] CLAIM: No departure can guarantee an appearance of the lights.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: T7 "no departure can guarantee an appearance"

[18] CLAIM: Day 4 is a guided aurora safari on arrival; Day 5 ends with aurora observation at the hotel camp; Day 6 is a night-time aurora hunt after dog sledding.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TJ Day 4, Day 5, Day 6
    NOTES: TJ is the repo's source of truth for day plans.

[19] CLAIM: "Think in nights, not hours."
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: CB

[20] CLAIM: The guide checks forecasts, cloud cover and road conditions and sometimes drives a long way to find a gap in the clouds.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TB "forecasts", "cloud cover", "road conditions", "much farther from the city"

[21] CLAIM: Tromsø sits at about 69 degrees north.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: SG "69 degrees north"

[22] CLAIM: Tromsø lies directly beneath the auroral oval and is one of the world's most established places to see the lights.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: WB "destinations beneath the auroral oval", "Tromsø is one of the world's most established Northern Lights destinations"

[23] CLAIM: Activity is often strongest between 20:00 and 02:00.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: SG

[24] CLAIM: Displays can appear suddenly, disappear and return later; the night is not over at 9 pm.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TB

[25] CLAIM: Bergen's seven mountains on Day 1.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: T7 Day 1 heading "A stroll between the seven mountains | Bergen"
    NOTES: Corrected source, see correction 4.

### 7-Day Email 5, day 13

[26] CLAIM: From NOK 41,181, including all taxes, twin-share.
    SLOT: body (price)
    STATUS: 1 VERIFIED
    SOURCE: TJ price_nok 41181, price_qualifier "from"; T7 "From NOK 41,181", "all taxes"; HUB "NOK 41,181"
    NOTES: No page states per person. The email does not say per person, in line with the product-marketing do-not-claim list.

[27] CLAIM: Included: professional guide throughout; all transport in Norway including the flight; 1-day ski pass at Voss Resort; 6 nights of twin-share accommodation in classic hotels in Voss and Tromsø; 6 breakfasts and 5 dinners; guided winter experiences and Northern Lights activities.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: T7 Included list, verbatim; "Cozy, classic hotels in Voss & Tromsø with twin-share rooming"

[28] CLAIM: Not included: flights to and from Norway; ski equipment; lunches, beverages and snacks; travel insurance; personal expenses.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: T7 Not Included list, verbatim
    NOTES: Corrected wording, see correction 5.

[29] CLAIM: You fly into Bergen and home from Tromsø.
    SLOT: body
    STATUS: 1 VERIFIED
    SOURCE: TJ Day 1 and Day 7; T7 "pick you up at Bergen Flesland International Airport on Day 1 and drop you off at Tromsø Airport on Day 7"

[30] CLAIM: Send your preferred week through the tour page and we confirm availability.
    SLOT: body
    STATUS: 3 UNVERIFIED
    SOURCE: none
    NOTES: Marked `[CONFIRM]`. Decision 3.

[31] CLAIM: Deposit amount and balance due date.
    SLOT: body
    STATUS: 3 UNVERIFIED
    SOURCE: none; TC says payment is due before departure but gives no amount or date
    NOTES: Left as a `[CONFIRM]` marker. Decision 2.

[32] CLAIM: Cancel 60 days or more before departure for a full refund; 45 to 59 days, 75 percent; 30 to 44 days, 50 percent; under 30 days, no refund; card fees not refundable.
    SLOT: body
    STATUS: 1 VERIFIED
    SOURCE: T7 Cancellation Policy; TC cancellation bullets

[33] CLAIM: The flexible booking page promises a 14-day risk-free window and a lifetime deposit.
    SLOT: body (marker only)
    STATUS: 4 DISPUTED
    SOURCE: FB versus T7 and TC
    NOTES: Marked `[CONFIRM]`. Decision 1. Not stated to the reader until resolved.

[34] CLAIM: We recommend comprehensive health and accident insurance from your home country; the trip does not insure you.
    SLOT: body
    STATUS: 1 VERIFIED
    SOURCE: TC "highly advise ... travel insurance policy in your home country", "The organiser does not insure the participants"; TI "comprehensive health and accident"

[35] CLAIM: Guests rate the trip 4.9/5 on Tripadvisor.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: T7 badge "4.9/5 RATING" with the Tripadvisor logo in the page HTML
    NOTES: No review count on the page. The product-marketing rule asks for a named source and a number; the source is named and the rating is the number. Ask for the count.

### 7-Day Email 6, day 18

[36] CLAIM: You fly into Bergen and home from Tromsø.
    SLOT: body
    STATUS: 1 VERIFIED
    SOURCE: as [29]

[37] CLAIM: Reply time and whether a call is offered.
    SLOT: body
    STATUS: 3 UNVERIFIED
    SOURCE: none
    NOTES: Marked `[CONFIRM]`. Decision 4.

[38] CLAIM: Sender "Mate" at Outdoor Norway.
    SLOT: signature
    STATUS: 3 UNVERIFIED
    SOURCE: TE lists no Mate
    NOTES: Kept from the current sequence. Decision 4. Counted once for both tours.

### 7-Day Email 7, day 25

[39] CLAIM: Departures 23 January, 30 January, 6 February, 13 February and 27 February 2027, each 7 days.
    SLOT: body
    STATUS: 1 VERIFIED
    SOURCE: as [1]

[40] CLAIM: Rooms are twin-share.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: T7 "6 nights of twin-share accommodation"

[41] CLAIM: Single traveller option.
    SLOT: body
    STATUS: 3 UNVERIFIED
    SOURCE: none
    NOTES: Marked `[CONFIRM]`. Decision 7.

[42] CLAIM: The Alta trip is six days in one Arctic base with your own dog team, a snowmobile day and a whale cruise.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA Included list

[43] CLAIM: Full refund up to 60 days before departure.
    SLOT: body
    STATUS: 1 VERIFIED
    SOURCE: as [32]
    NOTES: Carries the Decision 1 marker because of [33].

[44] CLAIM: 60 days before 23 January 2027 is 24 November 2026; 60 days before 27 February 2027 is 29 December 2026.
    SLOT: body (dates)
    STATUS: 1 VERIFIED
    SOURCE: arithmetic from [1]; checked with Python date subtraction
    NOTES: The other three cut-offs, for the README: 1 December, 8 December and 15 December 2026.

[45] CLAIM: Sending the request is a question, not a booking.
    SLOT: body
    STATUS: 3 UNVERIFIED
    SOURCE: none
    NOTES: Marked `[CONFIRM]`. Decision 3.

### 7-Day Email 8, day 40

[46] CLAIM: We also build trips to your own dates.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TM "customized Norway private tours built around your goals, dates, and fitness level"

### 6-Day Alta Email 2, day 2

[47] CLAIM: Dates are flexible and available on request for 2026 and 2027, November to April.
    SLOT: body (dates)
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA "2026 and 2027 Flexible dates available", "Season November - April"

[48] CLAIM: November takes you well into the Arctic winter; December and January bring the longest nights.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: SG "November takes you much further into the Arctic winter", "December and January bring exceptionally long Arctic nights", "For the longest periods of darkness consider December and January"
    NOTES: Corrected, see correction 6.

[49] CLAIM: By February the days are noticeably longer than around the December solstice.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: BB, as [3]

[50] CLAIM: March is another strong month; Visit Norway notes spring activity.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: SG "another strong contender", and as [4]

[51] CLAIM: In April the dark window shrinks.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: SG "Potentially, particularly in early April and at destinations where sufficiently dark nights remain"

[52] CLAIM: April is an aurora month for this trip.
    SLOT: body (marker)
    STATUS: 4 DISPUTED
    SOURCE: TA season November to April; AB season September to late March
    NOTES: Marked `[CONFIRM]`. Decision 5.

[53] CLAIM: No single month is guaranteed to be better than another.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: AB "there isn't one guaranteed best month"

[54] CLAIM: Our Alta guide says not to build the whole trip around one night.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: AB "we wouldn't build an entire trip around a single night"

### 6-Day Alta Email 3, day 5

[55] CLAIM: Grade easy to medium; comfortable outdoors in winter and moderately active.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA "Easy to Medium", "comfortable spending time outdoors in winter conditions and taking part in moderately active experiences"

[56] CLAIM: Day 2 fjord and whale cruise, 4 hours, warm drinks and snacks on board.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA "four-hour journey in search of whales. Warm beverages and snacks are included"

[57] CLAIM: Which months the cruise runs.
    SLOT: body (marker)
    STATUS: 3 UNVERIFIED
    SOURCE: none
    NOTES: Marked `[CONFIRM]`. Decision 6.

[58] CLAIM: Day 3 dog sledding, 4 hours, your own team, through Gargia Valley, with lunch; then Gargia Lodge and the sauna.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA "four-hour dogsledding experience", "drive your own dog team", "with lunch", "Dogsledding in Gargia Valley", "settle into Gargia Lodge", "time at the sauna"
    NOTES: Corrected, see correction 8.

[59] CLAIM: Day 4 snowmobile, 4 hours across Finnmarksvidda, driving in pairs.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA "4-hour snowmobile adventure across Finnmarksvidda"; pairs line confirmed in the fetched text

[60] CLAIM: Some activities have age, licence or participation requirements, confirmed before departure.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA "Some individual activities may have their own age, licence or participation requirements. Full requirements will be confirmed before departure."
    NOTES: No age number is given, in line with the do-not-claim list.

[61] CLAIM: Day 5 free morning; optional 5-hour snowshoe to a frozen waterfall, not included.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA Day 5 block; Not Included "Optional Snowshoe Adventure to the Frozen Waterfall"

[62] CLAIM: Free time on Days 1, 2, 4 and 5.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA day blocks (free afternoon Day 1, free morning Day 2, free afternoon Day 4, free morning Day 5)

[63] CLAIM: Specialist equipment and safety gear provided where applicable.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA Included "Specialist equipment and safety gear for included guided activities, where applicable"
    NOTES: TA also shows an "All Gear Included" badge, which contradicts its own list. The email follows the list.

[64] CLAIM: Pack warm layers, a waterproof outer layer and winter footwear.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA packing section "packing warm layers", "Waterproof or weather-resistant outer layers", "Sturdy winter footwear"

[65] CLAIM: Dress for standing still, not just for the temperature on your weather app.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: AB "Dress for standing still, not just for the temperature shown on your weather app"

[66] CLAIM: A good trip for a first visit to Northern Norway.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA "a great fit if this is your first trip to Northern Norway"

[67] CLAIM: The 7-Day trip has fjords and a ski day before the Arctic.
    SLOT: body
    STATUS: 1 VERIFIED
    SOURCE: TJ itinerary; T7 day headings

### 6-Day Alta Email 4, day 9

[68] CLAIM: Sightings can never be guaranteed.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA "sightings can never be guaranteed"

[69] CLAIM: Day 1 welcome dinner at Raus Social, then a possible first sighting on the first night.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA "Raus Social", "from your very first night in the north ... the possibility of seeing the Northern Lights"

[70] CLAIM: Day 3 evening by the fire at Gargia Lodge, watching the sky.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA Day 3 "evening by the fire", "keep an eye on the sky"

[71] CLAIM: Day 4 kennel of about 40 huskies, a warm Arctic dinner, viewing away from light pollution.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA "40-dog husky kennel", "warm Arctic dinner", "away from light pollution"

[72] CLAIM: Day 5 a final chance after the farewell dinner.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA Day 5 "last chance"

[73] CLAIM: Day 2 has no aurora activity in the plan.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA Day 2 block lists the cruise and a free morning only
    NOTES: Corrected, see correction 9.

[74] CLAIM: Alta sits at about 70 degrees north and combines long, dark winter nights with quick access to Finnmarksvidda.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: AB "70° north", "long dark winter nights with quick access to Finnmarksvidda"

[75] CLAIM: The plateau gives you something you will not find at a city viewpoint.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: AB city viewpoint line

[76] CLAIM: On one night Alta could be clear while Tromsø is cloudy, and the other way round.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: WB "On one particular night, Alta could be clear while Tromsø is cloudy"

[77] CLAIM: Clouds can obscure an otherwise active aurora.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: AB

[78] CLAIM: Viewing is most often reported between about 6 pm and 1 am.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: AB "6 pm and 1 am"

[79] CLAIM: A Northern Lights snowmobile trip is a snowmobile adventure first and an aurora experience second.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: AB

[80] CLAIM: The rest of the trip goes ahead whatever the sky does.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA "The rest of the trip continues regardless of Aurora conditions"

### 6-Day Alta Email 5, day 13

[81] CLAIM: NOK 31,000, including all taxes, for 6 days and 5 nights.
    SLOT: body (price)
    STATUS: 1 VERIFIED
    SOURCE: TA "NOK 31,000", "Incl. all taxes"; HUB "NOK 31,000"
    NOTES: Not in TJ, so `verify_tours.py` does not cover it. No per person basis stated; the email does not claim one.

[82] CLAIM: 2 nights at Canyon Hotel in Alta, 3 nights at Gargia Lodge, about 30 minutes outside town, with a sauna and evenings by the fire.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA Included list; "approximately 30 minutes into the wilderness of Gargia Valley"; "Sauna and evening by the fire"
    NOTES: Corrected, see correction 10.

[83] CLAIM: Included: 5 nights; transfers as specified, from Alta Airport and back; professional local guides; 4-hour fjord and whale cruise; dog sledding with your own team; snowmobile across Finnmarksvidda; kennel evening; Northern Lights viewing opportunities throughout; sauna access; welcome dinner, dog sledding lunch, Arctic dinner, farewell dinner; selected warm beverages and snacks during the activities; specialist equipment where applicable.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA Included list, verbatim; "the final transfer from Gargia Lodge to Alta Airport"
    NOTES: Corrected wording, see correction 11.

[84] CLAIM: Not included: flights to and from Alta; the optional snowshoe; meals not listed; alcoholic and additional drinks; travel and accident insurance; personal expenses.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA Not Included list, verbatim

[85] CLAIM: Tell us your dates through the tour page and we confirm availability.
    SLOT: body
    STATUS: 3 UNVERIFIED
    SOURCE: none
    NOTES: Marked `[CONFIRM]`. Decision 3.

[86] CLAIM: Deposit amount and balance due date.
    SLOT: body
    STATUS: 3 UNVERIFIED
    SOURCE: none
    NOTES: Marked `[CONFIRM]`. Decision 2.

[87] CLAIM: Cancellation scale, as [32].
    SLOT: body
    STATUS: 1 VERIFIED
    SOURCE: TA Cancellation Policy; TC

[88] CLAIM: Flexible booking conflict, as [33].
    SLOT: body (marker)
    STATUS: 4 DISPUTED
    SOURCE: FB versus TA and TC
    NOTES: Marked `[CONFIRM]`. Decision 1.

[89] CLAIM: Insurance recommendation, as [34].
    SLOT: body
    STATUS: 1 VERIFIED
    SOURCE: TC; TI

[90] CLAIM: Guests rate the trip 4.9/5 on Tripadvisor.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA badge with the Tripadvisor logo in the page HTML
    NOTES: As [35]. No count shown.

### 6-Day Alta Email 6, day 18

[91] CLAIM: The transfer from Alta Airport is included.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA "arrival transfer to Canyon Hotel"

[92] CLAIM: Reply time and calls.
    SLOT: body
    STATUS: 3 UNVERIFIED
    SOURCE: none
    NOTES: Marked `[CONFIRM]`. Decision 4.

### 6-Day Alta Email 7, day 25

[93] CLAIM: The trip runs November to April, 6 days and 5 nights, on dates you choose.
    SLOT: body (dates)
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TA, as [47]

[94] CLAIM: Single traveller option.
    SLOT: body
    STATUS: 3 UNVERIFIED
    SOURCE: none
    NOTES: Marked `[CONFIRM]`. Decision 7.

[95] CLAIM: 60 days before 15 February 2027 is 17 December 2026.
    SLOT: body (dates)
    STATUS: 1 VERIFIED
    SOURCE: arithmetic; the 60-day rule as [87]
    NOTES: An example date, labelled as such in the email. Carries the Decision 1 and Decision 3 markers.

### 6-Day Alta Email 8, day 40

[96] CLAIM: We also build trips to your own dates and pace.
    SLOT: body
    STATUS: 2 LIKELY ACCURATE
    SOURCE: TM "built around your goals, dates, and fitness level"

## Consistency check across slots

- Price: Email 5 and Email 7 of each sequence send the reader to the tour page that shows the same figure. No email states a price the page does not show.
- Dates: the five 7-Day departures appear in Email 2 and Email 7 with the same dates. The Alta emails never name a fixed departure; the one date in Alta Email 7 is labelled as an example.
- Length: "7 days" and "6 days and 5 nights" match the pages and the date spans.
- Cancellation: identical wording in both Email 5 drafts and in both Email 7 drafts.
- Links: every URL in the two sequences returned HTTP 200 on 26 October 2026 (command in the README).
