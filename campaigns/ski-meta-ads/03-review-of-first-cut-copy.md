# Review of the ClickUp first-cut copy (9 creatives)

Scope: the nine Meta creatives in the ClickUp task "Static Image Ad - Skiing", checked against the live tour pages and the confirmed prices. Checked on 2026-10-06.
Every finding below was confirmed in the page text or by loading the URL. Where a page contradicts itself, the finding says so and the safe wording is marked [VERIFY].

## Fix before any design work

| # | Problem | Evidence | Fix |
|---|---|---|---|
| 1 | Creative 1 links to a dead page | `/multi-day-tour/9-day-norway-ski-road-trip` returns HTTP 404. The live page is `/multi-day-tour/ski-trip-in-norway` | Use the live URL |
| 2 | Every link ends in `?utm_source=chatgpt.com` | Present on all links in the brief | Replace with Meta UTMs so paid traffic is not reported as ChatGPT referrals |
| 3 | Creative 5 says "6 Days of Skiing in Fjord Norway" | The 6 Day page says "three ski days" and calls the trip "a mixed winter holiday, not a six-day ski trip" | Say "3 ski days" up front, or lead with the lessons and the 6 day length without the word skiing |
| 4 | Creatives 3 and 8 sell "Aurora Nights" and lead with the northern lights | The 7 Day page says "no departure can guarantee an appearance" | Lead with the trip, use possibility language for the aurora |
| 5 | Creative 4 says "Ski Days in Voss" (plural) | The inclusions list "1-day ski pass at Voss Resort" and the itinerary has one ski day. The FAQ uses "ski days" once, so the page is inconsistent [VERIFY] | Say "a ski day in Voss" |

## Creative by creative

| # | Copy | What works | What to change |
|---|---|---|---|
| 1 | SKI 4 FJORD RESORTS IN 9 DAYS / Voss, Myrkdalen, Sogndal, Stranda / Join 9-Day Ski Trip | The best of the nine. A count, four named places, a verb | The page names Voss and Stranda as its fjord skiing examples, so "4 fjord resorts" claims more than the page does. Try "4 resorts. 9 days. One fjord road trip." The page also says the trip suits "intermediate and advanced skiers", so say so. No price or dates. "Join" is a weak verb |
| 2 | Ski in Norway. With Fjords Below. / Resort & backcountry skiing in Voss. / Explore Skiing in Norway | Good rhythm. The hub supports "fjord-view descents" | Two products in one ad (resort and backcountry). "Explore" is the weakest travel CTA. No tour, price or date |
| 3 | Skiing and Aurora Nights in Norway / Bergen to Tromsø / Find Out How | Route in two words | "Find Out How" has no object. See fix 4 |
| 4 | Beginner Friendly / Ski Days in Voss, Aurora Nights in Tromsø / Check Dates | The eyebrow names who the trip is for | See fixes 4 and 5. The spec strip on the 7 Day page says "Easy to intermediate" while the text says "beginner-friendly" [VERIFY]. "Check Dates" sends the viewer to find what the ad could show |
| 5 | 6 Days of Skiing in Fjord Norway / Voss Resort • Myrkdalen / See the 6-Day Package | Places and length are clear | See fix 3. The page's real hooks are a lesson on every ski day and a day off skis. No price, no dates |
| 6 | 3 Days. Skiing + Snowshoeing. / Voss, Norway / See the 3-Day Trip | Honest and short | Plain, no emotional lift. The tour covers Voss, Hardangerfjord and Myrkdalen, so "Voss" is incomplete. No price or dates |
| 7 | Your 3-Day Winter Escape to Norway / Ski + Snowshoeing / See the 3-Day Trip | "Winter escape" speaks to the segment | Same tour as creative 6 with near-identical copy. The viewer cannot tell them apart. Similar ads may compete for the same audience (Meta's delivery behaviour here is not officially documented) [VERIFY] |
| 8 | 7-Day Northern Lights Tour / Bergen • Voss • Tromsø • Skiing • Huskies • Northern Lights / Explore the Tour | Concrete list | A noun dump with no hierarchy. Leads with the one thing that cannot be promised. See fix 4 |
| 9 | 7 Days \| 6 Nights / 5 Norwegian Winter Experiences / Bergen • Skiing • Snowshoeing • Huskies • Northern Lights / Explore the 7-Day Tour | "7 Days \| 6 Nights" is exact (6 nights twin-share). A count is a good curiosity hook | The count includes Bergen, which is a city stop, not an experience. The page lists four activities (snowshoeing, skiing, dog sledding, aurora). Keep the number identical in every variant. Same tour as creative 8 |

## Patterns across the nine

1. None of the nine shows a price or a date. The winning references that carry them (the 3-Day Autumn Getaway) use them as the main design element.
2. Every CTA is a soft verb: Join, Explore, Find out how, Check dates, See. None names the next step.
3. Six of the nine sell only two tours. Four sell the 7 Day trip (3, 4, 8, 9) and two sell the 3-Day Ski and Snowshoe (6, 7). Rewordings of one idea are not separate concepts. Five tours and both day tours have no ad at all.
4. Skill level shows in only two of nine, yet level is the first thing every buyer checks.
5. No proof anywhere: no rating, no group size, no guide credential, no inclusion that removes a worry.
6. The sensory material on the pages (frozen waterfalls, waffles with jam at a mountain cafe, the gondola from the train station, a campfire grill) is untouched. Only "Voss" and "fjord" appear.

## What the winners do that the first cut does not

The three reference ads that the client audit found generate more leads each show a named product, a human-scale photo and short rhythmic copy. Two of the three also show a date or a price.
The strongest layout is the 3-Day Autumn Getaway: name, a date line with a calendar icon, and a white "STARTING FROM NOK 14,165" pill over a photo of happy guests.
Both a price-and-date ad and a no-price ad appear among the winners, so test the two against each other for each tour instead of locking one template.

Files in this folder that act on these findings: `01-simplified-copy.md` (name, dates, price for all seven tours) and the skill-written ads.
