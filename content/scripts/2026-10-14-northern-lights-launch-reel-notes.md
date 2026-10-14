# Northern Lights launch reel (Instagram): notes

Script file: `content/scripts/2026-10-14-northern-lights-launch-reel.md`

## Status

Brief
- Platform: Instagram Reel, 9:16, front matter `reels`. Tier short, style voiceover, creator staff, relationship staff, sound original, narrator standard.
- Takeaway: a northern lights trip now comes in more than one length.
- Tour: ski-aurora-7day (the 7 day trip), plus a Northern Lights day tour and multi-day tours that are named in the owner's brief only.
- Objection answered: is a full week the only way to go for the northern lights?
- The owner asked for 30 to 35 s. The short tier caps at 25 s and changing tiers.json is the owner's call. The script is declared at 24 s, so it is a valid short. The 30 to 35 s path is in "Extending to 30 to 35 s".

Validator runs on the script file (draft, strict, final)
- Plain: RESULT: PASS (0 blocking, 3 warnings). 51 words, estimated 21.6 s, declared 24 s, 6 beats, 3 facts, 1 number.
- Strict: RESULT: FAIL (0 blocking, 3 warnings). The three warnings below, nothing else.
- Final: RESULT: FAIL (3 blocking, 0 warnings). The same three F04 lines. The script carries no [VERIFY] marker, so BR13 has nothing to block. All open [VERIFY] items are in this notes file.
- `--open-items` on the script: 0 placeholders, 1 unverified fact row (F1).
- Warnings kept, all F04 and all from one cause: F1 is verified no because tours.json says its itinerary is not yet confirmed. The lines are "beat 2: number only in an unverified fact row" (the 7 in "7 day"), "caption: number only in an unverified fact row" (the 7 in the caption) and "fact used but not verified yes: F1". They stay until the owner confirms the itinerary; then F1 goes to yes with that confirmation quoted in the source cell.
- Isolation check, rerun after the second revision: a throwaway copy outside the repo with only the F1 verified cell set to yes prints RESULT: PASS in plain, strict and final, with no warning or blocking lines, so F1 is the only thing the validator holds open.

Length note. The voiceover is about 21.6 s at the validator's pace. The cut runs 24 s: the extra 2.4 s is the pause after the last word and the end card hold. The seconds field is the real declared end and was not adjusted to pass.

What passing does not cover. The script says only what the facts table holds, and F1 is verified no, so beats 2 and 3 rest on an itinerary the owner has not confirmed. The day tour and the other multi-day tours have no facts beyond "launched", so the script names them and states nothing else about them, and beat 5 says only that the day tour is the shorter choice. It is not ready to film or post until the open items below are closed, the itinerary, footage and the bio link first.

Revision after review, second round (51 words, 24 s, same three F04 warnings)
- Beat 1: the hook is now "Which northern lights trip fits you?" (6 words). A reviewer said the old hook did not name the subject to a cold viewer. The new one names it, has "you" and fits the 3 s window. The hooks tried and dropped are under "Hook variants".
- Beat 3: now "You ski one day, and other nights you look up." A reviewer said the old line joined the ski day and the night hunt into one evening. F1 has the ski on one day and the aurora trips on other days, so the line keeps one ski day and puts the night search on other nights.
- Beat 4: the voice now ends "No tour can." A reviewer read the old second sentence as a slogan tag. "No tour can" is F4. The overlay is unchanged.
- Beat 5: "Northern Lights" is capitalised, as F2 and beat 2 write it.
- Caption: sentence one now reads "a Northern Lights day tour, the 7 day Northern Lights tour and other multi-day tours", with the same capitals as the voice. The product naming is an open item for the owner.
- Validator: the hook lost one word, so 51 words and an estimated 21.6 s. No new warning.

Earlier round (seven findings, 52 words): the F1 source cell lost a person's name, beat 3 made the guest the subject, beat 4 became the one team line with a new overlay, beat 5 named the day tour, and beat 6 says "your tour".
Concept C was cut to one idea, and the caption, variants, pointers and beat maps followed the new lines.

## Concepts

### A. More than one length (the validated script)

