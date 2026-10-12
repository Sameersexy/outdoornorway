# X (Twitter) ads: formats, limits, policy, tone and the 2026 platform state

What this is: the platform reference for any X output (a promoted post or a website card). Read it at step 5 (slots and budgets) and step 7 (policy and fact pass) when the platform is X, and when the user asks whether X is worth a test. Platform data verified 2026-10-06, with the gaps stated below.

## Contents

1. Read this first: what could and could not be checked
2. Formats and limits
3. Ad policy
4. A promoted post that does not look like an ad
5. Replies and quotes
6. Links
7. Threads
8. The 2026 platform state
9. Audience reality
10. Slot budgets for X output
11. Pre-flight checklist
12. Sources

## 1. Read this first: what could and could not be checked

The research pass could read X's developer documentation (docs.x.com). It could not read X's own business pages. The business.x.com and help.x.com pages returned status 402 or 403 to the fetcher.

So the evidence on X is thinner than the evidence on Meta. Every number from a source other than docs.x.com is Reported or Vendor, and the secondary sources disagree in places. The tags:

| Tag | Meaning |
|---|---|
| verified 2026-10-06 | Read on X's developer documentation. The URL is in the row. |
| Reported | Trade press or a spec guide describing the platform. Likely, not certain. |
| Vendor | An agency or tool claim with no X page behind it. A hypothesis. |
| [VERIFY: reason] | Not confirmed. Check it in X Ads Manager before you rely on it. |

Say this plainly to the user: on X, check the limits in the composer before you hand over copy. The 280 character post limit is stable. Card limits, image file sizes and button labels are the numbers that move.

## 2. Formats and limits

| Element | Value | Source | Status |
|---|---|---|---|
| Post text in ads | 280 characters | https://benly.ai/learn/x-ads/x-twitter-ads-formats-specs (updated 24 March 2026) | Reported. [VERIFY: X pages unreachable] |
| Link length | every link counts as 23 characters | https://benly.ai/learn/x-ads/x-twitter-ads-formats-specs and https://lettercounter.org/blog/twitter-ads-character-limits/ (1 February 2026) | Reported. [VERIFY] |
| Long posts (Premium, up to 25,000 characters) | reported as organic only, not for ads | https://lettercounter.org/blog/twitter-ads-character-limits/ | [VERIFY: confirm ads cannot use long posts] |
| Website card headline | up to 70, 50 recommended to avoid truncation, two lines then an ellipsis | https://www.veuno.com/x-formerly-twitter-ad-specs-your-guide-for-2026/ (December 2025) | Reported. [VERIFY] |
| Website card description | up to 200, about 125 visible | https://lettercounter.org/blog/twitter-ads-character-limits/ | [VERIFY: vendor figure] |
| Carousel | 2 to 6 cards | https://docs.x.com/x-ads-api/creatives | verified 2026-10-06 |
| Carousel headline | 70 characters, one URL per card allowed | https://benly.ai/learn/x-ads/x-twitter-ads-formats-specs | Reported. [VERIFY] |
| Image ratios | 1.91:1, 1:1 and 4:5 | https://benly.ai/learn/x-ads/x-twitter-ads-formats-specs | [VERIFY: another guide lists 1.91:1 or 1:1 and a 2:1 to 1:1 range, https://www.veuno.com/x-formerly-twitter-ad-specs-your-guide-for-2026/] |
| Image sizes | 1200 x 675 (1.91:1), 1080 x 1080 (1:1), 1080 x 1350 (4:5). Minimum 600 x 335 | https://benly.ai/learn/x-ads/x-twitter-ads-formats-specs | Reported. [VERIFY] |
| Image file size | 5 MB in two spec guides. The Ads API documentation says 3 MB, formats bmp, jpeg and png, minimum width 800 px | https://docs.x.com/x-ads-api/creatives | Conflict. API figure verified 2026-10-06. [VERIFY: current Ads Manager limit. Use a file under 3 MB until confirmed] |
| Video ratios | 16:9, 1:1, 9:16 | https://benly.ai/learn/x-ads/x-twitter-ads-formats-specs | Reported. [VERIFY] |
| Video length | up to 2 minutes 20 seconds in the interface, 15 to 30 seconds recommended. The API allows 10 minutes | https://benly.ai/learn/x-ads/x-twitter-ads-formats-specs and https://docs.x.com/x-ads-api/creatives | Interface figure Reported. [VERIFY: interface limit, X pages unreachable]. API figure verified 2026-10-06 |
| Video file | MP4 or MOV, H.264, AAC, up to 1 GB (under 30 MB suggested), 30 or 60 fps | https://benly.ai/learn/x-ads/x-twitter-ads-formats-specs and https://www.veuno.com/x-formerly-twitter-ad-specs-your-guide-for-2026/ | Reported. [VERIFY] |
| Button labels | Install, Open, Play, Shop, Book, Connect, Order | https://www.veuno.com/x-formerly-twitter-ad-specs-your-guide-for-2026/ | [VERIFY: this list is for app buttons. Current website card labels not confirmed] |
| Sales objective layout | from 13 May 2025 the headline and a customisable CTA button sit below the image or video | https://www.socialmediatoday.com/news/x-formerly-twitter-updates-link-format-ads-adds-cta-button/748010/ | Reported, quoting X. [VERIFY: trade press, X page not read] |
| Promoted-only posts | created through a dedicated endpoint, they do not appear on the public timeline | https://docs.x.com/x-ads-api/campaign-management | verified 2026-10-06 |
| Account structure limits | 200 active campaigns, 100 line items per campaign, 8,000 active line items per account | https://docs.x.com/x-ads-api/campaign-management | verified 2026-10-06 |

