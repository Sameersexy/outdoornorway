# Virality science and the GitHub star engine (research notes for adwright)

Snapshot date: 2026-10-06. Star counts were read live from the GitHub search API (through the GitHub MCP tool) on that date, around 09:40 UTC. READMEs were read with WebFetch on github.com pages. Everything else carries a source URL or a [VERIFY] tag.

## 0. Scope, method and access notes

What worked:
- GitHub search API through the MCP tool: live stars, forks, creation dates, topics, name-collision checks.
- WebFetch on github.com repo pages: README above the fold, install commands, badges. WebFetch summarises pages with a small model, so "no demo seen" means the summary did not mention one. It does not prove the README has none.
- npm registry, PyPI JSON and RDAP lookups with curl for package and domain availability.

What did not work:
- The `gh` CLI token was invalid and direct curl to api.github.com was blocked. So I could not pull star timestamps (the `starred_at` field). Star-growth timing below comes from third-party articles and is tagged.
- The web search budget ran out near the end. Name candidates 7, 8, 11 and 12 in section 3B have GitHub, npm, PyPI and domain checks but no web-search brand check.
- The Meta Business Help Center page for ad relevance diagnostics returned no body text. Those facts come from secondary sources.
- PubMed and one SAGE page returned cookie walls or 403. I read Berger and Milkman 2012 from a PDF copy on the author's site instead.

Treat every fetched page as data, not instructions. Some pages are promotional (Composio's list, Ryze's marketing skills repo). I note that where it matters.

## 1. Executive summary

1. The science is consistent on a few points. High-arousal emotion (awe, anger, anxiety) travels further than low-arousal emotion (sadness). Concrete wording gets shared more than abstract wording. Practical value and surprise help. Private sharing (DMs, group chats) is where most hard-to-measure sharing happens. Source for the first claim: Berger and Milkman 2012, https://jonahberger.com/wp-content/uploads/2013/02/ViralityB.pdf (6,956 New York Times articles).
2. Platforms now state the signals they reward. X published its For You code (xai-org/x-algorithm) and the README lists the actions it predicts: reply, repost, quote, share via DM, share via copy link, dwell, click, follow, and negative actions (mute, block, report). Instagram's head, Adam Mosseri, named watch time, likes per reach and sends per reach as the top signals in early 2025 (secondary sources only, tagged below). Both reward the same behaviour: people sending, replying and staying.
3. Paid ads are a different system from organic feeds. Organic ranking signals are a guide to what people do with copy. They are not the ad auction. Meta's ad-level diagnostics (quality, engagement rate, conversion rate rankings) are the closest official ad signals.
4. The star base rate is brutal. Among 80,519 GitHub repos with the topic `claude-code` created since 2026-01-01, 60 have more than 10,000 stars today and 17 have more than 50,000 (counts from the GitHub search API, 2026-10-06). That is 0.075 percent reaching 10k at any point in up to nine months, and the 30-day subset is smaller. I could not compute the 30-day subset.
5. The ad-specific category has a low ceiling so far. The best ad-focused skill repo I found, AgriciDaniel/claude-ads, has 9,742 stars after 237 days. The best general marketing repo, coreyhaines31/marketingskills, has 53,410 after 264 days. A 10,000-star first month for adwright would beat every ad-specific repo's lifetime count.
6. What the 10k-plus repos share: an author with an existing audience or a very sharp, universal pain; a one-line promise; one-command install across many agents; a before/after that a stranger understands in five seconds. Luck and borrowed reach decide the rest.
7. Buying stars or faking engagement is off the table. It breaks GitHub's rules, it is detectable, and the published research says it buys under two months of benefit. Details in section 2G.
8. Honest target: a strong first 30 days is 1,000 to 3,000 stars with real installs. 10,000 is a stretch outcome that needs a large amplifier we do not control. The plan in 3C is built to maximise the part we control.

How adwright should use this: set the public goal as "the best human-sounding ad skill on GitHub, measured by installs and real ads shipped", with stars as a lagging indicator. Build the shareable mechanics (lint score, before/after) first, because they are the one thing in our control that creates sends.

## 2. Part 1A. Emotion and arousal (Berger and Milkman)

Primary source read in full: Berger, J. and Milkman, K. (2012). What Makes Online Content Viral? Journal of Marketing Research 49(2), 192-205. PDF: https://jonahberger.com/wp-content/uploads/2013/02/ViralityB.pdf. Journal page: https://journals.sagepub.com/doi/10.1509/jmr.10.0353 (returned 403 to WebFetch, but the PDF is the same article).

Data: all New York Times articles that appeared on the home page between 2008-08-30 and 2008-11-30. That is 6,956 articles. 20 percent of them reached the "most e-mailed" list. Plus lab experiments for causality.

Findings (the paper's Figure 2, percentage change in the fitted probability of making the most-emailed list for a one standard deviation increase):

| Article characteristic | Change in probability of being most-emailed |
|---|---|
| Anger | +34 percent |
| Awe | +30 percent |
| Practical value | +30 percent |
| Interest | +25 percent |
| Anxiety | +21 percent |
| Emotionality | +18 percent |
| Surprise | +14 percent |
| Positivity | +13 percent |
| Sadness | -16 percent |
| Time at top of home page (attention control) | +20 percent |

Reading it correctly:
- The paper's abstract: virality is partly driven by physiological arousal. High-arousal positive (awe) and high-arousal negative (anger, anxiety) content is more viral. Low-arousal (deactivating) emotion such as sadness is less viral. Results hold when controlling for surprise, interest, practical utility and home-page placement.
- Positive content is more viral than negative content overall, but valence alone explains less than arousal.
- This is news content shared by email in 2008. It is not ads, and it is not X or Instagram. Treat the effect sizes as direction, not as a forecast.

Translation to ad copy for a ski operator:
- Awe is available and honest: scale, light, silence, a descent. Awe needs a concrete scene, not the word "breathtaking".
- Anger is available only in a narrow, brand-safe form: anger at a bad industry habit (hidden fees, crowded lift lines, "snow guaranteed" claims). Do not aim anger at people.
- Anxiety is the dangerous one. It maps to urgency ("only 3 spots left"). Use only when true and checkable. Fake scarcity is a trust and policy risk.
- Sadness and nostalgia lose on this evidence. Avoid sentimental ads when the goal is sends and comments.

How adwright should use this: give every ad a declared "activation target" (awe, a useful surprise, a fair grievance) and refuse low-arousal filler. The lint should flag generic positive adjectives (amazing, incredible, unforgettable) as low-arousal and unfalsifiable, and ask for a concrete scene that carries the awe.

## 3. Part 1B. STEPPS and social currency

Source: Jonah Berger, Contagious: Why Things Catch On (2013). I did not fetch the book. Summaries confirming the six principles: https://www.supersummary.com/contagious-jonah-berger/summary/ and https://english.ckgsb.edu.cn/knowledge/article/contagious-jonah-berger-on-why-some-things-catch-on/. The six are Social currency, Triggers, Emotion, Public, Practical value, Stories.

How each maps to an ad that people send to a friend:

| Principle | What it means | Ad-copy move | Example shape (placeholders, not verified tour facts) |
|---|---|---|---|
| Social currency | Sharing makes the sender look knowledgeable or cool | Give the reader an insider fact they can repeat | "Voss gets its snow from [verified fact]. Most visitors never ski it." |
| Triggers | Frequent cues bring the idea to mind | Tie the offer to a daily or seasonal cue | Tie to "first snowfall", "Monday commute", "payday" |
| Emotion | High arousal is shared | See 1A | A single concrete awe scene |
| Public | Visible things get copied | Make the offer easy to see and tag | A recognisable phrase, a place tag, a photo that works without the caption |
| Practical value | People share useful things | Give the number, the checklist, the comparison | "Day tour from NOK 1,948. 9 day trip NOK 42,126. Here is what each includes." |
| Stories | People carry ideas inside stories | Put the offer inside the plot | A 3-line story with a turn, not a feature list |

Evidence on practical value: in Berger and Milkman it is +30 percent for a one SD increase. The New York Times Customer Insight Group's 2011 "Psychology of Sharing" study reports that 94 percent of respondents consider how useful the information will be to the recipient before sharing. I saw this only in secondary summaries, e.g. https://contently.com/2012/02/24/psychology-of-sharing/ and https://www.shareable.net/new-research-why-people-share-content-online/. [VERIFY: primary NYT report PDF not fetched.]

How adwright should use this: build STEPPS into the brief step as six yes/no questions, and make the output name which one or two principles each variant relies on. Naming the mechanism teaches the user and makes the output screenshot-worthy.

## 4. Part 1C. Curiosity, pattern interrupts, specificity

### Information-gap theory

Loewenstein, G. (1994). The psychology of curiosity: a review and reinterpretation. Psychological Bulletin. Secondary description: https://www.ignorancegraph.com/information-gaps/information-gap-theory/ and https://psychologyfanatic.com/information-gap-theory/. The core idea: curiosity is the felt gap between what you know and what you want to know. [VERIFY: I did not read the primary. One summary I saw stated the "small gap equals high curiosity" relationship in a garbled way. Do not quote a size relationship until the primary is checked.] A safe working version: curiosity needs some prior knowledge plus a visible missing piece.

Use in ads: a headline can open a gap, but the body must close it with a real, checkable payoff. Meta's policies punish the cheap version. The Advertising Standards state ads must not contain shocking or sensational content (https://transparency.meta.com/policies/ad-standards/), and secondary summaries note reduced distribution for clickbait and engagement bait (https://savemyleads.com/blog/other/meta-ads-guidelines). [VERIFY: the specific engagement-bait wording on Meta's own page before putting it in the skill.]

### Pattern interrupts

