# Output shape: X posts

The exact output adquill returns for an X (Twitter) promoted post. Read it at step 8 of the method when the platform is X. The filled example uses the fictional brief from assets/brief-template.md.

X has two text layers, the post and the website card. Do not copy the Meta layout onto it. The post must stand alone with no image, because it is the only thing a reader is sure to see.

## Rules for this output

1. One section per variant. Each variant is a different idea, in a different shape (a plain list, a person talking, a single statement). Four posts with the same three-beat shape read as a machine.
2. The post is at most 280 characters. Show the count. Line breaks count as characters.
3. The card headline and card description are optional. Tag both [VERIFY] because X's own spec pages could not be read, and show their counts against the reported limits.
4. No hashtags, no link in the post text (the link lives in the card), no emoji. These are style choices that follow X's reported ad quality direction [VERIFY: reported, not read from X].
5. The post carries the fact in line one or two: the thing, the date, the price.
6. No sentence appears in two slots.
7. Every variant ends with a receipt: Angle, Mechanism, Risk, Test hypothesis.
8. One group chat line, one image or card spec, a policy and fact pass with tiers, and a status line.
9. Say that X is a secondary channel for most small advertisers, and that the user should compare cost per landing page view with Meta.

## Slots and sources

| Slot | Budget | Source | Status |
|---|---|---|---|
| post | 280 characters | https://benly.ai/learn/x-ads/x-twitter-ads-formats-specs | [VERIFY: X pages unreachable, secondary source] |
| card_headline | up to 70, 50 recommended to avoid truncation | https://www.veuno.com/x-formerly-twitter-ad-specs-your-guide-for-2026/ | [VERIFY: secondary source] |
| card_description | up to 200, about 125 visible | https://lettercounter.org/blog/twitter-ads-character-limits/ | [VERIFY: vendor figure] |
| link inside the post | counts as 23 characters, so keep it in the card | https://benly.ai/learn/x-ads/x-twitter-ads-formats-specs | [VERIFY: secondary source] |
| card image | 1.91:1 at 1200 x 675, or 1:1 at 1080 x 1080 | same benly page | [VERIFY: 4:5 reported by one source, not by another] |
| image file size | 5 MB (benly) or 3 MB (X Ads API docs) | https://docs.x.com/x-ads-api/creatives | [VERIFY: sources conflict, use the smaller until you check Ads Manager] |

## The shape

```text
# X posts: <offer>
Brief: <brand> (fictional brief, if it is an example)
Status: <ready to paste | draft, not ready to publish> (<reason>)
Platform data verified 2026-10-06 where marked, otherwise [VERIFY]

## Diagnosis
Awareness level / Sophistication stage / Job to be done / Main anxiety

## Ledger facts used
<rows used> and <rows not used>

## Post 1: <angle name>
Post (n/280):
<the post text, line breaks as they will appear>

| Slot | Text | Count | Budget |
|---|---|---|---|
| card_headline | | n | 70 [VERIFY] |
| card_description | | n | 200 [VERIFY] |

Hook type: <type>
Lint: <score>/100

Receipt
- Angle:
- Mechanism:
- Risk:
- Test hypothesis:

## Post 2 and Post 3 (same shape, different idea and shape)

## Angle check
| Post | Hook type | Shape | Person | Offer angle |

## Group chat line
<one sentence to paste to a friend>

## Card spec (for the designer)
<ratio, size, file size, who adds text, photo direction>

## Policy and fact pass
Block / Warn / Note / Fact check

## Before you publish
<card link, landing page price, preview check>
```

## Filled example (fictional brief)

Everything below belongs to a fictional brief. Brekke Ski Guides does not exist. The prices, dates and numbers are made up.

---

# X posts: Intro to ski touring

Brief: Brekke Ski Guides (fictional brief)
Status: ready to paste, after the card and preview checks under "Before you publish"
Platform data verified 2026-10-06 where marked, otherwise [VERIFY]

## Diagnosis

