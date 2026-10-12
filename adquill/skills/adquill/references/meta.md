# Meta (Facebook and Instagram) ad specs, text limits, delivery and Advantage+ settings

What this is: the platform reference for any Meta output. Read it at step 5 (slots and budgets) and step 7 (policy and fact pass), and again whenever the user asks for a button label, a safe zone, a character count or an Advantage+ setting. Platform data verified 2026-10-06.

## Contents

1. How to read the evidence tags
2. Image specs
3. Video and Reels specs
4. Safe zones for 9:16
5. Carousel and collection
6. Call to action buttons
7. Text limits and truncation
8. Anatomy of the ad, Facebook mobile feed
9. Anatomy of the ad, Instagram feed
10. Character budgets per slot
11. Delivery mechanics: official and vendor lore
12. Advantage+ creative and text edits
13. Placements that changed in the last 12 months
14. Re-verify routine
15. Sources

## 1. How to read the evidence tags

Platform pages move faster than any reference file. Every number below carries one of these tags.

| Tag | Meaning |
|---|---|
| verified 2026-10-06 | Read on a Meta page by the adquill research pass. The page URL is in the row. |
| Reported | Trade press or a practitioner describing the platform. Cross-checked where possible. Treat as likely, not certain. Every Reported row also carries a [VERIFY] note, so no row reads as confirmed when it is not. |
| Vendor | An agency, tool or blog claim with no Meta page behind it. Treat as a hypothesis. |
| [VERIFY: reason] | Could not be confirmed. Do not present it to the user as fact. Check it in Ads Manager preview or on the live Meta page. |
| adquill heuristic | Our own working rule for legibility. Not a Meta rule. Say so when asked. |

Meta states its text lengths as recommendations. Ads Manager accepts longer text. The limit that matters is where the layout cuts the text. Write "recommended" and "cuts at about", never "the limit".

## 2. Image specs

The workhorse is the 4:5 single image at 1440 x 1800.

| Placement | Ratio | Recommended size | Minimums | File | Max size | Source | Status |
|---|---|---|---|---|---|---|---|
| Facebook Feed | 4:5 (3% tolerance) | 1440 x 1800 | 600 px wide, 750 px high | JPG, PNG | 30 MB | https://www.facebook.com/business/ads-guide/update/image/facebook-feed/link-clicks | verified 2026-10-06 |
| Instagram Feed | 4:5 (1% tolerance). Allowed range from 4:5 down to 1.91:1 | 1440 x 1800 | 500 px wide | JPG, PNG | 30 MB | https://www.facebook.com/business/ads-guide/update/image/instagram-feed/link-clicks | verified 2026-10-06 |
| Stories and Reels (image used as 9:16) | 9:16 | 1080 x 1920 is the working standard | none confirmed | JPG, PNG | 30 MB | https://adsuploader.com/blog/meta-ads-safe-zones | [VERIFY: Meta's Stories image spec page returned 404 to the research pass, figures come from vendor guides] |

Three practical notes.

