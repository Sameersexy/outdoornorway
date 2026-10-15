# Short form playbook: 25 seconds

For Instagram Reels, YouTube Shorts and TikTok. Hard max 25 s, warn above 23 s. Limits in tiers.md.

A 25 s short carries one idea. Sampled travel creators publish 37 to 122 s shorts; our cap is 2 to 5 times tighter. Copy their hook and close, never their middle.

## Pick the style first

Three styles share this tier. Set `style:` in the front matter. A TikTok script sets `style: ugc_talk` or `style: ugc_text` explicitly; a script without the field is `voiceover`.

| | voiceover | ugc_talk | ugc_text |
|---|---|---|---|
| Who | A calm read over edited footage | A guide, staff member or guest talking to the phone | Text on a clip, little or no talk |
| Words per second | 2.4 | 3.0 | n/a |
| Words, hard max (target) | 60 (40 to 55) | 75 (55 to 68) | 12 spoken, zero is normal |
| Hook | Beat 1 ends by 3 s, 4 to 9 words, hard max 10 | First word by 0.5 s, first sentence 6 to 15 words, hook up to 4 s when beat 1 has an overlay | Overlay in beat 1 from frame one |
| Words per beat | 8 to 15, hard max 18 | 10 to 20, hard max 24 | n/a |
| Sentence average (hard max) | 6 to 9 (12) | 7 to 12 (16) | n/a |
| Overlay | 6 words, 32 characters per line | Title up to 8 words, 40 characters per line | 4 to 12 words in the whole script, 40 characters per line |
| Length and beats | 8 to 25 s, 4 to 7 beats of 3 to 6 s | 8 to 25 s, 4 to 7 beats of 3 to 6 s | 7 to 15 s, 1 to 3 beats of 2 to 15 s |
| Call to action | Exactly 1, 8 words, last 4 s | 0 or 1, 10 words, last 5 s, a soft prompt (U05) | 0 or 1, 8 words, last 4 s |
| Facts, numbers | 3 facts, 1 per beat, 2 numbers | Same | 1 fact |
| Beat 1 visual | Motion or a person (H02 warns) | A person, selfie, POV, handheld or hands (U01 blocks) | Same as ugc_talk |
| Disclosure, music | D01 and SND01 by relationship and sound | Same | Same |

tiers.md renders the exact numbers from tiers.json. The structures and hook formulas below are written for `voiceover`. For ugc_talk and ugc_text, use the hook library and repeatable formats in `references/ugc-style.md`; the grids below still work as a starting point once you move the disclosure line into a beat that starts by 5 s.

## Four structures

Pick one per script. Each has its own grid. All of them keep the hard rules: beat 1 ends by 3 s, beats last 3 to 6 s, the loop closes in the last or second-last beat, the cta starts in the last 4 s.

**Outcome-first rewind.** Show the end, then how you got there. Best for a result the viewer wants.

| Beat | Time | Role | Job |
|---|---|---|---|
| 1 | 0-3 | hook, open:A | The end state on screen, the question in words |
| 2 | 3-9 | setup | Rewind to the start: where the guest was |
| 3 | 9-15 | build | The one step that made the difference. One fact |
| 4 | 15-21 | payoff, close:A | Back at the end state, now it makes sense |
| 5 | 21-25 | cta | One ask |

**One real-time scene.** Six short pulses of one moment, no cutaways to explain. Best for a sensory detail or a small surprise.

| Beat | Time | Role | Job |
|---|---|---|---|
| 1 | 0-3 | hook, open:A | Mid-action, a sound or a movement |
| 2 | 3-6 | setup | Where and when, in one line |
| 3 | 6-10 | build | What happens next |
| 4 | 10-14 | shift | The thing nobody expected |
| 5 | 14-19 | payoff, close:A | Why it happened |
| 6 | 19-23 | cta | One ask |

**Guide and guest Q and A.** Two voices: the guest asks what the viewer is thinking, the guide answers. Name the speaker in the visual column, not the voiceover (labels cost words). Best for an objection.

