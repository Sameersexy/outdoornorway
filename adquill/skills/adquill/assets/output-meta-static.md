# Output shape: Meta static ads

The exact output adquill returns for a Meta (Facebook and Instagram) static image ad. Read it at step 8 of the method, and copy the shape without changing the order. The filled example uses the fictional brief from assets/brief-template.md.

## Rules for this output

1. One section per variant. Each variant is a different idea.
2. Every slot shows its text, its character count and its budget. Counts are computed in code and include spaces and the comma in "NOK 4,900".
3. No sentence appears in two slots. The headline may repeat the offer (the price), and may not repeat a sentence from the primary text.
4. Lint every slot with scripts/slop_lint.py and its --slot name (meta_image_line_1 to 3, meta_primary, meta_headline, meta_description, reels_line). Show the lowest score and any hits.
5. Every variant ends with a receipt of four lines: Angle, Mechanism, Risk, Test hypothesis.
6. One group chat line for the whole set. It holds the same facts as the ads.
7. One image spec brief. The designer or a layout tool puts the text on the image. An image generator never renders it, because generators garble text and can invent details.
8. A policy and fact pass with tiers: block, warn, note.
9. A status line that says either "ready to paste" or "draft, not ready to publish", with the reason.

## The shape

```text
# Meta static ads: <offer>
Brief: <brand> (fictional brief, if it is an example)
Status: <ready to paste | draft, not ready to publish> (<reason>)
Platform data verified 2026-10-06

## Diagnosis
Awareness level: <level> (<given | defaulted>)
Sophistication stage: <1 to 5> (<given | guessed>)
Job to be done: <one sentence>
Main anxiety: <one sentence>

## Ledger facts used
<list of ledger rows used, each with its value>
Not used (not verified or not allowed): <list>

## Variant 1: <angle name>
| Slot | Text | Count | Budget |
|---|---|---|---|
| image_line_1 | | n | 25 |
| image_line_2 | | n | 30 |
| image_line_3 | | n | 20 |
| primary_text | | n | 125 visible |
| headline | | n | 27 |
| description | | n | 30 |
| cta | <button label from references/meta.md> | label | label |
| reels_line | | n | 40 |

Hook type: <type>
Lint: <score>/100 (<hits or none>)

Receipt
- Angle: <one sentence>
- Mechanism: <named mechanism from references/psychology.md>
- Risk: <what must be true for this to be honest>
- Test hypothesis: <if X, then Y beats Z>

## Variant 2: <angle name>
(same shape)

## Variant 3: <angle name>
(same shape)

## Angle check
| Variant | Hook type | Scene | Person | Offer angle |
|---|---|---|---|---|

## Group chat line
<one sentence written to be pasted to a friend>

## Image spec brief (for the designer)
<ratio, resolution, margins, type hierarchy, the three lines, photo direction,
9:16 version, who adds the text>

## Policy and fact pass
Block: <list or none>
Warn: <list or none>
Note: <list>
Fact check: <every number mapped to a ledger row, weekdays checked, price matches landing page>

## Before you publish
<Advantage+ settings, preview checks, landing page price>

Platform data verified 2026-10-06. adquill does not publish ads. Check the live
policy pages before you spend.
```

## Filled example (fictional brief)

Everything below belongs to a fictional brief. Brekke Ski Guides does not exist. The prices, dates and numbers are made up.

---

# Meta static ads: Intro to ski touring

Brief: Brekke Ski Guides (fictional brief)
Status: ready to paste, after the two preview checks under "Before you publish"
Platform data verified 2026-10-06

## Diagnosis

- Awareness level: problem-aware (given in the brief)
- Sophistication stage: 3 (guessed, not checked against competitor ads)
- Job to be done: do something different with a weekend that the buyer can already almost do
- Main anxiety: "am I good enough", then "what if it is called off"

## Ledger facts used

NOK 4,900 per person. Sunnmøre Alps, meeting at a car park above Brekke. Saturdays 9 Jan to 27 Feb 2027, eight departures. Six people per guide. Red runs with control required. Typical day times. Gear hire NOK 650 per person. Free cancellation up to 7 days before. Full refund or another Saturday if the guide calls the day off for avalanche risk. Taught on the day: skins, kick turns, transceiver.

Not used (not verified or not allowed): guide certification (no certificate number), guest reviews (none supplied), seats left (not supplied), any superlative.

## Variant 1: The day, hour by hour