- Takeaway: a northern lights trip now comes in more than one length.
- Hook (6 words): "Which northern lights trip fits you?" Overlay "Just launched" (F2). It names the subject, speaks to the viewer with "you" and names no place.
- Beat map:
  1. 0 to 3 s, hook: guests walk across snow in the evening, stop and look up. Opens the loop on which trip fits the viewer. The overlay cites F2.
  2. 3 to 7 s, setup and disclosure: "One way is the 7 day Northern Lights tour." "One way" tells the viewer there is another and does not answer the hook. Overlay "We work at Outdoor Norway" names the relationship in first person (F1).
  3. 7 to 12 s, build: "You ski one day, and other nights you look up." The viewer is the subject, the ski day stays one and the night search sits on other nights, so the line does not join the two into one evening. The wording follows F1 ("a ski day", "aurora observation", "an aurora hunting trip at night"). Ski turn, then a wide shot of figures crossing a snowy field after dark (F1).
  4. 12 to 16 s, shift: "We can't promise the lights. No tour can." This is the team line, and "No tour can" is F4. Overlay "Needs clear sky / and aurora activity" gives the two conditions from F4 that the voice does not say.
  5. 16 to 20 s, payoff: "Can't spare a week? Take the Northern Lights day tour." The day tour is held back to this beat, so the loop closes on something new that the table supports (F2). The gain is a shorter way to go. More than that needs day tour facts.
  6. 20 to 24 s, call to action: "Find your tour at the link in bio."
- End card (3 words): "Northern lights tours". The multi-day tours are carried in the caption only (F3), so the voiceover and the card stay inside the 3 fact cap.
- Instagram fit: the question and the motion sit in the first 3 s, the text works on mute, one call to action, no price on screen.

### B. One night or one week

- Takeaway: a northern lights trip can be one day or seven.
- Hook (8 words): "Your northern lights trip, one day or seven?"
- Status: concept only. It needs facts about the day tour that nobody has supplied, so it cannot be written as a passing script yet.
- Beat map (contrast cut, one place name):
  1. Hook: split cut between a short evening outing and a ski slope, overlay with the one place name.
  2. Day tour: what it is and where it starts. [VERIFY: day tour start point, duration, start time and inclusions, owner confirms]
  3. The week: 7 days with a ski day and an aurora hunting trip (F1).
  4. Honesty line: no tour can promise the lights (F4).
  5. Payoff: you pick the length.
  6. Call to action: link in bio.
- The one place name: [VERIFY: which single place name the cut uses and whether the day tour starts there, owner confirms].
- End card (4 words): "One day or seven".
- Instagram fit: the cut reads well on mute and the contrast is the hook. The weakness is that the day half is generic until real day tour footage exists.

### C. Guide to camera (creator brief)

- Takeaway: a guide says, in their own words, why no northern lights tour can promise the lights.
- Hook (7 words): "Are you planning a northern lights trip?"
- Outline (one paragraph): style ugc_talk, creator guide, relationship guide, sound original. One selfie take outside on a real evening, the guide walking and talking to the phone. The disclosure beat names the guide's role by 5 s. The guide's lines come only from the guide's own answers to `.claude/skills/scriptcraft/assets/guide-moment-intake.md`: each answer becomes a facts row with the guide's words quoted, and nothing is written for them. The facts allowed are F4 plus whatever the guide supplies in writing, and the 3 fact cap still applies. The loop is the honest odds: it opens on the question and closes when the guide says why no tour can promise the lights. The launch is left to the other scripts. When the owner picks C, a creator brief is written for the person filming.
- Closing overlay (6 words, text on the last frame, since ugc names no end card): "Northern lights tours, link in bio".
- Instagram fit: a person talking to camera is native to the feed, and it carries the most trust. It is the slowest to make because it depends on a guide being on location and on release forms.

## Recommended

Concept A. It is the only one that can be written today. It passes the validator in draft, with F1 waiting on the owner's itinerary confirmation, it covers the owner's three products (the 7 day tour and the day tour in the voice, multi-day tours in the caption), and it leaves the aurora promise out. B is the next idea to write once the day tour facts exist. C is the follow-up once a guide has a real evening to describe.

