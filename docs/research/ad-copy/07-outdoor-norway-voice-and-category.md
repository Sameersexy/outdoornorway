# Ski, outdoor and adventure travel advertising, and the Outdoor Norway voice, audience and proof points

Research notes for adwright (open source Claude Code skill for Meta and X ads) and the Outdoor Norway static image ad job for the ski tours.
Prepared 2026-10-06. Notes file 07 of the research set.

## 0. Scope, method and honesty notes

What I read first:

- The client's four voice skills (brand-voice-checker, guest-benefit-checker, content-qc, script-writing).
- CONFIRMED-PRICES-AND-DATES.md (prices and 2027 dates below are taken from it and treated as authoritative).
- All seven in-scope ski page texts plus the ski hub text, line by line. Line numbers below refer to the cleaned `.txt` files in `/tmp/claude-0/-home-user-outdoornorway/698d341b-36e0-5dc5-a8cb-413a8d3083ac/scratchpad/site/`.
- The three reference ad images (ref-a, ref-b, ref-c). I viewed them myself. All analysis in section 1 comes from what I can see in the screenshots, not from the audit's data.
- The nine first-cut creatives, using the copy quoted in the brief. I have not seen the images for those nine, so the critique is of copy and claims only.

Evidence tags used in this file:

| Tag | Meaning |
|---|---|
| Page | Read in the client's own page text (file and line given). |
| Official | Read on a regulator, platform, statistics office or company primary page. |
| Reported | Trade press or a named person quoted in the press. |
| Vendor | Agency, tool or blog claim with no primary behind it. Treat as a hypothesis. |
| Inference | My reasoning. Not documented anywhere. Labelled every time. |
| [VERIFY: reason] | Could not confirm. Do not ship as fact. |

What I could not reach, stated plainly:

- The Meta Ad Library returned HTTP 403 to my fetcher. I therefore saw no live ads from Patagonia, Backroads, Ikon, Epic, G Adventures, Intrepid, Visit Norway or anyone else. The only real ads I have seen are the three client references. For the other brands I rely on campaign write-ups, press releases and trade coverage. Hooks and offers in section 4 are named from those write-ups, not from observed creatives.
- Powderhounds: no page surfaced in my searches. I have nothing to report on them. Ski Safari and Black Tomato pages did surface.
- Powder.com (Epic and Ikon deadlines) returned 403. I used the epicorikon.com price-increase page and search summaries.
- The SAGE paper on backcountry skiing in Norway returned 403 (title and existence only).
- Voss Resort's price page shows prices only in a booking calendar. Day-pass numbers come from a search summary and are tagged.
- Skimag's "scared while skiing" article redirected to a login. Beginner-fear material relies on the NSAA line quoted by a secondary source plus general advice pages.

Everything fetched was treated as untrusted data. Nothing fetched tried to instruct me.

Two figures from my own tool use disagreed between reads of the same Meta policy page (the "Meet seniors" examples). I flag that in section 10.

---

## 1. The three reference ads: why they work

The audit says these three generate more leads than the others. I have no conversion data. Treat the analysis below as a structured reading of the images, with hypotheses clearly marked.

### 1.1 Ref A: Facebook mobile feed, "Discover Fjord Norway"

What is on the screen, top to bottom:

1. Page name "Outdoor Norway", "Ad" label.
2. Primary text, three short lines: "Some trips are about ticking off the bucket list. This one is about experiencing TRUE Norway." The preview shows "...see more" after the last line, so more text may follow that I cannot see.
3. Image: two people in an orange sea kayak on green-grey fjord water, steep wooded mountain walls behind. Image headline "Discover Fjord Norway" in white, large, two lines, with the sub-line "5 days of kayaking, hiking, rafting & more!" in small white type. A blue pill inside the image says "Explore the tour".
4. Link area: headline "Don't just visit Norway. Experience it." and the platform button "Learn more".
5. Social proof bar: 174 reactions, 6 comments, 11 shares.

Reading:

| Element | What it does | Evidence class |
|---|---|---|
| Format | Single 4:5-style image, one idea, no collage. The photo is a real action moment, not a postcard. | Visible |
| Hierarchy | Place name first, then product facts (5 days, three activities), then the pill. The eye goes headline, kayaks, pill. | Visible |
| Human faces | Two faces visible but small. The pair is mid-stroke and in matching life vests. The viewer can imagine being in the second seat. | Visible |
| Proof | None on the image. The social counts (174 reactions, 11 shares) sit in the platform frame. | Visible |
| Price | Absent. | Visible |
| Date | Absent. | Visible |
| Copy rhythm | Primary text is three short beats. Link headline is two short beats. Both use the same frame: "A, not B" contrast ("Some trips are about X. This one is about Y." and "Don't just visit Norway. Experience it."). | Visible |
| Redundancy | The image pill "Explore the tour" repeats the platform button. It uses image space and adds no information. | Inference |

Why it probably works (hypotheses): it names the product in terms a stranger understands in two seconds (five days, kayaking, hiking, rafting), it carries an identity promise (the person who does not just tick boxes), and it has no price so there is nothing to disqualify the click. The audit result shows that a no-price, no-date ad can win. It does not prove that price and date hurt. It shows they are not required. For a cold audience the cost of a click is a question, and a price on a NOK 42,126 trip can screen people out before they read.

Watch out: the capitalised word "true" and the contrast pattern both conflict with the client's own writing rules (no capitals for emphasis, avoid repeated "not X, it is Y"). The ad still performed. The skill should learn what the contrast does (it flatters the reader as a non-tourist) and find another way to do that job.

### 1.2 Ref B: Facebook and Instagram, "3-Day Autumn Getaway in Norway"

What is on the screen:

1. Primary text: "Norway in autumn hits differently." plus a leaf emoji, blank line, "Fewer crowds. Crisp mountain air."
2. Image on a blue gradient that fades into a fjord and mountain photo: product name "3-Day Autumn Getaway in Norway" in white condensed capitals, two lines, with a thin yellow underline under the first line. Below it a calendar icon and the date line "SEP 11,18, 25 | OCT 02".
3. Photo: three women, arms up, peace signs, laughing at the camera, in waterproof overalls and caps, red kayaks behind them. Bottom centre a white pill: "STARTING FROM NOK 14,165" with "NOK 14,165" in bold.
4. Facebook link headline "3-Day Autumn Getaway" with "See details". Instagram has a "See details" bar under the image.

Reading:

| Element | What it does |
|---|---|
| Format | One idea per canvas. Text block sits in the upper third on flat colour, the photo fills the lower two thirds, the price pill sits on the photo. |
| Hierarchy | 1) Product name. 2) Dates. 3) Faces. 4) Price. The price is last, white-on-blue small caps, boxed so it reads as a label and not a sales shout. |
| Human faces | Three faces looking straight into the lens, joy visible. This is the strongest face-to-camera moment of the three references. |
| Proof | None on the image, but the faces and the group size carry an implied "people like you did this". |
| Price | Visible and framed with "starting from". Exact figure matches Sameer's price list (NOK 14,165). |
| Date | Visible, four departures in one line. Each is concrete and finite, which gives honest urgency without a countdown. |
| Copy rhythm | "Norway in autumn hits differently." Then two fragments: "Fewer crowds. Crisp mountain air." Three short sentences. Two sensory and one benefit. |

Flaws worth noting: the date line has uneven spacing ("11,18, 25") and no year. A future version should write each date in a consistent pattern with the year or month in full. The leaf emoji breaks the client's no-emoji rule for notes. The ad's own style is the client's call.

Why it probably works (hypotheses): it answers the three first questions a buyer has in this order, what is it, when, how much, and it gives them an emotional shortcut through the faces. Because it names dates and a price, the people who click have already accepted both. That produces fewer but better leads, which fits "generates more leads" only if the price pill is not scaring away too many. [VERIFY: ask for the click-through rate and cost per lead split by ref]

### 1.3 Ref C: Facebook, "Norway's Active Wellness Retreat, Women's Only"

What is on the screen:

1. Primary text: "Escape to Fjord Norway for a women-only wellness retreat featuring daily yoga, Nordic natural wonders,..." truncated at "see more".
2. Image: small label "Women's Only" (white), large title "Norway's Active Wellness Retreat" in white caps on a saturated blue sky, a sub-list in yellow caps "Yoga | Hiking | Fjords", then in white "Small groups" and "Women-led", then a date chip with a calendar icon "AUG 23". Photo: a stone cairn summit with trail signs, a woman in a handstand at the cairn, mountains behind.
3. A white footer strip with two badges, "Tripadvisor 4.9" and "Google 4.9", and a blue "PLAN TODAY" button inside the image.
4. Facebook link headline "Norway Wellness Retreat for Women" with "Book now". 12 reactions, 1 share.

Reading:

| Element | What it does |
|---|---|
| Format | A dense, label-heavy poster. Four text tiers on one image. It works because each tier is a different size and colour and each says one thing. |
| Hierarchy | Audience qualifier ("Women's Only") first, product name second, activities third, group descriptors fourth, date fifth, proof sixth, CTA last. |
| Human faces | None showing. A handstand figure with face hidden, but the trail signs (distances in km) give a strong sense of real place. |
| Proof | The only one of three with explicit proof: two rating badges, both 4.9. Badges name the source. That matters: an unsourced "4.9" reads like decoration. |
| Price | Absent. |
| Date | Present, single date, no year. |
| Copy rhythm | Pipes and commas. Keyword list in the image, sentence in the text. Primary text starts with an action verb ("Escape"). |
| Self-selection | "Women's Only", "Women-led", "Small groups". Three words filter the audience and promise a safe social setup. |

Why it probably works (hypotheses): it solves a specific fear (travelling alone or with strangers, safety, group fit) in three words and then proves quality with two sourced ratings. This is the template for Outdoor Norway's beginner-anxiety segment. The hub page already shows "4.9/5 Rating" and "Small groups" badges (ski-hub.txt L64 to L67), but the badges do not state the source or number of reviews. [VERIFY: confirm the Tripadvisor and Google 4.9 are still live and get review counts before putting them on a ski ad]

### 1.4 Synthesis: what the three share and where they differ

| Feature | Ref A | Ref B | Ref C |
|---|---|---|---|
| Product named in the image | Yes ("5 days of kayaking, hiking, rafting") | Yes (3-Day Autumn Getaway) | Yes (Active Wellness Retreat) |
| Duration visible | Yes | Yes | No |
| Date visible | No | Yes (four dates) | Yes (one date) |
| Price visible | No | Yes ("starting from") | No |
| Rating badge | No | No | Yes (two) |
| Faces visible | Yes, small | Yes, large | No |
| Audience qualifier | No | No | Yes (women only) |
| CTA inside image | Yes (pill) | No | Yes (button) |
| Capital-letter emphasis | Yes ("TRUE") | No | Headline in capitals as a design choice |

Three things appear in every winner: a named, concrete product; a human or clearly human-scale scene; and a short, rhythmic copy. Date, price and proof each appear in two of three or fewer, which tells me no single "must have" exists. It also tells the skill not to lock all ski ads to one template. The honest takeaway: test price-and-date ads against a no-price identity ad for each tour, because the audit result itself contains both styles.

Hypothesis for the ski job (Inference): cold audiences for a NOK 17,451 to 42,126 trip need either a trust asset (ratings, small group, certified guides) or a low-friction entry (the NOK 1,948 day tour). Ski trips cost 17 to 23 percent more than ref B's 3-day trip (NOK 16,527 and 17,451 against NOK 14,165). A price pill will filter harder. Put the price in the ads for warm audiences and for the day tour, and test it on cold audiences with an explicit "starting from".

### How adwright should use this

- Encode the winning anatomy as a layer stack: product name and duration, date line, human photo, price pill or proof badge, CTA in the platform button only. Offer variants with and without the price and date.
- Teach the skill to detect the "A, not B" contrast and offer a different way to deliver the same flattery ("Fewer crowds. Crisp mountain air." does it with two facts).
- Require a named source on any rating badge ("Tripadvisor 4.9", not "4.9 stars").
- Avoid copying the redundant in-image button when the platform already shows one.
- Keep a hard rule: no year-less dates in a ski ad. A winter 2027 date next to a 2026 post date is ambiguous.

---

