# Visuals, overlays, captions and safe zones

The visual column is written first. The voice adds what the picture cannot show. Everything here applies to both tiers and all styles unless a tier or style is named. UGC framing, native text and music rules for `ugc_talk` and `ugc_text` are in the UGC section below and in references/ugc-style.md.

## How to write the visual column

- One shot per idea, separated by " / ". Name a subject and an action: "guide digs a small pit", not "safety".
- Write shots that exist or can be filmed on one shoot day. Mark anything that needs a new shoot in the caption notes.
- Short: a new shot every 3 s at most, never a static shot over 4 s. Long: every 6 s at most.
- A real continuous take (a POV walk, a drone push) is one shot. Start the cell with `one take:` and name the move: "one take: POV, snowshoes step from the road into the forest". V01 then treats it as motion, not a static hold. A one take that names no move gets a warning. Never split one shot into a fake "a / b" to pass V01: the crew will film what you wrote.
- The best shot goes to the payoff, not the hook. The hook gets the clearest motion.
- Do not narrate what the picture already shows. "Here is the fjord" over the fjord wastes words.

## Visual hook library

Voiceover style: beat 1 must show motion or a person. The validator warns if beat 1 names none of: person, skier, guide, hands, POV, drop, skis, walk, hike, pan, drone, glide, snow, boots. It blocks logo, title card, intro, fade in, black screen and a talking-head greeting.

Grouped by what the frame does. Each frame pairs with a hook formula (short-form.md) and a counterpoint: a line that adds what the picture does not say. The lines show shapes; write your own. S works vertical, L works landscape.

| Frame does | Shot | Formula | Counterpoint shape | Tier |
|---|---|---|---|---|
| Motion | POV skis on skins sliding uphill | Specific question | "Your skis are walking. Here's how." | S L |
| Motion | Snowshoes sink, then hold, in deep snow | Specific question | "Two steps and the snow stops winning." | S |
| Motion | one take: drone pushes along a ridge to one small figure | Scale question | "That dot is a guest on day one." | L |
| Two-person contrast | A skier carves past while a snowshoer on the trail waves | The unsaid belief | "Same mountain. Only one of them skis." | S L |
| Two-person contrast | Parent on skis, child on snowshoes, walking side by side | Three people, one trip | "Your kids don't ski. Bring them anyway." | S L |
| Two-person contrast | The guide's calm face beside a guest's red face mid-climb | Guide confession | "Your guide is going slow on purpose." | S |
| Reaction face | A guest's face as the view opens at the tree line | Outcome first | "You'll forget the climb in about a second." | S L |
| Reaction face | A child's face at the first bite of a hut waffle | Small scene | "Lunch is the part the kids talk about." | S |
| Reaction face | A guest laughing in soft snow after a slow fall | Visual contradiction | "Your favourite part of the day." | S |
| Small mishap | A glove slides downhill and a guest chases it | Honest downside | "Clip your gloves. Ask us how we know." | S |
| Small mishap | Snow drops off a branch onto a hood | Visual contradiction | "This is the warm part of the day." | S |
| Sound-first | Dark frame lifting to a headlamp, skins squeaking | Small scene | "Seven a.m. You hear the track before you see it." | S L |
| Sound-first | A thermos lid unscrews at a windy stop, steam rises | Surprising rule | "Your guide stops before you're tired." | S L |
| Overhead group | Drone straight down on a line of skiers and snowshoers | Three people, one trip | "Skis or snowshoes, you share one route up." | L |
| Overhead group | A group eats lunch in a circle on the snow, from above | Small scene | "Lunch is on the ridge you just climbed." | S L |
| Close detail | Hands press a skin onto a ski base | Specific question | "This strip is the whole trick." | S |
| Close detail | Frost on a guest's eyelashes, then a grin | Honest downside | "Your face gets cold. Your feet don't." | S |
| Close detail | Wet boots drying by a cabin stove | Loop-back | "...and that's why your guide wants you a little cold." | S L |

A number in a counterpoint counts toward the numbers budget and needs a facts row if it is a claim. Do not claim a group size; the do-not-claim list bans group size numbers.

## UGC visuals (ugc_talk and ugc_text)

The phone is the camera and a person is the subject. Write every visual cell as who or what is on camera, doing what, from where: "selfie, guide Ingrid walks up the skin track", not "skin track".

