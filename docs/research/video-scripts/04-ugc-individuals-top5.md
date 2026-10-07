# 04. UGC style: five individual creators (UK and US) to learn from

Scope: individual people on personal TikTok accounts. No brand, resort, tour operator or tourism board accounts. Country checked on the creator's own page or a reputable profile. Snapshot date: 7 October 2026.

Grades. A: platform or regulator, or platform-reported counts. B: documented creator process or large dataset. C: our own small-sample measurement or practitioner lore. Every measurement in the tables below is grade C unless marked.

Method in one paragraph. Profile counts were read from the public TikTok profile page (A, snapshot). Recent video IDs came from the public embed page. Per video we pulled info.json and captions with yt-dlp. When TikTok had no captions we ran faster-whisper (base.en) on the audio and kept only real speech; whisper output on music-only clips was discarded as lyrics or hallucination and recorded as zero spoken words. Visuals: low-resolution copies, eight-frame contact sheets and ffmpeg scene detection (threshold 0.3) for cuts per 10 seconds. Scene detection undercounts whip pans and continuous POV, so cut counts are a floor. Transcripts and media stay in scratchpad/transcripts and scratchpad/vis only.

## 1. The five

| Rank | Creator | Handle | Country and evidence | TikTok followers / likes (A, 7 Oct 2026) | Why picked |
|---|---|---|---|---|---|
| 1 | Ryan Wachendorfer | @ryanwachendorfer | US. Own bio: "Pro snowboarder from Colorado". Recent posts geotagged CH by the platform. | 710,300 / 28.6M | Biggest individual winter account found. Fast first-person voiceover over phone footage. Brand tags handled lightly. |
| 2 | Alex Hackel | @alexhackel | US. Montana State University profile: X Games medalist skier from Boston (montana.edu). | 170,200 / 13.2M | Posting from Norway right now (platform location NO on his last four posts, sound labelled "original lyd"). Text-on-screen meme format. Co-owns a ski brand and promotes it through a hashtag, not a pitch. |
| 3 | Hannah, Adventures of the Wests | @adventuresofthewests | UK. Own bio: family adventures "from Brighton". Own videos: Nottingham Trent University, prices in pounds, camping at Normans Bay (East Sussex). Platform location GB on last four posts. | 53,600 / 2.2M | Closest to "real guest" UGC. Her ski accommodation tour is the best booking-adjacent video in the sample. Runs labelled AD partnerships on her own account. |
| 4 | Brit | @mtn.brit | US. Own bio: Breckenridge, CO. Own video: says she is 29 and lives in a mountain town, moved from the city. Platform location US. | 39,300 / 1.4M | Part-time ski instructor who talks to camera. Closest model for a guide on camera. Ikon Pass partner posts. |
| 5 | Jess Cohen | @jess.cohenn | US. Own video says the snow has started "here in Colorado". Platform location US. Listed by Popfly as a ski creator. | 68,900 / 1.2M | Full-time ski creator (her own caption). Weekly series format, brand unboxing, gifted kit. Shows how brand-heavy UGC can go flat. |

Notes on the ranking. Followers alone would put Kara and Nate and Drew Binsky above most of these, but they are not winter creators (see section 6). Jess Cohen is fifth on relevance and follower count; her nine recent videos were all published on the snapshot day, so their view counts are not settled and are not used to judge her.

## 2. Numbers first

### 2.1 Performance of the measured videos (A for raw counts, C for medians)

| Creator | Videos | Median duration (s) | Median views | Range of views | Like % | Comment % | Share % | Save % |
|---|---|---|---|---|---|---|---|---|
| Ryan Wachendorfer | 6 (Sep 2026) | 37.5 | 6,127 | 2,438 to 67,800 | 6.18 | 0.11 | 0.11 | 0.16 |
| Alex Hackel | 8 (30 Sep to 7 Oct 2026) | 10.5 | 7,443 | 1,199 to 70,200 | 10.64 | 0.05 | 0.36 | 0.25 |
| Hannah (Wests) | 5 (Sep 2025 to Oct 2026) | 51 | 3,191 | 441 to 312,600 | 5.79 | 0.07 | 0.07 | 0.25 |
| Brit | 7 (Dec 2024 to Sep 2026) | 71 | 1,363 | 732 to 528,500 | 6.83 | 0.41 | 0.14 | 0.17 |
| Jess Cohen | 6 (all 7 Oct 2026) | 49.5 | 305 | 82 to 8,174 | 3.39 | 0.00 | 0.00 | 0.20 |

