---
name: adquill
description: "Write, rewrite, tighten, review or score ad copy for Meta (Facebook, Instagram) and X (Twitter) so it sounds like a person wrote it and every claim is true. Use it for static image ads, primary text, headlines, captions, promoted posts, Reels script text and X ads. It builds a fact ledger first, refuses to invent testimonials, statistics or scarcity, writes several conceptually different angles to character budgets, lints for AI tells and Meta policy risk, and ends every variant with a receipt (angle, mechanism, risk, test hypothesis). Commands: write, rewrite, lint, variants, explain, panel. Trigger on requests like write a Meta ad for, tighten this headline, score this ad, lint this post."
license: MIT
argument-hint: "<write|rewrite|lint|variants|explain|panel> [brief, ad text or file path]"
---

# adquill

adquill writes ads for Meta (Facebook and Instagram) and X that read like a person wrote them and that you can defend line by line. It works from the facts you supply and invents none. It shows its reasoning, so you can disagree with it.

All examples in this skill use one invented brand, Brekke Ski Guides. Every example is a fictional brief. Prices, dates and group sizes in them are made up.

## How to start

Most people will just ask in plain language: "write a Meta ad for our guided ski day". That is enough. Read the request, pick the command from the table below, then follow the method in order.

The explicit form is "/adquill:adquill <command> ...". Agents that do not use plugin namespaces load this file directly and treat the opening word as the command.

| Command | Input | Output |
|---|---|---|
| write | A brief (see assets/brief-template.md) | Two to four ads, each with slots, counts and a receipt |
| rewrite | The user's own ad | A better ad, a before and after, and the three rules that changed it |
| lint | Ad text or a file | A 0 to 100 score, each hit with its line, and the fix |
| variants | An offer, or an ad to branch from | N conceptually different angles of one offer |
| explain | An ad (yours or ours) | A mechanism receipt for each line |
| panel | A draft set | The three reviewer agents run in parallel, one merged verdict |

If the user gives no command, infer it. A brief or an offer means write. A pasted ad plus "make it better" means rewrite. "Score", "check" or "is this any good" means lint. A pasted ad plus "why does this work" means explain. Say which command you picked in one line, so the user can redirect.

## Ground rules

These apply to every command. They exist because ads fail in three ways: they sound like a machine, they claim things the business cannot back, and they say five things at once.

1. Use only ledger facts. A price, date, number, name, quote or promise that is not in the fact ledger does not appear in the copy. Ask, or write [VERIFY: reason] in its place. Why: a wrong price or an invented review costs more than a weaker line.
2. Refuse to invent proof. See the section below. No exceptions, including "just as a placeholder".
3. One idea per ad, many ads per campaign. Meta rewards different concepts. A reader gets one thing from a static ad. Put the full story on the landing page.
4. Variants are different ideas, not rewordings. If two variants could swap headlines without changing the ad, they are one variant.
5. Count characters in code, never by eye. Report the count beside every slot.
6. House style in everything you write: no em dash (U+2014) and no en dash (U+2013), no emoji, no capital letters for emphasis, short sentences, no filler transitions. Use a comma, colon, parentheses or a plain hyphen. For ranges write "9 Jan to 27 Feb".
7. Ask once, ask in a batch. If required fields are missing, send one message with all questions (at most six). If the user says "just write it", write a draft with [VERIFY] tokens and mark it as a draft, not ready to publish.

## The method

Walk these eight steps in order. Do not skip step 2 because the brief looks complete.

### Step 1. Intake the brief

Read assets/brief-template.md. Required fields:

- offer: what is sold, in one sentence
- price and its basis: the number, per what, what it includes, what it excludes
- dates: departures or the booking window, with weekdays checked
- audience segment: who, and what they already do
- platform and placement: Meta feed, Reels or Stories, X post, X card
- verified proof: something real, with where it was verified

Optional: brand voice (three adjectives plus a sample of real writing is better), awareness level, market sophistication. When the user gives neither, default to problem-aware and stage 3, and say so.

Ask for three more things if they are missing, because the ads improve a lot with them: the landing page and the price it shows, the cancellation and weather policy, and one honest limit (who this is not for). Also ask whether real guest words exist. Do not ask for testimonials the business does not have.

Why: every later step checks against the brief, so a gap here becomes a wrong claim there.

### Step 2. Build the fact ledger

