# Itinerary download emails

Status: draft, awaiting approval. Nothing in this folder has been sent. The emails here replace the follow-up sequence that goes out after someone downloads a tour itinerary, for the 7-Day Bergen to Tromsø trip and the 6-Day Alta trip. Read this file first, then the two sequence files.

| File | What it holds |
|---|---|
| [7-day-bergen-tromso-sequence.md](7-day-bergen-tromso-sequence.md) | Seven emails for the 7-Day Northern Lights Tour, Bergen to Tromsø, plus one optional check-in |
| [6-day-alta-sequence.md](6-day-alta-sequence.md) | Seven emails for the 6-Day Alta trip, plus one optional check-in |
| [fact-check-report.md](fact-check-report.md) | Claim-by-claim check of both sequences against the live pages, with the corrections made and the open questions |

Every fact in the emails comes from the live tour pages, the blog posts and the policy pages listed under Sources, all fetched on 26 October 2026, or from `campaigns/ski-meta-ads/tours.json`. Anything the site does not publish is marked `[CONFIRM ...]` in the draft and listed under Decisions needed. Do not send an email that still carries a `[CONFIRM]` marker.

## Why the old sequence did not move people

The original emails got the facts right. Six things held them back.

- Every email had the same shape: a list of six things and a button back to the itinerary the reader already had. Nothing in the sequence was new information after Email 2.
- No email answered the questions a buyer works through before paying NOK 31,000 to 41,000: how much, what is included, how do I get there, what if I cancel, what if we see nothing, can I physically do it. The price appeared nowhere.
- The two "manners" per email doubled the writing with no hypothesis behind them. At the volumes a download list produces, a body-copy test cannot reach a result; subject lines can.
- The last two emails introduced the other tour at the moment the reader should be deciding. Adding a choice at decision time lowers conversion (Iyengar and Lepper 2000).
- The "ask me a question" email asked for a question without naming the questions people actually have, so it asked the reader to do the work.
- They carried no social proof, no risk reversal and no true deadline.

## The new spine

One version per email. Each email answers the next question a buyer asks and asks for one small step. Days count from the download.

| Email | Day | The reader's question | The step we ask for | Button goes to |
|---|---|---|---|---|
| 1 (existing delivery email) | 0 | What is this? | Open the itinerary | Itinerary PDF |
| 2 | 2 | When, and which week? | Reply with the month or week | Season guide (blog) |
| 3 | 5 | Can I do it? | Check yourself against the requirements | Tour page, day by day |
| 4 | 9 | What if we see nothing? | Accept the odds, keep reading | Aurora blog for that base |
| 5 | 13 | How much, for what, and what if I cancel? | Forward to the travel partner | Tour page, price and inclusions |
| 6 | 18 | What is stopping me? | Reply with the one thing | Reply by email |
| 7 | 25 | Is it time to decide? | Request your dates | Tour page, date request |
| 8 (optional) | 40 | Still interested? | Reply or request dates | Tour page |

Stop rules: stop the sequence when the person books, requests dates, or replies "not this year". A reply to any email goes to a person, and the next scheduled email still goes out unless the reply changes the stop rule.

Suggested edit to Email 1, the delivery email: add the price line ("From NOK 41,181 including taxes" or "NOK 31,000 including taxes") and one question ("Which month are you thinking of? Reply and tell me."). The sequence then starts with a known price, and the reply gives the team something to work with from day 0.

## Rules applied

- Voice and the do-not-claim list from `.claude/product-marketing.md`. No group size numbers, no age limits, no "all gear included", no "slots left", no "per person", no guaranteed sightings, no guaranteed departures.
- The rating appears once per sequence as "4.9/5 on Tripadvisor", the form the tour pages use.
- The Tripadvisor review page and the site's own reviews page are not linked: the reviews page shows no winter trips and no named rating source.
- The cross-sell to the other tour appears once, in Email 3, as an honest exit line, and once more in Email 7 as one of three questions. Nowhere else.
- Every button URL was fetched live on 26 October 2026. Links to the month guide and the Alta guide use the blog URLs as published; their slugs contain words the voice guide avoids, which is fine for a URL and a page title but not for our own sentences.
- No scarcity wording. The only deadline used is the real one: the full-refund cut-off 60 days before departure, as published on the tour pages.