| Beat | Time | Role | Job |
|---|---|---|---|
| 1 | 0-3 | hook, open:A | The guest's doubt, said out loud |
| 2 | 3-8 | explain | The guide's short answer |
| 3 | 8-12 | shift | The guest pushes back |
| 4 | 12-17 | proof | The guide shows it. One fact |
| 5 | 17-21 | payoff, close:A | The guest, convinced, in one line |
| 6 | 21-25 | cta | One ask |

**Loop-back.** The last spoken line runs into the first, so the replay feels continuous. Best for a rule or a habit.

| Beat | Time | Role | Job |
|---|---|---|---|
| 1 | 0-3 | hook, open:A | The rule, mid-sentence |
| 2 | 3-7 | setup | The usual mistake |
| 3 | 7-12 | explain | Why the rule exists. One fact |
| 4 | 12-17 | build | What changes when you follow it |
| 5 | 17-21 | payoff, close:A | The result |
| 6 | 21-24 | cta | A short spoken tail that leads into beat 1; the ask is on the overlay |

Worked loop-back beat 6 (from examples/short-fictional.md, hook "Your guide wants you a little cold."): voiceover "That's why, on every climb," (5 words, role cta), overlay "Send to your overdresser". The replay lands on the hook and completes the sentence. The spoken tail carries no ask; the overlay and caption do. The cta role stays on the beat, so C01 to C04 still apply.

Words: about 40 to 55 in all. Hook 4 to 7 words (6 with narrator slow): at 2.4 words per second, 8 or 9 words need 3.3 to 3.8 s and get a T04 warning in a 3 s beat. 10 words block (H01). With narrator brisk (3.0 words per second) the target is about 50 to 69 words and a 9 word hook fits a 3 s beat.

## Hook formulas

The goal of a hook is interruption: the viewer was about to scroll. Polite hooks lose. Each hook must be paid off by the payoff beat; a hook the video does not answer trains people to scroll. The lines below show the shape. Do not reuse them.

| Formula | Pattern | Shape (illustrative) |
|---|---|---|
| Surprising rule | Your guide wants [unexpected thing]. | "Your guide wants your hands cold." |
| Outcome first | Show the end, then ask how. | "You skied down that. Here's the way up." |
| Specific question | A question about the trip, never about the viewer. | "How do snowshoes not sink?" |
| Small scene | Time, place, one sense. | "Eight a.m. Only the squeak of your boots." |
| Counter-belief | Name a common belief, then test it. Discovery, never "you are wrong". | "Touring looks steep. Watch the pace." |
| Guide confession | A guide admits a habit or a mistake. | "Your guide packs two lunches. Here's why." |
| Visual contradiction | The words say the opposite of the picture. | Over a slow fall into soft snow: "Your favourite part of the day." |
| Honest downside, said with a smile | The real cost, told plainly. | "Your legs will notice tomorrow." |
| The unsaid belief | What the viewer thinks but never heard said. | "You think you'll be the slow one." |

Banned openers: greetings, "in this video", "welcome to", the brand name, a rhetorical "Ready to...?", personal-attribute questions ("Are you a beginner?"). BR01 and BR08 enforce most of them.

A fragment pair in the hook ("Eight a.m. Only the squeak...") is fine even if S01 warns about the average sentence length. Say why under accepted warnings.

## Visual hooks for beat 1

Frame 1 is already moving: one subject, high contrast, readable with the sound off. Pick from the hook library in visuals-and-text.md (grouped by what the frame does: contrast, reaction, mishap, sound-first, overhead, detail, one take). Never a logo, a title card, black, a fade in, or a talking head saying hello (H02 for voiceover). In ugc_talk and ugc_text the first frame must show a person, a selfie, a POV, a handheld shot or hands in action, and no visual cell may name an end card, logo, title card, stock footage, animation, slide or lower third (U01 and U02 block).

## Overlays and captions

