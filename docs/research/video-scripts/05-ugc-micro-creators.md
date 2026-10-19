# 05. UGC micro-creators: guides, patrollers, instructors and real travelers

Scope: individual UK and US creators on their own personal accounts. No brand, resort, operator or tourism accounts. Measured 2026-10-07.

Method, in short:
- Captions pulled with yt-dlp from public TikTok and YouTube pages. TikTok captions are cue-level, so word timing inside a cue is interpolated. Words per second (wps) uses full duration as the denominator. It understates the true speaking rate when there is B-roll.
- Where TikTok had no captions, I downloaded the audio and ran faster-whisper (base.en) locally. Music lyrics and other speakers were excluded by hand. A video with 0 to 3 detected words is logged as "no voice".
- Follower counts come from each public TikTok profile page or YouTube about page on the day. Engagement ratios: likes per view (LR) and shares per view (SR).
- Grades: A platform official or peer reviewed. B documented process or large dataset. C my own small sample or practitioner lore. Every measured number here is C.
- Transcripts are not kept in this repo. No scripts are reproduced. Quotes are 15 words or fewer.
- Creator names, handles, channel names and profile links are left out because this repo is public. Labels A to E match note 04. Labels F to M are new here.

## 1. Subjects and country verification

| # | Creator | Role | Country | Evidence | Followers (date) | Lead platform |
|---|---|---|---|---|---|---|
| 1 | Creator F | Qualified ski instructor, French Alps | UK | Own site: calls himself a British instructor working in France | 42.7k TikTok, 83.5k YouTube | TikTok and Shorts |
| 2 | Creator G | Ski patroller, Utah | US | TikTok bio: ski patroller in a Utah town. TikTok upload region US on 4 of 4 latest | 2.7k TikTok | TikTok |
| 3 | Creator H | Snowcat operator at a US resort, posting personally | US | TikTok bio: snow cat operator for the resort. Upload region US 4 of 4 | 99.6k TikTok | TikTok |
| 4 | Creator I | Patroller, 7th season, Utah resort | US | YouTube about: describes work on the ski patrol of a Utah resort. Country field: United States | 1.48k YouTube | Shorts |
| 5 | Creator J | Full-time ski instructor, Utah resort | US | YouTube about: full time ski instructor. Country field: United States | 11.6k YouTube | Shorts |
| 6 | Creator D | Ski enthusiast, mountain-town resident | US | TikTok bio: a Colorado mountain town. Upload region US 4 of 4 | 39.3k TikTok | TikTok |
| 7 | Creator C | Family traveler, ski trips | UK | TikTok bio: real family adventures from a UK coastal city. Upload region GB 4 of 4 | 53.6k TikTok | TikTok |
| 8 | Creator K | Snowboarder, vlogger | US | YouTube country field: United States. A third-party profile site lists a US birth | 33.2k TikTok, 128k YouTube | TikTok and YouTube |
| 9 | Creator E | Freeride skier, full-time creator | US (weaker) | Upload region US 4 of 4. A creator roundup says she competes on a freeride qualifier tour. No self-stated country found | 68.9k TikTok | TikTok |
| 10 | Creator L | Backcountry skier | US | YouTube country field: United States | 12.2k YouTube | Shorts |
| 11 | Creator M | Travel writer, covers Norway snowshoeing | US | YouTube country field: United States | 11.8k YouTube | YouTube |
| ref | Creator A | Pro snowboarder | US | TikTok bio: pro snowboarder | 710.3k TikTok | Above range, used only as a ceiling |

Dropped: a Swiss-resort instructor account (34.4k). Strong guide format, but country not verifiable; uploads come from Switzerland. One Voss video from a channel with 4 subscribers and 275 views: country unverified and no traction. TikTok-native subjects: 1, 2, 3, 6, 7, 9 (six).

Norway coverage: only Creator M (snowshoeing, glacier, goat farm in Norway). I found no verified UK or US individual posting about Voss or Myrkdalen with traction. That is a gap Outdoor Norway's own guides can fill.

## 2. Measurements