- Awareness level: problem-aware (given)
- Sophistication stage: 3 (guessed)
- Job to be done: do something different with a weekend that the buyer can already almost do
- Main anxiety: "am I good enough", then "what if it is called off"
- Channel note: X reaches about 1.02 million people in Norway as ad reach, against about 3.05 million for Facebook (DataReportal, figures as of October 2025, https://datareportal.com/reports/digital-2026-norway) [VERIFY: figures came through a page summariser]. Treat X as a test channel.

## Ledger facts used

NOK 4,900 per person. Saturdays 6 Feb to 27 Mar 2027, eight departures. Six people per guide. Red runs with control required. Typical day times. Gear hire NOK 650 extra. Free cancellation up to 7 days before. Full refund or another Saturday if the guide calls the day off for avalanche risk. Guide, avalanche kit loan and route planning included. Taught: skins, kick turns, transceiver.

Not used (not verified or not allowed): guide certification, guest reviews, seats left, any superlative.

## Post 1: The plain list

Post (173/280):

```text
Guided ski touring day. Saturdays, 6 Feb to 27 Mar 2027.

Six people per guide. Typical day: meet 08:30, back at the car about 15:30.

NOK 4,900. Gear hire is NOK 650 extra.
```

| Slot | Text | Count | Budget |
|---|---|---|---|
| card_headline | Guided ski touring day, NOK 4,900 | 33 | 70 [VERIFY] |
| card_description | Guide, avalanche kit loan and route planning included. Free cancellation until 7 days before. | 93 | 200 [VERIFY] |

Hook type: specificity
Lint: LINT_P1

Receipt
- Angle: the whole offer in three lines a reader can screenshot.
- Mechanism: concreteness and price transparency (what is and is not included).
- Risk: false precision on the times. The post says "typical" and "about".
- Test hypothesis: if a plain, complete post suits a cold X audience, this post gets a lower cost per landing page view than Post 3.

## Post 2: The rule, in a person's voice

Post (184/280):

```text
If we call the day off for avalanche risk, you pick another Saturday or take a full refund. That holds for all eight Saturdays, 6 Feb to 27 Mar 2027. NOK 4,900 a person, six per guide.
```

| Slot | Text | Count | Budget |
|---|---|---|---|
| card_headline | Day called off? Rebook or refund | 32 | 70 [VERIFY] |
| card_description | Intro to ski touring, guided. Gear hire is NOK 650 extra. | 57 | 200 [VERIFY] |

Hook type: direct benefit, written as a rule
Lint: LINT_P2

Receipt
- Angle: the cancellation worry answered with a rule, spoken by the people who make the call.
- Mechanism: risk reversal (cancellation and safety refund).
- Risk: overselling the refund. The post states only the avalanche rule. Match the booking terms word for word before it runs.
- Test hypothesis: if the call-off worry blocks bookings, this post gets more landing page views from people who clicked an earlier post.

## Post 3: The entry bar

Post (182/280):

```text
You need to ski red runs with control. That is the entry bar for our intro to ski touring. We teach skins, kick turns and the transceiver. Saturdays, 6 Feb to 27 Mar 2027. NOK 4,900.
```

| Slot | Text | Count | Budget |
|---|---|---|---|
| card_headline | First ski tour, NOK 4,900 | 25 | 70 [VERIFY] |
| card_description | Guide, avalanche kit loan and route planning included. Gear hire is NOK 650 extra. | 82 | 200 [VERIFY] |

Hook type: honest concession (a contrarian hook)
Lint: LINT_P3

Receipt
- Angle: name the entry bar first, so the right people stop scrolling.
- Mechanism: honest constraint that answers the level anxiety with a fact.
- Risk: reads as exclusion. The post states a requirement of the day and says nothing about the reader's body, age or fitness.
- Test hypothesis: if self-selection raises click quality, this post has fewer clicks than Post 1 and a higher share of clickers who reach the dates.

## Angle check

| Post | Hook type | Shape | Person | Offer angle |
|---|---|---|---|---|
| 1 | specificity | three short blocks | the curious first-timer | the day and the price |
| 2 | direct benefit | one long sentence, then a short one | the cautious planner | the refund rule |
| 3 | honest concession | four sentences, rising | the confident resort skier | who it is for |

The three shapes differ on purpose. No two rows match on more than one column.

## Group chat line

Found a guided intro to ski touring: Saturdays 6 Feb to 27 Mar, six people per guide, NOK 4,900. You need to ski red runs. Want to book one?

140 characters. Same facts as the posts.

## Card spec (for the designer)

This brief is fictional.

- Image: 1.91:1 at 1200 x 675 px, or 1:1 at 1080 x 1080 px [VERIFY: X pages unreachable, secondary source https://benly.ai/learn/x-ads/x-twitter-ads-formats-specs].
- File size: keep the file under 3 MB until you have checked Ads Manager. Sources say 5 MB (benly) and 3 MB (https://docs.x.com/x-ads-api/creatives) [VERIFY: conflict].
- Text on the image: none needed. The post carries the facts, and a clean image fits X's reported quality direction [VERIFY]. If a price pill is wanted, set the type by hand, and never let an image tool render it.
- Photo direction: a real photo of a real group on skins in daylight, faces visible, taken by the brand with consent. No stock, no generated people, no third-party logos.
- The link goes in the card, not in the post text.

## Policy and fact pass

Block: none.

Warn:
- Post 2: refund wording must match the booking terms exactly.

Note:
- No hashtags, no link in the post, no emoji, in line with the reported ad quality direction (https://www.medianama.com/2025/08/223-x-aesthetic-score-ad-pricing-change/) [VERIFY: dates and current status].
- Post 3: "You need to ski red runs with control" is a requirement of the offer, not a claim about the reader.
- X policy pages could not be read for this check. Read the live deceptive and fraudulent content policy before you spend (https://business.x.com/en/help/ads-policies/ads-content-policies/deceptive-and-fraudulent-content) [VERIFY].

Fact check: 6 Feb 2027 and 27 Mar 2027 are Saturdays (calendar calculation). Every number maps to a ledger row: 4,900, 650, 6, 8, 08:30, 15:30, 7. Typical times carry "typical" or "about". No testimonial, rating, certification or seat count appears.

## Before you publish

1. Set the card link to the landing page that shows NOK 4,900 per person and the eight dates.
2. Preview each post on a phone-sized view. Check that the line breaks in Post 1 survive.
3. Start with a small budget. Compare cost per landing page view with Meta before you add spend.

Platform data verified 2026-10-06 where marked, otherwise [VERIFY]. adquill does not publish ads. Check the live policy pages before you spend.

---

Sources

- X post and card specs (secondary, X pages unreachable) [VERIFY]: https://benly.ai/learn/x-ads/x-twitter-ads-formats-specs, https://www.veuno.com/x-formerly-twitter-ad-specs-your-guide-for-2026/, https://lettercounter.org/blog/twitter-ads-character-limits/
- X Ads API creatives (image size, carousel): https://docs.x.com/x-ads-api/creatives
- X ad quality direction, reported: https://www.medianama.com/2025/08/223-x-aesthetic-score-ad-pricing-change/
- Norway audience figures: https://datareportal.com/reports/digital-2026-norway [VERIFY]
