# Meta and X advertising: formats, specs, policy, delivery and creative practice (as of 6 October 2026)

Research notes for adwright (open source Claude Code skill for Meta and X ads) and the Outdoor Norway client job (Voss, guided ski trips, NOK 1,948 day tour to NOK 42,126 for 9 days).

## 0. How to read these notes

Evidence tiers used throughout:

| Tag | Meaning |
|---|---|
| Official | Read on a Meta, X or primary-company page, or in a primary document (earnings transcript, regulator page). |
| Reported | Trade press or an established practitioner quoting or describing the platform. Cross-checked where I could. |
| Vendor | Agency, tool or blog claim with no primary source behind it. Treat as hypothesis. |
| [VERIFY: reason] | Number or claim I could not confirm. Do not ship it in the skill as fact. |

What I could not reach (stated plainly):

- All business.x.com and help.x.com pages returned HTTP 402 or 403 to my fetcher. X numbers below come from X's API docs (docs.x.com) and from secondary spec sheets. They disagree in places, and I flag each case.
- Meta's Advertising Standards "misleading claims" page returned 404. I could read the standards index, the personal attributes page, the violent and graphic content page and the prohibited commercial practices page. Misleading-claims specifics come from vendor write-ups and are tagged.
- The Meta Business Help Center pages on the learning phase returned only their titles. I rely on the text Meta's own pages show in search results.
- WordStream's 2025 Facebook benchmarks page returned 403. I use a secondary page that tabulates it.
- Meta's Stories ad spec pages returned 404. Stories numbers come from the Reels spec page (official) plus secondary guides.
- I did not find a source for star counts, and none are needed here.

Everything fetched was treated as untrusted data. No fetched page gave instructions that changed this work.

---

## 1. The short version (ten things the skill must know)

1. Meta's static image feed spec is 4:5 at 1440 x 1800 (minimum 1080 x 1350 is what most guides use, official minimum is 600 x 750 on Facebook, 500 px wide on Instagram), JPG or PNG, 30 MB max. This is the workhorse for the Outdoor Norway job. Source: Meta Ads Guide pages, section 2.
2. Meta's text limits are recommendations, not hard caps. The only hard behaviour that matters is truncation. About 125 characters of primary text show on mobile feed before "See more". Official Facebook feed guidance says primary text 50 to 150 characters, headline 27. Source: Meta Ads Guide, section 3.
3. Instagram feed single-image ads reportedly do not show the headline at all. The CTA bar and the primary text do the work. This is Vendor-level and must be checked in Ads Manager preview. Section 7.
4. 9:16 placements (Reels, Stories) share one safe zone on Meta's Reels spec page: keep 14% of the top, 35% of the bottom and 6% of each side free. On a 1080 x 1920 canvas that is 269 px, 672 px and 65 px. Section 2.
5. Andromeda is real and official (Meta engineering blog, 2 December 2024). The famous "Entity ID", "60% similarity penalty" and "run 8 to 20 concepts" rules are not in that post. They are vendor lore. What Meta itself has said (December 2025) is: give the system a broad portfolio of creative. Meta also shipped a "Creative diversity" column in Ads Manager on 26 August 2026, labelled "estimated and in development". Section 4.
6. Advantage+ creative can now rewrite the headline text inside your image by default (reported from 27 July 2026). For a price-on-image ad this is a real risk. Turn it off per ad. Section 4.4.
7. Meta removed placement exclusions for Sales and Leads campaigns in late August 2026 and removed Messenger Stories as a placement on 27 August 2026. Write every ad to survive every placement. Section 4.6.
8. Meta policy risk for tour operators is mostly about three things: "you" plus a personal attribute, price or offer mismatch with the landing page, and claims nobody can guarantee (snow, weather, "best"). Section 5.
9. Norway adds its own layer: price rules, labelling of paid creator content, and labelling of retouched people in ads. Section 5.5.
10. X is a secondary channel for this client. Norway ad reach on X is about 1.0 million people (DataReportal, October 2025) against about 3.05 million on Facebook and 2.65 million on Instagram. X's own ad platform was rebuilt from 30 April 2026. CPMs are lower, direct-response returns are reported as weaker. Section 8.

---

## 2. Meta formats and specifications

All "Official" figures in this section were read from Meta's Ads Guide pages (facebook.com/business/ads-guide/update/...) during this research pass (before 6 October 2026). Meta does not show every number for every objective, so I name the page.

### 2.1 Single image