Ratios are per view. Every account has one or two outliers that carry it. Hannah's Val Thorens accommodation tour (312,600 views) earned 9,288 saves (2.97 %) and 5,084 shares (1.63 %). Brit's five ski tips video (528,500 views) earned 9,592 saves (1.81 %). Both are practical, you-focused, save-worthy videos. Their story videos sit near 0.1 to 0.5 % saves.

### 2.2 Speech metrics per video (C)

wps = spoken words divided by full duration. w3 = words spoken in the first 3 s. 1st = time of first word. you/me = second person versus first person tokens. num/30 = numerals per 30 s. src: vtt = TikTok captions, wh = whisper.

| Video | Format | Dur | Words | wps | w3 | 1st (s) | Avg sent | num/30 | you/me | ? | src |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ryan, Japan in September | VO over vlog | 23 | 112 | 4.87 | 11.9 | 0.38 | 22 | 9.1 | 1/7 | 0 | vtt |
| Ryan, dry slope halfpipe | VO over vlog | 45 | 188 | 4.18 | 11.6 | 0.30 | 19 | 6.7 | 4/6 | 0 | vtt |
| Ryan, 7-Eleven haul | to camera, sparse | 44 | 42 | 0.95 | 9.3 | 0.14 | 8 | 2.0 | 0/3 | 0 | vtt |
| Ryan, three other posts | music, no speech | 28 to 42 | 0 | 0 | 0 | none | none | none | none | none | wh, discarded |
| Alex, all eight posts | text meme over clip, sound | 8 to 16 | 0 own words | 0 | 0 | none | none | none | none | none | wh, discarded |
| Hannah, ski hostel tour | VO, selfie and B-roll | 60 | 199 | 3.32 | 13.0 | 0.00 | n/a | 1.5 | 11/3 | 0 | vtt |
| Hannah, data tip (AD) | to camera plus VO | 46 | 183 | 3.98 | 13.3 | 0.02 | 23 | 2.6 | 4/15 | 1 | vtt |
| Hannah, kids toy (AD) | to camera plus VO | 35 | 138 | 3.94 | 14.3 | 0.02 | 14 | 2.6 | 0/6 | 0 | vtt |
| Hannah, camping (AD) | VO, B-roll | 51 | 202 | 3.96 | 10.3 | 0.00 | 13 | 1.8 | 5/7 | 1 | vtt |
| Hannah, home swap (long) | to camera walk-through | 179 | 648 | 3.62 | 12.6 | 0.02 | 11 | 1.2 | 7/41 | 0 | vtt |
| Brit, five ski tips | text tips over song | 21 | 0 own words | 0 | 0 | none | none | none | none | none | vtt is lyrics |
| Brit, I am back | to camera plus B-roll | 71 | 286 | 4.03 | 12.2 | 0.00 | 20 | 2.5 | 6/33 | 0 | vtt |
| Brit, beginner as an adult | to camera plus B-roll | 90 | 386 | 4.29 | 14.7 | 0.02 | 26 | 2.3 | 13/38 | 1 | vtt |
| Brit, first trail race | to camera | 113 | 379 | 3.35 | 13.1 | 0.10 | 15 | 1.3 | 8/29 | 0 | vtt |
| Brit, new sport | to camera | 88 | 361 | 4.10 | 13.1 | 0.06 | 17 | 1.0 | 2/35 | 0 | vtt |
| Brit, tips with a friend | two to camera | 60 | 206 | 3.43 | 11.5 | 0.00 | 11 | 4.5 | 10/7 | 1 | vtt |
| Brit, fall ride | selfie while riding | 36 | 101 | 2.81 | 10.1 | 0.00 | 13 | 1.7 | 5/7 | 0 | vtt |
| Jess, workout series ep 5 | VO intro and outro, music | 70 | 90 | 1.29 | 9.0 | 0.00 | 18 | 1.3 | 1/6 | 0 | wh |
| Jess, workout series ep 3 | VO intro and outro, music | 82 | 65 | 0.79 | 9.2 | 0.00 | 16 | 0.4 | 4/2 | 0 | wh |
| Jess, apparel unboxing | to camera, chatty | 100 | 190 | 1.90 | 5.8 | 0.00 | 5 | 0.3 | 5/8 | 2 | vtt |
| Jess, mum cheering on a run | ambient speech | 29 | 32 | 1.10 | 4.6 | 0.00 | n/a | 0 | 2/0 | 0 | wh |

