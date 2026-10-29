# Website tour filters: tour-to-filter mapping sheet

Ticket: [Website destination filters v1](https://app.clickup.com/t/17tmpu8hjtm) (owner Sameer, design Abhishek, review Marcio and Karlo)

This plan is for the team building the tour filters on the new "Norway Guided Tours" page. It answers one question: which filter values does each tour get?

## Inputs (read 29 Oct 2026)

1. Ticket: core destinations confirmed by Marcio are Lofoten, Tromsø, Alta, Narvik, Bergen, Voss, Oslo, Flåm and Ålesund. Multi-select per trip. Keep the list short.
2. Figma frame 7217:79: filter groups are Destination, Activity, Trip Type (Day Tours, Multi-Day Tours, Northern Lights Tours), Season (Summer May to Sep, Winter Oct to Apr, Year Round) and Duration (Half Day, Full Day, 2-3 Days, 4+ Days). The hero search uses Destination, Activity, Trip type and Season. The design also shows "Fjord Norway" as a destination and "Fishing" as an activity.
3. Internal 2027 rates sheet: tabs MULTIDAY TOURS PRICES, WINTER DAY TOURS, SUMMER DAY TOURS, COMBO PRICES, SPRING, AUTUMN TOURS and COURSES hold tours. Rental, hotel, shuttle and lesson-pricing tabs do not. No prices go into the new sheet or this repo.
4. Northern lights page: 2 multi-day tours and 10 Alta day tours. The 10 day tours are not in the rates sheet.
5. Site sitemap and `campaigns/ski-meta-ads/tours.json` give the page URL per tour.

## Phases

### Phase 1: Master tour list
Verified when: every tour row in the seven tabs, plus every tour on the northern lights page, appears once, with duplicates merged and each row's source noted.
Files to touch: scratch CSV only.

#### Step 1.1: Build the list (Size: S)
- Acceptance criteria: one row per sellable tour; duplicates merged (for example "7 Day Ski in Fjord Norway & Aurora in Tromsø" is the Bergen to Tromsø northern lights page); status set for each row.
- Verification command: a Python count of rows per source tab against the tab row counts.
- Test seams: the count script.
- Blocked by: gate answers.

### Phase 2: Facts per tour
Verified when: each tour with a live page has destinations, activities, season and duration taken from that page.

#### Step 2.1: Scrape tour pages (Size: M)
- Acceptance criteria: one live fetch per tour page; places and activities recorded only when the page names them; tours with no page are marked "From name only".
- Verification command: a script that lists rows with no source.
- Blocked by: 1.1.

### Phase 3: Google Sheet
Verified when: the sheet opens with the three tabs below, dropdowns work, and the counts tab matches a recount in Python.

#### Step 3.1: Create and fill the sheet (Size: M)
- Tab "Tour filters": A Tour name (website name), B Source tab, C Status, D Page URL, then one filter value per cell in fixed column blocks: Destination 1 to 3, Activity 1 to 6, Trip type 1 to 2, Season 1 to 2, Duration, then Notes.
- Tab "Filter values": every allowed value per group with a live COUNTIF of tours.
- Tab "Open items": conflicts and unknowns, each with who confirms it.
- Formatting: frozen header row and name column, colour per filter block, dropdown validation from "Filter values", filter view on.
- Blocked by: 2.1.

## Decision log
| Decision | Chosen option | Why |
| --- | --- | --- |
| Pending gate | | |

## Not yet specified
- Phase 2: some combo rows in the rates sheet have no page and no clear status. Fog until the scrape shows which are live.

## Always / Never
- Always: one filter value per cell; facts from a page or the rates sheet; every guess flagged in Notes.
- Never: prices in the new sheet; edits to the rates sheet; sharing the sheet with anyone but Sameer; adding tours that appear on neither source.

## Progress
| Phase | Status |
| --- | --- |
| 1 Master list | Waiting on gate |
| 2 Facts | Waiting on gate |
| 3 Sheet | Waiting on gate |
