# Ad policy checklist: the block, warn and note tiers for Meta and X, plus the Norway and EEA layer

What this is: the risk reference for step 7 (policy and fact pass). Read it before you call any draft "ready to paste", and whenever a user asks "will this get rejected?". Platform policy summarised as of 2026-10-06.

## Contents

1. How the three tiers work
2. The risky phrase table
3. Meta personal attributes
4. Price and landing page mismatch
5. Promised results and unrealistic outcomes
6. False urgency and scarcity
7. Testimonials, ratings and statistics
8. Imagery match
9. Text in images, logos and edited creative
10. Norway and EEA layer
11. X
12. Worked example
13. Pattern families for the linter
14. Sources

## 1. How the three tiers work

Meta reviews the image, every text field and the landing page. Most rejections and many account-quality problems come from five areas: a personal attribute joined to "you", a price that differs from the landing page, a promised outcome nobody can promise, false urgency, and imagery that does not match the offer. The tiers sort those risks by what you do next.

| Tier | Meaning | What adquill does |
|---|---|---|
| block | Do not publish as written. Either the platform forbids it or the claim cannot be proven. | Rewrite it or remove it. If it stays, the status line says "draft, not ready to publish". |
| warn | Probably fixable, and risky as written. | Fix it, or write one line saying why the claim is defensible and which ledger row proves it. |
| note | A thing to check on the live page or in the preview. | List it under "Before you publish". |

Rules that apply in every tier:

- The linter finds phrases. It cannot find a wrong price. The fact pass (every number against the ledger, the landing page price pasted in by the user) finds those, and a mismatch is a block.
- Only ledger facts may appear. A missing fact becomes [VERIFY: reason]. adquill does not make up a proof point to clear a warning.
- Policy pages change. Read the live page before you spend money. Section 14 lists them.

Evidence for this file: Meta's Advertising Standards index, the personal attributes page, the prohibited commercial practices page and the violent and graphic content page were read (verified 2026-10-06). Meta's misleading claims page returned 404, so that part rests on vendor summaries and carries [VERIFY]. X's policy pages returned 403 (see section 11).

## 2. The risky phrase table

These are the patterns the linter and the manual pass look for. The table quotes risky phrases on purpose, so it sits inside a lint ignore block. The examples are written for the fictional brief (Brekke Ski Guides does not exist, prices are made up).

<!-- adquill-lint: ignore-start -->