Average sentence length depends on caption punctuation, which is unreliable on auto captions. Treat it as rough.

### 2.3 Summary by creator (C)

| Creator | Median wps, speaking videos | Median words in first 3 s | First word | Contractions per 100 words | Casual markers per 100 words | Cuts per 10 s (sampled) |
|---|---|---|---|---|---|---|
| Ryan | 4.18 (n=3) | 11.6 | 0.1 to 0.4 s | 1.6 to 2.7 | about 0.5 ("so", "like") | 6.3, 3.7, 3.2 |
| Alex | 0 (text-led) | 0 | none | n/a | n/a | 0 to 3.4 |
| Hannah | 3.95 (n=5) | 13.0 | 0.0 s | 1.0 to 3.8 | about 1.5 ("so", "honestly", "actually") | 5.5, 4.5 |
| Brit | 3.73 (n=6) | 12.7 | 0.0 to 0.1 s | 2.8 to 3.4 | about 1.6 ("so", "like", "honestly") | 1.8 (text), 5.3 (talk) |
| Jess | 1.29 (n=4, music gaps) | 7.4 | 0.0 s | about 1 | about 3 in the unboxing | not sampled |

Three findings drive the validator section.

1. Talking creators run 3.3 to 4.9 words per second over the full clip, and speech starts at 0.0 to 0.4 s. That is 40 to 100 % faster than our 2.4 wps voiceover cap (C).
2. They put 10 to 15 words into the first 3 s. Our hook rule is 4 to 9 words. The hook in UGC is the first sentence plus the first frame plus the overlay, not a short line (C).
3. Casual markers are rarer than the stereotype. "So" is the only frequent one. "Like", "honestly" and "literally" appear about once per video at most. Scripts that sprinkle "okay so" and "literally" will sound fake (C).

### 2.4 Official guidance and rules (A)

| Source | What it says | Use |
|---|---|---|
| TikTok Ads help, Creative best practices | Introduce the proposition in the first 3 s; hook within the first 6 s; feature creators, employees or customers; a DIY, not overly polished style; 9:16, sound on, keep content in the UI safe zone; end with a clear call to action; trends and the Commercial Music Library. | Supports staff-led UGC and a single CTA. |
| Same page | For text: "We recommend displaying 5-10 words per second when using text." | Odd phrasing; we read it as caption pacing, not overlay length. Do not convert into a rule without testing. |
| FTC, Disclosures 101 for influencers | Disclose any financial, employment, personal or family relationship with a brand. The disclosure should be in the video, not only the description. Audio plus on-screen is more likely to be noticed. | Guides and staff posting about Outdoor Norway must disclose, in the video. |
| ASA and CAP, Recognising ads (UK) | A prominent "Ad" label upfront. Owners and employees are covered. "Sponsored" or "gifted" alone is unlikely to be clear. A bio note is not enough. | UK viewers: put "Ad" at the start of the caption and on screen when a guide promotes a trip. |

## 3. Creator profiles

### 3.1 Ryan Wachendorfer (US, 710,300 followers)

Speaking style. Fast, flat, matter-of-fact first person. 4.2 to 4.9 wps, first word under 0.4 s, no greeting. Long run-on sentences joined with "and" and "then". Few casual markers. Humour is dry understatement, for example that "snowboarding" is a loose word when it is hot and raining. Numbers are concrete and spoken casually: flight length, aircraft type, days at the facility, hours per day. Places are named plainly (LAX, Tokyo, Japan, Colorado).

