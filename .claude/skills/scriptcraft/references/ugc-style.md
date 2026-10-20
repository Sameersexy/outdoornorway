# UGC style: a guide, a phone and one idea

Read this before any TikTok script, and before any script with `style: ugc_talk` or `style: ugc_text`. Numbers come from three research notes dated 2026-10-07: the top five UK and US individual creators (note 04), micro creators who guide, teach, patrol or travel (note 05) and TikTok mechanics and rules (note 06). Every measured number is grade C (our own small sample) unless it says otherwise. Every limit lives in `scripts/tiers.json`; this page explains them.

## What UGC means here

User-generated content, made by our own people. A guide, a staff member or a real guest films on a phone, holds it at arm's length or clips it to a chest strap, and talks the way they talk. First person, handheld, selfie or POV, natural light, native TikTok text. No crew, no logo, no end card, no brand typeface.

It is not a voiceover film shot to look cheap. The viewer should feel they are watching a person, not a company. TikTok's own creative guidance says the same thing: feature people (creators, employees, customers), go lo-fi, use the creator's own voice (grade A). Lo-fi is not low quality: film at 720p or better, in good light, with the mic near the mouth (grade A, 2021 data).

What does not change: one idea per video, the fact and number limits, and every brand rule. The research found that creators talk faster, but the extra speed is connective talk (so, and then, here's the thing), not more facts. Micro creators carry 0.4 to 2.7 numerals per 30 s; our cap of 3 facts in 25 s is already above all of them.

## The three styles

Set the style in the front matter. A TikTok script sets `style: ugc_talk` or `style: ugc_text` explicitly; leaving it out means `voiceover`.

| Style | What it is | Use it when | Tiers |
|---|---|---|---|
| `voiceover` | The original scriptcraft film: a calm read over edited footage | Brand films, Reels and Shorts cut by an editor, every YouTube landscape video | short, long |
| `ugc_talk` | A person talks to the phone or over their own clips, first person | A guide explains one thing, answers a guest question, shows a place or tells one moment | short, long |
| `ugc_text` | Little or no talking. One or two lines of on-screen text over a clip that loops | A relatable joke, a tip that reads in one glance, a silent day-in-the-life | short only |

Pick `ugc_text` more often than you think. Of the 15 TikTok videos over 100k views in the micro-creator sample, 10 had no scripted creator voice (C, n = 15). Creator D's 21 s text-only tips post reached 528,500 views and 9,592 saves; her talk posts sat at 700 to 2,000.

Other front matter fields, all optional:

| Field | Values | Default | What it drives |
|---|---|---|---|
| `creator` | guide, guest, staff, editor | guide | Who is on camera or filming. Recorded in the report |
| `relationship` | staff, guide, guest_paid, guest_gifted, guest_unpaid | staff | The disclosure rule D01 |
| `sound` | original, commercial_library, voiceover_only, trending, none | original | The music rule SND01 |

An invalid value is a parse error (exit 2) naming the line. `ugc_text` with tier long is a parse error too.

## How creators actually speak

| Measure | Top five (note 04) | Micro creators (note 05, 06) | Our rule |
|---|---|---|---|
| Words per second, full clip | 3.3 to 4.9 for the talkers. Medians: Creator A 4.18, Creator C 3.95, Creator D 3.73 | Pooled spoken median 2.87 over 49 videos. Talking clips of 45 s or less: median 3.46 (n = 6) | ugc_talk short 3.0, long 2.8 (tiers.json, J) |
| First word | 0.0 to 0.4 s | 0.0 to 0.1 s in 5 of 6 short clips | First word by 0.5 s (H01) |
| Words in the first 3 s | 10 to 15 (medians 11.6 to 13.0) | 8 to 11 in short clips | First sentence 6 to 15 words, hook hard max 15 (H01) |
| Casual markers | About 0.5 to 1.6 per 100 words. "So" is the only frequent one | Fillers (um, uh, like) only in improvised videos, which did not get the spoken hits | Warn above 2 per 100 words (U06) |
| Contractions | 1.0 to 3.8 per 100 words | Not measured | Warn below 1 per 100 words (U06) |
| You versus I | Mostly I in stories, mostly you in the practical hits (Creator C's tour 11 you to 3 me) | You share median 0.38; instructors 0.5 to 0.67 | Hook says you or opens on a first-person stake (U03) |
| Facts | One concrete detail per beat, said casually | 0.4 to 2.7 numerals per 30 s | Unchanged: 1 per beat, 3 per short, 2 numbers (F01 to F03) |

Why 3.0 and not 4: the measured rate counts connective talk that adds no information, our guides are often non-native English speakers, and the footage needs silent action gaps (a kick turn, a laugh, the sound of skins). At 3.0 words per second a 25 s short holds 75 words at most and targets 55 to 68.

How to sound like a person without faking it:
- Start mid-thought, at frame one. No greeting, no "so today".
- Use contractions: I'm, you're, it's, that's, don't. A script with none reads like a press release.
- One "so" or "honestly" in a short is plenty. "Okay so literally" in every beat reads fake (U06 warns).
- Never script um or uh. Never script a guest's words: write the question the guide asks and let the guest answer.
- Sentences of 7 to 12 words on average, hard max 16 (S01). Spoken run-ons are fine on camera; in a script they turn into lectures.
- Let the guide say it their way on the day. The script fixes the hook, the facts, the disclosure line and the call to action. The rest is talking points (see the creator brief in `assets/creator-brief-template.md`).

## Hook library

The hook in UGC is three things at once: the first frame, the first sentence and the title overlay. Each format below lists the creator who showed it, a paraphrased shape (never copy it), its word count and the first frame. Rule ids in brackets.

| Format | Seen in | Shape (paraphrased) | Words | First frame |
|---|---|---|---|---|
| Expectation flip | Creator A, Japan in September | "Everyone pictures Norway in winter as dark all day. This is noon." | 12 | Selfie at the trailhead, bright slope behind, breath steaming |
| The statement hook | Creator D, beginner as an adult | "Learning to ski tour as an adult is a very good idea." | 11 | Talking to the phone on the skin track, group passing behind |
| Reveal tour | Creator C, ski hostel tour | "This is where you sleep after a touring day, and it's not a hotel." | 14 | Selfie at the cabin door, a hand pushing it open |
| Someone asked me | Creator C, toy question | "Someone asked me what I wear under my shell, so here it is." | 13 | Phone at arm's length, the base layer held up to the lens |
| Reply to a comment | Creator C, chalet story | Reply sticker on screen, then "You asked if you'd hold the group up. Watch this." | 10 | Reply sticker over the guide filming the group on the skin track |
| Myth bust | Creator F, bend the knees | "Everyone tells you to lean back in deep snow. I tell guests the opposite." | 14 | Side shot of a skier in soft snow, the myth as the overlay |
| POV | Common on TikTok, not used by our five, so unmeasured | Overlay only: "pov: your guide stops for a layer check" | 8 on screen | Chest POV, guide's raised pole in frame |
| Tips list | Creator D, five ski tips | Overlay: "three things I check before every tour" | 7 on screen | Hands opening a pack on the snow, top-down |
| Text meme loop | Creator B, before and after lunch | Overlay: "me telling the group it's one more kick turn" | 9 on screen | Chest POV on a switchback, the group below looking up |

Rules that apply to every row:
- The first frame shows a person, a selfie, a POV, a handheld shot or hands in action (U01 blocks otherwise). Name it in the visual cell: "selfie", "chest POV", "hands", "guide".
- The hook says you or your, or opens on a first-person stake: I, I'm, my, we (U03 warns if neither).
- Pay the hook off in the video. A reveal that never reveals trains viewers to scroll.
- A number in the hook counts. "Three things" spelled costs one of your 2 numbers; "3 things" as a digit also needs a facts row cited in that beat (F04).
- Banned openers stay banned in every style: "hey guys", "welcome back", "in this video" (BR01). A name and role line after the first sentence is fine and doubles as disclosure: "I'm Kari, I guide ski touring in Voss."

## Repeatable formats for guides

From note 05, section 5. Word counts assume a 25 s short at 2.8 words per second; our ugc_talk cap is 75 words at 25 s. Styles in the last column.

| Format | Seen in | Beat structure (seconds) | Spoken words | Filming note | Style |
|---|---|---|---|---|---|
| One fix I give every guest | Creator F, Creator L | 0 to 3 name the mistake. 3 to 15 demo with one cue. 15 to 21 why, one line. 21 to 25 question to comments | 45 to 60 | Selfie or chest mount at the start, then a colleague films the demo from below. One take per cue | ugc_talk |
| Myth bust | Creator F, Creator E | 0 to 3 state the myth. 3 to 12 what actually happens, shown. 12 to 21 the replacement cue. 21 to 25 ask what else they were told | 45 to 60 | Myth as the overlay so it reads muted | ugc_talk |
| Day in the life of a guide | Creator G, Creator D | 4 to 6 clips of 3 to 5 s: van, avalanche gear check, group skinning, the top, dinner. One overlay per clip | 0 to 15 | Phone in a chest pocket. Vertical. Natural sound | ugc_text |
| Snow report from the guide | Creator I, Creator H | 0 to 3 date and place. 3 to 15 what it looks like now, pole in the snow. 15 to 22 what we do today. 22 to 25 sign-off line | 35 to 55 | Same spot and same opener every time. Measured depth only. Never forecast (BR09) | ugc_talk |
| What guests ask me | Creator F, Creator K | 0 to 3 the question on screen. 3 to 20 the answer with footage. 20 to 25 ask the next one below | 40 to 55 | TikTok reply-to-comment. Real questions only | ugc_talk |
| What is in my guide pack | Creator L, Creator H | 0 to 3 open the pack. One item per 4 s beat: beacon, shovel, probe, first aid, thermos. Last beat the why | 40 to 55 | Top-down on snow. Item name as overlay, 1 to 2 words | ugc_talk or ugc_text |
| Real moment, then the lesson | Creator K, patrol call | 0 to 10 real footage, no talk. 10 to 22 what to do, 2 steps. 22 to 25 save this | 25 to 40 | Only if nobody is hurt and everyone shown agrees. Never stage danger | ugc_talk |
| Series counter | Creator D, day 4 of 100 | Overlay "guide season day 12" at 0.0 s. 3 to 5 clips. One caption line | 0 to 10 | The number must be true and continue. It is a digit, so it needs a facts row (F04) | ugc_text |
| First-timer guest moment | Creator C, Creator J | 0 to 3 the guest says what they feared. 3 to 18 the run. 18 to 25 the guest's reaction in their words | 20 to 45, guest speaks | Written consent. The guest's words, never ours | ugc_talk |
| Place in 20 seconds | Creator M, Creator C | 0 to 3 where we ski on day 2. 3 to 20 three shots, one fact each. 20 to 25 question | 45 to 55 | Walk and talk, phone at arm's length | ugc_talk |
| Long: one day, start to finish | Creator M, Creator K | Hook 0 to 10, 4 to 6 chapters of 25 to 40 s, close on the group | 400 to 520 | Landscape. The guide narrates live, not in post | ugc_talk, long |

Where a format ends on a comment question, phrase it as a choice ("which one would you pack first?") or a save or send prompt: U05 accepts only the soft prompts listed in tiers.json, and an open comment question warns. A beat structure here is a starting grid. The validator still checks beat count (4 to 7 in a short), beat length (3 to 6 s), words per beat (ugc_talk 10 to 20, hard max 24) and the loop.

## ugc_text in one table

| Limit | Value | Rule |
|---|---|---|
| Video length | 7 to 15 s | T01 |
| Beats | 1 to 3, each 2 to 15 s | B01, B02 |
| Spoken words | 0 to 12, zero is normal | W01 |
| Overlay | 4 to 12 words in the whole script, across one or two lines | O01 |
| First overlay | In beat 1, visible from frame one | O04 |
| Loop | open:A in beat 1, close:A in the last beat | L01 |
| Call to action | 0 or 1, at most 8 words, in the last 4 s | C01 to C03 |
| Facts | 1 at most | F02 |

The joke or the tip lives in the overlay. The picture does the payoff: the landing, the view, the steam off the thermos. Built to loop, so the last frame should cut back into the first.

## Native text

- ugc_talk: one title overlay in beat 1, up to 8 words and 40 characters per line, 2 lines (O01). Later overlays are optional keywords.
- Burned-in captions that mirror speech are a separate track, made in the app or the editor. They are not overlays and do not go in the text column.
- Sentence case or lower case. No capitals for emphasis (U04 warns, R02 applies everywhere). No emoji, no dashes (R01).
- In-app font or a lookalike, never the brand typeface. White with a soft shadow, top third, inside the safe zone in `references/visuals-and-text.md`.
- An overlay adds to the voice. It never repeats it word for word (O03).
- TikTok's guidance mentions "5 to 10 words per second" for text. We read it as caption pacing, not an overlay length, and do not enforce it [VERIFY exact wording].

## What fails

| Pattern | Evidence (C unless marked) | Rule that catches it |
|---|---|---|
| Long sincere monologues | Creator D's talk posts 700 to 2,000 views; her silent tips post 528,500 | Words and beat limits (W01, W03, T01) |
| Ad-style product stories and unboxings | Creator C's AD posts 441 to 3,191 views against 312,600 for her practical tour. Creator E's gifted unboxings 82 to 386 | Reviewer authenticity check; BR07 sales verbs |
| Selling early | Creator F's course pitch videos underperformed their tips by about 40 to 200 times | C01 (ask outside the cta beat), BR07 |
| Greetings and channel intros | "Welcome back" openers sat on Creator E's lowest videos | BR01 |
| End cards, logos, title slides | No creator measured in notes 04 and 05 used one | U02 |
| Spoken list dumps | Lists worked only as on-screen text | F01 to F03, ugc_text |
| Garbled audio | Wind and music made several captions unusable | Filming note: mic near the mouth |
| No reason to stay | Silent hits escalate (more snow, steeper, the landing); a talk with no payoff does not | L01 loop open and close |

## Brand rules and authenticity, together

Every brand rule applies in every style. The table shows how to keep the human voice inside them.

| Authentic cue | Brand rule | How to keep both |
|---|---|---|
| First-person hook ("I nearly turned back on my first tour") | Guest first | Allowed when it names a stake, a situation or a mistake (U03). R03 then counts I and my on the guest side, against we, our, us and the brand name |
| Name and role intro | No greetings (BR01) | "I'm Kari, I guide in Voss" after the first sentence. "Hey guys" stays blocked |
| Casual words | Clean voice | One or two per short (U06). Never um or uh |
| Self-deprecating humour | No negative framing of difficulty (BR05) | Joke about the guide or the weather, never about the tour being hard or the guest failing. "My legs were jelly" is fine. "This is brutal" is not |
| Ski slang | Cliche list (BR03) | Slang the audience uses is fine. Marketing cliches (winter wonderland, hidden gem, bucket list) stay blocked |
| "Best day ever" | No unsupported superlatives (BR11) | Rewrite as a plain personal moment: "my favourite day this season". BR11 does not read intent, so "best" still needs a sourced row |
| Aurora excitement | No aurora guarantees (BR09, BR10) | Show it when it happened, with the date. "We got lucky that night." Never "you will see". Say it cannot be promised |
| Fresh snow | No snow guarantees (BR09) | Date the clip. "This was Tuesday", never "every day looks like this" |
| No logo | Brand recall | The brand appears through the disclosure line, a jacket worn naturally and the caption tag |
| Scarcity in slang | No scarcity (BR04) | "Spots are going fast" is blocked in every style. Real departure dates go in the caption |

Never let staff appear as ordinary guests. A guide never says "I booked this trip". Posing as a consumer is a blacklisted practice under EU consumer law (UCPD Annex I, point 22, grade B) [VERIFY with counsel].

## Disclosure (D01)

| relationship | Who | Validator | What to do |
|---|---|---|---|
| staff | Office or ops staff posting about the company | Warn if no disclosure beat in the first 5 s naming the role or the brand | A beat with role `disclosure` starting by 5 s: "I work at Outdoor Norway" in the voice or the overlay |
| guide | A guide posting about trips they guide | Same warning | "I guide for Outdoor Norway" in the voice or the overlay, by 5 s |
| guest_paid | A guest paid to post | Block without both: caption starts with Ad, #ad, Advert, Advertisement, Reklame or Annonse, and a `disclosure` beat starting by 5 s that says so (ad, paid, sponsored, gifted, free trip, reklame and the other paid_words in tiers.json) | Say it and show it: "Ad. Outdoor Norway paid me to film this trip" |
| guest_gifted | A guest given a discount, upgrade, gear or a free trip | Same block | "Ad. I got this trip free from Outdoor Norway" |
| guest_unpaid | A guest who posts on their own, unasked and unrewarded | No requirement | Still no staff-written lines. If we later boost it as a Spark Ad, it becomes advertising and needs the label |

The sources behind it:
- FTC (US, A): disclose any financial, employment, personal or family relationship, in the video, not only the description; early; spoken and on screen together works best. Employees should disclose.
- ASA and CAP (UK, A): a prominent "Ad" label upfront. Owners and employees are covered. "Sponsored" or "gifted" alone is unlikely to be clear. A bio note is not enough.
- Forbrukertilsynet (Norway, A): anyone given a benefit to post must label. "Reklame" or "annonse" are always clear; in English, "advertisement". It advises against "ad", "sponset" and "i samarbeid med", and says the platform label alone is not enough [VERIFY with counsel].
- TikTok (A): the content disclosure toggle is required when you promote your own business, product or service ("Your brand"), and for third-party branded content ("Branded content"). Which one a guide uses about their employer is unclear [VERIFY with counsel].

Outdoor Norway is a Norwegian trader, so Norwegian law likely applies whatever the audience [VERIFY with counsel]. The validator enforces the floor: Ad, #ad, Advert, Advertisement, Reklame or Annonse first in the caption, and a disclosure beat starting by 5 s. The safer wording for a Norwegian trader is "Advertisement" first in the caption and on screen, and the validator accepts it; confirm with counsel which word to standardise on. Turn on the TikTok toggle for every staff, guide, paid or gifted post.

The disclosure beat does not need to be its own beat. Beat 2 can carry `disclosure, setup` if it starts by 5 s and the role line is in its voice. Put the same role line on screen too, in 2 to 5 words ("Ingrid, Brekke guide"): many viewers watch muted and the FTC and ASA want the disclosure seen, not only heard. D01 warns when the beat has no overlay. In ugc_text the line may be up to 6 words and does not count against the 2 content lines, unless it sits on the hook beat.

## Music (SND01)

| sound | Means | Validator |
|---|---|---|
| original | The creator's own voice and natural sound | Pass |
| commercial_library | A track from TikTok's Commercial Music Library | Pass |
| voiceover_only | Voice with no music | Pass |
| none | Silent or natural sound only | Pass |
| trending | A trending song from the general library | Block when the script names the brand, a trip or a price |

TikTok (A): the Commercial Music Library is a pre-cleared library of about 1 million songs, and businesses cannot use the general music library for commercial use. A guide's personal post about the company is commercial content, so trending chart audio is out even on a personal account [VERIFY with counsel]. CML clearance covers TikTok only, not Reels or Shorts [VERIFY with counsel]: strip the track and re-add music cleared for that platform before cross-posting. Natural sound (skins, wind, boots on snow) is the most native option and carries no licence risk.

## Guests on camera: consent

- Written release before filming a guest as the subject, with separate tick boxes for organic posting, staff personal accounts, paid ads and other platforms. Right to withdraw, with a named contact. Norway's image right (Åndsverkloven section 104) and GDPR both apply [VERIFY with counsel].
- Minors only with a guardian's written consent [VERIFY with counsel].
- Never film injured or distressed guests. Faces off if in doubt.
- Background people in a wide shot are lower risk but still personal data. Ask the group at the trip briefing and offer a no-camera band [VERIFY with counsel].
- Before boosting any post as a Spark Ad, get a written reuse release and make sure the label is already on: the caption locks once authorised (B) [VERIFY with counsel].
- Guest proof lines are never scripted. The script writes the question; the guest answers in their own words.

## Safety on camera

TikTok removes risky acts by non-professionals that could be imitated and cause harm, and allows professionals doing extreme sports with warning labels (A, Community Guidelines 2026 H2). Guides are the professionals; frame every off-piste or touring clip as guided practice.

- Avalanche gear visible in any off-piste clip: beacon, shovel, probe. Guide in position, spacing on slopes.
- No closed terrain, no cliff drops or jumps with guests, no skiing over people, no helmets off in moving shots.
- Never show a guest doing something unguided in avalanche terrain.
- No "send it", "full send", "no risk" or "totally safe".
- Do not repost other creators' clips; reused clips with other watermarks are not eligible for the For You feed (A).

## Which rule enforces what

| Rule | Style | Severity | Checks |
|---|---|---|---|
| U01 | ugc_talk, ugc_text | block | Beat 1 visual shows a person, selfie, POV, handheld shot or hands in action |
| U02 | ugc_talk, ugc_text | block | No end card, closing card, logo, title card, stock footage (stock drone footage too), animation or animated map, price or title graphic, slide or lower third in any visual cell |
| U03 | ugc_talk | warn | The hook says you or your, or opens on I, I'm, my or we |
| U04 | ugc_talk, ugc_text | warn | No capitals for emphasis in overlays |
| U05 | ugc_talk, ugc_text | warn | The call to action is a soft prompt from tiers.json (save this, send this to, which one, follow along, or a logistics line pointing to the caption or, on YouTube, the description, such as "dates are in the caption"); link in bio alone warns, in any beat |
| U06 | ugc_talk | warn | Casual markers above 2 per 100 words, contractions below 1 per 100 words |
| U07 | ugc_talk, ugc_text | warn | Each visual cell has 3 or more words naming who or what is on camera |
| D01 | ugc_talk, ugc_text; voiceover when relationship is written | block or warn | Disclosure, see above |
| SND01 | all styles | block | sound trending with the brand, a trip or a price in the script |
| R04 | all styles | warn | Two distinct 5-word runs (a copied sentence of 6 words or more) in the voiceover, two in the visual and overlay cells, or 3 shots that restate shots from `examples/` or `assets/`. Needs a file path; `--no-example-copy` skips it for the validator's own tests |
| R03 | all styles | warn | You plus I against we, our, us and the brand name (ugc); you against company words (voiceover) |
| F04 | all styles | warn, block with --final | Every digit in a beat is in a facts row that beat cites |

Run `python3 -I scripts/script_check.py --explain U05` for what a rule counts and the usual fix.