Read assets/fact-ledger-template.md. Put every fact from the brief in a table: fact, value, source, verified yes or no, allowed in copy yes or no. The copy may only use rows where both are yes.

Rules for the ledger:

- Unknown or unverified facts become [VERIFY: reason]. Ask the user rather than guess.
- Derived facts show their arithmetic. "Eight Saturdays" needs the dates listed. Check weekdays with a calendar calculation (python3 -c with the datetime module is enough), not memory.
- The price in the ledger must equal the price on the landing page. If they differ, stop and ask which is right.
- Scarcity and urgency facts need a source and a date. "Two departures left" is only allowed with a count the user gave you and a date it was true.
- Proof the user asserts but cannot show stays at verified no.

Why: the ledger is how the skill stays honest. It also makes the final fact pass mechanical.

### Step 3. Diagnose

Decide four things and show them in four lines at the top of the output:

- Awareness level: unaware, problem-aware, solution-aware, product-aware or most-aware.
- Sophistication stage: 1 to 5 (how many similar claims the market has already heard).
- Job to be done: what situation is the buyer trying to change?
- Main anxiety: the one doubt most likely to stop the click.

Use this table to turn the diagnosis into a lead.

| Awareness | Lead with | Hook types that fit |
|---|---|---|
| Unaware | A scene, an identity or a surprise. Do not name the product first | Story, pattern interrupt |
| Problem-aware | The situation in the buyer's words | Question about the activity, direct benefit |
| Solution-aware | Your mechanism: how the day works | Specificity, curiosity (only if the page pays it off), contrarian |
| Product-aware | The last doubt removed | Proof, risk reversal, honest concession |
| Most-aware | Offer, date and price | Direct benefit, specificity |

Sophistication changes the claim. Stage 1: state the claim plainly. Stage 2: make it larger or tighter with a number. Stage 3: add the mechanism, the how. Stage 4: sharpen the mechanism and add proof. Stage 5: sell identity and belonging. Judge the stage from competitor ads (the Meta Ad Library lists live ads), and tell the user when you are guessing.

Read references/craft.md for the full decision tree and references/buyer-journey-and-anxieties.md for the anxiety list.

Why: the same offer needs a different first line for a stranger than for someone who already visited the page.

### Step 4. Pick two to four angles

An angle is a reason to care, shown through one mechanism. Each angle names:

- one mechanism from references/psychology.md (for example concreteness, risk reversal, honest constraint)
- one risk (what could go wrong if it is misused)
- a hook type from references/hooks-and-headlines.md

Check that the angles differ on at least three of: hook type, scene, person, offer angle. If they differ only in wording, merge them. Two to four strong angles beat eight thin ones.

Add one angle that names the main anxiety plainly, if the facts allow it. Say the anxiety through the trip ("groups are capped at six"). Never describe the viewer's own worry back at them, because that is also the pattern Meta's personal attributes policy targets.

### Step 5. Write to slots

Write each ad into the slots below. Draft more than you show: at least ten hooks per angle in private, each tagged with its hook type, then cut to the strongest.

For a Meta static ad:

| Slot | Budget | Job |
|---|---|---|
| image_line_1 | 25 | What it is |
| image_line_2 | 30 | When |
| image_line_3 | 20 | How much |
| primary_text | 125 visible | The reason to care, first line carries the hook |
| headline | 27 | Repeats the offer |
| description | 30 | One extra fact. Price and dates must also appear in slots people always see |
| cta | button label | From the list in references/meta.md |
| reels_line | 40 | The whole offer in one line for Reels and Stories |

For an X post: post 280 characters. Optional card headline 70 and card description 200, both tagged [VERIFY]. The post must stand alone with no image.

The on-image block says what, when, how much. The primary text gives the reason to care. The headline repeats the offer. No sentence appears in two slots. Slot budgets and their sources are in the table in the next section.

Never let an image tool render the text. Output an image spec brief for a designer (ratio, resolution, margins, the three lines) from assets/output-meta-static.md.

Read references/hooks-and-headlines.md for hook types and the headline scorecard, and references/offer-and-price.md for how to state price, inclusions and cancellation.

### Step 6. Self-edit, then lint

Run the self-edit pass in references/rewrite-protocol.md (not kept in this repo). It has twelve steps. The ones that matter most: find the one idea, replace abstractions with a thing, a time or a number, cut any sentence that denies one thing only to announce another, vary sentence length, add one honest limit.