Hook formats. Expectation flip: you have heard of X in the usual season, but we are doing it in the off season (his line: "You've probably heard about snowboarding in Japan in January"). Day-one check-in: "checking in from day one" with an oddity (no snow). Haul: here is everything I bought. Countdown: a caption about being back in the trees in four months.

Structure, short (23 to 45 s). Hook with a contrast in sentence one. Then a chronological travel chain: plane, car, food, venue. A how-it-works explainer in the middle (how a dry slope halfpipe works). Ends on a concrete benefit fact, not a CTA. No end card.

Visuals. Selfie at the airport, handheld follow shots, cockpit and food inserts, then the activity. 3.2 to 6.3 cuts per 10 s. Native TikTok captions only; text overlay is light.

Sound. Voiceover over trending or original music for the travel posts; pure music for clips.

Brand handling. Tags (@Canyon on a bike unboxing, a fellow athlete on the Japan trip) sit in the caption. The video itself is the experience. No pitch line.

What fails. Music-only posts with no hook line got 2,400 to 5,700 views against 12,500 and 67,800 for the two voiceover explainers (n is tiny, C). The explainer that taught something (how the dry slope works) did best.

### 3.2 Alex Hackel (US, 170,200 followers)

Speaking style. None. His recent posts carry zero own spoken words. The voice is in the overlay text: one or two short lines of in-group skier humour, for example before lunch versus after lunch, or a joke that he has decided his injury is over. Overlays run 6 to 11 words, white text with a soft shadow, top third, sentence case.

Hook formats. Relatable meme ("I can't be the only one"), versus split (before and after), send-to-a-friend (caption "Send it to them"), reaction audio (a sports commentary clip, a movie line about speed).

Structure. 8 to 16 s. Setup text appears at frame one and stays. Payoff is the footage: a crash, a big air, a fast run. Built to loop.

Visuals. Helmet or chest POV, follow cam, some 360 camera. 0 to 3.4 cuts per 10 s.

Brand handling. He co-owns 1000 Skis (montana.edu). The brand appears as #1000skis on every post and on the gear. Never a spoken pitch. Shares run 0.36 % of views, the highest in the sample, because the posts are made to be sent.

What fails. Nothing obvious in performance terms. For us the risk is content: crash and injury jokes and speed humour clash with a guided safety brand.

### 3.3 Hannah, Adventures of the Wests (UK, 53,600 followers)

Speaking style. Warm, quick, conversational British English, 3.3 to 4.0 wps. Starts talking at 0.0 s. Mostly first person in story posts (you/me 4/15 in the data tip), but strongly second person in the viral tour (11/3). Prices said plainly in pounds and euros. Self-aware humour about her husband, Simon, who appears on camera as the foil.

Hook formats. "It's not what you're imagining" reveal tour (the Val Thorens hostel). "Someone asked me" reply format (a toy question). "My husband taught me this trick" with a mild grievance. Storytime with "Looking back at this as a full blown adult". Reply-to-comment (her chalet business story starts as a reply).

Structure, short (35 to 60 s). Hook plus title overlay. Then a fast inclusions list over B-roll: location, meals, cake, rooms, kit hire, each with a price or a number. Then the price line and how to book. Ends with "hit save for your next ski holiday" plus follow. Long (179 to 219 s): walk-through with running commentary, ends on "let me know in the comments" or a simple "let's go".

Visuals. Selfie hook, then B-roll of the place. 4.5 to 5.5 cuts per 10 s. Bold title overlay at the top in the first frame. Word-by-word burned-in captions with one highlighted word, centred low.

Brand handling. Paid posts start the caption with "AD" (data tip, kids toy, camping trip). The ad is framed as a solved problem from her own life: Simon noticed, here is what we sorted. Her best performer is not labelled AD: it names the booking agent once, gives a "from" price for a long weekend, and asks for a save. The booking mention is one sentence of logistics, not a pitch.