| Placement | Ratio | Recommended resolution | Minimums | File | Max size | Tolerance | Source |
|---|---|---|---|---|---|---|---|
| Facebook Feed | 4:5 | 1440 x 1800 | 600 px wide, 750 px high | JPG, PNG | 30 MB | 3% | https://www.facebook.com/business/ads-guide/update/image/facebook-feed/link-clicks |
| Instagram Feed | 4:5 | 1440 x 1800 | 500 px wide. Ratio range from 4:5 (400 x 500) to 1.91:1 (191 x 100) | JPG, PNG | 30 MB | 1% | https://www.facebook.com/business/ads-guide/update/image/instagram-feed/link-clicks |
| Stories and Reels (image used as 9:16) | 9:16 | 1080 x 1920 is the working standard. Reels spec page lists 1440 x 2560 for video | see Reels row below | JPG, PNG | 30 MB | n/a | secondary guides, [VERIFY: Meta's Stories image spec page returned 404] |

Notes:

- Meta's Facebook feed page says "use movement and sound to show unique features". The official guidance is pushing video, even on the image page.
- Instagram's profile grid changed to a taller crop in January 2025. Reported sources say the grid now crops to 3:4 while the feed still shows up to 4:5. Ads live in the feed, not the grid, but an organic post that later appears on the grid will be cropped. My own arithmetic: a 1080 x 1350 (4:5) image cropped to 3:4 loses about 34 px on each side. Keep names, prices and dates at least 40 px in from the left and right edges. [VERIFY: grid crop behaviour, reported by https://influencermarketinghub.com/instagram-image-sizes/ and similar]

### 2.2 Video, including Reels

| Placement | Ratio | Resolution | Length | Max size | Min size | Text fields | Source |
|---|---|---|---|---|---|---|---|
| Facebook Feed video | 4:5 | 1440 x 1800 | 1 second to 241 minutes | 4 GB | 120 px | Primary 50-150, headline 27 | https://www.facebook.com/business/ads-guide/update/video/facebook-feed/link-clicks |
| Instagram Feed video | 9:16 listed on the Meta page | 1080 x 1920 | 1 second to 60 minutes | 4 GB | 250 px wide | Primary 125, 30 hashtags max | https://www.facebook.com/business/ads-guide/update/video/instagram-feed/link-clicks |
| Instagram Reels | 9:16 | 1440 x 2560 | up to 15 minutes | 4 GB | 250 px wide under 30 s, 500 px wide at 30 s or longer | Primary text 44 characters | https://www.facebook.com/business/ads-guide/update/video/instagram-reels/link-clicks |

Common to all Meta video pages I read: MP4 or MOV (GIF also accepted on feed), H.264, square pixels, fixed frame rate, progressive scan, stereo AAC at 128 kbps or higher, no edit lists. Captions and sound are listed as "optional, but recommended" (feed) or "optional but strongly recommended" (Reels).

Conflict to note: secondary sources give Instagram Reels primary text as 44 (awareness) or 72 (traffic) and Facebook Reels as 40 primary and 55 headline. The 44 figure is on Meta's page. Treat 72 and 40/55 as [VERIFY: only in https://adsuploader.com/blog/meta-ad-copy-specs and https://socialrails.com/blog/facebook-ad-character-limits].

Mobile footer note from Meta: on Facebook Feed mobile, when the objective is Awareness or a goal such as 2-second views, impressions or engagement, the headline, description and CTA footer do not display. Pick the objective with that in mind. Source: Facebook Feed video spec page above.

### 2.3 Safe zones for 9:16 (Reels and Stories)

Official (Meta Reels spec page): leave at least 14% of the top, 35% of the bottom and 6% on each side free of text, logos and critical elements.

| Canvas | Top 14% | Bottom 35% | Each side 6% | Centre working band (my arithmetic) |
|---|---|---|---|---|
| 1080 x 1920 | 269 px | 672 px | 65 px | about 950 px wide x 979 px tall |
| 1440 x 2560 | 358 px | 896 px | 86 px | about 1268 px wide x 1306 px tall |

Reported: Stories sources quote 14% top and 20% bottom (that 20% figure is the link sticker or CTA clearance, not the full interface), and one guide says Stories and Reels now share the same 9:16 numbers, covering Facebook in-stream reels too. Source: https://adsuploader.com/blog/meta-ads-safe-zones (Vendor, cites a Meta help diagram I could not open). Use the stricter Reels numbers everywhere. They are safe for Stories too.

Feed safe zone: Meta publishes none that I could read. One vendor says 250 px top and bottom for 4:5 and 100 px on all edges for 1:1 [VERIFY: vendor-only]. My working rule for the skill: 5% inner margin on all sides for 4:5 and 1:1 feed images, and treat the left and right 40 px as unsafe because of the Instagram crop.

### 2.4 Carousel

| Placement | Cards | Ratio | Resolution | Text | Source |
|---|---|---|---|---|---|
| Facebook Feed | 2 to 10 | 1:1 | at least 1080 x 1080 | Primary 80, headline 20, description 18 | https://www.facebook.com/business/ads-guide/update/carousel/facebook-feed/link-clicks |
| Instagram Feed | 2 to 10 | 4:5 for image-only carousels, 1:1 for any carousel with video | at least 1080 x 1080 | Primary 125, 30 hashtags | https://www.facebook.com/business/ads-guide/update/carousel/instagram-feed/link-clicks |

Also official: card video 1 second to 240 minutes on Facebook and 1 second to 2 minutes on Instagram. Meta may apply "custom positioning" to carousel cards, meaning card order can vary per person while the overall sequence stays consistent.

Practical read: the 20 character carousel headline is tight. "Ski day, NOK 1,948" is 18 characters.

### 2.5 Collection and Advantage+ catalog

- Collection (Facebook Feed, Awareness page): cover image or video at 1.91:1 to 1:1, at least 1080 x 1080, followed by 3 product images. It opens an Instant Experience (full-screen landing). Primary 125, headline 40. Source: https://www.facebook.com/business/ads-guide/update/collection
- Collection and Advantage+ catalog ads need a product catalog. For nine tours with long booking pages, a carousel with one card per tour does the same job with less setup. I did not find a source that confirms a tour or activity catalog type is supported for Advantage+ catalog travel ads. [VERIFY: whether "destination" or "experience" catalog types suit guided tours]

### 2.6 Flexible format and Advantage+ creative

- Flexible ads let one ad hold up to 10 images or videos, and Meta picks the form (single, video, carousel) per viewer. Source: https://metricool.com/flexible-ads-meta/ and https://www.jonloomer.com/flexible-ad-format/ (Vendor/Reported).
- Reported: from March 2026 Meta removed the top-level "Flexible" option and moved the behaviour into a "Flexible media" toggle inside Advantage+ creative. [VERIFY: reported by https://adsuploader.com/blog/meta-flexible-ads and the Advantage+ reference, no Meta page read]

### 2.7 Call to action buttons (exact lists from Meta)

Facebook Feed (image, link-clicks page), 31 labels:

Download, Get promotions, Get updates, Watch live video, Get Tickets, Remind Me, Visit profile, Try in Camera, Apply now, Subscribe, Check Availability, Get offer, Get quote, Learn more, Order now, Contact us, Listen now, Send WhatsApp message, Buy tickets, Visit Instagram profile, Sign up, See details, Book now, Send message, Watch more, Shop now, See menu, Request time, Get access, Call now, Get showtimes.

Instagram Feed (image, link-clicks page), 27 labels. Same list minus Watch live video, Get Tickets, Visit profile and Get access.

Meta's own caveat: "not all calls to action may be available to you, depending on your industry". The list also varies by objective and conversion location (website, Messenger, WhatsApp, call).

Subset that makes sense for a tour operator:

| Button | Use it when | Note |
|---|---|---|
| Book now | Landing page lets you book and pay or hold a spot | Strongest commitment. Matches a booking page. |
| Check Availability | Landing page shows dates and spaces | Lower friction than Book now for a NOK 42,126 trip. Available on both Facebook and Instagram feed. |
| Learn more | Landing page is an itinerary or tour page | Safe default, weakest signal. |
| Get offer | A real, dated offer exists (for example an early booking price) | Only with an actual offer on the landing page. |
| Get quote | Custom group or multi-day enquiry | Fits the 9 day trip better than the day tour. |
| Request time | Call back or consultation | Fits a sales-assisted trip. |
| Contact us, Send message, Send WhatsApp message | Pre-sale questions | Needs someone answering quickly. |
| Sign up | Newsletter or season alert list | Not a booking. |
| See details | Neutral | Rarely better than Learn more. |
| Call now | Phone-led sales | Mobile only. |

Not relevant: See menu, Shop now, Order now, Download, Listen now, Get showtimes, Try in Camera.

### How adwright should use this

- Ship a `meta-specs.json` that carries the tables above with a `source` and `retrieved` field per row, and a `confidence` field (official, reported, vendor).
- Default static output: one 4:5 file at 1440 x 1800, with a text-safe inner margin of 5%. Add a 9:16 file at 1080 x 1920 only when the user asks for Stories and Reels, and apply 14/35/6 margins.
- Offer CTA choice from the travel subset only. Default to Book now when the landing page has a booking widget, Check Availability when it shows dates, Learn more otherwise. Never suggest Get offer without a stated real offer.
- Never state a character "limit" as a hard cap. Use "recommended" and "truncates at about".

---

## 3. Text limits and truncation

### 3.1 What Meta states (official, Ads Guide)

| Placement | Primary text | Headline | Description | Source |
|---|---|---|---|---|
| Facebook Feed (image and video) | 50-150 characters | 27 | not shown on this page | facebook.com Ads Guide, feed pages above |
| Instagram Feed | 125 | 40 | none | https://www.facebook.com/business/ads-guide/update/image/instagram-feed/link-clicks |
| Instagram Reels | 44 | none | none | Reels spec page above |
| Facebook Feed carousel | 80 | 20 | 18 | carousel page above |
| Instagram carousel | 125 | not listed | none | carousel page above |
| Collection (Facebook Feed) | 125 | 40 | none | collection page above |

Secondary tabulation (Reported, "read from each placement page in July 2026"): Stories 125 / 40, Marketplace 125 / 40 / 30, Search results 125 / 40 / 30, In-stream video 125 / 40, Right column headline 40. Source: https://socialrails.com/blog/facebook-ad-character-limits

### 3.2 Truncation behaviour

- Meta's numbers are guidance. Ads Manager accepts far longer text. The practical limit is where the layout cuts it. Source: https://socialrails.com/blog/facebook-ad-character-limits (Reported) and https://adplus.com/tools/ad-specs-validator/facebook-125-character-primary-text (Vendor).
- Mobile feed cuts primary text at about 125 characters with "See more". Vendor detail: the cut depends on line height and screen width. A small iPhone shows about 110 characters, a large one about 135, and large accessibility fonts about 80. Desktop feed cuts around 200. [VERIFY: vendor only, test on your own preview]
- Claim that "about 1% of users tap See more" appears in vendor posts without a source. [VERIFY: no primary study found]. Use the safe version: the first line is the ad for most people.
- Primary text maximum: vendors say 3,000 characters in the UI and 1,024 to 4,096 in the API. [VERIFY: vendor only]
- Instagram allows up to 30 hashtags per Meta's spec pages. Ads do not need them.
- When you use Advantage+ placements, the shortest placement controls. Facebook Reels (40 character primary text per one vendor) and Instagram Reels (44 official) are the tightest. Write a 40 character version of the offer.

### How adwright should use this

- Budget copy in three tiers: a 40 character "Reels line", a 125 character "feed line" and an optional long body that only 1 in many readers sees.
- Put price, product and action inside the first 125 characters. The long body adds story, never the only appearance of price or dates.
- Count characters with the real string, including spaces and the thousands comma in "NOK 1,948". Report the count next to each variant.

---

## 4. Delivery mechanics in 2025 and 2026

### 4.1 What is official

- Andromeda: Meta Engineering blog, 2 December 2024. It is the retrieval stage of the ad system. It picks a few thousand candidates from tens of millions. Claims in the post: +6% recall improvement, +8% ads quality on selected segments, over 100x improvement in feature extraction latency and throughput, 3x end-to-end inference QPS, 10x inference efficiency. The post also says advertisers using Advantage+ creative saw a 22% ROAS increase and image generation gave +7% conversions. Source: https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/
- The only diversity statement in that post is forward-looking: the architecture is expected to move to an autoregressive loss that "delivers a more diverse set of ad candidates". It does not describe a similarity penalty and does not use the word "Entity ID".
- Meta Generative Recommender and GEM: Meta Q2 2026 earnings call transcript. Quote: Meta "introduced Meta Generative Recommender" and uses LLMs "to reason about ad content and user preferences together". Combined with the GEM ranking model and improved user understanding models, this "generated an 8.3% increase in ad clicks and a 15.7% uplift in conversions on Facebook". Early LLM pilots drove "a 1% increase in app event conversions on Instagram". Advantage+ reached over $75 billion annual run-rate. Over 9 million small businesses use at least one AI creative tool. Source: https://s21.q4cdn.com/399680738/files/doc_financials/2026/q2/META-Q2-2026-Earnings-Call-Transcript.pdf
  Caution: one vendor page attributes the 15.7% to the Generative Recommender alone. The transcript ties it to the combination of GEM and user understanding models. Quote it the way Meta said it.
- Creative advice from Meta (Reported, Social Media Today, 17 December 2025): provide multiple variations so the system can match creative to people; build "a broad portfolio of assets that take more creative liberty across text, image, and video"; Meta's figures are image generation "11% higher CTR and 7.6% higher CVR" and text generation "3% higher CTR"; for Reels hooks Meta names three types (value promise, statement of intent, question or invitation) and says music or voiceover in Reels campaigns shows "up to 13% higher incremental conversions". Source: https://www.socialmediatoday.com/news/meta-shares-tips-on-reels-hooks-creative-diversification-in-ads-and-threa/808182/ . Note these are Meta's marketing claims, not independent tests.
- Creative diversity rating: reported launch on 26 August 2026. Ads Manager scores each ad set Low, Medium or High for visual and thematic variety. It sits under Columns, Customize columns, Creative diversity. The interface label is "estimated and in development". Reports say many mixed-format ad sets still get Low, and no link to cost or delivery is confirmed. Sources: https://www.marketingconcurrent.nl/en/blog/meta-ads-manager-introduces-creative-diversity-score-what-a-low-rating-really-means and https://commonthreadco.com/blogs/coachs-corner/meta-ads-changes-2026 (Reported). Use it as a hint, not a target.
- Learning phase: Meta's help text (as shown in search results) says it recommends waiting until an ad set has about 50 optimisation events since the last significant edit, and an ad set is "learning limited" when it is unlikely to get around 50 events in the week after the last significant edit. Source: https://www.facebook.com/business/help/942374239243867 and https://www.facebook.com/business/help/112167992830700/ (page body not retrievable, titles only).
- Targeting: Meta's developer blog of 21 January 2025 announced removal of detailed targeting exclusions (as summarised by https://ppc.land/meta-removes-detailed-targeting-exclusions-for-ad-accounts/ , which cites https://developers.facebook.com/blog/post/2025/01/21/removal-of-detailed-targeting-exclusions/). Reported figures about 22% to 22.6% lower cost per conversion without exclusions come from Meta's stated testing as relayed by secondary sources. [VERIFY: exact figure, two secondary sources differ by 0.6 points]. Reported: interest consolidation with a final cutoff on 15 January 2026. [VERIFY: only vendor sources, e.g. https://www.wickedreports.com/blog/meta-removes-detailed-targeting-exclusions-from-ad-campaigns]

### 4.2 What is vendor lore (tag every one [VERIFY])

| Claim | Where it appears | Status |
|---|---|---|
| Meta assigns an "Entity ID" and collapses similar ads into one | Many agency blogs | One source states plainly that "Entity ID" is "an explanatory device ... rather than an official term Meta publishes" (https://adsuploader.com/blog/meta-andromeda). Concept is plausible, the label is not Meta's. [VERIFY: not in Meta documentation] |
| A "Creative Similarity Score" above 60% triggers suppression, under 40% is good | 303 London guide, Chatter Buzz, Segwise and others | I traced the 60% figure to 303 London's guide, not to Meta (https://nikhil.pro/meta-ads-creative-similarity-explained/). [VERIFY: no Meta source] |
| One ad set with 25 diverse creatives gives 17% more conversions at 16% lower cost than five ad sets with five each | Search summary of agency posts | [VERIFY: no study or method found] |
| Brands testing 20+ new ads a month get 65% higher ROAS than under 10 | Same | [VERIFY: no study or method found] |
| Run 8 to 20 distinct concepts, refresh every 2 to 3 weeks | Many | Consistent with Meta's "broad portfolio" advice in direction only. The numbers are vendor. [VERIFY] |
| "Around 70% of a creative must look different" | One agency | [VERIFY: no source] |
| Static ads fatigue after 20 to 30 days and video after 40 to 60 | Segwise-style blogs | [VERIFY: unsourced] |

What is safe to say: Meta states creative is the main lever it wants advertisers to pull, it ships a diversity indicator, and it removed several hand controls. The exact penalty mechanism is not public.

### 4.3 Concepts, ads and ad sets for a small budget

Meta states no number. Vendor ranges: 8 to 20 concepts for large accounts, 3 to 5 genuinely different creatives for small businesses (https://www.superads.ai/blog/creative-diversity-in-ads, Vendor). For the Outdoor Norway job the practical plan, labelled as my recommendation and not a Meta rule:

- One campaign per goal (for example "ski season bookings").
- One broad ad set per market (Norway, and one for each foreign market with a separate language).
- Four to eight ads in the ad set, each a different concept. A concept differs in the first-second hook, the scene (powder, group, guide, lodge, après), the person, and the offer angle (price, ease, local guide, group size). Changing only the headline or the colour of the price pill does not make a new concept.
- Same product can carry several concepts. The day tour at NOK 1,948 and the 9 day trip at NOK 42,126 are different buyers and should not share one ad.

### 4.4 Advantage+ creative and the risk of auto-edited text

Reference list (Vendor, maintained by a tool vendor, 31 enhancements): https://adsuploader.com/blog/advantage-plus-creative-enhancements

- Text-touching enhancements: Text improvements (rewrites or surfaces keywords from your copy), Text generation (new headline and primary text variants), Enhance media text (rewrites overlay text per viewer), Show summaries (AI summary), Enhance CTA (swaps CTA message), Translations, Dynamic description (catalog).
- Default behaviour: the reference says some items (for example Dynamic description, Image touch-ups, Relevant comments) are on by default via the API, and Marketing API v22.0 (January 2025) no longer lets you opt in or out of the single `standard_enhancements` bundle. [VERIFY: vendor reference]
- 27 July 2026: image text rewriting inside Advantage+ creative reported as on by default for eligible campaigns. It generates up to 8 variants of the headline text in your image while keeping font, colours and layout. Sources: https://commonthreadco.com/blogs/coachs-corner/meta-advantage-plus-creative-image-text-rewriting-ecommerce-2026 , https://www.xwork.my/meta-advantage-creative-ad-image-text/ , first documented by Jon Loomer (https://www.jonloomer.com/meta-rewrite-text-ad-images/, returned 403 to me). None of these cite a Meta announcement page. [VERIFY: Meta's own wording]
- Price risk: one write-up warns that a headline like "RM99 One-Time Fee" could be rewritten into something generic or something that changes the implied price, and says any image with a price point should have the swap disabled or each variant reviewed. Source: https://www.xwork.my/meta-advantage-creative-ad-image-text/
- Controls: per-ad toggles in the Advantage+ creative section; bulk edit; account-level "Creative features" in Advertising Settings; Branding section under Identity (logo, fonts, colours, tone) and the Restricted Words list. Restricted Words was added on 2 September 2025 with the quote "Specify if there are certain words or phrases you don't want to appear in AI-generated text options and we'll exclude them in Advantage+ Creative text generation" (https://www.socialmediatoday.com/news/meta-adds-restricted-words-ai-ad-copy-generation/759084/). The guardrails are reported as imperfect: Meta "still occasionally slips in an emoji".
- Buyer-reported tests say Text improvements off beats on for text-heavy direct response, because rewritten hooks drift from the approved angle. [VERIFY: anecdotal, https://commonthreadco.com and similar]. Meta's own number for text generation is a 3% higher CTR.

### 4.5 Learning phase for a low-volume advertiser

A tour operator will not get 50 purchases a week per ad set. Options, as practitioner heuristics:

- Optimise for an earlier event that does reach volume (landing page view, view content, add to cart, initiate checkout) and read bookings from the booking system. [VERIFY: choice depends on tracking quality, Conversions API and booking flow]
- Avoid significant edits mid-flight (budget swings, new audiences, swapping creative en masse). New ads in an ad set are a normal part of creative refresh but can re-enter learning. Meta's definition of "significant edit" was not retrievable. [VERIFY]
- Keep fewer ad sets so that events pool.

### 4.6 Placements: what changed

- Late August 2026: Meta began telling advertisers that "Excluding placements, platforms, devices and operating systems will no longer be available for your ad sets" for Sales and Leads campaigns. Account-level placement controls and value rules remain. Reported by https://www.socialsamosa.com/news-2/meta-remove-placement-controls-from-ad-sets-12401398 and https://www.relevantaudience.com/facebook-ads/meta-removes-option-to-exclude-ad-placements/ . One summary says it was not a formal Meta announcement and reached only some advertisers. [VERIFY: scope by objective]
- Messenger Stories removed as an ad placement on 27 August 2026 (same sources, plus https://commonthreadco.com/blogs/coachs-corner/meta-ads-changes-2026).
- Placement asset customisation (assign a 4:5 file to Feed and a 9:16 file to Stories and Reels inside one ad) remains the way to control what each surface shows. A 1:1 file is letterboxed or auto-cropped into 9:16 otherwise. Source: Vendor guides such as https://withblip.com/blog/meta-ads-placement-customization-guide/ . [VERIFY: Meta help page not read]

### 4.7 Reels first, hooks, sound, captions

- Meta says Reels hooks matter in the first few seconds and names three hook types (see 4.1). Source: Social Media Today above.
- The famous "47% of campaign value in the first three seconds, 74% in the first ten" is from a Facebook and Nielsen study of 173 Brand Effect studies, using only campaigns that showed positive lift, and published around 2015 (https://www.facebook.com/business/news/updated-features-for-video-ads and https://martech.org/even-brief-video-views-drive-brand-lift-facebook-nielsen-study-finds/). It is old and selected. Do not present it as a 2026 finding.
- On the same Meta page: captioned video ads increased view time by 12% on average in internal tests. Also from 2015-era text: design for sound off because many videos were "basically meaningless without sound". Date-stamp both when you use them.
- Sound-on rates in Reels (figures like 60% to 80% sound on) circulate in vendor posts with no study behind them. [VERIFY]
- Hook rate (3-second views divided by impressions) is a buyer metric, not a Meta official KPI name. Vendor ranges: median 20.9% across 479 top-spending videos in June to August 2026 (https://www.biddyco.com/blog-posts/hook-rate-benchmarks-meta), 25% to 35% as a solid target in older Motion material. [VERIFY: both vendor]

### 4.8 UGC and creators versus polished

- Meta's claim (11 December 2025, Marketing Dive): adding partnership ads to campaigns "delivers 19% lower CPAs and 13% higher click through rates on average", and "71% of consumers say they make a purchase within a couple of days after seeing creator content". Source: https://www.marketingdive.com/news/meta-streamlines-brands-creator-partnerships-with-ai-powered-updates/807629/ . This is Meta marketing its own product.
- Motion's 2026 benchmark (550,000 ads, 6,000 advertisers, about USD 1.3 billion, September 2025 to early January 2026, Facebook and Instagram): by hit rate the top asset types were text only 11.60%, product image with text 8.75% and UGC 7.56%; top hooks were Newness 11.37%, Sale announcement 11.35% and Price anchor 10.89%; only about 5% of ads spend at least 10 times their account median. Source: https://motionapp.com/thumbstop-pulse/creative-benchmarks-2026/ . This supports the on-image price block and says polished and UGC both win. Check Motion's definition of "hit rate" before quoting it. [VERIFY: definition]
- Static versus video: a Segwise analysis (67,000 ads, 100+ accounts) puts the median mix at 61% static and 39% video, and quotes ATTN Agency numbers (video CTR 1.9% vs static 1.1%, video CPA $48.20 vs static $34.50, video engagement 5.2% vs 1.4%). Source: https://segwise.ai/blog/static-video-ratio-meta-ads . These are secondhand figures. [VERIFY: ATTN source not opened]

### How adwright should use this

- Treat Andromeda as "write several different ads, not one ad ten ways". Make the skill output a concept set where each concept names its hook, scene, person and angle, and refuse to label two ads as different concepts if only the headline changes.
- Tag every delivery claim with official, reported or vendor in the skill's reference file. Never write "Meta penalises similarity above 60%" in output.
- Always output an "Advantage+ creative checklist" for ads with price or dates in the image: turn off Text improvements, Text generation, Enhance media text, image text rewriting and Enhance CTA; set Restricted Words; review the preview of every variant.
- Write each ad so it still works if the placement is not what you chose. That means 4:5 with centred content for feed, a separate 9:16 for Reels and Stories, and a 40 character line that survives alone.
- Include a hook library with Meta's three hook types plus a price-led hook and a date-led hook.

---

## 5. Policy

### 5.1 Meta Advertising Standards (official structure)

Index read: https://transparency.meta.com/policies/ad-standards/ . Sections relevant here:

- Unacceptable content: includes discriminatory practices, misinformation, locally illegal products or services, and others.
- Prohibited commercial practices: ads cannot "employ prohibited commercial practices - such as deceptive pricing, unauthorized endorsements, and guaranteed investment returns" to mislead for financial gain. Page: https://transparency.meta.com/policies/ad-standards/deceptive-content/prohibited-commercial-practices/
- Objectionable content: includes personal attributes, violent and graphic content, profanity, adult content.
- Violent and graphic content: "Ads must not contain shocking, sensational or excessively violent content." and "Advertisers can't run ads that include imagery that is shocking, gruesome, or otherwise sensational in nature." Page: https://transparency.meta.com/policies/ad-standards/objectionable-content/violent-graphic-content/ . The page text I read says nothing about extreme sports or stunts. [VERIFY: how reviewers treat crashes, avalanches or helicopter drops]
- Intellectual property: third-party infringement and use of Meta's own IP (brand resource guidelines).
- Additional requirements listed on the index: data use restrictions, targeting requirements (no discrimination), relevance requirements (ads must accurately represent offerings and match landing pages), branded content (use the branded content tool for third-party product features) and EU Digital Services Act (beneficiary and payer identification).
- Restricted goods: alcohol must target 18+ and follow local law. Relevant if an ad shows or mentions drinks at a lodge or après.

### 5.2 Personal attributes

Official text (https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/): "Ads must not contain content that asserts or implies personal attributes." Covered attributes include race, ethnicity, religion, age, sexual orientation, gender identity, disability, health status, financial situation, voting status, union membership, criminal record and names. Prohibited examples on the page: "Meet other black singles near you!", "Are you Christian?", "Meet other seniors", "Do you have diabetes?", "Billy Taylor, get this t-shirt". Allowed style examples: "Date Christian singles!".

Reported nuance: the trigger is "you" joined to a protected attribute, not the word "you" itself. "Book your trip" is fine. Source for the nuance: https://www.jonloomer.com/qvt/can-we-use-the-words-you-or-your/ (not opened, title only) and https://www.stackmatix.com/blog/meta-ads-personal-attributes-policy (Vendor). [VERIFY]

Applied to ski ads:

| Risky | Why | Safer |
|---|---|---|
| "Over 50 and still skiing?" | Age plus "you" | "Ski days for every age group" is still age-adjacent. Prefer "Ski Voss with a local guide." |
| "Are you a beginner who is scared of the slopes?" | Fear and ability framing, can read as health or condition | "First time off-piste? Local guides, small groups." (only if true) |
| "Single? Join our ski week" | Relationship status | "Ski week for solo travellers" [VERIFY: not on Meta's list but close] |
| "Your knee will thank you" | Health | Avoid |
| "Ski trip for families with disabled kids" | Disability | Avoid in copy and in targeting |
| "Rich enough to ski Norway?" | Financial situation | Avoid |

### 5.3 Misleading claims, unrealistic outcomes, urgency, price

Official page not retrieved (404). Vendor summaries agree on these patterns (https://www.auditsocials.com/blog/meta-ad-misleading-claims-personal-attributes-prohibited-content-policy-2026 , updated 9 May 2026, and https://adsuploader.com/blog/meta-ad-guidelines): ads must not deceive or fail to deliver the promised benefit; review covers the creative, every text field and the landing page; fake countdown timers and false scarcity ("Only 3 left") get flagged; unsupported statistical claims get flagged; fake editorial or news formatting gets flagged; testimonials must represent typical experience. [VERIFY: wording and any new 2026 rules, read the live page before the skill quotes anything]

What this means for a tour operator:

- Price in the image, primary text, headline and landing page must be the same number. "From NOK 1,948" requires the landing page to show NOK 1,948 as the starting price.
- "Limited spots" must be true. If the group cap is real and the page shows remaining places, say so. Do not run a countdown that resets.
- No guarantees about snow, weather, aurora, summit or descent quality. "Fresh tracks sorted" is a promise. "Fresh tracks on the best days" is safer. Check each outcome claim against the operator's actual terms.
- Superlatives ("best", "number one", "most") need proof on the landing page.
- "Free" and "included" claims must match the booking terms exactly. Meta's reviewer opens the landing page in real time (Vendor claim, https://adsuploader.com/blog/meta-ad-guidelines).
- Landing page must function, be mobile friendly and match the ad's product. Broken links and "minimal content" pages are rejection reasons in vendor reports.

### 5.4 Text in images, logos, trademarks, UGC, testimonials

- The old 20% text rule was removed in September 2020 (https://adzooma.com/blog/facebook-advertising-removes-20-text-rule-on-images/ , https://www.socialmediatoday.com/social-networks/facebooks-changed-20-ad-image-text-overlay-rule). Meta still said at the time that images with less text generally perform better. Claims that heavy text gets less delivery today are Vendor lore. [VERIFY]
- Meta IP policy: do not use Facebook or Instagram logos or names in ways that imply endorsement. Use Meta's brand resource rules. Third-party marks (resort, lift company, gear brand) used in a way that implies partnership can be reported. [VERIFY: nominative use of a place or resort name such as Voss is normally fine, brand logos of third parties need permission]
- Creator content: use the branded content tool and partnership ads (https://transparency.meta.com/policies/ad-standards/ index lists "Branded Content").
- Testimonials: keep real, attributable, typical. Do not invent reviews.

### 5.5 Norway and EU specifics

- Price rule for reductions: Forbrukertilsynet says that for goods marketed as reduced, the reference price is the lowest price used for at least 30 days before marketing starts. The same page says this rule does not apply to services, which includes guided tours. For services, the general ban on misleading marketing still applies, so a "was NOK X" claim must reflect a real earlier price. Source: https://www.forbrukertilsynet.no/vi-jobber-med/prismarkedsforing/salg-og-bruk-av-forpriser . [VERIFY: whether a package that includes goods changes this]
- Labelling paid creator content: Marketing Control Act section 3 requires marketing to be identifiable. "Reklame" or "annonse" count as clear labels, and platform tools alone are not enough per the regulator's guidance as summarised in search results (https://www.forbrukertilsynet.no/vi-jobber-med/reklame-i-sosiale-medier/ofte-stilte-sporsmal-om-reklame-i-sosiale-medier). Forbrukertilsynet published an influencer marketing report on 17 December 2025 (reported). [VERIFY: confirm label wording with the regulator page]
- Labelling retouched people: Norway has a guideline on labelling retouched advertising (https://www.forbrukertilsynet.no/english/guidelines/the-norwegian-consumer-authoritys-guideline-on-labelling-retouched-advertising returned 404 for me). [VERIFY: scope, and whether AI-generated people in ads count]. Safe rule for the skill: use real photos of real guests with consent, and say if a person is generated.
- EU DSA: Meta's standards list beneficiary and payer identification for ads in the EU. [VERIFY: whether Norway (EEA) is in scope yet]
- EU personalisation: Meta rolled out a "less personalised ads" choice to all EEA users in January 2026, and reports say it reduces signal. Source: https://ppc.land/metas-2026-dma-report-reveals-whatsapp-ads-a-eu200m-fine-and-a-defiant-stance-on-personalized-advertising/ and https://seresa.io/blog/meta-dma-less-personalized-ads/metas-lpa-rollout-just-split-your-eu-audience-into-two-tiers (Reported/Vendor). [VERIFY: Norway coverage and effect on delivery]
- Teens: Meta says age and location are the only information advertisers can use to target 13 to 17 year olds. Source: search summary of Meta's announcement via https://www.techbuzz.ai/articles/meta-bows-to-eu-pressure-with-new-ad-choice-model-for-2026 (Reported). [VERIFY: primary Meta page]
- Location fees: Meta charges location fees for ads delivered in the UK (2%), France, Italy and Spain (3% each) and Austria and Turkey (5% each), effective May 2026 with billing from 1 July 2026, on top of ad spend. Source: https://www.mediapost.com/publications/article/413378/meta-passes-eu-digital-services-tax-to-advertisers.html (Reported, 10 March 2026). Norway was not listed in anything I read. If the client targets British or Alpine-market skiers, budget 2% to 5% extra.

### 5.6 What gets travel and adventure ads rejected in practice

Mostly Vendor reports; use as a checklist, not as policy text. Sources: https://megadigital.ai/en/blog/facebook-ads-rejected/ , https://madgicx.com/blog/facebook-ad-rejected , https://www.brandwatch.com/blog/facebook-ad-policies-why-your-ads-arent-getting-approved/ , https://gripasmarketing.com/meta-ads-claims-personal-policy/

1. Personal attribute phrasing ("Are you...", "other ... like you", age, health, disability, money).
2. Landing page mismatch (different price, different product, general homepage, missing refund or terms).
3. Misleading or unprovable claims (guarantees, superlatives, outcomes).
4. Fake urgency or scarcity (resetting timers, "only 3 left" without basis).
5. Shocking or sensational imagery (injury, crash, graphic risk). Action shots are normally fine. Keep them clean.
6. Alcohol shown or mentioned without 18+ targeting.
7. Broken or thin landing pages, no business information.
8. Misuse of Meta brand names or icons, or a third-party logo without rights.
9. Targeting issues (discriminatory exclusions are blocked in several categories).
10. AI-edited creative that changes a claim after approval (price rewritten by image text enhancements). This one is newer and my inference from the July 2026 change. [VERIFY]

### How adwright should use this

- Run a pre-flight lint on every output: personal attribute pattern check ("you" within a few words of age, health, disability, money, relationship, religion words), outcome guarantee check (guarantee, always, never, best, number one), urgency check (today only, last chance, only N left, countdown) and a price consistency check (same number across image, primary text, headline, landing page).
- Require the user to paste the landing page price. Block output if it differs.
- Add a Norway layer: no "was" price on a service without a real prior price, "reklame" label on creator content, flag AI-generated people.
- Show the lint result with plain reasons and the nearest safe rewrite.
- Always say "check the live policy page" in the output footer, and store the policy URL in the reference file.

---

## 6. Creative best practice and benchmarks

### 6.1 What official and credible sources support

- Mobile first: the vast majority of the surface is a phone. Use 4:5 for feed (largest vertical footprint) and 9:16 for Reels and Stories. 1:1 is the safe single-file fallback for mixed placements. Source: official ratios (section 2) and https://blog.hootsuite.com/facebook-ad-sizes/ (Vendor).
- Less text on the image, more value in the first look. Meta removed the 20% rule in 2020 but kept the advice to use less text. Keep on-image copy to what a thumb-scroller can read in one second: product name, date, price.
- Price pills and sale lines work as hooks in aggregate data: "Price anchor" and "Sale announcement" were among the top hooks by hit rate in Motion's 2026 benchmark (section 4.8).
- People-first imagery: Meta guidance and vendor advice point to showing people and real context, not stock. I found no primary study to quote. [VERIFY]
- Logo: put it small and consistent. Official specs say keep logos out of the 9:16 unsafe zones. No primary study on logo size or placement. [VERIFY]
- Captions and sound on video: official specs say recommended. Meta's 2015-era figure for captions is +12% view time. [VERIFY: dated]

### 6.2 Travel and tourism benchmarks (all tagged)

| Metric | Value | Source | Status |
|---|---|---|---|
| Facebook traffic campaigns, Travel average CTR | 2.76% | WordStream 2025 benchmarks as tabulated at https://www.enrichlabs.ai/blog/meta-ads-benchmarks-2025 (WordStream page returned 403) | [VERIFY: secondary tabulation, data window not stated] |
| Facebook traffic campaigns, Travel average CPC | $0.51 | same | [VERIFY: same] |
| All-industry traffic campaigns (WordStream 2025) | CTR about 1.71%, CPC about $0.70 | search-result summary of https://www.wordstream.com/blog/facebook-ads-benchmarks-2025 | [VERIFY: not read on page] |
| All-industry leads campaigns | CTR 2.59%, CPC $1.92, conversion rate 7.72% | same | [VERIFY: same; these are not travel-specific] |
| Recreation and Travel median CPM, Facebook | about $11.94 average over the period; low $9.44 (December 2025), peak $15.52 (June 2026); about 42% below a global baseline of about $20.58 | https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/recreation-and-travel (sample "over $3B" spend, medians) | Reported. The page states two slightly different date ranges. [VERIFY: window] |
| Tours and experiences CPC, prospecting | EUR 0.70 to 1.40 | https://adlibrary.com/posts/meta-ad-benchmarks-travel-2026 (16 May 2026) | Vendor. The page gives no method or sample size. [VERIFY] |
| Tour CPA range | EUR 35 to 120 | same | Vendor, unsourced. [VERIFY] |
| Seasonal CPM spike | 25% to 50% in peak travel seasons | same | Vendor, unsourced. [VERIFY] |
| Travel conversion rate on Meta | about 1.2% | search-result summary, many blogs | [VERIFY: no primary source] |
| Facebook ad ROAS for hospitality and travel "4x to 7x" or "12.9x" | circulates widely | multiple vendors | [VERIFY: do not quote. ROAS depends on definition and attribution] |

Seasonality hint for a ski operator: Superads shows Recreation and Travel CPM falling 24.8% from November to December and rising 33.6% from March to April. That is the category as a whole, mostly not ski. [VERIFY: apply to ski only after seeing the client's own history]

### 6.3 Static image versus video for this client

Evidence points both ways. Video earns more clicks and attention in aggregate vendor data, static often wins on cost per acquisition and is cheaper to produce. For a seasonal operator with a handful of products and a need for visible price and dates, a static set plus two or three short Reels is the sensible mix. The 61% static, 39% video median in the Segwise sample (section 4.8) is a sanity check, not a target.

### How adwright should use this

- Provide a benchmark table in the skill with every row tagged and with the retrieval date. Never present a single number as "the benchmark". Present ranges and say what to measure instead: the client's own CTR, cost per landing page view and cost per booking.
- Make the creative checklist short: one subject, one price, one date line, one logo, five seconds to read, safe zones respected, real people.
- Ask the user for last season's results and use those as the comparison, not vendor medians.

---

## 7. The static image ad job for a tour operator

A static feed ad has five parts that must not repeat each other. Each layer has one job.

| Layer | Job | Reader behaviour |
|---|---|---|
| On-image block | Say what, when, how much. Scannable in one second | Seen first. Often the only thing read |
| Primary text (above image) | Give the reason to care and the action | First line seen by everyone, rest only if "See more" tapped |
| Headline (below image, Facebook only) | Restate the offer as a button label companion | Facebook feed shows it, Instagram feed reportedly does not |
| Description (below headline) | One extra proof point | Often not shown on mobile feed |
| CTA button | Action | Always shown on link ads |

### 7.1 Labelled anatomy, Facebook mobile feed (top to bottom)

```
[Page photo] Outdoor Norway
             Sponsored                                  <- fixed, not editable
-------------------------------------------------------
Primary text   up to 125 chars before "See more"
               official recommendation 50-150
-------------------------------------------------------
[ Image 4:5, 1440 x 1800 ]
   on-image block: name / dates / price
-------------------------------------------------------
Display link   (domain, small, above headline)
Headline       27 chars recommended, bold      [ Book now ]
Description    30 chars, grey, often hidden on mobile feed
-------------------------------------------------------
Like   Comment   Share
```

Character budgets (Facebook feed):

| Slot | Budget | Hard behaviour |
|---|---|---|
| Primary text, visible part | 125 | "See more" cut at about 125 on mobile (about 110 to 135 by device, [VERIFY]) |
| Primary text, total | aim for 125 to 300 | Meta recommends 50 to 150. Longer is allowed |
| On-image line 1 (name) | 25 | one line at large size |
| On-image line 2 (dates) | 30 | one line |
| On-image line 3 (price) | 20 | "NOK 1,948" in the biggest weight |
| Headline | 27 | recommended per Meta. About 27 shows on mobile before truncation (vendor) |
| Description | 30 | vendor says often hidden. Do not put the price only here |
| Display link | domain only | set in Ads Manager |

### 7.2 Labelled anatomy, Instagram feed

```
[Profile photo] outdoornorway   Sponsored
-------------------------------------------------------
[ Image 4:5, 1440 x 1800 ]
   on-image block: name / dates / price
-------------------------------------------------------
[ Book now  >  ]        <- full-width CTA bar under the image
Like  Comment  Share  Save
outdoornorway  Primary text, first 125 chars ... more
-------------------------------------------------------
```

| Slot | Budget | Note |
|---|---|---|
| Primary text (caption) | 125 visible, official limit field says 125 | Starts after the account name, so the first words matter most |
| Headline | field up to 40 on Meta's page | Reported as not shown on single-image Instagram feed ads. [VERIFY in preview] |
| CTA bar | label from the 27 button list | Always shown |
| Hashtags | max 30 | Skip. Not needed |
| On-image block | same as Facebook | image must carry price and dates because the headline may not show |

Sources for the layout reports: https://blog.adnabu.com/facebook-ads/facebook-ad-specs/ , https://insights.vaizle.com/anatomy-of-a-facebook-ad/ and the search summaries (Vendor). Meta's spec pages list the headline for Instagram feed but do not say where it is rendered.

### 7.3 Worked example (illustrative, not client-approved copy)

Facts used: product "Ski day tour" at NOK 1,948. Dates and inclusions are placeholders. Replace with the product sheet. Do not publish inclusions that the product sheet does not confirm.

| Slot | Text | Characters |
|---|---|---|
| On-image line 1 | Voss Ski Day Tour | 17 |
| On-image line 2 / 3 | [Dates] \| NOK 1,948 per person | 30 |
| Primary text | Ski Voss with a local guide. NOK 1,948 for the day. Pick a date and book online. | 80 |
| Headline | Ski day tour from NOK 1,948 | 27 |
| Description | Guided day on snow. Book online. | 32 |
| Reels line (40 char budget) | Ski Voss. NOK 1,948. | 20 |
| CTA | Book now (or Check Availability) | label |

The 9 day trip version: headline "9 day ski trip, NOK 42,126" (26), primary text "Nine days of skiing in Norway. From NOK 42,126." (47). Confirm "from" against the landing page.

Why this works against the rules above: price, product and action all appear inside the first 125 characters; the on-image block carries the same three facts for people who never read text; the headline repeats the price only because Facebook may hide the description and Instagram may hide the headline; no claim promises snow or outcomes.

### 7.4 On-image design rules (practitioner heuristics, not Meta rules)

- Three lines maximum. Name, dates, price.
- Price in the heaviest weight, the date line second, the name third. Test a price pill versus plain text.
- Readable at 375 px wide preview. If you cannot read it on a phone-width preview, it is too small.
- Keep text away from the edges (5% margin) and out of the lower part where overlays might appear if the image is re-cropped.
- Photo of real guests on real snow in Voss, no lens flare stock. People face visible.
- Add a 9:16 variant with the Reels safe zones (section 2.3) if the ad runs in Stories and Reels.

### How adwright should use this

- Make the static ad a template with named slots (image_line_1, image_line_2, image_line_3, primary, headline, description, cta, reels_line), each with a character budget and a count shown beside the output.
- Do not allow the same sentence in two slots. Check string overlap.
- Always emit a plain-text "image spec brief" for the designer with ratio, resolution, margins and the three on-image lines, so the on-image text is never baked in by an AI image tool.
- Render a mock of the Facebook and Instagram layouts in the skill's preview so the user sees the truncation.

---

## 8. X (Twitter) advertising

Access note: business.x.com and help.x.com returned HTTP 402 or 403, so there are no direct reads of X's own spec pages from me. X's API docs (docs.x.com) were readable.

### 8.1 Formats and specifications

| Element | Value | Source | Status |
|---|---|---|---|
| Post length in ads | 280 characters | https://benly.ai/learn/x-ads/x-twitter-ads-formats-specs (updated 24 March 2026) | Reported |
| URL length | every link counts as 23 characters | same and https://lettercounter.org/blog/twitter-ads-character-limits/ (1 February 2026) | Reported |
| Premium long posts (up to 25,000 characters) | organic only for ads, per one source | lettercounter above | [VERIFY: confirm ads cannot use long posts] |
| Website card headline | up to 70 characters, 50 recommended to avoid truncation, two lines then ellipsis | https://www.veuno.com/x-formerly-twitter-ad-specs-your-guide-for-2026/ (December 2025) | Reported |
| Website card description | up to 200, about 125 visible | lettercounter above | [VERIFY: vendor] |
| Carousel | 2 to 6 cards, 70 character headline, one URL per card allowed | benly and https://docs.x.com/x-ads-api/creatives | Reported / Official (card count) |
| Image ratios | 1.91:1, 1:1, and 4:5 | benly | [VERIFY: veuno lists 1.91:1 or 1:1 and a 2:1 to 1:1 range] |
| Image recommended sizes | 1200 x 675 (1.91:1), 1080 x 1080, 1080 x 1350; minimum 600 x 335 | benly | Reported |
| Image file | JPG, PNG (GIF listed by benly), max 5 MB | benly, veuno | Conflict: X Ads API docs say 3 MB and list bmp, jpeg, png, minimum width 800 px (https://docs.x.com/x-ads-api/creatives). [VERIFY: current Ads Manager limit] |
| Video ratios | 16:9, 1:1, 9:16 | benly | Reported |
| Video length | up to 2 minutes 20 seconds in the UI, 15 to 30 seconds recommended. API allows 10 minutes | benly, docs.x.com | Reported / Official (API) |
| Video file | MP4 or MOV, H.264, AAC, up to 1 GB (under 30 MB suggested), 30 or 60 fps | benly, veuno | Reported |
| Image ad CTA buttons (app buttons) | Install, Open, Play, Shop, Book, Connect, Order | veuno and search summaries of business.x.com | Reported. This list is for app buttons. [VERIFY: current website CTA labels] |
| Sales objective format | from 13 May 2025 the headline and a customisable CTA button sit below the image or video for Sales objective ads | https://www.socialmediatoday.com/news/x-formerly-twitter-updates-link-format-ads-adds-cta-button/748010/ | Reported, quoting X |
| Promoted-only posts | created via a dedicated endpoint, do not appear on the public timeline | https://docs.x.com/x-ads-api/campaign-management | Official |
| Account structure limits | 200 active campaigns, 100 line items per campaign, 8,000 active line items per account | same | Official |

### 8.2 Policy

- Deceptive and fraudulent content: per a search summary of X's policy page, ads may not promote products with deceptive marketing, including clickbait that drives users to a landing page through "exaggerated, sensationalized, inaccurate language". Source: https://business.x.com/en/help/ads-policies/ads-content-policies/deceptive-and-fraudulent-content (403, summary only). [VERIFY: read the live page]
- Quality system: X's ad quality guidance reported in 2025 gives each ad an "aesthetic score". Reported criteria: grammar and punctuation, no more than one emoji (except in Japan and Korea), no hashtags, no URLs in the ad copy, no excessive cropping or "gimmicky" animation, no flashing or loud effects, layout clarity and landing page alignment. Better scores mean lower cost and better placement. X has not said whether advertisers will see the score or how much it changes price. Sources: https://www.medianama.com/2025/08/223-x-aesthetic-score-ad-pricing-change/ (6 August 2025) and https://www.adweek.com/media/x-will-give-brands-lower-ad-rates-for-aesthetic-ads-free-of-urls-emojis/ . The Adweek fetch gave an unclear date. [VERIFY: dates and current status]
- Equivalents to Meta's rules: misleading claims, health claims, adult content, tobacco and drugs are prohibited (search summary of X's pages). Price and landing page accuracy follow the same logic. Run the same lint as for Meta. [VERIFY: X-specific wording on pricing and urgency]

### 8.3 Platform state in 2026

- X rolled out a rebuilt, xAI-powered ads platform starting 30 April 2026, with AI retrieval and ranking and "contextual and semantic" delivery. Digiday (30 April 2026) says the full platform is expected "later this year". Source: https://digiday.com/marketing/x-upgrades-its-ad-platform-in-long-overdue-overhaul/ . A trade-press source repeats that nearly all top 100 advertisers returned, according to X's head of global advertising. That is X's own claim. [VERIFY]
- CPM: Digiday-relayed figures put X's average CPM at $2.23 (2024), $1.05 (2025), $0.64 (early 2026), against Facebook $4.93 and Instagram Reels $3.95. Affect Group, an agency, reports Q2 2026 X CPMs of $9 to $13 for Website Traffic campaigns and $8 to $10 for Travel, with a 2.0% Travel engagement rate (https://affectgroup.com/blog/x-advertising-cpm-benchmarks-for-the-united-states/ , 17 July 2026). The two sets of numbers cannot both describe the same thing. The low figure looks like a blended average and the agency figure like a managed-account objective average. [VERIFY: both. Use neither as a plan]
- Revenue: X ad revenue reported to be falling in 2025 and early 2026, and placements tied to X's AI assistant are being sold. [VERIFY: figures vary between about $1.8 billion and $2.46 billion depending on source]
- Return quality: an agency quote in Digiday says X "has struggled to keep up with its peers in direct-response advertising, and its returns have been subpar." (Shamsul Chowdhury, Zeno Group). That is an opinion from one agency.

### 8.4 Audience and tone reality for Norway

- DataReportal, Digital 2026 Norway, figures as of October 2025 and presented as ad reach, not active users: Facebook 3.05 million (54.1% of the population), Instagram 2.65 million (47.0%), X 1.02 million (18.2%), TikTok 1.80 million adults (39.8% of 18+), Snapchat 3.70 million (65.7%). Source: https://datareportal.com/reports/digital-2026-norway . An earlier search summary cited 1.11 million X users in early 2025, so the trend is down. [VERIFY: figures came through a page summariser]
- Global X audience is a third-party estimate in the range of about 557 to 611 million monthly users because X stopped publishing audited figures. Source: https://searchlab.nl/en/statistics/x-twitter-statistics-2026 (Reported). Not needed for the client job.
- Demographic and interest profile of X users in Norway: I found no sourced data. [VERIFY: pull from X Ads audience insights or Sprout, do not guess]
- Tone: plain, specific, human, quick. X users react badly to ads that look like ads. That is craft opinion, not a measured result. [VERIFY]

### 8.5 A promoted post that does not look like an ad

Practitioner pattern, supported by X's own "aesthetic" direction (no hashtags, no URLs in copy, at most one emoji, clean image):

- One sentence of plain copy in a human voice. No hashtags. No emoji, or one at most.
- A real photo, not a stock shot, in 1.91:1 or 1:1 (check 4:5 support).
- The link lives in the card, not in the text (link text counts 23 characters anyway).
- The facts are in the post: place, price, a date or window. "A guided ski day in Voss costs NOK 1,948." is 40 characters and tells the whole story.
- Use promoted-only posts for testing, so the brand's profile stays clean. Promote an existing organic post when it already has real replies, because social proof shows.

### 8.6 Replies, quotes, links, threads

- Replies and quotes on a promoted post appear like on any post. I found no source on whether advertisers can restrict replies on ads. [VERIFY]
- Link handling in organic posts is disputed. Vendor and AI answers say posts with links get less organic reach, while X's head of product Nikita Bier said links are no longer deboosted and Elon Musk said "We haven't for over a year" (Reported: https://www.freepressjournal.in/tech/x-product-head-nikita-bier-confirms-link-penalty-removed-over-a-year-ago-tells-mark-zuckerberg-he-can-post-them-directly). Nieman Lab reported in October 2025 that X added a feature to improve reach for links (https://www.niemanlab.org/2025/10/x-makes-overtures-to-journalists-with-new-feature-designed-to-improve-reach-for-links/). For paid ads the link penalty question matters less, because delivery is bought. [VERIFY: current organic behaviour]
- Threads: a promoted post is one post. The hook must stand alone. A thread only helps an organic account that is already promoted. [VERIFY: whether multi-post threads can be promoted as one unit]
- Best practice for outdoor and travel on X: no primary source found. Practitioner view: use X for moment-based posts (snow report, last places on a weekend tour), which only works if the facts are real. Test with a small budget and compare cost per landing page view with Meta. [VERIFY]

### How adwright should use this

- Treat X as a second output mode with two templates: "native post" (280 characters, no hashtag, no emoji or one, link in card) and "website card" (image 1.91:1 or 1:1, headline 50 characters recommended, 70 max).
- Do not copy the Meta anatomy to X. X has two layers: post text and card headline.
- Ship X specs with the conflict flags (5 MB versus 3 MB image limit) so the user checks before upload.
- Warn that X is a secondary channel for a Norwegian ski operator unless the client already has an audience there.

---

## 9. Spec sheet

Official means read on a Meta page. Reported means a secondary source. Tags are in the Status column.

| Platform | Placement | Element | Limit | Source URL | Status |
|---|---|---|---|---|---|
| Meta | Facebook Feed | Image ratio | 4:5 (3% tolerance) | https://www.facebook.com/business/ads-guide/update/image/facebook-feed/link-clicks | Official |
| Meta | Facebook Feed | Image resolution | 1440 x 1800 recommended, min 600 x 750 | same | Official |
| Meta | Facebook Feed | Image file | JPG or PNG, 30 MB | same | Official |
| Meta | Facebook Feed | Primary text | 50-150 characters (cut at about 125 on mobile) | same | Official, cut Vendor |
| Meta | Facebook Feed | Headline | 27 characters | same | Official |
| Meta | Facebook Feed | Description | about 30, often hidden on mobile | https://socialrails.com/blog/facebook-ad-character-limits | Reported |
| Meta | Facebook Feed | Video | 4:5, 1440 x 1800, 1 s to 241 min, 4 GB, MP4 MOV GIF | https://www.facebook.com/business/ads-guide/update/video/facebook-feed/link-clicks | Official |
| Meta | Instagram Feed | Image ratio | 4:5 (range 4:5 to 1.91:1, 1% tolerance) | https://www.facebook.com/business/ads-guide/update/image/instagram-feed/link-clicks | Official |
| Meta | Instagram Feed | Image resolution | 1440 x 1800, min 500 px wide | same | Official |
| Meta | Instagram Feed | Primary text | 125 characters | same | Official |
| Meta | Instagram Feed | Headline | 40 characters (reported not displayed on single-image feed ads) | same, plus vendor guides | Official field, display Vendor |
| Meta | Instagram Feed | Hashtags | max 30 | same | Official |
| Meta | Instagram Feed | Video | 9:16, 1080 x 1920, 1 s to 60 min, 4 GB | https://www.facebook.com/business/ads-guide/update/video/instagram-feed/link-clicks | Official |
| Meta | Instagram Reels | Video | 9:16, 1440 x 2560, up to 15 min, 4 GB, MP4 MOV, H.264 | https://www.facebook.com/business/ads-guide/update/video/instagram-reels/link-clicks | Official |
| Meta | Instagram Reels | Primary text | 44 characters | same | Official |
| Meta | Reels and Stories | Safe zone | 14% top, 35% bottom, 6% each side (269 / 672 / 65 px at 1080 x 1920) | same | Official, px my arithmetic |
| Meta | Stories | Image and video | 9:16, 1080 x 1920, primary 125, headline 40 | https://socialrails.com/blog/facebook-ad-character-limits | Reported, [VERIFY: Meta page 404] |
| Meta | Facebook Feed carousel | Cards and text | 2-10 cards, 1:1, 1080 x 1080 min, primary 80, headline 20, description 18 | https://www.facebook.com/business/ads-guide/update/carousel/facebook-feed/link-clicks | Official |
| Meta | Instagram Feed carousel | Cards and text | 2-10 cards, 4:5 images only, 1:1 with video, primary 125 | https://www.facebook.com/business/ads-guide/update/carousel/instagram-feed/link-clicks | Official |
| Meta | Collection | Cover and text | 1.91:1 to 1:1, 1080 x 1080 min, 3 product images, primary 125, headline 40, Instant Experience required | https://www.facebook.com/business/ads-guide/update/collection | Official |
| Meta | All feed | CTA buttons | 31 labels on Facebook, 27 on Instagram (see 2.7) | the feed spec pages above | Official |
| Meta | Delivery | Learning phase | about 50 optimisation events in the week after last significant edit | https://www.facebook.com/business/help/942374239243867 | Official (via search text) |
| Meta | Advantage+ creative | Text controls | per-ad toggles, Branding section, Restricted Words | https://www.socialmediatoday.com/news/meta-adds-restricted-words-ai-ad-copy-generation/759084/ | Reported |
| Meta | Targeting | Detailed targeting exclusions | removed (announced 21 January 2025) | https://developers.facebook.com/blog/post/2025/01/21/removal-of-detailed-targeting-exclusions/ | Official (via ppc.land) |
| X | Post | Text | 280 characters, link counts 23 | https://benly.ai/learn/x-ads/x-twitter-ads-formats-specs | Reported |
| X | Website card | Headline | 70 max, 50 recommended | https://www.veuno.com/x-formerly-twitter-ad-specs-your-guide-for-2026/ | Reported |
| X | Website card | Description | 200 max, about 125 visible | https://lettercounter.org/blog/twitter-ads-character-limits/ | [VERIFY: vendor] |
| X | Image ad | Ratios and size | 1.91:1, 1:1 (4:5 reported), 1200 x 675, 1080 x 1080, 1080 x 1350, min 600 x 335, 5 MB (API doc says 3 MB) | https://benly.ai/learn/x-ads/x-twitter-ads-formats-specs , https://docs.x.com/x-ads-api/creatives | Conflict, [VERIFY] |
| X | Video ad | Ratios, length, size | 16:9, 1:1, 9:16, up to 2:20 in UI, MP4 MOV, 1 GB | same | Reported |
| X | Carousel | Cards | 2 to 6, 70 char headline | https://docs.x.com/x-ads-api/creatives | Official (cards) |
| X | Promoted-only posts | Mode | does not show on public timeline | https://docs.x.com/x-ads-api/campaign-management | Official |
| X | Sales objective | Headline and CTA | below the media, customisable CTA (from 13 May 2025) | https://www.socialmediatoday.com/news/x-formerly-twitter-updates-link-format-ads-adds-cta-button/748010/ | Reported |

---

## 10. What changed in the last 12 months (roughly October 2025 to 6 October 2026)

Items just outside the window are marked "background".

Meta

- 2 September 2025 (background): Restricted Words setting for AI-generated text in Advantage+ creative. (https://www.socialmediatoday.com/news/meta-adds-restricted-words-ai-ad-copy-generation/759084/)
- 11 December 2025: Meta expanded creator tools for partnership ads and published "19% lower CPAs and 13% higher CTR on average". (https://www.marketingdive.com/news/meta-streamlines-brands-creator-partnerships-with-ai-powered-updates/807629/)
- 17 December 2025: Meta marketing guidance on Reels hooks and creative diversification. (https://www.socialmediatoday.com/news/meta-shares-tips-on-reels-hooks-creative-diversification-in-ads-and-threa/808182/)
- 15 January 2026: reported final cutoff for consolidated detailed targeting interests. [VERIFY: vendor sources]
- January 2026: less personalised ads choice rolled out to all EEA users (Reported). [VERIFY: Norway scope]
- March 2026: Flexible ad format reportedly folded into an Advantage+ creative toggle. [VERIFY]
- 10 March 2026: Meta announced location fees (UK 2%; France, Italy, Spain 3%; Austria, Turkey 5%), effective May 2026 and billed from 1 July 2026. (https://www.mediapost.com/publications/article/413378/meta-passes-eu-digital-services-tax-to-advertisers.html)
- 23 June 2026: Advantage+ text generation reportedly extended to image text, and a Brand memory feature in test. [VERIFY: vendor reference https://adsuploader.com/blog/advantage-plus-creative-enhancements]
- 27 July 2026: image text rewriting reported as default on in eligible Advantage+ campaigns. (see 4.4)
- 29 July 2026 (earnings call, Q2 2026): Meta Generative Recommender introduced; GEM plus user understanding models gave 8.3% more ad clicks and 15.7% more conversions on Facebook; Advantage+ run-rate above $75 billion. (https://s21.q4cdn.com/399680738/files/doc_financials/2026/q2/META-Q2-2026-Earnings-Call-Transcript.pdf)
- 19 to 21 August 2026: placement, platform, device and operating system exclusions being removed from ad sets for Sales and Leads campaigns (Reported, not a formal announcement). (see 4.6)
- 26 August 2026: Creative diversity rating (Low, Medium, High) in Ads Manager, labelled "estimated and in development".
- 27 August 2026: Messenger Stories ad placement removed.
- September 2026: reported items from one changelog, each [VERIFY: single vendor, https://commonthreadco.com/blogs/coachs-corner/meta-ads-changes-2026]: Creator Marketing Hub (15 September), Instagram live video ads (29 September), Threads ads no longer require an Instagram presence (22 September), exclusion-only custom audiences (10 August).

X

- 13 May 2025 (background): headline and CTA button below the image or video for Sales objective ads.
- August 2025 (background): "aesthetic score" ad quality system reported. (https://www.medianama.com/2025/08/223-x-aesthetic-score-ad-pricing-change/)
- 30 April 2026: xAI-powered rebuilt ad platform begins phased rollout. (https://digiday.com/marketing/x-upgrades-its-ad-platform-in-long-overdue-overhaul/)
- 2026: ad placements tied to the AI assistant and lower reported CPMs (see 8.3). [VERIFY]

### How adwright should use this

- Add a `changelog.md` to the skill with each item above, a date, a tag and a "last checked" date. Have the skill print the age of its spec data in every output.
- Because Meta changes this fast, put a "re-verify before use" step in the skill for specs older than 90 days.
- Treat the vendor-only items as watch items, not rules.

---

## 11. Open questions for the next research pass

1. Read Meta's live Advertising Standards pages on misleading claims, sensational content and discounts. All of those I read were summaries.
2. Get Meta's own page for Advantage+ creative image text rewriting, and the exact default status per campaign type.
3. Confirm where the headline renders on Instagram feed single-image ads in a live preview.
4. Open X's creative specs and ads policy pages in a browser (the fetcher returned 402) and settle the image file size (5 MB versus 3 MB), the website card limits and the CTA label list.
5. Find the client's last season results and use those in place of vendor benchmarks.
6. Confirm Norwegian and EEA scope for DSA beneficiary and payer fields, and the retouched-advertising label rule for AI-generated people.
7. Decide, with the client, which tour facts are safe to state in ads (inclusions, group size, guarantee language) so examples stop using placeholders.
