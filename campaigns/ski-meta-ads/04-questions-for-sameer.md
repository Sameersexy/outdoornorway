# Open questions before these ads go live

Nothing here blocks the copy drafts. Each item stops a specific claim from going into an ad. Until answered, the drafts use the safe wording in the last column.

| # | Question | Why it matters | Safe wording until answered |
|---|---|---|---|
| 1 | Are the multi-day prices per person? | The hub and pages do not say. A wrong "per person" is a price claim error | "from NOK 17,451" |
| 2 | Day tours: is the headline price NOK 1,948 (adult)? The pages also show NOK 1,753 (youth) and open group prices of NOK 1,858 (beginner) and NOK 1,650 (advanced) that need three guests | "From" must match the landing page. If fewer than three guests book, the guest may be asked to share a private guide fee | "NOK 1,948 per adult" |
| 3 | Are lift passes included on the 9 Day, 3-Day Ski and Snowshoe, and 3-Day Multi-Sport trips? | Not stated. The 7 Day trip includes a 1-day pass and the 6 Day package includes ski passes | Do not mention lift passes |
| 4 | Is "All gear included" true on any tour? The hub badge says so, but the 7 Day page says skis, boots, poles and helmets are not included | A false inclusion claim is a refund dispute | Do not claim gear is included |
| 5 | Real group size and guide ratio per tour | The hub says "Small groups" with no number. A real number is the strongest proof line available | "Small groups" only |
| 6 | Where does the 4.9/5 rating come from, and how many reviews? | The hub shows it with no source. The winning ad used named badges ("Tripadvisor 4.9", "Google 4.9") | No rating until sourced |
| 7 | Is "Few Slots left" on the hub true, live availability? | Meta and Norwegian marketing law treat false scarcity as misleading | No scarcity wording. Real departure dates only |
| 8 | Minimum age. The 3-day pages say both "10+ years" and "No age limits". The 7 Day page says 8, day tours say 14 | Cannot be stated in an ad until the pages agree | No age statement |
| 9 | Skill level of the 3-Day Ski and Snowshoe ("Beginner to intermediate" in the spec strip, "prior hiking and skiing experience is recommended" in the text) and the 3-Day Multi-Sport ("Intermediate" in the spec strip, "absolute beginner" in the text) | Decides whether a beginner angle is allowed | No beginner angle for those two |
| 10 | 7 Day trip: one ski day or more? The inclusions list a 1-day pass, one FAQ says "ski days" | Plural "ski days" is the claim in Creative 4 | "a ski day in Voss" |
| 11 | 7 Day trip: what counts as "5 winter experiences"? | Creative 9 counts Bergen as one of five | Name the activities, skip the count |
| 12 | 9 Day trip: which resorts show a fjord from the piste? | Decides whether "4 fjord resorts" is allowed | "4 resorts, one fjord road trip" |
| 13 | Cancellation and Lifetime Guarantee terms. The 9, 7 and 6 day pages state refund tiers, the 3-day pages describe a guarantee, and the 6 Day FAQ says the general terms differ | Risk reversal is a strong buyer reassurance, but the terms conflict | No cancellation claim in ads |
| 14 | Are the 7 Day and 9 Day trips registered as package travel (Norwegian package travel rules)? | May require specific ad disclosures | Ask the client's counsel |
| 15 | Real guest quotes and photo permissions for each tour | The best-performing reference ad used a large, happy group photo | No quotes. Use only photos that show the real product |
| 16 | Is any ski departure women-only or women-led? | The women-only wellness ad performed, but no ski page offers that | Do not imply it |
| 17 | Should the Canada ski road trip (NOK 43,124, in your price list but not on the /ski hub) get ads? | Left out because the task said /ski | Not included |
| 18 | Should the 3-Day Ski and Snowshoe and 3-Day Multi-Sport tour pages be fixed? Both still show the old prices (NOK 13,462 and NOK 12,749), and Multi-Sport still lists 2026 departures | Meta compares the ad price with the landing page. A mismatch can get the ad rejected | Hub price used. Fix the pages before launch |
| 19 | Fix the 9-day link in the ClickUp brief. The old URL returns 404 | A dead landing page | Live URL used |

Checked on 2026-10-06 against the live pages. Prices and dates are verified by `verify_tours.py`.

## Owner answers (12 October 2026)

- Row 4 (gear): the owner knows the hub badge and the 7 Day page disagree. The company wants the "All Gear Included" wording on the site. Scripts keep the rule in `.claude/product-marketing.md` and do not claim gear is included. [VERIFY: owner to say if scripts may use the badge wording]
- Row 6 (rating): the 4.9/5 comes from the company's Tripadvisor listing. The site could not link it to Tripadvisor, so it has no source on the page. [VERIFY: current number, review count and which listing] Scripts keep the rule: no rating badge without a named source and a current number.
