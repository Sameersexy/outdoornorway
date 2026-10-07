# 01. The copywriting craft canon and frameworks

Research notes for adwright. Date of research: 2026-10-06. Client test case: Outdoor Norway (Voss), ski tours from NOK 1,948 (day tour) to NOK 42,126 (9 day trip).

## 0. How to read these notes

**Evidence grades used below**

| Tag | Meaning |
|---|---|
| [PRIMARY] | I opened and read the original text or the platform's own page. |
| [SECONDARY] | I read a summary, review or teaching page about the original. The idea is probably right, the exact wording is not guaranteed. |
| [VERIFY: reason] | A number or claim I could not confirm. Do not ship it in an ad or in the skill without checking. |

**What I actually opened (primary)**

- Claude Hopkins, *Scientific Advertising* (1923), full text from the ScientificAdvertising.com edition on the Internet Archive: https://archive.org/details/scientific-advertising (I downloaded the text and read chapters 3, 5, 7 and 8 closely).
- IPA / Les Binet and Peter Field, *The Long and the Short of It* presentation (41 slides): https://ipa.co.uk/media/5811/long_and_short_of_it_presentation_final.pdf
- Meta's own page on video ad performance: https://www.facebook.com/business/news/updated-features-for-video-ads
- Meta's feed image ad spec page: https://www.facebook.com/business/ads-guide/image/facebook-feed/traffic
- Orwell, "Politics and the English Language": https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-works/politics-and-the-english-language/
- Copyhackers (Joanna Wiebe) pages on voice of customer and review mining; Harry Dry's Marketing Examples pages.
- The client's own `campaigns/ski-meta-ads/tours.json` (prices and departures, confirmed by Sameer on 2026-10-06).

**What I could not open**

Most of the books are in copyright and not freely online: Ogilvy, Caples, Schwartz, Sugarman, Halbert, Bencivenga, Kennedy, Collier, Sullivan, Hormozi, Sharp, Sutherland, Trott. For these I used teaching pages, summaries and quote collections. Where a number comes only from a summary I say so.

Publication years of in-copyright books (Sugarman 2007, Hormozi 2021, Sharp 2010, Binet and Field 2013, Sutherland 2019, Ogilvy 1963 and 1983) are given from general knowledge, not from a page I opened [VERIFY before quoting in public].

**Failed or empty fetches (so you know the gaps)**

- Campaign's Ogilvy excerpt: HTTP 403.
- X's own creative best practices and ad specs pages: HTTP 402. Every X-specific number below is therefore [SECONDARY] or [VERIFY].
- Meta's help page on the Stories and Reels safe zone: fetch returned only a title. The safe zone percentages in section 7 come from a search snippet.
- Meta's Reels ads page and ad creative page: returned a login wall.
- TED transcript for Sutherland: not rendered. I used a transcript site instead.
- marketingbullets.com (Bencivenga): HTTP 503. Bencivenga material is [SECONDARY].

**Style note for whoever reads this in the skill:** the client's rules (no dashes, no emojis, no shouting, no filler) apply to the ads and to these notes. Example ads below are marked **[illustrative]**. They use only facts from `tours.json` plus brand facts from the brief. Any claim about what the tour includes is flagged **[fact needed]**.

---

## 1. The three formats and their physics

adwright writes three kinds of text. Each one has a different job and a different amount of room.

| Format | Room | What the reader sees first | Its job |
|---|---|---|---|
| On-image headline (static) | 3 to 20 words (client rule) | The image, then the headline in under a second | Carry the one idea. Hail the right person. |
| Primary text hook (Meta) | About 125 characters visible before "See more" | The first line | Earn the next line. Give the reason or the offer. |
| X post | 280 characters standard | The first line in the timeline | Stand alone. No image rescue. |
| Reel hook (video) | First 3 seconds, on-screen text plus visual | Motion and a text line | Stop the thumb and promise something. |

**Facts about the limits**

