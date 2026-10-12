# Buyer psychology and influence for high-ticket experiential purchases

Research notes for adwright (open source Claude Code skill for Meta and X ads) and the Outdoor Norway client job.
Prepared 2026-10-06. Topic: how people decide to buy a NOK 17,000 to 42,126 guided ski trip, and how copy should respond.

Style note: these notes follow the client style rules (no dashes as punctuation, no emojis, no shouting caps). Where a number appears, a URL sits next to it or the tag [VERIFY: reason] does.

---

## 0. How to read these notes

### Evidence grades used

| Grade | Meaning |
|---|---|
| A | I opened the primary source (paper PDF, official policy, original report) and checked the number myself. |
| B | I read a reputable secondary summary or the abstract page. The number is probably right but I did not see it in the paper. |
| C | Practitioner, vendor or trade-press source. Treat as a hypothesis. |
| T | Theory or book. Widely cited, no single number to check. |

### Fetch problems (stated plainly)

- Think with Google pages (thinkwithgoogle.com) now redirect to business.google.com/think. Several older articles no longer open. The messy middle report itself (PDF, July 2020) opened fine and I read it in full.
- The Expedia Path2Purchase 2023 PDF was over the 10 MB fetch limit. I used trade-press summaries of it (grade B).
- Loewenstein's 1994 curiosity paper opened only as an image scan. I could not read it. The information-gap summary below is grade B/T.
- Several publisher pages (Wiley, Sage, Harvard-hosted PDF, Forbes) returned 403. Where that matters I say so.
- Meta's own ad standards page for personal attributes opened. The wording below comes from it (grade A, fetched 2026-10-06 via a summarising fetch tool, so confirm in the live policy before shipping).

### The ten rules in one place

1. The ad does not sell the trip. It starts or restarts a decision that runs for weeks and passes through other people.
2. Google's own experiment found social proof was the largest or second-largest lever in 28 of 31 categories. Specific, real reviews beat adjectives.
3. Scarcity was the weakest of six levers in Google's tests and can feel restrictive to someone still exploring. Use it only when true, and only late in the journey.
4. Experiences pay back in anticipation. The ad can sell the weeks of looking forward, not only the days on snow.
5. For NOK 17,000 and up, ability (money, time off, brain effort, social friction) is the binding constraint. Cut effort first, add motivation second.
6. The person who clicks is rarely the only person who must say yes. Write so the ad survives being pasted into a group chat.
7. Name the anxiety through the trip, never through the viewer. "Groups are split by level" passes Meta policy. "Worried you are too unfit?" does not.
8. Show the total price, what it covers, and what it costs to cancel. Per-day framing is a supplement, never a replacement.
9. Fake urgency is illegal in Norway and the EU, and Meta can reject it. It is also the weakest lever. There is no upside.
10. Several famous findings are shaky (loss aversion size, decoy effect in real settings, some Ariely work). adwright should prefer principles with independent support.

---

## 1. Evidence quality map (read before using any principle)

The behavioural science canon is uneven. A copy skill that treats every principle as equally solid will overclaim. This table sets the confidence level adwright should attach.

| Principle | Origin | Status in 2026 | Confidence for ad copy |
|---|---|---|---|
| Social proof | Cialdini; Google/Behavioural Architects 2020 | Strong in applied tests. Google found it largest or second-largest in 28 of 31 categories. | High |
| Authority | Cialdini; Google 2020 | Real but smaller than social proof. Works most where buyers lack domain knowledge. | Medium-high |
| Scarcity | Cialdini; Google 2020 | Most often the least effective of six levers in Google's simulation. Legal exposure when faked. | Low-medium, true use only |
| Power of free | Shampanier, Mazar, Ariely 2007; Google 2020 | Google replicated the idea in its own simulation: largest or second-largest in 18 of 31 categories. Ariely integrity caveat applies to him, but Google's test is independent. | Medium-high |
| Anchoring | Tversky and Kahneman 1974 | Classic. Effects in real price contexts are real but smaller than lab numbers, and weaker for experts. | Medium |
| Loss aversion | Kahneman and Tversky 1979; 1992 | Contested. Gal and Rucker 2018 argue the evidence does not support "losses loom larger" as a general law. Contingent versions survive. | Medium, use gently |
| Framing | Tversky and Kahneman 1981 | Holds across many settings. | Medium-high |
| Decoy (asymmetric dominance) | Huber, Payne, Puto 1982; Ariely | Frederick, Lee and Baskin 2014 found it largely vanishes with realistic, non-numeric stimuli. | Low for ski trip tiers |
| Choice overload | Iyengar and Lepper 2000 | Scheibehenne et al 2010 meta-analysis: mean effect near zero, large variance. Fires when options are many, similar and the buyer is unsure. | Medium, conditional |
| Mental accounting | Thaler 1985 | Well supported. | Medium-high |
| Endowment effect | Kahneman, Knetsch, Thaler 1990 | Supported in many settings, weaker for items bought for exchange. | Medium |
| Experiential over material | Van Boven and Gilovich 2003 and follow-ups | Large literature, consistent direction. | High |
| Anticipation boost | Kumar, Killingsworth, Gilovich 2014; Nawijn 2010 | Consistent direction. | High |
| Regret of inaction in the long run | Gilovich and Medvec 1995 | Replication attempt exists (Collabra 2022). I could not open the result. | Medium [VERIFY: replication outcome] |
| Fogg B=MAP | Fogg | Practical model, little formal test. | High as a design checklist |
| Forces of progress | Moesta | Practitioner model from interviews, not a lab result. | High as an interview and copy tool |

### Note on Dan Ariely

Ariely is cited in many marketing decks (decoy, power of free, social versus market norms). Facts as of this research:

- A 2012 PNAS honesty-pledge paper co-authored by Ariely was retracted in 2021 after Data Colada showed the insurance data were fabricated. All five authors agreed the data were fake and denied making it up themselves ([Big Think summary](https://bigthink.com/the-present/honesty-pledge-study-fraud-dan-ariely/), grade B).
- Retraction Watch reports a 2002 Psychological Science paper on procrastination and deadlines (Ariely and Wertenbroch) was retracted on 2 September 2026 after Data Colada found signs of tampering. The same report says a 2008 Journal of Marketing Research paper and a 2004 Psychological Science paper carry expressions of concern ([Retraction Watch, 3 Sept 2026](https://retractionwatch.com/2026/09/03/procrastination-study-duke-dan-ariely-psychological-science-data-colada-tampering-retraction/), grade B). The 2004 Psychological Science paper may be Heyman and Ariely, "Effort for payment" [VERIFY: I did not confirm which 2004 paper].
- Consequence for adwright: use Ariely's concepts only where independent evidence exists. The zero-price effect is backed by Google's own simulation. Social versus market norms has a replication-and-extension paper in Collabra 2022 that I could not open [VERIFY outcome]. Never cite "Ariely found" as the reason for a copy choice.

**How adwright should use this.** Attach a confidence label to every principle the skill invokes. In output notes, say "social proof (high confidence)" or "decoy (low confidence, skip)". When the skill must choose between two levers, it picks the higher-confidence one. It never writes "studies show" without a named source it can print.

---

## 2. The classic frameworks, translated for a ski trip

### 2.1 Cialdini: seven principles plus Pre-Suasion

Cialdini's Influence (first edition 1984, cited in Google's report as Collins) named six principles. The 2021 "New and Expanded" edition adds a seventh, unity. Pre-Suasion (2016) argues that what holds attention just before the ask shapes the answer ([overview of unity and the 2021 edition](https://www.neurosciencemarketing.com/blog/articles/cialdini-7th-unity.htm), grade B).

| Principle | Plain meaning | Ski trip translation |
|---|---|---|
| Reciprocity | Give first and people feel they owe a return. | A useful free asset: a one-page packing list, a "how to read avalanche forecasts" primer, a snow-conditions guide for Voss. Make it useful on its own. |
| Commitment and consistency | Small yes leads to bigger yes. People act in line with what they already said or did. | Save the date, join the trip chat, pick a level, hold a seat with a deposit. Each step is a yes. |
| Social proof | In uncertainty, copy others. | Real guest reviews with specific detail. A guest quote about the first morning beats "amazing experience". |
| Authority | Defer to credible experts. | Guide qualifications, years guiding the same terrain, named safety certification. Only real ones. |
| Liking | Say yes to people we like. | A named guide with a face and a voice. Warm, specific, local humour. |
| Scarcity | Rare means valuable. | A true cap on group size or beds. Never a fake counter. |
| Unity | Say yes to people who feel like "one of us". | Shared identity: people who ski off-piste, people who grew up near Voss, people who would rather be on skis than at a bar. Speak as "we". |

Real-world test of descriptive norms: Goldstein, Cialdini and Griskevicius ran hotel field experiments. A towel-reuse sign citing what most guests do beat a standard environmental appeal, and citing what guests "in this room" did added a further gain (26 percent, then a further 15 percent increase in reuse, per a [secondary summary](https://acawiki.org/A_Room_with_a_Viewpoint:_Using_Social_Norms_to_Motivate_Environmental_Conservation_in_Hotels), grade B; original in [Journal of Consumer Research 35(3)](https://www.jstor.org/stable/10.1086/586910)). Lesson for copy: the closest peer group persuades most. "People who booked this same trip" beats "thousands of happy customers".

Pre-Suasion in ad terms: the first line decides what the reader is thinking about when the offer arrives. If line one is about the quiet of a ridge at 7 a.m., the price in line five is judged against that picture. If line one is about price, the trip is judged as a cost.

**How adwright should use this.** Treat the seven principles as a menu, then pick one lead and one support per ad. Never stack all seven. Prefer social proof and authority (best evidence), plus unity for identity-driven audiences. Scarcity is allowed only when the skill is handed a verified number and a date.

### 2.2 Kahneman and Tversky

**System 1 and System 2.** Kahneman's Thinking, Fast and Slow (2011) frames fast intuitive judgment versus slow effortful thought. Ads on Meta and X are read in System 1 time: a thumb moves in under a second or two. The ad earns a System 2 visit (click, save, share) by being concrete and easy to process. [VERIFY: the "under a second or two" dwell time is a general feed-ad claim; no source opened.]

**Anchoring.** Tversky and Kahneman (1974, Science) spun a wheel that stopped at 10 or 65, then asked what percentage of African countries are in the UN. Median answers were 25 and 45 ([summary](https://yukaichou.com/behavioral-analysis/anchoring-adjustment-heuristic-decision-design/), grade B; paper: [Science 185](https://www.science.org/doi/10.1126/science.185.4157.1124)). For price: the first number the reader sees becomes the reference. People with more product knowledge shift less ([price anchoring review summary](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7434854/), grade B).

**Framing.** Tversky and Kahneman (1981, Science) showed that the same facts framed as gains or losses reverse choices ([Science 211](https://www.science.org/doi/10.1126/science.7455683), grade B for abstract). Copy implication: "Seven nights, guided, all meals" and "Seven nights for NOK 29,000" describe one thing and feel different.

**Prospect theory and loss aversion.** The 1992 cumulative version estimated a loss aversion coefficient near 2.25, meaning a loss is felt about 2.25 times as strongly as an equal gain ([summary of the 1992 estimate](https://repub.eur.nl/pub/10951/LossAversionunderProspect.pdf), grade B). Caveat: Gal and Rucker (2018, Journal of Consumer Psychology) reviewed the evidence and concluded it does not support the claim that losses on balance have more impact than gains ([abstract page](https://myscp.onlinelibrary.wiley.com/doi/abs/10.1002/jcpy.1047), grade B). Simonson and Kivetz replied with a contingent version ([reply](https://myscp.onlinelibrary.wiley.com/doi/abs/10.1002/jcpy.1046)). Safe reading: loss framing can work in specific contexts (the missed powder week, the friend group that goes without you) but "loss aversion is 2x" should never appear in copy logic as a fixed multiplier.

**How adwright should use this.** Lead with a concrete picture (System 1), then give the reader one number to anchor on that is real and sourced. Offer gain and loss versions as test variants, never as a law. Do not quote "2.25" in any output.

### 2.3 Thaler: mental accounting and endowment

- Mental accounting (Thaler 1985, Marketing Science): people keep separate mental budgets and judge each purchase by acquisition utility (value versus price) and transaction utility (the feel of the deal) ([abstract and DOI 10.1287/mksc.4.3.199](https://econpapers.repec.org/RePEc:inm:ormksc:v:4:y:1985:i:3:p:199-214), grade B).
- Implication: a NOK 42,126 trip is judged against a "holiday" or "treat" account, not against groceries. Copy that places the trip in the right account ("your one big trip this winter") lowers the sting. Copy that compares it to gear or rent invites the wrong account.
- Endowment (Kahneman, Knetsch, Thaler 1990): people given a mug valued it about twice as high as people who did not have one; median selling price 5.25 dollars versus a buying price of about 2.25 to 2.75 ([paper PDF](https://web.mit.edu/curhan/www/docs/Articles/15341_Readings/Behavioral_Decision_Theory/Kahneman_et_al_1990_Experimental_tests.pdf), grade B). For travel the useful analogue is psychological ownership before purchase: a held seat, a saved date, a named room, a trip "in your name". Mind the edges: this is for lightweight holds, not pressure.

**How adwright should use this.** Put the trip in the "treat" or "once-a-year" account. Offer low-effort holds (waitlist, saved dates, deposit) so the reader starts to feel ownership. Never create ownership by lying ("we have reserved your spot").

### 2.4 Ariely (with the caveat above)

- Power of free: Shampanier, Mazar and Ariely (2007, Marketing Science) found people treat zero as a special price; in a chocolate test, shoppers picked a lower-quality chocolate merely because it was free (the baseline was 15 cents for a Lindt truffle against 1 cent for a Hershey Kiss, where 73 percent bought the Lindt; the free-condition shares were not in the summary I read [VERIFY]) ([overview](https://thedecisionlab.com/reference-guide/psychology/zero-price-effect), grade B; [paper](https://pubsonline.informs.org/doi/10.1287/mksc.1060.0254)). Independent check: Google's simulation found "power of free" largest or second-largest in 18 of 31 categories, for example a free extra day in car hire pulled 70 percent of shoppers from the favourite ([Google, Decoding Decisions, 2020](https://www.thinkwithgoogle.com/_qs/documents/9998/Decoding_Decisions_The_Messy_Middle_of_Purchase_Behavior.pdf), grade A).
- Social versus market norms: Heyman and Ariely (2004) found that a gift framed as a favour and a payment framed as a price trigger different logics, and even naming a gift's price pushes the exchange into market mode ([Psychological Science 15(11)](https://www.researchgate.net/publication/8234759_Effort_for_Payment_A_Tale_of_Two_Markets), grade B). Use in ski copy: a guide who "built the route for you as a favour to the group" is a relationship story. A guide "billing 8 hours" is a market story. Keep the relationship tone in copy but state the price plainly.
- Decoy: asymmetric dominance. See Section 1: weak in real, qualitative settings. Skip it for trip tiers.

**How adwright should use this.** Free add-ons beat discounts in Google's test, so prefer "free [real item]" over "10 percent off" when a real extra exists (a free guide-led avalanche refresher, a free night, free transfer). The item must be real, specific and of genuine value. Do not use zero-price framing to hide costs elsewhere.

### 2.5 Fogg: B = MAP

"Behavior happens when Motivation, Ability, and a Prompt come together at the same time" ([behaviormodel.org](https://www.behaviormodel.org/), grade A). Fogg's ability factors are time, money, physical effort, brain cycles, social deviance and non-routine [VERIFY: the six factors come from Fogg's writing; the home page I opened did not list them]. Prompt types: spark (raises motivation), facilitator (raises ability), signal (reminder) [VERIFY: same].

Applied to a NOK 17,000 to 42,126 trip, the ability factors read:

| Ability factor | What it looks like for a ski trip | Ad or landing fix |
|---|---|---|
| Money | Total cost, flights on top, gear | Show total, what is included, what is not, a deposit step |
| Time | Days off work, school holidays | Dates visible, short-trip option (day tour NOK 1,948 as a first step) |
| Physical effort | Fitness, long days | Honest day profile, hours on snow, pace set by guide |
| Brain cycles | Comparing resorts, flights, operators | One page, one clear package, one "what you do next" |
| Social deviance | "Is this a silly spend?" "Will my group come?" | Social proof from people like them, shareable summary |
| Non-routine | Booking abroad, new operator, new terrain | Plain booking steps, clear policies, a human to message |

When motivation is already high (the person is in a ski group chat in October), the ad's best job is a facilitator: fewer clicks, clearer answers. When motivation is low (cold audience), the ad is a spark: a scene.

**How adwright should use this.** Before writing, the skill asks "is this audience motivation-limited or ability-limited?" and writes a spark or a facilitator accordingly. It checks that the landing page removes the named barrier. For premium trips the default is ability-limited.

### 2.6 Berger (Contagious, Invisible Influence) and the Heath brothers (Made to Stick)

**Berger's STEPPS** (Contagious, 2013): Social currency, Triggers, Emotion, Public, Practical value, Stories ([framework summary](https://www.shortform.com/blog/stepps-marketing/), grade C/T). Berger and Milkman (2012, Journal of Marketing Research) analysed New York Times articles over three months and found high-arousal emotions (awe, anger, anxiety) drive sharing more than low-arousal ones such as sadness ([search summary of paper](https://philpapers.org/rec/BERWMO-2), grade B). Invisible Influence (2016) covers how others shape choices without our noticing; it supports the social proof and identity sections below.

Implications for ski ads:

- Social currency: the trip makes the sharer look like someone with taste and nerve. Give them a line they can repeat: "7 nights on the line [guide] picked for us".
- Triggers: tie the ad to cues that recur (first snow, a forecast, payday, a Monday at the desk). Triggers keep the idea in mind for weeks.
- Awe sells. A clear, specific image of the place beats a generic "mountain panorama".
- Public: a trip is visible to others (stories, photos). Say what the story will look like.

**Heath brothers: SUCCESs** (Made to Stick, 2007): Simple, Unexpected, Concrete, Credible, Emotional, Stories ([Heath Brothers](https://heathbrothers.com/made-to-stick-introduction/), grade B). Curse of knowledge: Elizabeth Newton's tappers predicted listeners would name the song 50 percent of the time; listeners got 3 of 120 songs (2.5 percent) ([retelling](https://wagonheim.com/the-tappers-and-the-listeners/), grade C; the 1990 dissertation was not opened). Warning for Outdoor Norway: guides know the terrain so well that they write copy only insiders can parse ("do the Hardangervidda loop"). The reader cannot hear the tune.

**How adwright should use this.** Before writing, run SUCCESs as a checklist and score each ad on concreteness (is there a named place, time, sensation?) and credibility (is there proof?). Add a "tapper check": can a stranger who has never skied off-piste decode every noun in the ad?

### 2.7 Iyengar (choice overload) and Loewenstein (curiosity)

- The jam study (Iyengar and Lepper 2000): 6 jams converted 30 percent of tasters, 24 jams converted 3 percent, though the big table drew more stoppers (60 versus 40 percent) ([retelling](https://yukaichou.com/behavioral-analysis/paradox-of-choice-schwartz-choice-overload/), grade C).
- The meta-analysis (Scheibehenne, Greifeneder and Todd 2010, Journal of Consumer Research): 63 conditions from 50 experiments, N = 5,036, mean effect "virtually zero" with high variance; no sufficient conditions identified ([paper, PDF](https://scheibehenne.com/ScheibehenneGreifenederTodd2010.pdf), grade A for the abstract). A later review by Chernev, Bockenholt and Goodman (2015) names set complexity, decision difficulty, preference uncertainty and decision goal as moderators ([review PDF](https://chernev.com/wp-content/uploads/2017/02/ChoiceOverload_JCP_2015.pdf), grade B).
- A first-time buyer of a NOK 20,000 trip fits the conditions where overload bites: high stakes, unsure preferences. So the ad should present one recommended trip, not twelve.
- Loewenstein (1994, Psychological Bulletin): curiosity arises when attention is drawn to a gap between what one knows and what one wants to know; it needs some prior knowledge of the topic ([secondary summary](https://www.ignorancegraph.com/information-gaps/information-gap-theory/), grade B; I could not read the scan). Copy uses: a specific open question ("The one pass we only open when the wind drops") makes the reader click to close the gap. Rule: the gap must be honest. If the click does not pay it off, the ad is clickbait and Meta can treat it that way.

**How adwright should use this.** One ad, one trip, one next step. Use curiosity as a hook only when the landing page pays it off within the first screen. Offer the guest a choice only after the first yes (level, dates), where choice supports autonomy.

### 2.8 Jobs To Be Done and the Forces of Progress (Moesta)

Four forces: push (frustration with the present), pull (attraction to the new), anxiety (fear about the new), habit (comfort of the old). Change happens when push plus pull beat anxiety plus habit ([Moesta, Unpacking the progress making forces diagram](https://jobstobedone.org/radio/unpacking-the-progress-making-forces-diagram/), grade B). Moesta's Switch interview rebuilds the timeline of the decision.

Applied to a ski trip:

| Force | Example | Where it shows up in copy |
|---|---|---|
| Push | Same resort every year; grey winter at the desk; friends drifting apart; "I keep saying I will go" | Hook and trigger moment |
| Pull | The line you have seen in a film; a week with friends; a new level | Core promise and imagery |
| Anxiety | Am I good enough, will it be safe, is the money wasted, will the snow be there | Mid-ad proof, FAQ, risk reversal |
| Habit | The usual Alps package; the usual week in the same cabin; "we always go to Åre" | Contrast line that respects the habit |

The "job" is rarely "ski". It is closer to "be somebody who does this with people I like", "get back the feeling of being good at something", or "have a story". Each is a hire-able job.

**How adwright should use this.** The skill asks for the four forces first, using real guest interviews if available. A good ad addresses at least one push or pull and one anxiety or habit force. When the client has no interviews, the skill flags the guess and suggests five switch-interview questions to ask recent guests.

### 2.9 Experiential versus material purchases, anticipation, Happy Money

- Van Boven and Gilovich (2003, JPSP 85(6), 1193 to 1202): people judged experiential purchases to make them happier than material ones; experiences are more open to positive reinterpretation, more part of one's identity, and more connected to relationships ([overview of the paper](https://www.semanticscholar.org/paper/To-do-or-to-have-That-is-the-question.-Boven-Gilovich/85844562e67d74f1b134ce9ad86f7650d55e5436), grade B). A figure of 83 percent "mentally revisiting" experiential purchases more circulates in a search summary [VERIFY: exact figure not seen in paper].
- Kumar, Killingsworth and Gilovich (2014, Psychological Science, "Waiting for merlot"): people were happier when thinking about an upcoming experiential purchase, with no such lift for material purchases; Study 1 used 97 students and examples such as ski passes and concerts; Study 2 used experience sampling of 2,266 adults; effect held independent of cost ([ScienceDaily summary](https://sciencedaily.com/releases/2014/08/140825100051.htm), grade B). This is the most useful result for the copy: anticipation is a product feature.
- Kumar and Gilovich (2015), "Some thing to talk about?", reports that experiences give more story value in conversation than possessions ([Sage page](https://journals.sagepub.com/doi/abs/10.1177/0146167215594591), title and abstract not opened) [VERIFY: abstract].
- Nawijn et al (2010, Applied Research in Quality of Life 5(1), 35 to 47): vacationers were happier before the trip, and most were not happier after; very relaxing trips were the exception ([Tilburg record](https://research.tilburguniversity.edu/en/publications/vacationers-happier-but-most-not-happier-after-a-holiday/), grade A for citation; sample sizes of 974 vacationers and 556 non-vacationers and the eight-week fade come from a [secondary summary](https://spacedaily.com/m-a-survey-of-over-one-thousand-adults-found-that-vacations-do-make-us-happier-but-perhaps-surprisingly-the-boost-came-mostly-before-the-trip-from-anticipation-and-largely-faded-onc/), grade C) [VERIFY: sample sizes]. For a ski ad the honest reading is "the weeks before count too". It is also a warning against promising lasting life change from a week on snow.
- Dunn and Norton, Happy Money (2013): five principles: buy experiences, make it a treat, buy time, pay now and consume later, invest in others ([summary](https://www.forbes.com/sites/davidrae/2019/01/30/happy-money/), grade C). Dunn, Aknin and Norton (2008, Science) found spending on others raised happiness more than spending on oneself ([Science](https://www.science.org/doi/10.1126/science.1150952), grade B for abstract; a [replication of its one experiment](https://pmc.ncbi.nlm.nih.gov/articles/PMC9451075/) exists, I did not read the result). A trip with friends or a partner is spending that is partly on others.

**How adwright should use this.** The ad can sell three phases: before (the countdown that starts at booking), during, and after (the story). Keep "before" in copy: "The countdown starts when you book" is honest and has research support. Do not promise lasting happiness. Put "with people you like" in the lead whenever the trip is a group trip.

### 2.10 Regret, identity, self-determination, costly signalling

**Regret.** Gilovich and Medvec (1995): in the short run actions are regretted more; in the long run inactions are ([summary](https://www.semanticscholar.org/paper/The-experience-of-regret:-what,-when,-and-why.-Gilovich-Medvec/7792f8a0a372c01f572b326315ee9739df7e40b2), grade B). A replication was published in Collabra 2022 [VERIFY: I could not open the result]. Bezos's "regret minimization framework" is the popular form of this idea. Use in copy: the "someday" frame. "In ten years you will not remember the lift pass price. You will remember who was with you." Fine as emotion, but never as shame ("you will regret missing this") and never tied to false time pressure.

**Identity.** People buy what fits who they are or want to become. The Google messy middle report notes people use shortcuts to simplify; identity is a major shortcut. Reed et al (2012) cover identity-based consumer behaviour [VERIFY: not opened]. For ski travel the identity may be "skier who goes beyond the resort boundary", "parent who still does big things", "friend group that actually follows through". Copy should name an identity by behaviour, never by personal attribute (see Section 7).

**Self-determination theory** (Ryan and Deci 2000, American Psychologist 55(1), 68 to 78): three needs, autonomy, competence, relatedness ([Ryan and Deci PDF](https://selfdeterminationtheory.org/SDT/documents/2000_RyanDeci_SDT.pdf), grade B). Translated:

- Autonomy: "you choose the line, the guide sets the safety limit". Avoid commands ("Book now or miss out").
- Competence: progression, skills learned, a real sense of getting better. "By day three you will read the snow, not just ski it."
- Relatedness: shared effort with people who matter. Group photos, shared meals, guide who knows names.

**Costly signalling and status.** Berger and Ward (2010, Journal of Consumer Research) showed that insiders prefer subtle signals that outsiders miss, and brand logos follow an inverted-U with price ([abstract](https://academic.oup.com/jcr/article-abstract/37/4/555/1795043), grade B). For ski ads: experienced skiers read specifics (named terrain, snow type, gear detail) as proof the operator knows the craft. Loud adjectives ("epic", "ultimate") read as outsider talk. A high price is itself a signal of quality and of commitment; hiding it undermines that signal.

**How adwright should use this.** Use regret and identity as emotion, not pressure. Write for autonomy: offer a choice and a recommendation, never an order. Use insider specifics as credibility. Ban words that outsiders use to sell mountains ("epic", "breathtaking", "bucket list") unless the client voice file allows them.

---

## 3. Messy middle and the travel path to purchase

### 3.1 What Google found (primary source opened)

Google and The Behavioural Architects (July 2020, UK) observed 310 shopping journeys across 31 categories, filmed with think-aloud narration, then ran a simulation with 31,000 online shoppers aged 18 to 65 (1,000 per category) and 310,000 simulated purchases ([Decoding Decisions PDF](https://www.thinkwithgoogle.com/_qs/documents/9998/Decoding_Decisions_The_Messy_Middle_of_Purchase_Behavior.pdf), grade A).

Core model: a trigger starts the journey; the buyer loops between exploration (widening the options) and evaluation (narrowing them) until a purchase, then the experience feeds the next trigger. "There are no typical journeys. Instead there is a confusing web of touchpoints." Touchpoints observed include search engines, review sites, video sites, social media, comparison sites, forums, interest groups, retailer sites and more.

Six biases tested: category heuristics, social proof, authority, power of now, scarcity, power of free. Key results:

| Finding | Number | Source |
|---|---|---|
| Social proof (3 star versus 5 star reviews at equal review count) had the largest or second-largest effect | 28 of 31 categories | Google report, grade A |
| Power of free largest or second-largest | 18 of 31 categories | Google report, grade A |
| Authority (awards, expert reviews) | Smaller than social proof; strongest where buyers lack domain knowledge; impartial publications outweighed industry ones | Google report, grade A |
| Scarcity | "Most often the least effective bias"; can clinch at final evaluation; for explorers can "feel restrictive and provoke a negative reaction" | Google report, grade A |
| Package holiday category baseline | 34 percent switched to their second favourite brand with no bias applied | Google report, grade A |
| Package holiday with all six biases supercharged on the second favourite | 88 percent drawn away from the favourite | Google report, grade A |
| Search trend | "best" gained ground against "cheap" in many categories, including travel destinations, with "cheap" travel still more common in the UK data | Google report, grade A |

Limits: UK shoppers, 2020, simulated purchases with fictional brands, not ski trips, not NOK 17,000-plus purchases. The package holiday result (a large shift is possible) supports a message: loyalty is soft in travel, so a better-evidenced offer can win.

### 3.2 Travel path numbers

| Fact | Number | Source and grade |
|---|---|---|
| Time travellers spend with travel content before booking, 45-day window | 303 minutes (more than 5 hours) | Expedia Group Path2Purchase 2023, via [Hotel News Resource](https://www.hotelnewsresource.com/article127422.html), grade B |
| Average pages viewed in 45 days | 141 (up to 277 for US travellers) | Same, grade B |
| Page views per day early, and on the day of purchase | 2.5 early, 25 on purchase day | Same, grade B |
| Total path to purchase | 71 days: 33 inspiration, 38 research and planning | Expedia 2023 via [Travel Market Report/GTP summary](https://news.gtp.gr/2023/08/02/travelers-spend-over-5-hours-researching-trips-says-expedia/), grade C |
| Travellers undecided on destination at the start | 59 percent (UK: 62 percent) | Hotel News Resource, grade B |
| Use social media for inspiration | 77 percent | Same, grade B |
| Influenced by advertising | 19 percent (40 percent in Mexico) | Same, grade B |
| Sample | 5,713 survey respondents (24 March to 19 April 2023), 70,000+ digital panel, seven countries | Same, grade B |
| Travellers who changed destination, flight or accommodation before booking | 1 in 2 across APAC; nearly 4 in 5 in India and Thailand | Think with Google APAC (19,000 consumers, 7 markets, May to June 2023): [page](https://business.google.com/en-all/think/consumer-insights/insights-apac-traveler-behaviors/), grade A for that page |
| More than half cross-checked travel information elsewhere; more than 3 in 5 need strong confidence before booking | As stated | Same, grade A |
| YouTube as source of inspiration | #1 source among APAC travellers | Same, grade A; APAC only |
| Use social media to research and discover destinations (US, 1,000 adults, March 2025) | 41 percent; 66 percent of Gen Z; 55 percent discover via word of mouth; 39 percent via influencer content; 9 percent use AI tools for planning | Data Axle/Dynata via [Marketing Dive](https://www.marketingdive.com/news/social-traveler-numbers-say-influencers-white-lotus/745031/), grade B |

Reading these together: the journey is long (weeks to months), spread across many touchpoints, and the destination is often undecided at the start. Only a minority say advertising influences them, but that is self-report. Word of mouth and reviews rank high. The ad's role is rarely "close the sale". It is inspiration, shortlist entry, reassurance and a nudge.

### 3.3 What ski and adventure buyers research (closest data found)

Iglu's 2026 survey of UK skiers (sample size not stated in the trade article, [Snowsports News, June 2026](https://www.snowsportsnews.com/newsrepository/2026/june/in-iglu-s-biggest-ever-survey-ai-use-for-ski-trip-research-nearly-quadruples-in-a-year-but-snow-certainty-and-trusted-advice-still-decide-where-britain-skis/), grade C, [VERIFY: sample size and method]):

| Item | Number |
|---|---|
| Resort choice factors | Snow reliability 78 percent; value for money 56 percent; number of runs 46 percent |
| Trusted sources | "Been before" 55 percent; online articles 53 percent; word of mouth 51 percent; reviews 42 percent; AI tools 8.7 percent (up from 2.2 percent) |
| Social media as trip inspiration | 23 percent (up from 15 percent) |
| Compare multiple websites | 90 percent |
| Book a package | 60 percent; prefer online booking 58 percent; would speak to an expert 24 percent (up from 20 percent) |
| Travelling with | family 37 percent, couple 31 percent, friends 28 percent |
| Market profile | intermediates 46 percent of the market |
| Booked for snow certainty at high altitude | 61 percent |

These are UK mass-market ski package buyers, not Norwegian guided off-piste clients. They still hint at the questions Outdoor Norway must answer in the ad or on the landing page: snow reliability (Norway at low altitude invites doubt, so say what the plan is when conditions are poor), value, and a trusted voice. A peer-reviewed means-end study of ski destination choice exists ([PMC9780482](https://pmc.ncbi.nlm.nih.gov/articles/PMC9780482/)) but I could not open it before finishing [VERIFY].

### 3.4 What social advertising does in this path

- It feeds the inspiration phase (77 percent use social for inspiration per Expedia via secondary source; 23 percent of UK skiers in Iglu's survey).
- It re-enters during exploration and evaluation as retargeting and proof (reviews, UGC, guide content).
- It rarely closes the sale alone. Expect view-through and assisted conversions. [VERIFY: attribute the client's own numbers once they exist.]
- X is a conversation platform. The role there is voice, authority and replies, not scenic reels.

**How adwright should use this.** Treat each ad as one touch in a multi-touch path, and say so in the brief. The skill asks "which stage is this audience in?" and writes accordingly (Section 8). It builds a three-ad family per trip (spark, proof, facilitator) rather than one ad that tries to do everything. It never promises last-click ROAS from cold social. Because intermediates are almost half the UK market and snow reliability is the top factor, the skill's default FAQ list for ski copy starts with level and snow.

---

## 4. Group decision-making in leisure travel

### 4.1 What the research says

- Skiing is a group activity. In the Iglu survey 37 percent travel with family, 31 percent as a couple, 28 percent with friends (grade C).
- Holiday purchase is largely joint. Tourism research on couples finds a trend toward joint decisions, with women often dominant in the early stages (gatekeeping), shifting by stage ([Couple dynamic in household tourism decision making: women as gatekeepers?](https://www.researchgate.net/publication/254583454_Couple_Dynamic_in_Household_Tourism_Decision_Making_Women_as_the_Gatekeepers), grade C, abstract level) and longer and more complex than single-person decisions ([Smith et al 2017](https://doi.org/10.1177/1938965517704374), not opened) [VERIFY both].
- Practitioner advice on ski groups says each group needs one organiser who keeps the plan moving and records decisions (trade blogs such as [Snowcompare](https://www.snowcompare.com/blog/2024/09/ski-trip), grade C). This matches the B2B "mobiliser" pattern: one person carries the proposal to the others.
- Private sharing matters. A GWI and We Are Social study reported 63 percent of UK and US internet users share content through private messaging apps, ahead of open social media at 54 percent ([The Drum summary](https://www.thedrum.com/news/63-people-prefer-share-content-dark-social-channels), grade C, dated, [VERIFY: year]). Berger reports most word of mouth happens offline; his often-cited 7 percent online figure comes through a book summary ([source](https://www.shortform.com/blog/stepps-marketing/), grade C) [VERIFY].

### 4.2 The second reader problem

The person who clicks the ad is the champion. The people who must say yes are the second readers: the partner, the friend who is the weakest skier, the friend who controls the budget, the parent who watches the kids. The second reader sees the ad cold, in a chat thread, with the champion's one-line comment above it.

What the second reader asks, in order:

1. What is this? (one sentence)
2. When and how long? (dates)
3. How much, for what? (total price, what is included)
4. Can I do it? (level, fitness, age of group)
5. Is it safe and reputable?
6. What if I cannot go? (cancellation)
7. Who else is going?

What the champion needs from the ad:

- A link preview that works without context (title, image, price visible).
- A short block of text they can paste: trip name, dates, price, one line on level and one on safety.
- A reason that sounds like an idea the second reader would have, not a sales pitch.
- A way to take the next step without the whole group (a hold, a waitlist, a shared calendar invite).

### 4.3 How ads can arm the champion

| Tactic | How | Check |
|---|---|---|
| Forward test | Paste the ad text and the link preview into a blank chat. Does it answer questions 1 to 3 without the picture? | Pass or rewrite |
| Champion line | End with a copy-ready sentence: "[Trip], [dates], [total price], guided, [one-line level]. Hold a place with a deposit." | Facts match the landing page |
| Cost per person | Show the per-person total and note room sharing assumption. | Matches booking terms; do not understate |
| Group-ready proof | Review quotes from groups ("six of us, mixed levels") rather than only soloists. | Real, with consent |
| Open the second reader's anxiety | Add a small FAQ line aimed at the sceptic: "Mixed levels? The guide splits the day." | Only if the operator really does |
| Click-to-chat | Offer a WhatsApp or Messenger reply path for "I have a question for the group". Meta supports click-to-WhatsApp ad formats [VERIFY: current availability and Norwegian rules]. | Reply time promise is realistic |
| Date poll | A landing-page tool that lets a group vote on two or three departure dates (client product decision). | Needs dev work |

**How adwright should use this.** Add a "second reader pass" to the review step. The skill rewrites the ad as if pasted into WhatsApp and checks whether questions 1 to 3 survive. It adds an optional "champion line" block to every ad set, separate from the ad copy. It never invents group-size or date facts. Those come from the client's brief with a source.

---

## 5. Price psychology for premium trips

Outdoor Norway price points (from the brief): day tour NOK 1,948; trips up to 9 days at NOK 42,126. The 9-day trip costs about 21.6 times the day tour (42,126 / 1,948 = 21.62). Per day, the 9-day trip is NOK 42,126 / 9 = NOK 4,680.67, about NOK 4,681. For a worked illustration: a NOK 17,000 trip of 5 days would be NOK 3,400 per day. [VERIFY with client: actual lengths and included items for each price.]

### 5.1 Per-day framing

- Gourville (1998, Journal of Consumer Research 24(4), 395 to 408) showed "pennies-a-day" framing raises compliance because it moves the comparison to small recurring expenses instead of large one-off ones ([abstract page](https://academic.oup.com/jcr/article-abstract/24/4/395/1797969), grade B).
- Limits: the effect depends on a plausible small-expense comparison, and research on larger sums and aggregation exists (Bambauer-Sachse and Grewal) but I only saw a title [VERIFY direction]. Per-day framing also invites a hotel-per-night comparison that may flatter or hurt.
- Safe use: "Nine days, guided: NOK 42,126 in total. That is about NOK 4,681 a day, including [what is included]." Total first. Per-day second. Both in the same line or view.
- Never show per-day alone as the price. Package travel is marketed at a total price and Norwegian price information rules expect the total ([pakkereiseloven summary](https://lovdata.no/artikkel/pakkereiser/5166), grade B) [VERIFY with counsel].

### 5.2 Anchoring against flights, resort passes and competitors

- A buyer already holds reference prices: a week in the Alps, a lift pass, a flight. Anchoring suggests the first reference in the copy colours the rest.
- Use real anchors only. Example: "A six-day lift pass at [named resort] costs NOK [x] (checked [date], [link])." Put the date in the copy or on the page. Keep like-for-like: guided days versus unguided days are different products.
- Comparative claims carry legal rules (Marketing Control Act on comparative advertising, see section 7) [VERIFY with counsel].
- Anchoring effects are smaller with expert buyers (price anchoring review above). Intermediate to expert skiers will check your number.

### 5.3 The "what is included" stack

- Mental accounting favours a single bundled figure for a treat. Buyers dislike discovering add-ons.
- A stack ("guide, lodging, [meals], [transfers], safety gear loan, photos") makes value concrete (Heath: concrete).
- The stack also protects against drip pricing, which the evidence shows works commercially but is a regulatory target: on StubHub, hiding mandatory fees until checkout raised revenue by about 21 percent and made buyers 14.1 percent more likely to complete (Blake, Moshary, Sweeney, Tadelis, Marketing Science 40(4), 2021; [NBER working paper](https://www.nber.org/system/files/working_papers/w25186/w25186.pdf), grade B for the figures from a [secondary summary](https://dl.acm.org/doi/abs/10.1287/mksc.2020.1261)). The temptation is real. The ethical and legal answer is to show what is and is not included up front.

### 5.4 Deposit and payment framing

- Prelec and Loewenstein (1998) model a "pain of paying" and predict people prefer to prepay for consumption so that it can be enjoyed as if free ([Marketing Science 17(1)](https://pubsonline.informs.org/doi/10.1287/mksc.17.1.4), grade B). Dunn and Norton's "pay now, consume later" reflects the same idea.
- Fogg's money factor pushes the other way for first contact: a small deposit lowers the entry barrier.
- Both can be true. Deposit framing in copy: "Hold your place with NOK [x] today. The balance is due [date]." Say what the deposit is, when the rest is due, and what happens if plans change.
- Norwegian package travel rules govern price increases (notice at least 20 days before departure for an increase to be valid per the [NHO Reiseliv/travel summaries](https://www.travelnetkrs.no/pakkereiseloven), grade C) [VERIFY with counsel].
- Instalment or buy-now-pay-later options change both psychology and regulation. [VERIFY with counsel before any copy mentions them.]

### 5.5 Cancellation policy as risk reversal

- The anxiety force in Moesta's model is largely risk. A clear, fair cancellation policy cuts perceived risk (Fogg: lowers brain cycles and social risk).
- Evidence is mostly vendor or trade data: a survey cited by trade press says 70 percent of travellers would book flights earlier if they could adjust for free; an Expedia partner case study reported a flexible policy lifted bookings by 26 percent and revenue by 53 percent per listing ([Expedia partner case study](https://partner.expediagroup.com/en-us/resources/case-studies/evolve-drives-success-with-flexible-cancellation-policies), grade C). These are single-vendor numbers for rentals and flights, not guided trips. Use as a hypothesis to test.
- Copy rule: only advertise the exact policy the operator will honour, in plain words. "Free cancellation until [date]. After that [rule]." If there is no free cancellation, do not hint at one. Mention weather and safety cancellations by the operator (what is refunded) if relevant.

### 5.6 "From" pricing

- A "from NOK 1,948" line invites clicks and sets a low anchor. Lab research shows low advertised anchors raise attitude and purchase intention in general ([summary](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7434854/), grade B).
- Risk: if the "from" product is not what the ad shows (a day tour next to a 9 day powder trip image), buyers feel baited and the Marketing Control Act misleading-omission rules bite. Norwegian guidance on "from" prices I found is for real estate packages, not travel ([Forbrukertilsynet guidance example](https://www.forbrukertilsynet.no/vi-jobber-med/bolig/veileder-for-markedsforing-av-bolig/prisopplysninger), grade C) [VERIFY with counsel for travel].
- Practical rule: the product pictured or described is the product at the price shown. If the price is "from", say what it is the price for ("Day tour from NOK 1,948") and link to the range.

### 5.7 Price transparency as trust

- In the messy middle report, "best" gaining on "cheap" suggests that for considered purchases buyers want quality assurance more than the lowest price. [Reading of Google data, see section 3.]
- Showing the total, the inclusions and the policy up front earns the expert-buyer trust that anchoring cannot. It also avoids misleading-omission exposure.
- Forbrukertilsynet's 2023 sweep summary (148 of 399 online shops tested used manipulative design; 12 were Norwegian) shows regulators are looking at design and display of price information ([Netthandel.no, 28 Feb 2023](https://netthandel.no/forbrukertilsynet-forklarer-dette-ma-nettbutikkene-unnga-a-gjore/), grade B).

**How adwright should use this.** Put the total price in the ad whenever the placement allows. Offer per-day and per-person versions as a second line. Require a source and date for any outside anchor. Accept only real inclusions and cancellation terms from the brief. Provide three price-line templates: total plus per-day, total plus per-person, and deposit plus balance. Never write "from" without naming what the price buys.

---

## 6. Anxieties in adventure and ski travel

The anxiety force in Moesta's model is what ads most often skip. Evidence base here is thin: academic work exists on fear and self-efficacy in ski learning (one peer-reviewed study found lower fear and higher self-efficacy and mastery associated with better beginner performance, [PMC6162698](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6162698/), grade B), but most of what we know about travel anxieties comes from ski school and forum writing (grade C). Treat the table as hypotheses to test with the client's own enquiry and review data.

| Anxiety | What the buyer is really asking | How copy can answer (about the trip, not the viewer) | Policy risk to avoid |
|---|---|---|---|
| Am I fit enough? | "Will I be the problem?" | State the day profile: hours on skis, ascent, pace set by the guide, rest stops, route options. | Do not address the viewer's body or health ("Out of shape?", "Not as fit as you were?"). Meta lists health and disability as personal attributes. |
| Am I good enough? | "Will I embarrass myself?" | Level bands by name, with a description of what each can do. "Intermediate: comfortable on red runs in variable snow." | "Are you a beginner?" is borderline; "Trips for confident intermediates" describes the offering. |
| Will I be the slowest? | Fear of holding the group back (a common theme in ski-school and forum writing, grade C) | "The guide sets the pace and keeps the group together. Groups are split by level where needed." Only if true. | Avoid naming and shaming a slow skier in imagery. |
| Will there be snow? | Top factor in the Iglu survey (78 percent, grade C) | Say what Norway offers: the plan if conditions are poor, the dates window, what refunds apply. Honest about low-altitude risk. | Never promise snow. A claim like "guaranteed powder" is a misleading-act risk. |
| Is it safe? | Avalanche, injury, weather | Guide certifications, group size, safety kit, decision rules ("we turn around when [rule]"). Authority proof helps most where the buyer lacks knowledge (Google). | Do not use fear imagery of accidents. |
| Is it worth the money? | NOK 17,000 to 42,126 is a lot | Show the total and the stack. Show the cost per day alongside what a comparable unguided week would cost, with sources. Use guest quotes about value. | Avoid vague "best value". Avoid unverifiable savings claims. |
| Solo travel | "Will I be alone for a week?" | "Join a small group: [group size]. Most guests arrive on their own" only with a real number from bookings. | Do not write "Single?" or "Alone?"; relationship status and similar are sensitive attributes to avoid [VERIFY against current Meta policy list]. |
| Cold | "Will I be miserable?" | Practical: gear list, warm lunch stops, typical temperatures for the dates with a source. | Do not claim "never cold". |
| Gear | "Do I need to buy everything?" | What is loaned, what must be brought, rental cost. | Hidden extra costs: list them. |
| Logistics | "How do I get there?" | Where the trip starts, travel time from Oslo or Bergen, what is arranged by the operator. | Must match actual terms. |
| What if I cannot go? | Cancellation and insurance | Plain cancellation terms. | Never imply cover you do not provide. |
| Group fit | "Will I like the other guests?" | Group size, typical guest mix described by behaviour ("people who like early starts and long lunches"). | Avoid age or other attribute descriptions of guests. |

### Meta policy detail for these anxieties

Meta's Ad Standards say ads must not "assert or imply personal attributes" and list among them race, ethnicity, religion, age, sexual orientation or practices, gender identity, disability, physical or mental health, medical conditions, vulnerable financial status, voting status, trade union membership and criminal record. "You/your" language is allowed as long as it is not used to reference a personal attribute. Example pairs from the policy: "Depression counseling" is allowed and "Depression getting you down?" is not ([Meta, Privacy violations and personal attributes](https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/), grade A via summarising fetch; confirm in the live policy).

Practical pattern for adwright:

| Risky | Safer rewrite |
|---|---|
| "Worried you are too unfit for this?" | "Day profile: five hours on skis, long stops. The guide sets the pace." |
| "Are you too old to start powder skiing?" | "Powder skiing for confident intermediates, any age on the trip." (only if true; age mentions deserve a second look) |
| "Single and tired of holidays alone?" | "Small group trips. Join as a pair, a group or solo." |
| "Afraid of avalanches?" | "How we decide where to ski: [three rules]." |
| "Struggling on steeper runs?" | "Level 3 trip: red runs and gentle off-piste with coaching." |

**How adwright should use this.** Keep an anxiety library of eleven or twelve items. For each ad, the skill picks one anxiety, answers it with a fact about the trip, and runs a "second person plus attribute" scan (see Section 9 checklist). It writes the anxiety line as a statement about the offering ("Groups are split by level") or as a question about the trip ("How does the guide handle mixed levels?"). It does not write a question that starts with "Are you" followed by a body, health, age or status word.

---

## 7. Ethical persuasion, and the Norway and EU consumer-law angle

### 7.1 Principles for adwright

1. True scarcity only. The number comes from the booking system on the day of publishing, or it is a fixed fact ("max 8 guests").
2. No fake urgency. No restarting timers. No invented deadlines. No "only 2 left" that has not been checked.
3. No dark patterns: hidden fees, pre-ticked extras, confirm-shaming, obstructed cancellation, false hierarchy in buttons.
4. No manipulation of vulnerable states (grief, loneliness, anxiety about health).
5. No claims about guests that you cannot document (reviews, numbers, outcomes).
6. Evidence for factual claims must exist at the time of the ad (Marketing Control Act section 3 on documentation, [Lovdata](https://lovdata.no/dokument/NLE/lov/2009-01-09-2), grade B via summarising fetch).
7. If a persuasion lever would embarrass the client if the guest saw the mechanism, drop it.

Google's own result gives a practical reason as well: scarcity was the least effective bias in most categories and, for exploring shoppers, "could feel restrictive and provoke a negative reaction" ([Google, Decoding Decisions, 2020](https://www.thinkwithgoogle.com/_qs/documents/9998/Decoding_Decisions_The_Messy_Middle_of_Purchase_Behavior.pdf), grade A).

### 7.2 Norway (Marketing Control Act, markedsføringsloven)

High-level, not legal advice. All tagged [VERIFY with counsel].

| Topic | What I could confirm | Source and grade |
|---|---|---|
| Unfair commercial practices | Section 6 prohibits unfair commercial practices (contrary to good business practice and likely to materially distort consumer behaviour). | [Lovdata](https://lovdata.no/dokument/NLE/lov/2009-01-09-2), B |
| Misleading acts | Section 7 covers false information or deception about product characteristics, price or price advantage, and more. | Same, B |
| Misleading omissions | Section 8 covers omission of material information. For an invitation to purchase, material information includes main characteristics, trader identity, payment and delivery arrangements, and withdrawal rights. | Same, B |
| Aggressive practices | Section 9: harassment, coercion or undue influence that impairs freedom of choice. | Same, B |
| Documentation | Section 3 requires documentation of factual claims and clarity that marketing is marketing. | Same, B; Forbrukertilsynet also cites section 3 for documentation ([guidance PDF](https://www.forbrukertilsynet.no/wp-content/uploads/2025/06/veiledning-om-reglene-som-gjelder-ved-markedsforing-av-salg-og-betingede-tilbud-l2398774.pdf), A) |
| Price marketing | Forbrukertilsynet names sections 6 to 8 and 10 as central for sale and price marketing. | Guidance PDF above, A |
| Price reduction (reference price) | Price Information Regulation section 9a: when goods are marketed as reduced, state the prior price, defined as the lowest price used in the 30 days before the sale began; the discount must be computed from that price. The wording refers to goods (varer). | Guidance PDF above, A |
| Unfair practices blacklist | Falsely claiming a product is available only for a very limited time, or only on particular terms for a very limited time, to force an immediate decision is blacklisted (point 7 in the EU list; in the Norwegian regulation on unfair commercial practices). | [EU UCPD Annex I summary via search](https://eur-lex.europa.eu/NL/legal-content/summary/unfair-commercial-practices.html), B; Norwegian rule via [Dagbladet/Dinside page listing the blacklist](https://dinside.dagbladet.no/jobb/her-er-hele-svartelista/62321035), C |
| Countdown timers | Forbrukertilsynet's subdirector said an automatically restarting countdown timer "will easily be a breach of the marketing law" and may breach the blacklist regulation (Feb 2023). | [Netthandel.no](https://netthandel.no/forbrukertilsynet-forklarer-dette-ma-nettbutikkene-unnga-a-gjore/), B |
| Package travel | Package travel law (pakkereiseloven) applies to trips marketed at a total price that last more than 24 hours or include accommodation and combine two or more elements (transport, accommodation, other tourist services). Guided multi-day ski trips with lodging may qualify. | [Package travel summary, travelnetkrs.no](https://www.travelnetkrs.no/pakkereiseloven), C; [Lovdata law page](https://lovdata.no/lov/2018-06-15-32) not opened |

Important nuances:

- The 30-day reference price rule is written for goods. Day tours and trips are services. The misleading-price-advantage rule (section 7) still applies to services. Do not run "was NOK X, now NOK Y" copy unless the "was" price was a real, recent price. [VERIFY with counsel whether the 9a approach is applied to services by analogy.]
- Forbrukertilsynet's 2025 guidance notes that the discount must be calculated from the prior price (referring to the EU Court of Justice case C-330/23) (guidance PDF above, A).
- Reviews and endorsements: marketing must be identifiable, and fake reviews are an enforcement target in the EU after the Omnibus Directive amended the UCPD blacklist [VERIFY: points 23b and 23c].

### 7.3 EU (Omnibus Directive and UCPD)

- Directive (EU) 2019/2161 ("Omnibus") modernised consumer rules, adding Article 6a to the Price Indication Directive for price reduction announcements and stronger penalties under the UCPD ([EUR-Lex](https://eur-lex.europa.eu/eli/dir/2019/2161/oj/eng), grade A as source, details not read in full).
- Article 6a requires that a price reduction announcement indicates the prior price, the lowest price applied in the preceding period of not less than 30 days. The Commission's guidance states the Price Indication Directive applies to goods, not services ([search summary of the guidance](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52021XC1229(06)), grade B). Norway implements via the EEA Agreement (Prop. 50 LS 2022 to 2023) ([government page](https://www.regjeringen.no/no/dokumenter/prop.-50-ls-20222023/id2966742/?ch=6), not opened).
- UCPD Annex I point 7 (false limited-time claims) is on the list of practices unfair in all circumstances ([EU summary](https://eur-lex.europa.eu/NL/legal-content/summary/unfair-commercial-practices.html), grade B).
- Enforcement example: in 2019 the UK CMA obtained legally binding commitments from Expedia, Booking.com, ebookers, Hotels.com, Agoda and trivago on pressure-selling claims, covering discount claims, the number of other guests looking and the number of rooms left ([CMS summary](https://cms.law/en/gbr/legal-updates/CMA-secures-commitments-from-holiday-booking-sites-on-sales-practices), grade B). The UK is outside the EU and Norway, but it is a clear case that "only 1 room left" claims draw action.

### 7.4 What is safe, in practice

| Allowed with proof | Not allowed |
|---|---|
| "Max 8 guests on every departure." | "Only 2 spots left!" when the system shows 5 |
| "Booking for [date] closes on [date], when flights are held." (a real operational deadline) | A timer that resets on reload |
| "Early-booking price until [date], then NOK [x]." (a real, honoured change) | A "special price" that was never lower than the new price |
| "Rated 4.9 by 112 guests on [platform, date]." (checkable) | Invented or hand-picked-only review numbers |
| "Free cancellation until [date]." (if true) | "Risk-free" with unstated conditions |

**How adwright should use this.** Build a scarcity gate: the skill will not write a number-based scarcity line unless the brief supplies the number, the source and the date. It will not output a countdown. It flags price-reduction copy ("was/now", "% off") and asks for the prior price and its dates. It adds a final "compliance prompt" line to every output: "check with counsel: price claims, urgency, reviews, package travel info." It never states it is legal advice.

---

## 8. Buyer journey for a ski trip

Synthesised from the Google messy middle (trigger, exploration, evaluation, purchase, experience), Moesta's forces, Expedia and Iglu path data, and Fogg. Stage lengths are indicative: Expedia's 71-day travel path (33 inspiration, 38 research) is for general travel, and a NOK 17,000-plus trip may take longer [VERIFY with Outdoor Norway's own booking-lead-time data].

| Stage | What is happening | The buyer's question | Dominant forces | Job of the ad | Best-fit levers | Format and platform |
|---|---|---|---|---|---|---|
| 1. Trigger | Something starts the thought: first snow, a friend's photo, a bad week at work, a birthday, last season's regret | "Could I do something like that?" | Push, pull | Interrupt with one vivid, specific scene and a hint at who it is for. Start the anticipation. | Concrete image, curiosity gap, unity, awe, Pre-Suasion first line | Meta Reels and feed video; X short text with one strong image; no price pressure |
| 2. Consideration (exploration and evaluation) | Looking at resorts, operators, reviews, flights; the shortlist forms; many touchpoints over weeks | "Is this one of the right ones? Why Norway, why Voss, why these people?" | Pull versus habit | Earn shortlist status. Show the why-Norway case, the guide's credibility, the trip's shape, real proof. | Social proof, authority, liking, specifics (insider signals), "best" content | Carousel, short guide-led video, review cards; retargeting; X threads with the guide's voice |
| 3. Doubt | The group chat, the partner, the spreadsheet, the worry | "Can I do it? Is it safe? Is it worth it? What if it goes wrong? Will my group say yes?" | Anxiety | Answer the one objection the buyer cannot ask out loud. Arm the champion for the second reader. Lower ability barriers. | Risk reversal (cancellation), price transparency, anxiety FAQ, level descriptions, group quotes, forward-ready summary | Retargeting to site visitors; FAQ carousels; click-to-chat; shareable link and "send to your group" summary |
| 4. Decision | A date is picked, a deposit paid, or the idea is dropped | "What is the next small step? What happens after I pay?" | Ability, prompts | Make the next step tiny and clear: dates, total price, deposit, what happens next. Honest urgency only when a real deadline exists. | Facilitator prompt, commitment (deposit, hold), true scarcity if verified, power of free (a real add-on) | Retargeting with dates and price; direct response; X reply to enquiries |
| 5. After booking (anticipation and story) | Waiting for departure; sharing with friends; the trip itself; the memory | "Did I make the right call?" | Habit, relatedness | Not an ad job in the strict sense. But the same team can use email and social to keep the countdown warm and to collect reviews, which feed stages 2 and 3. | Anticipation, autonomy, competence, relatedness | Email, WhatsApp, owned channels; request review and consent for UGC |

Interplay with the messy middle: the buyer loops between stages 2 and 3 several times. Google found preferences shift easily in travel (34 percent switched with no bias applied in the package holiday simulation). A guest at stage 4 can slide back to stage 2 if a competitor's review appears. The ad family should keep proof flowing during the loop.

**How adwright should use this.** The first question the skill asks is "which stage?". It then loads the stage's levers and refuses to mix jobs (a trigger ad that quotes price per day is a mismatch). For each trip it produces: three stage-1 spark ads, two stage-2 proof ads, two stage-3 objection or champion ads, one stage-4 facilitator ad. Stage 5 is delivered as a short post-booking message set for the client's own channels.

---

## 9. Psychology-to-copy translation table

Platform fit is my editorial judgement, not a tested result: "Meta" means Facebook and Instagram feed, Stories and Reels; "X" means short text, replies and threads. Example lines use bracketed placeholders for facts the client must supply. Confidence labels refer to Section 1.

| # | Principle | What to write | Example line for a ski trip | Platform fit | Misuse risk |
|---|---|---|---|---|---|
| 1 | Social proof (specific reviews) | Quote one concrete detail from a real guest, with first name and trip date. | "'Day two, the guide found us untracked snow ten minutes from the hut.' [Name], [month year], [trip]." | Meta strong (card or story); X good (quote post) | Invented or doctored reviews are illegal (UCPD fake review rules) [VERIFY]. Selective publishing. |
| 2 | Social proof (aggregate rating) | State the rating with its count, platform and date. | "[4.x] from [n] guest reviews on [platform], checked [date]." | Meta image overlay; X short line | Rounding up, hiding the count, old data. |
| 3 | Descriptive norm (peer group) | Use the closest group: "people on this same trip". | "Most guests on the [month] departure come as a group of [3 to 6] friends." | Meta; X | Unsourced "most". Needs booking data. |
| 4 | Authority (credentials) | Named qualification and years on this terrain. | "[Guide name], [certification body], [n] winters guiding around Voss." | Meta (guide video); X (guide's own post) | Fake or unverifiable credentials; award from a pay-to-play body. |
| 5 | Authority (third party) | An impartial publication or award, linked. | "Featured in [publication], [month year]." | Meta; X | Quote out of context; paid placements shown as editorial. |
| 6 | Liking | Warm, specific, local voice from a named person. | "I grew up at the bottom of this hill, so I will tell you which side of the road to park on." | Meta video; X personal voice | Fake persona; AI-voiced "guide". |
| 7 | Unity (identity by behaviour) | Name a shared behaviour and speak as "we". | "We are the ones who check the forecast on Wednesday and call in sick on Friday." | X (voice); Meta | Using a protected attribute as identity (age, health, status). Exclusion. |
| 8 | Reciprocity | Give a real asset, then ask softly. | "Free: our one-page packing list for a cold week in Voss. No sign-up wall." | Meta lead ad or link; X link post | A gate that collects data for unrelated use; "free" that hides cost. |
| 9 | Power of free | Offer a real, named add-on instead of a discount. | "Book by [date] and your airport transfer is on us (worth NOK [x])." | Meta; X | Using "free" to hide an inflated base price; add-on of little value. |
| 10 | Commitment (small yes) | Offer a low-cost first step. | "Pick your level and save two possible dates. No payment." | Meta (lead or landing); X link | Dark patterns: pre-ticked boxes, hidden payment steps. |
| 11 | Commitment (hold) | Name the deposit, the date of balance and the exit. | "Hold your place for NOK [x]. Balance due [date]. Cancel free until [date]." | Meta retargeting; X reply | Hidden conditions; deposit non-refundable without saying. |
| 12 | True scarcity (capacity) | State the fixed cap. | "Eight guests per departure. Always." | Meta; X | Cap that does not exist. Use only with confirmed operating rule. |
| 13 | True scarcity (live seats) | State the live number with date. | "[3] places left on the [date] departure (checked [day, time])." | Meta dynamic ads; X (manual only) | Stale numbers; fake counters. Illegal if false. |
| 14 | Real deadline | State the operational reason for the deadline. | "We book the hut on [date], so the group closes then." | Meta retargeting; X | Invented deadline; deadline that extends silently. |
| 15 | Anchoring (sourced) | Present a real, dated reference price beside the total. | "A six-day lift pass at [resort] is NOK [x] ([date], [source]). The guide is on top." | Meta carousel; X | Unlike-for-like comparison; stale price; legal limits on comparative ads [VERIFY]. |
| 16 | Per-day framing | Total first, per-day second. | "NOK 42,126 for nine days, about NOK 4,681 a day, all in." | Meta; X | Per-day alone; "all in" when not. |
| 17 | Price transparency | State what is and is not included. | "Included: [guide, lodging, meals]. Not included: flights, insurance, [gear rental NOK x]." | Meta carousel; X thread | Burying the "not included" in small print. |
| 18 | Risk reversal (cancellation) | State the exact policy in one line. | "Free cancellation until [date]. After that [rule]." | Meta; X | Overselling a limited policy. |
| 19 | Loss and regret (reflective) | Tie to a real window, without pressure. | "The [month] forecast window is short. The trip is easier to plan than to explain to yourself later." | Meta video; X | Shaming; false time pressure. Tone must stay light. |
| 20 | Gain framing | Describe the specific payoff. | "Seven mornings with the mountain to yourselves." | Meta; X | Overpromising conditions ("guaranteed powder"). |
| 21 | Mental accounting (treat) | Put the trip in the once-a-year account. | "Your one big trip this winter." | Meta; X | Pushing people to overspend. Be honest on total cost. |
| 22 | Anticipation | Sell the weeks before as part of the product. | "The countdown starts the day you book: gear list, route map, a message from your guide." | Meta; X | Promising features you do not send. |
| 23 | Experiential over material | Contrast the lasting memory with a possession. | "A new jacket lasts a season. This week lasts the dinner-table story for years." | Meta; X | Sneering at products; claim that happiness is certain. |
| 24 | Curiosity gap (honest) | Pose a specific open question and answer it on the landing page. | "The one line we only ski when the wind drops. Here is how we decide." | Meta; X thread | Clickbait that pays off nothing. |
| 25 | Concreteness (SUCCESs) | Replace adjectives with nouns, numbers and times. | "6:40 coffee, 8:00 first lift, 11:30 hut soup, 15:30 back for the sauna." | Meta carousel or story; X | False precision. Schedule must be real. |
| 26 | Story | One short scene with a turn. | "At 9:10 [guest] stopped at the top and said nothing. Then: 'Okay. Again.'" | Meta video; X thread | Invented guest quotes presented as real. |
| 27 | JTBD (push) | Mirror the stuck situation, not the person. | "Same week, same resort, same photos. Time to change one of the three." | Meta; X | Using a personal attribute as the push (age, family status). |
| 28 | JTBD (anxiety, level) | Answer the level worry with a fact. | "Level 2: confident on red runs. The guide splits the group if the day needs it." | Meta; X | Overstating level fit; unsafe "anyone can do this" claims. |
| 29 | JTBD (habit) | Respect the old way, then offer the new. | "Love the Alps? Keep them. Add one week somewhere quieter." | Meta; X | Disparaging competitors falsely. |
| 30 | SDT (autonomy) | Offer a choice inside a frame. | "Pick the route. The guide keeps the safety line." | Meta; X | Fake choice (all options are the same). |
| 31 | SDT (competence) | Promise a specific skill and test it. | "By day three you read snow layers well enough to pick tomorrow's line." | Meta; X | Claiming skills the course does not teach. |
| 32 | SDT (relatedness) and Happy Money (invest in others) | Show shared effort and shared rewards. | "Six of us, three levels, one table at the end of each day." | Meta; X | Pushing guilt about not going. |
| 33 | Costly signal (insider specifics) | Use named places, snow types and kit. | "Tour skis, skins, [named terrain], [transceiver]." | X (insider voice); Meta niche audiences | Jargon that excludes newcomers; wrong detail. |
| 34 | Fogg facilitator | Remove the next-step effort. | "Dates, total, deposit and level on one page. Tap to hold a place." | Meta retargeting; X link | A step that claims to be one tap but needs five. |
| 35 | Second reader (forward test) | Add a copy-ready summary. | "Forward this to the group: [trip], [dates], NOK [x] total, guided, [level]." | Meta (landing page, WhatsApp share); X reply | A summary that differs from the landing page. |
| 36 | Pre-suasion (first line) | Open with the image you want held in mind. | "Seven a.m., minus eight, the only sound is your skins." | Meta video hook; X first line | Hook that the offer does not deliver. |

Count check: 36 rows.

Notes on the table:

- Rows 12, 13, 14 and 18 carry legal exposure. They require a documented source.
- Rows 7, 27 and 28 border on Meta's personal attributes rule. Keep the language about behaviour and the offering.
- Rows 16 and 17 interact: per-day text never replaces the total or the inclusions.

**How adwright should use this.** Ship the table as a lookup file in the skill (principle, pattern, example, fit, risk). Every ad it writes carries a label saying which row it used and which risk it checked. The skill rotates levers across the test set so that test results show what works for Outdoor Norway's audience, not just what the textbooks claim.

---

## 10. Pre-flight checklist adwright can run before it outputs any ad

1. Stage: trigger, consideration, doubt, or decision. One only.
2. Force: which of push, pull, anxiety, habit does this ad address?
3. Lead lever: one principle from the table, with its confidence label.
4. Concreteness: at least one named place, number, time or sensation.
5. Proof: is a real source present or tagged as needed from the client?
6. Total price present, with inclusions or a link to them?
7. Second reader pass: do questions 1 to 3 survive a WhatsApp paste?
8. Personal attribute scan on Meta: no "you" plus a health, age, disability, financial, relationship or identity word.
9. Scarcity and urgency scan: any number or date must come with a source and a date.
10. Reduction scan: any "was/now" or "% off" needs prior price evidence [VERIFY with counsel].
11. Banned words and style scan (client rules): no dashes as punctuation, no emojis, no shouting caps, no filler transitions, none of the client's banned filler or AI-sounding words.
12. Honesty: would the client be comfortable if the guest saw how the line was built?

---

**How adwright should use this.** Run the checklist as the last step of every generation and print pass or fail per line in the working notes, not in the ad. Fail closed: if line 9 or 10 cannot be answered, the ad is held back.

---

## 11. Open questions and unverified items

| Item | Status |
|---|---|
| Forrester "27 touchpoints before conversion" claim | Appeared in a secondary blog summary of messy middle. Not verified. Do not use. |
| Think with Google travel pages (summer 2024 trends, "whats-next-for-travel") | Redirected and unreadable on 2026-10-06. Use only the APAC page that opened. |
| Expedia Path2Purchase 2023 numbers | Read via trade press, not the PDF. [VERIFY against PDF at go2.advertising.expedia.com] |
| Iglu 2026 survey sample size and method | Not in the trade article. [VERIFY] |
| Nawijn 2010 sample sizes and eight-week fade | Secondary summary only. [VERIFY] |
| Van Boven and Gilovich "83 percent" | Search summary only. [VERIFY] |
| Replications of Gilovich and Medvec regret and Heyman and Ariely norms (Collabra 2022) | Titles found, results not opened. |
| Meta policy exact current wording | Obtained through a summarising fetch. Confirm on the live page. |
| Norwegian "from price" rules for travel services | The guidance found is for real estate. [VERIFY with counsel] |
| Whether Norway applies the 30-day prior price logic to services | Guidance text refers to goods. [VERIFY with counsel] |
| Package travel obligations for Outdoor Norway's multi-day trips | Likely relevant. [VERIFY with counsel: definition, price-increase notice, information duties, insolvency protection] |
| BNPL or instalment copy | [VERIFY with counsel] |
| Group decision research for ski specifically | I found general tourism literature and trade blogs. No ski-specific peer-reviewed study of the second reader. Treat as hypothesis. |
| Click-to-WhatsApp availability and rules in Norway | [VERIFY in Meta Ads Manager] |
| Dwell time on feed ads | No source opened. Omit specific seconds from any shipped copy. |

---

## 12. Source list

Primary or near-primary (opened):

- Google and The Behavioural Architects, Decoding Decisions: The Messy Middle of Purchase Behavior (July 2020): https://www.thinkwithgoogle.com/_qs/documents/9998/Decoding_Decisions_The_Messy_Middle_of_Purchase_Behavior.pdf
- Scheibehenne, Greifeneder, Todd (2010), Can there ever be too many options: https://scheibehenne.com/ScheibehenneGreifenederTodd2010.pdf
- Forbrukertilsynet guidance on sales and conditional offers (2025): https://www.forbrukertilsynet.no/wp-content/uploads/2025/06/veiledning-om-reglene-som-gjelder-ved-markedsforing-av-salg-og-betingede-tilbud-l2398774.pdf
- Marketing Control Act (English, Lovdata): https://lovdata.no/dokument/NLE/lov/2009-01-09-2
- Meta Ad Standards, privacy violations and personal attributes: https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/
- Think with Google APAC traveller behaviours: https://business.google.com/en-all/think/consumer-insights/insights-apac-traveler-behaviors/
- Fogg Behavior Model: https://www.behaviormodel.org/
- Nawijn et al record: https://research.tilburguniversity.edu/en/publications/vacationers-happier-but-most-not-happier-after-a-holiday/
- Retraction Watch on Ariely (3 Sept 2026): https://retractionwatch.com/2026/09/03/procrastination-study-duke-dan-ariely-psychological-science-data-colada-tampering-retraction/
- Netthandel.no on Forbrukertilsynet and manipulative design: https://netthandel.no/forbrukertilsynet-forklarer-dette-ma-nettbutikkene-unnga-a-gjore/
- Iglu survey via Snowsports News (June 2026): https://www.snowsportsnews.com/newsrepository/2026/june/in-iglu-s-biggest-ever-survey-ai-use-for-ski-trip-research-nearly-quadruples-in-a-year-but-snow-certainty-and-trusted-advice-still-decide-where-britain-skis/
- Hotel News Resource on Expedia Path2Purchase: https://www.hotelnewsresource.com/article127422.html
- Marketing Dive on social traveller data (Data Axle, March 2025): https://www.marketingdive.com/news/social-traveler-numbers-say-influencers-white-lotus/745031/
- ScienceDaily on Kumar, Killingsworth, Gilovich (2014): https://sciencedaily.com/releases/2014/08/140825100051.htm

Papers cited from abstract pages or secondary summaries (grade B and below) are linked inline.