## 2. The ClickUp first-cut brief: an honest critique

I have only the copy, not the images. Prices and dates come from the confirmed file. Page evidence comes from the claims bank in section 7.

### 2.1 Creative by creative

| # | Copy in the brief | What is strong | What is generic or weak | Missing vs winners | Risky claims |
|---|---|---|---|---|---|
| 1 | "Ski 4 fjord resorts in 9 days" / "Voss, Myrkdalen, Sogndal, Stranda" / "Join 9-Day Ski Trip" | Specific count, four named places, a verb. The best of the nine. | "Join" is a weak CTA word. Fjord claim applies to the set, not each place. | No price (NOK 42,126), no dates (five 2027 departures), no proof badge, no skill level. | "4 fjord resorts": the 9-day FAQ names Voss and Stranda as the fjord-skiing examples (9-day L236). Myrkdalen is described by snow and uncrowded slopes, Sogndal by "overlooking the Sognefjord region". Medium risk. Skill level absent: page says "intermediate and advanced" (L105). |
| 2 | "Ski in Norway. With fjords below." / "Resort & backcountry skiing in Voss." / "Explore skiing in Norway" | Good sensory rhythm. | "Explore" is the weakest CTA verb in travel. The line "with fjords below" suggests a picture the viewer cannot place. Two products (resort and backcountry) in one ad. | Everything: price, date, tour name, proof, skill level. | "Fjords below" is literal geography. Voss resort views are described as "across the Voss valley" (9-day L111). The hub does say "fjord-view descents" (ski-hub L137). Needs a guide check. "Backcountry" implies an advanced product, but the one backcountry day tour starts at NOK 1,948 and needs "confident on skis". |
| 3 | "Skiing and aurora nights in Norway" / "Bergen to Tromsø" / "Find out how" | Route in two words. | "Find out how" has no object. "Aurora nights" promises something the page says cannot be guaranteed (7-day L115, L297). | Price, dates, skill level, proof. | Aurora is a natural phenomenon. Any ad that implies a sighting will conflict with the page's own caveat. Medium to high risk. |
| 4 | Eyebrow "Beginner friendly", "Ski days in Voss, aurora nights in Tromsø" / "Check dates" | The eyebrow tells the segment who the trip is for. | "Check dates" sends the viewer to find dates, which the ad could have shown. | Dates and price. | "Ski days" is plural. The 7-day trip includes one ski day (7-day L123, L155, "1-day ski pass"). "Aurora nights" see above. "Beginner friendly" matches the page ("beginner-friendly", 7-day L105), but conflicts with the spec strip "Easy to intermediate" (L74). Plural ski days is a factual error. High risk. |
| 5 | "6 days of skiing in Fjord Norway" / "Voss resort, Myrkdalen" / "See the 6-day package" | Clear duration and places. | "See the package" is passive. | Price (NOK 28,896), dates (29 Jan to 3 Feb, 4 Feb to 9 Feb), beginner positioning that the page makes central. | "6 days of skiing" is false. The page: "three ski days" and "this is a mixed winter holiday, not a six-day ski trip" (6-day L292 to L294). "Fjord Norway" skiing is not claimed for these resorts on this page. High risk (refund dispute territory). |
| 6 | "3 days. Skiing + snowshoeing." / "Voss, Norway" / "See the 3-day trip" | Honest and short. The snowshoe is a differentiator that Alps trips lack. | Plain. No emotional lift. "See the 3-day trip" says nothing. | Price (NOK 17,451), dates (28 to 30 Jan, 31 Jan to 2 Feb, 7 to 9 Feb), the audience (page: "families and friend groups"). | Location is Voss, Hardangerfjord and Myrkdalen (3-day ski L80). Calling it "Voss" is acceptable but incomplete. Age conflict: "10+ years" vs "no age limits" (L90 vs L114). Do not state an age. |
| 7 | "Your 3-day winter escape to Norway" / "Ski + snowshoeing" / "See the 3-day trip" | "Winter escape" speaks to the segment (couples, remote workers). | It is near-identical to creative 6. The viewer cannot tell the two trips apart. Sub-line leaves out the powder day, which is this trip's selling point. | Price (NOK 16,527), dates (5 to 7 Feb, 12 to 14 Feb with Valentine's Day, 5 to 7 Mar), tour name. | Two different products with near-same copy. Another trap: the page says Intermediate and "Basic resort skiing skills" (multi-sport L88, L111), while the day-one text says "absolute beginner" (L95). Do not claim beginner. |
| 8 | "7-day northern lights tour" / "Bergen, Voss, Tromsø, skiing, huskies, northern lights" / "Explore the tour" | Concrete list. | A noun dump with no hierarchy. Headline sells the aurora, which is the one thing that cannot be promised. | Price (NOK 41,181), dates, proof. | Headline leads with aurora (guarantee risk). "Skiing" is one beginner day with a 1-day pass. |
| 9 | Eyebrow "7 days | 6 nights" / "5 Norwegian winter experiences" / "Bergen, skiing, snowshoeing, huskies, northern lights" / "Explore the 7-day tour" | "7 days | 6 nights" is exact and checks out (6 nights twin-share, 7-day L156). The count hook ("5") is a good curiosity device. | Duplicates creative 8 for the same tour. "Explore the 7-day tour" repeats creative 8's CTA. | Price, dates, proof. | The count must match the page. Count the list: Bergen, skiing, snowshoeing, huskies, northern lights = 5. The page also sells a private fjord boat day. If the ad says "5", the count must stay consistent across every variant. |

### 2.2 Patterns across the nine

1. None of the nine carries a price or a date. Both winning references that carry a date or a price (ref B, ref C) use them as central design elements.
2. Every CTA is a soft verb: Join, Explore, Find out how, Check dates, See. The winners use "Explore the tour", "See details" and "Plan today". The verb quality is similar. The issue is that nothing in the ad earns the click beyond curiosity.
3. Three creatives sell one tour (6 and 7 both 3-day, 8 and 9 both the 7-day). That suits a test, but not as two separate "concepts". Under Meta's creative-diversity guidance (sibling notes 03, section 4) similar ads compete for the same audience and learn less. [VERIFY: Meta's delivery behaviour is partly vendor lore, see notes 03]
4. Skill level is shown in only two of nine (creative 4 eyebrow, and indirectly 1). The page analysis shows skill level is the first filter for every segment.
5. No proof anywhere: no rating, no group size, no guide credential, no inclusion that removes a worry (gear, lessons, ski pass).
6. Three creatives carry claims the pages do not support (4, 5, 8). Fix before design.
7. The nine only use "Voss" and "Fjord" as place words. The sensory and cultural material the pages offer (frozen waterfalls, waffles, campfire grill, the train from Bergen) is untouched.

### 2.3 Direction for the fix (not final copy)

- Tour names: use the confirmed names. Creative 8 and 9 should use "7 Day Ski in Fjord Norway & Aurora in Tromsø" or a shortened form of it that keeps skiing in the name.
- Put the date line and the "from NOK" pill on the warm-audience versions. For cold audiences, test one version with price and one without.
- Fix the plural "ski days", the "6 days of skiing" line and the aurora promise first.
- Make each of the seven tours visibly different at thumb distance: place names, duration and one unique hook each.
- Illustrative lines, not approved (each supported by page text): "One ski day in Voss. Three nights under Arctic skies in Tromsø." (7-day L123, L124 to L131, FAQ L297), "Three ski days, a lesson on each. The Hardangerfjord on snowshoes in between." (6-day L105, L140), "Two nights, two dinners, skis and boots included." (multi-sport L128).

### How adwright should use this

- Add a "claim to source" pass to every output: each factual phrase must trace to a page line. Fail anything that counts a ski day or promises a sighting.
- Add a "same product, same face" check: if two creatives sell one tour, flag them as variants and not concepts.
- Add a CTA verb check that prefers verbs tied to a next step the viewer can predict ("See dates and prices", "Plan your trip") over "Explore".

---

## 3. Outdoor Norway voice guide for ads

### 3.1 What the client's own rules say (Official: brand-voice-checker, guest-benefit-checker, content-qc)

| Rule | Source | Meaning for an ad |
|---|---|---|
| Tone: warm, confident, friendly. Not overly casual, pushy or robotic. | brand-voice-checker rubric | No shouting, no hype stack. Confident does not mean loud. |
| Language: descriptive, sensory, nature-inspired. Not generic, cliche or exaggerated. | same | Name the thing. Avoid "magical", "breathtaking", "unforgettable". |
| Style: short and vivid, mixed with flowing, poetic lines. | same | On a static image: one short line, plus one longer, calmer line in the primary text. |
| Perspective: speak to "you", use "we". Not "the company" or passive third person. | same | "We guide", "you ski". Never "Outdoor Norway offers". |
| Lead with the guest's problem or benefit, not the itinerary or the sales pitch. | guest-benefit-checker | The first line is the guest's stake. Logistics only with a reason to care. |
| The guest is the subject. | same | "You ski the fjord" beats "Our guides lead the group". |
| No negative framing on any activity. Describe difficulty by what the day involves, not adjectives or warnings. | content-qc, step 5 | Never "only for experts" or "if you can handle it". Write "confident on skis" and "long ascents". |
| No unsupported superlative (largest, first, only). | content-qc | "Best", "most", "only" need a source. |
| No guarantee of a natural phenomenon. | content-qc | Aurora, snow, powder: possibility language only. |
| Price, season and inclusion facts must match the source. | content-qc | See sections 7 and 11. |
| Mission: unforgettable outdoor adventures that leave guests empowered, inspired, connected to nature. Values: sustainability, local expertise, guest empowerment. | brand-voice-checker | Local expertise is the strongest asset in a paid ad. Empowerment is the emotional job. |
| Writing rules for this research set: no dashes, no emojis, no ALL CAPS emphasis, short sentences, no filler. | Task rules | Treat as house style in every output. |

Note the tension: the mission uses the word "unforgettable", but the rubric says to avoid cliche and exaggeration. Treat "unforgettable" as brand mission language, not an ad word. Show the memory, do not label it.

### 3.2 Voice in one paragraph

Outdoor Norway talks like a Voss local who guides for a living and is not trying to sell. The voice is warm and plain. It uses facts that only someone who has been there would know (the gondola starts at the train station, the waffle is eaten with jam at the mountain café, the snowshoe route climbs steeply for the first stretch and then opens above the trees). It says "you" when it describes what the guest will do, and "we" when it describes what the team looks after. It does not hype the weather or promise a sky. It admits what a trip does not include and trusts the reader to decide.

### 3.3 "We" and "you"

| Situation | Use | Example pattern (illustrative) |
|---|---|---|
| Guest action | "You" | "You ski Voss, Myrkdalen, Sogndal and Stranda." |
| Team action | "We" | "We handle the transfers and the route." |
| Shared moment | "We" only when a guide and guest do it together | "We skin up at nine." (day tour starts 9:00, day tours L156) |
| Never | "Outdoor Norway offers", "Our company", "Guests will" | Third person breaks the rubric. |
| Questions to "you" | Sparingly, and never tied to a personal attribute (section 10) | "Alps queues?" is fine. "Are you a beginner?" is not. |

### 3.4 Vocabulary

Use (each is grounded in the client pages or in observable Norwegian specifics):

| Word or phrase | Why | Source |
|---|---|---|
| Fjord, plateau, gondola, chairlift | Concrete geography. The Voss gondola leaves from the train station. | 9-day L100 to L125, hub L137 |
| Guide, local guide, certified guide | The page language is "certified guides" (hub L66). | Page |
| Small group | Hub badge "Small groups" (hub L65). No number is stated, so do not add one. | Page |
| Resort, lift-served, piste | Honest vocabulary for the resort trips. | Page |
| Skins, skinning, touring binding | Only for the two day tours. | Beginner L68 |
| Frozen waterfall, frozen lake, birch and snow-covered forest | Image-ready details from the pages. | 9-day L117, L115 (frozen lakes), L111 (snow-covered forests) |
| Campfire, grilled food, warm drink | A specific moment on the multi-sport trip. | Multi-sport L97 |
| Waffles, mountain café, coffee | Local, sensory, specific. | 9-day L121 |
| Train from Bergen, about an hour | A real convenience with a scenic moment. | 3-day ski L141, hub L137 |
| Husky team, dog sled | Concrete and visual. | 7-day L131 |
| Aurora (possible, never certain) | Honest verb: "look for", "hunt for", "wait for". | 7-day L115 |
| Snowshoe | Distinctive in this category. | Multi-sport page |
| "Guide handles routes, conditions and logistics" | A benefit line from the hub (hub L121). | Page |