| Slot | Text | Count | Budget |
|---|---|---|---|
| image_line_1 | Intro to ski touring | 20 | 25 |
| image_line_2 | Saturdays, 9 Jan to 27 Feb | 26 | 30 |
| image_line_3 | NOK 4,900 | 9 | 20 |
| primary_text | Typical day in the Sunnmøre Alps: meet 08:30, skins on 09:15, first descent about 11:40, back about 15:30. Six per guide. | 121 | 125 visible |
| headline | Ski touring day, NOK 4,900 | 26 | 27 |
| description | Gear hire NOK 650 per person | 28 | 30 |
| cta | Check Availability | label | label |
| reels_line | Try ski touring with a guide. NOK 4,900. | 40 | 40 |

Hook type: specificity
Lint: 100/100 (lowest of 7 slots, no hits)

Receipt
- Angle: a beginner can picture the whole day, so the unknown gets smaller.
- Mechanism: concreteness (times and numbers instead of adjectives).
- Risk: false precision. The times are typical, and the owner says conditions can shift them, so the copy says "typical" and "about".
- Test hypothesis: if not knowing what the day looks like is the main hurdle, this variant gets more link clicks per impression than Variant 3.

## Variant 2: Called off? You choose

| Slot | Text | Count | Budget |
|---|---|---|---|
| image_line_1 | Ski touring, 6 max | 18 | 25 |
| image_line_2 | Saturdays, 9 Jan to 27 Feb | 26 | 30 |
| image_line_3 | NOK 4,900 | 9 | 20 |
| primary_text | Day called off for avalanche risk? Pick another Saturday or take a full refund. 8 Saturdays, 6 people per guide. | 112 | 125 visible |
| headline | Ski touring, NOK 4,900 | 22 | 27 |
| description | Cancel free up to 7 days out | 28 | 30 |
| cta | Check Availability | label | label |
| reels_line | Day called off? Rebook or full refund. | 38 | 40 |

Hook type: question about the activity, with a direct benefit
Lint: 100/100 (lowest of 7 slots, no hits)

Receipt
- Angle: the second doubt after "can I do it" is "what if it is called off", and the refund rule answers it with a fact.
- Mechanism: risk reversal (cancellation and safety refund).
- Risk: overselling the refund. The copy states only the avalanche rule and the 7 day rule, as in the booking terms. Paste the terms onto the landing page before the ad runs.
- Test hypothesis: if worry about cancellation stops people from clicking, this variant beats Variant 1 on clicks per impression among people who have seen the landing page before.

## Variant 3: Red runs required

| Slot | Text | Count | Budget |
|---|---|---|---|
| image_line_1 | Red runs required | 17 | 25 |
| image_line_2 | Saturdays, 9 Jan to 27 Feb | 26 | 30 |
| image_line_3 | NOK 4,900 | 9 | 20 |
| primary_text | You need to ski red runs with control. You do not need to have toured. 6 per guide, and we teach skins and kick turns. | 118 | 125 visible |
| headline | First ski tour, NOK 4,900 | 25 | 27 |
| description | Avalanche kit loan included | 27 | 30 |
| cta | Check Availability | label | label |
| reels_line | Ski red runs? Then learn to skin up. | 36 | 40 |

Hook type: honest concession (a contrarian hook)
Lint: 100/100 (lowest of 7 slots, no hits)

Receipt
- Angle: say the entry bar first, and the right people recognise themselves.
- Mechanism: honest constraint, which answers the level anxiety with a fact (references/psychology.md, job to be done: anxiety).
- Risk: reads as exclusion. The copy states the requirement of the day. It makes no claim about the viewer's body, age or fitness.
- Test hypothesis: if self-selection raises click quality, this variant gets fewer clicks than Variant 1 and a higher share of clickers who check availability.

## Angle check

| Variant | Hook type | Scene | Person | Offer angle |
|---|---|---|---|---|
| 1 | specificity | the schedule on the day | the curious first-timer | the day itself |
| 2 | question and benefit | the call-off moment | the cautious planner | the refund rule |
| 3 | honest concession | the entry bar | the confident resort skier | who it is for |

No two rows match on more than one column. Each is a different idea.

## Group chat line

There's a guided ski touring day on Saturdays from 9 Jan: 6 people per guide, NOK 4,900 per person, avalanche kit loan included. You ski red runs, so you're in. I'm looking at 16 Jan. Are you free?