What fails. Her AD posts sit at 441 to 3,191 views. Her practical tour sits at 312,600. Product-first stories underperform place-first, money-saving tours (C, n small).

### 3.4 Brit (US, 39,300 followers)

Speaking style. Talk to camera, 3.4 to 4.3 wps, earnest and encouraging. Long sentences (15 to 26 words on caption punctuation). First person dominant (you/me 13/38 in the beginner post). Contractions about 3 per 100 words. Light humour ("always wear glitter, it makes you go faster" as the tips sign-off). Places and numbers are personal: her age, "100 days", the three month countdown.

Hook formats. Big statement ("Being a beginner as an adult is one of the coolest things you can do"). Fake-out ("I found a sport I love more than skiing. Just kidding"). Intro post ("Hi, I'm Brit, I'm 29 and I live in a mountain town"). Tips list (five tips as an instructor, text only). Countdown.

Structure. Text tips (21 s): one tip per shot, overlay of 9 to 12 words each, trending song, no speech. Talk posts (60 to 113 s): statement hook, name intro after the hook, story, lesson, invite to follow along.

Visuals. Chairlift selfie, friend filming her skiing, walking selfie in town. Text tips video 1.8 cuts per 10 s; talk post 5.3.

Brand handling. Ikon Pass posts read like trip memories: she went heli-skiing on her pass and calls it the best ski day of her life, then a line on what pass holders can unlock. Kit lists live in the caption with handles and a ShopMy link. We could not see from the data whether the platform paid-partnership label was on.

What fails. The talk posts get 700 to 2,000 views. The 21 s silent tips post got 528,500 and 9,592 saves. Long sincere monologues earn comments (0.4 to 0.8 %, best in the sample) but little reach.

### 3.5 Jess Cohen (US, 68,900 followers)

Speaking style. Two modes. Presenter mode in her "Mountain Motivation" series: "welcome back to session 5" and a sign-off for next week, fast in bursts with music between. Chatty mode in unboxings: short fragments, "okay so", "literally", "like", questions to the viewer.

Hook formats. Series opener, "I can't be the only one" relatable caption, "OMG snow", things I will die on (a ski opinion list, her best recent post at 8,174 views).

Structure. Series: intro line, workout over music with exercises in the caption, outro with next episode. Unboxing: open box, react, try on, thank the brand.

Brand handling. A gifted parcel is opened on camera with "welcome to the team". Brands are tagged in captions. This is the most ad-like content in the sample and it is the weakest (82 to 386 views), although these posts are less than a day old.

What fails. Greetings and "welcome back" openers waste the first 3 s. Unboxings look like ads.

## 4. Cross-creator patterns

Hook formats seen, by frequency in this sample: statement or expectation flip (6), relatable meme text (6), tips or list (3), reveal tour (1), storytime or reply (2), countdown (3), series opener (2). Not seen in this sample: "POV:" captions and "things nobody tells you". They exist on TikTok but our five do not use them, so we have no measurement.

Endings. Ryan and Alex end on the payoff with no CTA and rely on the loop. Hannah ends with a save prompt plus follow, or a comment keyword ("comment camping meals" and they send the recipes). Brit ends with "follow along". No one uses an end card, a logo sting or a URL on screen.

Camera. All phone or action cam, vertical. Selfie for the hook, then POV or a friend filming. Continuous POV runs (0 cuts) and fast vlogs (5 to 6 per 10 s) both work.

Text on screen. Three jobs: a title in the first frame (Hannah), the whole message (Alex, Brit tips), or captions (Hannah, Brit). Overlays for memes run 6 to 12 words across one or two lines.

## 5. What to copy, adapt and not copy

Copy.
- Start speaking at 0.0 to 0.5 s with the reason to watch. No greeting.
- One concrete, checkable detail per beat said casually: a price "from", a time, a day count.
- Save-worthy practical formats: what is included, what to pack, how the day runs. These earned 2 to 3 % saves.
- A single booking sentence of logistics near the end, then a save prompt. Hannah's tour is the template.
- Text-led clips with one line of honest guide humour over a POV run.
- Disclosure inside the video.

