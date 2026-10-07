# Brand voice and claims for Outdoor Norway scripts

Sources: the company skills brand-voice-checker, guest-benefit-checker and content-qc; `.claude/product-marketing.md`; `campaigns/ski-meta-ads/tours.json`. The machine rules are in `scripts/brand_rules.json`. To reuse the skill for another brand, swap that file.

## The voice in one paragraph

A Voss local who guides for a living and is not trying to sell. Warm, plain, confident. Uses details only someone who has been there would know: the gondola leaves from beside the train station, the waffle comes with jam at the mountain cafe, the skin track goes quiet once you leave the car park. Says "you" for what the guest does and "we" for what the team looks after. Never hypes the weather or promises a sky. Admits what a trip does not include.

## Brand voice: four rows (brand-voice-checker)

| Row | Do | Don't |
|---|---|---|
| Tone | Warm, confident, friendly | Overly casual, pushy, robotic |
| Language | Descriptive, sensory, nature-inspired | Generic, cliche, exaggerated |
| Style | Short and vivid lines, one calmer flowing line | Overly complex or dry |
| Perspective | "You" for the guest, "we" for the team | "The company", "Outdoor Norway offers", passive third person |

Mission language ("unforgettable outdoor adventures") is not script language. Show the memory, do not label it.

## Guest first: four checks (guest-benefit-checker)

1. Opens with the guest's question, doubt or desire, not "Day 1, we arrive in Bergen".
2. Every logistics detail passes the "so what" test: the reason to care is stated or obvious.
3. Helpful, not a pitch: a viewer learns something even if they never book.
4. The guest is the subject. "You ski the fjord" beats "Our guides lead the group".

## Difficulty

Describe it by what the day involves: "long ascents", "confident on red runs", "[n] hours on skis", "the guide sets the pace". Never "only for experts", "not for beginners", "if you can handle it", "brutal", "extreme" (BR05). The backcountry beginner tour is for people new to touring but already confident on skis; never call it a beginner ski tour.

## Natural phenomena

- Never promise snow, powder, sunshine, wildlife or the aurora (BR09). That includes "certain", "for sure", "no question", "no doubt", "not a chance you miss", "never miss" and "[phenomenon] every morning, night or week".
- A negation makes a line safe only when it governs the guarantee word directly: "can't promise", "no guide can guarantee", "not guaranteed", "isn't always". "No question, guaranteed" is still a guarantee.
- Any script that mentions the aurora or northern lights must also say it cannot be promised (BR10). The 7 Day trip page says no departure can guarantee an appearance.
- Possibility lines: "if the sky clears", "a chance of seeing the lights", "depends on the sky", "no one can promise the aurora". A bare "a chance of cloud" does not count.

## Rule summary (brand_rules.json)

| Id | Severity | Catches |
|---|---|---|
| BR01 | block | Greeting or channel intro in beat 1 ("hey guys", "welcome to", "in this video") |
| BR02 | block | End signals and sign-offs ("that's it", "to wrap up", "thanks for watching", "like and subscribe") |
| BR03 | block | Cliche and hype ("winter wonderland", "breathtaking", "magical", "epic", "stunning", "bucket list", "adrenaline", "perfect powder", "seamless", "nestled", "majestic") |
| BR04 | block | Scarcity and urgency ("few spots left", "last chance", "hurry", "don't miss out", "seats are going fast", "filling up fast", "spaces are limited") |
| BR05 | block | Negative framing of difficulty ("only for experts", "brutal", "survive", "extreme") |
| BR06 | block | Company-speak ("Outdoor Norway offers", "our guests", "guests will", "we are proud") |
| BR07 | warn | Sales verbs before the CTA ("we offer", "book today", "secure your spot") |
| BR08 | warn | Personal-attribute address ("are you a beginner", "scared of", "are you over") |
| BR09 | block | Guarantee wording near aurora, snow, powder, weather, wildlife, unless a negation governs the guarantee word |
| BR10 | block | Aurora mentioned with no possibility line |
| BR11 | block | Superlatives ("best", "biggest", "ultimate", "world's", "#1", "world-class", "unbeatable", "premier", "award-winning") unless the same beat cites a facts row that contains the same word. In the caption, any row counts |
| BR12 | warn | A date with no year anywhere in the script |
| BR13 | block, --final only | A placeholder ([VERIFY], [TODO], [TBD], [LINK]) still in voiceover or overlay |
| BR14 | warn | Possible exclusivity claim ("the only", "the most", "the first", "first-ever", "nobody else", "leading"). "Your first tour" and "lesson first" are not flagged |

