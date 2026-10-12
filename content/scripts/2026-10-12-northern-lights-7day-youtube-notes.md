# Northern Lights 7 day tour, YouTube script: status and open items

Script file: `content/scripts/2026-10-12-northern-lights-7day-youtube.md` (tier long, voiceover, about 2 min 50 s spoken, 16 beats, description with chapters).
Tour page: https://www.outdoornorway.com/multi-day-tour/northern-lights-tour-bergen-tromso (the page you named; its text was read on 2026-10-08 and matches `tours.json`, id `ski-aurora-7day`).

## Status

- The validator passes the script in strict mode: no failures, no warnings.
- `--final` fails on 37 placeholders (rule BR13). Every one is a `[VERIFY]` in a visual cell for footage, a permission, a guest release or a fact. That is by design: nobody could be asked, so no shot is invented.
- It is not ready to record or publish. The last independent review scored the hand-edited version 6.1 out of 10 and gave REJECT, because my own edit put "ski days" into beat 7 (the trip has one ski day, and the do-not-claim list bans the plural). I fixed that and the other small items the reviewer found. Those last fixes have not been independently re-reviewed.

## Score history (the reviewer's own numbers, mean of ten items)

| Version | Mean | Verdict | Note |
|---|---|---|---|
| Angle B v1, "two Norways" | 5.0 | REJECT | No source explains why the trip goes south first, so the loop cannot be paid off. Dropped. |
| Angle A v1, "honest odds" | 5.5 | REVISE | Overstated lines, brochure voice. |
| v2 | 5.4 | REJECT | Regressed. |
| v3 | 5.7 | REVISE | Time jumps, labels used before they were introduced, wrong pronouns. |
| v4 | 6.3 | REVISE | Rebuilt in trip order. Hook 7, loop 6, overload 7, visual 6, guest benefit 7, brand voice 5, facts 7, sounds human 6, distinct 5, objection 7. |
| v5 (v4 plus hand edits) | 6.1 | REJECT | My "ski days" error, then fixed. |

Two skeptic audits (sources, and rules, law and safety) ran on v3 and v4. They found a wrong day order, an implied count of aurora evenings, a weather-style overstatement and unsafe shots, all fixed.

## Needed from you, in order

1. **Day 4.** `tours.json` and the page itinerary say a guided aurora safari follows the flight. One FAQ says Day 4 is "the transfer". Another says "Days 4 through 6 are dedicated to northern lights viewing". A third says "three nights chasing the Northern Lights". The script states no count. If the safari is confirmed, add that first evening to beat 7 and fix the page FAQ.
2. **Lunch.** `tours.json` and the page's Day 5 text say a chef cooks lunch on the boat. The page's Not Included list says "Lunches". The script says nothing about lunch.
3. **Gear.** The page header says "All Gear Included" and "All equipment + guide + transfers + stay". Not Included says skis, boots, poles and helmets are not in the price. The Day 3 text says "Our package includes top quality equipment". The video says the gear is not included, so the page has to be corrected before the video links to it.
4. **Price basis.** The page says twin-share rooms and "Incl. all taxes". Nothing says whether a single supplement applies or whether "from" is bookable on every departure. The script says only "From NOK 41,181" in the description.
5. **Guides.** Does one guide stay with the group all week, or do guides change between Voss and Tromsø? The script says only "a professional guide throughout the trip".
6. **Weather.** What happens when a boat or sled day is weathered off? The script makes no promise either way.
7. **Level wording.** The page says no previous skiing experience is required and the ski day is beginner-friendly. `product-marketing.md` says level wording conflicts across pages. The script does not use it.

## Needed from the guides

The Voss guide (Day 2) and the Tromsø guide (Day 5 camp evening, Day 6 hunt) should answer questions 3, 4, 5, 7, 9 and 10 of `.claude/skills/scriptcraft/assets/guide-moment-intake.md`. Every round of review named the same ceiling: the only sensory words are the page's own adjectives, the night shots are generic, and the opening frame is not tied to the question. Real moments from real evenings are the only fix, and more rewrite rounds will not replace them.

## Shoot notes from the audits

- **Releases.** A written release from every guest in shot, with separate boxes for organic YouTube, ads and other platforms, a way to withdraw and a named contact. Guardian consent for under 18 (the page sets a minimum age of 8). [VERIFY with counsel: Norwegian image right and GDPR]
- **Permissions.** Bergen station, Voss Resort, the boat operator, the dog yard and the musher, the hotel camp (exteriors only), Bergen and Tromsø airports (landside only, no boarding passes in frame).
- **Safety.** The aurora hunt stop is a placeholder: ask the Tromsø guide where it really stops, and keep guests off the road edge. At Voss, stop at the side of the run, helmets on. On the boat, show the operator's safety gear. Mount the sled camera only with the musher's approval. Show calm dogs.
- **Sky shots.** Film real evenings. No composited or AI sky. If any sky is altered, YouTube's altered content disclosure applies.
- **Screen recordings.** Crop out the page header, the 4.9/5 badge, the gear banner, the What's Included info box and the "Lunches" line.
- **Music.** Natural sound only as written. Any track needs a licence that covers YouTube and ads.

## Known weaknesses the reviewer left open

- Language: only page adjectives ("high rising peaks", "cold mountain air").
- Rhythm: six beats in a row open on a time marker (the next morning, then comes, next).
- Mini-payoffs 1 and 2 give the same reward twice. The chapter questions are itinerary prompts with obvious answers.
- The payoff line reworded the page's pitch line.
- Frame 1 (a train leaving Bergen) is lit and moves, but nothing links it to the question. The "lit car park" hunt stop is unlikely.

## Variants from the writer

- Hook: "Picture your week in Norway with cloud every night. Would you still go?" Should stop more cold viewers because it makes the loss concrete. The reviewer may flag "Picture" as a staged opener like "Imagine", so check before using.
- Call to action: "Before you choose a week, open the trip page below and read what isn't in the price." Should bring more qualified clicks, because the honest payoff and the ask match.

## How this was made

Two writer agents wrote two angles. An independent reviewer scored each, and the better one went through four versions, each followed by a review and two skeptic audits. The orchestrator hand-edited the last fixes, and a reviewer checked them, which is how the "ski days" error was caught. Work on this script also added two validator rules: chapter lines in a YouTube description (C06), and `[VERIFY]` placeholders in visual cells block `--final` (BR13).