Sensory words that are specific to Norway and not cliches (Inference, grounded where marked):

- Sound: the squeak of dry cold snow; a gondola hum; skins on snow (the page describes climbing skins and skinning, Beginner L68); a chair clacking over a frozen lake.
- Light: low winter sun; blue hour (Inference); a polar night sky in Tromsø (7-day describes "long northern nights", L113).
- Texture: birch bark and rime frost; cold-smoke powder (careful: "powder" is conditions-dependent); the weight of a wool layer (pages advise wool base layers, 9-day L172).
- Taste: waffle with jam at a mountain café (9-day L121); a hot drink at a campfire (Multi-sport L97); Norwegian dinner after the lifts close (9-day L111, but see "do not claim").
- Scale: a fjord seen from above. Folgefonna glacier on the horizon (3-day ski L78). Four fjords visible from the snowshoe route (3-day ski L78: Samlafjorden, Sørfjorden, Eidfjorden, Granvinsfjorden).
- Place names with a story: Hangurstoppen (6-day L113), Mount Oksen (day tour L149), Tjoflot (3-day ski L78).

Avoid (cliche list). The client pages themselves use many of these, so the ad voice must be tighter than the page voice:

| Avoid | Reason |
|---|---|
| Winter wonderland | Overused on the pages (hub, 3-day ski, 7-day). Cliche under the rubric. |
| Breathtaking, magical, unforgettable, epic, spectacular, stunning | Exaggeration. |
| Bucket list | Used in ref A for a contrast. Consider other devices. |
| Hidden gem | Used on the 9-day page (L123). Cliche. |
| Adrenaline, thrill-seekers, rush | Wrong tone for beginners and families, and over-promises. |
| Journey (as a noun for a trip) | Filler. |
| Perfect powder, pristine snow | A promise about conditions. Beginner L60 says "perfect powder conditions". Do not repeat. |
| Guaranteed anything | Guarantee of a natural phenomenon. |
| Few slots left, last chance, don't miss out | False urgency risk, see section 10. |
| Seamless, hassle-free, stress-free | Filler and banned in this set's style rules. |
| Best, most scenic, number one | Needs proof. The 9-day FAQ's "most scenic Norway ski trip we run" (L258) is a safe own-range claim only with "we run". |
| "Hei!" and "Vi ses snart" | Used once on the 9-day page. Acceptable as a rare warm touch, never as a headline gimmick. |
| Tipping language | Not ad material. |

### 3.5 Sentence shape

- A short sentence of 3 to 7 words as the hook. A second sentence with the fact. A third that names the proof or the offer.
- One flowing line in the primary text is allowed, to satisfy "short and vivid, mixed with flowing, poetic lines". Keep it to a single sentence of about 20 words.
- Numerals for numbers ("3 days", "4 resorts", "NOK 17,451").
- Dates in full: "30 Jan to 7 Feb 2027" (the page uses "30 Jan - 07 Feb").
- No hashtags and no emoji on X (notes 03 section 8.5).

### 3.6 Voice checks run against sample lines (illustrative, not approved)

| Line | Tone | Language | Style | Perspective | Verdict |
|---|---|---|---|---|---|
| "Four ski resorts. Nine days. One fjord road trip." | Pass | Pass | Pass | Weak (no "you") | Add a "you" in the primary text. |
| "You ski Voss in the morning and Myrkdalen the next day." | Pass | Pass | Pass | Pass | Check against the 9-day itinerary: Voss days 2 and 3, Myrkdalen day 4, so "next day" is wrong. Needs to read "after two days in Voss". |
| "Unforgettable fjord skiing adventure." | Fail (generic) | Fail | Pass | Fail | Cliche stack. |

### How adwright should use this

- Ship a voice file with the "use" and "avoid" tables above and a lint that flags any avoid-list word, any third-person company reference, any capital-letter word used for emphasis, any em or en dash, and any emoji.
- Include a "specific detail picker" that pulls one sensory detail per tour from the claims bank so every ad carries a fact only this operator can say.
- Have the lint run the brand-voice rubric rows as a checklist (tone, language, style, perspective) and the content-qc rule on negative framing and unsupported superlatives.

---

## 4. What the best category brands do on Meta and X (documented, not observed)

I could not open the Meta Ad Library (403). The table lists documented campaigns, press and company statements. A creative that I cannot see is not described.

### 4.1 Case notes

| Brand | Campaign or fact | Hook and offer named in the source | Result claimed | Evidence class | Source |
|---|---|---|---|---|---|
| Visit Norway | "Winter alpine skiing" retargeting campaign, launch week 41 (trade page), retargeting window of about 4 weeks | Position Norway "as a preferred destination for alpine skiing holidays, especially aimed at families with children". Markets: Denmark, Sweden, UK, Germany. Motivation segments: Social Immersion, Broadening My Cultural Horizons, Energy, Sharing and Caring. No creative or copy shown. | None stated | Official (trade page) | https://www.visitnorway.com/travel-trade/practical-information/retargeting/take-part-in-this-autumns-campaigns/ |
| Inghams Ski | "Ski Better with Inghams" (Sept 2025) with Norway offers | Offer mechanics: "Norway: buy one, get one free on all lift passes" and "Learn to Ski" packages (six-day pass, five days tuition, equipment rental). Norway example: 7 nights at Park Hotel, Voss from GBP 762 per person, saving GBP 274, flights and transfers included. | None stated | Reported | https://planetski.eu/2025/09/24/inghams-ski-launches-new-winter-campaign/ |
| Inghams Ski | New weekly charter London Gatwick to Bergen, first flight 21 Dec 2025, serving Voss, Myrkdalen and Geilo | Value for money and snow reliability, family and beginner terrain | Agents: "that charter will make a big difference" | Reported | https://travelweekly.co.uk/news/inghams-ski-charter-to-bergen-will-make-big-difference-say-agents |
| Ski Safari | Norway pages and blog "Try skiing the Norwegian way" | Hooks: "Rarely queue for a lift, even during peak weeks", slopes "often completely empty", ski-anywhere easy off-piste, train travel as part of the trip, dog sledding, snowshoeing. Prices: 7-night holidays from GBP 739 per person, average customer spend GBP 1,090 (company statement). | Company statements, not independent | Vendor | https://www.skisafari.com/blog/try-skiing-the-norwegian-way |
| Crystal Ski, Ski Solutions | Trade reports 2024/25 | Crystal MD: "excellent for beginners and intermediates, and most importantly in these times of climate change it is snow-sure". | Crystal: Norway passengers up 140% year on year. Ski Solutions: 2024/25 bookings up 57%, passengers up 83%. Both as reported by PlanetSKI. | Reported | https://planetski.eu/2024/11/28/skiing-in-scandinavia-surges/ and https://planetski.eu/2024/10/22/skiing-in-norway-grows-grows/ |
| Epic Pass and Ikon Pass | Sales deadlines and price tiers | Real deadlines. Ikon Pass price increase expected after 8 Oct 2026 (forecast by a pass-tracking blog: Ikon Pass up about USD 110 to USD 1,559). Epic gives extra benefits to early buyers (buddy tickets) and raises price in stages. | Not a creative case. Shows how a ski brand creates honest urgency with dates and price tiers. | Reported | https://www.epicorikon.com/news/ikon-pass-prices-increasing-october-2026 and https://www.powder.com/ski-resorts/epic-ikon-pass-deadline-fast-approaching (403 for me, search summary only) |
| Backroads | "Say Yes to Summer" (Jan 2026) | Early booking: "Travelers who plan now have the best selection of dates available." No discount stated. Company claim: nearly 50% of 2025 summer bookings were made in January and February. Group pricing from 10 travellers. | None independent | Vendor (company press release) | https://www.backroads.com/about/media/press-releases/backroads-launches-new-say-yes-summer-campaign |
| Backroads | 2026 trends release | Women's Adventures bookings projected to grow 100% in 2026. Mountain lodge and hut stays up more than 170% since 2024. Company data. | None independent | Vendor | https://www.backroads.com/about/media/press-releases/future-adventure-travel-backroads-announces-2026-trend-outlook |
| G Adventures | "Love the World" (2025) | Lead-gen with a community story: "dream big, share stories". | 130,000+ entries, largest lead-gen effort. NPS 78. Company statements. | Reported | https://www.travelmarketreport.com/canada/destinations/articles/g-adventures-fy-2025-sales-targets-smashed-community-keeps-growing |
| Intrepid | "Only Intrepid" (Sept 2025 chapter) | First-person, immersive, real people, real places. Shifted from about 80% performance spend to a 50/50 brand and performance split. | 2024 chapter: 55% rise in global brand search (company). Other figures (21% awareness, 10,000 first-time customers, USD 29m sales) come from trade coverage. | Official for the first, Reported for the rest | https://www.intrepidtravel.com/us/newsroom/releases/next-chapter-of-only-intrepid |
| Inspired by Iceland / Promote Iceland | "Looks like you need Iceland" and "Let it out" (2020), "OutHorse" (about 2022) | Pattern-interrupt humour that names a universal frustration (lockdown, always-on email) and offers Iceland as the release. | Agency case write-up: 725,000 people used the site, 2.67 billion media impressions, 5.7x increase in booking intent. | Vendor (case study) | https://www.sookio.com/blog/the-anatomy-of-a-campaign-promote-iceland-let-it-out and https://www.stuckiniceland.com/inspired-by-iceland/ |
| Visit Finland | "Masterclass of Happiness" (May 2024) | Frame Finnish living as a teachable skill. Social-first, creator reach. | Awards-entry figures: 150,000+ applicants, EUR 165m earned media value, 8% rise in overnight stays. | Vendor (award entry summary) | https://www.adsoftheworld.com/campaigns/masterclass-of-happiness |
| Arc'teryx | "No Wasted Days" (Oct 2023) | Uncommon journeys, unexpected protagonists, real people. | No metrics published | Official (company newsroom) | https://www.amersports.com/newsroom/no-wasted-days-arcteryxs-global-brand-campaign/ |
| REI | "#OptOutside" (2015) | Counter-intuitive stance: closed on Black Friday. | 1.4 million people took part. 2.7 billion media impressions in 24 hours (reported). | Reported (old, craft only) | https://www.retailtouchpoints.com/features/news-briefs/rei-optoutside-campaign-results-show-power-of-sincerity-plus-engagement |
| Patagonia | Storytelling and community, Worn Wear | Real customers, repair stories. One summary says less than 1% of revenue goes to paid media. | [VERIFY: figure from a marketing-blog summary, not a primary source] | Vendor | https://www.ptengine.com/blog/business-strategy/sustainable-success-patagonias-unique-approach-to-digital-marketing/ |
| Black Tomato | Luxury tailor-made Norway: ski and sail in Lofoten, Svalbard ski adventure | Experience-led, high end. A different tier from Outdoor Norway. | None | Official (company pages) | https://www.blacktomato.com/destinations/norway/lofoten-ski-sail/ |

### 4.2 Patterns across the case notes

Documented (appears in at least one source above):

