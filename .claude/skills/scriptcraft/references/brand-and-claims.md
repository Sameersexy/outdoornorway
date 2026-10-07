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

- Never promise snow, powder, sunshine, wildlife or the aurora (BR09).
- Any script that mentions the aurora or northern lights must also say it cannot be promised (BR10). The 7 Day trip page says no departure can guarantee an appearance.
- Possibility verbs: look for, wait for, if the sky clears, a chance of.

## Rule summary (brand_rules.json)

| Id | Severity | Catches |
|---|---|---|
| BR01 | block | Greeting or channel intro in beat 1 ("hey guys", "welcome to", "in this video") |
| BR02 | block | End signals and sign-offs ("that's it", "to wrap up", "thanks for watching", "like and subscribe") |
| BR03 | block | Cliche and hype ("winter wonderland", "breathtaking", "magical", "epic", "stunning", "bucket list", "adrenaline", "perfect powder", "seamless", "nestled", "majestic") |
| BR04 | block | Scarcity and urgency ("few spots left", "last chance", "hurry", "don't miss out") |
| BR05 | block | Negative framing of difficulty ("only for experts", "brutal", "survive", "extreme") |
| BR06 | block | Company-speak ("Outdoor Norway offers", "our guests", "guests will", "we are proud") |
| BR07 | warn | Sales verbs before the CTA ("we offer", "book today", "secure your spot") |
| BR08 | warn | Personal-attribute address ("are you a beginner", "scared of", "are you over") |
| BR09 | block | Guarantee wording near aurora, snow, powder, weather, wildlife |
| BR10 | block | Aurora mentioned with no possibility line |
| BR11 | block | Superlatives ("best", "biggest", "ultimate", "world's", "#1") without a facts row that contains the same word |
| BR12 | warn | A date with no year anywhere in the script |
| BR13 | block, --final only | A placeholder ([VERIFY], [TODO], [TBD], [LINK]) still in voiceover or overlay |
| BR14 | warn | Possible exclusivity claim ("only", "most", "first", "nobody else"). Ordinary use like "your first tour" is fine; reword to avoid the warning |

The full phrase lists are in the JSON. Read them before writing, not after the validator complains.

## Facts and [VERIFY]

- Facts come only from: tours.json, product-marketing.md, a page URL the user names, or the user in writing. Never from memory.
- Each fact is one row: id, the fact with the number exactly as spoken, the source, verified yes or no.
- Every digit spoken or shown must appear in a row with verified yes (F04). Unverified rows are allowed in a draft and block with --final.
- Prices: "from NOK X" for multi-day trips, "NOK X per adult" for day tours. Never "per person" until confirmed.
- Dates in full with the year: "30 Jan to 7 Feb 2027".
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
- Any group size or guide ratio number. Any age limit.
- Scarcity of any kind unless live availability is confirmed.
- A rating without a named source and a current number.
- Beginner positioning on the 3-Day Ski and Snowshoe or the 3-Day Multi-Sport.
- Questions about the viewer's age, fitness, level or status.

## House style in every script cell

No em or en dashes, no emojis (R01). No capitals for emphasis (R02). No AI vocabulary: delve, tapestry, leverage, robust, seamless, unlock, elevate, game-changer, journey as a noun. No "not X but Y" contrasts, no "Imagine...", no rhetorical "Ready to...?". Numerals for numbers.