- Max 6 words, 32 characters per line, 2 lines. On screen at least 1.5 s.
- Beat 1 always has an overlay: most feed video starts muted.
- An overlay adds a keyword or names the question. It never repeats the voice (O03 warns above 60 percent overlap).
- Burned-in captions are a separate track for sound-off viewers. They are not overlays and do not go in the text column.
- Details in visuals-and-text.md.

## Call to action

Voiceover: the rules below. ugc_talk and ugc_text: 0 or 1 call to action, max 10 words, in the last 5 s, and it should be a soft prompt from tiers.json (save this, send this to, which one, follow along, or one logistics sentence on how to book). A call to action that is only "link in bio" or "comment for the link" warns, and so does an open comment question (U05). Booking links go in the caption.

- Exactly one. Starts in the last 4 s. Max 8 words.
- One verb: send, save, follow, comment, ask, book. Two or more ask verbs in the cta beat get a C03 warning. A booking or link ask in any other beat gets a C01 warning.
- "Send this to..." targets sends per reach, a signal Instagram names as important (B).
- "Book" names the destination ("from the link in bio") and that page must sell the same tour.
- A short holds 2 numbers in all. A price on the cta overlay is 1. A full date with the year is 2 more, so dates go in the caption, backed by a verified facts row (F04 checks caption digits too).
- Never stack asks ("like, follow and book").

## Weak versus strong

| Weak | Why it fails | Strong |
|---|---|---|
| "Hey guys, welcome to Voss!" | Greeting spends the 3 s window | A surprising rule about the guest's day, in 7 words or fewer |
| "Fjords, mountains, snow and amazing views." | Noun list, no stake, no picture | One named thing the guest does there: "You eat lunch on the ridge you just climbed." |
| "Join us for 9 days, 4 resorts, from NOK 42,126!" | 3 numbers in one breath | Trip in the voice, "From NOK 42,126" alone on the CTA overlay |
| "Experience perfect powder on our epic tours." | BR03 words, a snow promise | "The guide picks the slope from this week's snow." |
| "Only for experienced skiers." | Negative framing (BR05) | "For skiers confident on red runs." |
| "Book now, limited spots!" | Scarcity (BR04) | "Day tours every Saturday and Sunday. Link below." |
| Overlay: "Your guide wants you cold" over the same spoken line | Redundant | Overlay: "Why start cold?" |

## Checklist before running the validator

- [ ] Style set. TikTok scripts say `style: ugc_talk` or `style: ugc_text`. `relationship` and `sound` set when they differ from the defaults (staff, original).
- [ ] One idea. Can you say it in one sentence of under 12 words?
- [ ] Beat 1, voiceover: motion, "you", overlay, 7 words or fewer (6 with narrator slow). ugc_talk: a person on camera, first word at frame one, you or I in the first sentence, a title overlay.
- [ ] Disclosure beat starting by 5 s when relationship is staff, guide, guest_paid or guest_gifted (D01).
- [ ] Every number is in a verified facts row cited in that beat. Dates with the year sit in the caption.
- [ ] Every factual line says no more than its fact row.
- [ ] At most 3 facts, 2 numbers, 1 place name.
- [ ] Payoff closes the hook question in the last or second-last beat.
- [ ] Voiceover: one CTA, last 4 s, 8 words or fewer. ugc: at most one soft prompt, last 5 s, 10 words or fewer.
- [ ] Every beat has 2 shots unless it is 3 s or shorter, or one real continuous take marked `one take:`.
- [ ] No line copied from the examples or this page.

## Real Outdoor Norway facts that fit a short

From `campaigns/ski-meta-ads/tours.json` and `.claude/product-marketing.md`. Copy the exact wording into the facts table.

- Backcountry Ski Tour, Beginner to Intermediate: NOK 1,948 per adult, every Saturday and Sunday, January to April.
- Bergen to Voss: about an hour by direct train.
- 7 Day Ski in Fjord Norway and Aurora in Tromsø: aurora only as a possibility (BR10).
- Do not claim: group sizes, "all gear included", "6 days of skiing", beginner level on the 3-day trips.
