# AI writing pitfalls, and the cure, for ad and travel copy

Research notes for the adwright skill. Written 2026-10-06. Client: Outdoor Norway (Voss).

House rules applied in this file: no em dash (U+2014), no en dash (U+2013), no emojis, no capitals for emphasis. Where a source quote contained a dash, I replaced it with a comma and say so. Every statistic has a URL or a [VERIFY] tag. Anything I could not fetch or confirm is said plainly.

## 0. How to read this file

The skill has one job here: make ad copy that a stranger reads, believes and acts on, without the reader feeling a machine wrote it. The evidence says three things.

1. AI text has measurable fingerprints. Word choice, sentence shape, formatting and rhythm all drift in known directions.
2. Removing fingerprints is the easy half. The hard half is putting something true and specific in their place. A pattern remover cannot supply a price, a time of day or a smell of wet wool. The skill has to ask for those facts or leave the line out.
3. The goal is better copy and honest copy. Beating a detector is not a goal, and the ethics section explains why.

Status of the main sources I opened:

| Source | What I did | Status |
|---|---|---|
| Wikipedia, Signs of AI writing | Fetched the whole page (253,759 characters) | Read in three passes (characters 0 to 253,759) through a fetch tool that summarizes each pass, so fine detail and the reference list may be lost. |
| Kobak et al., excess vocabulary | Read the arXiv PDF text, including supplement word list | Read in full. The Science Advances page returned HTTP 403. |
| Juzek and Ward, lexical overrepresentation | Read the arXiv abstract page only | Abstract only. |
| Reinhart et al., PNAS 2025 | Search result summary only | Not opened. [VERIFY] before quoting numbers. |
| Russell, Karpinska, Iyyer, ACL 2025 | Read the arXiv abstract page | Abstract only. |
| Pangram pages (signs, phrases) | Fetched both | Read. Vendor data, corpus not stated. |
| tropes.fyi | Fetched the full directory | Read. |
| blader/humanizer | Fetched repo page and SKILL.md; star count from the GitHub search API on 2026-10-06 | Read. |
| conorbronsdon/avoid-ai-writing | Fetched SKILL.md summary | Summary only. |
| Anthropic prompting docs (the current model page, best practices page) | Fetched and searched the saved text | Read the writing sections. |
| Adpharm anti-slop playbook | Fetched | Read. |
| GPTZero explanation pages | Fetched one, searched one | Partly read. |
| Reddit | Search returned no usable thread | Not used. Community voice comes from Hacker News and blogs. |
| X (Twitter) | Not reachable by fetch | Not used. |

## 1. What the research says

### 1.1 Wikipedia's field guide

Wikipedia editors (WikiProject AI Cleanup, formed 2023) keep the most detailed public catalog of AI tells: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing . NPR covered its launch: https://www.npr.org/2025/09/04/nx-s1-5519267/wikipedia-editors-publish-new-guide-to-help-readers-detect-entries-written-by-ai . The guide says its signs are descriptive and not proof. It also says one or two hits can be coincidence, and many hits across a text are a strong signal. That is the right model for a linter: count and cluster, do not convict on one word.

Points from the page that matter for ad copy:

- Promotional drift. The page lists "boasts a", "vibrant", "rich", "profound", "showcasing", "exemplifies", "commitment to", "natural beauty", "nestled", "in the heart of", "groundbreaking", "renowned", "diverse array". It says that even when asked for an encyclopedic tone, models slide toward travel-guide and press-release language. Travel copy is the home turf of this problem.
- Copula avoidance. "Serves as", "stands as", "features", "offers" replace plain "is" and "has". The page cites a study that found a drop of more than 10 percent in "is" and "are" in 2023.
- Negative parallelism. "Not only X but Y", "It's not X, it's Y", and the reverse "Y rather than X".
- Rule of three. Adjective, adjective, adjective, or phrase, phrase, and phrase.
- Shallow -ing riders. A fact followed by "highlighting", "underscoring", "reflecting", "fostering".
- Vague attribution. "Experts argue", "industry reports", "observers have cited".
- Style signs. Title Case headings, bold overuse, inline-header vertical lists, em dash overuse, emoji as structure, curly quotes (weak alone).
- Vocabulary changes by era. The chat era of 2023 to mid 2024: additionally, crucial, delve, intricate, landscape, meticulous, pivotal, tapestry, testament, vibrant. The era after it: align with, enhance, fostering, highlighting, showcasing. The page says "delve" fell sharply in 2025. It also warns that overuse of one word does not make its synonyms suspect.
- Human detection is weak. The page says humans are about as good as chance in one 2025 study, and that expert annotators reach about 90 percent.
- Em dashes are fading as a chatbot tell. A section of the page reports a July 2026 study in which only Claude used em dashes more than professional writers. I could not open that study. [VERIFY: study title and authors]. This matters because the skill runs on Claude.

### 1.2 Excess vocabulary, measured

Kobak, Gonzalez-Marquez, Horvat, Lause. "Delving into LLM-assisted writing in biomedical publications through excess vocabulary." Science Advances, 2 July 2025, vol 11 no 27. Preprint: https://arxiv.org/abs/2406.07016 . I read the PDF text.

- Corpus: more than 15 million PubMed abstracts, 2010 to 2024.
- Finding: at least 13.5 percent of 2024 abstracts were processed with LLMs (a lower bound), up to about 40 percent in some subcorpora.
- Excess words: 454 excess words in 2024, against 190 at the Covid peak in 2021. Of the 379 excess style words in 2024, 66 percent were verbs and 14 percent adjectives. Before 2024, excess words were mostly content nouns (79.2 percent), such as disease names.
- Strongest words by frequency ratio r: "delves" r = 28.0, "underscores" r = 13.8, "showcasing" r = 10.7. By absolute frequency gap: "potential" (0.052), "findings" (0.041), "crucial" (0.037).
- The supplement lists 291 excess style words with low frequency. Examples relevant to ad copy: bolster, commendable, compelling, crafted, elevate, embracing, empowers, encompasses, endeavors, enduring, exceptional, fostering, groundbreaking, harness, heighten, illuminates, imperative, innovative, interplay, intricate, invaluable, leverages, meticulous, multifaceted, noteworthy, nuanced, paving, pivotal, poised, realm, remarkable, revolutionize, seamless, showcasing, streamline, swift, transformative, unparalleled, unlocking, unveil, versatility.

Caution: this is scientific writing. Words like "potential" and "findings" are normal there and in ads they are irrelevant. Use the study for the mechanism (LLMs prefer style verbs and adjectives) and for the verb-heavy shape, not as a ban list for ski copy.

Juzek and Ward. "Why does ChatGPT delve so much?" https://arxiv.org/abs/2412.11385 . They studied 21 focal words and found no evidence that architecture, algorithm choices or training data explain the overuse. They tested whether human-feedback training (RLHF) contributes, with mixed results. Read: abstract only. Conclusion for us: nobody has a clean cause, so do not build the skill on a causal story. Build it on observed patterns.

Reinhart et al. "Do LLMs write like humans? Variation in grammatical and rhetorical styles." PNAS 122(8), Feb 2025. https://www.pnas.org/doi/10.1073/pnas.2422455122 . Search summary only: instruction-tuned models use more present participle clauses and more nominalizations than humans, and the gap persists when asked to write informally. [VERIFY: effect sizes before quoting]. This supports two rules in the linter: flag ", highlighting ..." riders and abstract noun stacks.

### 1.3 Who can spot it

Russell, Karpinska, Iyyer. ACL 2025. https://arxiv.org/abs/2501.15654 . Five annotators who use LLMs often, voting together, misclassified 1 of 300 articles. They used two kinds of cue: known AI vocabulary, and qualities such as formality, originality and clarity. They stayed accurate against paraphrasing and "humanizer" tools. Pangram's write-up of the same work says non-experts perform near chance and tend to blame "fancy" rare words, while experts know the exact overused words, such as "testament" and "crucial": https://www.pangram.com/blog/russell .

Implication: the readers who matter most (marketers, journalists, heavy chatbot users) are the experts. Rare words are not the problem. Familiar stock phrases are.

### 1.4 What a vendor measured

Pangram, "9 signs of AI writing, backed by data": https://www.pangram.com/signs-of-ai-writing . Rates per 10,000 words, AI versus human, as published by the vendor:

| Sign | AI | Human | Vendor multiplier |
|---|---|---|---|
| Markdown | 90 | 8 | 12x |
| AI phrases | 30 | 3 | 12x as listed on the page (30 vs 3 is 10x) |
| Em dashes | 17 | 2 | 10x as listed (17 vs 2 is 8.5x) |
| Bullet lists | 28 | 3 | 9x |
| Triads | 19 | 5 | 4x |
| "Not just X but Y" | 3 | 1 | 3x |
| Unusual unicode | 71 | 28 | 3x |
| AI-style headers | 2 | 1 | 2x |
| Emojis | 0.2 | 0.1 | 2x |