## Decisions needed before anything is sent

1. Cancellation terms. The tour pages and the terms page give a 60, 45 and 30 day scale (full refund, 75%, 50%, none). The flexible booking page promises a 14-day risk-free window and a lifetime deposit on 90 days notice. Which applies to these two trips? Email 5 and Email 7 depend on the answer.
2. Deposit and balance. No page states the deposit amount or when the balance is due. Email 5 needs "Hold your place with NOK X, balance due Y days before departure" or it stays vague.
3. What the date request does. Is "Request your dates" a question that the team answers, or does it take payment? Email 7 says "a question, not a booking". Confirm.
4. Sender. The emails are signed "Mate". The team page lists no one by that name. Decide who signs, with their role, and whether a reply is answered within a stated time or a call can be offered. Email 6 depends on this.
5. Alta in April. The Alta trip is sold for November to April; the Alta blog puts the aurora season at September to the end of March. Email 2 for Alta treats April as a daylight-heavy month with a smaller aurora window. Confirm the wording or shorten the sold season.
6. The whale cruise. Confirm it runs in every month the trip is sold, or which months it does not. Email 3 for Alta names it without a caveat.
7. Single travellers. Rooms are twin-share on the 7-Day. Is there a single supplement or a share option? Email 7 asks "who is coming" and cannot answer the solo case.
8. Age and licence rules. The 7-Day page states a minimum age; the Alta page says activities may have age or licence requirements confirmed before departure. The voice guide forbids age limits in copy, so the drafts say "confirmed before departure" and nothing more. Fine, or do you want the number?
9. Ski gear on the 7-Day. The Day 3 page text reads as if gear is included; the inclusions list says it is not, rentals can be arranged. The drafts follow the inclusions list. Fix the page text or confirm the drafts.
10. Manner 1 and Manner 2 are dropped. If you want a test, test the subject lines (two per email, listed in each sequence file) and keep one body.

## Principles used, and where they came from

- The buying decision as a sequence of questions. The repo research (`docs/research/ad-copy/02-psychology-influence.md`) orders them: what is this; when and how long; how much for what; can I do it; is it safe and reputable; what if I cannot go; who else is going. The spine follows that order, so each email gives the reader the next thing they need.
- Second reader. A trip at this price is rarely a solo decision. Email 5 is written to be forwarded and says so.
- Commitment and consistency (Cialdini, Influence). Small public steps lead to larger ones, so Email 2 asks for a reply with a month before anyone asks for money.
- Reciprocity (Cialdini). Each email gives something useful before asking: a season guide, a fitness check, the real odds, the full price breakdown.
- Social proof (Cialdini; Google Decoding Decisions 2020, where it was the largest single lever in travel). Used once per sequence, with a named source and number.
- Two-sided messages raise credibility (Eisend 2006, meta-analysis of 87 studies). Each sequence says plainly that the aurora is not guaranteed and names who the trip is not for.
- Loss aversion and risk reversal (Kahneman and Tversky, prospect theory). The cancellation terms and the insurance line reduce the cost of a wrong decision, which matters more than adding benefits at this stage.
- Choice overload (Iyengar and Lepper 2000). The reader sees five dated departures instead of an open calendar, and the other tour appears only in Email 3 and Email 7, where a choice is being closed.
- Anticipation (Kumar, Killingsworth and Gilovich 2014). Experiences pay back before they happen. Email 4 and Email 7 describe specific evenings and days so the reader can picture them.
- Fogg Behaviour Model (B = MAP). For a NOK 17,000 and up purchase, ability is the binding constraint, so every email cuts effort: one button, one ask, the numbers in one place.
- Honest deadline. The Norwegian Marketing Control Act and EU rules treat invented scarcity as unlawful. The only deadline used is the published refund cut-off.