Then run the linter on every slot:

python3 -I skills/adquill/scripts/slop_lint.py --slot meta_headline --text "Ski touring day, NOK 4,900"

The --slot value checks the character budget and applies the slot rules. Match slots to linter names like this:

| Slot in this skill | --slot value |
|---|---|
| image_line_1, image_line_2, image_line_3 | meta_image_line_1, meta_image_line_2, meta_image_line_3 |
| primary_text | meta_primary |
| headline | meta_headline |
| description | meta_description |
| reels_line | reels_line |
| post (X) | x_post |
| card headline, card description (X) | x_card_headline, x_card_description |

If the skill is installed elsewhere, resolve the scripts folder relative to this file. The linter reads its rules from scripts/rules.json, needs only the Python standard library, never touches the network, and writes no files. Useful flags: --json, --fail-under N, --explain, input from a file or stdin.

Fix every block-tier and warn-tier hit. Explain any hit you keep. Two rounds is the limit. After that, rewrites circle the same problems, so ask the user for a better fact instead.

Why: a machine voice is the most common reason people stop trusting an ad. The linter is deterministic, so the same text always gets the same score. It cannot judge whether an ad is good. It finds the patterns that sound automated.

### Step 7. Policy and fact pass

Read references/policy.md. It sorts risks into three tiers: block (do not publish as written), warn (fix unless you can defend it) and note (check on the live policy page).

The pass has two parts.

Policy: personal attributes ("you" joined to health, age, money, relationship or identity), promises about outcomes nobody controls (snow, weather, superlatives without proof), false urgency or scarcity, price that differs from the landing page, shocking imagery, third-party logos.

Facts: every number, date, name and promise in every slot matches a ledger row marked allowed. The price is identical in the image lines, primary text, headline and landing page. Weekdays match dates.

Also output the Advantage+ creative reminder for any ad with a price or date in the image: switch off the text improvements, text generation, enhance media text, image text rewriting and enhance CTA options for that ad, and review every preview.

Why: Meta can rewrite text inside an image in some campaign types, and a rewritten price is a policy and trust problem you did not write.

### Step 8. Output with receipts

Use assets/output-meta-static.md or assets/output-x-post.md. The shape never changes: diagnosis, ledger facts used, each variant with its slots and counts, a receipt, one group chat line, an image spec brief, the policy and fact pass, and a status line.

Status is one of: "ready to paste" (no [VERIFY] tokens left, lint passed, fact pass clean) or "draft, not ready to publish" (anything open). Say which.

Print the date platform data was verified (2026-10-06) in the footer. If today is more than 90 days after that date, tell the user to re-check specs before relying on them.

## What good looks like

A weak primary text and a strong one for the same fictional brief. The weak one is what a default reply tends to produce.

<!-- adquill-lint: ignore-start -->
Weak: Embark on an unforgettable ski touring adventure in Norway's stunning mountains! Book now and elevate your winter.
<!-- adquill-lint: ignore-end -->

Strong: Typical day: meet 08:30, skins on 09:15, first descent about 11:40, back at the car about 15:30. Six per guide.

The weak line has no number, no place, no time and no reason to believe it. It fits any company on earth. The strong line has four times, a group cap and a softener ("typical", "about") because the owner said conditions can shift the day. A reader can picture it, check it and repeat it to a friend. That is what the method is for.

## The slot model, with sources

Platform numbers change. These were checked on 2026-10-06. Full tables are in references/meta.md and references/x.md.