| Family | Risky pattern | Tier | Why | Safer pattern |
|---|---|---|---|---|
| Personal attribute | "Are you [age, health, religion, money, relationship, identity]?" for example "Are you over 50 and still skiing?" | block | Meta bans copy that asserts or implies a personal attribute | Describe the trip: "Ski touring days, six per guide." |
| Personal attribute | "Do you have [condition]?" | block | Health status | Describe the offer, never the viewer's body |
| Personal attribute | "Meet other [attribute] near you", "Ski trips for seniors" | block | Names the viewer as a member of a group | "A ski week with a lesson every day." Say nothing about who the viewer is |
| Personal attribute | "Can't afford the Alps?", "Rich enough to ski Norway?" | block | Financial situation | "NOK 4,900 for the day, guide and beacon included." |
| Personal attribute | "Your knee will thank you", "Scared of the slopes?", "Out of shape?" | warn | Reads as health or mental state [VERIFY: borderline] | "Gentle terrain. A guide at the front and one at the back." (only if true) |
| Personal attribute | "Are you a beginner?" | warn | Ability is not on Meta's list, the pattern is the same [VERIFY] | "First day on skins? We start with 40 minutes of practice." (only if true) |
| Personal attribute | "Single? Join our ski week" | warn | Relationship status [VERIFY] | "Solo skiers welcome" (only if true) |
| Personal attribute | "[First name], this tour is for you" | block | Names the viewer | Do not personalise by name or trait |
| Promised result | "guaranteed snow", "guaranteed powder", "aurora guaranteed", "summit guaranteed", "100% safe", "risk-free" | block | Unrealistic or unprovable outcome | "Season runs December to April." "We pick the route the evening before, from the forecast." |
| Promised result | "always", "never fails", "every guest", "perfect conditions" | warn | Absolute claim | State the real rate or the real rule |
| Promised result | "Safe off-piste" | block | Unprovable safety claim | State the process: "Route chosen the evening before from the avalanche forecast." (only if true) |
| Promised result | "Best", "number one", "most scenic in Norway", "world-class" | warn | Superlative without proof on the landing page | "The most scenic day we run." (own range) |
| False urgency | countdown timer, "ends tonight", "book before midnight" with no real end | block | False urgency. Meta flags it, and Norwegian rules treat false timers as misleading | A real date: "Last departure 27 Feb." |
| False urgency | "Only 3 left", "few places left" with no ledger count and date | block | False scarcity | "Six places per departure" (a true cap), or the live count with its date |
| False urgency | "Last chance", "don't miss out", "selling fast" | warn | Pressure without a fact behind it | Replace with the date or the cap |
| Price | image, text, headline and landing page show different prices | block | Price mismatch | One number everywhere, copied from the landing page |
| Price | "per person" or "per group" not stated on the page | warn | Basis unclear | Write "from NOK 4,900" until the basis is confirmed |
| Price | "Was NOK 6,900, now NOK 4,900" with no earlier price in the ledger | block | Reference price must be real. The 30 day reference rule is for goods, and general misleading-marketing rules still apply to services | Drop the "was" price, or put the real earlier price and its dates in the ledger |
| Price | "Save 30%" with no base price | warn | Percentage the ledger does not support | State the price |
| Price | "free", "included" not matching the booking terms | warn | Terms mismatch | Copy the inclusion list from the terms page |
| Proof | an invented review, rating, star count, guest number or study | block | Fabricated proof | Use a real ledger row, or write [VERIFY: reason] |
| Proof | "4.9 stars" with no platform, count or date | warn | Needs a named source | "4.8 on ExampleReviews, 31 reviews, checked 2026-10-01" (fictional) |
| Proof | "Guests rave", "thousands of happy skiers" | warn | Vague attribution | One real quote with a name and permission, or drop it |
| Proof | a quote with no name | warn | Cannot be traced | "Anna K., guest, Feb 2026" with her permission |
| Format | fake news or editorial layout ("Local guide shocks experts") | block | Deceptive format [VERIFY: vendor summary] | Plain ad layout |
| Imagery | injury, crash or graphic risk | block | Meta bans shocking or sensational imagery | A clean action shot |
| Imagery | helicopter, avalanche or cliff stunt shown as the product | warn | Reviewer and audience read it as a risk claim [VERIFY: how reviewers treat it] | Show the product as sold |
| Brand | Meta logos or names used to imply endorsement, a third-party logo without rights | block | Intellectual property rules | Name the place, skip the logo |
| Alcohol | drinks shown or named | warn | Restricted goods, needs 18+ targeting | Skip it, or set 18+ |
| Creator content | paid creator post with no "reklame" or "annonse" label (Norway) | warn | Marketing must be identifiable | Add the label and use the branded content tool |

<!-- adquill-lint: ignore-end -->

## 3. Meta personal attributes

The rule, from Meta's page: ads must not contain content that asserts or implies personal attributes. Source: https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/ , verified 2026-10-06.

Categories on that page, as read: race and ethnicity, religion, age, sexual orientation, gender identity, physical or mental health, disability, financial status, voting status, trade union membership, criminal record and name. [VERIFY: exact wording of the financial category and the full list on the live page]

The pattern to catch is two parts in one line:

1. The viewer is addressed or grouped by an opener.
2. The next words state an attribute from the list.

The openers sit in an ignore block because they are the banned pattern itself.

<!-- adquill-lint: ignore-start -->

Openers: "Are you ...", "Do you have ...", "Meet other ...", "... near you", or a first name.

The exact opener most advertisers trip on is "Are you" plus an attribute, as in "Are you over 50?". adquill treats that as block tier.

<!-- adquill-lint: ignore-end -->

Examples Meta lists as prohibited, as read on the page and in the research notes. They are real policy examples and they sit in an ignore block.

<!-- adquill-lint: ignore-start -->