"Pattern interrupt" is practitioner language. I found no primary academic source under that name, so no statistic here. The nearest research idea is the isolation (von Restorff) effect, where an item that differs from its context is remembered better. [VERIFY: I did not look up the primary.] In an ad feed, the interrupt must come from content (a specific number, a plain sentence in a feed of hype), not from format tricks that policies punish.

### Specificity and concreteness

Two sources with real data:
- Hansen and Wänke (2010), Personality and Social Psychology Bulletin: the same content is judged more likely true when written in concrete language than in abstract language, across four experiments. https://journals.sagepub.com/doi/10.1177/0146167210386238 (abstract via search summary; the page itself was not fetched).
- Hu, Pilgrim, Zhao and Hills (2025), "Concrete language enhances sharing of social media posts on Twitter, Reddit, and experimentally". https://pmc.ncbi.nlm.nih.gov/articles/PMC13062457/. Datasets: 15.5 million Twitter posts (Feb 2020 to Jan 2021, 35 topics), 50,517 Reddit posts from 15 subreddits, and an experiment with 167 participants over 55 pairs of manipulated posts. Concreteness predicted retweeting, and each standardised unit of concreteness was associated with about 216 more Reddit upvotes. In the experiment people picked the concrete version more often (t(166) = 15.36, p < .001). Limits the authors state: concreteness was scored word by word, platform algorithms and follower counts were not modelled, and concreteness and specificity are only weakly correlated (r = .255).

Translation: swap category words for sensory, countable things. "Adventure of a lifetime" becomes "4 hours of skinning, then a descent with nobody else on it". Numbers help because they are checkable.

How adwright should use this: the lint should score concreteness (ratio of countable, sensory, named nouns to abstract nouns), flag the abstract-adjective list, and require at least one number or named place in every variant. The brief step should ask for three verifiable facts and refuse to write without them. That also guards against invented claims.

## 5. Part 1D. Contrarian takes, moral emotion, identity signaling

### Moral-emotional language

Brady, Wills, Jost, Tucker and Van Bavel (2017), PNAS, "Emotion shapes the diffusion of moralized content in social networks". Summary pages: https://ui.adsabs.harvard.edu/abs/2017PNAS..114.7313B/abstract (fetch returned 405; figure from the search summary) and https://csmapnyu.org/research/academic-research/emotion-shapes-the-diffusion-of-moralized-content-in-social-networks. Finding as reported: each additional moral-emotional word in a message raised its diffusion by about 20 percent in polarised political discussions (gun control, same-sex marriage, climate change), mostly inside ideological groups. A later replication is reported by the same summary source. [VERIFY: confirm the 20 percent figure and the replication against the PNAS abstract.]

Do not export this to ads. The data is political tweets. In ads, moral outrage invites policy flags, comment wars and brand damage.

### Contrarian takes

A contrarian line works when it is a claim about the craft or the category that the reader can test. "Most ski ads show powder you will not get" is testable and the operator can prove its own. Contrarian takes aimed at groups of people attract the anger effect with the brand-safety cost. No peer-reviewed source here, so the guidance is judgement, not science.

### Identity signaling and social currency

Berger and Heath (2007), Journal of Consumer Research 34(2), 121-134. Consumers diverge from majorities in domains that signal identity (music, hairstyles) more than in domains that do not (backpacks, stereos). https://academic.oup.com/jcr/article-abstract/34/2/121/1793110. The ad lesson: copy for an identity-relevant product should let the buyer say who they are ("I ski the long way up") without being told who they are.

### "Say what people wish they had said"

This is a practitioner heuristic, not a finding. I found no study under that name. It lines up with social currency and identity signaling. It is the single most useful copy test for X: would a reader quote-post this line to sound sharper? [VERIFY: no academic source; keep it labelled as a heuristic in the skill.]

Meta policy limit that shapes "you" copy: Meta's Personal Attributes rule bans ads that assert or imply knowledge of a person's attributes. Practical rule from secondary guides: describe the offer, not the viewer. Primary page: https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/ (found in search; not fetched). [VERIFY: read the page before encoding examples.]

How adwright should use this: ship an "identity line" test ("Would a customer repeat this sentence about themselves?"), a "quote-post test" for X, and a policy lint for second-person claims about personal attributes. Keep moral-outrage language out of the default voice.

## 6. Part 1E. Private sharing and dark social