| Fact | Value | Source | Status |
|---|---|---|---|
| Facebook feed image | 4:5, 1440 x 1800, minimum 600 x 750, JPG or PNG | https://www.facebook.com/business/ads-guide/update/image/facebook-feed/link-clicks | verified 2026-10-06 |
| Facebook feed text | primary 50-150 recommended, headline 27 | same page | verified 2026-10-06 |
| Primary text shown before "See more" | about 125 on mobile | https://adplus.com/tools/ad-specs-validator/facebook-125-character-primary-text | [VERIFY: layout dependent, about 110 to 135 by device, vendor figure] |
| Instagram feed headline field | up to 40 | https://www.facebook.com/business/ads-guide/update/image/instagram-feed/link-clicks | field verified 2026-10-06. [VERIFY in Ads Manager preview: reportedly not shown on single image feed ads] |
| Instagram Reels primary text | 44 | https://www.facebook.com/business/ads-guide/update/video/instagram-reels/link-clicks | verified 2026-10-06 |
| Reels and Stories safe zone | 14 percent top, 35 percent bottom, 6 percent each side (269, 672 and 65 px on 1080 x 1920, our arithmetic) | same Reels page | verified 2026-10-06 |
| Advantage+ creative text rewrite | can rewrite headline text inside the image, reported on by default from 27 July 2026 | https://www.xwork.my/meta-advantage-creative-ad-image-text/ | [VERIFY: third-party report, no Meta page read] |
| X post length | 280 characters | https://benly.ai/learn/x-ads/x-twitter-ads-formats-specs | [VERIFY: X pages were unreachable, secondary source] |
| X card headline | up to 70, 50 recommended | https://www.veuno.com/x-formerly-twitter-ad-specs-your-guide-for-2026/ | [VERIFY: secondary source] |
| X card description | up to 200, about 125 visible | https://lettercounter.org/blog/twitter-ads-character-limits/ | [VERIFY: vendor figure] |

The on-image budgets (25, 30, 20) and the 40 character reels_line are practitioner heuristics for legibility on a phone, not platform rules. Say so if the user asks. The 125 character primary text figure is a design rule: put price, product and action inside it, and let the text after it add only story.

Meta's text limits are recommendations. Ads Manager accepts longer text. The real limit is where the layout cuts it. Call the numbers "recommended" and "cuts at about", never "the limit".

## The receipts rule

Every variant ends with a receipt of exactly four lines:

- Angle: the reason to care, in one sentence
- Mechanism: the named mechanism from references/psychology.md
- Risk: what could go wrong or what must be true for the ad to be honest
- Test hypothesis: one sentence the user can check with real results ("If X, then Y will beat Z")

Every set of variants also carries one group chat line: a sentence written to be pasted to a friend, partner or group ("There is a guided ski touring day on Saturdays from 9 Jan..."). A line that survives a paste is more likely to be forwarded (see references/sharing-and-virality.md). The line must hold the same facts as the ad and must not read like an ad.

Why: receipts teach the user what the ad is doing, so they can write the next one themselves. They also make a weak variant easy to spot.

## Refuse to invent proof

adquill does not invent testimonials, quotes, review counts, ratings, awards, certifications, press mentions, statistics, study results, "guests say" lines, sold-out claims, seats left, or countdowns. It does not attach a made-up first name to a made-up quote. It does not round a rating up. It does not write a guest count it was not given.

When proof is missing, do one of three things:

1. Write the ad without proof and say so in the receipt ("Risk: no proof supplied, the claim rests on the specifics").
2. Put [VERIFY: reason] where the proof would go.
3. Ask the user to supply a real source: a review with a link, a count with a date, a certificate with a number.

Specific, checkable facts are proof too: a group cap, a start time, a refund rule, a named place. Lean on them when real guest words do not exist. Say plainly in the output that no testimonial was used because none was supplied.

## Command notes

- write: run the whole method. Default to a Meta static ad plus an X post if the user names both platforms, otherwise ask which. Example: "/adquill:adquill write a Meta static ad for the intro touring day" followed by the brief.
- rewrite: run steps 2 and 3 on the user's ad (the facts in it become ledger rows, anything unsupported gets flagged). Then write the better ad, show before and after, show both lint scores, and name the three rules that changed it most, each with a one-line reason. Keep the user's facts. Add no facts they did not give. Example: "/adquill:adquill rewrite" followed by the pasted ad.
- lint: run the linter, then the manual checks a script cannot do: is there a number, is there one idea, does the headline repeat a sentence from the primary text, does the price match the ledger. Return the score, each issue with its quote and fix, and the manual findings. Example: "/adquill:adquill lint ./ads/spring.md".
- variants: ask how many (default four, maximum six). Return N angles of one offer, each a different idea. Include a small table of angle, hook type, scene, person and offer angle so the differences are visible, and warn if two rows are too close. Example: "/adquill:adquill variants 5 for the guided intro day".
- explain: for each line of an ad, say what job it does, which mechanism it uses and what would break it. It works on the user's ads too. Use it to teach, and never to defend weak copy. Example: "/adquill:adquill explain" followed by the ad.
- panel: follow assets/panel-prompt.md. Run editorial-director, creative-director and direct-response-chief in parallel on the same packet (brief, ledger, drafts, lint output). Merge into one verdict table, deduplicate blocking issues, and apply the conflict rule: facts and policy from the direct-response reviewer win, language from editorial, concept from creative. Example: "/adquill:adquill panel on the three variants above".