Two layers, not Meta's five. An X ad has post text and, when you use a website card, a card headline and description. The anatomy of a Meta ad (image lines, primary text, headline, description, button) does not carry over. Write the post so it stands alone with no card.

## 3. Ad policy

The research pass could not open X's ad policy pages. Everything in this section is Reported or [VERIFY]. Read the live pages before you ship.

- Deceptive and fraudulent content. A search summary of X's policy says ads may not promote products with deceptive marketing, including clickbait that drives people to a landing page with "exaggerated, sensationalized, inaccurate language". Source: https://business.x.com/en/help/ads-policies/ads-content-policies/deceptive-and-fraudulent-content . [VERIFY: page returned 403, read the live page]
- Quality scoring. X's ad quality guidance, reported in August 2025, gives each ad an "aesthetic score". Reported criteria: grammar and punctuation, no more than one emoji (except in Japan and Korea), no hashtags, no URLs in the ad copy, no excessive cropping or gimmicky animation, no flashing or loud effects, a clear layout and a landing page that matches. A better score is reported to mean lower cost and better placement. X has not said whether advertisers will see the score or how much it changes price. Sources: https://www.medianama.com/2025/08/223-x-aesthetic-score-ad-pricing-change/ (6 August 2025) and https://www.adweek.com/media/x-will-give-brands-lower-ad-rates-for-aesthetic-ads-free-of-urls-emojis/ . [VERIFY: the Adweek date was unclear, and the current status is unconfirmed]
- Other prohibited areas, from search summaries of X's pages: misleading claims, health claims, adult content, tobacco and drugs. Price and landing page accuracy follow the same logic as on Meta. [VERIFY: X-specific wording on pricing and urgency]

Working rule for adquill: run the same policy lint as for Meta (references/policy.md). Block-tier phrases are block-tier on X too. Then add the X quality habits below.

| X quality habit | Why | Status |
|---|---|---|
| No hashtags | Reported scoring penalty, and they read as ad copy | Reported. [VERIFY] |
| No link text in the post | Reported scoring penalty. The link lives in the card | Reported. [VERIFY] |
| At most one emoji. adquill uses none | Reported scoring penalty. House style bans emoji anyway | Reported. [VERIFY] |
| Correct grammar and punctuation | Reported scoring criterion | Reported. [VERIFY] |
| Landing page matches the post | Reported criterion, and a policy matter | Reported. [VERIFY] |

## 4. A promoted post that does not look like an ad

Craft opinion, backed by X's own reported direction (no hashtags, no URLs in copy, at most one emoji, a clean image). Not a measured result. [VERIFY: craft opinion, test on a small budget]

What it looks like:

- One to three plain sentences in a human voice.
- No hashtags. No emoji.
- A real photo, not a stock shot, at 1.91:1 or 1:1 (check 4:5 support in your composer).
- The link in the card, not in the text.
- The facts in the post: place, price, a date or a window. A reader who never taps still learns the offer.
- One point of view, one honest constraint.

Weak and strong, fictional brief (Brekke Ski Guides does not exist, the price and dates are made up). The weak version sits in a lint ignore block because it is a deliberate pattern.

<!-- adquill-lint: ignore-start -->

Weak: Ready to elevate your winter? Join our unforgettable ski adventure in the Norwegian mountains! #ski #norway #adventure

<!-- adquill-lint: ignore-end -->

