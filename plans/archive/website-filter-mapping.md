# Website tour filters: tour-to-filter mapping sheet

This plan is for the team building the tour filters on the new "Norway Guided Tours" page. It answers one question: which filter values does each tour get? The output is a private Google Sheet. No prices go into it or into this repo.

## Inputs (read 29 Oct 2026)

1. The website filters ticket: 9 core destinations (Lofoten, Tromsø, Alta, Narvik, Bergen, Voss, Oslo, Flåm, Ålesund), multi-select per trip, short list.
2. Figma frame 7217:79: filter groups Destination, Activity, Trip Type (Day Tours, Multi-Day Tours, Northern Lights Tours), Season (Summer May to Sep, Winter Oct to Apr, Year Round) and Duration (Half Day, Full Day, 2-3 Days, 4+ Days).
3. The internal 2027 rates sheet: tabs MULTIDAY TOURS PRICES, WINTER DAY TOURS, SUMMER DAY TOURS, COMBO PRICES, SPRING, AUTUMN TOURS and COURSES.
4. Live site hubs: /multi-day-tour, /day-tour, /combo, /courses and /northern-lights-tours-norway.
5. Each tour's own page, fetched live. `campaigns/ski-meta-ads/tours.json` for the ski tours.

## Phases

### Phase 1: Facts per tour (Size: M)
- Fetch the four hubs and the northern lights page, list every live tour card.
- Fetch each tour page. Record only what the page says: places, included activities, optional activities, months, length, difficulty, minimum age.
- Match each rates sheet row to a page. Rows with no page keep a status instead.
- Verified when: every rates sheet row and every hub card has a row in `facts.json` (scratch), with a source for each fact.

### Phase 2: Map to filters (Size: S)
- Apply the decisions below in one Python script, so the mapping is repeatable.
- Verified when: a script check finds no value outside the allowed list, and no live tour without a destination.

### Phase 3: Google Sheet (Size: M)
- Tab "Tour filters": Tour ID, Tour name (website), Rates sheet name, Status, Source, URL, Region, Destination 1 to 3, Activity 1 to 6, Trip type 1 to 2, Season 1 to 2, Duration, then side columns Difficulty, Min age and Notes.
- Tab "Long format": one row per tour and filter value, for the developer.
- Tab "Filter values": the allowed values per group with a live count, plus a legend.
- Tab "Open items": conflicts and unknowns, each with who confirms it.
- Formatting: frozen header and name column, one colour per filter block, dropdowns from "Filter values", filter on.
- Verified when: the counts in the sheet match a recount in Python.

## Decision log
| Decision | Chosen option | Why |
| --- | --- | --- |
| Destinations | The ticket's 9 only, tagged when the page names the place | Ticket list is confirmed. Fjord Norway is a region, so it goes in a Region column |
| Region | Fjord Norway, Northern Norway, Abroad | Keeps the design's "Fjord Norway" card working without a fake destination |
| Trip type | Day Tour, Multi-Day Tour, Combo, Course, Northern Lights (multi-select) | Figma's 3 cannot hold combos or courses |
| Season | Winter, Spring, Summer, Autumn, Year Round, from page months and sheet departure dates | Rates sheet sells spring and autumn departures |
| Duration | Figma's 4 values, from the page | Pages are the public truth |
| Activity | Broad values (Biking covers MTB and e-bikes, Kayaking covers fjord, river and whitewater), only included activities | Short list, matches "Show more" |
| Rows with no page | Kept, with Status: Live page, Not online yet, Affiliate, Abroad, Not a tour | Nothing is lost, the developer filters on Status |
| Tour names | Website name, rates sheet name beside it | Customers see the website name |
| Extra groups | Difficulty and Min age as side columns, marked "not in design" | On every page, cheap to add, the team can decide |
| Review | Independent review on 29 Oct 2026, 16 findings, all folded in above | |

## Not yet specified
- Whether the abroad tours belong on a Norway filter page at all. Marked "Abroad" and logged in Open items.
- Whether the site's existing day-tour filters (Activity Type, Segment) feed the new filters. Logged in Open items for the developer.

## Always / Never
- Always: one filter value per cell; each fact from a page or the rates sheet; every guess flagged in Notes.
- Never: prices in the sheet; edits to the rates sheet; sharing the sheet; tours found on neither the rates sheet nor a live hub.

## Progress
| Phase | Status |
| --- | --- |
| 1 Facts | Done |
| 2 Mapping | Done |
| 3 Sheet | Done |

## Execution record (29 Oct 2026)

- Shipped: a private Google Sheet in Sameer's Drive, "Website Tour Filters v1 (tour mapping)", with tabs Read me, Tour filters, Filter values, Long format and Open items.
- Size: 71 tours, 51 with a live page, 39 flagged Check = Yes, 23 open items.
- Deviation: page-by-page fetching stopped at the owner's request. Facts come from the rates sheet, the northern lights page, tours.json and the multi-day and combo hub text already read. Gaps are flagged in Notes rather than filled.
- Deviation: Difficulty and Min age come from the rates sheet Level and Age limits columns, not from pages.
- Verified: the Tour filters text checksum (20607 characters, 1045 filled cells) matches the build script; all 42 counts in Filter values match a Python recount; the Long format tab has 448 rows, matching the script.