### 2.1 Spoken videos, per creator (medians)

Only videos where the creator actually talks. TT is TikTok, YT is YouTube.

| Creator | Platform | Videos | Median dur s | Median wps (range) | Median words first 3 s | Median first word s | Avg sentence words | Numerals per 30 s | You share of you+I | Questions total | Median LR | Median SR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Creator F, instructor | TT | 9 | 60 | 3.11 (2.26 to 3.54) | 10 | 0.1 | 17.9 | 1.2 | 0.50 | 10 | 2.3% | 0.12% |
| Creator F, instructor | YT Shorts | 3 | 87 | 2.62 (2.15 to 2.90) | 12 | 0.1 | 14.4 | 0.0 | 0.67 | 0 | 1.1% | n/a |
| Creator I | YT Shorts | 4 | 49 | 2.46 (2.00 to 2.60) | 7 | 0.8 | 8.3 | 1.5 | 0.17 | 2 | 2.5% | n/a |
| Creator J, instructor | YT Shorts | 3 | 59 | 2.41 (0.97 to 3.33) | 7 | 0.3 | 5.7 | 1.0 | 0.67 | 1 | 1.2% | n/a |
| Creator D | TT | 6 | 80 | 3.73 (2.81 to 4.29) | 13.5 | 0.0 | 16.2 | 2.7 | 0.24 | 2 | 7.0% | 0.12% |
| Creator C | TT | 6 | 56 | 3.95 (3.32 to 4.05) | 13 | 0.0 | 13.8 | 2.0 | 0.18 | 4 | 5.7% | 0.07% |
| Creator K | TT | 6 | 74 | 2.83 (1.16 to 3.97) | 1 | 4.4 | 11.4 | 1.5 | 0.60 | 10 | 4.4% | 0.20% |
| Creator E | TT | 3 | 82 | 1.47 (0.78 to 1.90) | 8 | 0.0 | 8.0 | 0.4 | 0.38 | 2 | 3.3% | 0.00% |
| Creator L | YT Shorts | 3 | 30 | 2.47 (0.36 to 2.90) | 10 | 0.3 | n/a | 1.7 | 0.55 | 0 | 0.8% | n/a |
| Creator M (Norway) | YT | 4 | 69 | 2.70 (1.96 to 3.10) | 7 | 1.5 | 10.1 | 1.0 | 0.33 | 0 | 0.4% | n/a |
| Creator H | TT | 2 | 37 | 0.59 (0.22 to 0.97) | 8 | 0.0 | 6.7 | 4.6 | 0.00 | 0 | 1.8% | 0.16% |
| ref: Creator A | TT | 3 | 44 | 4.18 (0.95 to 4.87) | 12 | 0.3 | 18.8 | 6.5 | 0.12 | 0 | 5.0% | 0.10% |

Pooled spoken median across the 11 subjects: 2.87 wps over 49 videos (C). Grade C for all rows.

### 2.2 Voice-free videos (whisper found 0 to 3 creator words)

| Creator | Video no. | Dur s | Views | LR | SR | What carries it (from caption and description) |
|---|---|---|---|---|---|---|
| Creator H | 1 | 114 | 6.9M | 6.9% | 0.50% | Storm footage, one-line caption about rain turning to snow |
| Creator H | 2 | 53 | 288.3k | 3.2% | 0.22% | POV skiing, 3-word caption |
| Creator H | 3 | 80 | 106.7k | 1.6% | 0.17% | "Snowed a foot last night" style caption |
| Creator G, patroller | 4 | 27 | 685.7k | 9.9% | 0.76% | Patrol day montage, trending audio |
| Creator G, patroller | 5 | 22 | 197.3k | 7.5% | 0.34% | Day in the life of a patroller, text plus music |
| Creator D | 6 | 21 | 528.5k | 6.4% | 0.22% | "5 tips" as on-screen text over music |
| Creator D | 7 | 42 | 350.8k | 12.3% | 0.26% | "Day N of 100" series counter, no voice |
| Creator K | 8 | 13 | 2.1M | 7.4% | 0.10% | Pond skim clip. Only a 12-word comic sound bite, no explanation |
| Creator K | 9 | 15 | 685k | 2.8% | 0.13% | Surprise moment clip. Only laughter and reactions |
| Creator F, instructor | 10 | 10 | 329.8k | 2.5% | 0.49% | Parallel-skiing tip as on-screen text, no voice |