Strong: A guided ski touring day above Brekke costs NOK 4,900. Six skiers per guide, skins on at 09:15, back at the car by 15:30. Saturdays 9 Jan to 27 Feb.

The strong post is 148 characters. It has a price, a group cap, two clock times and a date window. Saturdays were checked: 9 Jan 2027 and 27 Feb 2027 are both Saturdays. The weak post has no number, no place a reader can verify and three hashtags. It could be the post of any company on earth.

Card for the strong post (both fields [VERIFY] until the live composer confirms the limits):

| Slot | Text | Count | Budget |
|---|---|---|---|
| post | the strong post above | 148 | 280 |
| card headline | Ski touring day, NOK 4,900 | 26 | 70 (50 recommended) [VERIFY] |
| card description | Beacon, shovel and probe included. Pick a Saturday and book online. | 67 | 200, about 125 visible [VERIFY] |

The card headline repeats the price and no sentence from the post. The card description adds a fact the post did not carry. If a card is not used, the post alone must still sell the day.

Use promoted-only posts for tests, so the account's public timeline stays clean (docs.x.com, verified 2026-10-06). Promote an existing organic post when it already has real replies, because real replies read as social proof. Do not manufacture replies.

## 5. Replies and quotes

- Replies and quotes on a promoted post appear as they do on any post. [VERIFY: no source found on whether advertisers can restrict replies on ads]
- Plan for replies before you spend. Someone will ask the price, the dates or whether the day is safe for a beginner. Answer in public with the same facts that are in the fact ledger. A reply is copy. It follows the same rules: no invented number, no promised outcome.
- Quote posts can carry your ad to people who did not choose to see it, with their commentary on top. You cannot write that text. This is another reason to keep every claim in the ad provable. [VERIFY: whether a promoted-only post can be quoted]
- Do not buy, trade or fake replies, likes or reposts. That breaks adquill's pledge.

## 6. Links

- A link in the post text counts 23 characters (Reported, see section 2). The aesthetic scoring reportedly dislikes URLs in the copy. Put the link in the card or the button and keep the text clean.
- Link handling in organic posts is disputed. Vendor and AI answers say posts with links get less organic reach. X's head of product said links are no longer deboosted, and the owner said "We haven't for over a year". Sources: https://www.freepressjournal.in/tech/x-product-head-nikita-bier-confirms-link-penalty-removed-over-a-year-ago-tells-mark-zuckerberg-he-can-post-them-directly (Reported) and https://www.niemanlab.org/2025/10/x-makes-overtures-to-journalists-with-new-feature-designed-to-improve-reach-for-links/ (October 2025, Reported). [VERIFY: current organic behaviour]
- For paid ads the link question matters less, because delivery is bought.
- The landing page shows the same price and the same dates as the post. A mismatch is a policy problem and a trust problem.

## 7. Threads

- A promoted post is one post. The first line has to stand alone. Do not write a hook that depends on the next post.
- A thread only helps an organic account that already has an audience. [VERIFY: whether a multi-post thread can be promoted as one unit]
- If the user wants a thread, write it as organic copy, label it so, and keep the same fact rules.

## 8. The 2026 platform state

Everything here is Reported or [VERIFY]. None of it is a plan.

- 30 April 2026: X began a phased rollout of a rebuilt, AI-driven ads platform with AI retrieval and ranking and "contextual and semantic" delivery. The trade press says the full platform is expected "later this year". Source: https://digiday.com/marketing/x-upgrades-its-ad-platform-in-long-overdue-overhaul/ . A trade source repeats that nearly all of the top 100 advertisers returned, according to X's head of global advertising. That is X's own claim. [VERIFY]
- CPM. Digiday-relayed figures put X's average CPM at $2.23 (2024), $1.05 (2025) and $0.64 (early 2026), against Facebook $4.93 and Instagram Reels $3.95. An agency report gives Q2 2026 X CPMs of $9 to $13 for website traffic campaigns and $8 to $10 for travel, with a 2.0 percent travel engagement rate (https://affectgroup.com/blog/x-advertising-cpm-benchmarks-for-the-united-states/ , 17 July 2026). The two sets cannot describe the same thing. The low figure looks like a blended average and the agency figure like a managed-account objective average. [VERIFY: both. Use neither to plan a budget]
- Revenue. X ad revenue is reported to be falling through 2025 and early 2026, with figures that range from about $1.8 billion to $2.46 billion depending on the source. [VERIFY]
- Return quality. One agency executive told Digiday that X "has struggled to keep up with its peers in direct-response advertising, and its returns have been subpar." That is one opinion. [VERIFY]
- Reported platform changes: a Sales objective layout with the headline and button below the media (13 May 2025), the aesthetic quality system (August 2025), the ad platform rebuild (30 April 2026).