- Meta's own spec page lists feed image ad primary text at "50-150 characters" and headline at "27 characters", with a 4:5 image at 1440 x 1800 px [PRIMARY: facebook.com/business/ads-guide/image/facebook-feed/traffic].
- The "125 characters" truncation figure is a practical number, not an official one. A spec explainer states the cutoff is layout driven, "not officially published as a fixed number", and varies by device (about 110 on a small iPhone, about 135 on a large one, about 80 with accessibility text scaling) [SECONDARY: https://adplus.com/tools/ad-specs-validator/facebook-125-character-primary-text]. The same source recommends putting the hook in the first 40 characters. Treat both as design rules, and re-check against the Meta ads guide before publishing the skill.
- Meta research (with Nielsen) says up to 47% of the value of a video campaign was delivered in the first three seconds and up to 74% in the first ten. Meta also says 65% of people who watch the first three seconds go on to watch at least ten seconds [PRIMARY: facebook.com/business/news/updated-features-for-video-ads]. That page is undated and the figures look several years old [VERIFY: study date]. The direction is useful. The exact numbers should not be quoted as 2026 benchmarks.
- X: standard posts are 280 characters. I could not open X's own pages. Third party guides say the best performing ad copy is short (50 to 100 characters) and only the first ~40 characters show before truncation [VERIFY: both figures, secondary only]. Premium accounts can write longer posts, which does not change the ad discipline [VERIFY].

**How adwright should use this.** Write the three formats as one system, not three copies of one line. The image headline carries the idea. The primary text line gives the reason and the number. The X post is a self-contained version that works with no picture. Count characters in code, never by eye, and build the hook so the first 40 characters could stand alone.

---

## 2. The canon, person by person

Format for each entry: the idea (two sentences), when it works, when it fails, one real example with where it is documented, and the mapping to a static image ad, a Reel hook, and an X post.

### 2A. Foundations: Hopkins, Collier, Caples, Ogilvy

#### Claude Hopkins, *Scientific Advertising* (1923) [PRIMARY]

**Idea.** Advertising is salesmanship in print, and it can be measured. Test headlines with keyed coupons, and make every claim specific and checkable.

Passages worth keeping (from the text I read):

- Headline job: "The purpose of a headline is to pick out people you can interest... So the first thing you say is, 'Hey there, Bill Jones' to get the right person's attention." (Chapter 5)
- Test results: "It is not uncommon for a change in headlines to multiply returns from five to ten times over." The author says he had "keyed returns on nearly two thousand headlines used on a single product." (Chapter 5)
- Reader behaviour: "They skip three-fourths of the reading matter which they pay to get." (Chapter 5)
- Specificity: "Platitudes and generalities roll off the human understanding like water from a duck." "Say that a tungsten lamp gives more light than a carbon and you leave some doubt. Say it gives three and one-third times the light and people realize that you have made tests and comparisons." (Chapter 7)
- Offer service: "The best ads ask no one to buy." They "offer wanted information" and let the customer "prove the claims without any cost or risk." (Chapter 3)
- Limited offers: "an offer limited to a certain class of people is far more effective than a general offer." (Chapter 6)
- Free is not always good: "It is hard to pay for an article which has once been free." A paid coupon beat a free sample for the same product. (Chapter 6)
- Tell the full story: "Bring all your good arguments to bear." (Chapter 8). Note the conflict with one idea per ad, handled in section 3.

**When it works.** Skeptical or unfamiliar offers, price-sensitive buyers, any place you can measure. Specific numbers beat superlatives every time in the examples he gives.

**When it fails.** Hopkins wrote for a newspaper reader with time to read. A 12 word headline cannot "tell the full story". His mail order era assumed one insertion and one decision. Social feeds give you a glance.

**Real example.** Chapter 7: a brewer stopped saying "pure beer" and described the plate glass cooling room, the filtered air, bottles "washed four times by machinery", water from "4,000 feet", and "1,018 experiments" for the yeast. The text does not name the brewer. Teaching sources say it was Schlitz, and one search summary says sales rose from fifth place to a tie for first within months [SECONDARY: search summary, page not opened; VERIFY both the brewer name and the rank claim]. Also in Chapter 7: "Our net profit is 3 percent" beat "Lowest prices in America", and a razor maker advertised "a 78-second shave".

**Mapping.**
- Static: hail the person in the headline ("Never skied backcountry?"), then give one number.
- Reel: the first on-screen line names who it is for. Hopkins' "Hey there, Bill Jones" is the Reel hook.
- X: first line is a number or a named group. Skip adjectives like "best".

#### Robert Collier, *The Robert Collier Letter Book* (1931) [SECONDARY]

**Idea.** Start inside the reader's existing thoughts. The line usually quoted is "Always enter the conversation already taking place in the customer's mind" [VERIFY: exact wording and page, secondary quote pages only; the Letter Book date of 1931 is from https://www.jeremymac.com/blogs/news/7-copywriting-tips-from-the-robert-collier-letter-book-that-still-work-today].

**When it works.** Anywhere you can find the reader's own words (reviews, comments, forum posts). **When it fails.** When "their conversation" is guessed instead of researched, which gives generic pain-point copy.

**Real example (applied form).** Copyhackers review mining for the Beachway rehab centre: the control headline "Your Addiction Ends Here" lost to "If you think you need rehab, you do", a line lifted from a reviewer. The mined headline got more than 400% more clicks on the CTA button and more than 20% more lead form submissions [PRIMARY: https://copyhackers.com/2014/10/amazon-review-mining/ . Single client case, Copyhackers' own report].

**Mapping.** Static: use a phrase a real guest wrote. Reel: open with the sentence a customer says before they book. X: quote the guest phrase as the first line, with the source type (not a fake name).

#### John Caples, *Tested Advertising Methods* (first published in the early 1930s) [SECONDARY]

**Idea.** Headlines work through self-interest, news or curiosity, and the only way to know is to test. "It's what you say that counts, not how you say it" [SECONDARY quote: https://maverickwords.com/4-copywriting-lessons-from-john-caples-tested-advertising-methods].

Facts: sources disagree on the first edition year (1930 in one Wikipedia summary, 1932 in others) [VERIFY]. The book catalogues about 35 headline formulas in categories such as keywords (How to, Why, Who else, Which), benefit headlines, news headlines, price headlines, and one to three word headlines [SECONDARY: https://larslofgren.com/john-caples-headline-formulas/ . The page names the categories but did not include examples].

**When it works.** Self-interest first, news second, curiosity only when the payoff is clear. **When it fails.** Pure curiosity with no benefit, and "clever" headlines. Caples' own tone: blunt beats beautiful.

**Real example.** "They Laughed When I Sat Down at the Piano... But When I Started to Play!" for the U.S. School of Music, written in 1926 when Caples had been at Ruthrauff & Ryan about a year [SECONDARY: https://archive.seattletimes.com/archive/19900611/1076601/john-caples-author-of-famous-ad-line ; Wikipedia gives 1926, some sources 1925, VERIFY]. It spawned decades of "They laughed when..." imitations. No sales figures are documented in the sources I read.

**Mapping.** Static: story headline with the payoff visible in the picture (skier on a ridge). Reel: a before and after in three seconds is the piano ad in video form. X: story opener, reveal in the same post.

#### David Ogilvy, *Confessions of an Advertising Man* (1963) and *Ogilvy on Advertising* (1983) [SECONDARY]

**Idea.** The headline does most of the work, so do research first and put the promise and facts in the headline. "On the average, five times as many people read the headlines as read the body copy. It follows that unless your headline sells your product, you have wasted 90 percent of your money" [SECONDARY quote page: https://swipefile.com/five-times-as-many-people-read-the-headlines-david-ogilvy].

More material from teaching summaries, all [SECONDARY] and the percentages [VERIFY: could not trace to the book text]: headlines with a benefit, news, specifics, and the target audience named do better; avoid puns and wordplay; put the brand name in the headline [https://www.shortform.com/blog/writing-headlines/]. A summary also says Ogilvy advised six to twelve words and wrote at least sixteen headlines per ad [SECONDARY].

**When it works.** High consideration products with real facts to tell. **When it fails.** Commodity products with no news. A feed ad gets a glance, so "long headline with the whole promise" has to survive at 3 to 20 words.

**Real example.** Rolls-Royce, late 1950s: "At 60 miles an hour the loudest noise in this new Rolls-Royce comes from the electric clock." He spent about three weeks reading about the car, and the line came from a quote by the Technical Editor of *The Motor* [SECONDARY: https://www.enchantingmarketing.com/david-ogilvy-rolls-royce-advert/]. Ogilvy is quoted as saying "In my first Rolls-Royce advertisement, I used 719 words... In the next one I used 1400 words" [SECONDARY: https://swiped.co/file/rolls-royce-ad-by-david-ogilvy/]. Dates differ (1957, 1958, 1959) across sources [VERIFY]. One claim says he wrote 26 headlines to pick this one [SECONDARY, unconfirmed].

**Mapping.** Static: a fact that implies the benefit (Rolls-Royce never says "quiet"). Reel: spoken or on-screen fact, one per three seconds. X: the fact as line one, source as line two.

**How adwright should use this.** The foundations give five rules the skill can enforce. (1) Name the person in the first words. (2) One specific number beats any adjective. (3) Use the reader's own words, found by research. (4) Test, and write many headlines before picking. (5) Do not copy Ogilvy's long copy into a 125 character slot. Long copy belongs on the landing page, not in the ad.

---

### 2B. Eugene Schwartz, *Breakthrough Advertising* (1966) [SECONDARY]

**Idea.** Copy cannot create desire. It channels desire that already exists in the market. Then two diagnostic questions decide the copy: how aware is the reader (five levels), and how many similar claims has the market already heard (five stages).

The quote, as repeated by several summaries: "Copy cannot create desire for a product. It can only take the hopes, dreams, fears and desires that already exist in the hearts of millions of people, and focus those already existing desires onto a particular product" [SECONDARY: https://mirasee.com/blog/eugene-schwartz-breakthrough-advertising/ and others; VERIFY page].

**The five levels of awareness**

| Level | What the reader knows | Lead with | Typical headline job |
|---|---|---|---|
| Unaware | Nothing wrong, not looking | An identity, a story, or a surprising claim. Do not name the product | Echo an emotion or surface a problem |
| Problem aware | Has the pain, thinks it has no fix | Name the pain in their words, hint it is solvable | Name the need |
| Solution aware | Knows a solution type exists, not your product | Your mechanism and why others fall short | State the result and the how |
| Product aware | Knows you, not yet convinced | Proof, differentiation, objection handling | Add new proof or a new angle |
| Most aware | Wants it, needs a reason to act today | The offer, price, date | Product name and deal |

Sources for the table: https://selzee.com/eugene-schwartz-5-levels-of-awareness (approach per level, its example headlines are modern illustrations, not Schwartz's) and the Copyhackers/Mirasee-style summaries above [SECONDARY]. Note: summaries disagree on exact level names ("desire aware" appears in one). The five used here are the common version.

**The five stages of market sophistication**

| Stage | Market condition | What wins | Example in the weight loss category (selfstorming.com, an illustration) |
|---|---|---|---|
| 1 | No one has made the claim | State the claim plainly | "This pill makes you lose weight." |
| 2 | Others copy it | Enlarge the claim | "Lose twice the weight in half the time." |
| 3 | Claims are tired | Introduce a new mechanism (the how) | "Lose weight thanks to a new fat-blocking enzyme." |
| 4 | Mechanisms copied | Elaborate or improve the mechanism | "A second-generation enzyme that works without the side effects." |
| 5 | Everything has been heard | Sell identity and belonging | "Join the people who train like this." |

Source: https://www.selfstorming.com/tools/libraries/frameworks/market-sophistication and https://auresnotes.com/summary-breakthrough-advertising-eugene-schwartz/ [SECONDARY]. Schwartz's own recommendation for stage 3 is a strong quick promise followed by "the reason why you can deliver" [SECONDARY].

**When it works.** It tells you which of the other tools to pick. It is a diagnosis, not a template. **When it fails.** When used as a rigid label on a small local category where nobody has measured the stage. Judge sophistication by looking at what competitors actually run (the public Meta Ad Library lists live ads) rather than guessing.

**Real example.** Hopkins' chapter 7 shaving soap story is a sophistication story avant la lettre: when everyone said "abundant lather", the new maker said "Multiplies itself in lather 250 times" and "Softens the beard in one minute" (a stage 2 to 3 move: enlarge and make specific).

**Mapping.**
- Static: the awareness level decides the headline subject. Unaware gets an identity or surprise. Most aware gets dates and price.
- Reel: unaware needs a stronger visual hook and a story. Most aware can lead with the text of the deal.
- X: unaware posts need a standalone claim. Most aware posts can be a plain price and date list.

**For Outdoor Norway [illustrative guess, to be checked with real competitor ads].** Ski holidays in general sit at stage 4 to 5 ("powder paradise", "bucket list"). Guided backcountry day tours from a named place are a narrower category, probably stage 2 to 3. The 9 day trip competes in the saturated "ski trip" world, so it needs a mechanism or an identity, not "amazing".

**How adwright should use this.** Make awareness level and sophistication stage required inputs at the start of every job (default to asking, and default to "problem aware, stage 3" if the user gives nothing). The decision tree in section 8 turns the two answers into a framework and a hook type. Never invent the stage. If the user cannot say, adwright should offer to look at competitor ads first.

---

### 2C. Direct response masters: Halbert, Sugarman, Bencivenga, Kennedy

#### Gary Halbert [SECONDARY]

**Idea.** Choose the market before the message ("starving crowd"), and make mail look like it belongs in the personal pile. The "A-pile" is personal mail people always open, the "B-pile" is commercial mail [SECONDARY: https://www.profitableads.com/gary-halbert/ via search snippet]. The starving crowd quote: "The only advantage I want is a starving crowd" [SECONDARY, same source].

**When it works.** When audience and message match tightly, and when the ad looks native to the place it appears. **When it fails.** When "personal" is faked (fake handwriting, fake urgency). It also does not map to a feed that already picks audiences by itself.

**Real example.** The "Coat of Arms" letter (1971): one page, under 400 words, a plain envelope and the reader's surname in the first line. Claimed mailings of 600 million over thirty years come from Halbert's side and have not been audited [SECONDARY: https://x.com/ucheokorolive/status/1424681673225027585 and https://medium.com/@andy.a.g/the-sales-letter-that-mailed-for-thirty-years-worked-because-it-did-not-look-like-an-ad-89eb7acf9ba8 ; VERIFY: 600 million and the order figures].

**Mapping.** Static: an unpolished, native look can beat a polished ad (see Dry on ugly ads). Reel: a person talking, not a brand. X: write as a person, not a company.

#### Joe Sugarman, *The Adweek Copywriting Handbook* (2007) [SECONDARY]

**Idea.** The only job of the first sentence is to get the second sentence read. Build a "slippery slide" so each line pulls into the next, and sell on emotion while justifying with logic.

Summaries credit the book with about 31 psychological triggers (counts vary by source), 23 copy elements and 10 graphic elements [SECONDARY: https://marketingleader.guide/guides/profile-adweek_copywriting_handbook; VERIFY exact counts]. Lessons with quotes: "sell a concept, not a product", "You sell on emotion, but you justify a purchase with logic" [SECONDARY: https://www.creative-copywriter.net/content-marketing/learning-from-joseph-sugarman]. Harry Dry also flags the same idea: "Think slippery slide" and "Your first line is crucial" (tips 14 and 16 of his 17 [PRIMARY: https://marketingexamples.com/copywriting/tips]).

**When it works.** Anything with a sequence: primary text, X threads, Reel scripts. **When it fails.** Curiosity seeds with no payoff. They create irritation, and Meta's feed has no patience for it.

**Real example.** Sugarman's BluBlocker infomercials are widely cited, but I found no figures in the sources I could open, so I do not use them here [VERIFY].

**Mapping.** Static: the headline is "sentence one", the primary text first line is "sentence two", and the price line is "sentence three". Reel: each caption pulls to the next. X: line breaks as the slide, one beat per line.

#### Gary Bencivenga [SECONDARY]

**Idea.** Persuasion needs four things: an urgent problem, a unique promise, unquestionable proof, and a user-friendly proposition (the offer). His proof test is a jury question: "What proof would I need to persuade a fair-minded jury beyond a reasonable doubt that my copy rings true?" [SECONDARY: https://gameofconversions.com/gary-bencivenga-shoestring-business-ad-the-bencivenga-persuasion-equation/ and a search summary of his Marketing Bullets; VERIFY wording].

He also teaches reasons why in three areas: why the product is better, why to believe the claim, why to act now. And he repeats the point that "because" lifts belief (see the Langer study in section 3).

**When it works.** Any claim a customer could doubt. **When it fails.** If you have no proof, no copy trick will fix it. Bencivenga's lesson is to get proof first.

**Real example.** His "Shoestring Business" ad is cited in the same source. I did not read the ad itself, so I do not describe it [VERIFY].

**Mapping.** Static: proof shown in the image (the real photo of a real group, a date, a count). Reel: proof inside three seconds (real footage, not stock). X: the proof is line two.

#### Dan Kennedy [SECONDARY]

**Idea.** Success comes from matching market, message and media, and from a strong offer. His line "match bait to critter" and the "Godfather's offer", one the right prospect cannot refuse [SECONDARY: https://www.entrepreneur.com/growing-a-business/the-3-ms-of-successful-direct-marketing-campaigns-new/313518 and https://hooshmand.net/no-bs-direct-marketing-dan-kennedy-summary/]. He is credited with calling Problem, Agitate, Solution "the most reliable sales formula ever invented" [SECONDARY: http://www.nonprofitcopywriter.com/PAS-copywriting-formula.html ; the date of origin is unclear, one source says 2006 for *The Ultimate Sales Letter*, which looks like a later edition. VERIFY].

**When it works.** Lead generation and anything with a definable offer and deadline. **When it fails.** Fake deadlines and fake scarcity. They cost trust, and Hopkins already warned that exaggeration makes readers "discount all the statements that you make".

**Real example.** The Kennedy Triangle itself. For concrete documented ad results, I did not find a source I could verify [VERIFY].

**Mapping.** Static: the offer is the headline for warm audiences. Reel: the deadline on screen. X: offer, deadline, link, nothing else.

**How adwright should use this.** From this group, the skill keeps four tests: (1) Does line one earn line two (Sugarman)? (2) Is the claim provable and is the proof visible (Bencivenga)? (3) Is the offer clear, with a real date or limit (Kennedy)? (4) Does the ad look native and human (Halbert)? Real scarcity exists in the client data: the 6 day package has only two departures (29 Jan and 4 Feb 2027), the 9 day trip has five (30 Jan to 18 Apr 2027), and the Valentine's departure is 12 to 14 Feb. Do not invent seat counts. Ask the client [fact needed].

---

### 2D. The creative revolution: Bernbach, Abbott, Sullivan, Trott, Sutherland

#### Bill Bernbach (DDB) [PRIMARY for the Lemon text, SECONDARY for the rest]

**Idea.** "Advertising is fundamentally persuasion and persuasion happens to be not a science, but an art" [SECONDARY: https://en.wikipedia.org/wiki/William_Bernbach]. DDB paired a copywriter and an art director in one room, and used honesty, wit and white space to win against louder advertisers.

**When it works.** Brands with a true weakness they can turn into a strength; markets full of boasting. **When it fails.** When the "honest admission" is not backed by a real strength, or when the audience wants a plain offer.

**Real examples.**

- VW "Lemon" (1960, DDB). Full copy, as published in multiple collections: "Lemon. This Volkswagen missed the boat. The chrome strip on the glove compartment is blemished and must be replaced. Chances are you wouldn't have noticed it; Inspector Kurt Kroner did. There are 3,389 men at our Wolfsburg factory with only one job: to inspect Volkswagens at each stage of production... tote up 189 check points... say 'no' to one VW out of fifty... We pluck the lemons; you get the plums." [SECONDARY: transcription via search, see https://swipefile.com/volkswagen-lemon-print-ad/lemon-ad . VERIFY against a scan before quoting in the skill]. Note the structure: one word headline, specific numbers, a twist in the last line.
- VW "Think Small" (1959), written by Julian Koenig with art director Helmut Krone. Advertising Age named the VW campaign the best of the 20th century in 1999 [SECONDARY: https://en.wikipedia.org/wiki/Think_Small].
- Avis "We try harder" (1962), copywriter Paula Green with Krone. Avis moved from a loss of $3.2 million to a profit of $1.2 million in the first year. The market share gap against Hertz narrowed from 61 to 29 to 49 to 36 between 1963 and 1966 [SECONDARY: https://slate.com/business/2013/08/hertz-vs-avis-advertising-wars-how-an-ad-firm-made-a-virtue-out-of-second-place.html ; the cause of the profit is not isolated from other factors]. Lines like "Avis can't afford dirty ashtrays" show the structure: a concession plus a promise.

**Mapping.** Static: one image, one honest line, lots of space. Reel: the confession as the hook ("The worst thing about this trip..."). X: a plain admission with a specific number, then the redeeming fact.

#### David Abbott (AMV) [SECONDARY]

**Idea.** Plain, specific, friendly writing that treats the reader as intelligent. His copy was described as "easier to read than to ignore". Rules attributed to him: "If facts persuade, learn how to write a list so it doesn't read like one", small admissions create larger acceptance, and "plain, simple and familiar" words [SECONDARY: https://briefercopy.com/blog/david-abbott/]. Known work: Sainsbury's, Volvo, The Economist, Yellow Pages, Ikea, Chivas Regal, RSPCA [SECONDARY: https://en.wikipedia.org/wiki/David_Abbott_(advertising)]. I could not open any single Abbott ad text, so I name no ad copy here [VERIFY].

**When it works.** Considered purchases, informed buyers, long copy on landing pages. **When it fails.** In a 20 word slot, the technique shrinks to "plain words and one honest fact". That still works.

**Mapping.** Static: plain words, one fact. Reel: spoken script in everyday speech. X: a list written so it does not read like one (section 3, price list example).

#### Luke Sullivan, *Hey Whipple, Squeeze This* [SECONDARY, thin]

**Idea.** The summaries I could open say: start from the truest thing you can say about the brand; "Don't do an ad. Do something interesting"; reduce the ad to one element; find the emotional centre [SECONDARY: https://www.befreed.ai/book/hey-whipple-squeeze-this-by-luke-sullivan-with-sam-bennett , https://sobrief.com/books/hey-whipple-squeeze-this ; the second page returned 403 so I rely on search snippets]. A class reading of chapter 6 gives "simpler is always better" and "instant comprehension" for print [SECONDARY: https://openlab.citytech.cuny.edu/lulucomd2400sp2024/2024/04/17/reading-chapters-5-6-and-7-of-hey-whipple-squeeze-this-6th-edition/]. I could not verify his specific craft methods, so I do not attribute any.

**Mapping.** All three formats: the one-element test. Can the ad be described in one sentence by someone who saw it for two seconds?

#### Dave Trott [SECONDARY]

**Idea.** Be simple, direct and aimed at real people. Quoted from his work: "To grab hold of either [revenue or attention], we need to create a single, powerful message that people believe" and "Most people ignore advertising because most advertising ignores people" [SECONDARY: https://www.goodreads.com/work/quotes/25311444-predatory-thinking-a-masterclass-in-out-thinking-the-competition ; VERIFY: the second line is also attributed to others]. Books: *Creative Mischief* (2009), *Predatory Thinking* (2013) [SECONDARY: http://davetrott.co.uk/books/].

**When it works.** Crowded categories, and any time a team is tempted to add a second message. **When it fails.** When "simple" becomes empty. A simple message still needs a fact.

**Mapping.** Static, Reel, X: the "single message that people believe" test. Count claims. More than one claim means two ads.

#### Rory Sutherland, *Alchemy* (2019) [SECONDARY]

**Idea.** Value is perceived, so changing perception can be cheaper than changing the product. "Logic is what you use when you want to be right; psycho-logic is what you use when you want to be successful" [SECONDARY, attributed in a summary: https://www.antoinebuteau.com/lessons-from-rory-sutherland/ ; VERIFY].

**Real example.** Eurostar. In his 2009 TED talk Sutherland says engineers spent six billion pounds to make the journey 40 minutes faster, and proposes spending a fraction of that on the experience instead [SECONDARY transcript: https://singjupost.com/rory-sutherland-behavioural-economics-humans-and-advertising/ . The "Wi-Fi" and "champagne and models" versions vary between retellings, VERIFY which lines are from the talk and which from the book].

**When it works.** Pricing, packaging, framing and naming decisions. **When it fails.** As an excuse for gimmicks when the product is weak.

**Mapping.** Static: reframe the price or the time ("one day, NOK 1,948" vs "weekend plan"). Reel: show the change in how it feels. X: a counterintuitive but true observation.

**How adwright should use this.** The creative revolution gives the skill its permission to be honest and short. Rules to encode: (1) Include one honest concession where the truth supports it (for example, a tour that is not for complete beginners). (2) Count claims and cap at one per ad. (3) Use plain words an Abbott reader would use. (4) Check whether reframing the price, date or name would do more than adding a feature. Never fake an admission.

---

### 2E. Modern evidence: Wiebe, Dry, Hormozi, Sharp, Binet and Field

#### Joanna Wiebe (Copyhackers): voice of customer [PRIMARY pages]

**Idea.** Copy comes from customers' words. "When you write copy, you're supposed to join the conversation happening in your customer's head" and the best place to ask is the thank you page: "What was going on in your life that brought you to [try/join/buy] [product name] today?" [PRIMARY: https://copyhackers.com/join-the-conversation-customer/ ]. Review mining method: identify the audience and their goals, find reviews of solutions they use, read 200 plus reviews, extract language into a table, find recurring themes, then test [PRIMARY: https://copyhackers.com/2014/10/amazon-review-mining/].

**When it works.** Always, when you have real text. **When it fails.** When the sample is tiny or one loud reviewer is treated as the market.

**Real example.** Beachway (see Collier). Plus Copy School's thank-you-page survey: about 65% completion, 230 responses [PRIMARY, same page. No conversion lift stated].

**Mapping.** Static: guest phrasing as the headline. Reel: read a review as the hook (with permission). X: quote and credit type.

**For Outdoor Norway.** Mine Google, TripAdvisor and Facebook reviews of Outdoor Norway and of competitors, and the Q and A of ski forums. The phrases a guest used to describe the day are the headlines. Never invent a testimonial.

#### Harry Dry, Marketing Examples [PRIMARY pages]

**Idea.** Three tests: can you visualise it, can you falsify it, can nobody else say it [SECONDARY summary of his course: https://www.upgrow.io/harry-dry-copywriting-3-rules/]. His 17 tips include: write with your eraser; avoid passive; kill adverbs and adjectives; more periods and fewer commas; find the tension; write how you talk; avoid "landing page words" (he lists verbs like empower and supercharge); think slippery slide; your first line is crucial [PRIMARY: https://marketingexamples.com/copywriting/tips]. On adjectives: "Adjectives are okay. Just ideas don't start with them." [PRIMARY: https://marketingexamples.com/copywriting/adjectives].

**When it fails.** His site is a teaching and entertainment product. Some of its numbers are the author's own or are retold from social posts. For example "Make Ugly Ads" says a single low-effort creative made "$50K return on a 'Post-it'" and credits two other people [PRIMARY page, unverified claim: https://marketingexamples.com/ads/ugly ; VERIFY].

**Real example.** Sky Bet "Super 6": "Predict six correct scores. Win £1 Million." Dry credits it with a customer acquisition cost of £2.60 against an industry norm of about £200, and lists six offer traits: low friction, life integration, social fit, big prize, perceived achievability, free participation [PRIMARY page: https://marketingexamples.com/copywriting/sky-bet ; VERIFY: the £2.60 and £200 figures, they are his, not audited]. Also his rhetorical devices lesson on "One Scoop. Once a day. Every day." (parallelism, tricolon, no verbs) [PRIMARY: https://marketingexamples.com/copywriting/rhetorical-devices].

**Mapping.** Static: run the three tests on the headline. Reel: the line you can see in your head. X: periods and rhythm.

#### Alex Hormozi, *$100M Offers* (2021) [SECONDARY]

**Idea.** The value equation: (Dream Outcome x Perceived Likelihood of Achievement) divided by (Time Delay x Effort and Sacrifice). Raise the top two and cut the bottom two [SECONDARY: https://www.selfstorming.com/tools/libraries/frameworks/value-equation and https://www.scalabl.com/literature/100m-offers/]. Add scarcity, urgency, bonuses, guarantees and naming to lift perceived value. Four guarantee types: unconditional, conditional, anti-guarantee, implied [SECONDARY: https://www.gregfaxon.com/blog/100m-offers-summary].

**When it works.** For deciding what to say in the offer line. **When it fails.** For premium travel, a pile of "free bonuses" can read as cheap. Hopkins already warned that giving things away free cheapens the main product. And the equation is a thinking model, not measured science.

**Real example.** The book's own offers are the documented examples, and I could not open the book [VERIFY].

**Mapping to the client.**
- Dream outcome: a day on a Norwegian mountain, or nine days of skiing.
- Perceived likelihood: guides, small groups, group level (beginner or advanced). Group size and guide ratio are [fact needed].
- Time delay: how soon do they ski? Day tours run "every Saturday and Sunday, from January to April" (tours.json), so "book now, ski this weekend" is a real reduction of delay.
- Effort and sacrifice: gear, transport, avalanche knowledge. What is included is [fact needed]. Each inclusion is a headline.

#### Byron Sharp, *How Brands Grow* (2010) [SECONDARY]

**Idea.** Brands grow by reaching many buyers and being easy to remember and easy to buy: mental and physical availability, with distinctive assets (colour, shape, sound, character). One summary quotes Sharp: "advertising works best when it doesn't try and persuade, but merely makes us remember the brand at the point of purchase" [SECONDARY: https://www.yourmarketingrules.com/how-brands-grow/ ; VERIFY: exact wording, quote is a summary line].

**When it works.** For deciding what to repeat across ads. **When it fails.** For a one-off promotion where the brand has no existing memory, and for a local operator selling a high-ticket trip. Sharp's research draws on large repeat-purchase categories (supermarket goods) and is debated for low-frequency purchases [VERIFY: scope].

**Mapping.** Static: the logo, the colour and one repeated phrase in the same place every time. Reel: brand cue in the first second. X: consistent opening shape.

#### Les Binet and Peter Field, *The Long and the Short of It* (2013) [PRIMARY slides]

**Idea.** In the IPA databank of campaigns, emotional campaigns drive brand effects and long-term business effects more than rational ones, and rational messages give a big direct effect that decays fast. I read the slides:

- "Rational messaging: Big direct effect, but decays quickly." "Emotional priming: Decays slowly. Smaller effect on sales." (slide on "Balance head and heart")
- "Fame quadruples efficiency" (annualised ESOV efficiency 1.4 for fame campaigns against 0.3 for others)
- "Talk to all your prospects" and "Aim for fame"
- A 60:40 split of budget between brand building and sales activation, refined in the 2018 report *Effectiveness in Context* to roughly 50:50 for online sectors and 54:46 for B2B [SECONDARY: https://www.campaignlive.co.uk/article/binet-field-reveal-key-formulas-brand-building/1495641 via search snippet, VERIFY; and https://ipa.co.uk/knowledge/effectiveness-research-analysis/les-binet-peter-field for the report existence].

[PRIMARY: https://ipa.co.uk/media/5811/long_and_short_of_it_presentation_final.pdf]. The databank held 996 campaigns from 1980 to 2010 [SECONDARY: https://www.alexmurrell.co.uk/summaries/les-binet-and-peter-field-the-long-and-the-short-of-it].

**When it works.** For setting the mix of ads across the funnel. **When it fails.** As a copy rule for a single small ad. The data come from awards entries by large, mostly UK brands. A small tour operator with a Jan to Apr season does not have the budget for fame, and the data do not say how a Voss operator should write line one.

**Mapping.**
- Static: one emotional image and one rational fact. Emotion gets the thumb to stop. The fact gets the click.
- Reel: emotion in the first seconds, fact in the caption.
- X: the rational post (price, dates) has a short life. The emotional or story post builds the memory. Alternate.

**How adwright should use this.** Treat these five as a system check. (1) Wiebe: no headline without a customer phrase or a stated reason it is missing. (2) Dry: score visualise, falsify, only-us. (3) Hormozi: list the four value levers and note which the ad moves. (4) Sharp: define a small set of brand cues and use them every time. (5) Binet and Field: each campaign should contain both rational activation ads (price, date) and emotional priming ads (story, scene), not only one kind.


---

## 3. Frameworks and building blocks

### 3A. The named formulas

A warning first. Most formulas are scaffolding for long copy (sales pages, emails, video scripts). In a 3 to 20 word headline or a 125 character hook they shrink to a checklist, not a structure. The honest use is: pick the formula to decide what to include, then cut until one idea remains.

For the examples I mostly rely on Copyhackers' formula guide, which names a live page for each formula [PRIMARY for the definitions: https://copyhackers.com/2015/10/copywriting-formula/ . I did not open the pages it names, so I do not describe them]. Where I show a worked reading of a classic ad, it is my own analysis and I say so.

**AIDA (Attention, Interest, Desire, Action)**
- Idea: capture attention, hold interest with fresh information, build desire, request the action.
- History: the origin is contested. A *Printers' Ink* item from 9 February 1898 already said an ad "must attract attention, of course; but attracting attention is only an auxiliary detail". E. St. Elmo Lewis is the usual name, with a 1910 line "All advertising must attract attention, maintain interest, arouse desire, get action". Arthur Sheldon added satisfaction in 1911, and the first AIDA acronym reference cited by Wikipedia is a 1921 *Printers' Ink* article by C. P. Russell [SECONDARY: https://en.wikipedia.org/wiki/AIDA_(marketing)]. Critics note it assumes a straight line from awareness to purchase, which research has not supported.
- Works: as an order check on a long page. Fails: as a model of how people decide on a feed, where attention, desire and action can happen in two seconds.
- Mapping: static image = attention; headline = interest; the price and date lines = desire and action. Reel: all four in 15 seconds. X: attention and action only.

**PAS (Problem, Agitate, Solve)**
- Idea: name the problem, make it felt, then offer the fix. Dan Kennedy is credited with calling it "the most reliable sales formula ever invented" [SECONDARY: http://www.nonprofitcopywriter.com/PAS-copywriting-formula.html].
- Works: problem aware audiences, Reels (problem in 3 seconds, agitate in the next 5, solve in the rest). Fails: aspirational products. A ski holiday is a treat, so heavy agitation sounds wrong. Also, Meta has ad policies about implying you know personal attributes ("Are you overweight?") [VERIFY: Meta Advertising Standards, personal attributes section; not opened].
- Real example: Copyhackers names a Ramit Sethi page [not opened]. My reading: the Caples piano ad is PAS in a story shape: the problem is the laughter, the agitation is the wait, the solve is the first note.

**BAB (Before, After, Bridge)**
- Idea: describe life now, life after, and the bridge between. It is PAS without the pain [SECONDARY: https://copyhackers.com/2015/10/copywriting-formula/ and https://dowordsgood.com/before-after-bridge-formula-ad-trick/ ; I could not find who first defined BAB, VERIFY].
- Works: aspiration and travel, six second video. Fails: when the "after" cannot be shown honestly.
- Mapping: static = split frame; Reel = cut from the desk to the ridge; X = one line each for before, after, bridge. **[illustrative]** "Monday: inbox. Saturday: a Norwegian mountain. NOK 1,948." (57 characters, uses the real day tour price.)

**4Ps (two competing versions)**
- Version 1 (Henry Hoke Sr.): Picture, Promise, Prove, Push. Version 2 (Ray Edwards, as listed by Copyhackers): Problem, Promise, Proof, Proposal [SECONDARY: https://copyhackers.com/2015/10/copywriting-formula/ ; the Hoke attribution comes from https://copywriting.school/formulas/pppp-picture-promise-prove-push , VERIFY].
- Works: the two versions agree on the middle: promise then proof. Fails: sources mix the two, so do not cite "the 4Ps" without saying which.
- Mapping: static carries the picture and the promise. The primary text carries proof and push.

**4Us (Useful, Urgent, Unique, Ultra-specific)**
- Idea: a scoring checklist for headlines, credited to Michael Masterson and the AWAI training school [SECONDARY: https://www.awai.com/2022/05/4-goof-proof-ways-to-write-irresistible-headlines/ ; the date "almost 24 years ago" is relative to 2022].
- Works: ranking 30 headlines quickly. Fails: when "urgent" is faked to score points.
- Mapping: the best fit for adwright. Use it as the headline scorecard in section 6.

**PASTOR (Problem, Amplify, Story, Transformation, Offer, Response)**
- Idea: Ray Edwards' structure for long copy that adds story to PAS [SECONDARY: https://www.shortform.com/blog/ray-edwards-p-a-s-t-o-r-framework/ and https://copywriting.school/formulas/pastor ].
- Works: sales pages, email, long X threads, a 60 second video. Fails: anything under 100 words. Do not force it on a 125 character hook.

**QUEST (Qualify, Understand, Educate, Stimulate, Transition)**
- Idea: start by naming who it is for, show you understand them, teach a better way, build desire, move them to act. Attributed to Michel Fortin [SECONDARY: search result summary, page not opened, VERIFY]. Copyhackers cites a Gene Schwartz ad as its example [not opened].
- Works: the "Qualify" step is Hopkins' "Hey there, Bill Jones". Fails: educational steps need room. Mapping: Reel scripts of 20 to 30 seconds.

**FAB (Feature, Advantage, Benefit)**
- Idea: describe the feature, what it does better, then what it means for the buyer. Works as a way to translate a spec into a headline. Fails when copy stops at the feature [SECONDARY: https://copyhackers.com/2015/10/copywriting-formula/].
- Mapping: write FAB, then publish only the B on the image, the A as the second line, and the F as proof.

**How adwright should use this section.** Do not expose the formula names to the end user as a menu. Use them inside the skill as hidden structure: AIDA as the order check on landing pages, PAS or BAB for Reel scripts, 4Us as the headline scorecard, QUEST step one as the audience line. Never let a formula lengthen an ad.

### 3B. Building blocks that sit under every formula

**One idea per ad**
- Idea: each ad makes one claim, so the reader leaves with one thing. Trott's version: "a single, powerful message that people believe" [SECONDARY, see 2D].
- Conflict to handle: Hopkins says "Bring all your good arguments to bear" and tells advertisers to pack the whole story into every ad because "the average reader is only once a reader" (Chapter 8) [PRIMARY]. He wrote for one insertion in a newspaper. A feed lets you run many ads to the same person, and Meta's current delivery rewards different concepts, not copies (see 7).
- Reconciliation for adwright: one idea per ad, many ads per campaign, and the full story on the landing page.
- Real example: VW "Think Small" and "Lemon" each make exactly one point. [SECONDARY, see 2D]
- Mapping: static = one idea; Reel = one idea per three seconds; X = one idea per post.

**Reason-why copy**
- Idea: give a reason with every claim. The credit for "reason why" goes to the earlier advertising writer John E. Kennedy, and Hopkins insisted copywriters research the product to find real reasons [SECONDARY: search summary of https://www.igi-global.com/dictionary/claude-hopkins/74465 and Wikipedia; VERIFY].
- Evidence on "because": Langer, Blank and Chanowitz (1978, photocopier study). When people asked to cut in line to copy 5 pages: no reason 60% compliance, real reason ("I'm in a rush") 94%, a pointless reason ("because I have to make copies") 93%. For 20 pages: about 24%, 42%, 24% [SECONDARY: https://atticusli.com/replication-crisis/power-of-because-langer-1978/ ; sample of 120 adults; VERIFY against the paper]. The lesson: a reason helps on small asks, and only a real reason helps on bigger asks. A NOK 42,126 trip is a big ask.
- Real example: Rolls-Royce and Lemon both give the reason inside the headline or the first sentence. [SECONDARY, see 2A and 2D]
- Mapping: static = the number is the reason; Reel = say the reason, not just the claim; X = "because" inside the first line.

**Specificity**
- Idea: replace general with exact. Hopkins' chapter 7 rule, in his words: "a man who makes a specific claim is either telling the truth or a lie... Specific facts, when stated, have their full weight and effect." Dry's test: "can you falsify it" [PRIMARY: Hopkins; SECONDARY: https://www.upgrow.io/harry-dry-copywriting-3-rules/].
- Works: nearly always. Fails when the specific number is unimportant ("37 mountains") or wrong.
- Real example: Hopkins' "78-second shave" and "Multiplies itself in lather 250 times" [PRIMARY].
- Mapping to the client (data from tours.json): "Saturday and Sunday, January to April", "NOK 1,948", "30 Jan to 7 Feb 2027", "5 departures". Those are all falsifiable and exact.

**Unique mechanism**
- Idea: tell people why this product delivers when others did not (Schwartz stage 3). The mechanism is the "how".
- Works: stage 3 and 4 markets. Fails: made-up mechanisms. A mechanism has to be true and visible.
- Real example: the brewer in Hopkins chapter 7 who described how the beer was made, when all rivals just shouted "pure". The thing described is the mechanism. [PRIMARY]
- For the client: the 6 day package is named "Fresh & Cruisers". If that is a pairing of fresh powder days with groomed days, that is a naming-based mechanism [fact needed: confirm what "Cruisers" means]. The 3 day trip is "Ski and Snowshoe". The multi-sport trip is "Multi-Sport Explorer". Names are free mechanism copy.

**Big idea**
- Idea: one concept that can generate many ads. Ogilvy and Bernbach both used the term. A test for a big idea: can it be written as a headline, a script and a post without changing meaning?
- Real example: Avis "We try harder". The tagline ran for about fifty years [SECONDARY: https://www.crazyads.org/campaigns/avis-were-number-two via search summary; VERIFY]. It generated ads like "Avis can't afford dirty ashtrays" [Slate].
- Mapping: define the big idea once per campaign (one sentence) and test every ad against it.

**Offer construction**
- Idea: the offer is price, what is included, and the terms. Kennedy's "Godfather's offer"; Hormozi's equation; Dry's Sky Bet teardown (low friction, life integration, social fit, big prize, perceived achievability, free) [SECONDARY and PRIMARY, see 2C and 2E].
- Hopkins adds two rules: offer service, and limit the offer to a class of people (veterans, executives) since "those who are entitled to any seeming advantage will go a long way not to lose that advantage" (chapter 6) [PRIMARY].
- For the client: the "class" can be a level (beginner or advanced, which the two day tours already have), a date (Valentine's weekend, 12 to 14 Feb 2027), or a group (couples). Do not invent discounts. Prices were confirmed by Sameer on 2026-10-06 and the hub page is the source of truth. Two tour pages show stale prices (3-day Ski and Snowshoe page says NOK 13,462 against hub NOK 17,451, and 3-Day Multi-Sport page says NOK 12,749 against hub NOK 16,527) [PRIMARY: tours.json]. Always use the hub price.

**Risk reversal**
- Idea: take the buyer's risk onto you. Hopkins documents it: the electric motor maker who offered "a motor for one week's use... without cost or obligation", after which "about nine in ten of the trials led to sales" (chapter 3), and the horse parable (chapter 6) in which the seller who said "try for a week, then pay" beat the one who offered a refund [PRIMARY].
- Hormozi's four guarantee types: unconditional, conditional, anti-guarantee, implied [SECONDARY: https://www.gregfaxon.com/blog/100m-offers-summary].
- For the client: only claim what policy says. Weather, avalanche conditions, snow cover and cancellation terms are real objections for a ski trip [fact needed: client's actual cancellation and weather policy]. If a policy exists, that is a headline: it is the most specific reassurance for a NOK 42,126 purchase.
- Fails: a guarantee that the client cannot or will not honour. Never imply one.

**Price framing**
- Anchoring and decoy: Ariely's Economist experiment. With three subscription options (web $59, print $125, print and web $125), 16 of 100 students picked web only and 84 picked the combo. Without the print-only decoy, 68 picked web only and 32 the combo [SECONDARY: https://en.wikipedia.org/wiki/Decoy_effect and others; small classroom sample, field replication is mixed, VERIFY]. The relevant use: show the 3 day, 6 day and 9 day products side by side so the 6 day looks reasonable next to the 9 day.
- Charm endings: Anderson and Simester ran three field experiments and found a $9 ending increased demand in all three, with a stronger effect on new items [PRIMARY abstract: https://www.kellogg.northwestern.edu/academics-research/research/detail/2003/effects-of-9-price-endings-on-retail-sales-evidence/ ; no percentage on that page, so I give none]. The client's prices end in 8, 1, 6 and 7 (1,948; 41,181; 28,896; 17,451; 16,527; 42,126). Do not round or "fix" them.
- Per day framing: 42,126 divided by 9 is 4,680.67, so "about NOK 4,681 a day" is a true statement [calculated]. Use only if inclusions justify it. Per-day framing for the day tour makes no sense.
- Sutherland: perceived value and how a price is presented matter as much as the number [SECONDARY, see 2D].
- Hopkins: do not cheapen with free. "It is hard to pay for an article which has once been free." [PRIMARY]

**How adwright should use this section.** These are the nine things the skill should check on every draft: one idea, a reason, a specific number, a mechanism if the market is crowded, a link to the campaign's big idea, a clean offer, a risk reducer if there is a real one, a price shown with the right frame, and a plain next step. Ask the user for missing facts instead of inventing them. In particular, ask for the cancellation and weather policy once per client and store it.

### 3C. CTA writing

I found little hard evidence on CTA wording. What I have is craft doctrine from the sources and platform behaviour:

- Hopkins: "The best ads ask no one to buy" [PRIMARY, chapter 3]. A modern feed ad has a button, so the copy does not need "Buy now". Use the line near the button to remove one doubt.
- Sugarman: the whole copy exists to get the reader to the order [SECONDARY, 2C].
- Kennedy: one clear next step [SECONDARY, 2C].
- Third party guidance for X: put a clear CTA in the ad [SECONDARY: https://www.jeffbullas.com/thread/what-are-the-best-practices-when-advertising-on-x/ ; VERIFY].

Working rules for adwright (these are craft heuristics, not tested facts):
1. One action per ad.
2. The action names the next step, not the purchase: "See dates", "See the route", "Pick a date".
3. Put the reason next to the button: "Two departures only" (true for the 6 day package).
4. No fake urgency words ("Hurry", "Last chance") unless true and dated.
5. Test the verb. Meta's button list limits the options anyway.

**How adwright should use this.** Generate three CTA lines per ad (low, medium, high commitment) and recommend one. Mark them as test candidates, not proven winners.

---

## 4. Hook typologies

A hook is the first thing the reader meets: the headline on the image, the first line of the primary text, the first three seconds of a Reel, or the first line of a post. These categories come from practitioner guides [SECONDARY: https://www.opus.pro/blog/instagram-reels-hook-formulas and https://www.heyorca.com/blog/the-best-social-media-hooks-for-2026 , taxonomy from vendor blogs, no single standard]. I mapped each to a documented classic, and to the client. Client lines are **[illustrative]**, built only from tours.json facts, and each was length checked in code.

| Type | Mechanism | Documented real example | Static (illustrative) | Reel hook (illustrative) | X (illustrative) |
|---|---|---|---|---|---|
| Direct benefit | States what the reader gets | Hopkins on soap: "It floats" might prove interesting (his own hypothetical in chapter 5, not a documented ad) | "Every Saturday and Sunday, Jan to Apr: guided backcountry skiing. NOK 1,948." (76 characters) | On screen: "Backcountry skiing. Any weekend. NOK 1,948." | "Backcountry ski day in Norway. Every weekend, Jan to Apr. NOK 1,948." |
| Specificity | An exact number that proves effort | Lemon: 3,389 inspectors, 189 check points, 1 in 50 rejected; Hopkins: 78-second shave | "Five departures. Nine days. 30 Jan to 18 Apr 2027." (50 characters) | On screen counter: "9 days. 5 departures." | "9 day trip: 5 departures between 30 Jan and 18 Apr 2027. NOK 42,126." |
| Curiosity | Opens a gap the reader needs to close | Caples piano ad; "Do You Make These Mistakes in English?" (Sherwin Cody ad by Max Sackheim, ran for roughly 40 to 45 years per WARC and other pages; VERIFY) | "Fresh days. Cruiser days. Six days in Norway. NOK 28,896." (57 characters, needs [fact needed: meaning of Cruisers]) | "Two kinds of ski days. One trip." | "The 6 day package has two kinds of ski days. Here is the split." (only if the follow-up delivers) |
| Contrarian | Opposes common advice | Patagonia "Don't Buy This Jacket", NYT, 25 Nov 2011 (Black Friday). Cost about $57,000, "$40 million to $50 million of free publicity" per then CEO Casey Sheahan, quoted by Gelles. The widely repeated "sales rose 30%" claim is not backed in the pages I read [VERIFY]. | "Skip the lift queue. Climb your own line." (41 characters, [fact needed]: day tours climb) | On screen: "You do not need a lift pass for this." [fact needed] | "Guided ski day in Norway, no lift queue. NOK 1,948." (51 characters) [fact needed] |
| Story | A person, a turn, a payoff | Caples piano ad (1926) | "You booked the flights. Now book the mountain." (46 characters) | "Last winter I skied lifts only. This winter..." (needs a real guest, never invented) | "A guest told us..." only with a real, permitted quote |
| Proof | Visible evidence | Rolls-Royce electric clock; Lemon | A real photo of a real group with the date | Real footage, not stock, in the first second | Quote, number, link |
| Question | Asks what the reader is already asking | Sherwin Cody "Do You Make These Mistakes in English?" | "Never skied backcountry? Start with one day. NOK 1,948." (55 characters) | "Never skied backcountry?" | "Never skied backcountry? There is a beginner day tour every weekend, Jan to Apr." |
| Pattern interrupt | Breaks the expected shape of an ad | REI #OptOutside, 2015: closed all 143 stores on Black Friday; more than 1.4 million people and 170 organisations joined [SECONDARY: https://www.rei.com/blog/social/the-history-of-opt-outside via search snippet] | A plain screenshot, a handwritten note, an unexpected format | Start mid-action, or with the end result | A post that is only a date list, formatted like a boarding pass |

**Notes on the table**

- Every "illustrative" line obeys the client rules: no dashes, no emojis, short sentences. Check with the skill's linter before shipping any of them.
- Question hooks can slip into the "you" territory that Meta restricts when they imply a personal attribute. "Never skied backcountry?" is about an activity, not a trait, but check the policy [VERIFY].
- Avoid the "it is not X, it is Y" contrast frame in hooks. It is overused in AI text and the client dislikes it.
- Pattern interrupt is the hardest for a text-only skill to deliver. Often the interrupt is visual, and adwright should suggest it to the designer, not fake it in copy.

**How adwright should use this section.** For each brief produce at least one headline per hook type that fits the awareness level (section 8), and label each with its type so the user can see what is being tested. That also fits Meta's creative diversity guidance: the system favours different concepts over small edits [SECONDARY: https://www.jonloomer.com/meta-andromeda/ and vendor posts; Meta's own statement not opened; VERIFY]. Make the variants differ in hook type and angle, not in synonyms.

---

## 5. How professionals edit

Most of what follows is working doctrine from the sources. Very little of it has been tested in controlled studies. I say which parts have evidence.

**5.1 Write many, pick few**
- Hopkins (primary): the writer of the chapter "spends far more time on headlines than on writing. He often spends hours on a single headline. Often scores of headlines are discarded before the right one is selected." [PRIMARY: chapter 5].
- Ogilvy: "I never write fewer than sixteen headlines for a single advertisement" [SECONDARY: quote page found via search, source book not opened; VERIFY]. Another summary says he wrote 26 for Rolls-Royce [SECONDARY].
- The numbers 16, 26, 50 and 100 are conventions. I found no study that says what count is best. What the sources agree on is the direction: a large pool, then a cut.
- adwright rule: draft 30 headlines per angle, tag each with a hook type, then cut by clusters. Aim for different types in the final five, not five versions of one idea.

**5.2 Cut with rules, not feelings**
Orwell's six rules, in his words [PRIMARY: Orwell Foundation]:
1. "Never use a metaphor, simile or other figure of speech which you are used to seeing in print."
2. "Never use a long word where a short one will do."
3. "If it is possible to cut a word out, always cut it out."
4. "Never use the passive where you can use the active."
5. "Never use a foreign phrase, a scientific word or a jargon word if you can think of an everyday English equivalent."
6. "Break any of these rules sooner than say anything outright barbarous."

Dry's matching lines: "Write with your eraser", "Kill adverbs. Kill adjectives", "More periods, fewer commas", and "Avoid landing page words" [PRIMARY: https://marketingexamples.com/copywriting/tips]. Caples: a valid argument in blunt language beats a weaker one beautifully put [SECONDARY, 2A].

**5.3 Kill adjectives, keep facts**
Hopkins gives the reason: "superlatives of that sort are usually damaging. They suggest looseness of expression, a tendency to exaggerate" [PRIMARY: chapter 7]. Dry softens it: "Adjectives are okay. Just ideas don't start with them." [PRIMARY]. Edit pass: underline every adjective, then ask "what is the number, name, date or object behind it?" Replace "epic backcountry adventure" with the day, the price, the group level.

**5.4 Read it aloud**
I did not find a primary source for reading copy aloud as a method. It is craft convention, and it fits Dry's "write how you talk" and Abbott's "plain, simple and familiar" [SECONDARY]. For a machine, the equivalent is to check sentence length variety and to flag three beats of equal length in a row. The client's own editorial persona (repo file `adwright/agents/editorial-director.md`) lists tricolons and uniform rhythm as AI tells. Note the conflict: Dry praises tricolon ("One Scoop. Once a day. Every day."). For adwright, a tricolon is allowed only when the content really has three items.

**5.5 Walk away**
Abbott: "The best thing for me when tired is to do something else" [SECONDARY: https://briefercopy.com/blog/david-abbott/]. For a pipeline, the equivalent is a fresh reader: run the review in a separate agent that sees only the draft and the brief.

**5.6 Test, with the right unit**
- Hopkins: keyed coupons so each headline's returns are known. "The identical ad run with various headlines differs tremendously in its returns." [PRIMARY]. Caples built a whole method on this.
- In Meta, the unit worth testing is the concept (hook type and angle), not the adjective. Vendor guidance and Meta commentary say the delivery system favours distinct concepts [SECONDARY, VERIFY]. A test of "amazing" against "incredible" teaches nothing.
- The metrics that exist: Meta shows 3-second video plays and impressions. Hook rate is a ratio you calculate from them (3-second plays divided by impressions). Vendor blogs give 30 to 40% as average for Reels and call above 40% good [SECONDARY: https://reloop.so/blog/article/hook-rate/ and others; VERIFY: these are vendor figures, not Meta benchmarks].
- Small budgets cannot detect small differences. A NOK 1,948 product at low spend will not reach statistical significance for a tweak. Test big contrasts.

**5.7 Fact pass (the one amateurs skip)**
Every number, date and price gets checked against source. The client repo has `campaigns/ski-meta-ads/verify_tours.py`, which compares `tours.json` with the live hub page. Run it before any ad goes out. Known trap: two tour pages show stale prices (see 3B).

**5.8 The promise test**
Dry: a good title is one where the reader "would feel cheated if the content breaks the promise" [PRIMARY: https://marketingexamples.com/copywriting/promise]. Use on every curiosity hook: what happens on the landing page when the curiosity is not paid off?

**5.9 The adwright edit loop (proposed)**
1. Draft 30 headlines, 8 hook types.
2. Delete any with a banned word, a dash, an emoji, a "not X, it is Y" frame, or an unverified fact.
3. Score the rest on the 4Us plus Dry's three tests (section 6).
4. Pick five that differ in type. Rewrite each with Orwell rules 2, 3, 4.
5. Count characters and words in code. Re-check every number against `tours.json`.
6. Fresh-reader review.
7. Ship with labels (hook type, awareness level, which fact is the proof).

**How adwright should use this.** Encode steps 1 to 7 as the standard pipeline and keep the lint step mechanical. Resist adding more steps. The research supports volume and cutting, and supports testing, and supports checking facts. It does not support rituals.

---

## 6. Headline formulas and a scorecard

**Caples' formula families** (names only; the page I could open did not include his example headlines) [SECONDARY: https://larslofgren.com/john-caples-headline-formulas/]:
- Keyword openers: How to, How, Why, Which, Who else, Wanted, This, Because, If, Advice.
- Benefit headlines: testimonial, test or challenge, information value, story, delay warning, direct address, specific audience, question, facts and figures.
- News headlines: Introducing, Announcing, New, Now, At last, date inclusion.
- Price headlines: price feature, reduced price, special offer, payment plan, free offer.
- One to three word headlines.

**Ogilvy's list** (percentages from a teaching summary, VERIFY): include a benefit, include news, include the brand name, name the target group, be specific, avoid puns [SECONDARY: https://www.shortform.com/blog/writing-headlines/].

**4Us** [SECONDARY, 3A]: Useful, Urgent, Unique, Ultra-specific.

**Dry's three questions** [SECONDARY: https://www.upgrow.io/harry-dry-copywriting-3-rules/]: can you visualise it, can you falsify it, can nobody else say it.

**Proposed adwright scorecard (my synthesis, not a published standard).** Score each headline 0 to 2 per line. Keep anything at 9 or more out of 14.

| # | Test | Source |
|---|---|---|
| 1 | Names or implies the person (level, group, moment) | Hopkins |
| 2 | Contains one exact number, date or named thing | Hopkins, Dry |
| 3 | You can picture it | Dry |
| 4 | Only this brand could say it | Dry, Trott |
| 5 | Carries a benefit, news or a reason | Caples, Ogilvy |
| 6 | Real urgency, or none. Zero for fake urgency | 4Us, Kennedy |
| 7 | Fits 3 to 20 words and passes the client style rules | Client brief |

Treat the cutoff as a starting point and tune it on real results.

**Example scoring [illustrative]** for "Every Saturday and Sunday, Jan to Apr: guided backcountry skiing. NOK 1,948." Hail: 1 (names the activity, not the level). Number: 2. Picture: 2. Only us: 1. Benefit: 1. Urgency: 1 (recurring dates, not scarce). Fit: 2. Total 10 of 14. Rewrite to hail the level ("Beginner backcountry skiing...") and it moves to 11.

**How adwright should use this.** Show the user which formula family each headline comes from (for example "Why", "Question", "Price"). That makes the output teachable, and it differs from the black box feel of AI ad tools.

---

## 7. Short-form craft for 2025 and 2026 social ads

Evidence here is thin and mostly from vendors. I mark which parts are platform statements and which are craft doctrine.

### 7.1 What a scroll-stopping first line does

It does four jobs in the first 40 or so characters:
1. Hails the reader (Hopkins: pick out "people you can interest").
2. Gives a reason to read the next line (Sugarman: the first sentence exists to get the second read).
3. Carries a specific (Hopkins ch. 7).
4. Survives truncation, on both the image and the text.

Platform facts: Meta says up to 47% of a video campaign's value arrived in the first three seconds (study with Nielsen, undated) [PRIMARY: facebook.com/business/news/updated-features-for-video-ads]. A practitioner page quotes Meta's Reels hub as saying the strongest Reels ads land the hook within 1.5 seconds [SECONDARY: https://reloop.so/blog/article/hook-rate/ ; VERIFY, could not find the Meta source]. A widely repeated 2016 claim says people spend about 1.7 seconds on a mobile feed item [VERIFY: could not trace to its source]. Lumen eye tracking says only about 30% of viewable ads are actually looked at [VERIFY: search snippet only]. Take the direction: the first line has about one second.

### 7.2 Line breaks and rhythm in mobile feeds

- Doctrine from Dry: "More periods, fewer commas", write scannable copy, think slippery slide [PRIMARY].
- Sugarman: vary sentence length, use simple vocabulary, and give the copy rhythm [SECONDARY: creative-copywriter.net].
- One thought per line. A line should read as a complete beat. Put the number alone on a line when the number is the point.
- Line length: a UX source suggests 30 to 50 characters per line on a phone in portrait [SECONDARY: https://www.uxpin.com/studio/blog/optimal-line-length-for-readability/ ; VERIFY, general readability not ad specific]. Treat as a rule of thumb for on-image text.
- I found no controlled study of line breaks in Meta primary text. Test them. Meta shows line breaks as written, but the "See more" cutoff is by layout, so a hard break can push the hook off the visible area [VERIFY on a real device].
- Avoid the machine drumbeat: three sentences of equal length, repeated triplets, stacked colon reveals. The repo's reviewer persona lists these as tells.
- Emojis are banned by the client. So are dashes. A line like "Saturday. Norway. 1,948." can carry rhythm with periods alone.

### 7.3 Writing for sound-off viewing

- Meta (primary): "captioned video ads increase video view time by an average of 12%" (internal tests), and "41% of videos were basically meaningless without sound" in one Facebook video ad study [PRIMARY: facebook.com/business/news/updated-features-for-video-ads ; undated, studies not named].
- The "85% of Facebook video is watched without sound" figure comes from a Digiday story of 17 May 2016 quoting publishers (LittleThings and Mic said 85% of their views were silent, PopSugar said 50 to 80%). It is a publisher claim from 2016 for Facebook video, not a Meta platform statistic for ads in 2026 [SECONDARY: https://www.niemanlab.org/reading/publishers-say-85-percent-of-facebook-video-is-watched-without-sound/ and the Digiday original via search]. Many 2025 and 2026 blogs repeat "80% sound off" and attribute it to Meta [VERIFY: I could not find a Meta source]. Do not use these numbers in public copy. Use the design rule instead.
- Vendor claim: roughly 60% of Reels viewers have sound on [VERIFY].
- Design rule used by Meta guidance: design for sound off, then add sound as a bonus [SECONDARY: vendor pages; the phrase "design for sound off, delight with sound on" appears in several].
- Craft rules for adwright: (1) the offer and the number are in on-screen text; (2) burned-in captions in the same font as the brand; (3) the hook is readable in the first half second; (4) never rely on a voiceover line for the price or date; (5) keep text out of the Stories and Reels safe zone. A search snippet from Meta's help page gives about 14% from the top, 35% from the bottom and 6% on each side [VERIFY: the page fetch returned only the title].

### 7.4 Writing for people who skim

- Hopkins, in 1923: "They skip three-fourths of the reading matter which they pay to get." [PRIMARY]. Nothing has changed except the speed.
- Make the ad work at three depths: image plus headline (2 seconds), first line of primary text (5 seconds), the full text (the 1% who tap See more; "about 1% of users tap See more" is a vendor claim, VERIFY).
- Put the checkable facts where a skimmer's eye lands: a number, a date, a price, each on its own line.
- Reading level: vendors recommend grade 5 to 7 and short sentences of 8 to 12 words, and one study found posts readable at grade 5 or 6 earned more likes [SECONDARY: https://www.researchgate.net/publication/328295826_How_Readability_Shapes_Social_Media_Engagement ; VERIFY, platform and period unknown]. Another study warns readability formulas are unreliable for short-form text. Use plain words and test the output with a human, not a formula alone.

### 7.5 What changed in Meta delivery

Several 2025 and 2026 guides say Meta's retrieval system ("Andromeda") now rewards different creative concepts and treats near-duplicates as one [SECONDARY: https://www.dentsu.com/ae/en/our-latest-thinking/meta-andromeda-strategy , https://www.jonloomer.com/meta-andromeda/ ; the second returned 403 to my fetch, so I used search snippets; VERIFY against Meta's own statements]. Vendor posts suggest numbers (8 to 12 distinct concepts per campaign, similarity scores) that I could not trace to Meta [VERIFY]. The safe direction for the skill: output several different concepts, each in the three formats, instead of 20 rewrites of one line.

### 7.6 X posts (280 characters)

- X's own guidance was not retrievable. Third party sources say short copy performs best and the first 40 or so characters are what the timeline shows [VERIFY].
- Craft: the post has to stand without the image. Put the fact in line one. Use blank lines between beats. Put the link last. Long links count toward the limit in a fixed way on X (a shortened-link length) [VERIFY: current rule].
- A post is not a headline plus caption. If the image already shows the product, the text adds the number and the reason.
- Use a plain, human voice (Halbert's A-pile idea): a post that reads as a person talking tends to survive better than one that reads as a brand shouting. This is doctrine, not data.

**How adwright should use this.** Run the four first-line jobs (7.1) as a checklist on every hook, with a sound-off, image-hidden read as the last check, and make the skill state which job each hook performs. Avoid claiming platform statistics in the user-facing text. The only numbers adwright should publish are the client's own prices and dates.

---

## 8. The copywriter's decision tree

### 8.1 The inputs

1. **Awareness level** of the audience for this ad: unaware, problem aware, solution aware, product aware, most aware. Inference rule of thumb: cold prospecting audiences are mostly unaware or problem aware; people who visited the site are product aware; people who started a booking or are on the email list are most aware. This is my working rule, not a Schwartz rule.
2. **Sophistication stage** of the market: 1 to 5. Default for guided backcountry day tours: stage 3 [illustrative guess]. Default for multi-day ski trips: stage 4 [illustrative guess]. Replace the guess with a look at what competitors run.
3. **Fact bank**: price, dates, inclusions, policies, proof. Anything missing becomes a question to the client.

### 8.2 The tree in words

```
START: what does the reader already know?

Unaware  -> Lead with an identity, a scene or a surprise. Do not name the product first.
            Frameworks: BAB, story.   Hooks: pattern interrupt, story, identification.
            Format notes: Reel and static carry the weight. X needs a standalone claim.

Problem aware -> Name the situation in their words.
            Frameworks: PAS (light), BAB.   Hooks: question, direct benefit.
            Use Wiebe's method: take the phrase from a review.

Solution aware -> They know skiing tours exist. Show your mechanism.
            Frameworks: QUEST (qualify first), FAB (publish the B first).
            Hooks: specificity, curiosity (only if paid off), contrarian.

Product aware -> They know you. Remove the last doubt.
            Frameworks: proof stack (Bencivenga), risk reversal, 4Ps (promise and proof).
            Hooks: proof, specificity, honest concession (Bernbach).

Most aware -> Give the offer, the date and the price.
            Frameworks: offer first, 4Ps push, scarcity only if true.
            Hooks: direct benefit, specificity.

THEN adjust for the market's sophistication:

Stage 1  -> say the claim plainly. One number.
Stage 2  -> enlarge the claim with a larger or tighter number.
Stage 3  -> add a mechanism: the how, the named structure of the trip.
Stage 4  -> improve or sharpen the mechanism, add proof, name the difference from the usual.
Stage 5  -> identity and belonging: who goes on this trip, what it says about them.

THEN run the building blocks (section 3B): one idea, a reason, a specific, a mechanism if stage 3 or above,
the big idea link, a clean offer, a risk reducer if real, price framing, a plain next step.

THEN score (section 6), edit (section 5), count and fact check, and label.
```

### 8.3 The tree as a table

| Awareness | Framework | Preferred hook types | Image headline pattern | Reel hook pattern | X post pattern |
|---|---|---|---|---|---|
| Unaware | BAB, story | Pattern interrupt, story | Scene or identity, price last | Start mid-scene, text overlay | One vivid scene, then the number |
| Problem aware | PAS (light), BAB | Question, direct benefit | "Never X? Start with Y." | Name the situation in 3 seconds | A question, then a single fact |
| Solution aware | QUEST, FAB | Specificity, mechanism, curiosity | The named mechanism plus a number | Show the mechanism visually | Line one mechanism, line two proof |
| Product aware | Proof stack, risk reversal | Proof, honest concession | Proof as headline (date, count, policy) | Real footage and a real number | Proof line, link |
| Most aware | Offer first, 4Ps push | Direct benefit, specificity | Date plus price | Deal on screen at 0.5 seconds | Date list plus link |

### 8.4 Worked cases for Outdoor Norway

All lines are **[illustrative]**. They use facts from `tours.json`. Items that need the client are marked **[fact needed]**. Character counts checked in code.

**Case A. Cold audience, day tour (problem aware, stage 3). Framework: BAB. Hooks: identification, question.**
- Image headline: "Monday: inbox. Saturday: a Norwegian mountain. NOK 1,948." (57 characters, 8 words)
- Primary text: "Never been backcountry skiing? There is a beginner day tour every weekend, Jan to Apr. NOK 1,948." (97 characters)
- X: "Never skied backcountry?" / "There is a beginner day tour every Saturday and Sunday, January to April." / "NOK 1,948." / "outdoornorway.com/ski" (134 characters, blank lines between)
- Why: hails the beginner (Hopkins), names the exact schedule and price (specificity), and keeps the reason in the schedule. The fact "guided" belongs here if the client confirms the tour page says so [fact needed].

**Case B. Solution aware, 6 day package (stage 3 to 4). Framework: mechanism first (QUEST step one, then FAB). Hooks: curiosity (paid off), specificity.**
- Image headline: "Fresh days. Cruiser days. Six days in Norway. NOK 28,896." (57 characters) [fact needed: what "Fresh" and "Cruisers" mean in this tour. Do not publish until confirmed]
- Primary text: "Two departures only: 29 Jan and 4 Feb 2027. The 6 day Fresh & Cruisers package. NOK 28,896." (91 characters). "Two departures only" is true in the data: two start dates are listed.
- X: "6 day Fresh & Cruisers ski package, Norway." / "Two departures: 29 Jan and 4 Feb 2027." / "NOK 28,896." / link (119 characters)

**Case C. Product aware, 9 day trip (stage 4). Framework: proof and risk reversal. Hooks: proof, specificity, honest concession.**
- Image headline: "Nine days. Five departures. 30 Jan to 18 Apr 2027." (50 characters)
- Primary text: "9 days of skiing in Norway. 5 departures, 30 Jan to 18 Apr 2027. NOK 42,126. Dates on the page." (95 characters)
- Add, only with the client's real policy: one line of risk reduction about weather, snow or cancellation [fact needed]. This is the highest value fact the client can give adwright for this ad.
- X: "9 day ski trip in Norway." / "5 departures between 30 Jan and 18 Apr 2027." / "NOK 42,126." / link (107 characters)

**Case D. Most aware, Valentine's departure (3 day Multi-Sport Explorer, stage 3). Framework: offer first. Hooks: direct benefit, specificity.**
- Image headline: "Valentine's Day, 12 to 14 Feb. Three winter days in Norway. NOK 16,527." (71 characters, 13 words)
- Primary text: "Valentine's weekend, 12 to 14 Feb 2027: three days of winter sports in Norway. NOK 16,527." (90 characters) [fact needed: which sports and whether it suits couples]
- X: "Valentine's weekend, 12 to 14 Feb 2027." / "Three winter days in Norway." / "NOK 16,527." / link (115 characters)
- Note: the page text says "12 - 14 Feb (Valentine's Day)". The data labels this the Valentine's Day departure. 14 Feb 2027 falls on a Sunday.

**Self-check on these samples.** They contain no dashes, emojis or shouting. They have a deliberate drumbeat problem: four of the X posts use the same shape (three short beats and a link). That is fine for a data-led offer and would be a tell for editorial content. The skill should vary the shape between ads in the same campaign.

**How adwright should use this.** Make the awareness and sophistication questions the first step, with defaults. Output a small table per ad: awareness, stage, framework, hook type, proof fact, character count. The user can then see the reasoning and override it. This visible reasoning is a strong differentiator for a GitHub skill, because most AI ad tools hide theirs.

---

## 9. Verification log and open items

### 9.1 Claims verified from a primary source I opened

Hopkins' quotes on headlines, specificity, offers, samples and risk reversal (archive.org text). The IPA slides on rational versus emotional decay, and "fame quadruples efficiency" (1.4 against 0.3). Meta's 47% and 74% first-seconds figures, caption lift of 12% and the 41% sound-off finding (undated page), plus the feed spec of 50 to 150 characters for primary text and 27 for headline. Orwell's six rules. The Copyhackers Beachway result and thank-you page question. Client prices and departures from `tours.json`.

### 9.2 Claims that are secondary only (do not quote as fact without checking)

- All figures in Ogilvy's headline list (400%, 75%, 22%, 28%), the "sixteen headlines", the 26 Rolls-Royce headlines, the 719 and 1400 word counts.
- Halbert: 600 million mailings, 20,000 orders per day, sale for $75 million.
- Patagonia: "sales rose 30%". The $57,000 cost and "$40 million to $50 million of free publicity" are quoted from the then CEO in Gelles' piece, and are the company's own figures.
- Avis profit swing and share figures (Slate; the cause is not isolated).
- Lemon ad full text (transcription; verify against a scan).
- Schlitz and "fifth place to tied first".
- Eurostar figures in the Sutherland talk (retellings vary).
- Hormozi equation and guarantee types (summaries, not the book).
- Sherwin Cody ad longevity (40 to 45 years across sources).
- Dry's Sky Bet numbers (£2.60 CAC, about £200 benchmark) and the "Ugly Ads" $50K.
- Hook rate benchmarks, "1% tap See more", "1.7 seconds", "30% of viewable ads are viewed", "60% of Reels viewers use sound", safe zone percentages.
- Every X-specific number.

### 9.3 Things that look like facts and are not

- "85% of Facebook video is watched without sound": a 2016 publisher claim in Digiday, not a Meta statistic about ads today.
- The "125 characters" truncation: layout dependent, not published by Meta as a limit.
- "AIDA was invented by Lewis in 1898": contested. The 1898 formula in *Printers' Ink* was anonymous.
- "Dan Kennedy invented PAS": the sources only show he praised it.
- "Because" always works: in Langer's study the placebo reason failed on the bigger request (about 24% against 42% for a real reason).

### 9.4 Open questions for the client or the team

1. What do the tour pages actually include (guide, gear, transport, group size)? Needed for inclusions, mechanism and Hormozi levers.
2. What is the real weather and cancellation policy? Needed for risk reversal.
3. What does "Fresh & Cruisers" mean exactly?
4. Which competitor ads should be read in the Meta Ad Library to set the sophistication stage?
5. Are there real guest reviews that can be quoted, with permission?
6. Does the client want per-day price framing on the 9 day trip?