Caption (also in the script file):
We're Outdoor Norway, and we've launched a Northern Lights day tour, the 7 day Northern Lights tour and other multi-day tours. No tour can promise the northern lights, because they depend on the sky. The 7 day tour is from NOK 41,181. Details at the link in bio. #northernlights

Hook variants (checked against the current beats 2 to 6 on throwaway copies outside the repo with F1 set to yes; strict counts a warning as a fail)
- Kept as the A/B variant: "Is a week your only aurora trip?" (7 words, same slot). Hypothesis: "aurora" names the subject outright in the first 3 s, and the question comes straight from the objection line, so it is worth testing against the open question. A strict run passes (52 words, estimated 22.1 s).
- Dropped: "Northern lights: a week or a day?" (7 words). It has no "you" or "your" in the first 3 s, so H03 warns.
- Dropped: "Northern lights: do you have a week, or a day?" (10 words by the validator's count, 55 words in all). Beat 1 needs 4.2 s for the 3 s window. T04 and H01 fail, and T02 and W02 warn.
- Dropped: "Do you have a week for the northern lights?" (9 words, 54 words in all). Beat 1 needs 3.8 s for 3 s. T02, T04 and W02 warn.
- Dropped: "Is a week your only northern lights trip?" (8 words, 53 words in all). Beat 1 needs 3.3 s for 3 s. T02, T04 and W02 warn.

Variant: call to action "Pick your length at the link in bio." Hypothesis: "length" echoes the question the video opened with, so it should bring more link taps from viewers who stayed for the day tour line, with 8 words and the same slot. A strict run on a throwaway copy with F1 set to yes passes.

Assumptions
- Relationship staff and sound original, narrator standard, because nobody could be asked. The brief gave no on-camera guide.
- "we launched not the lights tour" in the brief is read as "we launched the Northern Lights tour", meaning ski-aurora-7day. F1 quotes the owner's own words and does not use the cleaned paraphrase. [VERIFY: owner confirms this reading]
- F1 is one row and verified no as a whole. The 7 days is in tours.json (days 7) and the hub heading, but the inclusions come from an itinerary that tours.json marks not yet confirmed. Splitting the row into a verified length and an unverified inclusions row would make 4 facts across the script (F1, the new row, F2, F4) and F02 caps it at 3.
- The day tour is a separate product from the 7 day trip, and "multi-day tours" means more than the 7 day trip. The script says only that they have launched.
- "30 seconds 35 seconds at max" is read as a hard ceiling of 35 s, not a target.
- Visuals are generic shots taken from the 7 day itinerary (the ski turn) and from night scenes. Beat 2 uses generic night shots and beat 5 generic group shots, because no day tour footage is known. Beat 3 no longer shows dog sledding or the private boat, because the new line does not mention them.
- The word "cold" and the word "snow" are not in the voice. The facts table has no weather or temperature row, so they stay in the visuals (breath steaming, packed snow, winter jackets). If the owner accepts them as plain description, "You ski one day, and other cold nights you look up." fits with the declared length kept at 24 s (a throwaway copy with F1 set to yes passes strict at 52 words, estimated 22.1 s). [VERIFY: owner decides]
- Beat 5 reads the day tour as the shorter choice because it is a day tour. It says nothing about what the day tour includes, where it starts or whether it goes out after dark.

## Instagram pointers

Every claim about current Instagram features below carries a tag, because the feature set changes and was not checked live.

1. Format: 9:16 at 1080 by 1920, filmed or cropped for vertical. [VERIFY: confirm current feature set for Instagram]
2. Hook inside 3 s: beat 1 has motion (guests walking, then looking up), the question in the voice and "Just launched" on screen, all inside 3 s. Put the strongest motion in frame 1, not a title or logo.
3. Sound off: burn in captions from the final voiceover as their own track, two lines at most, in the lower part of the safe box. Overlays add to the voice and never repeat it. [VERIFY: confirm current feature set for Instagram]
4. UI safe zone: keep text out of the top 14 percent (about 270 px), the bottom 35 percent (about 670 px) and 6 percent at each side. The shared safe box is x 122 to 838 px, y 270 to 1210 px. The skill grades this B and notes that no organic spec exists. The end card text must sit inside it. [VERIFY: confirm current feature set for Instagram]
5. Cover frame: pick a frame with people and the night sky and put the question on it, inside the safe box. Use a real frame, never a composited or generated sky. [VERIFY: confirm current feature set for Instagram, including how the profile grid crops the cover]
6. Pair with the carousel: if the designer makes a launch carousel, let the reel carry the news and the carousel carry the detail (the 7 day trip and price basis once the owner confirms them). Keep the facts the same in both. [VERIFY: whether a launch carousel exists, designer confirms]
7. Link: the call to action says "link in bio", so the bio link has to point to the tours before posting. See tours.json field url for the 7 day trip page. The day tour page is unknown. A link sticker is a different route and may not apply to a reel. [VERIFY: confirm current feature set for Instagram, and which page the bio link opens, owner confirms]
8. No aurora promise: the voice says we can't promise the lights, the overlay names what they need (clear sky and aurora activity), and the caption says no tour can promise them and that they depend on the sky. In comments, never answer "will we see them?" with a yes or with odds.
9. Music: sound is original, so voice and natural sound only. Trending audio is not allowed here because the script names the brand and a trip (rule SND01). If music is added, the licence must cover business use on Instagram. [VERIFY: confirm current feature set for Instagram, and the music licence, owner confirms]
10. Caption shape: the news in the first line, then the honest line, then the price with its "from" qualifier, then the link instruction, then one hashtag (the limit is 2). The first line should carry the point because only the start of a caption may show before the cut. [VERIFY: confirm current feature set for Instagram]
11. Disclosure: staff relationship. The overlay in beat 2 says "We work at Outdoor Norway" before 5 s, and the caption opens with "We're Outdoor Norway".

## Extending to 30 to 35 s

Beat map of a 32 s version of concept A (7 beats):
1. 0 to 3 s, hook: "Which northern lights trip fits you?" Overlay "Just launched" (F2).
2. 3 to 7 s, "One way is the 7 day Northern Lights tour." and disclosure (F1).
3. 7 to 12 s, "You ski one day, and other nights you look up." (F1).
4. 12 to 17 s, "We can't promise the lights. No tour can." (F4).
5. 17 to 22 s, "And there are multi-day tours as well." Overlay "More multi-day tours" (F3).
6. 22 to 28 s, "Can't spare a week? Take the Northern Lights day tour." Payoff, closes the loop (F2).
7. 28 to 32 s, call to action, same end card.

What the validator says about it
- With tiers.json as it is today, `seconds: 32` is a parse error: seconds must be between 8 and 25.
- Against a throwaway copy of tiers.json (outside the repo, tiers.json itself unchanged) with only the cap raised to 35, the 32 s version gives RESULT: FAIL (2 blocking, 5 warnings):
  - W01 (blocking): 59 words, maximum 55.
  - F02 (blocking): 4 facts, maximum 3 (F1, F2, F3, F4).
  - T02 (warning): estimated 25.0 s, warning line 21.0 s.
  - B01 (warning): 7 beats, target at most 6.
  - F04 (3 warnings): the same three lines as the 24 s script, from F1 being verified no.
- With warn_seconds also raised, T02 clears and the result is 2 blocking, 4 warnings.
- Limits scale with seconds divided by the cap, so raising the cap alone shrinks the word budget at the same time. A higher cap would also need the word, fact and beat limits reviewed together.
- About 25 s of the 32 s is spoken. The rest is hold and pause.

The owner's options (no choice is made here)
- Raise the short cap in tiers.json (and the related word, fact, beat and warn limits), then write the 32 s version against the new limits.
- Keep the 25 s cap and post the 24 s script, with the 30 to 35 s ideas going into concepts B and C instead.
- Keep the 24 s script and hold the end card past the voiceover. The validator reads the declared seconds, so it would pass, but the finished reel would run past the tier cap in practice and the validator cannot see that.
- Whatever runtime is chosen, check it against the current Reel length options. [VERIFY: confirm current feature set for Instagram]

## Open items

Owner (facts and decisions)
- Fact: the short cap. 30 to 35 s was asked, the tier cap is 25 s. Raise, keep or hold the end card.
- Fact, first request: what the northern lights day tour includes and how long it runs, in writing, so beat 5 can say what the viewer gains beyond "shorter than a week". Until then beat 5 says nothing more. [VERIFY: day tour duration and inclusions, owner confirms]
- Fact: the rest of the day tour. Price, start point, itinerary, departure dates and booking page are all unknown. The script states none of them. [VERIFY: day tour facts, owner confirms]
- Fact: the other multi-day tours. Which ones are in the launch, and any facts about them. The script says only that they have launched. [VERIFY: multi-day tours in this launch, owner confirms]
- Fact: confirm the 7 day itinerary in tours.json (its itinerary_note says not yet confirmed). Beat 3 uses the ski day and the aurora hunting trip from it, so F1 stays verified no and strict and final fail until this is closed. Also confirm that "from NOK 41,181" is the right price basis for the caption. [VERIFY: itinerary and price basis, owner confirms]
- Fact: confirm the reading of "we launched not the lights tour" as the Northern Lights tour. [VERIFY: owner confirms]
- Fact: naming. Confirm the product is named the same way everywhere. The tours.json name is "7 Day Ski in Fjord Norway & Aurora in Tromsø" and the script says "7 day Northern Lights tour". The caption now reads as a day tour, the 7 day tour and other multi-day tours. [VERIFY: product naming in the script and caption, owner confirms]
- Fact: the F2 and F3 quotes were carried over from the earlier draft and not rechecked here, because the brief file is not in the repo. [VERIFY: F2 and F3 quotes are the owner's own words, owner confirms]
- Permission: the bio link destination and the music licence, if any music is used. [VERIFY: bio link page and music licence, owner confirms]
- Fact: page conflicts already listed in the 12 Oct notes (gear, lunch, day 4, level wording) are not used in this script, so they do not block it.

Editor (footage and release)
- Footage: real clips for every visual: the evening snow walk and look up, the night sky over a ridge, a gloved hand pointing, boots on snow, a ski turn, a wide shot of a snowy field after dark with a line of small figures, guests in a row with heads tilted up, a guest laughing, the group walking away across snow, a slow pan along a track at night. No composited or generated sky. [VERIFY: which of these clips exist in the library, editor confirms]
- Release: a written release from every guest in shot, with guardian consent for anyone under 18. [VERIFY with counsel: Norwegian image right and GDPR, owner confirms who checks]
- Burned-in captions from the final voiceover once the audio is recorded.

Designer
- Cover frame and end card inside the safe box, and the carousel if there is one. [VERIFY: whether a launch carousel exists, designer confirms]

Voice recorder
- Standard narrator is assumed. If the voice is slow (text-to-speech or a non-native reader), the script needs about 48 words or fewer: a test copy at slow pace gave T01 estimated 25.4 s against a maximum of 24 and W01 51 words against a maximum of 49.

## Sources

- The owner's written brief of 14 Oct 2026 (quoted in the facts rows F1 to F3; the F1 quote is the owner's own words, and the brief file itself is not in the repo).
- `campaigns/ski-meta-ads/tours.json`, only through `script_check.py --tour ski-aurora-7day`: name, kind, days, itinerary and price with its "from" qualifier. The file was not read whole.
- `.claude/product-marketing.md`: the do-not-claim list and the page FAQ line behind F4.
- `.claude/skills/scriptcraft/SKILL.md`, `assets/script-template-short.md`, `references/short-form.md`, `references/tiers.md`, `references/brand-and-claims.md`, `references/visuals-and-text.md` and `examples/short-fictional.md` (format only, nothing reused).
- `.claude/skills/scriptcraft/scripts/brand_rules.json` for the place name and aurora rules, and the limits from `script_check.py --limits short voiceover`. tiers.json was not read whole or edited.
- `content/scripts/2026-10-12-northern-lights-7day-youtube.md` and its notes, for format and for the page conflicts only.
- Not checked: live site pages, the live Instagram feature set, `references/ugc-style.md`, `references/psychology-for-scripts.md`, `assets/guide-moment-intake.md` and `assets/creator-brief-template.md` (named for concept C, not read).