Plain advice for the user: treat X as a test channel unless the business already has an audience there. Spend a small amount, compare cost per landing page view and cost per booking against Meta, and decide from your own numbers.

## 9. Audience reality

- Norway, as of October 2025, from DataReportal's Digital 2026 report, shown as ad reach and not as active users: Facebook 3.05 million (54.1 percent of the population), Instagram 2.65 million (47.0 percent), X 1.02 million (18.2 percent), TikTok 1.80 million adults (39.8 percent of those 18 and over), Snapchat 3.70 million (65.7 percent). Source: https://datareportal.com/reports/digital-2026-norway . [VERIFY: the figures reached the research pass through a page summariser]
- An earlier search summary cited 1.11 million X users in early 2025, which points to a falling trend. [VERIFY]
- Global monthly users are a third-party estimate of about 557 to 611 million, because X stopped publishing audited figures. Source: https://searchlab.nl/en/statistics/x-twitter-statistics-2026 . Status: Reported. [VERIFY: third-party estimate]
- The age, gender and interest profile of X users in Norway: no sourced data found. [VERIFY: pull it from X Ads audience insights, do not guess]
- Tone. People on X react badly to posts that look like ads. That is craft opinion, not a measured result. [VERIFY]
- Moment-based posts suit X: a snow report, a weekend with places left. This only works when the facts are real and current. A claim of "places left" needs a count and a date in the ledger.

If the user's market is not Norway, replace this section's figures with the reach numbers for that market from the same DataReportal series or from X's own audience tool.

## 10. Slot budgets for X output

| Slot | Budget | Status |
|---|---|---|
| post | 280 characters, a link counts as 23 | Reported. [VERIFY: X pages unreachable] |
| card headline (optional) | 70 maximum, 50 recommended | [VERIFY: Reported] |
| card description (optional) | 200 maximum, about 125 visible | [VERIFY: vendor figure] |

Counting rules:

- Count the real string in code, with spaces and the thousands comma in "NOK 4,900". Show the count beside the text.
- If the post carries a link, add 23 and not the length of the URL. adquill prefers no link in the post text.
- Both card fields carry the tag [VERIFY] in the output until the user confirms the limits in the composer.
- The post stands alone. A reader who sees no card still gets what, when, how much.
- No sentence appears in the post and in a card field.

## 11. Pre-flight checklist

1. Every number in the post is a ledger row marked allowed.
2. The price and dates match the landing page.
3. No hashtags, no emoji, no link text in the post.
4. No outcome promise, no invented scarcity (references/policy.md).
5. The image is a real photo, in a ratio your composer accepts, under 3 MB until the limit is confirmed.
6. The card limits were checked in the composer.
7. Someone owns the replies for the first week.
8. The user knows X is a test channel with thin evidence behind it.

## 12. Sources

Read on X's developer documentation, verified 2026-10-06:

- https://docs.x.com/x-ads-api/creatives
- https://docs.x.com/x-ads-api/campaign-management

Reported or Vendor (see the row tags):

- https://benly.ai/learn/x-ads/x-twitter-ads-formats-specs
- https://lettercounter.org/blog/twitter-ads-character-limits/
- https://www.veuno.com/x-formerly-twitter-ad-specs-your-guide-for-2026/
- https://www.socialmediatoday.com/news/x-formerly-twitter-updates-link-format-ads-adds-cta-button/748010/
- https://business.x.com/en/help/ads-policies/ads-content-policies/deceptive-and-fraudulent-content
- https://www.medianama.com/2025/08/223-x-aesthetic-score-ad-pricing-change/
- https://www.adweek.com/media/x-will-give-brands-lower-ad-rates-for-aesthetic-ads-free-of-urls-emojis/
- https://digiday.com/marketing/x-upgrades-its-ad-platform-in-long-overdue-overhaul/
- https://affectgroup.com/blog/x-advertising-cpm-benchmarks-for-the-united-states/
- https://datareportal.com/reports/digital-2026-norway
- https://searchlab.nl/en/statistics/x-twitter-statistics-2026
- https://www.freepressjournal.in/tech/x-product-head-nikita-bier-confirms-link-penalty-removed-over-a-year-ago-tells-mark-zuckerberg-he-can-post-them-directly
- https://www.niemanlab.org/2025/10/x-makes-overtures-to-journalists-with-new-feature-designed-to-improve-reach-for-links/