Adapt.
- Alex's relatable memes, but about cold hands, skins, lunch on the ridge, not injuries.
- Brit's tips list, but each tip from a guide on a real tour day.
- Ryan's expectation flip for Voss: what people expect of Norway in winter versus what a day actually looks like.
- Name intro after the hook, for example "I'm Kari, I guide ski touring in Voss", which doubles as disclosure.

Do not copy.
- Crash, speed and injury humour.
- Unboxings and "welcome to the team" gifted content.
- Long sincere monologues as the default short format.
- Trending copyrighted songs on posts that promote the company. Use original sound or the Commercial Music Library.
- Weather and aurora promises. None of the five promise snow; keep it that way.

## 6. Next five considered and why they were cut

| Creator | Country and evidence | TikTok (A) | Why cut |
|---|---|---|---|
| Bernie Rosow, @bernierosow | US. Vermont-born Mammoth snowcat operator and grooming supervisor (ActiveNorCal, 27 Apr 2026). | 99,600 followers; one POV run at 6.9M views | He died in April 2026 while backcountry skiing, per ActiveNorCal and other outlets. No new posts. His archive remains the clearest staff-POV reference: night worker, POV runs, camera reviews tagged to DJI, a ZAG Skis team announcement in the caption only. |
| Kara and Nate, @karaandnate | US. Platform location US on recent posts; bio says they founded Daily Drop. Not independently verified, moot as cut. | 370,500 | Recent TikToks mostly promote their own company and giveaways. Little winter. Their best recent post (1.8M views) had a 0.67 % like rate. |
| Dylan Dipentima, @dylandipentima | US. IZEA lists him as a Vermont-based pro skier; bio says ski bum in the Tetons. | 57,200 | Highly relevant backcountry content and sponsors listed in bio, but latest post dates to September 2024. |
| Drew Binsky, @drewbinsky | US. | 866,200, verified | Travel generalist, presenter style, no winter or ski focus. |
| Gus Kenworthy, @guskenworthy | British-American Olympic skier (TikTok newsroom UK, 2022). | 183,300, 34 videos | Too few posts, mostly actor and celebrity content. |

Dropped for country not verifiable: George Treble of @alpine_ski_tutorials (42,700; teaches in the French Alps; no nationality stated on his site) and Jason, @jasonleftwrightleft (34,400; Zermatt instructor; nothing public on nationality). Casey Willax (33,300) was cut on relevance and unclear identity.

## 7. Changes the validator and skill need for UGC style

1. Add `style: voiceover | ugc_talk | ugc_text`. Keep all current voiceover rules for `voiceover`. Reason: the measured UGC numbers break the voiceover limits on purpose.

2. Pace for `ugc_talk`. Short: allow up to 3.6 effective wps, cap 90 spoken words at 25 s, target 65 to 80. Long: allow up to 3.8 wps, cap 760 words at 200 s, target 550 to 650. Keep facts at 1 per beat and 3 per short script, 12 per long script. Reason: creators run 3.3 to 4.9 wps (C); the speed is filler and connective talk, not more facts.

3. Hook for `ugc_talk`: first spoken word by 0.5 s; first sentence 6 to 15 words, may run past 3 s if a visual or overlay hook is on screen from frame one; first person allowed ("I", "we") when the first sentence promises a payoff for the viewer, or the overlay addresses "you". Reason: measured 10 to 15 words in the first 3 s, first word at 0.0 to 0.4 s, and the strongest hooks were first-person reveals.

4. `ugc_text` format: zero spoken words allowed. Overlay 1 or 2 lines, 4 to 12 words total, on screen from frame one to the end, top third inside the safe zone. Length 7 to 15 s, built to loop, CTA optional. Reason: Alex's eight posts and Brit's 528,500-view tips post.

5. Overlay for `ugc_talk`: a title of up to 8 words in the first frame, plus optional burned-in captions that mirror speech. Captions do not count against the 6 words and 32 characters line rule; titles do, raised to 8 words and 40 characters. Reason: Hannah's title plus word-by-word captions.