1. Operators sell Norway against the Alps on crowds, snow certainty and value. Ski Safari: "Rarely queue for a lift". Crystal: "snow-sure". Inghams: lift-pass offers and learn-to-ski bundles.
2. Offers target the two top barriers directly: cost (buy-one-get-one-free passes, early-bird tiers) and fear (learn-to-ski packages with tuition and equipment in one price).
3. Honest urgency uses a real calendar: pass price tiers with dates (Epic, Ikon), "plan now for the best choice of dates" (Backroads). None of the sources uses a fake countdown.
4. Human and first-person content for brand work (Intrepid, Arc'teryx, REI, Patagonia). Faces and real people appear in all of them.
5. The strongest destination campaigns turn a shared frustration into the hook (Iceland, Finland). That is brand-scale work with creators and PR. A static ad from a small operator can borrow the structure (one shared frustration, one relief) and not the scale.
6. Booking windows are early. A survey cited by Firebird Partnership: "41% of all UK skiers now book more than 6 months ahead, up from 26% pre-pandemic" (Ski Club and MTN survey, 2024/25). Reported, secondhand. Today is 6 Oct 2026 and the first 2027 departure (7-day, 23 Jan) is 109 days away, so the remaining sales window for most departures is under four months.
7. Package spend anchors the price conversation. Ski Safari lists an average of GBP 1,090 for a 7-night Norway holiday with flights. Outdoor Norway's guided, no-flight prices are not directly comparable and the ad should not claim "cheaper" or "better value" against them.

Inference (not documented): the small-operator ski ads that pull leads probably do so by combining a named place, a dated departure and a human face, as ref B does. The three references are the only direct evidence I have.

### 4.3 What this means for X

Notes 03 section 8.4 reports Norwegian X reach of about 1.02 million (DataReportal, October 2025, a page summary, tagged [VERIFY] there) against Facebook 3.05 million and Instagram 2.65 million. X for a ski operator is a secondary channel. The documented examples above are mostly brand work on other channels. I found no primary source for ski or outdoor performance on X. [VERIFY: pull X Ads audience insights for Norway before committing budget]

### How adwright should use this

- Build the library of "offer mechanics" from the table: lift-pass or lesson bundles, honest date windows, early-booking framing, group pricing. Let the user pick one mechanic per ad, and require that the mechanic exists in the client's terms.
- Never invent an offer. The client's pages give no discount. The skill must ask for any offer, never create one.
- Include a one-line caution in the skill that the category case studies are mostly brand work with large budgets, and that a static image ad for a small operator should be judged on clarity and proof.

---

## 5. The skier buyer: psychology, and why Norway over Austria or France

Separation rule: Documented means a source says it. Inference means I am reasoning. Both are labelled.

### 5.1 Documented drivers of the ski holiday decision

| Driver | What the source says | Class | Source |
|---|---|---|---|
| Fear of injury | The NSAA (US ski areas association) finds the number one barrier to try ski or ride is fear of injury, then cost. The secondary source gives no sample size or year. | Reported, thin | https://www.slopefillers.com/why-dont-ski-survey-action/ |
| Cost | "90% of younger skiers cite affordability" (Ski Club of Great Britain figure via a search summary). | Vendor [VERIFY] | search summary of https://matadornetwork.com/read/small-ski-resorts-growing-in-popularity/ |
| Value over convenience | 68% of customers say value matters more than convenience or choice. 60% choose a resort by lift-pass cost. 87% cite snow certainty as important. All from an Iglu Ski 2025 survey, relayed by Firebird. | Reported | https://www.firebirdpartnership.com/post/ski-sector-2025-26 |
| Early booking | 41% of UK skiers book more than 6 months ahead (Ski Club and MTN survey). | Reported | same |
| Adult beginner anxiety | Adults worry about lifts, about holding others up or feeling silly, and about injury and recovery time. Instruction is the main remedy cited. | Vendor (advice sites) | https://travelwithmansoureh.com/blog/learning-to-ski-as-an-adult-practical-tips-and-mistakes-to-avoid |
| Crowds as a complaint | A Tripadvisor review analysis by PrivacyTutor (30,000+ reviews, year not stated) lists overcrowding as a main complaint at several Alpine resorts. Les Deux Alpes has 56.7% overcrowding and Ischgl 58%. Cost complaints top 57.7% at Zermatt. | Vendor | https://welove2ski.com/which-european-ski-resorts-get-the-most-complaints/ |
| Snow reliability in the Alps | A study of French Alps resorts 1961 to 2019 found challenging snow conditions became more frequent in 1991 to 2019, with the steepest changes in November and in March to April. Snowmaking helped mainly in December and January and "did not counterbalance" the decline at lower-elevation resorts or in spring. | Official (peer reviewed) | https://tc.copernicus.org/articles/16/863/2022/ |
| Global snow cover in ski areas | A PLOS ONE study projects that 13% of ski areas will lose all natural annual snow cover and about a fifth will lose more than half by 2071 to 2100 (search summary). | Official (peer reviewed) [VERIFY wording] | https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0299735 |
| Norway demand | Crystal Ski: Norway passengers up 140%. Ski Solutions: 2024/25 Norway bookings up 57%. UK annual visitors to Norway reported at 45,000 to 50,000 by an agent, "UK traffic now exceeding Swedish and Danish". | Reported | links in section 4.1 |
| Norwegian outdoor culture | In SSB's survey, 66% did longer hikes or skiing in the previous 12 months in 2021 (73% in 1974). The share who do it at least three times a week doubled from one in ten in the early 1970s to two in ten in the early 2020s. | Official | https://www.ssb.no/en/kultur-og-fritid/idrett-og-friluftsliv/artikler/outdoor-activities-in-norway-status-and-historical-development |
| Friluftsliv meaning | A compound of "free air life", commonly attributed to Ibsen in 1859. | Vendor [VERIFY the attribution] | https://www.lifeinnorway.net/friluftsliv-outdoors/ |

### 5.2 Why a European ski buyer might pick Norway over Austria or France

Documented in the sources above:

- Fewer crowds. Ski Safari, PlanetSKI and the Outdoor Norway pages all say so. Outdoor Norway's own page: "Myrkdalen and Stranda are significantly less crowded than well-known Alpine destinations" (9-day L249). That is the client's own claim and a comparative one, so keep it tied to the page text.
- Snow security by latitude. PlanetSKI: Norwegian resorts "over 1,000 miles north of the Alps" with colder, more stable temperatures. Crystal MD: "snow-sure".
- Value. Ski Safari lists 6-day lift pass GBP 229 and equipment GBP 116 (company numbers). Travel Weekly agents say the weak krone helps affordability while bar prices stay high.
- Nordic extras. Aurora, huskies, snowshoeing, train rides (Ski Safari, Inghams).
- Easy access. Direct flights from London Gatwick to Bergen from 21 December 2025 (Inghams). From Bergen, Voss is about an hour by train (3-day ski L141: "just over one hour").
- Heritage. PlanetSKI's line that Norway has more Winter Olympic medals than any other nation (405 total, 148 gold, as of the 2025 article). Milano Cortina 2026 then added a record 41 medals and 18 golds (Life in Norway, NBC Olympics). A "birthplace of skiing" claim appears on Ski Safari. [VERIFY: the origin of skiing is contested. Do not claim "invented skiing" in an ad.]

Honest counterpoints the skill should know (Documented unless marked):

- Altitude. Voss Resort's base is listed at 284 m and its top at 964 m (skiresort.info via search summary, other sources give 220 m and 945 m). Myrkdalen's base is listed at about 1,500 feet (about 457 m) with a vertical of about 2,000 feet (Norway Home of Skiing). Norway's snow case rests on latitude and maritime precipitation, not height. [VERIFY: confirm elevations with the resorts] Coastal Norway can see mild spells and rain in winter (Inference). The ad must not promise snow.
- The Voss area's own tourism page calls Myrkdalen "one of the most snow sure destinations in Europe" (visitvoss.no). That is a destination claim. Quote it as theirs and not as a fact the client can prove.
- Cost. Norway is expensive in food and alcohol terms. Travel Weekly agents advise "go half board" and note bar prices. Tour prices here exclude lunches, dinners (mostly), beverages and flights.
- Day length. Ski Safari concedes that day length in December is "similar to the Alps". Voss's January and February days are short (hub L131: "January and February are about deep winter conditions, snow-covered valleys and shorter days").
- Size. Voss Resort lists 14 pistes over about 40 km (skiresort.info via search summary, [VERIFY]). Voss and Myrkdalen together: "almost 70 kilometres of slopes" and "20 ski lifts" (visitvoss.no). Alpine ski areas run to hundreds of kilometres. The pitch is variety and calm, not size.

### 5.3 The fjord skiing difference (Page, with limits)

The client pages state:

- "Norway fjord skiing puts you on slopes that descend toward open water, with fjord panoramas visible from the pistes." (9-day L235)
- "Voss and Stranda are the greatest examples on this road trip." (9-day L236)
- "Fjord skiing in Norway combines mountain descents with views of dramatic fjords and open water below." (hub L142)
- "A rare sea-to-summit experience" (hub L143).

The Voss ski area lies inland near a lake (the 9-day page itself describes views "across the Voss valley", L111). Do not write a headline that puts a fjord under every ski turn. Use "views of the fjord country" for the set and name Stranda for the open-water view. [VERIFY: with a guide, which resorts show a fjord from the piste]

### 5.4 Inference: the psychological job of the Outdoor Norway buyer

- The buyer is spending a lot (NOK 17,451 to 42,126) and usually travelling with someone. The cost of a bad trip is social as well as financial. Proof and specifics reduce that cost.
- Skiers who are tired of queues carry a specific memory: the lift line. The page promise "free from queues or crowded pistes" (9-day L119) and "lift queues are typically short" (L121) are the sentences that answer that memory. Use the second ("typically short"), which is hedged and safer.
- For beginners, the fear is social (holding the group up) as much as physical. A visible "lesson on every ski day" (6-day L140) is the cleanest answer.
- For couples and friends, the job is a story to tell. Dated, named trips give them one.

### How adwright should use this

- Give the skill a "decision driver" slot per ad: queue relief, snow certainty, fear relief, value, variety, story. One driver per ad, with the proof line from section 8.
- Include an "altitude honesty" rule: never write "guaranteed snow" or "snow-sure". Allow "season runs December to April" (9-day FAQ L238) with the "up to Mother Nature" hedge on the page.
- Keep the Norway versus Alps comparison to the client's own page claim and a neutral frame ("no queue lines", "fjord views"). Do not name Alpine resorts or competitors in the ad.

---

## 6. Audience segments for the ski tours

Seven segments. Each lists the job to be done, the main anxiety, the angle, the fit among the seven in-scope tours, and the evidence class. Segment descriptions are Inference unless marked. The pages themselves name some audiences (marked Page).

| # | Segment | Job to be done | Main anxiety | Angle that fits | Best tours | Evidence |
|---|---|---|---|---|---|---|
| 1 | Alps-weary intermediate and advanced skiers (couples and friend groups, mostly 30 to 60, Nordic, UK, Benelux, German) | Get more variety and less queuing from a ski week they already know how to do | Will it be as good as the Alps? Is Norway too expensive? Will the snow be there? | Variety, calm, fjord setting. "Four resorts, nine days, a guide who handles the route." | 9 Day Ski Trip (NOK 42,126) | Page names this audience: "intermediate and advanced skiers who want to experience more than a traditional ski holiday" (9-day L105). Demand data: section 5. |
| 2 | Aurora-first first-time Norway visitors (couples 35 to 65, small friend groups) | See Norway from the fjords to the Arctic in one trip | Aurora might not show. Will the skiing be too hard? | Seven days, two sides of Norway, aurora as a bonus. | 7 Day Ski in Fjord Norway & Aurora in Tromsø (NOK 41,181) | Page: "for travellers who want to experience a proper Norwegian winter without needing to be experienced skiers" (7-day L104). "It's also a great fit if you're visiting Norway for the first time and can't decide between the fjords of Western Norway and the Arctic north" (L106). |
| 3 | Learn-to-ski adults and occasional skiers | Learn on safe terrain with real instruction and without feeling like the slow one | Fear of injury, fear of holding others up, cost of rental and lessons | A lesson on every ski day, two gentle resorts, a day off skis. | 6 Day Ski Package (NOK 28,896) | Page: "Designed for beginners and occasional skiers" (6-day L103). Barrier data: section 5.1. |
| 4 | Families and friend groups wanting a short winter break | A compact trip with ski and non-ski days so mixed abilities fit | Will the kids and the non-skiers be bored? Is it too long, too complex? | Three days, three different days. | 3-Day Ski and Snowshoe Experience (NOK 17,451) | Page: "Crafted for families and friend groups" (3-day ski L59). Hub: snowshoeing "works particularly well ... if you're travelling with non-skiers" (hub L111). |
| 5 | Couples and remote workers needing a winter reset | A long weekend that feels like a break and fits a working week | Will it take too long to organise? Will it be too sporty? | Valentine's departure for couples. Three days that fit a working week. | 3-Day Winter Multi-Sport Explorer (NOK 16,527) | Page: "The February Valentine's Day departure is specifically designed for couples, and the three-day format fits cleanly into a working week for remote workers" (multi-sport L175). |
| 6 | Confident resort skiers curious about ski touring (visitors with a spare Saturday or Sunday in Voss) | Try touring with a guide, gear sorted, no experience needed | Avalanche risk, fitness, the gear, the cost of kit | "New to ski touring, confident on skis." Guide goes through the equipment. | Backcountry Ski Tour Beginner to Intermediate (NOK 1,948) | Page: "You need no experience with skinning, touring bindings or avalanche gear" (Beginner L71). |
| 7 | Experienced off-piste skiers and freeriders | Long ascents and steep descents with local knowledge | Is this a real objective or a tourist tour? Will the guide pick good terrain? Safety | Terrain chosen 48 hours out from weather, snow and avalanche forecast. | Backcountry Ski Tour Intermediate to Advanced (NOK 1,948) | Page: "we require a good level of off-piste skiing, no exceptions" (Advanced L69). |

Additional segment cues:

- Segment 6 is also the cheapest path to the brand for segments 1 and 4: a NOK 1,948 first purchase can feed a retargeting pool for the multi-day trips. (Inference.)
- Segment 3 and segment 4 overlap on the 3-Day Ski and Snowshoe page, but the page recommends "prior hiking and skiing experience" (3-day ski L92), so the safe segment for that tour is "families and friend groups" and not "beginners".
- Women-only or women-led ski groups. Ref C performs with that angle, but no ski tour page offers it. Do not imply one. [VERIFY: whether a women's ski departure is planned]
- Seniors. Pages state "no maximum age limit" (9-day L246, 7-day FAQ). Use "no upper age limit" as a trip fact, never as address to the viewer (section 10).

### How adwright should use this

- Make "segment" a required input. For each segment, preload the anxiety and the proof lines from sections 7 and 8.
- Never write a beginner-segment line for the 3-day ski and multi-sport pages. The pages contradict themselves on level (section 7). Ask the user to resolve first.
- Offer a two-step funnel option: day tour ad for cold audiences, multi-day ad for retargeting.

---

## 7. Claims bank per tour

Format: each claim is a near-quote from the page text, with the file and line. Prices and 2027 dates are from CONFIRMED-PRICES-AND-DATES.md. Where the page contradicts the confirmed price, the confirmed price is used and the conflict is listed.

Global notes that apply to all seven tours:

- Group size and guide ratio: no page states a number. The hub shows a "Small groups" badge (hub L65) with no figure. Do not write "max 8", "group of 10" or any number.
- Per person: not stated. Use "from NOK X". [VERIFY: confirm with Sameer whether prices are per person before writing "per person"]
- Rental: "All gear included" appears on the hub (L67) and on the 9-day, 7-day and 6-day pages as a badge (9-day L91, 7-day L93, 6-day L94), but the same pages list ski gear as rentable or not included. Do not claim "all gear included" on those three tours.
- Guest rating: hub shows "4.9/5 Rating" on each tour (for example hub L64 and next to each product). The source and review count are not given. [VERIFY]
- Cancellation policy differs by page. The 9-day, 7-day and 6-day pages state 60, 45, 30 day tiers of full, 75% and 50% refund and none under 30 days (9-day L175 to L178). The two 3-day pages describe a "Lifetime Guarantee" and forfeiture within 60 days (3-day ski L155 to L162). The 6-day FAQ says the tour information shows a 50% deposit, a 45-day booking window and a Lifetime Guarantee, while the general terms "contain different payment and cancellation provisions" (6-day L331 to L333). Do not put cancellation terms in ads.
- Tipping: not an ad topic.

### 7.1 9 Day Ski Trip in Norway, NOK 42,126

Dates 2027: 30 Jan to 7 Feb, 11 Feb to 19 Feb, 20 Feb to 28 Feb, 13 Mar to 21 Mar, 10 Apr to 18 Apr. Page: 9-day-ski-holidays.txt.

| Fact | Near-quote | Line |
|---|---|---|
| What it is | "Ski Norway across Voss, Myrkdalen, Sogndal and Stranda on a guided fjord road trip." | L60 |
| Price | "From NOK 42,126" and "Incl. all taxes" | L84 to L85 |
| Duration | "9 days" | L67 |
| Resorts | Voss Resort (Days 2 and 3), Myrkdalen (Day 4), Sogndal (Days 5 and 6), Stranda (Days 7 and 8) | L110 to L125 |
| Route | Arrive Bergen Day 1, "welcome tour", transfer to Voss. Day 9 transfer to Ålesund, drop off at Vigra Airport. | L109, L127, L160 |
| Skill level | "perfect for intermediate and advanced skiers"; guest requirements "Confident on skis", "Good physical health" | L105, L155 to L156 |
| Difficulty label | "Moderate" | L73 |
| Season | Spec strip "Feb - Apr". FAQ: "Typically, this spans from early December to late April, but it's entirely up to Mother Nature" | L69, L238 |
| Accommodation | "4-star hotel in Voss"; "8 nights of accommodation including breakfast" | L71, L146 |
| Guide | "Certified Expert Guides"; "Guide" in inclusions | L89, L144 |
| Transport | "Transportation" in inclusions; "All other transportation and/or transfers during the trip between the initial pick-up and final drop-off are included" | L145, L161 |
| What the page says about queues | "You can enjoy the winter vibes free from queues or crowded pistes" (Sogndal) and "Lift queues are typically short" (Sogndal day) | L119, L121 |
| Crowds | "Myrkdalen and Stranda are significantly less crowded than well-known Alpine destinations" | L249 |
| Myrkdalen snow | "a resort renowned for its reliable snowfall and peaceful atmosphere" | L117 |
| Voss | "one of Norway's largest ski areas", "from gentle cruisers to steep black runs" | L111 |
| Stranda | "Perched high above the fjords", "skiing with panoramic views stretching across snow-covered peaks and deep blue fjords below" | L123 |
| Scenic claim, own range only | "This is the most scenic Norway ski trip we run." | L258 |
| Variety vs short trips | "a 3 day or a 4 day skiing trip in Norway covers only one resort. This road trip covers four" | L244 |
| Gear | Bring your own boots, poles, helmet, avalanche kit, or rent: "items above you can rent from us, prices below" (price table is not in the text) | L164 to L167 |
| Not included | "Lunch, dinner, beverages and snacks", "Accident/travel insurance", airfare | L149 to L151, L159 |
| Age | "no maximum age limit" | L246 |
| Own gear | Only with touring bindings (FAQ text, appears to be template text) | L252 |

Do not claim:

- "All gear included" (badge at L91, contradicted by L164 to L167).
- Lift passes included. Not listed anywhere in the inclusions (L144 to L147). [VERIFY: with Sameer. This is the most important gap on the biggest tour.]
- Dinner included. Day 2 text says "a hearty Norwegian dinner await[s]" (L111) but dinner is "Not Included" (L149).
- Backcountry or touring. The itinerary is resort skiing with "off-piste areas when conditions allow" (L111).
- Beginner friendly. The page says intermediate and advanced (L105). Myrkdalen day does mention "beginners and intermediates" (L117), which conflicts.
- "Fjord views at every resort". Page names Voss and Stranda as "greatest examples" (L236).
- A group size, a guide ratio, "small group".
- Guaranteed snow, powder, or "no queues".
- "Season Feb to Apr" as the dates window (first departure is 30 Jan).
- "Luxury". The FAQ question includes "luxury" but the answer speaks only of scenic route (L257 to L259).

Page problems to log (content-qc): "All gear included" badge versus rental; "Easy to medium activities" (L88) versus "Moderate" (L73) versus "intermediate and advanced" (L105); FAQ text and stale prices in the related products block (NOK 13,462 and NOK 31,769 at L272 and L282); snowboard FAQ describes snowshoes and splitboards (touring template, L252 to L256).

### 7.2 7 Day Ski in Fjord Norway & Aurora in Tromsø, NOK 41,181

Dates 2027: 23 to 29 Jan, 30 Jan to 5 Feb, 6 to 12 Feb, 13 to 19 Feb, 27 Feb to 5 Mar. Page: 7-day-ski-and-aurora.txt.

| Fact | Near-quote | Line |
|---|---|---|
| What it is | "a 7-day northern lights tour that combines snowshoeing, beginner-friendly skiing, dog sledding and the Aurora between Bergen and Tromsø" | L60 |
| Price | "From NOK 41,181", "Incl. all taxes" | L85 to L86 |
| Duration, nights | 7 days, "6 nights of twin-share accommodation" | L68, L156 |
| Season | "January - March" | L70 |
| Skill level | "You don't need previous skiing experience. The ski day in Voss is beginner-friendly." Spec: "Easy to intermediate" | L105, L74 |
| Minimum age | "Minimum age is 8 years old" | L173 |
| Route | Day 1 Bergen; Day 2 train to Voss (about an hour) plus guided snowshoe tour; Day 3 skiing at Voss Resort; Day 4 flight Bergen to Tromsø plus Aurora Safari; Day 5 private boat trip on the fjords with onboard chef lunch, Aurora observation at the hotel's camp; Day 6 dog sledding plus Aurora hunt; Day 7 transfer to Tromsø Airport | L118 to L134 |
| Ski day | "Day 3 is a dedicated skiing day at Voss Resort" and "1-day ski pass at Voss Resort" | L297, L155 |
| Included | Professional guide throughout; all transportation in Norway; flight Bergen to Tromsø; 1-day ski pass; 6 nights twin-share; 6 breakfasts; 5 dinners; guided winter experiences and Northern Lights activities | L152 to L159 |
| Not included | Ski equipment ("rentals are available and can be arranged"), lunches, beverages and snacks, flights to and from Norway, insurance, personal expenses | L161 to L166 |
| Rental line | "Skis, ski boots, poles and helmets are not included in the trip price, but rental equipment is available and can be arranged for your ski day in Voss." | L201 |
| Aurora honesty | "Of course, the Northern Lights are a natural phenomenon, so no departure can guarantee an appearance." | L115 |
| Own positioning | "a trip for people who want to see the Northern Lights, but don't want their entire holiday to depend on seeing them" | L102 |
| Meal prices | Lunch "(€15 to €25)", the one dinner not included "approximately €20 to €30" | L171 |
| Pickup and drop | Pickup Bergen Flesland Day 1, drop-off Tromsø Airport Day 7 | L180 |

Do not claim:

- "All equipment" or "all gear included". The spec strip says "All equipment + guide + transfers + stay" (L76) and the badge says "All Gear Included" (L93), but the page says ski equipment is not included (L161, L201).
- Ski days (plural). One ski day.
- A guaranteed or probable aurora. Say "chances".
- "Private" tour. The boat is described as "private boat" for the day, but guest group status is not stated.
- Lunch included. Day 5 describes an onboard chef lunch (L128) but lunches are listed as not included (L162). [VERIFY]
- "Three nights of aurora" without checking. FAQ says "three nights chasing the Northern Lights" (L313) and elsewhere that "Days 5 and 6 are aurora and Arctic experience days" (L299). Itinerary shows Aurora on days 4, 5 and 6 (L125, L128, L131).
- "7 nights". It is 6 nights.
- "Fjord skiing". The ski day is at Voss Resort. The 7-day FAQ itself says "fjord skiing in Voss" (L313). The 9-day page names Voss as a fjord example. Use with care.

### 7.3 6 Day Ski Package Fresh & Cruisers, NOK 28,896

Dates 2027: 29 Jan to 3 Feb, 4 Feb to 9 Feb. Page: 6-day-ski-package.txt. The page headline is "6-Day Norway Ski Package in Voss & Myrkdalen" (L59). The words "Fresh & Cruisers" appear only in related-product blocks on other pages.

| Fact | Near-quote | Line |
|---|---|---|
| What it is | "A 6-day Norway ski package for beginners, with three ski days, personalised lessons at Voss Resort and Myrkdalen, guided Hardangerfjord snowshoeing, five hotel nights and a Bergen finish." | L60 |
| Price | "From NOK 28,896", "Incl. all taxes" | L84 to L85 |
| Season | "January and February" | L69 |
| Difficulty | "Beginner" | L73 |
| Audience | "Designed for beginners and occasional skiers who want to learn to ski in Norway or build confidence with personalised instruction." | L103 |
| Lessons | "Personalised instruction at Voss Resort on Days 2 and 4, and Myrkdalen on Day 5." | L140 |
| Ski passes | "Voss Resort ski passes: Two days, including gondola travel in both directions." "Myrkdalen ski pass: One day of resort access." | L141 to L142 |
| Snowshoe | "Guided snowshoe tour: One excursion in the Hardangerfjord region." plus snowshoe equipment | L143 to L144 |
| Accommodation | "Three nights at Fleischer's Hotel and two nights at Myrkdalen Hotel." Twin room, or double room for couples | L146 to L147 |
| Meals | "Breakfast: Five breakfasts" | L148 |
| Bergen | "Mount Fløyen funicular: A ticket for the Bergen visit on Day 6." | L149 |
| Resorts | "Voss pairs gondola-accessed skiing with cafés, restaurants and a town connected to Bergen by train. Myrkdalen adds beginner-friendly slopes and a mountain hotel stay, approximately 30 minutes away by road." | L107 |
| Honest framing | "This is a varied winter holiday, not an advanced backcountry ski tour." | L103 |
| Why three ski days | "Because this is a mixed winter holiday, not a six-day ski trip." Ski days are Days 2, 4 and 5 | FAQ L292 to L294 |
| Snowshoe demand | "includes uphill walking and a challenging initial ascent" | L103 |
| Not included | Flights, lunches, dinners, beverages, snacks, insurance | L151 to L156 |
| Rental | "Skis, boots, poles and helmets are not included in the trip price, but rental options are available locally." | L192 |
| Hotel names | Fleischer's Hotel (3 nights), Myrkdalen Hotel (2 nights) | L146 |

Do not claim:

- "6 days of skiing". Three ski days.
- "All gear included" (badge L94, contradicted at L192 and L315 to L317).
- Meals included. Spec strip says "meals" (L75), page says breakfast only.
- Rental, airport pickup, Bergen train tickets or return transfers. The page says "Do not assume they are included or excluded" (L157).
- Child eligibility or age. The FAQ says the published information "contains different age references" (6-day FAQ L324 to L325).
- "Fresh powder". The tour name implies it, but the page positions it as resort skiing with lessons.
- Price from the FAQ. The FAQ says "Contact us for the current price and availability". The confirmed price is NOK 28,896.
- Lesson group size or duration (FAQ says to confirm "the lesson duration and format").
- Deposit or cancellation terms (page says they conflict).

### 7.4 3-Day Ski and Snowshoe Experience, NOK 17,451

Dates 2027: 28 to 30 Jan, 31 Jan to 2 Feb, 7 to 9 Feb. Page: 3-day-ski-and-snowshoe.txt. The page's own price "From 13,462 (NOK)" at L67 is stale. The typo "31nd Jan" at L148 should read "31 Jan".

| Fact | Near-quote | Line |
|---|---|---|
| Positioning | "A ski escape in the Heart of Fjord Norway", "Crafted for families and friend groups" | L59 |
| Badges | "Easy to medium slopes", "Professional guide", "Unique snowshoe trails", "Beautiful Fjord Norway vistas" | L60 to L63 |
| Location | "Voss & Hardangerfjord & Myrkdalen" | L80 |
| Season | "Dec - Apr" | L82 |
| Duration | "3 days" | L86 |
| Difficulty | "Beginner to intermediate"; recommendation: "Prior hiking and skiing experience is recommended for this trip." | L88, L92 |
| Day 1 | Voss Resort: "Glide down perfectly groomed slopes or take lessons with the family" | L96 |
| Day 2 | Guided Hardangerfjord snowshoe hike. "Our guided tour ensures an immersive experience suitable for all ages." Shuttle to start. | L99 to L100 |
| Day 3 | Myrkdalen: "versatile, but family-friendly, slopes" | L103 |
| Snowshoe route | Mt. Oksen from Tjoflot through native forest, "panoramic views of Voss's mountain ridge and Norway's third-largest glacier, Folgefonna", fjords named | L78 |
| Myrkdalen | "Established in 2003", "snow-sure season from December to May" (page claim) | L78 |
| Included | "Activities + equipment + guide" (spec), "Professional Guide", "All Transportation" | L84, L131 |
| Not included | "Lunch, dinner, beverages and snacks", insurance | L133 |
| Access | Train from Bergen, "just over one hour", accommodation "only 50 metres" from Voss station | L141 to L142 |
| FAQ summary | "Three days covers Voss Resort, a snowshoe hike at Hardangerfjord, and a full skiing day at Myrkdalen. ... Guides and all transport are included throughout." | L166 |
| Rental | "We do offer rental gear if needed." | L129 |

Do not claim:

- Accommodation included. Hotels are described (L136) but not listed in inclusions (L131). [VERIFY: with Sameer]
- Lift passes included. Not listed. [VERIFY]
- "Beginner". Spec says "Beginner to intermediate" but the recommendation asks for prior hiking and skiing experience.
- An age. "10+ years" (L90) versus "No age limits" (L114).
- "Pristine" or "perfect" snow.
- "Don't miss out", "Book today" (page body L75 uses them). Avoid in the ad.
- Anything from the template line "Basic bike riding skills" (L115).
- The price on the page (stale).

### 7.5 3-Day Winter Multi-Sport Explorer, NOK 16,527

2027 dates only: 5 to 7 Feb, 12 to 14 Feb (Valentine's Day departure, Sunday 14 Feb 2027), 5 to 7 Mar. The page's "2026" dates are past. Page: 3-day-winter-multi-sport.txt. The page price "From 12,749 (NOK)" at L67 is stale.

| Fact | Near-quote | Line |
|---|---|---|
| Positioning | "A thrilling 3 day journey into the Winter Wonderland" and "a daring explorer, a couple seeking an extraordinary escape, or a remote worker craving a revitalising break" | L59 |
| Badges | "Easy to medium slopes", "Professional guide", "Snowshoeing on pristine hillsides", "Beautiful Fjord Norway vistas" | L60 to L63 |
| Location, season | "Voss", "Dec - Apr" | L80, L82 |
| Difficulty | "Intermediate", "Prior hiking and skiing experience is recommended", "Basic resort skiing skills" | L88, L92, L111 |
| Day 1 | Voss Resort groomed slopes with guides | L95 |
| Day 2 | Snowshoe hike, "grill some local delicacies on an open campfire, sipping a warm beverage" | L97 |
| Day 3 | "powder skiing experience ... guided by our seasoned experts you will glide through hidden powder skiing routes" | L99 |
| Included | "Professional Guide", "Snowshoes and poles", "Ski, ski boots, ski poles and helmets", "2 dinners", "2 nights of accommodation including breakfast", "Shuttle transfer from the hotel to the activities location" | L128 |
| Not included | "Lunch, dinner, beverages and snacks" (other meals), insurance | L130 |
| FAQ | "three completely different experiences: groomed slopes at Voss Resort, a snowshoe hike through Hardangerfjord, and powder skiing on the final day" | L167 |
| Couples and remote workers | "The February Valentine's Day departure is specifically designed for couples" | L175 |
| Meeting point | "Evangervegen 14 5704 Voss", "300 metres from the Voss Train Station" | L185 to L186 |

Do not claim:

- Beginner friendly. Page level is "Intermediate" (L88), skills "Basic resort skiing", though Day 1 text says "absolute beginner" (L95).
- Powder as a promise. The page implies it. Natural snow conditions vary.
- Lift pass included. Not listed. [VERIFY]
- The 2026 departures.
- Dinner on every night. Two dinners over two nights is stated.
- "Hidden routes" as a safety statement. The page names no avalanche kit or route plan for the powder day. Do not call it "backcountry". [VERIFY]
- The page's phrase "guarantees an unforgettable winter experience" (L59, L75).

Page conflict to log: meeting point at multi-sport L185 is "Evangervegen 14", while the day tour pages state "Evangervegen 32" (Beginner L116) and "tourist information center" (Beginner L157).

### 7.6 Backcountry Ski Tour, Beginner to Intermediate, NOK 1,948

Dates: "available every Saturday and Sunday, from January to April" (day-backcountry-beginner.txt L147). The page title uses "Beginner". Hub title: "Backcountry ski tour, beginner".

| Fact | Near-quote | Line |
|---|---|---|
| Positioning | "New to ski touring, confident on skis"; "Professional guide"; "Theoretical instruction before you start"; "Beautiful panorama vistas" | L61 to L64 |
| Skill statement | "This tour is for guests who are new to ski touring but already confident on skis. You need no experience with skinning, touring bindings or avalanche gear. Before you head uphill, your guide goes through the equipment and technique." | L71 |
| Hard limit | "If you are new to skiing, it is not the right tour." | L100 |
| Price | "1948 NOK (Adults) 1753 NOK (Young)" | L90 |
| Duration | "5 Hours" (spec). Start "9:00 am", return "around 3 pm" | L94, L156 |
| Season | "Jan - Apr" | L88 |
| Included | "Guide", "Transportation from Voss town to the skiing location and back to Voss" | L111 |
| Not included | "Lunch, beverages and snacks", "Avalanche safety kit (beacon, shovel, probe and backpack)" (rentable), "Lift tickets", insurance, transport if outside Voss town | L113 |
| Rental | "Skis, skins, boots and helmet available to rent. Avalanche kit and backpack available to rent. Gear sorted out before you start." | L83 |
| Where | Location decided "48-hours before ... based on the group's wishes, as well as the weather, snow conditions, and avalanche forecast". Candidate areas: Mount Oksen (Hardangerfjord), Lønahorgi (Voss to Afdal traverse), Raundalen, Vikafjell, south side of the Sognefjord | L147 to L153 |
| Meeting | "Show up 10 minutes before your scheduled time", Evangervegen 32, "300 metres from Voss Gondola" and from the train station | L116 |
| Age | "+14 years old (the guardian signs waiver for minors)" | L128 |
| Open group | "Open Group Pricing NOK 1,858 per person per day. A minimum of 3 participants is required for the open group to operate." Private guide fee "NOK 5,500 per day" in addition | L161 |

Do not claim:

- "Beginner" as a viewer label ("for beginners"). The page's own hard limit says new skiers should not book. Use "New to ski touring".
- "No experience needed" without "confident on skis".
- Avalanche kit included.
- A specific summit or location in the ad (chosen 48 hours out).
- "Every weekend" as a promise. Open group needs 3 participants or a refund or a shared fee.
- "Perfect powder" (L60).
- "Best backcountry ski tour in Norway" (page H1, L58). It is a superlative with no source.
- "5 hours" and "9 to 3". Pick one after checking with the guides. [VERIFY]
- Price as "NOK 1,948 per person" until confirmed. The same page sells an "Open Group" price of NOK 1,858 per person and a "private guide fee" of NOK 5,500. [VERIFY: which is the hub's NOK 1,948]

### 7.7 Backcountry Ski Tour, Intermediate to Advanced, NOK 1,948

Dates: every Saturday and Sunday, January to April (day-backcountry-advanced.txt L149). Page evidence below.

| Fact | Near-quote | Line |
|---|---|---|
| Positioning | "Pristine powder snow", "Professional guide", "Clean mountain air", "Beautiful Fjord vistas" | L61 to L64 |
| For whom | "designed specifically for those who have extensive experience in the backcountry and are looking for long days with endless powder and steep drops" | L68 |
| Hard rule | "for our big mountain runs, we require a good level of off-piste skiing, no exceptions. These days will include long ascents that require both a high level of fitness and previous hours spent hiking in backcountry conditions" | L69 |
| Safety process | "Location chosen 48 hours before the tour, based on weather, snow conditions and avalanche forecast" | L83 |
| Gear | "Skis, skins, boots, helmet, avalanche kit and backpack available to rent" | L85 |
| Spec | "Intermediate to advanced", "14+ years Experience on skis", "5 Hours", "Jan - Apr" | L98, L100, L96, L90 |
| Price | "1948 NOK (Adult) 1753 NOK (Youth)" | L92 |
| Included | "Private guide", transportation Voss town and back | L113 |
| Not included | Lunch, beverages, snacks, avalanche kit (rentable), lift tickets, insurance, transport from outside Voss | L115 |
| Open group pricing table | "1 person: 1,650/day per person ... 2 people: 3,300/day per group ... 7 people: 10,500/day per group". Open group minimum 3. Private guide "4,500,- NOK/day" | L164 to L171 |
| Start | "9:00 am", return "around 3 pm" | L158 |

Do not claim:

- "Private guide" as a feature. Inclusions say "Private guide" (L113) while the product is also sold as an open group.
- "Endless powder" or "steep drops" as promises.
- That avalanche safety equipment is included.
- That the group is small.
- The NOK 1,948 as the only price. The table at L164 to L171 shows 1,650 per person and group rates that rise (for example 5,250 for three, 1,750 each). [VERIFY: Sameer decides the headline price]
- "Best". Use the page's own wording with care.

### 7.8 Hub-level facts usable in any ski ad (ski-hub.txt)

| Fact | Near-quote | Line |
|---|---|---|
| Rating, group, guide badges | "4.9/5 Rating", "Small groups", "Certified guides", "All gear included" | L64 to L67 (the last conflicts with several tours) |
| Voss access | "The resort sits minutes from Voss town centre, Bergen is one hour away by direct train" | L137 |
| Mix of skiing | "groomed resort runs with guided backcountry access and fjord-view descents from the same base" | L137 |
| Variety | "Longer ski trips can link several areas together instead of keeping you on the same mountain all week." | L121 |
| March | "March is one of our favourite months to ski: there's more daylight for longer days in the mountains while winter conditions are still well established." | L131 |
| Snowshoes with non-skiers | "Snowshoeing offers an accessible alternative" | L111 |
| Eco | "certified Eco Lighthouse (Miljøfyrtårn) company" | 9-day L286 |
| Contact | +47 56 99 40 21 | hub L5 |

### How adwright should use this

- Convert each table into a JSON claims file keyed by tour. The generator may only draw facts from that file. Anything outside it comes out as "[VERIFY]".
- Give the "do not claim" list its own lint: flag "all gear included", "ski days", "6 days of skiing", "guaranteed", "private" and any group-size number.
- Add the page-conflict log to the intake so the user resolves badges, prices and level before ads go live.

---

## 8. Objections and the proof line for each

Proof lines are near-quotes from pages and can be used or adapted. Anything marked [VERIFY] has no proof on the page.

| # | Objection | Segment | Proof line (source) | Use in |
|---|---|---|---|---|
| 1 | "Is Norway too expensive?" | 1, 2 | State the price plainly: "From NOK 42,126, incl. all taxes" (9-day L84 to L85). Name what is included (8 nights with breakfast, transport, guide, L144 to L147) and what is not (lunch, dinner, drinks, L149). | Price pill, primary text |
| 2 | "Will there be snow?" | 1, 3, 4 | "Typically, this spans from early December to late April, but it's entirely up to Mother Nature" (9-day L238). Safer: "Season runs December to April." Page claim: "a resort renowned for its reliable snowfall" (9-day L117). | Primary text. No guarantee. |
| 3 | "I'm a beginner. Will I hold the group up?" | 3 | "Personalised instruction at Voss Resort on Days 2 and 4, and Myrkdalen on Day 5" (6-day L140). "Your first lesson ... focuses on safety, fundamental technique and skiing at your level" (6-day L88). | 6-day ad |
| 4 | "Is the 7-day trip too hard if I do not ski?" | 2 | "You don't need previous skiing experience. The ski day in Voss is beginner-friendly" (7-day L105). | 7-day ad |
| 5 | "Is it safe? What about avalanches?" | 6, 7 | "Location chosen 48 hours before the tour, based on weather, snow conditions and avalanche forecast" (Advanced L83). "Certified guides" (hub L66). "You need no experience with ... avalanche gear. ... your guide goes through the equipment and technique" (Beginner L71). | Day tour ads |
| 6 | "What is included? Any hidden costs?" | all | Each tour's own inclusion list (section 7). Use the exact items. For gear: rental "available" on the day tours (Beginner L83) and "Ski, ski boots, ski poles and helmets" included on multi-sport (L128). | Primary text. Footer line. |
| 7 | "Are lift passes included?" | 1, 4, 5 | 7-day: "1-day ski pass at Voss Resort" (L155). 6-day: ski passes for 3 days (L141 to L142). 9-day, 3-day ski, multi-sport: not stated. [VERIFY] | Only where stated |
| 8 | "A 6-day package with only three ski days?" | 3 | "Because this is a mixed winter holiday, not a six-day ski trip. ... Day 3 includes a guided Hardangerfjord snowshoe experience" (6-day FAQ L292 to L294). | 6-day ad. Say "3 ski days" up front. |
| 9 | "What if the aurora does not show?" | 2 | "no departure can guarantee an appearance" (7-day L115). "If the sky puts on a show, incredible. If it makes you wait, you've still spent seven days experiencing Norway in winter" (L116). | 7-day ad. Lead with the trip, not the sky. |
| 10 | "Will I be on a crowded mountain?" | 1 | "Lift queues are typically short" (9-day L121). "Free from queues or crowded pistes" (Sogndal day, L119). | 9-day ad |
| 11 | "Small group or a coach tour?" | all | Hub badge "Small groups" (hub L65). No number is stated. [VERIFY: number] | Badge only |
| 12 | "Can my partner or kids who do not ski join?" | 4, 5 | "Snowshoeing offers an accessible alternative" (hub L111). Snowshoe day: "suitable for all ages" (3-day ski L99). 7-day minimum age is 8 (L173). | 3-day ski ad |
| 13 | "I am over 60. Is it for me?" | 1, 2 | "Our winter tours have no maximum age limit; as long as you're physically fit, and you are enthusiastic, you're welcome to join" (9-day L246). | Trip fact, never addressed to viewer |
| 14 | "How do I get there?" | all | "Bergen is one hour away by direct train" (hub L137). 9-day: pickup at Bergen Flesland on Day 1 (L160). 7-day: pickup in Bergen, drop at Tromsø Airport (L180). | Primary text for logistics-sensitive buyers |
| 15 | "Who are these guides?" | 6, 7 | "Certified guides" (hub L66). For avalanche training detail, no page gives credentials. [VERIFY: ask for the certification names] | Day tour ads |
| 16 | "Can I change my dates?" | all | Pages conflict (section 7 notes). [VERIFY: cancellation and Lifetime Guarantee terms] | No ad claim |
| 17 | "Is it a real ski trip or a tourist trip?" | 1, 7 | 9-day: "a guided fjord road trip" over four resorts (L60). Day tour: "we require a good level of off-piste skiing, no exceptions" (Advanced L69). | Ads for confident skiers |
| 18 | "Is the rating real?" | all | Hub "4.9/5 Rating". Needs named source and count before use. [VERIFY] | Badge |

### How adwright should use this

- Hold the objection table as a lookup: the user picks a segment, the skill proposes the top two objections and drops in the proof line with its source.
- Do not let the skill answer any objection that has [VERIFY]. It should ask the user.

---

## 9. Competitor and category positioning map

### 9.1 Who the buyer compares against (documented where noted)

| Group | Examples | What they sell | Typical hook | Price signal | Source |
|---|---|---|---|---|---|
| UK mass operators | Inghams, Crystal Ski, Ski Solutions, Sno Group, Snowfinders | Flights, hotel, lift pass, optional lessons. Voss, Myrkdalen, Geilo and others from London Gatwick to Bergen. Self-guided. | Value, "snow-sure", learn-to-ski bundles, BOGOF lift passes | 7 nights from GBP 762 per person at Park Hotel Voss (Inghams); Ski Safari quotes GBP 739 from, GBP 1,090 average | PlanetSKI, Travel Weekly, Ski Safari |
| Specialist tailor-made | Ski Safari | Multi-stop "ski safaris" by train: Bergen Railway Ski Safari (Geilo and Voss), Ski and Northern Lights Safari (Tromsø plus ski near Oslo), Ski and Fjord Explorer Safari | Rarely queue, quiet slopes, Nordic extras | Mid | skisafari.com |
| Luxury tailor-made | Black Tomato | Lofoten ski and sail, Svalbard ski adventure | Rare places, curated | High | blacktomato.com |
| Local guides in Voss | Wild Voss, Hardanger Fjellguide | Guided ski touring, avalanche courses, tailored holidays. Wild Voss states its guides are "NF certified avalanche instructors". | Credentials, tailor-made, local | Not published | wildvoss.no |
| Resort ski schools | Voss Resort, Myrkdalen | Lessons, passes | Convenience | Voss adult day ticket about NOK 690 in peak season, Myrkdalen about NOK 600 (search summary, [VERIFY]) | norwaysbest, visitvoss |
| Aurora specialists in Tromsø | Aurora tour companies | One-off aurora chases | The sky | Varies | The 7-day page names one competitor in its FAQ (7-day L313). Do not name competitors in ads. |
| Alpine substitutes | Austria, France, Switzerland, Italy | Large resorts, better-known | Scale, après, familiarity | Lift passes often higher | section 5 |

### 9.2 Positioning map (axes: guided small-group vs self-guided package, and resort variety vs backcountry depth)

| | Resort-based, variety | Mixed (resort plus non-ski) | Backcountry depth |
|---|---|---|---|
| Guided, fixed departure, no flights | Outdoor Norway 9 Day, 6 Day | Outdoor Norway 7 Day, 3 Day x2 | Outdoor Norway Day tours |
| Guided, tailor-made | Ski Safari (partly) | Ski Safari, Black Tomato | Wild Voss, Hardanger Fjellguide |
| Self-guided package with flights | Inghams, Crystal, Ski Solutions | Inghams (Norway offers) | Not offered |

Reading of the map (Inference): Outdoor Norway is one of few operators in the fixed-date, guided, no-flights, mixed-resort cell. Its direct rivals for the day tour are local guiding firms with stronger avalanche credentials on show. Its rivals for multi-day trips are packages that include flights at lower headline prices.

### 9.3 Positioning statements the evidence supports

1. "A local guide in Voss who links fjord resorts, lessons and non-ski days into one dated trip." Proof: pages.
2. "Ski days with a fjord view and no flights to book." Proof: pages (flight not included, section 7). The "no flights to book" phrase is an inference. Use "flights not included" in plain text instead.
3. "Skiing for the people who do not want the whole holiday to depend on the weather or the sky." Proof: 7-day L102.

Not supported: "cheapest", "most credible guides", "best snow", "only".

### 9.4 Price positioning

| Tour | Price (NOK) | Price per day (NOK, rounded) | Notes |
|---|---|---|---|
| Backcountry day tours | 1,948 | 1,948 | Day. Gear and lift tickets extra. |
| 3-Day Winter Multi-Sport Explorer | 16,527 | 5,509 | Includes 2 nights, 2 dinners, ski gear. |
| 3-Day Ski and Snowshoe Experience | 17,451 | 5,817 | Inclusions unclear. |
| 6 Day Ski Package | 28,896 | 4,816 | 5 nights, 3 ski days, ski passes. |
| 9 Day Ski Trip | 42,126 | 4,681 | 8 nights, breakfast, transport. |
| 7 Day Ski and Aurora | 41,181 | 5,883 | Flight Bergen to Tromsø, 6 nights, 5 dinners. |

Per-day figures are my arithmetic for internal comparison only. Do not use in ads. Prices are "from" and the per-person status is unconfirmed.

### How adwright should use this

- Give the skill a "do not name competitors" rule and a "do not claim cheaper" rule.
- Have it choose one of the three positioning statements per ad, based on tour and segment.
- Offer a comparison mode for the human user (not for ad copy) that shows the map above.

---

## 10. Meta policy risk check for ski ads

Policy readings come from Meta's Advertising Standards pages I could open, plus the sibling research (notes 03, section 5). Where my own tool reads disagreed, I say so. Always read the live page before shipping. [VERIFY: all quotes]

### 10.1 What Meta's personal attributes policy says

From https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/ :

- "Ads must not contain content that asserts or implies personal attributes."
- Named categories: race or ethnicity, religion, age, sexual orientation, gender identity, physical or mental health, disability, vulnerable financial status, voting status, trade union membership, criminal record, name.
- Prohibited examples include: "Are you 18 years old?", "Do you have diabetes?", "Are you bankrupt? Check out our services.", "Meet other seniors".
- Allowed examples include broad references and "you" language without an attribute, "Meet seniors" and "A service for teens".
- My two reads of the same page returned one inconsistent pair (one allowed-list item showed up on both lists). The pattern I take from the page: addressing the viewer as the attribute ("Are you...", "other ...") is the trigger, and a passing reference or a descriptor of the offer is not. [VERIFY on the live page]

Skill level ("beginner", "intermediate", "advanced") is not a listed attribute. Fear, injury or physical condition language can drift toward health. The age and health categories are the ones a ski ad can touch.

### 10.2 Risk table

| Item | Example risky line | Why | Severity | Safer pattern |
|---|---|---|---|---|
| Ability label as viewer label | "Are you a beginner?" | "Are you" plus a status. Ability is not listed but the pattern is the same as listed examples. | Medium | Describe the trip: "A ski week with a lesson on every ski day." |
| Fear or health language | "Scared of the slopes?" "Worried about injury?" | Can read as implied mental or physical state. | Medium to high | "A lesson on each ski day. Gentle terrain." |
| Age | "Skiing over 60?" "Ski trips for seniors" | Age category | Medium to high | "No upper age limit" as a trip fact, not addressed to the viewer. Do not target by age in the copy. |
| Fitness | "Do you have the fitness?" | Health | Medium | "Guest requirements: good physical health" on the landing page. |
| Women-led | "Ski trip for women only" | Gender is not on Meta's list (gender identity is). A women-only product descriptor is common and used in ref C. | Low [VERIFY] | Product descriptor only, and only if a women's departure exists |
| Financial status | "Can't afford the Alps?" | Financial situation | High | "From NOK 17,451" with inclusions |
| Relationship status | "Single? Join a ski week" | Pattern in vendor lists | Medium [VERIFY] | "Solo travellers welcome" only if true |
| Scarcity: slot counts | "Few slots left" | Hub shows this badge. Meta prohibits false scarcity. Forbrukertilsynet also treats false urgency as misleading. | High | Delete unless live availability is confirmed |
| Scarcity: countdown | "Book before midnight" | False urgency unless real | High | Real departure dates |
| Urgency: calendar | "Departures: 30 Jan to 7 Feb" | A real, finite date | Low | Keep |
| Price: "from" | "From NOK 1,948" | Allowed if the landing page shows the same starting price. Forbrukertilsynet: price information must include taxes and mandatory fees. Pages say "Incl. all taxes" on four tours. | Low if consistent | Match image, text, headline and landing page |
| Price: per person | "NOK 17,451 per person" | Not stated by the pages | High if wrong | Write "from NOK 17,451" until confirmed |
| Price: stale | NOK 13,462 or 12,749 on the 3-day pages | Landing page conflict | High | Fix the page, then run the ad |
| Price: wide range under one "from" | Day tour "from NOK 1,948" when open group is NOK 1,858 or 1,650 | Landing page mismatch | Medium to high | Resolve first |
| Discount framing | "Was NOK X, now NOK Y" | Forbrukertilsynet's 30-day reference rule covers goods and notes it does not apply to services (notes 03). General misleading-marketing rules still apply. | Medium | Do not use without proof of earlier price |
| Guarantee | "See the aurora guaranteed" | Page itself denies it. Meta flags unrealistic claims. | High | "Chances" language |
| Guarantee: snow | "Guaranteed snow" | Unprovable | High | "Season runs December to April" |
| Superlatives | "Best backcountry tour in Norway" | Needs proof. Page H1 uses it. | Medium | Own-range wording, "the most scenic trip we run" |
| Safety claims | "Safe off-piste" | Unprovable | High | State the process: "location chosen 48 hours out from the avalanche forecast" |
| Ratings | "4.9" | Needs named source and current number | Medium | "Tripadvisor 4.9" with source verified |
| Testimonials | Quote without name | Must be real | Medium | Real guest quote with permission |
| Imagery | Backcountry photo on a resort trip | Landing page and ad must match what is offered (content-qc check 11) | Medium | Photo matches the product |
| Imagery: safety | No helmets, wrong gear | Reviewer and audience perception | Low | Helmets visible on skiers |
| Alcohol | Après drinks | Restricted goods | Low to medium | Avoid, or 18+ targeting |
| Text in image | Heavy text | The old 20% rule ended in 2020 (notes 03) | Low | Keep text short for legibility |
| AI-edited text | Advantage+ editing text in image | Can alter a price or date after approval (notes 03, section 4.4) | Medium | Turn off text-altering enhancements, check final render |
| UTM | `utm_source=chatgpt.com` on every ClickUp link | Mislabels traffic | Medium (reporting) | Meta UTMs |

### 10.3 Norwegian and EEA layer

- Price information must include taxes and mandatory fees (Forbrukertilsynet, travel and transport). For "from" prices that apply only to some options, the range should be shown. https://www.forbrukertilsynet.no/vi-jobber-med/reise-og-transport
- Limited-quantity claims must be true and clear. Forbrukertilsynet also warns against false countdown timers. https://www.forbrukertilsynet.no/lov-og-rett/veiledninger-og-retningslinjer/forbrukerombudets-retningslinjer-markedsforing-flybilletter-tilbys-begrenset-antall-billetter-annonsert-pris
- Package travel rules. A package combines at least two kinds of travel service (transport, accommodation, other significant tourist services) for the same trip. The 7-day and 9-day trips combine transport, accommodation and guided activities, so the Norwegian Package Travel Act (pakkereiseloven) and the travel guarantee scheme (Reisegarantifondet) may apply. https://lovdata.no/lov/1995-08-25-57 [VERIFY: confirm with the client whether the trips are registered as package travel and what ad disclosures apply]
- Labelling creator content as advertising (notes 03).
- Location fees on Meta ads for some EU markets and the UK (notes 03). If UK skiers are the target, budget for the fee.

### 10.4 X

I could not open X policy pages (HTTP 402 and 403 per notes 03). Apply the same claim rules. X audiences punish ad-like voice, so keep the wording plain (notes 03, section 8.5).

### How adwright should use this

- Run the risk table as a lint in three tiers: block (guarantee, false scarcity, price mismatch), warn (personal-attribute pattern, superlative, rating without source), note (image match, AI-edit).
- Make the footer say: "Policy readings are a checklist, not legal advice. Read the live Meta page and the client's terms."
- Add a rule to the intake: every ad needs a pasted landing page price. If the page shows a stale price, stop.

---

## 11. Open items to confirm with Sameer (the VERIFY list)

| # | Item | Why it matters |
|---|---|---|
| 1 | Are lift passes included in the 9 Day, 3-Day Ski and Snowshoe, and 3-Day Multi-Sport trips? | Not stated. The biggest cost question on the biggest trips. |
| 2 | Is accommodation included in the 3-Day Ski and Snowshoe? | Inclusions list guide and transport only. |
| 3 | Are prices per person? | Pages do not say. |
| 4 | Which price is the day tour price: NOK 1,948, NOK 1,858 (beginner open group), or NOK 1,650 (advanced open group)? | Landing page mismatch risk. |
| 5 | Is "All gear included" correct on any tour? | Contradicted on the 9-day, 7-day and 6-day pages. |
| 6 | Group size and guide ratio for each tour | Not stated anywhere. A real number is a strong proof point. |
| 7 | Source and count behind "4.9/5" | Needed for a badge. |
| 8 | Which resorts show a fjord from the piste | Controls the "fjords below" line. |
| 9 | Age rules: 3-day pages say both "10+ years" and "no age limits"; 6-day says confirm age; 7-day says 8; day tours say 14 | Cannot state in ads. |
| 10 | Level for the 3-Day Multi-Sport (Intermediate versus "absolute beginner") | Decides whether a beginner angle is allowed. |
| 11 | Live availability and whether a "limited places" claim is true | Hub "Few Slots left" badge. |
| 12 | Cancellation terms and Lifetime Guarantee terms | Pages conflict. |
| 13 | Package-travel status and any disclosure rule | Legal. |
| 14 | Day 5 lunch on the 7-day (onboard chef) | Conflicts with "lunches not included". |
| 15 | Meeting point address for the multi-sport and day tours | Evangervegen 14 versus 32 versus tourist information. |
| 16 | Real guest quotes and photo permissions | Needed for faces (ref B pattern). |
| 17 | Whether any ski departure is women-only or women-led | Ref C angle. |
| 18 | A real photo set per tour that matches the product | Content-qc imagery check. |

---

## 12. Sources

Client files: all `.txt` pages and CONFIRMED-PRICES-AND-DATES.md in the site folder, the three PNG references, and the four voice skill files.

Web sources opened or read as search summaries:

- Visit Norway trade page on the winter alpine skiing campaign: https://www.visitnorway.com/travel-trade/practical-information/retargeting/take-part-in-this-autumns-campaigns/
- PlanetSKI on why British skiers choose Norway (Nov 2025): https://planetski.eu/2025/11/21/skiing-in-norway-is-this-season-the-time-to-visit/
- PlanetSKI Norway growth: https://planetski.eu/2024/10/22/skiing-in-norway-grows-grows/ and https://planetski.eu/2024/11/28/skiing-in-scandinavia-surges/
- Inghams campaign: https://planetski.eu/2025/09/24/inghams-ski-launches-new-winter-campaign/
- Travel Weekly on the Bergen charter: https://travelweekly.co.uk/news/inghams-ski-charter-to-bergen-will-make-big-difference-say-agents
- Ski Safari: https://www.skisafari.com/blog/try-skiing-the-norwegian-way
- Inghams reasons to ski in Norway: https://www.inghams.co.uk/ski-holidays/inspiration/insider-guides/reasons-to-ski-in-norway
- Visit Voss: https://www.visitvoss.no/en/derfor-bor-du-leggje-skiferien-til-voss-og-myrkdalen
- Myrkdalen facts: https://www.norwayhomeofskiing.com/en/myrkdalen/
- Wild Voss: https://www.wildvoss.no/en/activities/guided-ski-touring/
- Black Tomato: https://www.blacktomato.com/destinations/norway/lofoten-ski-sail/
- Firebird Partnership ski sector round-up: https://www.firebirdpartnership.com/post/ski-sector-2025-26
- Copernicus (French Alps snow reliability): https://tc.copernicus.org/articles/16/863/2022/
- PLOS ONE (global snow cover in ski areas): https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0299735
- Ski complaints analysis: https://welove2ski.com/which-european-ski-resorts-get-the-most-complaints/
- NSAA fear-of-injury line (secondary): https://www.slopefillers.com/why-dont-ski-survey-action/
- SSB outdoor activities: https://www.ssb.no/en/kultur-og-fritid/idrett-og-friluftsliv/artikler/outdoor-activities-in-norway-status-and-historical-development
- Friluftsliv overview: https://www.lifeinnorway.net/friluftsliv-outdoors/
- Norway at Milano Cortina 2026: https://www.lifeinnorway.net/norway-at-2026-winter-olympics/
- Backroads: https://www.backroads.com/about/media/press-releases/backroads-launches-new-say-yes-summer-campaign and https://www.backroads.com/about/media/press-releases/future-adventure-travel-backroads-announces-2026-trend-outlook
- G Adventures: https://www.travelmarketreport.com/canada/destinations/articles/g-adventures-fy-2025-sales-targets-smashed-community-keeps-growing
- Intrepid: https://www.intrepidtravel.com/us/newsroom/releases/next-chapter-of-only-intrepid
- Promote Iceland: https://www.sookio.com/blog/the-anatomy-of-a-campaign-promote-iceland-let-it-out and https://www.stuckiniceland.com/inspired-by-iceland/
- Visit Finland: https://www.adsoftheworld.com/campaigns/masterclass-of-happiness
- Arc'teryx: https://www.amersports.com/newsroom/no-wasted-days-arcteryxs-global-brand-campaign/
- Epic and Ikon: https://www.epicorikon.com/news/ikon-pass-prices-increasing-october-2026
- Meta personal attributes policy: https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/
- Forbrukertilsynet travel and price guidance: https://www.forbrukertilsynet.no/vi-jobber-med/reise-og-transport
- Pakkereiseloven: https://lovdata.no/lov/1995-08-25-57
- Sibling research: notes 03 (platforms, policy), notes 02 (psychology) in the same folder.