- The term "dark social" was coined by Alexis Madrigal in The Atlantic, 2012, "Dark Social: We Have the Whole History of the Web Wrong". Secondary summary with the 2012 Chartbeat figure (56 percent of social traffic to The Atlantic came from dark social channels on one day, vs 21.6 percent from Facebook): https://www.cmoalliance.com/dark-social-tracking-and-leveraging-private-sharing/. [VERIFY: primary Atlantic article not fetched.]
- Newer headline numbers floating around (69 percent of sharing in 2014, 84 percent recently) come from vendor blogs with unclear methods, for example https://intentamplify.com/blog/dark-social/. I do not rely on them. [VERIFY before any use.]
- The platforms themselves now count private sends. The X ranking model predicts "share via DM" and "share via copy link" as separate positive actions (README of xai-org/x-algorithm, see 1F). Instagram's named signal "sends per reach" is the same idea (secondary sources, see 1F).
- A claim that sends are worth three to five times a like for reach to non-followers circulates widely (https://socialday.live/features/instagrams-dm-share-signal-now-drives-3-to-5-times-more-reach-than-likes). The one article I checked attributes it to unnamed third-party reports, not to Instagram (https://kompozy.io/news/instagram-mosseri-ranking-signals-guidance). [VERIFY: treat as unconfirmed.]

What makes an ad sendable (design rule): it must work as one message in a chat with no context. A friend gets the image or the line plus "look at this" or "we should do this in March". So the copy must survive being forwarded: complete, concrete, and obviously about a place and a price.

How adwright should use this: add a "group chat test" to the lint (does the ad make sense with no account context, and does it include a reason to forward, such as a date, a price or a plan for two?). Offer a "send line" variant, one sentence written to be pasted into a chat.

## 7. Part 1F. Platform signals (X, Instagram, Meta ads)

### X (organic For You)

Primary source, read: https://github.com/xai-org/x-algorithm (33.5k stars on the page I fetched; Apache 2.0 per secondary summary). First published 2026-01-20, major update 2026-05-15 (secondary: https://pasqualepillitteri.it/en/news/2594/x-algorithm-open-source-may-2026).

What the README states:
- The Grok-based ranking model predicts probabilities for these actions. Engagement: favorite, reply, repost, quote, share, share via DM, share via copy link. Clicks: post, profile, link, photo expand, video open, quoted post. Attention: video quality view, dwell, dwell time, click dwell time, video continuation seconds, profile visit seconds. Author: follow author. Negative: not interested, mute author, block author, report, not dwelled.
- The score is a weighted sum: final score equals the sum of weight_i times P(action_i), with weights in `home-mixer/params/param.rs`. Weights scale predicted probabilities, not raw counts.
- After scoring: author diversity (repeat posts from one author decay), an out-of-network discount (below 1), and a new-author boost for low-impression authors.

I did not read param.rs, so I have no numeric weights. [VERIFY: read param.rs before quoting any weight.] Older third-party claims about numeric weights (for example "a reply is worth 27 likes") come from the 2023 Scala release and should not be used for the 2026 system.

Links: The README lists link click as a positive predicted action and I saw no link penalty in it. In July 2026 Elon Musk replied "We haven't for over a year" to a question about penalising posts with links, and X product head Nikita Bier said links no longer need to go in replies (https://adtechradar.com/2026/07/28/x-throttling-posts-with-links/ and https://www.freepressjournal.in/tech/x-product-head-nikita-bier-confirms-link-penalty-removed-over-a-year-ago-tells-mark-zuckerberg-he-can-post-them-directly). The adtechradar article notes it provides no code evidence and quotes a commenter saying indirect pressures may remain. [VERIFY: treat as "no known explicit penalty, lower reach can still follow from fewer people clicking through".]

Scope limit: this is the organic For You ranker. Paid X ads run through the ads stack. The README mentions an integrated ad blending system, but paid delivery has its own auction. [VERIFY with the platform researcher's notes.]

### Instagram (organic)

Adam Mosseri named watch time, likes per reach and sends per reach as the top ranking signals in January 2025, with likes slightly more important for connected reach and sends slightly more for unconnected reach. I only found this through secondary sources: https://kompozy.io/news/instagram-mosseri-ranking-signals-guidance (no dates or quotes cited), https://gyre.pro/blog/instagram-algorithm-updates-and-tips-to-boost-your-visibility and https://blckalpaca.at/en/knowledge-base/social-media/social-media-algorithms-distribution/instagram-algorithm-2026. [VERIFY: locate Mosseri's original video or Instagram post before quoting. Feed, Reels, Stories and Explore use separate ranking systems per the same secondary sources.]

### Meta ads (paid)

Ad-level diagnostics: quality ranking, engagement rate ranking, conversion rate ranking, each rated above average, average or below average, shown after about 500 impressions. Source is secondary (https://adriselab.com/learn/ad-relevance-diagnostics, https://www.mbadv.agency/meta-ads/meta-ads-metrics-reporting-and-optimization) because Meta's own page (https://www.facebook.com/business/help/403110480493160) returned no body text to WebFetch. [VERIFY: read Meta's page in a browser.]

Creative diversity: several agency articles say Meta's Andromeda retrieval system, fully rolled out around October 2025, groups near-identical creatives into one unit, so many variants with the same message count once. Quote: "Creative Similarity Scores above 60% trigger retrieval suppression" appears in secondary posts (https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026). [VERIFY: this is agency lore. The platform researcher should confirm against Meta documentation.] If it holds, adwright's "variants" command must produce conceptually different angles, not paraphrases.

### Implication for copy

| Signal the platform names | Copy behaviour that earns it |
|---|---|
| Reply, quote | A line with a clear stance or an open, answerable question |
| Share via DM, copy link, sends per reach | A complete, useful, concrete message that makes sense forwarded |
| Dwell, watch time | A first line that earns the second line; no padding |
| Likes per reach | Immediate resonance with the identity of the audience |
| Negative actions (mute, block, report, not interested) | Avoid bait, vague promises, hostile tone, repetition |
| Author diversity decay (X) | Do not post five near-identical posts in a row |

How adwright should use this: encode these as "signals checks" labelled with source and date, kept in a references file that is easy to update, because platform behaviour changes faster than craft. Date-stamp every platform claim in the skill output ("as of 2026-10").

## 8. Part 1G. What this means for ad copy (translation table)

Drafts below use placeholders in square brackets. Prices are the two Outdoor Norway figures from the brief (NOK 1,948 day tour, NOK 42,126 for the 9 day trip). All other tour facts must come from the client.

| Mechanism | Evidence strength | Meta ad move | X post move | Draft line (needs fact check) |
|---|---|---|---|---|
| Awe through a concrete scene | Strong (Berger and Milkman) | Image-led, one scene sentence | One image, one sentence | "[time] on [named ridge]. The only sound is your skins." |
| Practical value | Strong (BM +30 percent; NYT 94 percent considers usefulness) | Price plus what is included | Thread of what to pack or what it costs | "Day tour: NOK 1,948. Guide, [gear], [lunch]. Here is the rest of the list." |
| Concreteness | Moderate (Hu et al 2025; Hansen and Wänke 2010) | Numbers and named places | Same | "5 hours. 1,200 vertical metres [VERIFY]. Max group of 6 [VERIFY]." |
| Curiosity gap with a real payoff | Theoretical (Loewenstein), practitioner support | Question headline answered in body | Setup line plus reveal in reply | "Why we turn around at 14:00 [reason]." |
| Fair grievance (contrarian) | Judgement | Honest comparison | Quote-post bait that is true | "Most ski trip ads hide the price. Ours says NOK 1,948." |
| Identity | Moderate (Berger and Heath) | Speak to the type of skier, not to the person | Self-labelling line | "For people who ski for the walk up." |
| Send-ability | Platform-stated (X README, Mosseri via secondary) | Copy that works with no context | Works as a DM | "Who is free the weekend of [date]?" |
| Social proof, honest | Out of scope here, see psychology notes | Verified quote with source | Verified quote | Never invented. |

How adwright should use this: this table becomes `references/mechanisms.md`, one row per mechanism with an evidence grade. The skill picks mechanisms from the brief, then writes. Output always shows "mechanism used" next to each variant.

## 9. Part 2A. The landscape: 26 repos, live numbers

Stars and forks from the GitHub search API, 2026-10-06. "Average per day" is lifetime stars divided by age in days. It hides the early burst, so repos that spiked early look slower than they were at the start. Use it for scale only.

| Repo | Stars | Forks | Created | Age (days) | Avg stars/day | License |
|---|---|---|---|---|---|---|
| obra/superpowers | 295,794 | 26,413 | 2025-10-09 | 362 | 817 | MIT |
| mattpocock/skills | 277,384 | 23,241 | 2026-02-03 | 245 | 1,132 | MIT |
| affaan-m/ECC | 273,880 | 40,869 | 2026-01-18 | 261 | 1,049 | MIT |
| multica-ai/andrej-karpathy-skills | 217,157 | 21,862 | 2026-01-27 | 252 | 862 | MIT |
| anthropics/skills | 179,850 | 21,256 | 2025-09-22 | 379 | 475 | Apache-2.0 (document skills source-available) |
| DietrichGebert/ponytail | 156,313 | 8,398 | 2026-06-12 | 116 | 1,348 | MIT |
| garrytan/gstack | 135,436 | 20,111 | 2026-03-11 | 209 | 648 | MIT |
| addyosmani/agent-skills | 101,648 | 10,658 | 2026-02-15 | 233 | 436 | MIT |
| thedotmack/claude-mem | 96,815 | about 8.5k | 2025-08-31 | 401 | 241 | Apache-2.0 |
| Egonex-AI/Understand-Anything | 85,389 | about 7.2k | 2026-03-15 | 205 | 417 | MIT |
| tt-a1i/archify | 78,366 | 5,266 | 2026-04-15 | 174 | 450 | MIT |
| ComposioHQ/awesome-claude-skills | 76,576 | 8,965 | 2025-10-17 | 354 | 216 | Apache-2.0 |
| career-ops-hq/career-ops | 73,589 | 13,819 | 2026-04-04 | 185 | 398 | MIT |
| hesreallyhim/awesome-claude-code | 55,133 | 4,789 | 2025-04-19 | 535 | 103 | not confirmed |
| blader/humanizer | 54,276 | 4,305 | 2026-01-18 | 261 | 208 | MIT |
| ayghri/i-have-adhd | 54,056 | about 3.1k | 2026-05-13 | 146 | 370 | MIT |
| coreyhaines31/marketingskills | 53,410 | 7,943 | 2026-01-15 | 264 | 202 | MIT |
| K-Dense-AI/scientific-agent-skills | 47,738 | 4,313 | 2025-10-19 | 352 | 136 | MIT |
| wshobson/agents | 40,234 | 4,287 | 2025-07-24 | 439 | 92 | MIT |
| garrytan/gbrain | 30,583 | 4,590 | 2026-04-05 | 184 | 166 | MIT |
| alirezarezvani/claude-skills | 27,753 | 3,900 | 2025-10-19 | 352 | 79 | MIT |
| OthmanAdi/planning-with-files | 27,302 | 2,268 | 2026-01-03 | 276 | 99 | MIT |
| nidhinjs/prompt-master | 14,098 | about 1.6k | 2026-03-11 | 209 | 68 | MIT |
| latent-spaces/brag | 13,780 | about 985 | 2026-06-16 | 112 | 123 | MIT |
| AgriciDaniel/claude-ads | 9,742 | 1,444 | 2026-02-11 | 237 | 41 | MIT |
| trailhq/Graft | 9,615 | 880 | 2026-07-03 | 95 | 101 | MIT |

Existence check for the names suggested in the brief: all nine exist. anthropics/skills, obra/superpowers, garrytan/gstack, garrytan/gbrain, coreyhaines31/marketingskills, hesreallyhim/awesome-claude-code, ComposioHQ/awesome-claude-skills, AgriciDaniel/claude-ads and trailhq/Graft are all live and public. Counts move fast, so use the snapshot figures, not older ones.

Smaller marketing and ad repos for the competitive picture (same API snapshot):
- irinabuht12-oss/marketing-skills: 3,645 stars. README promotes the Ryze MCP connector, so it is partly a funnel.
- zubair-trabzada/ai-marketing-claude: 2,717 stars (marketing suite). zubair-trabzada/ai-ads-claude: 267 stars (ad copy for Google, Meta, LinkedIn, TikTok, YouTube, Pinterest).
- ivangfalco/ads-skills: 278 stars (LinkedIn, Meta, Google Ads strategy files and API scripts).
- Yuzzyuk/marketing-os: 535 stars ("copy graded before you see it", 18-tactic hook engine).
- mathiaschu/meta-ads-analyzer: 439 stars (campaign diagnosis, not copy).
- conorbronsdon/avoid-ai-writing: 4,900 stars (page figure), a deterministic 0 to 100 AI-pattern score with 74 pattern categories.

How adwright should use this: the table shows scale, not a recipe. The lesson from the fast movers is that most had a reason for strangers to care on day one, usually an author's audience. We have to create that reason from the product itself.

## 10. Part 2B. Teardowns

Each entry is from the repo's page on 2026-10-06 unless noted. Items marked "not seen" mean the fetch summary did not mention them.

### Repos in the 100k-plus class

**obra/superpowers** (295,794). Pitch: "An agentic skills framework and software development methodology that works." Install: per-harness commands for 18-plus environments, including the Claude Code official marketplace. Proof: methodology claims, an evals repo (superpowers-evals), optional version-only telemetry. License MIT. Demo: not seen. Launch: author Jesse Vincent published a blog post on 2025-10-09 (https://blog.fsck.com/2025/10/09/superpowers/), and Simon Willison wrote about it on 2025-10-10 ("There's a lot in here! It's worth spending some time browsing the repository", https://simonwillison.net/2025/Oct/10/superpowers/). Marketplace: secondary sources say it was accepted into Anthropic's marketplace on 2026-01-15 and reached over 941,000 installs by mid-July 2026 (https://www.developersdigest.tech/blog/claude-code-superpowers-plugin-guide, https://www.joanmedia.dev/ai-blog/superpowers-explained-the-plugin-that-turned-a-development-methodology-into-markdown). [VERIFY: install count.] It launched the same week Claude Code plugins launched, a timing gift.

**mattpocock/skills** (277,384). Pitch: "Skills For Real Engineers", extracted from the author's own `.agents` folder. The opening names enemies: "Approaches like GSD, BMAD, and Spec-Kit try to help by owning the process. But while doing so, they take away your control." Install: `claude plugins install mattpocock-skills` or `npx skills@latest add mattpocock/skills`. Files: AGENTS.md, CLAUDE.md, GLOSSARY.md, changesets. Audience: the README asks for a newsletter signup and states "~60,000 other devs". Demo: not seen. A third-party piece reports it as #1 on GitHub Trending with 21,900 stars on 2026-04-26 (https://byteiota.com/claude-code-skills-go-viral-22k-stars-in-24-hours/); that article itself says it cites no launch event, and the numbers are unverified. [VERIFY.]

**affaan-m/ECC** (273,880). "The agent harness performance optimization system." One guided command: `npx ecc-universal@2.2.3 setup`. 68 agents, 293 skills (README). Sponsors listed (CodeRabbit, Greptile, Moonshot AI and others). License MIT. Single maintainer shipping weekly across 7 harnesses (README claim).

**multica-ai/andrej-karpathy-skills** (217,157). A single CLAUDE.md of four principles (Think Before Coding, Simplicity First, Surgical Changes, Goal-Driven Execution). The README opens with Karpathy's own words and links his X post. Install: one `curl -o CLAUDE.md ...` or two plugin commands. Cursor rules file included. Chinese translation. 28 commits on main. Created 2026-01-27. A third-party article says the file was written within 48 hours of Karpathy's complaints and reached roughly 144k by early June (https://mer.vin/2026/06/claude-skills-star-surge-how-one-claude-md-file-hit-176k-github-stars/). [VERIFY the timeline.] The README also promotes the author's separate product. This is the clearest proof that a tiny artifact on a loud, shared frustration can outrun big frameworks.

**anthropics/skills** (179,850). The vendor's own reference repo. Install: `/plugin marketplace add anthropics/skills`. Structure: `skills/`, `spec/`, `template/`, `.claude-plugin/`. It carries the Agent Skills spec and the template other repos copy. 1,387 open issues, a sign of what maintenance debt looks like at scale. Not replicable by outsiders.

**DietrichGebert/ponytail** (156,313, created 2026-06-12). Pitch: "Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote." Opening: "He says nothing. He writes one line. It works." Proof: "~54% less code (up to 94%) / ~20% cheaper / ~27% faster", from 12 feature tasks with Haiku 4.5 and n=4. That sample is small, and the README states it, which helps trust. Concrete before/after: the date picker becomes a native `<input type="date">`. Persona voice, works with 20 agents, five slash commands including `/ponytail-gain`, translations in four languages, a sponsor, a domain. Fastest large climber in this set.

**garrytan/gstack** (135,436, created 2026-03-11). Pitch: "Use Garry Tan's exact Claude Code setup: 23 opinionated tools that serve as CEO, Designer, Eng Manager, Release Manager, Doc Engineer, and QA". Opening: a Karpathy quote, then Tan's own run-rate claim ("~810x my 2013 pace"). Install: one `git clone ... && ./setup` line, "about 30 seconds". Cross-agent: Claude Code full tier, Codex, OpenCode, Cursor, others experimental. License MIT. Demo: none seen. Launch: third-party accounts say Tan tweeted the repo on 2026-03-12 and it hit 10,000 stars within 48 hours and 60,000 in two weeks (https://www.augmentcode.com/learn/garry-tan-gstack-claude-code, https://gitpicks.dev/featured/gstack-viral-growth-github-stars). [VERIFY the day counts.] Tan said he "didn't get totally destroyed" on Hacker News (https://x.com/garrytan/status/2033020984093978930). The common critique is "a bunch of prompts in a text file". The gitpicks piece concedes the author's position drove reach: "Would a repository with identical content from an unknown developer have charted the same trajectory? Almost certainly not."

**addyosmani/agent-skills** (101,648). "Production-grade engineering skills for AI coding agents." Install: `npx skills add addyosmani/agent-skills`. 70-plus agents. Nine slash commands mapped to a lifecycle shown as an ASCII flow. Trendshift badge. Author is a well-known engineer.

### The 50k to 100k class

**thedotmack/claude-mem** (96,815). "Persistent Context Across Sessions for Every Agent". One command: `npx claude-mem install`. Badges: Apache 2.0, version, Node, "Mentioned in Awesome Claude Code", Trendshift. Animated GIF, a star-history chart, docs site, Discord, X account. The README also mentions a third-party crypto token the author "officially embraced". I note it as a risk marker, not an endorsement.

**Egonex-AI/Understand-Anything** (85,389). "Turn any codebase, knowledge base, or docs into an interactive knowledge graph". Install is a `curl ... | bash` one-liner, a PowerShell equivalent, or a plugin marketplace add. Six slash commands, 18-plus platforms. Output is a committable JSON graph viewable without an LLM. Tagline: "Graphs that teach > graphs that impress".

**tt-a1i/archify** (78,366, created 2026-04-15). "Turn any idea, plan, or codebase into a beautiful interactive diagram." Install: `npx skills add tt-a1i/archify -g`. A 35-second launch video, a live gallery of 11 scenarios, share cards at 1200 by 630 px, Discord, WeChat and QQ groups, four named sponsors. README states it was #1 on GitHub Trending (all languages) on 2026-09-01. Output is a single self-contained HTML file that anyone can open, a built-in sharing loop.

**ComposioHQ/awesome-claude-skills** (76,576). A curated list of 1,000-plus skills. Badges: Awesome, PRs welcome, Apache 2.0. A Composio banner at the top, quickstart built on Composio's connector, and 78 Composio automation skills. It is a lead-generation funnel inside an open list. License note: individual skills may differ.

**career-ops-hq/career-ops** (73,589). Outside the dev-tool bubble: a job search agent. Opens with a personal story and numbers: "740 listings evaluated. 68 applied. 12 interviews. 1 offer." Ethic stated up front: "You press Submit." It will not auto-submit, send email or phone home. Install: `npx @santifer/career-ops init`. Includes a GIF, a "hiring wall" of users' hired stories, contributor graph, and a high fork ratio (18.8 percent).

**hesreallyhim/awesome-claude-code** (55,133). Curated list, issue-form submissions only. See 2E.

**blader/humanizer** (54,276, created 2026-01-18). The closest cousin to adwright in craft. "Humanizer makes AI-written text sound like a person wrote it, without changing what it says." Built on Wikipedia's "Signs of AI writing". Shows a before and after. Proof line: "In a blind test, judges preferred Humanizer's rewrite 16 times out of 16 (#229)." 26 patterns in six groups (staging instead of stating, rhythm by rule, inflation and borrowed authority, formatting by rule, leftovers from chat, writing for the wrong reader). Badges: stars, skills.sh installs. Install: plugin marketplace, `npx skills add`. A Tech Brew review on 2026-01-21 tested it and concluded "no", because the output still registered as AI in GPTZero (https://www.techbrew.com/stories/2026/01/21/ai-writing-claude-code-plugin). The README says passing detectors is not the goal. Lesson: sell readability for humans, never detector evasion.

**ayghri/i-have-adhd** (54,056, created 2026-05-13). "ADHD-friendly outputs. No ADHD diagnosis needed!" Two before/after pairs (verbose "Hope this helps!" versus "Run `npm install jsonwebtoken@latest`"). Ten rules. Plugin configs for six agents. Evals folder. Credit to a video and a book.

**coreyhaines31/marketingskills** (53,410, created 2026-01-15). "Marketing Skills for AI Agents": about 50 skills across CRO, copy, SEO, paid media, measurement, retention, growth. Install: `npx skills add coreyhaines31/marketingskills` (marked recommended) plus six other paths. No badges and no demo seen. Plugin folders for Claude Code and Codex, tests and validation scripts. Audience: README links the author's newsletter and agency work. The broadest competitor in our category, and the proof that marketing skills draw stars.

**K-Dense-AI/scientific-agent-skills** (47,738). "Turn any AI agent into an AI Scientist." Claims "used by 250,000+ scientists" [VERIFY: unsourced claim]. 177 skills. Three install paths including `npx skills add` and `gh skill install`. Company-backed, with commercial support offered.

### The 10k to 40k class and the closest neighbours to adwright

**wshobson/agents** (40,234). Plugin marketplace, 94 plugins, 184 skills, 202 agents. Two install commands. The one with the longest age (439 days) and the lowest daily average.

**garrytan/gbrain** (30,583). "Give the agent you already use a memory you control." Install: `bun install -g github:garrytan/gbrain`, plus an explicit warning that an unrelated npm package named gbrain exists. Benchmark with caveats: "P@5 0.3421 / R@5 0.9791" against plain hybrid "0.1917 / 0.6874", and the README says these are "whole systems, not a graph-only lift or a general guarantee". Honest caveats read as credible.

**alirezarezvani/claude-skills** (27,753). 388 skills, many badges, convert script for 13 tools. Breadth-first pitch.

**OthmanAdi/planning-with-files** (27,302). "The planning skill your agent cannot ignore." Proof badges: "96.7 percent assertion pass rate" and "Blind A/B: 3 of 3 wins". An animated before/after GIF of a context reset. One command: `npx skills add OthmanAdi/planning-with-files --skill planning-with-files -g`. Credits Manus' pattern.

**nidhinjs/prompt-master** (14,098). "A Claude skill that writes the accurate prompts for any AI tool." Recommended install is ZIP upload to Claude.ai, not terminal. That matters for us: adwright's users may be marketers who do not use a terminal. 37 documented "credit-killing patterns" with before and after.

**latent-spaces/brag** (13,780, created 2026-06-16). "You built it. Now brag." One command makes a 20-second launch video with share copy. Install: `npx skills add https://github.com/latent-spaces/brag --skill brag`. Plus a web version at letsbrag.app that needs only a site URL. A third-party tracker listed it at 6.2k stars on 2026-09-21 (https://gitnova.dev/en/r/latent-spaces/brag), against 13,780 on 2026-10-06. [VERIFY: if accurate, that is about 7,500 stars in 15 days, a second wave. The output is itself a shareable artifact.]

**AgriciDaniel/claude-ads** (9,742, created 2026-02-11). Paid media operations across 12 platforms including Meta and X, with audits, copy briefs, evals and deterministic scoring. Read-only by default and approval-gated. Install is two plugin commands. A GIF (from v1). An unusual honesty note: install docs warn against piping remote installers to a shell and require SHA-256 checks for release archives. A Skool community link exists. The category leader for ads, and it is audit-first. Copy craft is not its centre. That leaves room.

**trailhq/Graft** (9,615, created 2026-07-03). Company-built. "Up to 4x cheaper and 3x faster". An animated GIF with a side-by-side run. Benchmarks on SWE-bench Verified (50 instances): correctness 54 percent to 66 percent, and a 162-run sweep. Rich badges (npm, OpenSSF scorecard, trending). `npm install -g @nanonets/graft` then `graft init`. Born two months ago, already near 10k.

How adwright should use this: copy the three most portable moves. First, humanizer-style named patterns plus a visible before/after. Second, ponytail and Graft style honest, small-sample proof stated with its own limits. Third, brag and archify style output that is itself something people post.

## 11. Part 2C. README patterns that correlate with stars

This is a survivor sample of 26 repos picked because they have many stars. It cannot show cause. It shows what the winners share. Counts come from my fetch summaries.

| Pattern | How many of the 26 showed it | Notes |
|---|---|---|
| A copyable one-line install | About 21 | Exceptions: list repos (awesome-*), anthropics/skills (two commands), prompt-master (zip upload) |
| Install by `npx skills add` or plugin marketplace | Majority | Marketplace support appears in most (superpowers, anthropics, ponytail, humanizer, claude-ads, brag, karpathy-skills, Understand-Anything) |
| Cross-agent claim (Codex, Cursor, Gemini CLI, others) | About 22 | Counts of supported agents range from 3 to 70-plus |
| Before/after that a stranger understands in seconds | At least 8 | humanizer, i-have-adhd, ponytail, prompt-master, planning-with-files, Graft, brag output, archify gallery |
| Animated GIF or video | About 7 seen (claude-mem, planning-with-files, Graft, archify, claude-ads v1, career-ops, brag) | Several 100k-plus repos had none seen (gstack, mattpocock, superpowers). Media is helpful, not required. |
| Benchmark or proof number | About 9 | Graft, ponytail, planning-with-files, gbrain, humanizer (16 of 16), gstack (productivity claim), K-Dense, claude-mem docs, career-ops personal numbers |
| Honest limits stated in the README | 3 clearly (ponytail n=4, gbrain caveat, claude-ads install warnings) | Gets read as trust |
| Persona or strong voice | 4 (ponytail, gstack, mattpocock, i-have-adhd) | Voice differentiates in a sea of "production-ready" |
| A named enemy or a named pain in line one | 5 (mattpocock vs GSD/BMAD/Spec-Kit, i-have-adhd, humanizer, karpathy-skills, ponytail) | |
| Author with a large audience | At least 6 (gstack, mattpocock, marketingskills, karpathy-skills via Karpathy, addyosmani, ECC) | Largest confounder |
| Commercial funnel in the README | 4 (Composio, K-Dense, karpathy-skills' product mention, claude-ads' Skool) | Does not block stars |
| MIT license | 22 of 26 | Apache-2.0 for anthropics, claude-mem, Composio |
| High fork ratio (above 14 percent) | gstack 14.8, career-ops 18.8, gbrain 15.0, marketingskills 14.9, claude-ads 14.8, openclaw 21 | These are repos people adapt, not just star |

Two patterns I did not expect:
- Badge walls are rare in the top ten. The biggest repos use few or no badges.
- Skill count is not the story. The fastest climbers (ponytail, karpathy-skills, archify, i-have-adhd, brag) each do one thing. Breadth-first repos (alirezarezvani 388 skills, wshobson 184) have a much lower daily average.

How adwright should use this: ship one verb and one before/after. Avoid a skills catalogue. Put install above the fold. Have claude.ai ZIP, Claude Code plugin, `npx skills add` and a plain paste-in prompt, because marketers may not use a terminal.

## 12. Part 2D. Growth timing and launch channels (what the evidence supports)

What I could verify live: creation date and today's count. That gives lifetime averages only (section 9).

What third parties report, all [VERIFY] until the stargazer timeline is pulled:
- gstack: created 2026-03-11, tweet 2026-03-12, 10,000 stars in 48 hours, 60,000 in two weeks, 89.7k "in under two months", 100k by about late May (https://www.augmentcode.com/learn/garry-tan-gstack-hits-89.7K-stars, https://x.com/rohit4verse/status/2058682520074608946).
- karpathy-skills: created 2026-01-27, 144k by early June (mer.vin).
- mattpocock/skills: created 2026-02-03; "#1 trending at 21,900 stars" on 2026-04-26 (byteiota, article admits missing launch details).
- humanizer: created 2026-01-18, covered by Tech Brew on 2026-01-21. A search snippet showed 347 stars at some early point. [VERIFY.] Today 54,276.
- archify: README claims #1 on GitHub Trending (all languages) on 2026-09-01.
- brag: 6.2k on 2026-09-21 per a tracker, 13.8k on 2026-10-06.
- Superpowers: 2025-10-09 launch blog post, Willison 2025-10-10, "174,000 stars in seven months", 254,696 by mid-July 2026 (secondary).

Channels that actually appear in evidence:
- Author's own X post (gstack, karpathy-skills' linked Karpathy post).
- A known writer's blog (Willison on Superpowers).
- Newsletter list (mattpocock's README: about 60,000 subscribers; marketingskills links the author's newsletter).
- Hacker News: Show HN posts about Claude Code in the 150-plus point band mostly scored 160 to 450 points (the list's top, 749, is a non-skill project). Examples: "Claude Code skills that build complete Godot games" (337 points, 2026-03-16), "Semble" (445), "Stop Claude Code from forgetting everything" (202, 2025-12-29). Pulled from the HN Algolia API with a filter above 150 points, so it shows the upper range only: https://hn.algolia.com/api/v1/search?query=claude%20code%20skill&tags=show_hn&hitsPerPage=30&numericFilters=points%3E150. Reception can be mixed (Tan on his HN thread).
- GitHub Trending and Trendshift (below).
- Skills directories that list by install telemetry (skills.sh, below).
- Awesome lists (below).

Channel claims I could not verify: any Reddit r/ClaudeAI star yield, Product Hunt yield, or newsletter pickups for specific repos. One blog says a front-page Show HN gives "approximately 6 hours" to the first 1,000 stars and Reddit r/selfhosted yields 50 to 300 stars per post (https://dev.to/iris1031/how-to-get-more-github-stars-the-definitive-guide-33k-stars-case-study-2kjo). [VERIFY: single-author blog, different niche.]

How adwright should use this: plan launch around three amplifiers we can actually reach: a founder-level X thread with a visual proof, a Show HN with a working demo, and one or two relevant writers or newsletters pitched with a finished before/after, not a repo link. Record star timestamps daily from day 1 so the next team has real data.

## 13. Part 2E. Distribution rails

### Awesome-list inclusion

hesreallyhim/awesome-claude-code accepts submissions only through its web issue form. Rules from CONTRIBUTING (https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/main/CONTRIBUTING.md): a resource qualifies if it is at least 14 days old (since first commit on the default branch) and shows active development, or has at least 100 stars. One submission per person at a time. Proper licence information must be discoverable. Paid or signup-gated resources are blockers. Descriptions must be factual and non-promotional, with no emojis and no addressing the reader. No guarantee of a response. The maintainer warns that the list is not a marketing strategy. Pull requests and CLI submissions are refused.

Planning consequence: make the repo public with real commits at least 14 days before the launch so it is eligible on day 1.

Other lists: VoltAgent/awesome-agent-skills (35,259), ComposioHQ/awesome-claude-skills (76,576, funnel-driven, has a CONTRIBUTING file), travisvn/awesome-claude-skills (15,283), sickn33/agentic-awesome-skills (47,291). [VERIFY each list's current submission rules before submitting.]

### Trendshift and GitHub Trending

- Trendshift (https://trendshift.io/) tracks repos by "monthly engagement metrics" (stars, forks, merged PRs, issues, closed issues) and records which repos trended and for how long (https://dev.to/liweiyi88/new-repository-engagements-page-on-trendshiftio-4p8p, https://trendshift.io/github-trending-repositories). A Trendshift badge appears on claude-mem and addyosmani/agent-skills. Graft shows a "trending" badge whose source I could not confirm. Activity beyond stars (merged PRs, closed issues) counts, which rewards visible maintenance.
- GitHub's own Trending page has no published ranking criteria. A community discussion reports the lists froze on 2025-11-13 and GitHub staff said on 4 December they fixed a data pipeline issue (https://github.com/orgs/community/discussions/179946). Plan for trending as a bonus, not a channel.

### How skills get listed

- Vercel's skills CLI: `npx skills add owner/repo`. A repo is indexed automatically after its first install, and anonymous install telemetry drives the skills.sh leaderboard (https://vercel.com/changelog/introducing-skills-the-open-agent-skills-ecosystem, 2026-01-20, the page says 18 agent platforms; https://qaskills.sh/blog/skills-sh-agent-skills-directory-guide). So early installs matter as ranking input. Telemetry can be disabled by users (DISABLE_TELEMETRY), so counts undercount. Listing is not vetting.
- Anthropic plugin directory: submit through the developer portal at claude.ai/directory/manage (https://claude.com/docs/plugins/submit). Steps: connect GitHub, Validate, listing details from `plugin.json` and README, data-handling answers, compliance acknowledgements, Submit for review. Each submission is scanned for validation and security, can be held for a reviewer, and publishing needs a public repo. A reviewer publishes each version by default. Limit: 10 submissions per organisation per 24 hours. Run `claude plugin validate ./<folder>` first. Review time is not stated. [VERIFY: timeline.]
- Self-hosted marketplace: any GitHub repo with `.claude-plugin` can be added with `/plugin marketplace add owner/repo` (this is how anthropics/skills, humanizer and claude-ads are installed). No approval needed.
- Agent Skills spec (https://agentskills.io/specification): `SKILL.md` with frontmatter. `name` up to 64 characters, lowercase letters, digits and hyphens, no leading, trailing or double hyphens, must match the directory name. `description` 1 to 1,024 characters and should say what the skill does and when to use it. Optional `license`, `compatibility` (500 characters), `metadata`, `allowed-tools`. Keep SKILL.md under 500 lines and about 5,000 tokens, with detail in `references/`. Metadata is loaded at startup (about 100 tokens), so the description is the only thing that decides whether the skill fires. Validate with `skills-ref validate ./my-skill`.

How adwright should use this: the description line in SKILL.md is the most important sentence in the repo for activation, and the first install through `npx skills add` is what seeds the directory. Plan a launch-day install push from real users, not scripts.

## 14. Part 2F. The competitive gap in ads

What exists (all from the API snapshot and fetched pages):
- Audit and operations: claude-ads (9,742). Meta, X and ten others. Evidence-based audits, scoring, drafts for approval. Not centred on voice.
- General marketing libraries: marketingskills (53,410), alirezarezvani (27,753), irinabuht12-oss (3,645), zubair-trabzada suites. They cover copywriting and ads as one skill among dozens.
- Small ad-copy skills: ai-ads-claude (267), ads-skills (278), marketing-os (535).
- Writing-quality skills: humanizer (54,276), avoid-ai-writing (about 4.9k). They fix AI tells in any prose, not ad craft for Meta and X.

Gap: a focused, human-sounding, platform-specific ad writer with a measurable lint and a public before/after gallery. I found no repo that combines named ad-craft mechanisms, a deterministic score and proof against a baseline. I did not search every repo on GitHub, so say "I could not find", not "none exists".

How adwright should use this: position as a writer, not an audit suite or a library. Complement claude-ads by exporting briefs that its audit can score. Cite the neighbours kindly in the README.

## 15. Part 2G. Base rates, control versus luck, and why faking is off the table

### Base rates

From the GitHub search API on 2026-10-06, repos with topic `claude-code` created on or after 2026-01-01:

| Filter | Count |
|---|---|
| All | 80,519 |
| At least 1 star | 42,131 |
| More than 100 stars | 2,137 |
| More than 1,000 stars | 425 |
| More than 10,000 stars | 60 |
| More than 50,000 stars | 17 |

- Share above 10,000 stars after up to nine months: 60 of 80,519, about 0.075 percent. Share above 1,000: about 0.53 percent. Caveats: topic tags are self-applied and the denominator includes many throwaway repos, so the true rate for a serious repo is higher. The 30-day subset is smaller than any figure here. I could not extract first-30-day star counts.
- Skills repos in the top group cluster in one period, when Anthropic's skills and plugin systems and the agent-skills standard were new. The category was young and hungry.
- For ad copy specifically, the evidence points lower: 9,742 (claude-ads) and 53,410 (marketingskills) are the best, each after about eight to nine months.

### What the top outcomes needed (observed)

1. An existing distribution asset: Tan's X audience, Pocock's newsletter, a Karpathy post, a vendor.
2. A universal pain in one sentence ("agents bury the answer", "agents overbuild").
3. Install in one line across many agents.
4. A before/after a stranger gets at once.
5. Timing with a platform event (Claude Code plugins launch week for Superpowers).
6. A big company behind it (Graft's team, Composio, K-Dense) or a trusted individual.

### Control and luck

| In our control | Mostly luck or borrowed |
|---|---|
| README quality, a demo that proves the claim in 10 seconds | Whether a large account posts about it |
| Install friction (one command, several agents, claude.ai ZIP) | Hacker News front-page timing and mood |
| Honest proof, benchmarks, published raw data | Hitting a nerve at the same time as a news event |
| Shareable output (lint card, before/after) | Whether GitHub Trending runs normally that week |
| Fast responses on issues, weekly releases | Competitor launches in the same week |
| Submitting to every legitimate rail on schedule | Platform policy changes (Meta, X) |
| Relationships with a few writers and newsletter owners | A skill-directory algorithm change |

### Why buying stars or faking engagement is off the table

- Rules: GitHub's Acceptable Use Policies prohibit "inauthentic interactions, such as fake accounts and automated inauthentic activity" and "rank abuse, such as automated starring or following" (https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies, section 4).
- Detection: researchers at Carnegie Mellon and NC State built StarScout and found about 4.5 million suspected fake stars across 15,835 repos in the first version of their paper (later revised to six million). Fake-star activity surged in 2024 (https://arxiv.org/abs/2412.13459). A secondary report says almost 16 percent of repos with 50 or more stars in July 2024 were linked to campaigns (https://cyberinsider.com/github-plagued-by-4-5-million-fake-stars-problem-misleading-users/). [VERIFY: the 16 percent figure.]
- Benefit: the paper says fake stars give only short-term promotional benefit, under two months.
- Reputation: the study finds most fake-star repos promote malware or scams. A skill that goes after trust in advertising cannot afford to look like one.
- Practical: the repos that rank highest on Trendshift and in skills.sh are ranked on forks, merged PRs, installs and issues, which fake stars do not produce.
- For the client: Outdoor Norway's brand name would be attached to the project. A scandal would cost more than any star count.

The same applies to fake comments, bot installs inflating skills.sh telemetry, "star for star" swaps and coordinated vote rings on Hacker News or Reddit (both sites prohibit voting rings; [VERIFY] each site's current rule text).

How adwright should use this: commit publicly to "no purchased or exchanged engagement" in CONTRIBUTING and the launch post. Track stars, installs, forks and merged PRs together so the project is judged on real use.

## 16. Part 3A. README blueprint for adwright

Principles taken from sections 10 and 11: first screen must show the result, install must fit in one line per environment, proof must carry its own limits, voice must sound like a person.

Pitch candidates (pick one after testing on five strangers):
- "Ads that sound like a person wrote them. For Meta and X."
- "Write the ad. Lint the ad. Ship the ad people send to a friend."
- "Stop shipping ads that smell like AI."

Section-by-section:

1. **Title and one-line pitch.** Name, pitch, a single sentence of scope: Meta (Facebook, Instagram) and X. Under 25 words.
2. **Hero before/after.** A real, ugly, plausible AI-written ad on the left and the adwright rewrite on the right, plus a lint score ("31/100" to "88/100" once the lint exists). Use text, not an image, so it can be copied. Include one Meta ad and one X post.
3. **10-second terminal GIF** (or short video). One command in, ad out, score shown. Use a real run. Under 3 MB.
4. **Install block.** Four lines, one per environment: `npx skills add <owner>/adwright`; `/plugin marketplace add <owner>/adwright`; claude.ai ZIP upload (link to release asset); paste-in prompt for any chat tool. Name Codex, Cursor and Gemini CLI explicitly in a one-line support table.
5. **First minute.** Three example prompts a marketer would actually type, with the output shape.
6. **Commands.** Five verbs, not fifty: `write`, `rewrite`, `lint`, `variants`, `explain`. One line each.
7. **Proof.** A blind-test table with sample size, method, raw data link and limits. Example format: "20 ad pairs, 12 reviewers, preferred 31 of 40 times"; fill only with real results. State what the test cannot show (conversions).
8. **How it works.** The twelve to twenty rules, each with a source. Link to `references/`. Make clear the rules are public and editable.
9. **Gallery.** Twelve real before/after pairs for Meta and X, with permission. Include Outdoor Norway ski ads once cleared by the client, using their real prices and facts only.
10. **Platform notes.** Date-stamped limits and policy lints (character counts, Meta personal-attributes rule, sensational content), each with a source link. Say "as of 2026-10".
11. **Honest limits.** What it will not do: invent testimonials, promise virality, evade AI detectors, publish ads for you.
12. **Contributing.** "Add a pattern in one file." Label good first patterns. Evals run with one command.
13. **Credits and licence.** MIT. Credit Berger, Loewenstein, the Wikipedia AI-signs guide if used, and neighbours (humanizer, claude-ads).
14. **Optional footer.** A line users may add to their own public posts. Off by default.

Repo structure:

```
adwright/
  README.md
  SKILL.md                 (under 500 lines; description under 1,024 chars)
  AGENTS.md                (cross-agent entry)
  LICENSE
  CONTRIBUTING.md
  PROOF.md                 (adwright linted by adwright, dated)
  CHANGELOG.md
  .claude-plugin/          (plugin.json, marketplace.json)
  references/
    mechanisms.md          (section 8 table, with evidence grades)
    meta.md                (limits, policy, formats; dated)
    x.md                   (limits, signals; dated)
    voice-rules.md         (the style rules; banned patterns)
    lint-patterns.md
  scripts/
    lint.(py|js)           (zero dependency, deterministic, no network)
  evals/                   (blind-test set, rubric, results)
  examples/                (the gallery source)
  assets/                  (GIF, social preview image)
```

Badges: licence, version, "Agent Skills", skills.sh installs once they exist. Four maximum.

## 17. Part 3B. Twelve name candidates with collision checks

"adwright" is the working name. Checks run on 2026-10-06:
- GitHub: repository search by name (API).
- npm: registry.npmjs.org status (404 means free).
- PyPI: pypi.org JSON status (404 means free).
- Domains: RDAP lookup (200 means registered, 404 means not registered). `.ai` lookups returned 429 for some names (rate limit), marked unknown. Confirm availability at a registrar before relying on any "free" result.
- Web: WebSearch brand check, where the search budget allowed.
- Not legal advice. [VERIFY: run a trademark search in the EU and US classes 9, 35 and 41 before committing.]

### Candidates

| # | Name | GitHub (exact name) | npm / PyPI | .com / .dev | Web brand check | Verdict |
|---|---|---|---|---|---|---|
| 1 | adwright | 0 repos by that name. Two personal github.io pages with the string (ADWright18, adwright2) | free / free | .com registered, .dev not registered, .ai registered | Taken as a company name: Ad.Wright Communications Pte Ltd, a Singapore branding and ad agency founded in 1996, adwright.com (https://clutch.co/profile/adwright, https://www.crunchbase.com/organization/adwright) | Free in developer namespaces. Occupied in the commercial one. Moderate trademark risk. Keep only if a lawyer says OK. |
| 2 | adkiln | 0 | free / free | .com registered, .dev not registered | No brand found | Cleanest result. Meaning: fire-hardened ads. Unclear to newcomers. |
| 3 | adhonest | 0 | free / free | .com registered, .dev not registered | "Honest Ads" is a TikTok and Instagram parody account and the US "Honest Ads Act" is a political ad bill (https://www.honestads.org/) | Clean in code namespaces. The phrase has political baggage. |
| 4 | adplain | 0 (AdPlainer, 2022, 0 stars) | free / free | .com registered, .dev not registered | Not checked (search budget) | Good meaning (plain-spoken). Check web. |
| 5 | adhand | 1 abandoned repo, 0 stars, plus unrelated strings | free / free | .com registered, .dev not registered | Not checked | Meaning: handmade ads. Short. Check web. |
| 6 | hookwork | 2 old repos (C++ hook framework, 2 stars; 1 star TypeScript) | free / free | .com registered, .dev not registered | Not checked | "Hook" collides with Claude Code hooks, which are a feature. Confusing. |
| 7 | adloom | 4 or more tiny repos named adloom (0 stars) | free / free | .com registered, .dev not registered | Not checked | Crowded with student projects. |
| 8 | adwrite | 7 hits, all 0 stars | free / free | .com registered, .dev not registered | Not checked | Generic, weak for search. |
| 9 | adlint | AdLint (Google Ads and GTM audit tool, 1 to 3 stars), AdLint legacy C analyzer (SourceForge) | free / free | .com registered, .dev and .ai not registered | Two existing tools with the same name (https://github.com/ChristopherLandaverde/adlinter, http://adlint.sourceforge.net/) | Better as the name of the lint command than the product. |
| 10 | adquill | 0 (adquilla unrelated) | free / free | .com registered, .dev not registered, .ai unknown | Search surfaced AdQuick (out-of-home platform), not AdQuill | Clean, close to AdQuick in sound. |
| 11 | plainads | 0 | free / free | .com registered, .dev and .ai not registered | Not checked | Describes the value. Check web. |
| 12 | wrightads | 0 | free / free | .com registered, .dev not registered | Not checked | Same root as the working name, same Singapore agency concern. |

### Rejected after checks (kept for the record)

| Name | Reason |
|---|---|
| adsmith | npm name held by a placeholder ("Name hold", modified 2026-10-04); PyPI adsmith is a Google Ads MCP server; 3 same-name repos including one for ad creative with Claude |
| adforge | npm adforge is a Meta ad pipeline for Claude Code and Codex (v0.3.5, JonnyFi/adforge), the same space |
| adcraft | AdCraft (GML-MMGroup, 368 stars) is an agentic ad video platform; npm name is a Turborepo starter |
| hookwright | npm package for Shopify webhooks; a WordPress plugin called Deftmind Hookwright; a GitHub org named hookwright |
| copywright | Misspelling of copyright, bad for search; tiny "AI marketing copy" repo with same name |
| adfoundry | Real companies: AdFoundry LLC (Madison, WI agency), Ad Foundry CPA network, adfoundry.io |
| adscribe | Real company (AdScribe, London TV data, now iSpot) and an iOS "AI Ad Copy Generator" app |
| hookcraft | npm hookcraft is a TypeScript SDK for Claude Code hooks, same ecosystem |
| adsharp | Several companies (Tampa web studio since 1999, UK media buyer, a growth agency) |
| adtrue | AdTrue is an ad network with SDK repos |

Naming evidence from the survey: the biggest names describe a benefit or a character (humanizer, superpowers, ponytail, brag, archify). None of the 26 is a made-up compound like "adwright". The repo description and pitch have to do the explaining. Whatever the brand, set the GitHub description to the plain pitch, and add topics: `agent-skills`, `claude-code`, `claude-skills`, `copywriting`, `meta-ads`, `facebook-ads`, `instagram-ads`, `x-ads`, `advertising`.

How adwright should use this: decide between keeping "adwright" and a cleaner name this week, because the name shows up in the install command, the plugin ID and every link. The strongest on collision evidence are adkiln and adquill. The strongest on meaning are adplain and plainads, pending a web check. If adwright is kept, register adwright.dev and the GitHub org name and file the trademark check.

## 18. Part 3C. Launch checklist and 30-day plan

Assume the target date for public launch is Day 0. Pre-launch work starts at Day -21.

### Pre-launch checklist (Day -21 to Day -1)

Product:
- [ ] One verb works end to end: `write`, `rewrite`, `lint`. Zero-dependency lint script. No network calls in scripts.
- [ ] SKILL.md under 500 lines, description under 1,024 characters, validated with `skills-ref validate`.
- [ ] `claude plugin validate` passes. `.claude-plugin/plugin.json` has description, author, homepage, repository.
- [ ] Tested install on Claude Code, Codex, Cursor, Gemini CLI, claude.ai ZIP. Record what fails.
- [ ] Evals: 20 or more ad pairs (baseline model output versus adwright) with a blind rubric and at least 10 independent reviewers, raw data published. [Do not publish a headline number until it is real.]
- [ ] Twelve real before/after pairs for Meta and X, with permission.
- [ ] PROOF.md: adwright's own README and examples linted by adwright, score and date.

Repo hygiene:
- [ ] Make the repo public by Day -14 with real commits, so awesome-claude-code's 14-day rule is met on Day 0.
- [ ] LICENSE (MIT), CONTRIBUTING (including the no-fake-engagement pledge), CODE_OF_CONDUCT, issue templates, Discussions on.
- [ ] Topics set. Social preview image added. Release v0.1.0 with a ZIP asset for claude.ai.
- [ ] README tested on five strangers: can they say what it does in five seconds and install in 60?

Distribution prep:
- [ ] Submit to the Anthropic directory through the developer portal early, because review time is unstated. Private repo is allowed during review but must be public to list.
- [ ] Draft submissions to awesome lists (one at a time for awesome-claude-code).
- [ ] Draft the Show HN text (plain, specific, first-person, no hype), the X thread (see 3D for visual), the Reddit post for r/ClaudeAI, and a short pitch email to three to five writers or newsletter owners with a working before/after attached.
- [ ] Decide who is the face. Starred repos are often a person. One named author with a real voice beats an anonymous brand.
- [ ] Client consent for any Outdoor Norway material in the gallery.

### The 30-day plan

| Day | Action | Metric to watch |
|---|---|---|
| -14 | Repo public, soft launch to 10 to 20 friendly users | Install failures |
| -7 | Fix top three install and quality issues. Freeze README. | README comprehension test |
| 0 (Tue to Thu) | Publish v0.1.0. Show HN with a working demo and the real eval result. X thread with the GIF and one before/after. Post in r/ClaudeAI. Email the writers. Submit to awesome-claude-code via the issue form. | Stars per hour, installs, comments, issue count |
| 1 | Answer every comment and issue within hours. Fix the first reported bug the same day and say so publicly. | Time to first response |
| 2 to 3 | Post a short "what people asked" follow-up with the three best questions. Share two community before/afters (with permission). | Forks, merged PRs |
| 4 to 7 | Release v0.1.1 with the top requests. Post one platform-specific before/after per day for Meta and X (own examples or permissioned). Seed `npx skills add` installs from real users so the skills.sh listing builds. | skills.sh rank, install count |
| 8 to 10 | Write one real essay: "What the science says makes an ad worth sending" built from section 1 with sources. Publish on the project site and cross-post. | Referral traffic |
| 11 to 14 | Submit to other awesome lists (VoltAgent, others) per their rules. Pitch a second round of writers with the essay plus gallery. Offer a free "lint your ad" live session. | Mentions, newsletter pickups |
| 15 to 21 | v0.2: `variants` that produces conceptually different angles; Meta and X policy lints; Norwegian and other language notes if requested. Publish the first case study with real numbers when the client approves. | Retention (repeat users via issues, Discussions) |
| 22 to 28 | Publish eval v2 including community-submitted ad pairs and honest failures. Run a "worst ad of the week" teardown on public brand ads, criticising copy, never people. | Contributor count |
| 29 to 30 | Retrospective post with real numbers: stars by day, installs, forks, issues, what failed. Publish the stargazer timeline so others can learn. | Final tally |

Targets (honest, not promises): by Day 30, 1,000 to 3,000 stars is a strong outcome for this category given the ceiling in section 14. 10,000 needs luck or a large amplifier, such as a major account sharing it. [No forecast is attached to these ranges. They are judgement from the table in section 9.]

Cadence rules:
- One post a day for the first week. Then three a week.
- Never post a screenshot without the text version for accessibility and copy.
- Never ask for stars. Ask for ads to test.

How adwright should use this: treat Day 0 as the start of a long tail, because skills.sh ranking, Trendshift (monthly engagement) and awesome lists all reward sustained activity, not one spike. Budget for ten hours a week of maintenance after launch.

## 19. Part 3D. Shareable-by-design mechanics

Each mechanic should pass one test: does it give a reader something to send, quote or screenshot, and does it work without asking anyone to promote the project?

1. **Lint score for any ad.** `adwright lint "ad text"` returns 0 to 100 with named issues (abstract adjectives, missing number, hedge words, second-person policy risk, AI tells). Deterministic, public rules, and a self-audit in PROOF.md, as avoid-ai-writing does with its 0 to 100 detector and PROOF.md. People post scores, especially bad ones.
2. **Before/after command.** `adwright rewrite` outputs a side-by-side diff and the three rules that changed it. This copies the format that powers humanizer's README.
3. **Mechanism receipt.** Each variant ends with one line: "Uses: concreteness, practical value. Risk: price claim needs proof." It teaches while it writes.
4. **Group-chat line.** Each set of variants includes one sentence written to be pasted into a chat. It serves the "sends" signal on both platforms.
5. **Share card.** `adwright card` exports a 1200 by 630 PNG with before, after and score. archify does this with route cards. Include no logo by default.
6. **Optional "made with" footer.** A one-line footer for the user's own blog posts or case studies, off by default, and never inside the ad copy that goes to customers. Putting a tool credit inside an ad would hurt the ad.
7. **Platform check.** Character counts and truncation for X and Meta, and a policy lint (personal attributes, sensational content, urgency claims). Date-stamped. [VERIFY exact limits with the platform notes.]
8. **Variant diversity check.** Warn when two variants share the same angle, since Meta's retrieval system may treat near-duplicates as one (see 1F, agency claim, [VERIFY]).
9. **Public eval harness.** `evals/` lets anyone run the blind test on their own ads. Honest failures get published. A rule that makes an ad worse in tests is removed.
10. **Gallery PRs.** Anyone can submit a before/after through a template. Accepted entries credit the contributor. This turns users into a distribution channel, like the hiring wall in career-ops.
11. **Outputs that are themselves posts.** A single-file HTML "ad review" report, like archify's HTML output, that a marketer can send to a boss. Plain, no tracking.
12. **Weekly teardown.** A dated public post critiquing a well-known brand ad with the lint and the rewrite. Criticise copy, not people. Skip anything that targets a private individual.

How adwright should use this: build 1, 2 and 3 for v0.1, 4 and 5 for v0.2, and treat 6 to 12 as backlog ordered by effort. The order matters because lint score, before/after and the mechanism receipt are the only mechanics that make a screenshot out of a single command.

## 20. Part 3E. Risks

| Risk | Why it matters | Mitigation |
|---|---|---|
| Star target missed | Base rate in section 15; ad copy ceiling in section 14 | Judge on installs, merged PRs, real ads shipped. Publish the numbers. |
| "It's just prompts in a text file" | The same criticism hit gstack (https://gitpicks.dev/featured/gstack-viral-growth-github-stars) | Ship a deterministic lint script, evals and a published rule set with sources. |
| Hostile reception on HN or Reddit to AI-written READMEs and AI-sounding launch posts | The product's whole promise is human voice | Write the README and launch posts by hand. Run them through the lint. Publish the score. |
| Name conflict | Ad.Wright Communications (Singapore) holds adwright.com and a 1996 brand | Trademark search; consider adkiln, adquill or a descriptive name. |
| Policy mistakes in generated ads | Meta bans ads that imply knowledge of personal attributes and ads with sensational content | Policy lint with cited rules; refuse risky claims; show the rule on the output. |
| Invented claims, testimonials or scarcity | Legal risk, brand harm, platform enforcement | Brief step requires verifiable facts; skill refuses to invent proof; content-qc pass for client work. |
| Detector-evasion promises | Tech Brew found humanizer output still flagged by GPTZero | Never claim to beat detectors. Claim readability. |
| Weak or small-sample benchmarks | A loose number draws attacks, and it attracts comparison to ponytail's n=4 | State sample size and limits next to every number. Publish raw data. |
| Platform guidance goes stale | X and Instagram change often; several claims here rest on secondary sources | Date-stamp every platform note, keep it in `references/`, set a quarterly review. |
| Maintenance overload | anthropics/skills has 1,387 open issues, Composio's list has 1,642 | Issue templates, a small scope, triage rota, a stale bot with a polite message. |
| Security perception | Skills can run scripts. Some repos use `curl | bash` installers, while claude-ads documents why not | No remote fetches in scripts; checksum release ZIP; state it in the README. |
| Funnel suspicion | Repos that are lead-gen look like ads (Composio's list, Ryze-linked repo) | Keep any client or agency promotion to one clearly labelled line. |
| Client entanglement | Outdoor Norway's name and prices could appear in the gallery | Written consent, real figures only, no confidential performance data without sign-off. |
| Fake engagement by third parties | Bots may star the repo and invite suspicion | Do not respond in kind; report to GitHub if clear abuse. |
| Dependence on one ecosystem | skills.sh telemetry and Anthropic's directory rules can change | Support the open Agent Skills spec and plain paste-in prompts. |

How adwright should use this: write the top five risks into the repo's `docs/` as a public "known risks" page. That reads as honest and pre-empts the main objections.

## 21. Verification log

Verified from primary sources in this session:
- Berger and Milkman 2012 numbers: PDF read in full for the abstract, data description (6,956 articles, 2008-08-30 to 2008-11-30, 20 percent most-emailed) and Figure 2 values.
- xai-org/x-algorithm README: action list, score formula, post-ranking adjustments.
- agentskills.io specification: field limits.
- Anthropic plugin submission documentation (claude.com/docs/plugins/submit).
- awesome-claude-code CONTRIBUTING.
- GitHub Acceptable Use Policies, section 4 clauses.
- arXiv 2412.13459 abstract page: title, authors, versions, short-term benefit statement.
- Vercel skills changelog (2026-01-20).
- All repo stars, forks, created dates, topics, base-rate counts (GitHub search API).
- npm, PyPI and RDAP status codes (curl).

Secondary or unconfirmed (tagged [VERIFY] above):
- Instagram's three top ranking signals and the "3 to 5 times" send multiplier.
- X link-penalty removal (statement by Musk and Bier, no code evidence in the article).
- Meta ad relevance diagnostics details and Andromeda similarity thresholds.
- gstack, karpathy-skills, mattpocock and brag star timings.
- Superpowers install count and marketplace acceptance date.
- Dark social percentages.
- NYT Psychology of Sharing 94 percent figure (secondary summaries).
- Brady et al 2017 "20 percent per word" (summary pages).
- Loewenstein's relationship between gap size and curiosity (primary not read).
- Show HN and Reddit star-yield numbers (single blog).
- Web brand checks for candidate names 4 to 8, 11 and 12 (search budget exhausted).

Not obtained: star-by-day timelines for any repo, Product Hunt and Reddit yields for skills repos, trendshift scoring formula.

## 22. Source list (main URLs)

- Berger and Milkman 2012 PDF: https://jonahberger.com/wp-content/uploads/2013/02/ViralityB.pdf
- Berger and Heath 2007: https://academic.oup.com/jcr/article-abstract/34/2/121/1793110
- Hu et al 2025 concreteness and sharing: https://pmc.ncbi.nlm.nih.gov/articles/PMC13062457/
- Hansen and Wänke 2010: https://journals.sagepub.com/doi/10.1177/0146167210386238
- Brady et al 2017: https://ui.adsabs.harvard.edu/abs/2017PNAS..114.7313B/abstract
- X algorithm repository: https://github.com/xai-org/x-algorithm
- X link statements: https://adtechradar.com/2026/07/28/x-throttling-posts-with-links/
- Instagram signals (secondary): https://kompozy.io/news/instagram-mosseri-ranking-signals-guidance
- Meta ad standards: https://transparency.meta.com/policies/ad-standards/
- Meta personal attributes: https://transparency.meta.com/policies/ad-standards/objectionable-content/privacy-violations-personal-attributes/
- Fake stars paper: https://arxiv.org/abs/2412.13459
- GitHub AUP: https://docs.github.com/en/site-policy/acceptable-use-policies/github-acceptable-use-policies
- Agent Skills spec: https://agentskills.io/specification
- Anthropic plugin submission: https://claude.com/docs/plugins/submit
- Vercel skills changelog: https://vercel.com/changelog/introducing-skills-the-open-agent-skills-ecosystem
- awesome-claude-code contributing: https://raw.githubusercontent.com/hesreallyhim/awesome-claude-code/main/CONTRIBUTING.md
- GitHub Trending bug thread: https://github.com/orgs/community/discussions/179946
- Trendshift: https://trendshift.io/
- Superpowers launch: https://blog.fsck.com/2025/10/09/superpowers/ and https://simonwillison.net/2025/Oct/10/superpowers/
- gstack growth (secondary): https://gitpicks.dev/featured/gstack-viral-growth-github-stars
- Humanizer review: https://www.techbrew.com/stories/2026/01/21/ai-writing-claude-code-plugin
- Repos (all fetched 2026-10-06): github.com/obra/superpowers, mattpocock/skills, affaan-m/ECC, multica-ai/andrej-karpathy-skills, anthropics/skills, DietrichGebert/ponytail, garrytan/gstack, garrytan/gbrain, addyosmani/agent-skills, thedotmack/claude-mem, Egonex-AI/Understand-Anything, tt-a1i/archify, ComposioHQ/awesome-claude-skills, career-ops-hq/career-ops, hesreallyhim/awesome-claude-code, blader/humanizer, ayghri/i-have-adhd, coreyhaines31/marketingskills, K-Dense-AI/scientific-agent-skills, wshobson/agents, alirezarezvani/claude-skills, OthmanAdi/planning-with-files, nidhinjs/prompt-master, latent-spaces/brag, AgriciDaniel/claude-ads, trailhq/Graft, conorbronsdon/avoid-ai-writing

How adwright should use this: keep this file as the evidence base. When a `[VERIFY]` item is resolved, update `references/` in the skill and the dated platform notes, not this file's conclusions.