- Meta's image page for Facebook Feed pushes video ("use movement and sound to show unique features"). A static ad is still a normal, working format. It is cheaper to make and it carries a price and a date well.
- Instagram changed its profile grid to a taller crop in January 2025. Reports say the grid now crops to 3:4 while the feed still shows up to 4:5. Ads run in the feed, so this only touches organic posts that later sit on a grid. Arithmetic: a 1080 x 1350 image cropped to 3:4 loses about 34 px on each side. Keep names, prices and dates at least 40 px in from the left and right edges. Source: https://influencermarketinghub.com/instagram-image-sizes/ . [VERIFY: grid crop behaviour is reported, not read on an Instagram page]
- Feed safe zone: Meta publishes none that the research pass could read. One vendor says 250 px top and bottom for 4:5 and 100 px on every edge for 1:1 (https://adsuploader.com/blog/meta-ads-safe-zones). [VERIFY: vendor only]. adquill heuristic: keep a 5 percent inner margin on every side of a 4:5 or 1:1 feed image.

## 3. Video and Reels specs

Static ads are the main output of adquill. These rows exist so the image spec brief can name the right video format when a user asks for a Reels version.

| Placement | Ratio | Resolution | Length | File limits | Text fields | Source | Status |
|---|---|---|---|---|---|---|---|
| Facebook Feed video | 4:5 | 1440 x 1800 | 1 second to 241 minutes | 4 GB, MP4, MOV, GIF | primary 50-150, headline 27 | https://www.facebook.com/business/ads-guide/update/video/facebook-feed/link-clicks | verified 2026-10-06 |
| Instagram Feed video | 9:16 listed on the Meta page | 1080 x 1920 | 1 second to 60 minutes | 4 GB | primary 125, up to 30 hashtags | https://www.facebook.com/business/ads-guide/update/video/instagram-feed/link-clicks | verified 2026-10-06 |
| Instagram Reels | 9:16 | 1440 x 2560 | up to 15 minutes | 4 GB, MP4, MOV, H.264 | primary text 44 | https://www.facebook.com/business/ads-guide/update/video/instagram-reels/link-clicks | verified 2026-10-06 |

Shared by the video pages read: H.264, square pixels, fixed frame rate, progressive scan, stereo AAC at 128 kbps or higher. Captions and sound are "optional, but recommended" on feed and "optional but strongly recommended" on Reels.

Conflict to flag. Some vendor tables give Instagram Reels primary text as 72 for traffic ads and Facebook Reels as 40 primary and 55 headline. Only the 44 figure is on a Meta page. Treat 72, 40 and 55 as [VERIFY: only in https://adsuploader.com/blog/meta-ad-copy-specs and https://socialrails.com/blog/facebook-ad-character-limits].

Footer note from Meta's Facebook Feed video page: on mobile, when the objective is Awareness, or a goal such as 2-second views, impressions or engagement, the headline, description and CTA footer do not display. Pick the objective with that in mind. Source: the Facebook Feed video page above, verified 2026-10-06.

## 4. Safe zones for 9:16

Meta's Reels spec page says to leave at least 14 percent of the top, 35 percent of the bottom and 6 percent of each side free of text, logos and anything critical. Source: https://www.facebook.com/business/ads-guide/update/video/instagram-reels/link-clicks , verified 2026-10-06.

The pixel values below are adquill arithmetic from those percentages.

| Canvas | Top 14% | Bottom 35% | Each side 6% | Working band left in the middle |
|---|---|---|---|---|
| 1080 x 1920 | 269 px | 672 px | 65 px | about 950 px wide by 979 px tall |
| 1440 x 2560 | 358 px | 896 px | 86 px | about 1268 px wide by 1306 px tall |

Reported: Stories guides quote 14 percent top and 20 percent bottom, where the 20 percent is link sticker or CTA clearance and not the full interface. One guide says Stories and Reels now share the same 9:16 numbers. Source: https://adsuploader.com/blog/meta-ads-safe-zones . [VERIFY: vendor guide, cites a Meta help diagram that did not open]. Use the stricter Reels numbers for every 9:16 file. They are safe for Stories too.

Design consequence: the three on-image lines of a static ad (what, when, how much) must fit inside the middle band of a 9:16 file. On 1080 x 1920 that is the stretch between y = 269 and y = 1248. Anything lower sits under the interface.

## 5. Carousel and collection

| Format | Cards | Ratio and size | Text | Source | Status |
|---|---|---|---|---|---|
| Facebook Feed carousel | 2 to 10 | 1:1, at least 1080 x 1080 | primary 80, headline 20, description 18 | https://www.facebook.com/business/ads-guide/update/carousel/facebook-feed/link-clicks | verified 2026-10-06 |
| Instagram Feed carousel | 2 to 10 | 4:5 for image-only carousels, 1:1 for any carousel with video, at least 1080 x 1080 | primary 125, up to 30 hashtags | https://www.facebook.com/business/ads-guide/update/carousel/instagram-feed/link-clicks | verified 2026-10-06 |
| Collection (Facebook Feed) | cover plus 3 product images | cover 1.91:1 to 1:1, at least 1080 x 1080 | primary 125, headline 40 | https://www.facebook.com/business/ads-guide/update/collection | verified 2026-10-06 |

Card video runs 1 second to 240 minutes on Facebook and 1 second to 2 minutes on Instagram. Meta may apply custom positioning to carousel cards, which changes card order per person while the overall sequence stays consistent (same carousel pages, verified 2026-10-06).

A 20 character carousel headline is tight. "Ski day, NOK 4,900" is 18. Collection and catalog formats need a product catalog and open a full-screen landing format. For a small operator with a handful of departures, a carousel with one card per departure does the same job with less setup. [VERIFY: whether a tour or activity catalog type exists for Advantage+ catalog ads, no Meta page read]

Flexible format (reported): one ad holds up to 10 images or videos and Meta chooses the form per viewer. From March 2026 the top-level option was reportedly folded into a "Flexible media" toggle inside Advantage+ creative. Sources: https://metricool.com/flexible-ads-meta/ , https://www.jonloomer.com/flexible-ad-format/ , https://adsuploader.com/blog/meta-flexible-ads . [VERIFY: Vendor and Reported only, no Meta page read]

## 6. Call to action buttons

The exact lists below come from Meta's Ads Guide pages for image ads with the link clicks objective, verified 2026-10-06. Sources: https://www.facebook.com/business/ads-guide/update/image/facebook-feed/link-clicks and https://www.facebook.com/business/ads-guide/update/image/instagram-feed/link-clicks .

Facebook Feed, 31 labels:

Download, Get promotions, Get updates, Watch live video, Get Tickets, Remind Me, Visit profile, Try in Camera, Apply now, Subscribe, Check Availability, Get offer, Get quote, Learn more, Order now, Contact us, Listen now, Send WhatsApp message, Buy tickets, Visit Instagram profile, Sign up, See details, Book now, Send message, Watch more, Shop now, See menu, Request time, Get access, Call now, Get showtimes.

Instagram Feed, 27 labels. The Facebook list minus Watch live video, Get Tickets, Visit profile and Get access.

Meta's own caveat on those pages: not all calls to action are available to every advertiser, depending on industry. The list also varies by objective and by conversion location (website, Messenger, WhatsApp, call). Check the button dropdown in Ads Manager before you recommend a label.

### The subset that fits a guided trip or tour

| Button | Use it when | Note |
|---|---|---|
| Book now | The landing page lets the visitor book and pay or hold a place | Strongest commitment. Must match a booking page. |
| Check Availability | The landing page shows dates and places left | Lower friction than Book now for a higher-priced trip. On both Facebook and Instagram feed. |
| Learn more | The landing page is an itinerary or tour page | Safe default. Weakest signal. |
| Get offer | A real, dated offer exists and the landing page shows it | Never recommend it without a stated real offer. |
| Get quote | Custom group or multi-day enquiry | Fits a sales-assisted trip. |
| Request time | A call back or consultation | Fits a sales-assisted trip. |
| Contact us, Send message, Send WhatsApp message | Pre-sale questions | Needs someone who answers within the hour. |
| Sign up | Newsletter or season alert list | Not a booking. |
| See details | Neutral | Rarely better than Learn more. |
| Call now | Phone-led sales | Mobile only. |

Not relevant to tours: See menu, Shop now, Order now, Download, Listen now, Get showtimes, Try in Camera.

Default rule for adquill: Book now when the landing page has a booking widget, Check Availability when it shows dates and places, Learn more otherwise. Say why in one line.

## 7. Text limits and truncation

### What Meta's pages state

| Placement | Primary text | Headline | Description | Source | Status |
|---|---|---|---|---|---|
| Facebook Feed (image and video) | 50-150 recommended | 27 | not on the page | https://www.facebook.com/business/ads-guide/update/image/facebook-feed/link-clicks | verified 2026-10-06 |
| Instagram Feed | 125 | 40 | none | https://www.facebook.com/business/ads-guide/update/image/instagram-feed/link-clicks | verified 2026-10-06 |
| Instagram Reels | 44 | none | none | https://www.facebook.com/business/ads-guide/update/video/instagram-reels/link-clicks | verified 2026-10-06 |
| Facebook Feed carousel | 80 | 20 | 18 | https://www.facebook.com/business/ads-guide/update/carousel/facebook-feed/link-clicks | verified 2026-10-06 |
| Instagram carousel | 125 | not listed | none | https://www.facebook.com/business/ads-guide/update/carousel/instagram-feed/link-clicks | verified 2026-10-06 |
| Collection (Facebook Feed) | 125 | 40 | none | https://www.facebook.com/business/ads-guide/update/collection | verified 2026-10-06 |

A secondary tabulation, "read from each placement page in July 2026", lists Stories 125 / 40, Marketplace 125 / 40 / 30, Search results 125 / 40 / 30, in-stream video 125 / 40 and right column headline 40. Source: https://socialrails.com/blog/facebook-ad-character-limits . [VERIFY: Reported, not read on Meta pages]

Facebook Feed description: the Meta page read does not list a description limit. A vendor tabulation says about 30 and often hidden on mobile (https://socialrails.com/blog/facebook-ad-character-limits). [VERIFY: Reported]

### Where the layout cuts the text

- Mobile feed cuts primary text at about 125 characters and shows "See more". The cut depends on line height and screen width. A vendor says a small phone shows about 110, a large one about 135 and large accessibility fonts about 80. Desktop feed cuts around 200. Source: https://adplus.com/tools/ad-specs-validator/facebook-125-character-primary-text . [VERIFY: vendor only, test in your own preview]
- Vendor posts say about 1 percent of viewers tap "See more". [VERIFY: no primary study found]. The safe version: the first line is the ad for most people.
- Maximum primary text: vendors say 3,000 characters in the interface and 1,024 to 4,096 in the API. [VERIFY: vendor only]
- Instagram allows up to 30 hashtags per Meta's spec pages. An ad does not need them.
- With Advantage+ placements on, the shortest placement is the binding one. Instagram Reels is 44 on Meta's page. Write a 40 character version of the offer that survives alone.

## 8. Anatomy of the ad, Facebook mobile feed

The diagram shows where each slot lands on a phone. Numbers in square brackets point to the slot table under it. The copy is from a fictional brief (Brekke Ski Guides does not exist, the price and dates are made up).

```text
+-----------------------------------------------------+
| [page photo]  Brekke Ski Guides                     |
|               Sponsored                             |  [0] fixed, not editable
+-----------------------------------------------------+
| Six skiers per guide. Skins on at 09:15, first      |
| descent about 11:40, back at the car by 15:30.      |  [1] primary_text
| NOK 4,900 for the day.                              |      116 characters, fits before the cut
+-----------------------------------------------------+
|                                                     |
|              4:5 image, 1440 x 1800                 |
|                                                     |
|          Guided ski day, Brekke                     |  [2] image_line_1
|          Saturdays 9 Jan to 27 Feb                  |  [3] image_line_2
|          NOK 4,900                                  |  [4] image_line_3
|                                                     |
+-----------------------------------------------------+
| brekke-example.test                                 |  [5] display link (domain)
| Ski touring day, NOK 4,900            [ Book now ]  |  [6] headline, [7] CTA
| Guide and beacon included                           |  [8] description
+-----------------------------------------------------+
| Like        Comment        Share                    |
+-----------------------------------------------------+
```

| Ref | Slot | What the reader does with it | Budget |
|---|---|---|---|
| 0 | page name, Sponsored label | Fixed by Meta | none |
| 1 | primary_text | Everyone sees the first line. Only people who tap "See more" read the rest. | 125 visible (Meta recommends 50-150) |
| 2 to 4 | image_line_1 to 3 | Seen first, often the only thing read. Says what, when, how much. | 25, 30, 20 (adquill heuristic) |
| 5 | display link | Domain only, set in Ads Manager | none |
| 6 | headline | Repeats the offer in a few words | 27 (Meta recommendation) |
| 7 | CTA button | Always shown on link ads when the objective shows the footer | label from section 6 |
| 8 | description | Often hidden on mobile feed | about 30 [VERIFY: Reported] |

Sources for the layout: Meta's feed pages (section 2) for ratio and headline, and the vendor layout guides https://blog.adnabu.com/facebook-ads/facebook-ad-specs/ and https://insights.vaizle.com/anatomy-of-a-facebook-ad/ . [VERIFY: layout details such as description visibility are vendor reports, confirm in Ads Manager mobile preview]

What happens when the primary text is longer than the cut:

```text
| Six skiers per guide. Skins on at 09:15, first      |
| descent about 11:40, back at the car by 15:30. N... |  <- cut near 125 characters
| See more                                            |
```

Rule that follows: the price, the product and the action sit inside the first 125 characters. Anything after the cut adds story. It is never the only place a price or a date appears.

## 9. Anatomy of the ad, Instagram feed

The headline field exists on Meta's page. Vendor guides report that single-image Instagram feed ads do not render it. So the image carries the price and the dates, and the CTA bar carries the action.

```text
+-----------------------------------------------------+
| [profile photo] brekkeskiguides      Sponsored      |  [0] fixed
+-----------------------------------------------------+
|                                                     |
|              4:5 image, 1440 x 1800                 |
|                                                     |
|          Guided ski day, Brekke                     |  [1] image_line_1
|          Saturdays 9 Jan to 27 Feb                  |  [2] image_line_2
|          NOK 4,900                                  |  [3] image_line_3
|                                                     |
+-----------------------------------------------------+
| Book now                                         >  |  [4] CTA bar, full width
+-----------------------------------------------------+
| Like    Comment    Share                      Save  |
| brekkeskiguides Six skiers per guide. Skins on at   |  [5] primary_text starts after
| 09:15, first descent about 11:40, back at the... more |     the account name
+-----------------------------------------------------+
```

| Ref | Slot | Note | Budget |
|---|---|---|---|
| 1 to 3 | image lines | Must carry what, when and how much, because the headline may not show | 25, 30, 20 (adquill heuristic) |
| 4 | CTA bar | Label from the 27 Instagram labels in section 6. Always shown. | label |
| 5 | primary_text | Starts after the account name, so the account name eats part of the visible budget. The first words matter most. | 125 visible per Meta's field |
| none | headline | Field accepts up to 40. Reported as not displayed on single-image feed ads. | 40 field. [VERIFY in Ads Manager preview] |
| none | hashtags | Up to 30 allowed. Skip them. | not needed |

Sources: https://www.facebook.com/business/ads-guide/update/image/instagram-feed/link-clicks (field limits, verified 2026-10-06), https://blog.adnabu.com/facebook-ads/facebook-ad-specs/ and https://insights.vaizle.com/anatomy-of-a-facebook-ad/ (layout, Vendor). [VERIFY: where the headline renders on Instagram feed single-image ads. Meta's page lists the field and does not say where it shows.]

Because Advantage+ placements show the same ad on both surfaces, write the headline so the ad still works if only one of the two slots is visible. The image lines carry the full offer. The headline repeats the price. The description adds one extra fact.

## 10. Character budgets per slot

These are the budgets adquill uses in its output tables. The linter checks them when run with --slot.

| Slot | Budget | Where the number comes from | Status |
|---|---|---|---|
| image_line_1 (what) | 25 | adquill heuristic for one line at large type on a 375 px wide phone preview | heuristic |
| image_line_2 (when) | 30 | adquill heuristic | heuristic |
| image_line_3 (how much) | 20 | adquill heuristic. "NOK 4,900" is 9 characters, with room for "from" or "per person". | heuristic |
| primary_text | 125 visible before "See more" | Meta page (Instagram Feed 125, Facebook Feed 50-150 recommended) and the mobile cut | cut about 125, [VERIFY: 110 to 135 by device, vendor figure] |
| headline | 27 (Facebook feed) | https://www.facebook.com/business/ads-guide/update/image/facebook-feed/link-clicks | verified 2026-10-06 |
| headline (Instagram field) | up to 40, [VERIFY: not shown on single image feed ads] | https://www.facebook.com/business/ads-guide/update/image/instagram-feed/link-clicks | field verified 2026-10-06 |
| description | 30 | https://socialrails.com/blog/facebook-ad-character-limits | [VERIFY: Reported, often hidden on mobile] |
| cta | a label from section 6 | Meta feed pages | verified 2026-10-06 |
| reels_line | 40 | adquill heuristic for the tightest placement. Instagram Reels primary text is 44 on Meta's page. | heuristic, 44 verified 2026-10-06 |

Rules for counting and using the budgets:

- Count the real string with a program, including spaces and the thousands comma in "NOK 4,900". Show the count next to the text.
- Put price, product and action inside the first 125 characters of primary text.
- No sentence appears in two slots. The headline may repeat the price. It may not repeat a sentence from the primary text.
- The on-image block says what, when, how much. Three lines. Price in the heaviest weight, the date line second, the name third. Readable on a 375 px wide preview. If it is not, the type is too small.
- The designer or a layout tool puts the text on the image. An image generator never renders it, because generators garble characters and can invent details.

Worked example, fictional brief (Brekke Ski Guides, made-up price and dates, Saturdays checked: 9 Jan 2027 and 27 Feb 2027 are both Saturdays).

| Slot | Text | Count | Budget |
|---|---|---|---|
| image_line_1 | Guided ski day, Brekke | 22 | 25 |
| image_line_2 | Saturdays 9 Jan to 27 Feb | 25 | 30 |
| image_line_3 | NOK 4,900 | 9 | 20 |
| primary_text | Six skiers per guide. Skins on at 09:15, first descent about 11:40, back at the car by 15:30. NOK 4,900 for the day. | 116 | 125 |
| headline | Ski touring day, NOK 4,900 | 26 | 27 |
| description | Guide and beacon included | 25 | 30 |
| cta | Book now | label | label |
| reels_line | Ski touring day. NOK 4,900. | 27 | 40 |

Why it works: the three facts a thumb-scroller needs sit on the image. The primary text gives a reason to trust the day (six per guide, real times). The headline repeats the price for the surface where the description hides. Nothing promises snow or a result.

## 11. Delivery mechanics: official and vendor lore

Tag every delivery claim in output with one of official, reported or vendor. Never write a vendor rule as if Meta said it.

### What is official

| Claim | Source | Status |
|---|---|---|
| Andromeda is the retrieval stage of Meta's ad system. It picks a few thousand candidates from tens of millions. Post of 2 December 2024. | https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/ | verified 2026-10-06 |
| The same post says the system is expected to move to an autoregressive loss that "delivers a more diverse set of ad candidates". It names no similarity penalty and does not use the term "Entity ID". | same page | verified 2026-10-06 |
| Meta's Q2 2026 earnings call credits its recommender and ranking models plus better user understanding with "an 8.3% increase in ad clicks and a 15.7% uplift in conversions on Facebook". Quote it the way Meta said it. One vendor page ties the 15.7% to a single model. The transcript ties it to the combination. | https://s21.q4cdn.com/399680738/files/doc_financials/2026/q2/META-Q2-2026-Earnings-Call-Transcript.pdf | verified 2026-10-06. Meta's own marketing claim, not an independent test |
| December 2025 creative advice from Meta: give the system a broad portfolio of assets "that take more creative liberty across text, image, and video". Image generation "11% higher CTR and 7.6% higher CVR", text generation "3% higher CTR". Three Reels hook types: value promise, statement of intent, question or invitation. | https://www.socialmediatoday.com/news/meta-shares-tips-on-reels-hooks-creative-diversification-in-ads-and-threa/808182/ | Reported (17 December 2025). Meta's marketing figures, not independent tests. [VERIFY: trade press, no Meta page read] |
| Learning phase: Meta's help text recommends about 50 optimisation events after the last significant edit. An ad set is "learning limited" when it is unlikely to reach about 50 events in the week after the last significant edit. | https://www.facebook.com/business/help/942374239243867 and https://www.facebook.com/business/help/112167992830700/ | [VERIFY: page bodies did not load, wording is from Meta text shown in search results] |
| Detailed targeting exclusions were removed (developer blog, 21 January 2025). | https://developers.facebook.com/blog/post/2025/01/21/removal-of-detailed-targeting-exclusions/ | Reported via https://ppc.land/meta-removes-detailed-targeting-exclusions-for-ad-accounts/ . [VERIFY: the developer blog page was not read, and the lower cost per conversion figure of 22 to 22.6 percent differs by 0.6 points between two secondary sources] |
| A Creative diversity column (Low, Medium, High per ad set) appeared in Ads Manager on 26 August 2026. The interface labels it "estimated and in development". | https://www.marketingconcurrent.nl/en/blog/meta-ads-manager-introduces-creative-diversity-score-what-a-low-rating-really-means and https://commonthreadco.com/blogs/coachs-corner/meta-ads-changes-2026 | Reported. No link to cost or delivery is confirmed. Use it as a hint, not a target. [VERIFY: trade press, no Meta page read] |

### What is vendor lore

Every row below carries [VERIFY: no Meta source]. They are common in agency posts. Do not state them as Meta rules.

| Claim | Where it circulates | Status |
|---|---|---|
| Meta assigns an "Entity ID" and collapses similar ads into one | Many agency blogs. One source calls it "an explanatory device" and says it is not an official Meta term (https://adsuploader.com/blog/meta-andromeda) | The idea is plausible. The label is not Meta's. [VERIFY: not in Meta documentation] |
| A "similarity score" above 60 percent suppresses delivery, under 40 percent is good | Agency guides. Traced to one London agency guide, not to Meta (https://nikhil.pro/meta-ads-creative-similarity-explained/) | [VERIFY: no Meta source] |
| One ad set with 25 varied creatives gives 17 percent more conversions at 16 percent lower cost than five ad sets of five | Agency post summaries | [VERIFY: no study or method found] |
| Brands testing 20 or more new ads a month get 65 percent higher return on ad spend than brands under 10 | Same | [VERIFY: no study or method found] |
| Run 8 to 20 distinct concepts, refresh every 2 to 3 weeks | Many | Agrees with Meta's "broad portfolio" advice in direction only. The numbers are vendor. [VERIFY] |
| About 70 percent of a creative must look different | One agency | [VERIFY: no source] |
| Static ads fatigue after 20 to 30 days, video after 40 to 60 | Vendor blogs | [VERIFY: unsourced] |
| About 1 percent of viewers tap "See more" | Vendor posts | [VERIFY: no primary study] |
| 47 percent of campaign value comes in the first three seconds of a video | Facebook and Nielsen study of positive-lift campaigns, around 2015 (https://www.facebook.com/business/news/updated-features-for-video-ads) | Old and selected. Do not present it as a 2026 finding. |

What is safe to say: Meta says creative is the main lever it wants advertisers to pull, it ships a diversity indicator, and it has removed several hand controls. The exact penalty mechanism is not public.

### What this means for the writing

- Write several different ads, not one ad ten ways. A concept differs in the first-second hook, the scene, the person and the offer angle. A new headline or a recoloured price pill is not a new concept.
- A small advertiser can start with 3 to 5 clearly different creatives per ad set. That range is a vendor suggestion (https://www.superads.ai/blog/creative-diversity-in-ads). [VERIFY: Vendor]. adquill asks for two to four angles, which sits inside it.
- Learning phase for a low-volume advertiser: a business that books a few dozen guests a season will not see 50 purchases a week per ad set. Options, as practitioner heuristics: optimise for an earlier event that reaches volume (landing page view, view content, add to cart, initiate checkout) and read bookings from the booking system, keep fewer ad sets so events pool, and avoid big edits mid-flight. [VERIFY: the right event depends on tracking quality and the booking flow. Meta's definition of "significant edit" did not load.]
- Hook rate (three-second views divided by impressions) is a buyer metric, not a Meta KPI name. Vendor ranges exist, such as a median of 20.9 percent in a June to August 2026 sample (https://www.biddyco.com/blog-posts/hook-rate-benchmarks-meta). [VERIFY: vendor, do not quote as a benchmark]

## 12. Advantage+ creative and text edits

Advantage+ creative can change what your ad says. For an ad with a price or a date, that is a policy risk and a trust risk, because the copy that runs may differ from the copy you approved.

### What can touch text

The list below is a vendor reference (31 enhancements, maintained by a tool vendor). Source: https://adsuploader.com/blog/advantage-plus-creative-enhancements . [VERIFY: Vendor, no Meta page read. Menu names change often.]

The feature names are quoted as labelled in that reference, so the table sits inside a lint ignore block.

<!-- adquill-lint: ignore-start -->

| Setting (as labelled) | What it does to text | For a price or date ad |
|---|---|---|
| Text improvements | Rewrites your copy or surfaces keywords from it | Off |
| Text generation | Writes new headline and primary text variants | Off |
| Enhance media text | Rewrites the overlay text on your image per viewer | Off |
| Image text rewriting | Reported: generates up to 8 variants of the headline text inside the image, keeping font, colours and layout | Off |
| Enhance CTA | Swaps the button message | Off |
| Show summaries | Adds an AI summary | Off |
| Translations | Translates the ad | Off unless you review each language |
| Catalog description option | Catalog ads only | Not used for static ads |

<!-- adquill-lint: ignore-end -->

### What is known about defaults and dates

- 27 July 2026: image text rewriting reported as on by default for eligible Advantage+ campaigns, with up to 8 variants of the headline text in the image. Sources: https://commonthreadco.com/blogs/coachs-corner/meta-advantage-plus-creative-image-text-rewriting-ecommerce-2026 , https://www.xwork.my/meta-advantage-creative-ad-image-text/ , and a first write-up at https://www.jonloomer.com/meta-rewrite-text-ad-images/ (it returned 403 to the research pass). None of them cites a Meta announcement page. [VERIFY: Meta's own wording and the default state per campaign type]
- Some enhancements (the catalog description option, image touch-ups, relevant comments) are reported as on by default through the API. Marketing API v22.0 (January 2025) reportedly no longer lets an advertiser opt in or out of the single standard enhancements bundle. [VERIFY: vendor reference]
- Price risk: one write-up warns that an on-image line such as a one-time fee could be rewritten into something generic or into something that changes the implied price, and advises disabling the swap on any image with a price point, or reviewing every variant. Source: https://www.xwork.my/meta-advantage-creative-ad-image-text/ . [VERIFY: Vendor write-up]
- Restricted Words was added on 2 September 2025. Meta's wording, as quoted by the trade press: "Specify if there are certain words or phrases you don't want to appear in AI-generated text options and we'll exclude them in Advantage+ Creative text generation". Reported guardrail limits: Meta "still occasionally slips in an emoji". Source: https://www.socialmediatoday.com/news/meta-adds-restricted-words-ai-ad-copy-generation/759084/ . Status: Reported. [VERIFY: trade press, no Meta page read]
- Buyer-reported tests say Text improvements off beats on for text-heavy direct response, because rewritten hooks drift from the approved angle. [VERIFY: anecdotal, https://commonthreadco.com and similar]. Meta's own figure for text generation is a 3 percent higher CTR (December 2025, Reported, see section 11).

### How to switch them off for a price or date ad

Menu names and positions change. The controls below are where vendor guides place them. Look for the same words in your Ads Manager. [VERIFY: Vendor guidance, confirm against your own Ads Manager before relying on this]

1. Open the ad, go to the Ad setup or Creative section, and find the Advantage+ creative (or "Creative features") block. Switch off every text-touching option listed above for that ad.
2. For many ads at once use bulk edit, and check the account-level "Creative features" in Advertising Settings so a new ad does not inherit the default.
3. In the Branding section under Identity (logo, fonts, colours, tone) set the Restricted Words list. Add the words you never want in generated text: superlatives, outcome promises, urgency words and any price word you did not write.
4. Open the preview for every placement and every variant. Read each price and date against the fact ledger.
5. After the ad goes live, open it from the Facebook page or the Ad Library and compare the running text with the approved text. If anything differs, pause and fix before spending more.

adquill prints this checklist in the "Before you publish" section of every output that has a price or a date on the image.

## 13. Placements that changed in the last 12 months

Window: roughly October 2025 to 2026-10-06. Items just outside it are marked background. Every row is Reported or Vendor, so every row carries a [VERIFY] note. No Meta page was read for this table.

| Date | Change | Source | Status |
|---|---|---|---|
| 2 September 2025 (background) | Restricted Words setting for AI-generated text in Advantage+ creative | https://www.socialmediatoday.com/news/meta-adds-restricted-words-ai-ad-copy-generation/759084/ | Reported. [VERIFY: trade press, no Meta page read] |
| 11 December 2025 | Creator tools for partnership ads expanded. Meta published "19% lower CPAs and 13% higher click through rates on average" for campaigns that add partnership ads | https://www.marketingdive.com/news/meta-streamlines-brands-creator-partnerships-with-ai-powered-updates/807629/ | Reported. Meta marketing its own product. [VERIFY: trade press, no Meta page read] |
| 17 December 2025 | Meta guidance on Reels hooks and creative portfolios | https://www.socialmediatoday.com/news/meta-shares-tips-on-reels-hooks-creative-diversification-in-ads-and-threa/808182/ | Reported. [VERIFY: trade press, no Meta page read] |
| January 2026 | Less personalised ads choice rolled out to all EEA users | https://ppc.land/metas-2026-dma-report-reveals-whatsapp-ads-a-eu200m-fine-and-a-defiant-stance-on-personalized-advertising/ | Reported. [VERIFY: Norway scope and effect on delivery] |
| 15 January 2026 | Reported final cutoff for consolidated detailed targeting interests | https://www.wickedreports.com/blog/meta-removes-detailed-targeting-exclusions-from-ad-campaigns | [VERIFY: vendor sources only] |
| March 2026 | Flexible format reportedly folded into a "Flexible media" toggle inside Advantage+ creative | https://adsuploader.com/blog/meta-flexible-ads | [VERIFY: no Meta page read] |
| 10 March 2026 | Location fees announced: UK 2%, France, Italy and Spain 3% each, Austria and Turkey 5% each. Effective May 2026, billed from 1 July 2026, on top of ad spend. Norway not listed in anything read | https://www.mediapost.com/publications/article/413378/meta-passes-eu-digital-services-tax-to-advertisers.html | Reported. If you target those markets, budget 2% to 5% extra. [VERIFY: trade press, no Meta page read] |
| 23 June 2026 | Advantage+ text generation reportedly extended to image text. A brand memory feature in test | https://adsuploader.com/blog/advantage-plus-creative-enhancements | [VERIFY: vendor reference] |
| 27 July 2026 | Image text rewriting reported as default on in eligible Advantage+ campaigns | see section 12 | [VERIFY: no Meta page read] |
| 19 to 21 August 2026 | Placement, platform, device and operating system exclusions removed from ad sets for Sales and Leads campaigns. Account-level placement controls and value rules remain | https://www.socialsamosa.com/news-2/meta-remove-placement-controls-from-ad-sets-12401398 and https://www.relevantaudience.com/facebook-ads/meta-removes-option-to-exclude-ad-placements/ | Reported. One summary says it was not a formal announcement and reached only some advertisers. [VERIFY: scope by objective] |
| 26 August 2026 | Creative diversity column in Ads Manager | see section 11 | Reported. [VERIFY: trade press, no Meta page read] |
| 27 August 2026 | Messenger Stories removed as an ad placement | https://commonthreadco.com/blogs/coachs-corner/meta-ads-changes-2026 | Reported. [VERIFY: single vendor changelog, no Meta page read] |
| September 2026 | One changelog lists a Creator Marketing Hub (15 September), Instagram live video ads (29 September), Threads ads without an Instagram presence (22 September) and exclusion-only custom audiences (10 August) | https://commonthreadco.com/blogs/coachs-corner/meta-ads-changes-2026 | [VERIFY: single vendor changelog] |

Consequence for the writing: with placement exclusions gone in some campaign types, every ad must survive every placement. That means a 4:5 file with centred content for feed, a separate 9:16 file for Reels and Stories, and a 40 character line that works alone. Placement asset customisation (assign a 4:5 file to Feed and a 9:16 file to Stories and Reels inside one ad) remains the way to control what each surface shows. Without it a 1:1 file is letterboxed or auto-cropped into 9:16. Source: https://withblip.com/blog/meta-ads-placement-customization-guide/ . [VERIFY: Vendor guide, Meta help page not read]

## 14. Re-verify routine

Meta changes these numbers often. Before relying on this file:

1. Check the date at the top. If today is more than 90 days after 2026-10-06, treat every row as stale and re-check the Meta Ads Guide pages in section 15.
2. Open Ads Manager, build a draft ad and read the preview on mobile Facebook and mobile Instagram. Confirm the truncation point, whether the Instagram headline shows, and the button list for your objective.
3. Read the live Advantage+ creative settings for the ad. Do not trust a default.
4. Re-run any [VERIFY] row that your ad depends on. If it stays open, say so in the output.

## 15. Sources

Meta pages (read, verified 2026-10-06):

- https://www.facebook.com/business/ads-guide/update/image/facebook-feed/link-clicks
- https://www.facebook.com/business/ads-guide/update/image/instagram-feed/link-clicks
- https://www.facebook.com/business/ads-guide/update/video/facebook-feed/link-clicks
- https://www.facebook.com/business/ads-guide/update/video/instagram-feed/link-clicks
- https://www.facebook.com/business/ads-guide/update/video/instagram-reels/link-clicks
- https://www.facebook.com/business/ads-guide/update/carousel/facebook-feed/link-clicks
- https://www.facebook.com/business/ads-guide/update/carousel/instagram-feed/link-clicks
- https://www.facebook.com/business/ads-guide/update/collection
- https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/
- https://s21.q4cdn.com/399680738/files/doc_financials/2026/q2/META-Q2-2026-Earnings-Call-Transcript.pdf
- https://developers.facebook.com/blog/post/2025/01/21/removal-of-detailed-targeting-exclusions/

Trade press and vendor pages (Reported or Vendor, see the row tags):

- https://www.socialmediatoday.com/news/meta-shares-tips-on-reels-hooks-creative-diversification-in-ads-and-threa/808182/
- https://www.socialmediatoday.com/news/meta-adds-restricted-words-ai-ad-copy-generation/759084/
- https://www.marketingdive.com/news/meta-streamlines-brands-creator-partnerships-with-ai-powered-updates/807629/
- https://www.mediapost.com/publications/article/413378/meta-passes-eu-digital-services-tax-to-advertisers.html
- https://ppc.land/meta-removes-detailed-targeting-exclusions-for-ad-accounts/
- https://ppc.land/metas-2026-dma-report-reveals-whatsapp-ads-a-eu200m-fine-and-a-defiant-stance-on-personalized-advertising/
- https://commonthreadco.com/blogs/coachs-corner/meta-ads-changes-2026
- https://commonthreadco.com/blogs/coachs-corner/meta-advantage-plus-creative-image-text-rewriting-ecommerce-2026
- https://www.marketingconcurrent.nl/en/blog/meta-ads-manager-introduces-creative-diversity-score-what-a-low-rating-really-means
- https://www.socialsamosa.com/news-2/meta-remove-placement-controls-from-ad-sets-12401398
- https://www.relevantaudience.com/facebook-ads/meta-removes-option-to-exclude-ad-placements/
- https://www.xwork.my/meta-advantage-creative-ad-image-text/
- https://www.jonloomer.com/meta-rewrite-text-ad-images/
- https://www.jonloomer.com/flexible-ad-format/
- https://metricool.com/flexible-ads-meta/
- https://adsuploader.com/blog/advantage-plus-creative-enhancements
- https://adsuploader.com/blog/meta-ads-safe-zones
- https://adsuploader.com/blog/meta-ad-copy-specs
- https://adsuploader.com/blog/meta-flexible-ads
- https://adsuploader.com/blog/meta-andromeda
- https://socialrails.com/blog/facebook-ad-character-limits
- https://adplus.com/tools/ad-specs-validator/facebook-125-character-primary-text
- https://blog.adnabu.com/facebook-ads/facebook-ad-specs/
- https://insights.vaizle.com/anatomy-of-a-facebook-ad/
- https://influencermarketinghub.com/instagram-image-sizes/
- https://nikhil.pro/meta-ads-creative-similarity-explained/
- https://www.superads.ai/blog/creative-diversity-in-ads
- https://www.biddyco.com/blog-posts/hook-rate-benchmarks-meta
- https://withblip.com/blog/meta-ads-placement-customization-guide/
- https://www.wickedreports.com/blog/meta-removes-detailed-targeting-exclusions-from-ad-campaigns
- https://www.facebook.com/business/news/updated-features-for-video-ads
- https://www.facebook.com/business/help/942374239243867
- https://www.facebook.com/business/help/112167992830700/