- "Are you Christian?"
- "Do you have diabetes?"
- "Are you 18 years old?"
- "Are you bankrupt? Check out our services."
- "Meet other seniors"
- "Meet other black singles near you!"
- "Billy Taylor, get this t-shirt"

Examples Meta shows as allowed: broad references and "you" language without an attribute, such as "Date Christian singles!", "Meet seniors" and "A service for teens". [VERIFY: the research pass read one inconsistent pair on this page, one allowed item appeared on both lists. Read the live page.]

<!-- adquill-lint: ignore-end -->

What follows from those examples:

- The word "you" is not the trigger. "Book your day" is fine. The trigger is "you" joined to a protected attribute. Reported by https://www.jonloomer.com/qvt/can-we-use-the-words-you-or-your/ and https://www.stackmatix.com/blog/meta-ads-personal-attributes-policy . [VERIFY: Vendor, not read on Meta's page]
- A descriptor of the offer is safe. A label for the viewer is not. "A ski week with a lesson every day" describes the offer. "For beginners who are nervous" labels the viewer.
- Skill level (beginner, intermediate, advanced) is not a listed attribute. Fear, injury and fitness language drifts toward health. Age and health are the two categories an outdoor ad touches most. Write about what the trip is and what happens on it.
- Targeting and copy are separate checks. Do not write copy that implies you targeted by an attribute.
- A fact stated as a trip rule is fine when it is not aimed at the viewer: "Guests need to be in good physical health" belongs on the landing page, not in the headline.

Self-check, three questions for every line with "you" or "your":

1. Does the next noun phrase name an age, a health state, a disability, a money state, a relationship, a religion or an identity?
2. Could the line make a reader think "how do they know that about me?"
3. Can the line be rewritten about the trip, the guide or the day with no loss of meaning?

If the first or second answer is yes, rewrite the line. If the third answer is yes, rewrite it anyway. The safer line costs nothing.

## 4. Price and landing page mismatch

Meta's standards index lists relevance requirements: ads must accurately represent the offering and match the landing page. Source: https://transparency.meta.com/policies/ad-standards/ , verified 2026-10-06 (index read). Vendor reports say the reviewer opens the landing page in real time and that broken links and thin pages are rejection reasons (https://adsuploader.com/blog/meta-ad-guidelines). [VERIFY: Vendor]

Procedure, every time:

1. Ask the user for the landing page URL and the price it shows. Paste it into the ledger. If the user cannot paste it, the price is [VERIFY: landing page price not supplied].
2. Compare it with the price in all four places: the on-image line, the primary text, the headline and the description.
3. Check the basis: per person or per group, per day or per trip, taxes and mandatory fees included, "from" price and what the cheapest option is.
4. Check the dates against the page, and the weekdays against a calendar.
5. Check inclusions. Words like "included" and "free" must match the booking terms exactly.
6. Check the page works on a phone, loads, and shows the product in the ad.

If the price differs, stop. Ask which is right. Do not publish an ad that differs from its landing page, and do not "fix" it by guessing. A stale price on the page is the owner's problem to correct before the ad runs.

A "from" price is allowed when the landing page shows that starting price. If the page shows a range under one "from", show the range or pick the product the price belongs to.

## 5. Promised results and unrealistic outcomes

Meta's prohibited commercial practices page bans practices that mislead for financial gain. The page names deceptive pricing, unauthorized endorsements and investment return promises as examples. Source: https://transparency.meta.com/policies/ad-standards/deceptive-content/prohibited-commercial-practices/ , verified 2026-10-06. The misleading claims page returned 404. Vendor summaries agree that ads must not deceive or fail to deliver the promised benefit and that unsupported statistical claims get flagged (https://www.auditsocials.com/blog/meta-ad-misleading-claims-personal-attributes-prohibited-content-policy-2026 and https://adsuploader.com/blog/meta-ad-guidelines). [VERIFY: wording and any 2026 changes, read the live page]

For outdoor and travel offers the dangerous outcomes are the ones nature controls: snow, weather, aurora, summits, descents and safety. The rule is simple. Promise the process, not the result.