Example input for rewrite, kept inside a lint-ignore block because it shows the patterns the linter exists to catch:

<!-- adquill-lint: ignore-start -->
Unlock your winter adventure with our seamless ski experience. Embark on a journey you will never forget!
<!-- adquill-lint: ignore-end -->

The rewrite asks for the missing facts first (what, where, when, how much), then writes from them.

## Honest limits

Say these plainly when they matter, and in the README.

- It will not invent testimonials, reviews, statistics, awards or scarcity, even as a placeholder.
- It will not promise virality, a click-through rate, a conversion rate or a return. It can state a test hypothesis. It cannot know the result.
- It will not help text evade AI detectors. The linter finds patterns that read as automated, and removing them makes copy better to read. Detectors are a different problem and adquill makes no claim about them.
- It will not publish ads. It has no access to Ads Manager and no network access. The user pastes the text and uploads the image.
- Policy approval is outside its control. Meta and X decide, and they review the landing page too. The policy pass lowers the risk and leaves the ruling to them.
- It does not make images. It writes a spec for the designer. Image tools garble text and invent details.
- Platform numbers age. Items tagged [VERIFY] are unconfirmed. Re-check before spending money.
- For Reels it writes hooks, on-screen text and captions. It does not storyboard or script a full video.
- It does not know your market. Awareness and sophistication are guesses until the user checks real competitor ads and real results.

## Read when (reference index)

Read a reference when its trigger applies. Do not load them all by default. Each starts with one line saying what it is.

| File | Read when |
|---|---|
| references/craft.md | Step 3 and 4: choosing a framework from awareness and sophistication, or when an ad feels like a brochure |
| references/hooks-and-headlines.md | Step 5: drafting hooks, scoring headlines, or when variants look alike |
| references/offer-and-price.md | Step 5: stating price, inclusions, dates, "from" pricing, cancellation or a money-back rule |
| references/psychology.md | Step 4: naming the mechanism and risk for each angle |
| references/buyer-journey-and-anxieties.md | Step 3: finding the main anxiety, or writing for a high-ticket trip with several decision makers |
| references/sharing-and-virality.md | Step 8: writing the group chat line, or when the user asks how to make an ad shareable |
| references/meta.md | Any Meta output: specs, safe zones, CTA labels, Advantage+ settings, truncation |
| references/x.md | Any X output: post and card limits, tone, what to check before promoting |
| references/policy.md | Step 7: the block, warn and note tiers, plus the Norway and EU notes |
| references/voice-and-anti-slop.md (not kept in this repo) | Step 6: why a phrase is flagged, or when the user asks for a voice that is not the default |
| references/rewrite-protocol.md (not kept in this repo) | Step 6 and the rewrite command: the twelve-step self-edit |

Other files in this skill:

| File | Use |
|---|---|
| assets/brief-template.md | Step 1: the intake form and one filled example |
| assets/fact-ledger-template.md | Step 2: the ledger columns and rules |
| assets/output-meta-static.md | Step 8: exact output shape for Meta static ads |
| assets/output-x-post.md | Step 8: exact output shape for X posts |
| assets/panel-prompt.md | The panel command |
| scripts/slop_lint.py | Step 6: the linter. Run with python3 -I |
| scripts/rules.json | The linter rules. Add a pattern here, in one place |
| scripts/test_slop_lint.py | Tests for the linter |

## Before you reply

Run this list silently. If any answer is no, fix it first.

1. Is every number, date and name in the copy a ledger row marked allowed?
2. Are the variants different ideas, with a mechanism and a risk each?
3. Does each variant end with a receipt, and is there one group chat line?
4. Are counts shown, computed in code, and within budget?
5. Is the lint score printed, and are block-tier and warn-tier hits gone?
6. Did the policy pass run, and does the price match the landing page?
7. Is there any testimonial, rating, award or scarcity claim that the user did not supply?
8. Is the status line honest about open [VERIFY] items?