Of the 15 TikTok videos over 100k views in this sample, 10 had no scripted creator voice (C, n = 15, selection biased toward what each profile surfaced). The 5 spoken ones were Creator F's 3 tips, Creator C's accommodation tour and Creator K's patrol call.

### 2.3 Spoken hits and their contrast

| Creator | Hit (views, dur) | Same creator, weaker videos | Difference |
|---|---|---|---|
| Creator F | Single tip on leaning in turns, 452.7k, 37 s, 3.43 wps | Course pitch "roadmap via link in bio" 2.0k, 149 s. Recruiting video 5.3k, 133 s. "Full video on my YouTube" 2.4k, 99 s | One tip, under 60 s, no sale vs a sales pitch over 90 s |
| Creator F | Myth-bust on "bend the knees", 247.4k, 39 s | Same | Insider correction of a cliche |
| Creator C | Ski accommodation tour, 312.6k, 60 s, 3.32 wps, SR 1.63% (highest in set) | Paid AD posts 441 to 3.2k views | Useful, saveable trip info vs ads |
| Creator K | How to call ski patrol, 432.5k, 61 s, real incident footage, first word at 10 s | Talking trick tutorial 1.3k, 75 s, 3.97 wps | Real event and a safety lesson vs talking head |
| Creator D | Text-only tips and series counter, 351k to 529k | Talking videos about her life 0.7k to 9.9k | Text plus picture beat talking for her |
| Creator E | Text list "ski hills I will die on" 8.2k, 8 s | Spoken series "Mountain Motivation" 82 and 368 views, 70 to 82 s | Series label alone did not carry a long talk |

## 3. Micro-creators versus the first ring

The first-ring top-five notes were not available to me at writing time. The comparison uses the large travel creators measured in 02 (creator median 2.75 wps, shorts 2.87 wps, first word 0.0 to 0.4 s, all C).

- Pace is the same. Micro spoken median 2.87 wps, the same as the big creators' shorts. The difference is the spread: micro speakers run 1.5 to 4.0 wps, because many do not plan a script at all.
- Voice is optional. The big creators always talk. Micro hits are often silent: footage, one caption line, a trending sound. This is the largest difference in the data.
- Length. Micro spoken videos are long (median 56 to 82 s for TikTok speakers). Their best spoken hits are 37 to 61 s. The silent hits are 13 to 42 s, except Creator H's 114 s storm reel.
- Facts are sparse. Numerals per 30 s are 0.4 to 2.7 for most. Our 3 facts in 25 s equals 3.6 per 30 s, already above every micro guide. Keep the fact cap.
- First person dominates. You-share median is 0.38 across subjects. Only the instructors (Creator F, Creator J) sit at 0.5 to 0.67. Travelers sit at 0.18 to 0.24 and still hit 312k and 529k.
- Plan versus improvise. Planned: Creator F and Creator C (clean sentences, 0.0 s first word, 10 to 13 words in 3 s). Improvised: Creator K, Creator I, Creator J (fillers "um", "uh", "like" up to 14 per video, sentences of 6 to 11 words, first word up to 4.4 s). The planned ones had the spoken hits. The improvised ones won on real moments, not on words.

## 4. How guides teach in 20 seconds without lecturing

From Creator F, Creator J, Creator L and Creator K's tutorial (C):
1. Name the mistake, not the lesson. Creator F opens on a common error or a cliche. One example opener calls "bend the knees" a cliche ski instructor phrase.
2. One cue, shown on a body. The demo runs while he talks. No list.
3. Say why in one sentence, in plain physics. No jargon stack.
4. Stop. The 10 s parallel tip (329.8k) is one idea and "Good luck!".
5. Ask a question at the end. Creator K asks if he missed anything. Creator F asks which strand of skiing you like. Comments did the rest.