6. CTA: 0 or 1. Allowed forms: save prompt, send-to-a-friend, comment keyword, follow along, or one logistics sentence on how to book. Max 10 words. Spoken or on screen, any time in the last 5 s. Ban end cards, logo stings, URLs on screen and "link in bio" more than once. Reason: no measured creator used end cards; the save prompt sat on the best practical video.

7. Greeting rule: keep blocking "hey guys", "welcome back" and "hi everyone" as openers. Allow a name and role intro (max 10 words) after the first sentence. Reason: Jess's "welcome back" openers performed worst; Brit's intro works only after a statement hook.

8. Casual markers: no requirement. Flag if "literally", "honestly", "okay so" or "like" (as filler) together exceed 2 per 100 words. Contractions: expect 1 to 4 per 100 words, warn below 1. Reason: measured creators used few markers; forced slang reads fake.

9. Disclosure: required field `relationship: staff | guide | guest_paid | guest_gifted | guest_unpaid`. For anything but `guest_unpaid`, require an "Ad" label at the start of the caption and an in-video disclosure in the first 5 s (spoken role line or on-screen text), and the TikTok content disclosure setting on. Reason: FTC and ASA guidance (A).

10. Sound: field `sound: original | commercial_library | voiceover_only`. Block `trending_song` when the post mentions Outdoor Norway, a trip or a price. Reason: TikTok points businesses to the Commercial Music Library (A); licensing is the operator's risk.

11. Brand rules stay. Unsupported superlatives, snow and aurora guarantees and scarcity stay blocked in every style. Allow honest effort statements with a payoff ("two hours up for the run down") and keep fear framing blocked. Reason: Bernie's effort framing performed; honesty is our edge.

12. New skill output: a creator brief, not a word-for-word script, for `ugc_*`. Fields: hook line plus two alternates, three talking points with one approved fact each from the claims bank, a shot list (selfie hook, POV, B-roll, reaction), overlay text, CTA option, disclosure line, banned claims, and a target length. Reason: UGC sounds scripted when read; guides need points and shots.

13. Visual guidance (not enforced): talk and vlog 3 to 6 cuts per 10 s; continuous POV allowed with zero cuts. Reason: both patterns appear in high performers (C).

## 8. Uncertainties

- Every measurement is a small sample (4 to 8 videos per person). Grade C.
- Whisper base.en output on music was discarded by hand. Some short spoken lines inside music posts may be missed.
- Auto-caption punctuation limits sentence length accuracy.
- Jess Cohen's videos were less than a day old.
- Platform location (CH, NO, GB, US) is where a post was made, not nationality; used only as support.
- We could not see paid partnership labels in the metadata.

## 9. Sources

- TikTok profiles and videos, public pages read 7 Oct 2026: tiktok.com/@ryanwachendorfer, @alexhackel, @adventuresofthewests, @mtn.brit, @jess.cohenn, @bernierosow, @karaandnate, @dylandipentima, @drewbinsky, @guskenworthy, @alpine_ski_tutorials, @jasonleftwrightleft.
- Montana State University, Alex Hackel profile: https://www.montana.edu/dxi/articles/alex-hackel.html
- ActiveNorCal, Mammoth community mourns Bernie Rosow (27 Apr 2026): https://www.activenorcal.com/the-california-ski-community-is-mourning-the-sudden-loss-of-a-mammoth-mountain-legend/
- IZEA, 17 skiing influencers: https://izea.com/resources/skiing-influencers/
- Popfly, ski and snowboard creators: https://www.popfly.com/post/ski-snowboard-creators
- TikTok newsroom UK, Team GB 2022: https://newsroom.tiktok.com/en-gb/tiktok-teams-up-with-team-gb-for-the-winter-olympics
- TikTok Ads help, Creative best practices: https://ads.tiktok.com/help/article/creative-best-practices?lang=en
- FTC, Disclosures 101 for social media influencers: https://www.ftc.gov/business-guidance/resources/disclosures-101-social-media-influencers
- ASA, Recognising ads, social media and influencer marketing: https://www.asa.org.uk/advice-online/recognising-ads-social-media.html
- Alpine Tutorials (George Treble): https://alpinetutorials.com