[VERIFY: corpus, models and dates are not stated on the page; the vendor sells a detector]. The ranking is still useful: formatting and punctuation tells outweigh single words. Their phrase list (https://www.pangram.com/resources/most-common-ai-phrases) is review-and-fiction oriented ("recently had the pleasure", "complex tapestry", "anyone looking to elevate", "testament to human").

### 1.5 The em dash

- Freeburg, "The Last Fingerprint: How Markdown Training Shapes LLM Prose" (March 2026 preprint): https://arxiv.org/abs/2603.27006 . Twelve models, five providers, told to avoid markdown. Em dashes survived in most. One model family produced 0.0 per 1,000 words and another produced 9.1 under suppression. A search summary also gave two more models at 9.09 and 6.95. [VERIFY: those two figures were not in the abstract I read]. The author frames em dashes as a trace of fine-tuning method.
- FIU expert Mustafa Ocal says models learn from highly rated sources that use em dashes: https://news.fiu.edu/2026/why-does-ai-use-so-many-em-dashes-an-expert-explains . That is an explanation from one expert, not a measured cause.

Takeaway: telling a model "no em dashes" is not enough. It often keeps them. The skill needs a post-check (the linter) and not only an instruction.

### 1.6 What detectors measure

GPTZero's own explainer: https://gptzero.me/news/how-ai-detectors-work/ . Perplexity is how surprised a language model is by the text. Burstiness is how much that surprise varies across the document, which shows up as variation in sentence length and structure. GPTZero says its current model also uses sentence-level classification and an internet text search. Its published accuracy figures (99 percent accuracy, 1 percent false positives on pure samples) are vendor claims. [VERIFY: independent confirmation].

Counter-evidence on reliability:

- Liang et al., Patterns 2023: seven detectors flagged 61.3 percent of TOEFL essays by non-native writers as AI on average. https://www.cell.com/patterns/fulltext/S2666-3899(23)00130-7 (via https://www.sciencedaily.com/releases/2023/07/230710113921.htm ).
- Jabarian and Imas, NBER w34223 (2025): commercial detectors beat an open-source one. Pangram was near zero on false positives in their tests and Originality.ai had false negatives up to 40 percent in some cases. https://www.nber.org/system/files/working_papers/w34223/w34223.pdf (summary via search). The avoid-ai-writing README claims over 70 percent misclassification by open-source detectors and cites this paper. I could not confirm that claim. [VERIFY].

So the honest summary is: detectors vary a lot, some work well, all can be wrong about a given person, and experienced humans spot stock phrases better than most tools. The skill should aim at the human reader.

### 1.7 Anthropic's own guidance

Anthropic prompting guide for the current Claude model (platform docs, prompt engineering section "Writing density"). [link: source page, left out because its address names a model] The guide says the model has few stock phrases but its prose can be dense, with long sentences and few paragraph breaks. It defines "mannered prose" this way: it substitutes metaphor and flourish for direct statement, the phrases exist to display the writer, and the fix is to say what you mean and use the literal phrase when one is available. Its examples: "a dial worth turning" for "a parameter worth varying", "this point earns its keep" for "this point still matters". It suggests adding the definition to the user message (preferred) or the system prompt, and offers a short form: "Please remove all mannered prose."

The general best-practices page (https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) advises prose over heavy markdown for long-form content, with a sample instruction block for minimizing markdown, and says matching the prompt's own formatting to the desired output helps.

For ad copy this is directly useful. The mannered-prose definition catches "adventure awaits" and "the magic of" for the same reason it catches "a dial worth turning". Both put the writer on display.

### 1.8 Existing anti-slop projects on GitHub

Star counts from the GitHub search API, read 2026-10-06:

| Repo | Stars | Notes |
|---|---|---|
| https://github.com/blader/humanizer | 54,287 | Created 2026-01-18, MIT. 26 patterns in 6 groups (staging, rhythm, inflation, formatting, chat leftovers, wrong reader). Built on the Wikipedia guide. |
| https://github.com/conorbronsdon/avoid-ai-writing | 4,876 | Audit and rewrite modes, severity tiers P0 to P2, guardrail against inventing specifics. |
| https://github.com/Nanako0129/sepia | 2,998 | De-AI skill, narrative repair for fiction. |
| https://github.com/AIScientists-Dev/academic-humanizer | 1,790 | Academic writing. |
| https://github.com/harshaneel/humanize | 517 | Detection-literature oriented. |
| https://github.com/Anbeeld/WRITING.md | 372 | Concrete anchors, genre-aware, self-audit loop. |
| https://tropes.fyi (gist https://gist.github.com/ossa-ma/f3baa9d25154c33095e22272c631f5a1) | n/a | 32 tropes in a single markdown file for a system prompt. |

Three observations for positioning adwright:

1. The demand is proven. One general humanizer passed 54,000 stars in under nine months.
2. All of these remove tells. None, from what I read, is built around ad and travel copy, and none ships a tested deterministic linter with false-positive guards for outdoor vocabulary. That gap is real, but I checked only the repos above. [VERIFY: a wider scan before claiming "first"].
3. The best idea in the set is the guardrail in avoid-ai-writing and WRITING.md: never invent specifics, quotes, numbers or stakes while rewriting. adwright should make that a headline feature, because ads are where invention causes legal trouble.

### How adwright should use this

Use three layers. Layer one is a short prompt block that defines mannered prose and bans the top stock phrases. Layer two is a fact bank intake so the model has real specifics to write with. Layer three is the linter, run on every draft, with the result fed back for one revision. Count and cluster hits rather than judging single words. Never quote vendor multipliers in the skill's README without the [VERIFY] caveat.

## 2. Catalog of tells

Severity here means how loudly the tell reads to an expert reader in an ad. P0 means block, P1 fix, P2 review. The linter codes (Section 7) match.

### 2.1 Lexical tells (words and phrases)

| Tell | Example | Why it reads as machine | Replacement strategy |
|---|---|---|---|
| Era vocabulary: delve, tapestry, testament, realm, intricate, meticulous, pivotal, underscore, showcase, foster, bolster | "A rich tapestry of Norwegian winter" | Rare in human ad copy, frequent in model output (Kobak et al.). | Delete the sentence, or name the thing the tapestry stands for. |
| Ad verbs: unlock, elevate, empower, transform, supercharge, reimagine, harness, leverage, streamline | "Elevate your ski season" | Verbs with no physical action. The reader cannot picture anyone doing them. | Use a verb a body can do: climb, skin, carve, wait, eat, sleep, drive. |
| Empty intensifiers and magic adverbs: truly, deeply, incredibly, quietly, fundamentally, genuinely, absolutely | "A truly unforgettable day" | Adds volume, not information. "Quietly" is a favorite of fiction-style output (tropes.fyi). | Cut the adverb. If the sentence dies, it had no content. |
| Vague superlatives: best, ultimate, perfect, world-class, premier, epic | "The ultimate ski experience" | Unprovable, and every competitor says it. | State the measurable fact: group size, hours on snow, vertical metres, price. |
| Copula dodge: serves as, stands as, boasts, features, offers | "The lodge boasts a sauna" | Plain "is" and "has" are avoided (Wikipedia guide). | "The lodge has a sauna." |
| Significance inflation: testament to, plays a crucial role, evolving landscape, rich heritage | "A testament to Norwegian outdoor culture" | Ordinary facts dressed as history. | Say what happened and when. |
| Vague attribution: experts say, guests love, travellers rave | "Guests rave about our guides" | Unnamed authority. In ads it can also be a misleading claim. | Quote one real guest with permission, or drop it. |
| Filler transitions: Furthermore, Moreover, Additionally, It is worth noting | "It's worth noting that conditions vary" | Signals structure, adds nothing. | Start the sentence at the point. |
| Hedge stacks: could potentially, might possibly, may arguably | "Could potentially offer fresh snow" | Repeated editing adds qualifiers (humanizer pattern 9). | One honest hedge, with the reason: "Snow depends on the week's weather." |
| Chatbot residue: Certainly!, Great question, I hope this helps, Here is a revised version | Left at the top of a pasted caption | Only a chatbot says it. | Strip. Never ship wrapper text. |

### 2.2 Structural tells

| Tell | Example | Why it reads as machine | Replacement strategy |
|---|---|---|---|
| Negative parallelism: "It's not just X, it's Y"; "Not X but Y"; "Y rather than X" | "It's not just a ski trip, it's a way of life" | The most reported single tell. tropes.fyi calls it the most common. It argues against a claim nobody made. Wikipedia's page lists three variants. | State Y as a fact. "Nine days of skiing." Drop the straw man. |
| Countdown: "Not X. Not Y. Just Z." | "No queues. No crowds. Just snow." | Negation tripled, then a reveal. | One concrete contrast at most, with a real detail: "No lift queue. You climb for it." |
| Tricolon and rule of three | "Adventure, relaxation, and culture" | Triads are 4x more common in AI text per the vendor data (19 vs 5 per 10,000 words). Often the third item is filler. | Pick the one item you can prove. Or list two and stop. Gear lists of three real items are fine. |
| "Whether you are X or Y" | "Whether you're a beginner or an expert" | Audience sweep that avoids choosing a reader. | Name who the tour is for and who it is not for. |
| Rhetorical question opener | "Ready to ski the fjords?" | Stock opener from sales copy. | Open with a fact, a date, a price, or a small scene. |
| "The X? A Y." | "The result? Pure magic." | False suspense. | Give the result. |
| Colon reveal and fake-depth openers | "Here's the thing:", "At its core,", "The real question is" | Announces a point instead of making one (humanizer patterns 3 and 4). | Make the point. |
| Summary closers | "In conclusion", "All in all" | Wrap-up codas are a learned habit. | End on the last useful fact or the call to action. |
| Em dash overuse | One sentence with two dashes | 17 per 10,000 words in AI text vs 2 in human (vendor figures). Model-dependent. House rule here: none. | Comma, colon, parentheses, or a full stop. |
| List-ification | A bullet list of benefits in a feed ad | Models reach for structure. Bullets are 9x more common (vendor). | Prose, or at most one line of three real facts. |
| "Imagine..." | "Imagine waking up to fjord views" | Invitation to futurism (tropes.fyi). | Describe what happens at 07:30 on day two. |
| False range | "From adventure to relaxation to culture" | Items not on one scale. | Use a true range: "From 30 Jan to 10 Apr." |
| Shallow -ing rider | "...offering skiing, highlighting local culture" | Participle clause tacked on (Wikipedia, Reinhart et al.). | Cut it. If the fact matters, give it its own sentence. |

### 2.3 Tonal tells

| Tell | Example | Why it reads as machine | Replacement strategy |
|---|---|---|---|
| Relentless enthusiasm | "Amazing! Incredible! Unforgettable!" | A flat register of delight with no variance. Humans vary mood. | One exclamation mark at most per ad, and only when something surprising is said. |
| Grandiose stakes | "Will change how you see winter" | Everything is world-historical (tropes.fyi). | Small, true stakes: warm hands, a good run, a hot meal. |
| Sycophancy and flattery | "You deserve this" | Models trained on human preference lean toward agreement and praise: https://arxiv.org/abs/2310.13548 . | Respect the reader. Give information. |
| Patronising teacher voice | "Let's break it down", "Think of it as" | Assumes the reader needs a lesson. | Say it once, plainly. |
| Performed candor | "Honestly?", "Let's be honest" | Candor as decoration (avoid-ai-writing guardrails). | Be candid by stating a real downside. |
| Corporate filler | "Your trusted partner", "commitment to excellence", "peace of mind" | Stock B2B phrases. | Say what you do and what it costs. |

### 2.4 Rhythmic tells

| Tell | Example | Why it reads as machine | Replacement strategy |
|---|---|---|---|
| Uniform sentence length | Six sentences of 14 to 18 words | Low burstiness. GPTZero's definition ties burstiness to variation. | Mix a 3-word sentence with a 25-word one. |
| Uniform paragraph length | Four paragraphs of three sentences | Template shape. | Let one paragraph be a single line. |
| Repeated openings | "Our guides... Our tours... Our team..." | Anaphora by default. | Vary the subject: the snow, the time, the reader. |
| Manufactured fragments | "He published this. Openly. In a book." | Short sentences for fake emphasis (tropes.fyi). | Use a fragment only when it carries a fact: "Thursday. Rain." |
| Synonym cycling | "tour", then "excursion", then "expedition" | Refusal to repeat a noun. | Repeat the noun. Ads are allowed to repeat "ski". |

Note on the last two: the cure list below recommends deliberate fragments. The difference is whether the fragment holds information.

### 2.5 Formatting tells

| Tell | Example | Why it reads as machine | Replacement strategy |
|---|---|---|---|
| Headers and bullets inside ad copy | A markdown heading in a Meta primary text | Markdown is the top sign in the vendor data (90 vs 8 per 10,000 words). It also renders as raw symbols on Meta and X. | Plain text. Line breaks only. |
| Emoji clusters and emoji as bullets | A snowflake, a mountain and a plane at line starts | Emoji as structure (Wikipedia guide). House rule: none. | Words. |
| Bold spam | "**Expert guides**: ..." | Bold-first bullets are a named trope. | Remove bold. In the landing page, bold at most one phrase. |
| Title Case headlines | "Your Ultimate Norwegian Ski Adventure" | Wikipedia and tropes.fyi list it. | Sentence case. |
| Hashtag stacks | Five or more hashtags on X | Template engagement habit. | Zero to two, and only if the audience uses them. |
| Unicode decoration | Arrows, check marks, curly quotes | Hard-to-type characters that models like. Curly quotes alone prove nothing. | Plain characters. |

### 2.6 Semantic tells

| Tell | Example | Why it reads as machine | Replacement strategy |
|---|---|---|---|
| Abstract nouns | "A journey of discovery and connection" | Nominalization (Reinhart et al.). No picture forms. | Replace each abstract noun with a thing, a time, a number. |
| No specifics | "Fresh powder and stunning views" | Could describe any ski trip on earth. | Add the place, the day, the price, the hour. |
| No stakes | Everything is wonderful | No cost, no risk, no trade-off. | State the effort or the downside. |
| Generic place description | "Nestled among majestic mountains" | Models describe places from the average of promotional text. A travel-guide editor made this point about AI guides: no personality, no firsthand detail (https://blog.ricksteves.com/cameron/2023/07/ai-vs-human-traveler). | Describe what you saw on a given day. |
| Narrating the document | "In this ad we explore" | Writing about the text, not the subject. | Cut. |
| Fake specificity | An invented guest quote or a made-up number | Plausible detail with no source. Worse than vagueness. | Use only supplied facts. See Section 8. |

### How adwright should use this

Store this catalog as three things: a short "never write" list in the skill prompt (the 40 loudest tells), a longer "review list" the draft pass checks, and the machine-readable rules in Section 7. Tag every rule with a one-line reason so the skill can explain a flag to a client in plain words ("this sentence argues with a claim nobody made"). The reason column is also the best README content, because people share lists of tells.

## 3. Travel, outdoor, ski and ad slop

### 3.1 Travel and outdoor

Evidence that these are old clich\u00e9s and not only AI habits:

- Corinne Mossati, travel writing clich\u00e9s, 29 April 2010: "hidden gem", "unspoiled gem", "off the beaten track", "has something for everyone", "perched", "must see", "the pearl of". https://gourmantic.com/perched-nestled-and-other-hidden-gems/
- Pitch Travel Write list: "sun-kissed", "lush greenery", "breathtaking beauty", "stunning landscape", "crystal clear seas", "pristine beaches", "snow-capped mountains", "unique charm", "quaint village", "best-kept secret", "bucket list", "hidden gem", plus flat adjectives like "magnificent", "spectacular", "charming", "awesome". Advice: be specific, show instead of tell. https://www.pitchtravelwrite.com/cliches.html
- BuzzFeed's AI-assisted travel guides, 30 March 2023: "hidden gem" or "secret gem" appeared about 25 times across the set, and the line "Now, I know what you're thinking" appeared seven times in a handful of stories, alongside "lively markets", "homely eateries", "amazing cuisines", "unique culture, beautiful scenery, and amazing food". https://siliconangle.com/2023/03/30/buzzfeeds-new-ai-generated-travel-articles-dystopian-bad-dream/

So the clich\u00e9s predate models. Models inherit them because promotional travel text is most of the training data for the topic. The Rick Steves editor's point is the same: the training mass is promotional, so output defaults to promotion.

Word and phrase list for the skill (flag these in travel, outdoor and ski copy):

| Group | Items |
|---|---|
| Scenery adjectives | breathtaking, majestic, stunning, spectacular, magnificent, picturesque, idyllic, enchanting, mesmerizing, awe-inspiring, pristine, untouched, unspoiled, crystal clear, snow-capped, postcard-perfect |
| Experience nouns | adventure of a lifetime, unforgettable memories, bucket list, once in a lifetime, journey, escape, getaway (as vague noun), playground, paradise, winter wonderland, hidden gem, best-kept secret |
| Invitation verbs | immerse yourself, discover, explore, embark, unwind, indulge, awaken, escape the ordinary, experience the magic |
| Place filler | nestled, perched, in the heart of, tucked away, off the beaten path, something for everyone, rich heritage, charming village |
| Closers | adventure awaits, magic awaits, memories that last a lifetime, your dream getaway, look no further |
| Gear and guide filler | expert guides (unqualified), world-class, tailored experience, curated, bespoke |

### 3.2 Ad-specific slop

| Group | Items |
|---|---|
| Verbs | unlock, elevate, transform, empower, supercharge, reimagine, revolutionize, harness, leverage |
| Hype adjectives | game-changer, game-changing, cutting-edge, next-level, revolutionary, seamless, all-in-one, ultimate, premium |
| Hooks | Ready to...?, Tired of...?, Looking for...?, Say goodbye to..., Look no further, Don't miss out, Discover the magic of... |
| Urgency | Limited spots, selling fast, act now, hurry, last chance. These are also a honesty risk, see Section 8. |
| Social proof stock | Thousands of happy guests, join the community, loved by travellers |

The Adpharm guide (April 3, 2026) adds a useful instruction-side finding: words like "engaging", "compelling", "punchy", "modern", "fresh", "dynamic" and "professional yet approachable", when placed in the brief, push the model toward the generic register. [link: Adpharm source page, left out because its address names a model]. This is one publisher's claim from its own practice. [VERIFY: independent test]. It still suggests a design rule: the skill's own prompts should not use those words.

### 3.3 False friends: words that are fine in this domain

A ski and outdoor skill hits legitimate uses of flagged words. The linter has suppression rules for these.

| Word | Fine when | Example |
|---|---|---|
| harness | Climbing, glacier travel, sled dog or via ferrata gear | "You wear a harness on the glacier section." |
| elevate / elevation | Elevation is a normal measurement | "Elevation gain is 900 m." The linter matches "elevate" forms only. |
| unlock | Literal doors, huts, phones | "Unlock the cabin with the brass key." |
| navigate | Whiteout, fog, a map, a route | "We navigate by compass in a whiteout." |
| robust | Software, or a spec on a shell or boot | "A robust shell jacket." Flag it only when it describes ideas. |
| leverage | Finance noun, physics | "Leverage on a pole plant." |
| journey | A literal trip | "The train journey to Voss." |
| epic | Brand names and a ski pass | "Epic Pass." |
| testament, tapestry | Legal and art-history nouns | "Bayeux tapestry." |
| majestic | Proper nouns | "Majestic Hotel." |
| immersion | Maritime gear | "Immersion suit." |
| guaranteed | Negated honestly | "We cannot guarantee snow." |
| ready to | Literal readiness | "Ready to ski at 08:30." |
| powder, summit, peak | Technical terms | Always fine. |

### How adwright should use this

Ship the word lists as data files (JSON or YAML), grouped as above, so users can add their own region. Keep a separate "allow in context" list so the skill does not insult guides who say "harness" ten times a day. In the README, show the false-friend table. It signals that the linter was built by someone who skis.

## 4. The cures

AI slop is mostly a missing-information problem. The model fills the gap with the statistical average of other ads. The cure is real information plus a few craft moves. Each cure below has a test the skill can apply.

| Cure | What it means | Test | Example |
|---|---|---|---|
| Specific numbers | Prices, dates, hours, group sizes, distances, temperatures | Is there a figure a reader could check? | "NOK 28,896. Departs 29 Jan or 4 Feb." |
| Named places and things | Town, mountain, fjord, hut, gear item, dish | Would a local nod at the noun? | "Voss" beats "a charming Norwegian town." |
| Sensory verbs | What body parts do and feel | Can you see or feel the verb? | "Skin up", "click into your bindings", "stamp snow off your boots" |
| Concrete nouns | Replace abstract nouns with things | Can you photograph it? | "dry socks" beats "comfort" |
| First-hand observation | A thing a guide or guest saw, with a source | Does the brief say who saw it? | Only from client notes. Never invented. |
| Asymmetric rhythm | Long, short, shorter | Do two sentences in a row have the same length? | A 22-word sentence, then "Rain." |
| Contractions | "You'll", "we're", "can't" | Does it sound like speech? | "You'll want dry socks." |
| Deliberate fragments | Fragments that hold a fact | Does the fragment carry information? | "Saturdays and Sundays. January to April." |
| Dry humor | Understatement about a real discomfort | Is the joke about something true? | "Pick the month you'd like to be cold in." |
| The unglamorous true detail | The cold, the wait, the wet | Is it a small inconvenience that proves honesty? | "At 3pm you'll want dry socks." |
| A real constraint, stated honestly | What the product cannot do or promise | Would a cautious competitor leave it out? | "We can't order the sky." (aurora) |
| A point of view | A stance a reasonable person could disagree with | Could someone say no to this line? | "Take the early departure. The snow is better in February." only if the client believes it. |

### 4.1 The fact bank

The skill should collect these before writing. If a field is empty, the copy leaves that dimension out and says so.

| Field | Why it matters |
|---|---|
| Exact price and what it includes, per person or per group | Numbers and trust. The confirmed price file for this client flags "per person" as unconfirmed. |
| Dates, written in full | Real departures beat "all winter". |
| Group size and guide ratio | A specific that models invent. Never guess it. |
| Day shape: start time, hours on snow, meal timing | First-hand rhythm. |
| What to bring and what is provided | Unglamorous and useful. |
| A real downside or limit | Honest constraint. |
| Who it is for, who it is not for | Point of view. |
| One true detail from a guide | Sensory seed. Source it. |
| One real review, with name and permission | Social proof. |
| Words the client uses | Voice. |

### 4.2 Voice samples beat adjectives

Anthropic's docs and Adpharm both recommend giving the model real writing to imitate. Adpharm suggests pasting 200 to 600 words of actual prose rather than only naming a writer. WRITING.md says a paragraph with no checkable detail gets revised: https://github.com/Anbeeld/WRITING.md . Ask the client for three real captions or guide emails and use them as the voice sample.

### How adwright should use this

Make the fact bank the first step of every run, and make "no specific, no sentence" the central rule. The cures table doubles as the rewrite menu: for each flagged line, the skill must say which cure it applied. If it cannot apply one, it asks a question instead of inventing a detail. This is the main difference from a generic humanizer.

## 5. Before and after rewrites

Read this first: the Before lines are typical machine output. In the After lines, tour names, prices and dates come from the client's confirmed list (seven ski tours, 2027 departures, Saturday and Sunday day tours from January to April). Everything else in an After line (a dinner time, a guide habit, a weather remark, a hotel's room count) is illustrative and must be replaced with a client-confirmed fact before use. I wrote them to show the shape of a fix. The skill must never ship an illustrative detail as fact. Also, I ran all 30 After lines through the linter in Section 7: zero hits. All 30 Before lines trigger at least one P1.

### 5.1 Ski and fjord travel (20)

| # | Before | After | Cure used |
|---|---|---|---|
| 1 | Experience the magic of Norway's fjords on skis! | Ski down to the fjord. Then do it again tomorrow. 9 days, from NOK 42,126. | Concrete verb, number, rhythm |
| 2 | Whether you're a seasoned skier or a complete beginner, our backcountry tours have something for everyone. | Two day tours, two levels. Beginner to intermediate, or intermediate to advanced. Both NOK 1,948. Every Saturday and Sunday, January to April. | Choose the reader, numbers, fragments |
| 3 | Nestled in the heart of Voss, our tours offer a breathtaking gateway to Norway's winter wonderland. | Voss has a train station. The snow is a short drive from it. | Plain "has", named place, small true detail (confirm drive time) |
| 4 | Unforgettable memories await on our 6-day ski package! | 6 days. Fresh tracks in the morning, cruisers after lunch. NOK 28,896. Departs 29 Jan or 4 Feb. | The product's own idea, price, dates |
| 5 | It's not just a ski trip, it's a transformative journey that will elevate your winter. | Nine days of skiing. You'll sleep well for all of them. | Kill the straw man, dry humor |
| 6 | Chase the Northern Lights and carve fresh powder on our epic 7-day adventure! | Ski the fjords for a week, then fly to Tromso for the aurora. From NOK 41,181. The lights depend on the sky, and we can't order the sky. | Honest constraint, dry humor |
| 7 | Say goodbye to crowded slopes and discover hidden gems of untouched wilderness. | No lift queue. You climb on skins, and the way down is yours. | Concrete mechanism instead of "hidden gems" |
| 8 | Our expert guides ensure a safe and seamless experience for all skill levels. | Your guide reads the avalanche forecast at breakfast. If a slope is off the table, you hear which one and why. | First-hand routine (confirm with client) |
| 9 | Get ready to unlock the ultimate winter playground! | Pack dry socks. At 3pm you'll want them. | Unglamorous true detail |
| 10 | Majestic fjords, snow-capped peaks, and charming villages await. | The fjord is black at 8am and the snow is blue. Pour the coffee before you click into your bindings. | Sensory detail, one scene instead of a triad |
| 11 | Adventure awaits! Book your dream ski getaway today and create memories that last a lifetime! | 3 days of ski and snowshoe. Leaves 28 Jan, 31 Jan or 7 Feb. NOK 17,451. | Dates and price do the work |
| 12 | Looking for the perfect Valentine's getaway? Look no further! | Valentine's Day is 14 Feb. The 3-Day Winter Multi-Sport Explorer leaves on the 12th. NOK 16,527. | Real hook from the calendar |
| 13 | Immerse yourself in Norway's rich cultural heritage and stunning natural beauty. | Dinner is at 18:00. By 21:00 most of the group is asleep. | Daily rhythm (illustrative) |
| 14 | Our 9-day trip is a perfect blend of adventure, relaxation, and culture. | Five departures, 30 Jan to 10 Apr. Pick the month you'd like to be cold in. | Real dates, dry humor |
| 15 | Safety is our top priority, ensuring peace of mind for every guest. | On the beginner day tour you learn to use a transceiver before you need one. | Show the practice (confirm with client) |
| 16 | Book now before spots run out! | The 6 day package has two departures, 29 Jan and 4 Feb. The page shows what is open. | Remove fake urgency, point to live info |
| 17 | Powder dreams come true in Norway! | We can't promise fresh snow. February on the west coast can be wet, cold and both in the same hour. | Honest constraint (confirm weather claim) |
| 18 | Elevate your skiing with world-class instruction. | Bring skis you can walk uphill in. If you don't own a pair, ask before you pay. | Practical requirement, trust |
| 19 | Norway's fjords + skis = the ultimate winter adventure! Who's ready? #Norway #Ski #Adventure #Fjords | You can ski to a fjord in Norway. We checked. 9 days, from NOK 42,126. | X-length, dry humor, no hashtag stack |
| 20 | Join thousands of happy guests who have fallen in love with Norway on skis! | Use one real review, word for word, with the guest's first name and permission. No review on file yet? Leave social proof out. | Real proof or none |

Row 20 is an instruction to the writer and not a final line, on purpose: the skill cannot write a testimonial. The client's hub shows a 4.9 rating on each product, and the confirmed-facts note says the review count and source are unknown. Any use of "4.9" needs [VERIFY: count, source, date] first. The linter flags rating claims for that reason.

### 5.2 Other categories (10)

| # | Category | Before | After | Cure used |
|---|---|---|---|---|
| 21 | Software | Unlock seamless workflows and elevate your team's productivity with our all-in-one platform. | Your invoices go out on the 1st. This tool sends them on the 1st, and chases the late ones on the 8th. | Dates, a real mechanism |
| 22 | Hotel | Nestled in the heart of the city, our boutique hotel offers a vibrant tapestry of comfort and charm. | 42 rooms, one lift, a bakery next door. Quiet after 22:00 because the street is closed to cars. | Numbers, plain facts |
| 23 | Restaurant | Embark on a culinary journey of authentic flavours crafted with passion. | Pasta made at 9am, sold out by 8pm. Closed Mondays. | Times, a limit |
| 24 | Retail | Elevate your style with our premium, versatile, and durable boots. | Leather upper, resoleable, 1.1 kg a pair. Walk 20 km in them the day you get them. | Specs, a bold but checkable claim |
| 25 | Fitness | Ready to transform your body and unleash your best self? | Three 40 minute sessions a week. Week one is hard. Week four is when your stairs get easier. | Schedule, honest arc |
| 26 | Offer | Don't miss out on our incredible limited-time offer! | 20% off boots until Sunday 18 Oct, 23:59. After that the price goes back. | Real deadline, stated plainly |
| 27 | Thought post | It's not about AI, it's about the humans who use it. Here's the thing: leaders must adapt. | We trained 40 support agents on the new tool. Eleven stopped using it in a month. We asked why. | Story with numbers (author must supply real figures) |
| 28 | Property | This stunning property offers a rare opportunity to own a piece of paradise. | Three bedrooms, 94 m2, third floor, no lift. The kitchen was redone in 2022. The bathroom was not. | Candid flaw, numbers |
| 29 | Local service | Your trusted partner for all your plumbing needs, delivering exceptional service every time. | Leak at 11pm? Call 555 0142. We arrive within 90 minutes or the call-out is free. | A promise that can be broken |
| 30 | Education | In today's fast-paced world, learning a new language has never been more important. | Twelve weeks, two evenings a week, groups of six. By week four you order dinner without English. | Format, outcome |

All numbers in 5.2 are invented to show form. A real brief must supply them.

### How adwright should use this

Ship these 30 pairs as the skill's few-shot set and as the linter's regression tests (Before must flag, After must pass). Rotate which pairs appear in the prompt so output does not clone one voice. Mark each pair with the cure used, so the skill can reason about which move to apply. Never let the model copy an illustrative detail into a client ad; the pairs need a visible "example only" label in the skill file.

## 6. The rewrite protocol

A self-edit pass the skill runs on its own draft. Run it in order. Two rounds is the limit: WRITING.md observes that rewrites after one or two rounds circle the same model-level limits.

1. Freeze the facts. List every claim in the draft that carries a number, name, date, quote or promise. Each must trace to the brief or the fact bank. Mark the rest as invented and cut or ask.
2. Run the linter. Fix every P0 and P1 hit first. Do not touch P2 hits yet.
3. Find the one idea. Say the ad's point in one sentence. If you cannot, the draft is a brochure. Cut until it fits.
4. Check the opener. Does line one carry a fact, a price, a date, a scene, or a surprise? If it is a question, a greeting or a promise of magic, replace it.
5. Replace abstractions. For each abstract noun (journey, experience, adventure, memories), swap in a thing, a time or a number. If none exists in the fact bank, delete the sentence.
6. Kill straw men and triads. Rewrite every "not X, it's Y" as a plain statement of Y. For every list of three, ask if the third item earns its place. Keep at most one deliberate triad per piece, and only for real gear or real days.
7. Fix rhythm. Print sentence lengths. If the spread is narrow, merge two short sentences or split a long one. Add one fragment that carries a fact.
8. Contractions and voice. Read the draft aloud. Where it sounds like a brochure, use "you'll", "we're", "can't".
9. Add one honest limit. A real constraint, a real downside, or a real who-this-is-not-for line. If the brief gives none, ask for one.
10. Strip formatting. For feed ads: no headings, no bold, no bullets, no emoji, no hashtags beyond the platform norm. For landing pages: headings fine, bold sparingly, no bold-first bullets.
11. Honesty check. No scarcity claim without a live availability fact. No superlative without proof. No testimonial that is not real, verbatim and permitted. No rating without a source.
12. Run the linter again. Zero P0 and zero P1. P2 hits explained or fixed. Then stop.

Prompt block for the skill (put in the user turn, per Anthropic's advice to use the user message):

```text
Write for one reader. Use only the facts supplied. If a number, name, date, quote
or promise is not in the facts, do not write it; ask or leave it out.
Mannered prose substitutes metaphor and flourish for direct statement. When a
literal phrase exists, use it.
Do not use these shapes: "not X, it's Y"; "whether you're X or Y"; question
openers; three-item adjective lists; summary closers.
No em dash (U+2014), no en dash (U+2013), no emoji, no capitals for emphasis.
Vary sentence length. Use contractions. State one honest limit.
```

How well does this work? I did not test it against a model. [VERIFY: run an A/B on 20 briefs and count linter hits with and without the block].

### How adwright should use this

Encode the 12 steps as the skill's `edit` phase. The first and last steps call the linter. Give the user a `--explain` mode that prints each change with the cure used. That mode is the part people will screenshot.

## 7. Linter specification

The linter is a Python 3 script with no dependencies. The complete file is below in 7.4, and the test file in 7.5. On my run: 50 of 50 unit checks passed. All 30 Before lines reached REVISE or BLOCK, all 30 After lines scored PASS with no hits. A typical machine-written paragraph with bold-first bullets triggered 16 P1 hits and 12 P2 hits.

Honest limits: these are my regexes, tuned on my test strings and on 30 pairs. They have not been tested on a real corpus of human ad copy. Thresholds marked [HEURISTIC] are my choices, not published values.

### 7.1 Design

- Severity: P0 blocks (house rule or chatbot residue), P1 must be fixed, P2 needs a human look, P3 is information. Verdict: BLOCK if any P0, REVISE if any P1 or four or more P2, else PASS.
- Exit codes: 2 for any P0, 1 for any P1, 0 otherwise.
- Matching is case-insensitive where the rule says so. The apostrophe token `~` in a pattern expands to the character class that matches a straight or curly apostrophe.
- Dashes are matched by escape: the em dash (U+2014) as `\u2014` and the en dash (U+2013) as `\u2013`. The script file contains no literal dash characters.
- Each rule may carry a context-suppression regex. If it matches within 40 characters either side of a hit, the hit is dropped. This is how "harness" next to "glacier" survives.
- Metric checks (rhythm, specificity) run only when the text is long enough, and the thresholds are [HEURISTIC].

### 7.2 Rule table

| ID | Sev | Category | What it catches | Notes |
|---|---|---|---|---|
| H01 | P0 | house | em dash (U+2014) | Client rule. |
| H02 | P0 | house | en dash (U+2013) | Client rule. Use a hyphen or "to" for ranges. |
| H03 | P1 | house | `--` as a dash | Stand-in for em dash. |
| H04 | P2 | house | spaced hyphen used as a dash | Review: may be a real hyphen use. |
| H05 | P0 | house | emoji ranges U+1F300 to U+1FAFF, U+2600 to U+27BF, U+2B50, U+2B06, U+2B07, U+2705, U+274C, U+2728, U+FE0F | Client rule. |
| H06 | P2 | house | capital words of 4 or more letters | Allowlist: NOK, USD, EUR, UTM, FAQ, GPS, ABS, VAT, SMS, HTML, JSON, NORWAY, VOSS. Reference ads that use "STARTING FROM NOK 14,165" would flag; make the allowlist a config file. |
| H07 | P1 | house | `!!`, `?!`, `!?` | Stacked punctuation. |
| C01 | P0 | residue | chatbot phrases | "I hope this helps", "Certainly!", "Great question", "Here is a revised..." |
| C02 | P0 | residue | placeholders | `[insert ...]`, `{{...}}`, TODO, lorem ipsum |
| C03 | P1 | residue | cutoff and availability disclaimers | |
| L01 | P1 | lexical | delve family, tapestry, realm, testament, embark, unparalleled, multifaceted, myriad, plethora, beacon, kaleidoscope | Suppress: Bayeux, will and testament. |
| L02 | P1 | lexical | unlock, elevate, empower, supercharge, reimagine, revolutionize, transformative, game-changer, cutting-edge, next-level, seamless, holistic, synergy | Suppress: literal unlocking of doors and huts. |
| L03 | P1 | lexical | leverage, harness, streamline, utilize, foster, showcase, underscore, bolster, pivotal, meticulous, intricate, robust, "navigate the" | Suppress by context (climbing, glacier, rope, finance, software, whiteout, gear). |
| L04 | P1 | lexical | travel scenery and experience adjectives | Suppress: Majestic Hotel. |
| L05 | P1 | lexical | travel and ad cliche phrases | Suppress: immersion suit. |
| L06 | P1 | lexical | copula dodge, boasts, "a rich range of" | |
| L07 | P1 | lexical | shallow -ing rider after a comma | |
| L08 | P1 | lexical | significance inflation | |
| L09 | P1 | lexical | vague attribution | "guests love" is flagged on purpose. |
| L10 | P1 | lexical | throat-clearing and fake depth | |
| L11 | P1 | lexical | stock question openers | Literal "ready to ski at 08:30" has no question mark and passes. |
| L12 | P1 | lexical | filler transitions | |
| L13 | P1 | lexical | summary closers | |
| L14 | P1 | lexical | hedge stacks | |
| L15 | P1 | lexical | ad cliche pairings (epic adventure, perfect blend of, dreams come true, fall in love with, chase the northern lights) | |
| L16 | P1 | lexical | service and corporate filler | |
| L20 | P2 | lexical | magic adverbs and intensifiers | Frequently fine once. |
| L21 | P2 | lexical | tier 2 words: journey, experience, discover, explore, transform, curated, authentic, epic, iconic, and similar | Suppress: Epic Pass, train journey. |
| L22 | P2 | lexical | unsupported superlatives | |
| L23 | P2 | lexical | tier 2 AI vocabulary: crucial, vital, key, enhance, diverse, comprehensive, nuanced | |
| S01 | P1 | structural | negative parallelism, "it's not X, it's Y" | A literal correction ("That is not a ski run. It is a farm track.") also flags. Human review decides. |
| S01a | P1 | structural | "not just X but Y", "more than just a X, it's", "isn't about X. It's about Y" | |
| S01b | P1 | structural | "Not X. Not Y. Just Z." and "No X, no Y, just Z" | |
| S02 | P1 | structural | "Whether you're X or Y" | |
| S03 | P1 | structural | "The X? A Y." | |
| S04 | P2 | structural | "Imagine..." opener | |
| S05 | P2 | structural | false range "from X to Y to Z" | Suppressed for numeric and date ranges. |
| S06 | P2 | structural | compulsive counting headlines | |
| S07 | P2 | structural | "think of it as", "picture this", "here's the deal" | |
| S08 | P2 | structural | "despite these challenges" formula | |
| F01 | P2 | formatting | markdown bold | |
| F02 | P1 | formatting | markdown heading | In landing pages, run with `--channel web` and downgrade (see 7.6). |
| F03 | P2 | formatting | bullets and numbered lists | |
| F04 | P1 | formatting | bold-first bullet "**Label**: text" | |
| F05 | P1 | formatting | 4 or more hashtags in a row | |
| F06 | P2 | formatting | decorative unicode (arrows, check marks, stars) | |
| F07 | P3 | formatting | curly quotes | Weak alone. Wikipedia lists it as ineffective as a single sign. |
| F08 | P2 | formatting | horizontal rule | |
| F09 | P2 | formatting | Title Case line of 4 or more words | |
| A01 | P1 | honesty | scarcity and urgency | Needs a live availability check. [VERIFY with client] |
| A02 | P1 | honesty | absolute claims (guaranteed, risk-free, safest, cheapest) | Negations like "we can't promise" are suppressed. |
| A03 | P1 | honesty | ratings, guest counts, "thousands of happy guests" | Needs a source. |
| A04 | P1 | honesty | quoted testimonial pattern | Must be a real, verbatim, permitted quote. |
| M01 | P2 | rhythm | sentence-length coefficient of variation under 0.35 in 6 or more sentences | [HEURISTIC] |
| M02 | P2 | rhythm | no sentence under 7 words in 6 or more sentences | [HEURISTIC] |
| M03 | P2 | rhythm | same opening word in 3 or more sentences | `the` and `a` excluded. |
| M04 | P1 | semantic | fewer than 3 numbers plus named things per 100 words, in 40 or more words | [HEURISTIC] Names counted as capitalized words after a lowercase word or comma. |
| M05 | P2 | structural | 2 or more three-item lists in 40 or more words | Gear lists will trigger. Review. |
| M06 | P2 | tonal | exclamation marks above 25 percent of sentences | |
| M07 | P2 | structural | 3 or more colon reveals | |

### 7.3 False-positive warnings, in order of risk

1. Technical vocabulary. harness, navigate, leverage, robust, unlock and elevation have real uses. See Section 3.3. The suppression regexes cover the common ski contexts. They are not complete. Add terms as you meet them.
2. Names. Proper nouns such as "Majestic Hotel", "Epic Pass", "Paradise Lodge" will flag. Add an allowlist file.
3. Quoted material. Guest quotes, press quotes and legal text must be exempt. Mark them and skip them. Do not rewrite a real quote to satisfy the linter.
4. Non-native writers. Liang et al. found a 61.3 percent average false-positive rate for detectors on non-native essays. A word-and-pattern linter is not a detector, but it flags stock phrases that many second-language writers learned from tourism copy. Use it to edit, never to judge a person.
5. Humans write this way too. The Wikipedia guide and tropes.fyi both say one hit can be coincidence. Use counts. A single "stunning" is a style note. Five tells in 80 words is a pattern.
6. Metrics on short text. M01 to M05 need length. Meta primary text is often under 60 words. Do not treat the absence of a metric hit as a pass on rhythm.
7. Channel differences. Bullets and bold are fine on a landing page and wrong in a feed ad. Make F-rules channel-aware.
8. The negative parallelism regex is the noisiest rule. It stays P1 because the tell is common and the fix is cheap, but a human should confirm it.
9. Language. The rules are English. Norwegian copy needs its own list. I did not research Norwegian AI tells. [VERIFY: needs a Norwegian-language source].
10. Em dashes and other house rules apply to client copy. They are not a universal sign of AI. Many human writers use em dashes.

### 7.4 The linter script

Save as `adwright_lint.py`. Run `python3 -I adwright_lint.py draft.txt`.

```python
#!/usr/bin/env python3
"""adwright_lint: flag AI-writing tells in ad and travel copy.

Usage:  python3 adwright_lint.py file.txt [--channel meta|x|web] [--json]
Exit code: 2 if any P0 hit, 1 if any P1 hit, else 0.
Severity: P0 = block (house rule or chatbot residue), P1 = fix before shipping,
          P2 = review (often fine once, bad in clusters), P3 = info.
"""
import re, sys, json, statistics

DASH_EM, DASH_EN = "\u2014", "\u2013"
APOS = "['\\u2019]"           # straight or curly apostrophe (inserted for ~)
F = re.IGNORECASE

# (id, severity, category, regex, flags, message, suppress_if_context_regex or None)
RULES = [
 # ---------- house rules (client style) ----------
 ("H01","P0","house", "\u2014", 0, "em dash (U+2014): use a comma, colon, parentheses or a full stop", None),
 ("H02","P0","house", "\u2013", 0, "en dash (U+2013): use a plain hyphen or the word 'to' for ranges", None),
 ("H03","P1","house", r"(?<=\w) -- (?=\w)|(?<=\w)--(?=\w)", 0, "double hyphen used as a dash", None),
 ("H04","P2","house", r"(?<=[a-z,.]) - (?=[A-Za-z])", 0, "spaced hyphen used as a dash; check it is not a dash substitute", None),
 ("H05","P0","house", "[\U0001F300-\U0001FAFF\u2600-\u27bf\u2b50\u2b06\u2b07\u2705\u274c\u2728\ufe0f]", 0, "emoji (house rule: none)", None),
 ("H06","P2","house", r"\b[A-Z]{4,}\b", 0, "ALL CAPS word (house rule: no caps for emphasis)",
   r"\b(?:NOK|USD|EUR|UTM|FAQ|GPS|ABS|VAT|SMS|HTML|JSON|NORWAY|VOSS)\b"),
 ("H07","P1","house", r"!{2,}|\?!|!\?", 0, "stacked punctuation", None),
 # ---------- chatbot residue ----------
 ("C01","P0","residue", r"\b(?:I hope this helps|certainly[!,.]|of course[!,.]|great question|happy to help|let me know if|would you like me to|as an ai\b|as a language model|here(?:~s| is) (?:a|an|the|your) (?:revised|updated|draft|version|rewrite|ad|caption))", F, "chatbot residue", None),
 ("C02","P0","residue", r"\[(?:insert|your|company|name|link|date|tour)[^\]]{0,40}\]|\{\{[^}]+\}\}|\bTODO\b|lorem ipsum", F, "template placeholder left in copy", None),
 ("C03","P1","residue", r"\bas of (?:my|the) (?:last|latest) (?:update|training)|knowledge cutoff|based on (?:the )?(?:available|provided) information", F, "knowledge-limit disclaimer", None),
 # ---------- lexical: tier 1 (almost never fine in ad copy) ----------
 ("L01","P1","lexical", r"\b(?:delv(?:e|es|ed|ing)|tapestr(?:y|ies)|realms?|testament|embark(?:s|ed|ing)?|unparalleled|multifaceted|myriad|plethora|beacon|kaleidoscope)\b", F, "AI-vocabulary tier 1", r"\bbayeux\b|\blast will and testament\b|\bold testament\b|\bnew testament\b"),
 ("L02","P1","lexical", r"\b(?:unlock(?:s|ed|ing)?|elevat(?:e|es|ed|ing)|empower(?:s|ed|ing|ment)?|supercharg(?:e|es|ed|ing)|reimagin(?:e|es|ed|ing)|revolutioni[sz](?:e|es|ed|ing)|transformative|game[- ]chang(?:er|ers|ing)|cutting[- ]edge|next[- ]level|seamless(?:ly)?|holistic|synerg(?:y|ies))\b", F, "ad-slop verb or adjective", r"\bunlock(?:ed|ing)? (?:the )?(?:door|hut|cabin|lock|phone|gate|code|padlock)\b"),
 ("L03","P1","lexical", r"\b(?:leverag(?:e|es|ed|ing)|harness(?:es|ed|ing)?|streamlin(?:e|es|ed|ing)|utili[sz](?:e|es|ed|ing)|foster(?:s|ed|ing)?|showcas(?:e|es|ed|ing)|underscor(?:e|es|ed|ing)|bolster(?:s|ed|ing)?|pivotal|meticulous(?:ly)?|intricate|intricacies|robust|navigat(?:e|es|ed|ing) the)\b", F, "AI-vocabulary tier 1 (verbs and adjectives)",
   r"\b(?:climbing|glacier|rope|crampon|belay|via ferrata|sled|dog|avalanche|bergschrund|whiteout|software|api|code|server|finance|equity|debt|lever|navigate (?:the )?(?:whiteout|fog|cloud|map|route|lift|snow|terrain)|robust (?:shell|boot|ski|jacket|binding|glove|gear|construction))\b"),
 ("L04","P1","lexical", r"\b(?:vibrant|nestled|breathtaking|majestic|awe[- ]inspiring|picturesque|idyllic|enchanting|mesmerizing|captivating|stunning(?:ly)?|spectacular|magnificent|unforgettable|unmissable|must[- ](?:see|visit|do)|bucket[- ]list|once[- ]in[- ]a[- ]lifetime|hidden gems?|best[- ]kept secret|off the beaten (?:path|track)|like no other|second to none)\b", F, "travel-slop adjective", r"\bmajestic (?:hotel|theatre|theater)\b"),
 ("L05","P1","lexical", r"\b(?:immerse (?:yourself|yourselves)|immersive|adventure awaits|escape the ordinary|escape the (?:everyday|daily grind|crowds)|the magic of|discover the magic|magic awaits|say goodbye to|look no further|something for everyone|winter wonderland|natural playground|nature(?:~s)? playground|playground for|paradise on earth|your (?:next|ultimate|dream) (?:adventure|escape|getaway|journey)|take your .{1,25} to the next level|calling your name|memories that last a lifetime)\b", F, "travel/ad cliche phrase", r"\bimmersion suit\b"),
 ("L06","P1","lexical", r"\b(?:serves|stands|functions|acts|operates) as (?:a|an|the)\b|\bboasts?\b|\bfeatures? (?:a|an) (?:diverse|rich|wide|vast)\b|\ba diverse array\b|\ba (?:rich|vast|wide) (?:range|array|variety|selection) of\b", F, "copula dodge or inflated 'has'", None),
 ("L07","P1","lexical", r",\s+(?:highlighting|underscoring|emphasi[sz]ing|ensuring|reflecting|showcasing|fostering|symbolizing|cultivating|contributing to|enhancing|making it (?:the perfect|an ideal|easy to))\b", F, "shallow -ing rider", None),
 ("L08","P1","lexical", r"\b(?:is|are|stands as|serves as) (?:a )?testament to\b|\bplays? an? (?:crucial|pivotal|vital|key|significant) role\b|\bin today~s (?:fast[- ]paced|digital|ever[- ]changing|modern) world\b|\bever[- ]evolving\b|\bin the heart of\b|\brich (?:cultural )?(?:heritage|history|tapestry)\b|\bevolving landscape\b|\bindelible mark\b", F, "significance inflation", None),
 ("L09","P1","lexical", r"\b(?:experts|studies|research|critics|observers|many people|some say|industry reports|travellers|travelers|guests)\s+(?:argue|suggest|say|show|have shown|believe|agree|report|rave|love)\b", F, "vague attribution (name the source, or cut)", None),
 ("L10","P1","lexical", r"\bit~?s worth (?:noting|mentioning|remembering)\b|\bit is (?:worth noting|important to (?:note|remember|understand))\b|\blet~s (?:dive|delve|explore|unpack|break (?:this|it) down)\b|\bwithout further ado\b|\bhere~s (?:the (?:thing|kicker|catch|truth|secret)|what you need to know)\b|\bat its core\b|\bwhat really matters\b|\bthe real question is\b", F, "throat-clearing or fake-depth opener", None),
 ("L11","P1","lexical", r"\b(?:ready to|looking for|tired of|dreaming of|craving|searching for|want to|need a)\b[^.!?\n]{0,70}\?", F, "stock rhetorical-question opener", None),
 ("L12","P1","lexical", r"\b(?:furthermore|moreover|additionally|in addition|consequently|ultimately|overall)," , F, "filler transition", None),
 ("L13","P1","lexical", r"\b(?:in (?:conclusion|summary)|to sum up|all in all|at the end of the day|in a nutshell)\b", F, "summary closer", None),
 ("L14","P1","lexical", r"\b(?:could|might|may|can) (?:potentially|possibly|perhaps|arguably)\b|\bpotentially possibly\b|\bit could be argued\b", F, "hedge stack", None),
 ("L15","P1","lexical", r"\b(?:epic|ultimate|dream|perfect|ideal|unique|authentic|unforgettable) (?:adventure|getaway|escape|trip|holiday|vacation|experience|journey|destination)s?\b|\b(?:perfect|ideal|unique|seamless|harmonious) (?:blend|mix|combination|fusion|balance) of\b|\bdreams? (?:come|comes) true\b|\bfall(?:s|en)? in love with\b|\bchase the (?:northern lights|aurora|powder|thrill)\b", F, "ad cliche pairing", None),
 ("L16","P1","lexical", r"\b(?:your )?(?:trusted|one-stop|go-to|reliable) (?:partner|shop|solution|source)\b|\bfor all your [a-z]+ needs\b|\bexceptional (?:service|quality|customer|results)\b|\bcommitment to (?:excellence|quality|innovation)\b|\bdeliver(?:s|ing) (?:exceptional|outstanding|results|value|excellence)\b|\btop priority\b|\bpeace of mind\b|\bsafe and seamless\b", F, "service-business and corporate filler", None),
 # ---------- lexical: tier 2 (flag, review in context) ----------
 ("L20","P2","lexical", r"\b(?:quietly|deeply|fundamentally|remarkably|arguably|genuinely|truly|effortlessly|simply|literally|absolutely|incredibly|extremely|utterly|totally|amazingly|really)\b", F, "magic adverb or empty intensifier", None),
 ("L21","P2","lexical", r"\b(?:journey|landscape|ecosystem|paradigm|framework|solution|experience|curated|crafted|tailored|bespoke|world[- ]class|premier|ultimate|perfect|finest|epic|iconic|legendary|authentic|immerse|discover|explore|dive into|uncover|transform(?:s|ed|ing)?)\b", F, "tier 2 word: allowed once if literal, flag clusters",
   r"\b(?:epic pass|iconic pass|bergen line journey|train journey|boat journey|return journey|landscape (?:orientation|format)|transform(?:er|ing) (?:station|lift))\b"),
 ("L22","P2","lexical", r"\b(?:best|greatest|top[- ]rated|number one|#1|leading|unrivall?ed|unmatched|unbeatable|award[- ]winning)\b", F, "unsupported superlative: needs proof or cut", None),
 ("L23","P2","lexical", r"\b(?:crucial|vital|essential|key|valuable|enduring|enhanc(?:e|es|ed|ing)|align(?:s|ed|ing)? with|resonat(?:e|es|ed|ing) with|diverse|dynamic|innovative|comprehensive|nuanced)\b", F, "AI-vocabulary tier 2", None),
 # ---------- structural ----------
 ("S01","P1","structural", r"\b(?:it|this|that|these|those|they|we|you)(?:~s|~re| is| are| was| were| isn~t| aren~t| wasn~t| is not| are not| was not) (?:not )?(?:just |only |merely |simply |about |a matter of )?(?:not )?[^.!?\n;]{1,80}?(?:,|;|:|\u2014|\u2013| -- |\.\s+)\s*(?:it~s|it is|this is|that is|they~re|we~re|you~re|but|rather|instead|more)\b", F, "negative parallelism: 'not X, it is Y' (also reversed 'Y rather than X')", None),
 ("S01a","P1","structural", r"\bnot (?:just|only|merely|simply) [^.!?\n]{1,80}?,? but (?:also )?\b|\bmore than (?:just )?(?:a|an|another) [a-z-]+(?: [a-z-]+)?[,.;:] (?:it~s|it is)\b|\b(?:isn~t|is not) (?:about|just about) [^.!?\n]{1,60}\.\s+(?:it~s|it is) (?:about)?\b", F, "negative parallelism variant", None),
 ("S01b","P1","structural", r"\bnot (?:a|an|the)? ?[^.!?\n]{1,40}\.\s+not [^.!?\n]{1,40}\.\s+(?:just|only|a|an|the)\b|\bno [^.!?\n]{1,30},\s+no [^.!?\n]{1,30},\s+just\b", F, "countdown: 'Not X. Not Y. Just Z.'", None),
 ("S02","P1","structural", r"\bwhether you~?(?:re| are) (?:a |an )?[^.!?\n]{1,60}? or (?:a |an )?[^.!?\n]{1,60}?[,.!]", F, "'Whether you are X or Y' audience sweep", None),
 ("S03","P1","structural", r"\b(?i:the|a) (?i:result|catch|worst part|best part|truth|secret|kicker|twist|problem|answer|difference|best bit)\?\s+[A-Z]", 0, "'The X? A Y.' self-answered question", None),
 ("S04","P2","structural", r"(?m)^\s*imagine\b|\bimagine (?:a world|waking|standing|yourself|this|if)\b", F, "'Imagine' opener", None),
 ("S05","P2","structural", r"\bfrom [^.!?\n,]{2,40} to [^.!?\n,]{2,40},? (?:to|and) [^.!?\n]{2,40}\b", F, "false range 'from X to Y to Z'", r"\bfrom \d|\bfrom (?:mon|tue|wed|thu|fri|sat|sun|jan|feb|mar|apr)\w* to\b"),
 ("S06","P2","structural", r"\b(?:five|four|three|six|seven|\d+) (?:things|reasons|ways|tips|secrets|steps|mistakes)\b", F, "compulsive counting headline", None),
 ("S07","P2","structural", r"\b(?:think of it (?:as|like)|picture this|here~s the (?:thing|deal))\b", F, "patronising analogy or false suspense", None),
 ("S08","P2","structural", r"\b(?:despite (?:these|its|the) (?:challenges|setbacks|obstacles)|challenges and (?:legacy|opportunities)|future (?:outlook|prospects))\b", F, "outline-like challenges formula", None),
 # ---------- formatting ----------
 ("F01","P2","formatting", r"\*\*[^*\n]{1,80}\*\*|__[^_\n]{1,80}__", 0, "markdown bold", None),
 ("F02","P1","formatting", r"(?m)^\s{0,3}#{1,6}\s+\S", 0, "markdown heading in ad copy", None),
 ("F03","P2","formatting", r"(?m)^\s*(?:[-*\u2022]|\d+[.)])\s+\S", 0, "bullet or numbered list (fine on a landing page, suspect in a feed ad)", None),
 ("F04","P1","formatting", r"(?m)^\s*(?:[-*\u2022]\s+)?\*\*[^*\n]+\*\*\s*[:\-]", 0, "bold-first bullet: '**Label**: text'", None),
 ("F05","P1","formatting", r"(?:#[A-Za-z0-9_]+[ \t]*){4,}", 0, "hashtag stack (4 or more)", None),
 ("F06","P2","formatting", r"[\u2192\u2190\u21d2\u2248\u26a0\u2713\u2714\u2605\u2606\u25b6\u00bb]", 0, "decorative unicode symbol", None),
 ("F07","P3","formatting", r"[\u2018\u2019\u201c\u201d]", 0, "curly quotes (weak signal alone)", None),
 ("F08","P2","formatting", r"(?m)^(?:\s*[-*_]{3,}\s*)$", 0, "horizontal rule between sections", None),
 ("F09","P2","formatting", r"(?m)^[A-Z][a-z]+(?: [A-Z][a-z]+){3,}$", 0, "Title Case headline of 4+ words", None),
 # ---------- ad-specific honesty flags ----------
 ("A01","P1","honesty", r"\b(?:only|just) (?:a )?(?:few|\d+) (?:spots?|places?|slots?|seats?|rooms?) (?:left|remaining)\b|\b(?:few|limited|last|final) (?:spots?|places?|slots?|seats?)\b|\bselling (?:out )?fast\b|\bdon~t miss out\b|\bhurry\b|\bact now\b|\bwhile (?:stocks|spots) last\b|\bbefore (?:the |all )?(?:spots|places|seats|slots|tickets|it|they)(?: all)? (?:run|runs|sell|sells|are gone)\b|\bsell(?:s|ing)? out\b", F, "scarcity or urgency claim: needs a live availability check [VERIFY]", None),
 ("A02","P1","honesty", r"\b(?:guaranteed|100% (?:safe|satisfaction)|risk[- ]free|no risk|safest|cheapest|lowest price|cures|cured|miracle cure|fully refundable)\b", F, "absolute claim: needs proof or cut", r"\b(?:not|never|cannot|can~?t|don~?t|no|without) (?:\w+ ){0,3}(?:guaranteed|promise|risk)"),
 ("A03","P1","honesty", r"\b(?:rated|rating of) [0-9.]+|\b[0-9.]+/5\b|(?<![\d,])\d(?:\.\d)? stars?\b|\b\d[\d,]* (?:happy|satisfied) (?:guests|customers|travell?ers|skiers)\b|\b\d{2,}% of (?:guests|customers|clients)\b|\b(?:thousands|hundreds|millions) of (?:happy |satisfied |delighted |loyal )?(?:guests|customers|clients|skiers|travell?ers|people|users)\b|\bjoin (?:thousands|hundreds|millions|\d[\d,]*)\b", F, "social-proof number: needs a source [VERIFY]", None),
 ("A04","P1","honesty", r"[\"\u201c][^\"\u201d\n]{15,200}[\"\u201d]\s*[,.\u2014\u2013-]?\s*(?:[A-Z][a-z]+,?\s+(?:from|of)\s+[A-Z]|a (?:happy|recent|satisfied) (?:guest|customer|skier|traveller|traveler))", 0, "quoted testimonial: must be a real, permitted quote [VERIFY]", None),
]

COMPILED = [(i, s, c, re.compile(p.replace("~", APOS), fl), m, (re.compile(x, re.I) if x else None)) for (i, s, c, p, fl, m, x) in RULES]
ALLCAPS_ALLOW = {"NOK", "USD", "EUR", "UTM", "FAQ", "GPS", "ABS", "VAT", "SMS", "HTML", "JSON"}

def sentences(text):
    t = re.sub(r"\s+", " ", text.strip())
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"\u201c'(])", t)
    return [p for p in parts if p]

def words(s):
    return re.findall(r"[A-Za-z0-9\u00c0-\u024f'\u2019-]+", s)

def metrics(text, channel="meta"):
    out = []
    ws = words(text)
    n = len(ws)
    if n == 0:
        return out
    sents = sentences(text)
    lens = [len(words(s)) for s in sents]
    # M01 uniform rhythm (heuristic thresholds, tune on your corpus)
    if len(lens) >= 6 and statistics.mean(lens) > 0:
        cv = statistics.pstdev(lens) / statistics.mean(lens)
        if cv < 0.35:
            out.append(("M01", "P2", "rhythm", f"sentence length too uniform (CV={cv:.2f}, mean={statistics.mean(lens):.1f})"))
    # M02 no short sentence in a long text
    if len(lens) >= 6 and min(lens) > 6:
        out.append(("M02", "P2", "rhythm", f"no sentence under 7 words (min={min(lens)}); add a fragment"))
    # M03 repeated sentence openings
    firsts = [w[0].lower() for w in (words(s) for s in sents) if w]
    for k in set(firsts):
        if firsts.count(k) >= 3 and len(firsts) >= 4 and k not in ("the", "a"):
            out.append(("M03", "P2", "rhythm", f"{firsts.count(k)} sentences start with '{k}'"))
    # M04 specificity: digits and capitalised mid-sentence names per 100 words
    digits = len(re.findall(r"\d[\d,.:]*", text))
    names = len(re.findall(r"(?<=[a-z,] )[A-Z][a-z\u00c0-\u024f]{2,}", text))
    if n >= 40 and (digits + names) / n * 100 < 3:
        out.append(("M04", "P1", "semantic", f"low specificity: {digits} numbers and {names} named things in {n} words; add a price, date, place, gear or time"))
    # M05 tricolon density
    tri = re.findall(r"\b[A-Za-z-]{3,}, [A-Za-z-]{3,},? (?:and|&|or) [A-Za-z-]{3,}\b", text)
    if n >= 40 and len(tri) >= 2:
        out.append(("M05", "P2", "structural", f"{len(tri)} three-item lists in {n} words: {tri[:3]}"))
    # M06 exclamation density
    ex = text.count("!")
    if ex >= 2 and ex / max(len(sents), 1) > 0.25:
        out.append(("M06", "P2", "tonal", f"{ex} exclamation marks in {len(sents)} sentences"))
    # M07 colon reveal density
    colons = len(re.findall(r"[A-Za-z]: [A-Z]", text))
    if colons >= 3:
        out.append(("M07", "P2", "structural", f"{colons} colon reveals"))
    # M08 word budget by channel (Meta primary text is cut after about 125 characters in feed; verify in platform notes)
    return out

def lint(text, channel="meta"):
    hits = []
    for rid, sev, cat, rx, msg, sup in COMPILED:
        for m in rx.finditer(text):
            if rid == "H06" and (m.group(0) in ALLCAPS_ALLOW):
                continue
            if sup is not None:
                a, b = max(0, m.start() - 40), min(len(text), m.end() + 40)
                if sup.search(text[a:b]):
                    continue
            line = text.count("\n", 0, m.start()) + 1
            hits.append({"id": rid, "sev": sev, "cat": cat, "line": line, "match": m.group(0)[:80], "msg": msg})
    for rid, sev, cat, msg in metrics(text, channel):
        hits.append({"id": rid, "sev": sev, "cat": cat, "line": 0, "match": "", "msg": msg})
    order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    hits.sort(key=lambda h: (order[h["sev"]], h["line"]))
    return hits

def verdict(hits):
    if any(h["sev"] == "P0" for h in hits): return "BLOCK"
    p1 = sum(h["sev"] == "P1" for h in hits); p2 = sum(h["sev"] == "P2" for h in hits)
    if p1 >= 1 or p2 >= 4: return "REVISE"
    return "PASS"

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    text = open(args[0], encoding="utf-8").read() if args else sys.stdin.read()
    hits = lint(text)
    if "--json" in sys.argv:
        print(json.dumps({"verdict": verdict(hits), "hits": hits}, indent=2))
    else:
        for h in hits:
            print(f"{h['sev']} {h['id']} line {h['line']}: {h['msg']} :: {h['match']!r}")
        print("VERDICT:", verdict(hits))
    sys.exit(2 if any(h["sev"] == "P0" for h in hits) else 1 if any(h["sev"] == "P1" for h in hits) else 0)
```

### 7.5 Tests

Run `python3 -I test_lint.py` next to the linter. Expected output: `failures: 0 of 50`.

```python
import sys; sys.path.insert(0, ".")
from adwright_lint import lint, verdict
EM, EN = "\u2014", "\u2013"
POS = [  # (text, expected rule id)
 (f"It's not just a ski trip {EM} it's a way of life.", "S01"),
 ("It's not just a ski trip, it's a way of life.", "S01"),
 ("This isn't about skiing. It's about freedom.", "S01a"),
 ("Not a lift queue. Not a crowd. Just snow.", "S01b"),
 ("Not only a tour, but also a story.", "S01a"),
 ("Whether you're a first-timer or a seasoned pro, we have a tour.", "S02"),
 ("Ready to ski the fjords?", "L11"),
 ("The result? Powder.", "S03"),
 ("Discover the magic of Voss.", "L05"),
 ("Escape the ordinary and unlock your next adventure.", "L02"),
 ("We delve into the fjords.", "L01"),
 ("Nestled in the heart of Voss, a hidden gem awaits.", "L04"),
 ("A breathtaking, unforgettable bucket list trip.", "L04"),
 ("Say goodbye to crowded resorts.", "L05"),
 ("Great question! Here is a revised ad.", "C01"),
 ("Ski the fjord " + EN + " 9 days.", "H02"),
 ("Ski the fjord \u2744 now", "H05"),
 ("Book now!!", "H07"),
 ("Only 3 spots left", "A01"),
 ("Rated 4.9 stars by guests.", "A03"),
 ("Experts agree this is the best tour.", "L09"),
 ("Our guides leverage deep local knowledge.", "L03"),
 ("In conclusion, it was great.", "L13"),
 ("It's worth noting that snow varies.", "L10"),
 ("The lodge serves as a base, highlighting local culture.", "L06"),
 ("Skiing, highlighting local culture, fostering community.", "L07"),
 ("**Safety**: guides carry radios", "F04"),
 ("#ski #norway #voss #fjord #powder", "F05"),
 ("It could potentially work.", "L14"),
 ("Furthermore, the tour is good.", "L12"),
 ("An epic adventure, a perfect blend of fun and rest.", "L15"),
 ("Join thousands of happy guests!", "A03"),
 ("Book before spots run out.", "A01"),
 ("Your trusted partner for all your ski needs.", "L16"),
 ("Dreams come true here.", "L15"),
]
NEG = [
 ("We cannot promise fresh snow.", "A02"),
 ("The cure for a tired Sunday is a long run.", "A02"),
 ("More than 54,000 stars on GitHub.", "A03"),
 ("Snow is not guaranteed in February.", "A02"),  # (text, rule id that must NOT fire)
 ("Climbing harness and rope are included.", "L03"),
 ("You will need a harness for the glacier crossing.", "L03"),
 ("The gondola climbs 900 m. Elevation gain is 900 m.", "L02"),
 ("Unlock the cabin door with the brass key.", "L02"),
 ("Bayeux tapestry shop.", "L01"),
 ("Robust shell jacket recommended.", "L03"),
 ("Departures run from 30 Jan to 7 Feb.", "S05"),
 ("Prices in NOK, VAT included.", "H06"),
 ("Departs every Saturday and Sunday, January to April.", "S05"),
 ("The Bergen Line train journey takes about an hour and a half.", "L21"),
 ("We are ready to ski at 08:30.", "L11"),
]
fail = 0
for t, rid in POS:
    ids = {h["id"] for h in lint(t)}
    if rid not in ids:
        fail += 1; print("MISSED", rid, "::", t, "got", sorted(ids))
for t, rid in NEG:
    ids = {h["id"] for h in lint(t)}
    if rid in ids:
        fail += 1; print("FALSE POSITIVE", rid, "::", t)
print("failures:", fail, "of", len(POS) + len(NEG))
```

### 7.6 Suggested extensions

- Channel switch: for `web`, downgrade F01, F02, F03 to P3. For `x`, add a 280-character check and cap hashtags at 2 (confirm X's current character limits in the platform notes, not here).
- Config files: `allowlist.txt` for proper nouns and caps words, `blocklist.txt` for client-specific words.
- Quote shield: replace text between marked quote delimiters with spaces before linting.
- Autofix map for safe cases only: replace `--` with a comma, strip emoji, strip `**`. Do not autofix words.
- Output JSON with `--json` for the skill to read.
- Add a fact check hook: every digit sequence in the draft must appear in the brief. This catches invented numbers, which is more important than any word list. I did not write this check.

### How adwright should use this

Treat the linter as the skill's seatbelt, and put it first in the README. Run it in the skill's loop (draft, lint, revise once, lint). Publish the rule table and the regression pairs so contributors can add rules by pull request, with a failing test first. Do not describe it as a detector or promise any detection score. It is an editor.

## 8. Ethics

The goal is better writing and honest writing. Not fooling detectors.

Why not detector evasion:

- A tool that markets itself as "undetectable" invites misuse in schools and in fake reviews, and the repo would be judged for it.
- It does not work well anyway. Experienced readers still spot stock phrases after humanizer tools and paraphrasing (Russell et al.).
- In advertising, being "detected" is not the harm. Being wrong, misleading or fake is.

Hard rules for the skill:

1. No fake reviews. No invented testimonials. No invented guest quotes. No invented ratings or review counts. The skill can structure a request for a real review, or format a real review the client supplies verbatim with permission.
2. No fabricated specifics. Every number, date, name, distance, temperature and promise must come from the brief. Otherwise ask, or leave it out, or tag [VERIFY].
3. No fake urgency or scarcity. "Few spots left" needs a live availability fact. The client's confirmed-facts note says the hub shows a "Few Slots left" badge and that Meta penalizes false urgency and Norwegian marketing law treats it as misleading. I did not verify the Meta policy in this research file. [VERIFY: platform notes].
4. No absolute claims without proof: guaranteed, safest, risk-free, best.
5. Do not bypass, spoof or advertise as defeating AI detectors, and do not offer a "detector score" mode.
6. Keep human accountability. The client approves every ad. The skill produces drafts and a change log.

What the law and regulators say (checked, with limits):

- United States. The FTC final rule on fake reviews and testimonials was issued 14 August 2024 and took effect 21 October 2024. It bans fake or false reviews, including AI-generated ones, and allows civil penalties, stated as $51,744 per violation in law-firm summaries. https://www.wsgr.com/en/insights/ftc-issues-final-rule-banning-fake-and-misleading-consumer-reviews-and-testimonials.html and https://www.alston.com/en/insights/publications/2024/10/ftc-issues-final-rule-on-fake-reviews-testimonials . [VERIFY: current penalty amount, which adjusts for inflation].
- Norway. Forbrukertilsynet (the Consumer Authority) says businesses must not buy fake reviews or encourage employees to write reviews that do not reflect real experience. They must not delete negative reviews and publish only positive ones, and must clearly identify compensated reviews. https://www.forbrukertilsynet.no/lov-og-rett/veiledninger-og-retningslinjer/brukeromtaler-i-markedsforing . I read an English rendering of the Norwegian page, not the Norwegian text itself.
- Norway and AI labels. On 4 January 2024, Forbrukertilsynet concluded that the marketing act's retouching label does not cover AI-generated advertising, and recommended a law change. Misleading-marketing rules still apply to AI content. https://www.kampanje.com/markedsforing/forbrukertilsynet-ferdig-med-ki-utredning-merkeplikten-gjelder-ikke/716171 . That is a 2024 position and may have changed. [VERIFY: current status].
- EU. Article 50 of the AI Act brings transparency duties from 2 August 2026, including labeling of AI-generated text published to inform the public on matters of public interest, and deepfakes. Law-firm commentary says advertising examples in the Commission's guidelines are treated as needing standard labeling, with narrow room for exceptions. https://www.reedsmith.com/our-insights/blogs/viewpoints/102nbz0/transparency-obligations-for-ai-generated-content-the-code-of-practice-adequacy/ . I did not read the guidelines. Whether plain ad copy for a Norwegian operator is in scope, and how the EEA applies the act, is unclear. [VERIFY with a lawyer].

This is research, not legal advice.

### How adwright should use this

Put a short "What adwright will not do" section in the README: no fake reviews, no invented quotes, no detector bypass. It builds trust and protects the repo. In the skill, make the fact check a hard gate: if a number in the draft is not in the brief, the output must say so in a visible note. Add a client-facing line in each deliverable: "Specifics in this copy come from the brief. Items tagged [VERIFY] need your confirmation."

## 9. Open items and uncertainties

- The Wikipedia page came through a summarizing fetch tool in three passes. The reference list and exact study titles were mostly not returned.
- Reinhart et al. numbers were not opened. Juzek and Ward, and Russell et al., were read at abstract level only.
- Pangram's figures and GPTZero's accuracy are vendor claims. Corpus details are not published on the pages I read.
- The Science Advances page for Kobak et al. blocked the fetch (HTTP 403). I used the arXiv preprint, which matches the published title and numbers I could confirm. The published version may differ in small details.
- Reddit and X were not usable through the tools. No Reddit or X quotes are in this file.
- The July 2026 em dash study cited on Wikipedia was not opened.
- The linter has not been run on a corpus of human ad copy, so its false-positive rate on real work is unknown. Run it on 50 of the client's existing captions before trusting thresholds.
- The brief calls the skill adwright. The client repo is currently named adquill. Confirm the final name before publishing.
- The tools that read GitHub could not open the avoid-ai-writing file directly; I used a summary of it.

## 10. Source list

- https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- https://www.npr.org/2025/09/04/nx-s1-5519267/wikipedia-editors-publish-new-guide-to-help-readers-detect-entries-written-by-ai
- https://arxiv.org/abs/2406.07016 (Kobak et al.)
- https://arxiv.org/abs/2412.11385 (Juzek and Ward)
- https://www.pnas.org/doi/10.1073/pnas.2422455122 (Reinhart et al.)
- https://arxiv.org/abs/2501.15654 (Russell, Karpinska, Iyyer)
- https://www.pangram.com/signs-of-ai-writing
- https://www.pangram.com/resources/most-common-ai-phrases
- https://www.pangram.com/blog/russell
- https://arxiv.org/abs/2603.27006 (Freeburg)
- https://news.fiu.edu/2026/why-does-ai-use-so-many-em-dashes-an-expert-explains
- https://gptzero.me/news/how-ai-detectors-work/
- https://www.cell.com/patterns/fulltext/S2666-3899(23)00130-7 (Liang et al.)
- https://www.nber.org/system/files/working_papers/w34223/w34223.pdf (Jabarian and Imas)
- https://arxiv.org/abs/2310.13548 (sycophancy)
- [link: Anthropic prompting guide for the current Claude model, left out because its address names a model]
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- [link: Adpharm anti-slop playbook, left out because its address names a model]
- https://github.com/blader/humanizer
- https://github.com/conorbronsdon/avoid-ai-writing
- https://github.com/Anbeeld/WRITING.md
- https://gist.github.com/ossa-ma/f3baa9d25154c33095e22272c631f5a1 and https://tropes.fyi/
- https://gourmantic.com/perched-nestled-and-other-hidden-gems/
- https://www.pitchtravelwrite.com/cliches.html
- https://siliconangle.com/2023/03/30/buzzfeeds-new-ai-generated-travel-articles-dystopian-bad-dream/
- https://blog.ricksteves.com/cameron/2023/07/ai-vs-human-traveler
- https://www.wsgr.com/en/insights/ftc-issues-final-rule-banning-fake-and-misleading-consumer-reviews-and-testimonials.html
- https://www.forbrukertilsynet.no/lov-og-rett/veiledninger-og-retningslinjer/brukeromtaler-i-markedsforing
- https://www.kampanje.com/markedsforing/forbrukertilsynet-ferdig-med-ki-utredning-merkeplikten-gjelder-ikke/716171
- https://www.reedsmith.com/our-insights/blogs/viewpoints/102nbz0/transparency-obligations-for-ai-generated-content-the-code-of-practice-adequacy/