| Rule | Severity | What the cell needs |
|---|---|---|
| U01 | block | Beat 1 names a person, selfie, POV, handheld shot or hands in action. The cue list is in tiers.json |
| U02 | block | No cell names an end card, logo, title card, stock footage, animation, slide or lower third |
| U07 | warn | Every cell has 3 or more words and names who or what is on camera |

Framing vocabulary that films well on a phone:

| Framing | Use for |
|---|---|
| Selfie at arm's length, walking | The hook, the name and role line, the call to action |
| Chest POV (phone in a chest strap or pocket) | The skin track, kick turns, the descent, anything with both hands busy |
| Handheld, a colleague filming | The demo, the guest copying it, reactions |
| Tripod or phone propped in the snow | The group passing, a wide reveal, the guide in frame with the group |
| Top-down on the snow | Gear, the pack, the thermos, food |
| Hands in action | Skins on a base, a beacon check, a binding flipped to walk mode |

A talking selfie is one continuous shot. Mark it `one take:` and name the move ("one take: selfie, Ingrid walks up the track talking"), so V01 treats it as motion. Continuous POV runs with zero cuts and fast vlog cutting (3 to 6 cuts per 10 s) both appear in the creators' hits (C); neither is enforced beyond V01.

## Overlays (the text column)

| Rule | Short | Long |
|---|---|---|
| Max words | 6 | 8 |
| Max characters per line | 32 | 42 |
| Max lines | 2 | 2 |
| Min seconds on screen | 1.5 | 2 |
| Reading speed | 15 characters per second | 15 characters per second |

- Beat 1 always has an overlay. Muted viewers decide on the frame and the text.
- An overlay adds or highlights: the question, a keyword, the chapter name, the price in the CTA beat. It never repeats the narration (Mayer redundancy principle, A; the validator warns above 60 percent overlap).
- One overlay on screen at a time. Separate lines with " / " in the text column.
- Digits on screen count as numbers and facts, exactly like spoken ones. Each must be in a verified facts row cited in that beat (F04).
- Sentence case. No capitals for emphasis, no emojis, no dashes.

UGC overlays (native text):

| Rule | ugc_talk | ugc_text |
|---|---|---|
| Title in beat 1 | Up to 8 words, 40 characters per line, 2 lines | The joke or the tip, visible from frame one |
| Total overlay words | No extra limit beyond each overlay | 4 to 12 in the whole script, across one or two lines |
| Case | Sentence or lower case; capitals for emphasis warn (U04) | Same |
| Font and place | In-app font or a lookalike, top third, inside the safe box | Same |

Burned-in captions that mirror the speech stay a separate track in every style.

## Captions

- Burned-in captions are the full transcript for sound-off viewers. Generate them from the final voiceover. They are not overlays.
- Keep captions in the lower part of the safe box, 2 lines max.
- The post caption (the `## Caption` section) adds what the video left out: full dates with the year, price basis, a link. At most 2 hashtags. Its digits are checked too: each must be in a verified facts row (F04).

## Safe zones (vertical 1080 x 1920)

| Platform | Keep text out of | Grade |
|---|---|---|
| Instagram Reels | Top 14 percent (about 270 px), bottom 35 percent (about 670 px), 6 percent each side | B, from the Meta ads spec via summaries. No organic spec exists |
| TikTok | Top 13.2 percent, bottom 36.8 percent, right 22.4 percent, left 11.3 percent | C |
| YouTube Shorts | No official pixel spec found | n/a |

Shared safe box (strictest of the above): x 122 to 838 px, y 270 to 1210 px. It fits about 18 to 24 characters per line at a legible size, which is why short overlays stop at 32 characters over 2 lines.

Long form (16:9): keep text out of the bottom 20 percent in the last 20 s, where end screens sit [VERIFY: YouTube end screen window on support.google.com].

## Sound

- Natural sound is a beat: skins squeaking, wind, a thermos lid. Mark it with [PAUSE n] in the voiceover, n in seconds.
- Music sits under the voice. Drop it for a 2 s sound break at a re-engagement beat.
- Set `sound:` in the front matter: original, commercial_library, voiceover_only, trending or none (default original). `sound: trending` blocks when the script names the brand, a trip or a price (SND01): businesses must use TikTok's Commercial Music Library for commercial posts (A). Commercial Music Library clearance covers TikTok only [VERIFY with counsel]; re-clear music before posting the same file to Reels or Shorts.