<!-- adquill-lint: ignore-start -->

Words in this family: guarantee, guaranteed, risk-free, safe, safest, always, never, every, perfect, best, number one, world-class.

<!-- adquill-lint: ignore-end -->

<!-- adquill-lint: ignore-start -->

| Promise the result (block) | Promise the process (safe) |
|---|---|
| Fresh tracks sorted | Fresh tracks on the better days. We pick the route the evening before. |
| See the aurora on our tour | Clear nights give you a chance. Our guide checks the forecast each evening. |
| Safe off-piste | The route follows the avalanche forecast, and the guide turns the group around when it says so. |
| The best tour in Norway | The most scenic day we run |

<!-- adquill-lint: ignore-end -->

Check each outcome claim against the business's real terms. If the terms say "no refund for weather", the ad does not say "come rain or shine".

## 6. False urgency and scarcity

Meta flags fake countdown timers and false scarcity, according to vendor summaries (https://adsuploader.com/blog/meta-ad-guidelines and the Meta misleading claims page, which did not load). [VERIFY: read the live page]. Norwegian regulator guidance also treats false timers and untrue limited-quantity claims as misleading (section 10).

Urgency is allowed when it is true. A real date is the strongest urgency you can write.

<!-- adquill-lint: ignore-start -->

| True urgency (allowed) | False urgency (block) |
|---|---|
| "Saturdays 9 Jan to 27 Feb." A finite, real window | A timer that resets when the page reloads |
| "Six places per departure." A real group cap | "Only 3 left" with no live count behind it |
| "Booking closes 20 Dec" when the owner confirmed that date | "Book before midnight" with no midnight deadline |
| "Two places left on 16 Jan, as of 2026-10-06" with the count and date in the ledger | "Selling fast" with no sales data |

<!-- adquill-lint: ignore-end -->

The ledger rule: a scarcity or urgency fact needs a count, a source and the date it was true. If it is older than the ad's run, the line comes out or becomes a question for the owner.

## 7. Testimonials, ratings and statistics

adquill does not invent testimonials, ratings, reviews, guest counts or statistics. It says so, and it refuses to write a placeholder quote "just for layout". A missing proof point becomes [VERIFY: reason] and a question to the user.

What a usable piece of proof looks like in the ledger:

| Proof type | Needs | Example row (fictional brief, invented values) |
|---|---|---|
| Rating | Named platform, score, review count, date checked, URL | 4.8 on ExampleReviews, 31 reviews, checked 2026-10-01, example.test/reviews |
| Guest quote | Verbatim text, guest name (or initial), date, written permission, where it was published | "We were back at the car by half past three." Anna K., guest, Feb 2026, permission on file |
| Guest count | The count, the period, the source system | 412 guests, 2025 season, booking system export |
| Statistic or study | The figure, the publisher, the date, the URL | Do not use one unless the user supplies the source |
| Award or press | The name, the year, the link | Do not use one unless the user supplies the link |

Rules:

- The quote must be real, attributable and typical. Vendor summaries say Meta wants testimonials to represent a typical guest outcome. [VERIFY: Vendor, read the live page]
- Quote the words, not a summary of them. Do not tidy them into ad language.
- Vague crowd praise needs a ledger row that proves the number behind it. Without one, drop the line.
- A rating needs a platform and a count. "4.9" alone is a warn. A rating with no real source is a block.
- Fake or paid reviews are treated as misleading marketing under general rules in most EEA countries. [VERIFY: confirm with the national regulator]
- Reviews from a creator or partner that were paid for must be labelled as advertising (section 10).

## 8. Imagery match

The picture is a claim. Meta reviews it with the text and the landing page.

- Match the product. A backcountry photo does not sell a resort day. A summer photo does not sell a winter departure.
- Show the thing as sold. Group size in the photo should look like the group size in the text.
- Show the safety kit the product uses. If the guide requires helmets or beacons, the photo shows them. This is a trust matter and a reviewer matter. [VERIFY: reviewer treatment is a vendor report]
- Keep action shots clean. Meta's violent and graphic content page bans imagery that is "shocking, gruesome, or otherwise sensational in nature" and says ads must not contain "shocking, sensational or excessively violent content". Source: https://transparency.meta.com/policies/ad-standards/objectionable-content/violent-graphic-content/ , verified 2026-10-06. The page text read says nothing about extreme sports or stunts. [VERIFY: how reviewers treat crashes, avalanches or helicopter drops]
- Use real photos of real guests with their consent. If a person in the image is generated or retouched, say so (section 10).
- Do not use a third-party logo (a lift company, a gear brand, a venue) in a way that implies a partnership. Naming a place in plain text is normally fine. [VERIFY: nominative use of a place name, brand logos need permission]

## 9. Text in images, logos and edited creative

- The old 20 percent text rule was removed in September 2020. Meta still said at the time that images with less text generally perform better. Sources: https://adzooma.com/blog/facebook-advertising-removes-20-text-rule-on-images/ and https://www.socialmediatoday.com/social-networks/facebooks-changed-20-ad-image-text-overlay-rule . The claim that heavy text gets less delivery today is vendor lore. [VERIFY]
- Advantage+ creative can rewrite text inside an image and the copy around it. A rewritten price or date is a mismatch you did not write and cannot see until you check. Switch the text options off for any ad with a price or a date, and compare the running ad with the approved one. The full checklist is in references/meta.md, section 12.
- Do not use Meta's logos or names in a way that implies endorsement. Follow Meta's brand resource rules. Source: https://transparency.meta.com/policies/ad-standards/ (intellectual property section, index read).
- Creator and partner content goes through the branded content tool, as the standards index lists under Branded Content.

## 10. Norway and EEA layer

General terms only. Each row carries [VERIFY: confirm with the regulator or a lawyer] because the research pass read regulator pages as summaries.

| Topic | Plain statement | Source | Status |
|---|---|---|---|
| Price information | Price information includes taxes and mandatory fees. A "from" price that applies only to some options needs the range shown | https://www.forbrukertilsynet.no/vi-jobber-med/reise-og-transport | Reported. [VERIFY] |
| "Was" prices on services | For goods marketed as reduced, the reference price is the lowest price used for at least 30 days before the marketing starts. The regulator's page says that rule does not apply to services, such as guided tours. The general ban on misleading marketing still applies, so a "was" price must reflect a real earlier price | https://www.forbrukertilsynet.no/vi-jobber-med/prismarkedsforing/salg-og-bruk-av-forpriser | Reported. [VERIFY: whether a package that includes goods changes this] |
| Limited-quantity claims | A claim that places or tickets are limited must be true and clear. False countdown timers are treated as misleading | https://www.forbrukertilsynet.no/lov-og-rett/veiledninger-og-retningslinjer/forbrukerombudets-retningslinjer-markedsforing-flybilletter-tilbys-begrenset-antall-billetter-annonsert-pris | Reported. The guideline concerns flight tickets. [VERIFY: apply the principle, check for a rule that covers your product] |
| Labelling paid creator content | Marketing must be identifiable (Marketing Control Act, section 3). "Reklame" or "annonse" count as clear labels. A platform tool alone may not be enough | https://www.forbrukertilsynet.no/vi-jobber-med/reklame-i-sosiale-medier/ofte-stilte-sporsmal-om-reklame-i-sosiale-medier | Reported. [VERIFY: confirm the label wording on the regulator page] |
| Retouched people in ads | Norway has a guideline on labelling retouched advertising | https://www.forbrukertilsynet.no/english/guidelines/the-norwegian-consumer-authoritys-guideline-on-labelling-retouched-advertising | [VERIFY: the page returned 404, scope unknown, including whether generated people count]. Safe rule: real photos of real guests with consent, and say if a person is generated |
| Package travel | An offer that combines at least two kinds of travel service (transport, accommodation, other significant tourist services) for the same trip may be a package, which brings information duties and a financial protection scheme | https://lovdata.no/lov/1995-08-25-57 | [VERIFY: the act cited in the research notes may have been replaced, find the current package travel act on lovdata.no and confirm with a lawyer whether your trips are packages] |
| EU Digital Services Act | Meta's standards list beneficiary and payer identification for ads in the EU | https://transparency.meta.com/policies/ad-standards/ | [VERIFY: whether Norway, as an EEA country, is in scope yet] |
| Less personalised ads | Meta rolled out a less personalised ads choice to all EEA users in January 2026. Reports say it reduces the signal available to delivery | https://ppc.land/metas-2026-dma-report-reveals-whatsapp-ads-a-eu200m-fine-and-a-defiant-stance-on-personalized-advertising/ and https://seresa.io/blog/meta-dma-less-personalized-ads/metas-lpa-rollout-just-split-your-eu-audience-into-two-tiers | Reported, Vendor. [VERIFY: Norway coverage and effect] |
| Teen targeting | Meta says age and location are the only information advertisers can use to target 13 to 17 year olds | https://www.techbuzz.ai/articles/meta-bows-to-eu-pressure-with-new-ad-choice-model-for-2026 | Reported. [VERIFY: find Meta's primary page] |
| Location fees | Meta charges location fees on ads delivered in the UK (2%), France, Italy and Spain (3% each) and Austria and Turkey (5% each), effective May 2026 and billed from 1 July 2026. Norway was not listed in anything read | https://www.mediapost.com/publications/article/413378/meta-passes-eu-digital-services-tax-to-advertisers.html | Reported (10 March 2026). If you target those markets, budget 2% to 5% extra. [VERIFY: trade press, no Meta page read] |

What this means for the copy:

- Show prices with taxes and mandatory fees included, or say what is extra.
- No "was" price on a service without a real, dated earlier price in the ledger.
- No limited-places line without a true count and date.
- Label creator posts "reklame" or "annonse" when the user is in Norway, and use the platform's branded content tool as well.
- Real people, real consent, and a plain note when a person in an image is generated.
- If the offer is a multi-service trip, ask the owner whether package travel rules apply before you write the ad.

## 11. X

The research pass could not open X's policy pages (the fetcher got status 402 and 403). The working rule: apply the same claim rules as on Meta, because X forbids misleading claims and deceptive marketing too, per search summaries. Block-tier phrases stay block on X. Add the X habits in references/x.md: no hashtags, no link text in the post, no emoji. [VERIFY: X-specific wording on pricing and urgency, read the live page]

## 12. Worked example

A draft a hurried marketer or a default model reply might produce, for the fictional brief. It is a deliberate bad example, so it sits in an ignore block.

<!-- adquill-lint: ignore-start -->

Draft: Are you over 50 and still skiing? Guaranteed fresh snow on every Brekke tour. Only 3 spots left, book before midnight! Rated 4.9 by thousands of happy skiers. Was NOK 6,900, now NOK 4,900.

| Hit | Tier | Reason |
|---|---|---|
| "Are you over 50" | block | Age attribute joined to "you" |
| "Guaranteed fresh snow" | block | Promised outcome nobody controls |
| "Only 3 spots left" | block | No count or date in the ledger |
| "book before midnight" | block | No real midnight deadline |
| "Rated 4.9 by thousands" | block | No platform, no count, no date. Invented proof |
| "Was NOK 6,900" | block | No earlier price in the ledger |
| "happy skiers" | warn | Vague attribution |

<!-- adquill-lint: ignore-end -->

Rewrite, using only ledger facts (fictional brief): "Six skiers per guide. Saturdays 9 Jan to 27 Feb, NOK 4,900. We pick the route the evening before, from the forecast."

That is 116 characters, inside the 125 visible budget. It has a cap, a date window, a price and an honest process. Saturdays were checked (9 Jan 2027 and 27 Feb 2027 are both Saturdays). It makes no claim about snow, no claim about the viewer and no claim about scarcity. Every number on it can be checked on the landing page.

## 13. Pattern families for the linter

The linter owner turns these families into rules. Tier is the default. The score weight is the linter's choice.

<!-- adquill-lint: ignore-start -->

| Family id | Default tier | Detects |
|---|---|---|
| attr-opener | block | "Are you", "Do you have" followed within a few words by an age, health, disability, money, relationship, religion or identity word |
| attr-group | block | "Meet other", "for seniors", "singles near you", "[attribute] near you" |
| attr-adjacent | warn | "you" or "your" near fear, fitness, injury, beginner, out of shape, single, couple |
| outcome-promise | block | guarantee, guaranteed, risk-free, 100% safe, sure thing, never fails |
| outcome-absolute | warn | always, never, every guest, perfect conditions |
| superlative | warn | best, number one, world-class, most (with a place or category) and no ledger proof |
| urgency-false | block | countdown, ends tonight, before midnight, only N left, last few places, with no ledger fact |
| urgency-soft | warn | last chance, selling fast, don't miss out, hurry |
| price-was | block | was NOK, now NOK, "was" followed by a price, with no earlier price in the ledger |
| price-percent | warn | save N percent, N% off, with no base price in the ledger |
| proof-invented | block | star ratings, review counts, "thousands of guests" with no ledger source |
| proof-vague | warn | guests love, travellers rave, happy customers |
| format-fake-news | block | breaking, shocking discovery, "local guide shocks experts" |
| alcohol | warn | beer, wine, cocktail, après drinks |
| platform-slot | block | a slot over its budget when run with --slot |

<!-- adquill-lint: ignore-end -->

A price mismatch with the landing page has no phrase to match. The fact pass catches it, and the skill runs that pass by hand.

## 14. Sources

Meta policy pages (read, verified 2026-10-06):

- https://transparency.meta.com/policies/ad-standards/
- https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/
- https://transparency.meta.com/policies/ad-standards/deceptive-content/prohibited-commercial-practices/
- https://transparency.meta.com/policies/ad-standards/objectionable-content/violent-graphic-content/

Vendor and trade summaries (Reported or Vendor):

- https://www.auditsocials.com/blog/meta-ad-misleading-claims-personal-attributes-prohibited-content-policy-2026
- https://adsuploader.com/blog/meta-ad-guidelines
- https://www.jonloomer.com/qvt/can-we-use-the-words-you-or-your/
- https://www.stackmatix.com/blog/meta-ads-personal-attributes-policy
- https://adzooma.com/blog/facebook-advertising-removes-20-text-rule-on-images/
- https://www.socialmediatoday.com/social-networks/facebooks-changed-20-ad-image-text-overlay-rule
- https://megadigital.ai/en/blog/facebook-ads-rejected/
- https://madgicx.com/blog/facebook-ad-rejected
- https://www.brandwatch.com/blog/facebook-ad-policies-why-your-ads-arent-getting-approved/
- https://gripasmarketing.com/meta-ads-claims-personal-policy/

Norway and EEA:

- https://www.forbrukertilsynet.no/vi-jobber-med/prismarkedsforing/salg-og-bruk-av-forpriser
- https://www.forbrukertilsynet.no/vi-jobber-med/reise-og-transport
- https://www.forbrukertilsynet.no/lov-og-rett/veiledninger-og-retningslinjer/forbrukerombudets-retningslinjer-markedsforing-flybilletter-tilbys-begrenset-antall-billetter-annonsert-pris
- https://www.forbrukertilsynet.no/vi-jobber-med/reklame-i-sosiale-medier/ofte-stilte-sporsmal-om-reklame-i-sosiale-medier
- https://www.forbrukertilsynet.no/english/guidelines/the-norwegian-consumer-authoritys-guideline-on-labelling-retouched-advertising
- https://lovdata.no/lov/1995-08-25-57
- https://ppc.land/metas-2026-dma-report-reveals-whatsapp-ads-a-eu200m-fine-and-a-defiant-stance-on-personalized-advertising/
- https://seresa.io/blog/meta-dma-less-personalized-ads/metas-lpa-rollout-just-split-your-eu-audience-into-two-tiers
- https://www.techbuzz.ai/articles/meta-bows-to-eu-pressure-with-new-ad-choice-model-for-2026
- https://www.mediapost.com/publications/article/413378/meta-passes-eu-digital-services-tax-to-advertisers.html

X:

- https://business.x.com/en/help/ads-policies/ads-content-policies/deceptive-and-fraudulent-content

This is a checklist, not legal advice. Read the live platform policy page.