The full phrase lists are in the JSON. Read them before writing, not after the validator complains.

## Facts and [VERIFY]

- Facts come only from: tours.json, product-marketing.md, a page URL the user names, or the user in writing. Never from memory.
- Each fact is one row: id, the fact with the number exactly as spoken, the source, verified yes or no.
- A written client brief is a source. A row is verified yes only for what the brief states; anything you infer from it is no.
- A number is tied to the row you cite in that beat. Every digit spoken or shown, and every spelled number from twenty up ("ninety percent"), must appear in a verified row listed in that beat's facts column (F04). A number found only in another row warns in a draft and blocks with --final. A number in no row blocks.
- Caption digits are checked too (F04): any verified row will do.
- Every factual sentence maps to a fact id cited in that beat, and claims no more than the row. Row "snowshoe day for non-skiers" supports "non-skiers get a snowshoe day", not "nobody skis that day".
- Prices: "from NOK X" for multi-day trips, "NOK X per adult" for day tours. Never "per person" until confirmed.
- Every numeral counts toward the number budget, including the day and the year. Spoken lines and overlays carry one date element per beat ("in February 2027"). Full dates with the year ("30 Jan to 7 Feb 2027") go in the caption or description, backed by a verified row.
- Missing fact: write `[VERIFY: what to confirm, who confirms it]` in the voiceover and list it in open items. Never fill the gap with a plausible number.
- Never invent a URL. Use `[LINK: what the page is]`.

## Confirmed facts that scripts use most

| Fact | Source |
|---|---|
| Backcountry Ski Tour, Beginner to Intermediate: NOK 1,948 per adult, every Saturday and Sunday, January to April | tours.json, backcountry-beginner |
| Backcountry Ski Tour, Intermediate to Advanced: NOK 1,948 per adult, same days | tours.json, backcountry-advanced |
| 9 Day Ski Trip in Norway: from NOK 42,126, 2027 departures 30 Jan, 11 Feb, 20 Feb, 13 Mar, 10 Apr | tours.json, ski-9day |
| 7 Day Ski in Fjord Norway and Aurora in Tromsø: from NOK 41,181; one ski day; aurora not guaranteed | tours.json, product-marketing.md |
| 6 Day Ski Package Fresh and Cruisers: from NOK 28,896; three ski days, "a mixed winter holiday" | tours.json, product-marketing.md |
| Bergen to Voss: about an hour by direct train | product-marketing.md |

## Do not claim (from product-marketing.md)

- "6 days of skiing" on the 6 Day package. "Ski days" plural on the 7 Day trip.
- Any aurora sighting or guarantee. Guaranteed snow, perfect powder, all gear included.
- Any group size or guide ratio number. Any age limit. The words "small group" without a number are allowed: the hub shows a "Small groups" badge and product-marketing.md lists "small group" as a word to use.
- Scarcity of any kind unless live availability is confirmed.
- A rating without a named source and a current number.
- Beginner positioning on the 3-Day Ski and Snowshoe or the 3-Day Multi-Sport.
- Questions about the viewer's age, fitness, level or status.

## UGC: the same rules, a human voice

Every rule on this page applies in ugc_talk and ugc_text. What changes is who is speaking:

- "I" is fine for the guide or guest on camera. R03 counts I and my with you, against we, our, us and the brand name. The viewer still benefits from every line.
- The person on camera discloses the relationship in the video (D01). A guide is never written as an ordinary guest.
- Humour targets the guide or the weather, never the guest or how hard the day is (BR05).
- "Best day ever" is still a superlative (BR11). Say the moment instead: "my favourite run this season".
- Snow and aurora clips carry a date or "this was" framing, never "every day" or "you will see" (BR09, BR10).
- No trending songs on posts that name us, a trip or a price (SND01).

The full guide, with sources and [VERIFY with counsel] tags, is references/ugc-style.md.

## House style in every script cell

No em or en dashes, no emojis (R01). No capitals for emphasis (R02). No AI vocabulary: delve, tapestry, leverage, robust, seamless, unlock, elevate, game-changer, journey as a noun. No "not X but Y" contrasts, no tricolons, no slogan closers, no "Imagine...", no rhetorical "Ready to...?". The validator does not catch these; the reviewer does.

Numerals for numbers you claim ("2 hours", "NOK 1,948"). Spelling a number out does not hide it: "two" to "nineteen" still count toward the number budget, and "twenty" and up also need a facts row. Only "one" is free.