## Measurement and test plan

- Track per email: open rate, click rate on the one button, reply rate, and date requests within 30 days of download.
- The number that matters is date requests per 100 downloads. The second is replies to Email 2 and Email 6.
- Test subject lines only, two per email, and keep the body. Decide after a full month of sends.
- Review the sequence each quarter: dates roll over, prices change and blog URLs can move. Re-run the link check (below) before each season.

Link check: every URL in both sequence files should return a 200.

```
grep -ho 'https://www\.outdoornorway\.com/[A-Za-z0-9_./?=%-]*' campaigns/itinerary-download-emails/*.md | sort -u | while read u; do printf '%s ' "$u"; curl -s -o /dev/null -w '%{http_code}\n' "$u"; done
```

## Sources

All fetched on 26 October 2026.

| Page | URL | Used for |
|---|---|---|
| 7-Day tour page | https://www.outdoornorway.com/multi-day-tour/northern-lights-tour-bergen-tromso | Price, dates, inclusions, exclusions, requirements, cancellation scale, rating, day headings |
| 6-Day Alta tour page | https://www.outdoornorway.com/multi-day-tour/norway-northern-lights-tour-package | Price, flexible dates, inclusions, exclusions, requirements, hotels, day-by-day plan, cancellation scale, rating |
| Tour data | `campaigns/ski-meta-ads/tours.json` | 7-Day day-by-day plan and departures, checked with `verify_tours.py` on 26 October 2026 |
| Season guide (blog) | https://www.outdoornorway.com/blog/best-time-to-see-northern-lights-in-norway | Month descriptions, 20:00 to 02:00 window, Visit Norway note on spring activity |
| Tromsø aurora guide (blog) | https://www.outdoornorway.com/blog/tromso-norway-northern-lights | How guides choose a spot, several nights, "think in nights", displays return |
| Alta aurora guide (blog) | https://www.outdoornorway.com/blog/alta-norway-northern-lights | Alta latitude, Finnmarksvidda, Gargia, season, clouds, dress for standing still, 6 pm to 1 am |
| Where to see the lights (blog) | https://www.outdoornorway.com/blog/best-places-to-see-the-northern-lights-in-norway | Tromsø under the aurora oval, Alta versus Tromsø |
| Can you see the lights in Norway (blog) | https://www.outdoornorway.com/blog/can-you-see-the-northern-lights-in-norway | "Think in nights, not hours" |
| Skiing in Voss (blog) | https://www.outdoornorway.com/blog/why-voss-is-a-skiing-paradise-near-bergen | Voss Resort green slopes for first-timers, rentals, train from Bergen |
| Snowshoeing for beginners (blog) | https://www.outdoornorway.com/blog/snowshoeing-tour-a-beginners-guide | Few easy techniques, low-impact |
| Bergen in winter (blog) | https://www.outdoornorway.com/blog/bergen-norway-winter | Daylight by February, Bergen's seven mountains |
| 7-Day packing FAQ | https://www.outdoornorway.com/faq/what-should-i-bring-with-me-for-7-day-ski-fjord-norway-aurora-tour | Packing list sent before the trip, list of items |
| Flexible booking | https://www.outdoornorway.com/flexible-booking | 14-day window and lifetime deposit (conflict, see Decisions) |
| Terms and conditions | https://www.outdoornorway.com/terms-and-conditions | Cancellation scale, insurance advice, payment before departure |
| Travel insurance | https://www.outdoornorway.com/travel-insurance | Insurance recommendation |
| Tailor-made trips | https://www.outdoornorway.com/tailor-made-adventures | Optional Email 8 line for people whose dates do not fit |
| Northern lights hub | https://www.outdoornorway.com/northern-lights-tours-norway | Both tours on one page; not linked from the emails because it carries "slots left" and "all gear included" |
| Our team | https://www.outdoornorway.com/our-team/ | Sender check (no Mate listed) |