Credibility moves seen:
- Job in bio, not in the script (Creator F's instructor level, Creator H's night-work line, Creator G's patrol title). The video does not argue for authority.
- Uniform, cat cab, patrol sled or a dated snow report on screen (Creator I gives the date and fresh conditions each morning).
- Correcting folk wisdom ("bend the knees", "your DIN is not a flex" from Creator E's text list).
- Real incident handled calmly (Creator K's patrol call video).

Real guests and colleagues:
- Creator K and Creator I use friends and coworkers as the subject: someone lands a 360, someone needs help.
- Creator J's best clip is a child's first run down chutes. Family, with a parent filming.
- Creator C's whole channel is her family and partner.
- No creator in the sample showed paying clients in a tutorial. That is a consent and trust choice we should copy by default.

Humor: self-deprecating crash captions (Creator K "really feeling on point"), "good problem to have" about a delayed opening, and a switch trick goal (Creator H). Humor is aimed at the creator, never the guest.

What they leave out: prices (except Creator C, who is deal-led), booking language, company names, logos, end cards, intros. No one says "welcome to my channel" on a hit. Creator E's "welcome back to session five" opener sat on her two lowest videos.

## 5. Repeatable formats for a guide creator brief

Word counts assume 25 s short at 2.8 wps unless silent. Grade C, built from section 2 patterns.

| Format | Seen in | Beat structure (seconds) | Spoken words | Filming note |
|---|---|---|---|---|
| One fix I give every guest | Creator F, Creator L | 0 to 3 name the mistake. 3 to 15 demo with one cue. 15 to 21 why, one line. 21 to 25 question to comments | 45 to 60 | Selfie or chest mount at the start, then a colleague films the demo from below. One take per cue |
| Myth-bust | Creator F, Creator E | 0 to 3 state the myth. 3 to 12 "here is what actually happens" demo. 12 to 21 the replacement cue. 21 to 25 ask what else they were told | 45 to 60 | Text card for the myth so it reads muted |
| Day in the life of a guide (silent) | Creator G, Creator D | 4 to 6 clips, 3 to 5 s each: alarm or van, avalanche gear check, group skinning, summit, dinner. One overlay per clip | 0 to 15 | Phone in chest pocket. Shoot vertical. Natural sound, add a trending sound in-app |
| Snow report from the guide | Creator I, Creator H | 0 to 3 date and place. 3 to 15 what it looks like now, ski pole in fresh snow. 15 to 22 what we are doing today. 22 to 25 sign-off line | 35 to 55 | Same spot every time, same opener. Measured depth only. Never forecast |
| What guests ask me | Creator F's comment Q and A, Creator K | 0 to 3 the question on screen (reply sticker). 3 to 20 the answer with footage. 20 to 25 "ask the next one below" | 40 to 55 | Use TikTok reply-to-comment. Only real questions |
| Guide reacts or rates | Creator K reaction videos | 0 to 2 clip plays. 2 to 18 guide talks over it, one point. 18 to 25 verdict in 4 words | 30 to 50 | Only footage with written consent. Praise first, one fix |
| What is in my guide pack | Creator L gear, Creator H camera tests | 0 to 3 open the pack. One item per 4 s beat: beacon, shovel, probe, first aid, thermos. Last beat the "why" | 40 to 55 | Top-down on snow. Item name as overlay, 1 to 2 words |
| Real moment, then the lesson | Creator K patrol call | 0 to 10 real footage, no talk. 10 to 22 what to do, 2 steps. 22 to 25 "save this" | 25 to 40 | Only if nobody is hurt and everyone shown agrees. Never stage danger |
| Series counter | Creator D "day N of 100" | Overlay "Guide season day 12" at 0.0 s. 3 to 5 clips. One caption line | 0 to 10 | Number must be true and continue daily or weekly |
| First-timer guest moment | Creator C, Creator J | 0 to 3 guest says what they feared. 3 to 18 the run. 18 to 25 guest reaction in their words | 20 to 45 (guest speaks) | Guest films or is filmed with consent. Guest's words, not ours |
| Place in 20 seconds | Creator M Norway, Creator C tour | 0 to 3 "this is where we ski on day 2". 3 to 20 three shots with one fact each. 20 to 25 question | 45 to 55 | Walk-and-talk, phone at arm's length |
| Long: one day, start to finish | Creator M, Creator K vlogs | Hook 0 to 10, 4 to 6 chapters of 25 to 40 s, close on the group | 400 to 520 at 2.6 wps for 3:20 | Landscape. Guide narrates live, not in post |

## 6. Why guide-made videos fail

Seen in the sample (C):
- List dumps. Creator E's 70 to 82 s talky sessions: 82 and 368 views. Lists work only as on-screen text (Creator D's 529k tips video).
- Lecture tone and length. Creator F's 99 to 149 s explainers sit at 2.0k to 5.3k views. His 37 to 60 s single tips sit at 213k to 453k.
- Selling early. Every Creator F video with a course or link pitch underperformed his tip videos by roughly 40 to 200 times. Creator C's AD posts sat at 441 to 3.2k against her 312.6k value video.
- Channel intros and greetings. "Welcome back" and "hello" openers were on the lowest videos.
- Garbled audio. Wind, music and other people made several captions unusable. If the words matter, record near the mouth.
- No reason to watch to the end. Silent hits worked because the picture escalates (more snow, steeper, the landing). A talk with no payoff does not.

## 7. Brand and safety rules for guides on camera

- No guarantees about snow or the aurora. Report what is there today, with a date. Never "it will dump" or "you will see the lights".
- No unsafe skiing on camera. Stowe Mountain Rescue said in an NBC report that TikTok powder videos were pulling inexperienced people into the backcountry, and a rescued party cited TikTok as inspiration. TikTok says it will "limit, label, or remove content that depicts dangerous acts" (TikTok Newsroom, Feb 2022, A). Practical rules: avalanche gear visible in any off-piste clip, no closed terrain, no cliff drops with guests, no skiing over people, no helmets off in moving shots.
- Guest consent. Written or recorded consent for any identifiable guest. No minors without a parent's consent. No injured or distressed guests, ever. Faces off if in doubt.
- Disclosure. The US FTC says disclose any "financial, employment, personal, or family relationship with a brand", and to put it "in the video and not just in the description" (FTC, Disclosures 101, A). A guide must say they work for Outdoor Norway. UK rules (ASA and CMA) should be checked separately; I did not verify them here.
- No company selling in the video body. Booking info goes in the caption or a pinned comment.
- No superlatives about the company or the place that are not in the claims bank.

## 8. Changes the validator and skill need for UGC style

1. Add `style: ugc | voiceover`, default voiceover. All rules below apply only when `style: ugc`. Reason: micro-creator scripts break the voiceover limits by design (sections 2 and 3).
2. Add `voice: spoken | silent`. Silent allows 0 to 15 spoken words and moves the hook into overlay text. Reason: 10 of 15 TikTok hits over 100k had no scripted creator voice (C). Even Creator F, a talking instructor, had a 329.8k text-only 10 s tip.
3. Pace allowance with unchanged facts. Spoken UGC short: max 70 words in 25 s (2.8 effective wps), hard ceiling 75 (3.0 wps). Keep 1 fact per beat and 3 facts per script; recommend 2. Reason: micro spoken median 2.87 wps; numerals per 30 s are 0.4 to 2.7, below our current cap already.
4. Long UGC: max 520 words in 3:20 (2.6 wps). Chapters of 25 to 40 s. Reason: long spoken micro videos run 2.3 to 3.1 wps with B-roll gaps.
5. Hook. Keep 4 to 9 words inside 3 s and first word at or before 0.5 s for spoken. Allow first person in the hook (I, we, my) as long as it names a situation, a mistake or a stake. Keep "you" as a preference, not a requirement. Reason: you-share median 0.38; first-person openers drove 312.6k (Creator C) and the instructors used "you" mainly in the body.
6. Silent hook. First overlay at 0.0 s, 3 to 7 words. Each overlay card on screen for at least its word count divided by 5 seconds, matching TikTok's 5 to 10 words per second text guidance (A, see 02).
7. Name and role intro allowed. "I'm Kari, a ski guide in Voss" counts as part of the hook if it is 8 words or fewer and inside 3 s. "Hey guys", "welcome back", "hello and welcome" stay blocked.
8. CTA. UGC allows one CTA of 8 words or fewer in the last 4 s, and it should be a comment prompt, "save this" or a series tease. No booking or price CTA in the video. Booking line moves to a `caption` and `pinned_comment` output field. Reason: sales pitches underperformed by 40 to 200 times (C).
9. No end cards, logos, title slates or brand stings in UGC. Validator fails any beat with role `endcard`, `logo` or `title`. Brand appears only through the creator's disclosure line and the caption.
10. Disclosure required. UGC scripts need one disclosure beat or overlay, for example "I guide for Outdoor Norway", in the video. Not counted toward the hook or CTA. Reason: FTC (A).
11. Native text rules. Keep 6 words and 32 characters per line. Add max 2 lines on screen, and keep text out of the bottom 20 percent and right 15 percent where TikTok buttons sit (to be confirmed against TikTok safe-zone docs). Lowercase and casual punctuation allowed.
12. Casual markers allowed in UGC: "okay so", "honestly", "like", "kinda". Cap at 3 per short so it still reads clean. Fillers "um" and "uh" are never scripted.
13. Format field. `format:` must be one of the section 5 formats. Each format sets its own beat template and word range for the validator.
14. Safety lint. Block "send it", "full send", "no avalanche risk", "totally safe", "guaranteed powder", "you will see the lights". Require a `safety_note` in the brief for any off-piste or touring shot: gear visible, open terrain, no guests in hazard.
15. Consent field. Each person on screen tagged `consent: guide | colleague | guest_signed | none`. `none` fails if the person is identifiable. Minors need `guardian_signed`.
16. Creator brief output. Next to the beat table, output a one-page brief: format, goal in one line, the hook line, 3 talking points (not a word-for-word script), the one fact with its claims-bank source, shot list with phone position, safety and consent checklist, disclosure line, caption and pinned comment, and "say it your way" guidance. Reason: the strongest micro hits were not read from a script; a guide should improvise inside a fixed structure.
17. Duration targets for UGC short: 12 to 25 s. Keep the 25 s hard max. Reason: silent hits were 13 to 42 s and spoken hits 37 to 61 s, so our cap forces a single idea, which is what worked.

## 9. Uncertainties

- Small samples: 2 to 9 videos per creator. Selection follows what each profile and embed page exposed, mostly recent posts plus a few top posts.
- TikTok captions are cue-level; words in the first 3 s are interpolated.
- Whisper base.en can miss quiet speech under music. "No voice" means no creator speech detected, not proven silence.
- Engagement is at fetch time. Older videos had longer to grow.
- Creator E's country rests on TikTok upload region and a third-party roundup, not her own words.
- On-screen text in silent videos was not read; the description was used as a proxy.

## 10. Sources

- TikTok and YouTube profile and about pages, fetched 2026-10-07. Account and channel names are left out on purpose.
- Two third-party profile and roundup pages (one per creator) are not linked, to keep the creators unnamed.
- FTC, Disclosures 101 for Social Media Influencers: https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers (A)
- TikTok Newsroom, strengthening policies, Feb 2022: https://newsroom.tiktok.com/strengthening-our-policies-to-promote-safety-security-and-wellbeing-on-tiktok?lang=en (A)
- NBC, Stowe Mountain Rescue TikTok warning: https://www.nbcboston.com/news/local/stowe-mountain-rescue-vermont-tiktok-video-warning/3854184/
- TikTok Ads Help, creative best practices (via 02): https://ads.tiktok.com/help/article/creative-best-practices?lang=en (A)