197 characters. Same facts as the ads, plus a Saturday the sender picks (16 Jan is inside the window).

## Image spec brief (for the designer)

This brief is fictional.

- Ratio and size: 4:5, 1440 x 1800 px, JPG or PNG, under 30 MB (Meta Ads Guide, verified 2026-10-06: https://www.facebook.com/business/ads-guide/update/image/facebook-feed/link-clicks).
- Margins: keep all text at least 5 percent from every edge (72 px at the sides, 90 px at top and bottom). Practitioner heuristic, not a Meta rule. Keep the text block out of the lowest part of the image.
- Type hierarchy: price (line 3) heaviest and largest, date (line 2) second, name (line 1) third. Starting sizes to test: 160 px, 90 px and 80 px type. Adjust until all three lines read at 375 px wide.
- Contrast: text on a plain area or a solid band, at least 4.5 to 1 against the background (https://www.w3.org/TR/WCAG21/#contrast-minimum).
- On-image lines for Variant 1: "Intro to ski touring", "Saturdays, 9 Jan to 27 Feb", "NOK 4,900". Variants 2 and 3 use the lines in their tables.
- Photo direction: a real photo of a real group on skins, daylight, faces visible, taken by the brand with consent. No stock, no generated people. No third-party logos.
- Text is added in a layout tool or by a designer. An image generator never renders it.
- 9:16 version, only if the ad runs in Stories and Reels: 1080 x 1920 px. Keep text out of the top 269 px, the bottom 672 px and 65 px at each side, which leaves a centre band of about 950 x 979 px (Meta Reels spec, verified 2026-10-06: https://www.facebook.com/business/ads-guide/update/video/instagram-reels/link-clicks). The reels_line goes in this version.
- Instagram crops the profile grid to a taller shape, and the 72 px side margin keeps the text clear of it [VERIFY: reported by https://influencermarketinghub.com/instagram-image-sizes/, ads run in the feed, not the grid].

## Policy and fact pass

Block: none.

Warn:
- Variant 2: the refund wording must match the booking terms exactly. Check the landing page text before launch.

Note:
- Variant 3: "You need to ski red runs with control" describes a requirement of the offer. It does not assert a personal attribute about the viewer. Keep it about the activity.
- The price NOK 4,900 is the same in the image lines, headline and landing page (the user pasted the page price).
- The Instagram feed headline field reportedly does not show on single image ads [VERIFY in Ads Manager preview]. The image lines carry the price, so nothing is lost.
- The description slot is often hidden on mobile. Nothing important lives only there.

Fact check: 9 Jan 2027 and 27 Feb 2027 are Saturdays (calendar calculation). Eight Saturdays counted: 9, 16, 23 and 30 Jan, 6, 13, 20 and 27 Feb. Every number in the slots maps to a ledger row: 4,900, 650, 6, 8, 08:30, 09:15, 11:40, 15:30, 7. Typical times carry "typical" or "about". No testimonial, rating, certification or seat count appears.

## Before you publish

1. In Ads Manager, switch off for each of these ads: text improvements, text generation, enhance media text, image text rewriting and enhance CTA. Meta can rewrite text inside images in some campaign types, and a rewritten price or date is a trust and policy problem [VERIFY: reported by third parties from 27 July 2026, source https://www.xwork.my/meta-advantage-creative-ad-image-text/].
2. Open the Facebook feed and Instagram feed previews. Check where the primary text cuts at "See more" on a phone-sized preview.
3. Confirm the landing page shows NOK 4,900 per person and the eight dates.
4. Run one ad per concept in one broad ad set. Changing only the headline or the colour of the price does not make a new concept.

Platform data verified 2026-10-06. adquill does not publish ads. Check the live policy pages before you spend.

---

Sources

- Facebook feed image and text spec: https://www.facebook.com/business/ads-guide/update/image/facebook-feed/link-clicks (verified 2026-10-06)
- Instagram feed image spec: https://www.facebook.com/business/ads-guide/update/image/instagram-feed/link-clicks (verified 2026-10-06)
- Reels spec and safe zone: https://www.facebook.com/business/ads-guide/update/video/instagram-reels/link-clicks (verified 2026-10-06)
- Primary text cut at about 125 characters, device dependent [VERIFY: vendor figure]: https://adplus.com/tools/ad-specs-validator/facebook-125-character-primary-text
- Contrast minimum: https://www.w3.org/TR/WCAG21/#contrast-minimum
