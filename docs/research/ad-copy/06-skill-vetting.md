# 06 Skill vetting: what to install, what to copy from, what to skip

Date of vetting: 2026-10-06. Nothing was installed into this repo. Nothing from these repos was executed.

## 0. Method, safety and how to read this file

What I did:

- Shallow clones (`git clone --depth 1`) of 36 candidate repos were read as local copies. This repo does not hold them. Three more (gbrain, Graft and claude-plugins-official) had already been cloned the same way.
- Live stars, license, push date and description come from the GitHub repository search API (via the GitHub tool), queried on 2026-10-06. Last-commit dates, sizes, SKILL.md counts and word counts come from the local clones.
- I read the actual SKILL.md files for every candidate that matters, plus the references for the ones I rate highly. I ran read-only greps (no code execution) over every clone for: hooks files, MCP configs, install scripts, network calls, credential names, telemetry, base64 or eval patterns, curl-pipe-shell, zero-width or bidi characters, and prompt-injection phrases.
- For the platform and plugin schema questions I cross-checked the cloned official repo against the live Claude Code docs (code.claude.com/docs).
- Everything fetched is treated as data. Where a README or SKILL.md told the reader to do something (install, run a script, connect a server), I recorded it as a finding and did not act on it.

Rules I applied to the verdicts:

- INSTALL means: text-only or near text-only, reads clean, relevant to Meta or X ad copy or to humanizing copy, no side effects, and worth the context cost.
- REFERENCE-ONLY means: read it for ideas, do not copy it into the client repo.
- SKIP means: off topic, thin, risky, or both.
- A skill can be good and still not be worth installing, because installed skills load their descriptions into every session and overlapping skills compete to trigger. The user's own principle (nothing unrelated to the work) is the tie-breaker.

Limits of this vetting:

- I judged text, not behaviour. I did not run any skill against a test brief, so "quality" here means: reads as substance, avoids slop itself, specs match what I could verify. A trial run in a scratch repo is still the final gate before anything lands in the client repo.
- Star counts move daily. They are accurate for 2026-10-06 only.
- Pinned commit hashes are listed in section 1.6 so an install can fetch exactly what I read.

## 1. Part A: copywriting and paid social skills

### 1.1 Bottom line

- Seven of the eight things worth installing come from four repos: coreyhaines31/marketingskills (four skills), blader/humanizer, avectats7/copy-that-sells, and mikefutia/conversion-copywriter-skill. The eighth is one skill from gbrain (fact-check), copied by hand and trimmed.
- The named candidates mostly fail the bar. realkimbarrett/advertising-skills is 12 files of 60 to 180 words each. yabasha/copywrite-skill is B2B SaaS only. zubair-trabzada/ai-ads-claude is a generic template pack with emoji instructions. robpalmer99's Meta skill is real craft but built for supplement-style direct response and encourages tactics Meta penalises. AgriciDaniel/claude-ads is a well-built account audit system (34 skills, 80 scripts) and a poor fit for writing ad copy.
- No candidate covers X (Twitter) ads in depth. Corey's `ad-creative` and `social` skills have X sections; claude-ads has an X audit. Nobody has a verified X ad copy workflow. That is a gap adwright can fill.
- Meta spec accuracy is mixed. Several skills give the Facebook feed headline as 40 characters. Meta's own page says 27 for Facebook feed and 40 for Instagram feed (verified in research file 03). adwright must carry its own verified spec table and override any installed skill that disagrees.
- The instruction text of most skills uses em dashes heavily (see table in 1.5). The client style rule bans them in output. Installed copies should be scrubbed of em dashes once, and adwright's own rules should win on conflict.

### 1.2 Ranked table

Ranked by usefulness to this job (Meta and X ad copy for a Norwegian ski tour operator, honest, human sounding). Stars are live on 2026-10-06. Size excludes .git. "Last commit" is the clone HEAD date.

| Rank | Repo | Stars | License | Last commit | Size | SKILL.md files | Verdict |
|---|---|---|---|---|---|---|---|
| 1 | coreyhaines31/marketingskills | 53,420 | MIT | 2026-10-02 | 5.6 MB | 50 | INSTALL four skills only (copywriting, ad-creative, social, marketing-psychology) |
| 2 | blader/humanizer | 54,287 | MIT | 2026-09-27 | 136 KB | 1 | INSTALL |
| 3 | avectats7/copy-that-sells | 17 | MIT | 2026-07-21 | 632 KB | 1 (plus 11 reference files) | INSTALL (with a caveat on age and low stars) |
| 4 | mikefutia/conversion-copywriter-skill | 10 | MIT | 2026-07-22 | 96 KB | 1 | INSTALL (SKILL.md only, drop the script) |
| 5 | hardikpandya/stop-slop | 17,789 | MIT | 2026-03-18 | 40 KB | 1 | REFERENCE-ONLY (humanizer covers it; tiny, so safe to add later) |
| 6 | boraoztunc/skills (ogilvy skill) | 391 | Apache-2.0 (repo), MIT (skill frontmatter) | 2026-08-15 | 3.8 MB | 70 | REFERENCE-ONLY (one good file inside a design-heavy grab bag) |
| 7 | Yuzzyuk/marketing-os | 535 | MIT | 2026-08-17 | 220 KB | 1 (plus 18 references) | REFERENCE-ONLY (hooks.md, social.md, slop-patterns.md) |
| 8 | XZTP/meta-ads-optimiser | 2 | MIT | 2026-04-09 | 192 KB | 1 (plus 17 references) | REFERENCE-ONLY (best Meta platform notes, but no star signal) |
| 9 | digitaladsnack/digital-ad-snack-ai-tools-for-meta-ads | 0 | MIT | 2026-10-01 | 212 KB | 6 | REFERENCE-ONLY (awareness-level to concept mapping; output uses emoji) |
| 10 | robpalmer99/claude-code-copywriting-skills | 39 | CC BY 4.0 (GitHub shows NOASSERTION) | 2026-05-12 | 148 KB | 5 | REFERENCE-ONLY (craft is real, tactics do not fit this client) |
| 11 | wondelai/skills (influence-psychology, made-to-stick, contagious, storybrand-messaging) | 2,347 | MIT | 2026-09-10 | 21.6 MB | 196 | REFERENCE-ONLY (book summaries; pick files, never the bundle) |
| 12 | unicorn-marketers/red-team | 10 | MIT | 2026-05-26 | 200 KB | 1 | REFERENCE-ONLY (adversarial buyer review idea is worth borrowing) |
| 13 | MADEVAL/MindFluence | 50 | MIT | 2026-07-12 | 408 KB | 1 (13,000 words) | REFERENCE-ONLY (ethical gate is good; the file is far too large to load) |
| 14 | dripips/plain-prose | 25 | MIT | 2026-09-08 | 1.0 MB | 1 | REFERENCE-ONLY (same job as humanizer; has a JS checker I did not run) |
| 15 | Aboudjem/humanizer-skill | 264 | MIT | 2026-09-06 | 3.7 MB | 1 | SKIP (overlaps humanizer, adds CLI and docs site, voice presets aimed at detector evasion) |
| 16 | miqdadbadjuber/anti-slop | 4,569 | MIT | 2026-10-05 | 1.4 MB | 6 | SKIP for install (code and UI focus; its copywriting skill is useful to read) |
| 17 | AgriciDaniel/claude-ads | 9,743 | MIT | 2026-09-11 | 6.6 MB | 34 | REFERENCE-ONLY (audit and ops system, not a copy writer) |
| 18 | alirezarezvani/claude-skills (x-twitter-growth, ad-creative, content-humanizer) | 27,761 | MIT | 2026-08-26 | 52.6 MB | 846 | SKIP the bundle (846 skills, hooks in sub-plugins); read x-twitter-growth only |
| 19 | kostja94/marketing-skills | 1,014 | MIT | 2026-10-06 | 2.2 MB | 172 | SKIP (SEO heavy; Meta skill is 519 words of generic structure) |
| 20 | zubair-trabzada/ai-ads-claude | 267 | MIT | 2026-04-07 | 536 KB | 16 | SKIP |
| 21 | zubair-trabzada/ai-marketing-claude | 2,717 | MIT | 2026-03-01 | 488 KB | 15 | SKIP |
| 22 | realkimbarrett/advertising-skills | 757 | none stated in repo (frontmatter says MIT, no LICENSE file) | 2026-03-26 | 180 KB | 12 | SKIP |
| 23 | yabasha/copywrite-skill | 6 | none | 2026-02-14 | 60 KB | 1 | SKIP |
| 24 | brandonuttley/direct-response-copywriting-skill | 9 | MIT | 2026-04-24 | 92 KB | 1 | SKIP (long-form sales letters, not ads) |
| 25 | arturseo-geo/marketing-skill | 36 | MIT | 2026-03-24 | 100 KB | 1 | SKIP (generic overview, 2,479 words) |
| 26 | ivangfalco/ads-skills | 278 | MIT | 2026-07-15 | 936 KB | 4 | SKIP (B2B, runs API scripts with access tokens) |
| 27 | mathiaschu/meta-ads-analyzer | 439 | MIT | 2026-02-26 | 92 KB | 1 | SKIP (account analysis, setup.sh handles tokens) |
| 28 | YSY-99/meta-ads-api-field-guide | 16 | MIT | 2026-04-14 | 308 KB | 1 | SKIP (API automation, not copy) |
| 29 | Sandy-zippy/meta-ads-stack | 5 | MIT | 2026-06-16 | 196 KB | 6 | SKIP (operates live ad accounts, cron plist) |
| 30 | myroslavnahirniak/meta-ads-pro | 6 | none | 2026-06-04 | 2.3 MB | 1 | SKIP (Ukrainian language, account operations, no license) |
| 31 | Hainrixz/claude-ads | 93 | MIT | 2026-05-12 | 15.2 MB | 20 | SKIP (community fork of claude-ads; scripts publish to 14 social networks via a paid third party) |
| 32 | irinabuht12-oss/marketing-skills | 3,653 | none | 2026-09-23 | 7.7 MB | 49 | SKIP (vendor funnel: 101 files point at the Ryze MCP connector; includes a zip) |
| 33 | tarsluna/my-custom-skills | 12 | MIT | 2026-09-02 | 2.4 MB | 21 | SKIP (curl-pipe-bash installer, cron script, image-generation CLIs, French agency workflow) |
| 34 | vercel-labs/skills | 33,235 | MIT | 2026-10-05 | 1.5 MB | 2 | not a skill pack: the `npx skills` installer CLI. Do not use it (telemetry, see 1.7) |

Notes on the table:

- Stars for MindFluence, red-team, mikefutia, copy-that-sells and XZTP are in the single or double digits. Low stars are not a reason to reject text-only skills, but there is no community review behind them, so I read them line by line instead of trusting a count.
- blader/humanizer (54k stars) and marketingskills (53k stars) are the two clear standards in this space. Everything else is an order of magnitude smaller or more.
- gbrain, Graft and the official plugins repo are covered in Parts B, C and D, not here.

### 1.3 The seven candidates named in the brief

#### coreyhaines31/marketingskills (verified, 53,420 stars, MIT)

What is inside: 50 skills, 347 markdown files, about 428,000 words, plus `tools/clis/` (about 70 small Node CLIs for third-party services such as Kit, Hotjar, Ahrefs) and `tools/composio`, `tools/integrations`. Plugin manifests for Claude Code and Codex. Version 2.11.17.

What matters for adwright:

- `copywriting` (1,669 words, 3 references). Strong. It has an explicit "No AI Tells" section that bans contrast reveals, negation lists, trailing pile-ons, colon reveals, stock openers and em dashes in short copy. It also forces a swap test (would this line work on a competitor's site) and tells the model to flag `[NEED: differentiator]` rather than invent proof. Its own body text has zero em dashes. The page-structure sections are aimed at websites, so the ad-relevant half is the principles and the AI-tells list.
- `ad-creative` (3,469 words, 10 references). The most relevant file. It covers angles, hook systems, grounded inputs (every concept must cite a review, winning ad or comment, and the skill stops if the corpus is empty), platform spec tables for Google, Meta, LinkedIn, TikTok and X, static ad templates, a Meta creative format tier list, and iterate-from-performance-data loops. It is long and half of it is video and generative-tool production that adwright will not use. The body uses 59 em dashes.
- `social` (2,714 words, 9 references). Includes `x-algorithm.md` (posting rules derived from the open-sourced X ranking code). Useful for X native posts. Organic focus, not paid.
- `marketing-psychology` (3,025 words). A catalogue of mental models with marketing applications. Broad and generic. It is acceptable as a reminder list; the deeper psychology material in research file 02 is better.
- `ads` (4,322 words) is campaign strategy and audit, not copy. Skip. It contains the phrase "ignore previous instructions" only as a defensive rule about untrusted data (checked in context).

Safety read:

- The skills folders are markdown plus `evals/evals.json`. No hooks, no `.mcp.json`, no scripts inside the skills I propose to copy.
- The 71 script files are the `tools/clis/*.js` service CLIs. They read API keys from environment variables and call third-party services. They are not part of any skill and do not run unless someone invokes them. Do not copy `tools/`.
- Install route in the README is `npx skills add ...` (telemetry, see 1.7) or `/plugin marketplace add coreyhaines31/marketingskills` (installs all 50 skills). Use neither. Copy four folders.

Accuracy notes:

- The `ad-creative` Meta table says headline 40 characters and description 30. Meta lists 27 for Facebook feed headline and 40 for Instagram feed (research file 03, section on Meta spec). Its X table lists 280 for post text and 70 for card headline, which matches the reported figures in file 03; the 200 character card description figure is not verified there.
- `copywriting` quotes "+81% conversions, 38% shorter sales cycle, 28% lower CAC, 175% more referrals" for clearer positioning with no source link. Treat as [VERIFY: no source given in the skill]. Do not let adwright repeat it.

Risk note: low for the four text skills. Medium if the whole repo or plugin is installed (50 skills compete for triggers, mostly SaaS growth).

Verdict: INSTALL `copywriting`, `ad-creative`, `social`, `marketing-psychology`. Do not install the rest.

#### AgriciDaniel/claude-ads (verified, 9,743 stars, MIT)

What is inside: 34 SKILL.md files (33 under `skills/` plus the `ads/` orchestrator), 128 markdown files, 80 scripts (Python), a `claude_ads_core` package, a `control-plane`, evals, `install.sh` and `install.ps1`. Version 2.0.2. Covers Google, Meta, YouTube, LinkedIn, TikTok, Microsoft, Apple, Amazon, Reddit, Pinterest, Snapchat and X.

Judgement:

- This is a serious account-audit and operations system: scoring, JSON run bundles, mutation gates, capability gates. It is careful about not inventing claims ("Do not invent testimonials, certifications, scarcity, prices, outcomes").
- Its Meta creative reference refuses to hardcode spec numbers ("volatile; resolve from current official evidence"). That is honest and also useless as a spec table.
- `ads-create` is a brief-and-concept generator (223 words). `ads-x` is an audit procedure (229 words). Neither writes copy.
- The `ads/SKILL.md` and `ads-setup` hits for curl-pipe-shell are rules that refuse such installs. Clean on that point.
- The scripts call the network (page fetch, screenshots, live audits) and read credential variables. They are opt-in, but it is 80 scripts and a Python dependency set for a task that needs none.

Verdict: REFERENCE-ONLY. Borrow the idea of a source ledger and the cold-start rule in `ads-meta` (do not apply mature-account benchmarks to a new pixel). Do not install. Risk: medium (scripts, installer, dependency set, broad scope).

#### zubair-trabzada/ai-ads-claude (verified, 267 stars, MIT)

What is inside: 16 SKILL.md files (15 skills plus an orchestrator, about 43,000 words), 5 agents, `install.sh` (curl-pipe-bash path offered in the README), a PDF report script.

Judgement: `ads-copy` generates "10+ variations" using PAS, AIDA, BAB and 4Ps. Spec tables are generic and the Facebook feed headline is 40 characters (Meta says 27). The checklist tells the model to use emojis for Meta. The agitate step says "twist the knife". It has no X ads at all. Reads like a template pack, not craft. 26 em dashes in `ads-copy`.

Verdict: SKIP. Risk: low-medium (installer, `python3 ~/.claude/skills/...` execution path in the orchestrator).

#### robpalmer99/claude-code-copywriting-skills (verified, 39 stars, CC BY 4.0)

What is inside: five skills: `ad-copy` (Meta), `direct-response-copy`, `landing-page-copy`, `copychief` (copy review), `compliance-checker`. About 14,500 words. No scripts, no hooks.

Judgement:

- The `ad-copy` skill is real craft: awareness levels, sell-the-click versus sell-the-solution, see-more truncation at 125 characters, a clean spec table (headline 27 optimal, 40 max), hook types, and a rule to be specific ("47,312 women" over "thousands").
- It is written for health and supplement direct response. Examples lean on withheld information ("a reason your doctor won't tell you"), demographic callouts ("Attention men over 50"), and "it's not a diet, not a pill" negation hooks. Research file 03 lists personal-attribute phrasing (an age callout is one) and unprovable claims as Meta policy risks, and notes X's policy against sensationalised, clickbait style copy (the X page itself returned 403 there, so that part is a summary). The negation hooks also clash with the client rule against the contrast pattern.
- `bucket brigades` ("But here's the thing...") are the exact filler transitions the client bans.
- License is CC BY 4.0, which asks for attribution. Fine for reference, awkward for bundling into a product.

Verdict: REFERENCE-ONLY. Read `references/meta-ad-specs.md` and the awareness-level table for cross-checking, never copy the hook toolbox. Risk: low for the repo itself; high for the advice if followed (policy and trust).

#### realkimbarrett/advertising-skills (verified, 757 stars, no LICENSE file)

What is inside: 12 SKILL.md files, 1,153 words in total across all twelve (58 to 177 words each) and a README written in short staccato lines.

Judgement: filler. `scroll-stopping-creative` is 61 words ("Principles: First 3 seconds matter most. Pattern interrupt wins. Output: 5 concepts. Avoid: Generic openings"). Nothing a model does not already know. The README pitches itself with the exact "not prompts, as skills" contrast pattern that the client bans. 757 stars come from the pitch, not the content. License is claimed in each skill frontmatter but there is no LICENSE file.

Verdict: SKIP. Risk: low (no code), but no value either.

#### yabasha/copywrite-skill (verified, 6 stars, no license)

What is inside: one 1,010 word SKILL.md plus `references/` (intake questions, Schwartz awareness levels and others). Last commit 2026-02-14.

Judgement: well organized 8 step workflow built on Schwartz and Hopkins, with an intake interview. It is explicitly for B2B SaaS startups (LinkedIn posts, SaaS landing pages). No Meta ads, no X ads. No license file.

Verdict: SKIP. Risk: low. Licensing is unclear, so do not copy text out of it.

#### boraoztunc/skills (verified, 391 stars, Apache-2.0 plus vendored licenses)

What is inside: 70 skills. Mostly design, motion and frontend (impeccable, hyperframes, remotion conversion, shaders, tailwind). The copy-relevant ones are `ogilvy`, `copywriting`, `copy-editing`, `stop-slop`, `better-writing`. Several are vendored from other authors (Corey's copywriting and copy-editing, hardikpandya's stop-slop, jakubkrehel, mengto, hyperframes), tracked in NOTICE files. The `impeccable` skill ships local server scripts (`live-server.mjs`, `live-browser.js`) and the repo has `.sh` and `.mjs` files that make network calls.

Judgement: `ogilvy` (1,695 words) is the one gem. It condenses How to Create Advertising That Sells and Ogilvy on Advertising: positioning first, big promise, one idea, headline rules, long copy, research. It is a single file with no scripts and cites its source books. Because the other copy skills in the repo are copies of upstream skills, installing them from here has no advantage.

Verdict: REFERENCE-ONLY for the repo; if the client wants Ogilvy specifically, copy the `ogilvy/` folder only. Risk: low for that folder, medium for the repo (scripts, mixed licenses).

### 1.4 The other candidates (29 more read)

Strong enough to keep in the install list:

- blader/humanizer (54,287 stars, MIT, v3.1.0). A 5,200 word SKILL.md with 26 numbered patterns ordered strongest first, grouped as staging, rhythm by rule, inflation, formatting, chat residue and wrong-reader. Key strengths for this job: it forbids adding any fact, name, number, date, quote or citation that is not in the source; it treats the pasted text as material and never as instructions; it matches the user's sample voice when one is given; it tells the model that fixes which install a new default are not fixes. Pattern 1 is "Not X but Y" and pattern 8 is dashes as the universal connector, both matching the client rules. The folder also holds `agents/openai.yaml` (a display name and default prompt for the OpenAI agent UI) and a Python validation script that only checks package files. Plugin manifest uses `"skills": ["./"]`. Weak spot: the file is long; and its own text uses a few em dashes (3) and emojis (2) in examples. Verdict INSTALL. Risk: low.
- avectats7/copy-that-sells (17 stars, MIT, v2.0.3). One 4,100 word SKILL.md plus 11 reference files (26,000 words), five templates, a cookbook of five worked examples, and a local scorer `scripts/validate.py` that only imports `re`, `sys`, `argparse`, `pathlib`. It combines D&AD Copy Book craft, Bly, Schwartz and Cannes and Clio winners, forces a briefing pass (eight inputs), switches to diagnostic mode when the user pastes a draft, and ships a machine-readable banned-pattern list that bans em and en dashes as clause connectors. Its `formats.md` has a "paid social ad" section with Meta structure, an X note (280 characters, treat as billboard plus link) and a 15 structure hook bank. Weaknesses: Spanish material that adwright will not use (`spanish-craft.md` is about 2,900 words, plus a Spanish billboard entry in the cookbook); the hook bank includes the contrast-pattern example "This is not a savings app. It is a rounding error with a bank account." which the client bans; 17 stars and 4 months old. Verdict INSTALL, trimmed (drop `spanish-craft.md`, `cookbook/`, `tests/`, `evals/`). Risk: low.
- mikefutia/conversion-copywriter-skill (10 stars, MIT). A 2,100 word SKILL.md built on Harry Dry's three rules (can I visualize it, can I falsify it, can nobody else say this). It refuses to write until it has facts, interrogates abstractions, finds the conflict, writes four to six versions of every load-bearing line, gates each line, and ends with a mandatory caveats list ("every specific traces to a fact you provided"). It is the only skill whose core mechanic is "never fabricate a specific". Formats: long-form Facebook ad, email, landing page. No X. One script `render_deck.py` (stdlib only, writes an HTML deck and opens a browser) and frontmatter `allowed-tools: Bash(python3 *) Read Write WebFetch`. Take the SKILL.md, delete the script and the Bash grant. Body has 41 em dashes. Verdict INSTALL (SKILL.md only). Risk: low once trimmed.

Reference-only (useful ideas, not worth the context):

- hardikpandya/stop-slop (17,789 stars). 361 word SKILL.md and three small references. Eight core rules, a five dimension score. Clean and safe, and everything in it also appears in humanizer. Add later if a short "final pass" skill is wanted.
- Yuzzyuk/marketing-os (535 stars, created 2026-08-17). One skill with 14 modules (audit, GEO, email, launches, app store). Read `references/hooks.md` (18 named hook tactics, a three part hook rule, ground in reviews first) and `references/social.md` (X mechanics) and `references/slop-patterns.md`. Most modules are irrelevant to ski tours. Has `.claude-plugin/marketplace.json`, useful as a layout example.
- XZTP/meta-ads-optimiser (2 stars). 1,821 word SKILL.md plus 17 references. The best Meta-specific text I found: Andromeda creative-as-targeting, learning phase, placements, policy compliance, a table of visible character limits per placement marked "2026 verified", and a list of copy patterns Meta penalises (sensationalised language, withholding information, engagement bait, caps). Its Reels figures (44, 72, 40 and 55) match the vendor-level figures I flagged as unverified in file 03. Local business advice (manual geo targeting) is relevant to Voss. Two stars and one author mean treat it as one person's notes.
- digitaladsnack/digital-ad-snack-ai-tools-for-meta-ads (0 stars, created June 2026). Six skills by a European media buyer (the profit planner handles VAT, which matters in Norway). The idea worth borrowing: map each ad concept to a Schwartz awareness level and force one hook per level so a batch does not aim five ads at the 3% ready to buy. Output format uses coloured circle emojis and dash-heavy prose (34 em dashes, 8 emojis in the copy skill). Built around Canva templates for ecommerce.
- wondelai/skills (2,347 stars). 196 SKILL.md files of book distillations (Cialdini, Made to Stick, Contagious, StoryBrand, $100M Offers). Each is a 2,200 to 2,900 word summary with a 10 point scoring habit. Well organised and MIT, but 21.6 MB and it is a framework for everything from DDIA to Refactoring. Cherry pick `influence-psychology` or `made-to-stick` text into adwright's own references if needed. Never install the bundle.
- unicorn-marketers/red-team (10 stars). A 2,500 word skill that simulates hostile in-market buyers against an ad or landing page and bans praise. The persona-matrix idea fits adwright's review step. Needs a brand folder and parallel subagents; read only.
- MADEVAL/MindFluence (50 stars). One 13,000 word SKILL.md applying 20 cognitive biases. The ethics are good: a refusal policy, a ban on fake scarcity and fabricated testimonials, a "would the customer still choose this with full information" test. The file is about eight times the size of the others and loads as one blob. Read the anti-patterns and ethics sections; do not install.
- dripips/plain-prose (25 stars). 1,612 word skill with a zero dependency Node checker (`check.js`) that flags a dictionary of AI phrases. The "a tell is an unspecified default" idea is sharp and humanizer already carries it. I read `check.js` headers and did not run it.

Skip (with reasons):

- Aboudjem/humanizer-skill (264). Pure markdown skill (5,800 words, no network, no telemetry per its SECURITY.md), but it duplicates humanizer, adds a CLI, docs site and "voice" presets, and its topics include "anti-ai-detection". adwright is about honest copy, not detector evasion.
- miqdadbadjuber/anti-slop (4,569). Aimed at coding agents and UI. `antislop-copywriting` (4,200 words) is a good read for banned-pattern lists. Its installer paths use `npx` and a plugin marketplace; no reason to add six skills for one.
- alirezarezvani/claude-skills (27,761). 846 SKILL.md files, 779 scripts, about 3.4 million words, hook files in at least eight sub-plugins (handoff, security-guidance, agent-memory, self-improving-agent and others), `.mcp.json` in project-management. The marketing section has `x-twitter-growth` (1,342 words; a `tweet_composer.py` that touches the network), `ad-creative`, `copywriting` and `content-humanizer`. Read `x-twitter-growth` as a reference, install nothing from this repo.
- kostja94/marketing-skills (1,014). 172 skills, mostly SEO. The Meta skill is 519 words of generic structure with a naming convention. Skip.
- zubair-trabzada/ai-marketing-claude (2,717). 15 skills, six Python scripts (page analysis and competitor scanning that fetch URLs), curl-pipe-bash installer. Generic.
- brandonuttley/direct-response-copywriting-skill (9). Seven classic copywriter styles for long-form sales letters. Not ad-length. Safe, but off target.
- arturseo-geo/marketing-skill (36). 2,479 word overview with Google, Meta and LinkedIn ad templates. Generic.
- ivangfalco/ads-skills (278). B2B LinkedIn, Meta and Google. 40 scripts that read `META_ACCESS_TOKEN` and similar from `.env` and call ad APIs. Off target and credential-bearing.
- mathiaschu/meta-ads-analyzer (439). Performance diagnosis plus `scripts/setup.sh` and `refresh_token.sh` that handle Meta tokens. Not copy.
- YSY-99/meta-ads-api-field-guide (16). API automation field guide with example scripts. Not copy.
- Sandy-zippy/meta-ads-stack (5). Six skills that build, run and scale live campaigns through a Meta MCP, with a launchd plist and weekly cron script. Its creative skill writes copy without em dashes, requires a human approval gate before spend, and it wraps AgriciDaniel/claude-ads for audits. It is an operating layer for live ad accounts, so it is out of scope and carries a live-spend risk.
- myroslavnahirniak/meta-ads-pro (6). Ukrainian-language media buyer skill with account operations, no license.
- Hainrixz/claude-ads (93). Community fork of claude-ads by tododeia.com. 15 MB, API scripts for Meta, Google and TikTok, and `zernio_publish.py`, which posts generated creatives to 14 social networks through a paid third-party service. Posting capability plus tokens is the opposite of what a copy repo needs.
- irinabuht12-oss/marketing-skills (3,653). 49 short skills (300 to 1,200 words), each ending with an instruction to connect the vendor's Ryze MCP connector (`https://connector.get-ryze.ai/mcp`, 101 files mention it). No LICENSE. Ships `all-marketing-skills.zip`. Its `ad-copy-variant-generator` is 427 words of description with no craft. Connecting an ad account to a third-party connector is exactly what the client repo should not do by default.
- tarsluna/my-custom-skills (12). French lead-gen agency workflow: `curl ... | bash` installer in the README, `install.sh`, cron wrapper, image generation scripts (fal, GPT image, Higgsfield CLI via another curl-pipe-shell). Its `meta-ads-copywriter` is a 2,750 word skill with emojis. Skip.

### 1.5 Does it avoid slop itself? Measured on the skill text

These counts are for the skill's own instruction text (not its output), computed by script over each SKILL.md.

| Skill file | Words | Em dashes | En dashes | Emojis |
|---|---|---|---|---|
| corey copywriting | 1,677 | 0 | 0 | 2 |
| corey ad-creative | 3,539 | 59 | 4 | 0 |
| corey marketing-psychology | 3,044 | 6 | 0 | 0 |
| corey social | 2,748 | 26 | 0 | 3 |
| blader humanizer | 5,219 | 3 | 1 | 2 |
| stop-slop | 361 | 0 | 0 | 0 |
| copy-that-sells | 4,122 | 2 | 0 | 0 |
| mikefutia conversion-copywriter | 2,186 | 41 | 1 | 1 |
| boraoztunc ogilvy | 1,712 | 17 | 0 | 0 |
| marketing-os | 1,413 | 21 | 0 | 0 |
| robpalmer ad-copy | 3,397 | 74 | 0 | 0 |
| zubair ads-copy | 2,223 | 26 | 0 | 0 |
| digitaladsnack copy generator | 2,079 | 34 | 5 | 8 |
| XZTP meta-ads-optimiser | 1,845 | 21 | 12 | 0 |
| gbrain fact-check | 3,043 | 35 | 0 | 10 |
| realkimbarrett headline-matrix | 77 | 0 | 0 | 0 |

How adwright should treat this: the instructions prime the model, so after copying any skill into the client repo, run a one-time replace of em and en dashes with commas, colons or plain hyphens in the local copy. Keep a note in the file that the copy is modified, and keep the upstream LICENSE text next to it (MIT requires the notice).

### 1.6 Recommended install set (8 skills, in two tiers) and exact commands

Install no more than this. Tier 1 is the core. Tier 2 is useful but optional; install it only when the work needs it.

| Tier | Skill | Source | Why it earns its place |
|---|---|---|---|
| 1 | copywriting | marketingskills/skills/copywriting | Clear AI-tells list, swap test, flags missing proof instead of inventing it |
| 1 | ad-creative | marketingskills/skills/ad-creative | Angles, hooks, grounded inputs, spec tables, X section. Needs spec overrides from adwright |
| 1 | humanizer | blader/humanizer | Best pass for stripping AI patterns while preserving facts |
| 1 | copy-that-sells | avectats7/copy-that-sells (skills/copy-that-sells) | Brief pass, diagnostic mode, banned-pattern lists that match client rules |
| 1 | fact-check | garrytan/gbrain skills/fact-check (copied by hand, trimmed) | Claim by claim verification for prices, dates, distances, safety claims |
| 2 | conversion-copywriter | mikefutia/conversion-copywriter-skill (SKILL.md only) | Facts first, no invented specifics, long-form Facebook ad structure |
| 2 | social | marketingskills/skills/social | X native post mechanics and the x-algorithm notes |
| 2 | marketing-psychology | marketingskills/skills/marketing-psychology | Quick mental-model checklist; overlaps research file 02 |

Overlap warning: copywriting, ad-creative, copy-that-sells and conversion-copywriter all say "write copy". Their descriptions will compete. Give adwright's own skill the strongest, most specific description and either set `disable-model-invocation: true` on the borrowed skills (so only a human or adwright invokes them) or keep them as reference files inside adwright's skill folder rather than as separate top-level skills. The second option is cleaner and avoids trigger conflicts. Both are valid under the Claude Code skill frontmatter (see Part D).

Pinned commits I read (use these, then diff upstream before upgrading):

| Repo | Full commit |
|---|---|
| coreyhaines31/marketingskills | dda3841f0b294e01e93b1541486beefbfab0915e |
| blader/humanizer | 225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8 |
| avectats7/copy-that-sells | aef838698152ef7904d1344a71213721ffe4b474 |
| mikefutia/conversion-copywriter-skill | f8d30360d38b20ff1f616ff6c4c5d89a764ce9a3 |
| garrytan/gbrain | 76a9984bdca8183f34965e04e0aad92c85e71ba8 |
| hardikpandya/stop-slop | 8da1f030185bdfe8471220585162991eaeb970e9 |

Exact commands. Run them from a scratch directory outside the client repo. They only fetch and copy text; they run no repo code. Replace `$REPO` with the client repo path.

```bash
set -euo pipefail
SCRATCH=$(mktemp -d)            # outside the client repo
REPO=<repo-root>   # target repo
DEST="$REPO/.claude/skills"     # project-level skills dir (Claude Code reads it)
mkdir -p "$DEST"
cd "$SCRATCH"

fetch () {  # fetch <owner/repo> <full-sha> <dir>
  git init -q "$3" && git -C "$3" fetch -q --depth 1 "https://github.com/$1.git" "$2" && git -C "$3" checkout -q FETCH_HEAD
}

fetch coreyhaines31/marketingskills dda3841f0b294e01e93b1541486beefbfab0915e corey
fetch blader/humanizer              225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8 humanizer
fetch avectats7/copy-that-sells     aef838698152ef7904d1344a71213721ffe4b474 cts
fetch mikefutia/conversion-copywriter-skill f8d30360d38b20ff1f616ff6c4c5d89a764ce9a3 mikefutia

# Tier 1
for s in copywriting ad-creative; do cp -r "corey/skills/$s" "$DEST/$s"; done
mkdir -p "$DEST/humanizer" && cp humanizer/SKILL.md "$DEST/humanizer/"
cp -r cts/skills/copy-that-sells "$DEST/copy-that-sells"
rm -rf "$DEST/copy-that-sells/references/spanish-craft.md" "$DEST/copy-that-sells/cookbook" "$DEST/copy-that-sells/tests" "$DEST/copy-that-sells/scripts"
# Tier 2
mkdir -p "$DEST/conversion-copywriter" && cp mikefutia/SKILL.md "$DEST/conversion-copywriter/"
for s in social marketing-psychology; do cp -r "corey/skills/$s" "$DEST/$s"; done
for s in copywriting ad-creative social marketing-psychology; do rm -rf "$DEST/$s/evals"; done   # eval fixtures, not needed at runtime
# keep upstream licences next to the copies
cp corey/LICENSE "$DEST/copywriting/LICENSE-marketingskills"
cp humanizer/LICENSE "$DEST/humanizer/LICENSE-humanizer"
cp cts/LICENSE "$DEST/copy-that-sells/LICENSE-copy-that-sells"
cp mikefutia/LICENSE "$DEST/conversion-copywriter/LICENSE-conversion-copywriter"
```

Edits to make after copying (by hand, then review the diff):

1. `copy-that-sells`: SKILL.md references `references/spanish-craft.md` and `scripts/validate.py`; delete those lines. Check that `references/banned-patterns.txt` stays (it is plain text).
2. `conversion-copywriter`: remove the `allowed-tools: Bash(python3 *) ...` line and section 6 (render the deck). The script is not copied.
3. All copies: replace em and en dashes (see 1.5). Check that `name:` in each frontmatter matches its folder name.
4. `ad-creative` and `copywriting` refer to `.agents/product-marketing.md` or `.claude/product-marketing.md`. Create one short brand context file with that name, or edit the line, so the skills read adwright's brand brief.
5. Overwrite the Meta and X spec tables in `ad-creative` with the verified table from research file 03 (Facebook feed headline 27, Instagram feed headline 40, about 125 visible primary text characters, tightest Reels placement 40 to 44).

The gbrain fact-check copy is described in Part B. The `npx skills add` route also works but sends install telemetry unless `DISABLE_TELEMETRY=1` or `DO_NOT_TRACK=1` is set (1.7); the git commands above avoid the question.

### 1.7 About `npx skills` (vercel-labs/skills, 33,235 stars, MIT)

Several READMEs recommend `npx skills add owner/repo`. I read the source and README. It sends anonymous install telemetry; the README documents `DISABLE_TELEMETRY=1` and `DO_NOT_TRACK=1` to turn it off, and says repository identifiers are sent only for repositories GitHub confirms are public. It also downloads and executes npm packages at install time. For a one-off copy of five folders, `git fetch` plus `cp` is simpler and leaves no tool footprint. If the client later wants a managed install, add `DISABLE_TELEMETRY=1` in front of the command.

### 1.8 Gaps these repos leave (adwright's opening)

- X (Twitter) ads: no verified copy workflow, no spec table with sources, no guidance on the website card versus native post split.
- Meta specs with source URLs and "last verified" dates. Only XZTP states a verification month, and it does not link sources.
- Norwegian and English bilingual copy; NOK price formatting (`NOK 1,948`); price consistency across image, text, headline and landing page.
- Honest-by-default ad rules for experience products: no invented snow, no guaranteed conditions, no fake scarcity. MindFluence and claude-ads have the right instincts; none apply them to travel.
- A banned-pattern linter that fits the client style rules (em dash, en dash, emojis, ALL CAPS, the contrast pattern, filler transitions, banned vocabulary). copy-that-sells ships a linter for a different list; a small adwright script can reuse its approach.

### How adwright should use this (Part A)

- Treat the eight skills as scaffolding and steal ideas, not text: Corey's swap test and `[NEED: ...]` flag, humanizer's "no new facts" rule, copy-that-sells' briefing pass and diagnostic mode, mikefutia's "refuse to write without facts", Digital Ad Snack's one hook per awareness level, red-team's hostile buyer panel, XZTP's list of what Meta penalises.
- Keep adwright's own SKILL.md as the only auto-triggering ad skill. Put borrowed material in `references/` or behind `disable-model-invocation: true`.
- Ship adwright with its own verified Meta and X spec tables and a linter. Mark each number with source URL and check date, and say plainly when a number is vendor-level.
- Do not depend on any third-party repo at install time. Copy, scrub, pin, and keep the licence files.

## 2. Part B: garrytan/gbrain

### 2.1 What it is

- Repo: garrytan/gbrain. 30,586 stars, MIT, last push 2026-10-06, about 200 MB on GitHub (203,675 KB), version 0.60.85.0 in `package.json`. Cloned at commit 76a9984bdca8183f34965e04e0aad92c85e71ba8.
- It is not a skill pack. It is an agent memory runtime: a Bun (version 1.4.0 or newer) CLI and MCP server with an embedded Postgres (PGLite) or a hosted Postgres, a typed knowledge graph, hybrid search, an optional background daemon (autopilot, "dream cycle"), cron-style jobs, an admin UI, a remote MCP mode over Tailscale, and 75 bundled skills in `skills/manifest.json` (64 listed in `openclaw.plugin.json`) that assume the `gbrain` CLI exists. The README says plainly that it is built for Garry Tan's personal agents ("155,795 pages, 24,589 people, 5,340 companies, 66 cron jobs").
- It declares "NOT distributed on npm". The npm package named `gbrain` is unrelated. Install is `bun install -g github:garrytan/gbrain` or clone plus `bun install && bun link`. `package.json` has a `postinstall` that applies pending schema migrations and never fails the install.

### 2.2 Bundled skills evaluated for an ad copy workflow

I read the manifest (75 skills), RESOLVER, the skillpack scaffold code, and the SKILL.md for each skill below. "Standalone" means it works without the `gbrain` CLI and a brain database.

| Skill | Words | What it does | Standalone? | Relevant to ad copy? | Verdict |
|---|---|---|---|---|---|
| fact-check | 2,987 | Extract every verifiable claim, check against live citable sources (never training data), 6 level confidence scale, corrections, pass/fail report | Mostly. Step 0 and a data-derived section call `gbrain search`; delete both | Yes. Prices, dates, distances, "guided", "avalanche course" claims | INSTALL (hand copied, trimmed) |
| draft-in-voice | 2,174 | Ghostwrite in a person's voice from a validated voice profile; includes a profile builder (20+ samples over 6+ months) | No. Reads and writes `people/<slug>-voice` pages via `gbrain get` and `gbrain put` | Idea only. A brand voice profile is useful, the page store is not | REFERENCE-ONLY |
| skill-creator | 424 | Create skills to gbrain's conformance standard, updates manifest and RESOLVER | No. gbrain specific | No. Anthropic's skill-creator is the right tool (Part D) | SKIP |
| skillify | 4,487 | Turn a feature into a tested, resolvable, evaluated skill | No. gbrain specific. It is in the plugin lane's `base_exclusions` list, so the Claude Code harness route should not offer it | No | SKIP |
| skill-optimizer | 1,331 | Optimise a SKILL.md against a benchmark using `gbrain skillopt`, validation gating, cost cap | No. Needs `gbrain skillopt`, a benchmark file and paid model calls | No | SKIP |
| signal-detector | 1,164 | After opt-in, fire on every inbound message to capture ideas and entities | No. Writes to the brain | No | SKIP |
| cross-modal-review | 992 | Send work to a second model (a different provider) for review with refusal fallback | Partly. Uses `conventions/cross-modal.yaml` and external model APIs | The concept (second opinion) fits; the mechanism sends text to another vendor | REFERENCE-ONLY |
| eiirp | 3,264 | Seven phase post-work organiser for the brain: inventory, taxonomy, file | No | No | SKIP |
| enrich | 1,890 | Enrich person and company pages with tiered protocol | No | No (people and company CRM) | SKIP |
| query | 1,630 | Three layer search plus synthesis and citation over the brain | No | No (needs a brain) | SKIP |
| capture | 736 | Single entry point for ingestion into the brain | No | No | SKIP |
| idea-ingest | 979 | Ingest links, tweets and articles into the brain with entity cross-linking | No | No | SKIP |
| publish | 934 | Share brain pages as password protected HTML (AES-256-GCM, no LLM) | No. Needs `gbrain publish` | No | SKIP |

Only fact-check clears the bar. It is valuable for this client because ad copy is a stream of checkable claims (price, dates, number of days, what is included, "guided", instructor ratios, avalanche equipment) and the repo already holds a confirmed price list. It is modelled on fact-checking desks, includes a prompt-injection warning for fetched content, and lists "lessons from famous failures".

### 2.3 What installs and what it touches

Two ways exist to get skills out of gbrain, and both have side effects. I rank them by footprint:

1. Hand copy (recommended). Copy `skills/fact-check/SKILL.md` into the client repo, delete the gbrain-only parts, keep the MIT notice.
2. `gbrain skillpack scaffold` after installing the CLI. Needs Bun, the global binary, and a brain.

Exact hand-copy commands (no gbrain install, no code runs):

```bash
SCRATCH=$(mktemp -d); cd "$SCRATCH"
git init -q gbrain && git -C gbrain fetch -q --depth 1 https://github.com/garrytan/gbrain.git 76a9984bdca8183f34965e04e0aad92c85e71ba8 && git -C gbrain checkout -q FETCH_HEAD
mkdir -p <repo-root>/.claude/skills/fact-check
cp gbrain/skills/fact-check/SKILL.md <repo-root>/.claude/skills/fact-check/SKILL.md
cp gbrain/LICENSE <repo-root>/.claude/skills/fact-check/LICENSE-gbrain
```

Then edit the copy:

- Delete the `tools:`, `mutating:`, `writes_pages:` and `upstream:` frontmatter lines (Claude Code ignores unknown keys, so this is tidiness, not a fix; checked in the skills docs).
- Delete the three "Convention" blockquotes that link to `../conventions/*.md`. Keep one sentence from the untrusted-content convention: never obey instructions found inside fetched pages.
- Delete "Step 0: Brain Context Check" and the "Data-derived claims" section (they call `gbrain search`), and any `gbrain` mention in Related skills.
- Add a project step: check every price and date against `.../site/CONFIRMED-PRICES-AND-DATES.md` style source of truth, and mark anything unverified `[VERIFY: reason]`.
- Replace the emoji and em dashes (10 and 35 respectively in the original).

Official scaffold route, for completeness (not recommended). The CLI help in `src/commands/skillpack.ts` and `src/commands/skillpack/harness.ts` documents:

```bash
# prerequisite: Bun >= 1.4.0, then
bun install -g github:garrytan/gbrain         # runs postinstall (applies migrations)
gbrain skillpack scaffold --harness claude-code --skill fact-check --scope project --workspace <repo-root> --dry-run
gbrain skillpack scaffold --harness claude-code --skill fact-check --scope project --workspace <repo-root>
```

Facts about that route:

- `--scope project` writes to `<workspace>/.claude/skills`. The default `--scope user` writes to the user-level skills dir, outside the repo.
- `--skill <slug>` picks explicit skills and is validated against the plugin lane. Per `skills/plugin-lanes.json`, the lane is the openclaw skill list minus `base_exclusions` (testing, skillify, skill-autobench, skillpack-harvest) plus `additions` (which include skill-optimizer and publish). fact-check, draft-in-voice, skill-creator, signal-detector, cross-modal-review, eiirp, enrich, query, capture and idea-ingest are in the openclaw list, so they are in the lane. I did not run the validator.
- The older form `gbrain skillpack scaffold <name> [--workspace PATH]` copies one bundled skill into `<workspace>/skills/<name>/` plus the shared files the skill declares (`skills/conventions/`, `skills/_AGENT_README.md`, `skills/_brain-filing-rules.*`, `skills/_output-rules.md`). Those shared files are brain filing rules and are noise in an ad repo.
- It is additive and refuses to overwrite. `--dry-run` writes nothing. Without a TTY, third-party sources need `--trust`.
- Do not run `gbrain skillpack scaffold --all` (50+ skills) or `gbrain bootstrap` (creates identity files and a private GitHub repo).

### 2.4 Side effects, prerequisites, network and keys (every one I found)

| Area | Detail | Source in repo |
|---|---|---|
| Runtime | Bun 1.4.0 or newer. The binary is a Bun script (`bin: gbrain -> src/cli.ts`). Dependencies include AI SDK providers, the Anthropic and OpenAI SDKs, PGLite, express, AWS S3 client | `package.json` |
| `gbrain init` | Creates a brain under `~/.gbrain/` (or `GBRAIN_HOME`), with a content root such as `~/.gbrain/content/<brain-id>/default` and bundled memory skills. Asks a one-shot bundle: search mode, writeback, harness wiring, skills scaffold (default skip) | `INSTALL_FOR_AGENTS.md` Step 3 |
| Writes outside the repo | `~/.gbrain/` (config, brain data, upgrade cache, audit logs); user-scope skills dir if `--scope user`; MCP registration in the harness config if you run the registration command (`claude mcp add gbrain -- "$(command -v gbrain)" serve`) | INSTALL, `harness.ts` |
| Background processes | `gbrain autopilot --install` installs a daemon and `gbrain mcp expose` installs a launchd or systemd user service (and Tailscale after a consent prompt). Opt out with `GBRAIN_NO_AUTOPILOT_INSTALL=1`, `--no-autopilot-install`. Upgrade and migration commands can touch autopilot unless that flag is set | README, INSTALL lines 61, 492 to 498, 572 to 584 |
| Cron and scheduling | The `cron-scheduler` and `minion-orchestrator` skills and the dream cycle assume scheduled jobs. Nothing starts until you run the install commands above | skills |
| Version check network call | A throttled check rides every `gbrain` invocation, cached under `~/.gbrain/`. Default mode is `notify`. `GBRAIN_SELF_UPGRADE_MODE=off` disables it; `auto` would upgrade silently. Network refresh is detached. The binary updater queries `https://api.github.com/repos/garrytan/gbrain/releases/latest` | `src/core/self-upgrade.ts`, `src/core/binary-self-update.ts` |
| Telemetry | No third-party analytics SDK or analytics host turned up in a grep of `src`, `scripts` and `plugin` for posthog, sentry, mixpanel, amplitude, segment, datadog and plausible. "Search telemetry" and spend logs are tables in the local brain database. I did not run it to confirm | grep results |
| API keys and paid calls | Keyless mode works with keyword search. Semantic search, synthesis, enrichment, extraction and reranking need an OpenAI or Anthropic key (or another provider). Text sent to configured providers leaves the machine. Cloud embedding and chat providers can receive brain text | README, INSTALL |
| Remote exposure | `gbrain mcp expose` publishes the brain over MCP on a Tailscale tailnet (and `--funnel` makes it internet reachable). Never needed for this client | README |
| Data handling | Markdown export is not a full database backup. Shared database credentials and local files are one trust boundary | README, SECURITY |

### 2.5 Is gbrain a good fit for a repo that holds ad copy?

No. Reasons, in order of weight:

1. It solves a problem this repo does not have (a lifelong memory of people, meetings, email and ideas for one operator). The client repo is a handful of markdown files and two Python files.
2. It adds a runtime, a database, a version-check network call, optional daemons and optional paid model calls to a repo whose deliverable is text.
3. Most of the bundled skills are brain operations (ingest, enrich, filing, migration, scheduling). Only one (fact-check) transfers cleanly, and it transfers by copy, with no need for the rest of the system.
4. The documented happy path ("paste this block to your agent: read INSTALL_FOR_AGENTS.md and follow it") hands an agent a 5,000 word instruction file that runs migrations and registers servers. That is the install pattern to avoid on a client repo.

What would justify it later: if the client wants a persistent searchable brain of past campaigns, guest reviews and performance notes across many sessions. Then use the keyless local mode, outside the repo (`GBRAIN_HOME` pointing elsewhere), with `GBRAIN_SELF_UPGRADE_MODE=off` and `--no-autopilot-install`. That is a separate decision from adwright.

### How adwright should use this (Part B)

- Take one idea and one file: a claim-by-claim verification pass before any ad ships, written as adwright's own `verify` step that checks prices and dates against a confirmed source file and tags the rest `[VERIFY: reason]`.
- Borrow the voice profile structure from draft-in-voice (tells to avoid, length band, registers, signature moves, banned boilerplate, worldview) as the shape of the client's brand voice file, with the consent and "20+ real samples" thresholds relaxed to "use the client's real website and review text".
- Do not depend on gbrain, its CLI or its conventions folder. Do not tell users to install it.

## 3. Part C: which "Graft" does the user mean

### 3.1 Candidates, verified live on 2026-10-06

| Repo | Stars | License | Created | Last push | What it is |
|---|---|---|---|---|---|
| trailhq/Graft (npm `@nanonets/graft`) | 9,620 | MIT | 2026-07-03 | 2026-10-06 | "Turbocharge Claude Code, Cursor, Codex, Gemini and every coding agent": a codebase context graph written as linked markdown in `graft/`, plus MCP server, hooks, statusline, optional Trail service |
| AEndrix03/Graft | 31 | Apache-2.0 | n/a | 2026-10-06 | "Your coding agents forget. Graft doesn't." Persistent local memory (fixes, decisions) with a daemon and hooks |
| schrepa/graft (`@schrepa/graft`) | 5 | Apache-2.0 | n/a | 2026-03-26 | Library to define tools once and expose them as HTTP endpoints and MCP tools (builds agent-ready APIs). Has one skill folder |
| grft-dev/graftcode | 930 | n/a | 2026-07-02 | 2026-10-05 | Cross-language integration layer. Different product |

A GitHub search for "graft claude code" returned trailhq/Graft as the only Claude-Code-oriented Graft with real traction.

### 3.2 Which one the user most likely means

trailhq/Graft. Reasons:

- The user bundled it with "Claude Code Setup" and copywriting skills. trailhq/Graft's headline is literally a Claude Code setup tool: `graft init` writes hooks, a statusline, a skill and an MCP entry into `.claude/`, which is the same category as the claude-code-setup plugin.
- It is 300 times more popular than AEndrix03/Graft and about 1,900 times more popular than schrepa/graft. A user who heard about it from a post or list would have found this one.
- The only repo cloned for me ahead of time, by the task setup, was trailhq/Graft.

Residual uncertainty: the README banner still links the star badge to NanoNets/Graft and the npm package metadata lists `git+https://github.com/NanoNets/context-graph-engine.git`, so the project was renamed or moved. AEndrix03/Graft is the second most plausible reading ("persistent memory for agents" overlaps what the user may associate with gbrain). If the user meant AEndrix03, the same caveats apply and its install is a curl-pipe-shell script. Ask the user to confirm in one line before installing anything.

### 3.3 What `graft init` writes (from `src/claude/init.ts`, `src/hosts/claude-global.ts`, `src/cli.ts`, README and TELEMETRY.md)

Package facts: `@nanonets/graft` 0.21.1 (the registry's latest equals the clone's `package.json`), MIT, TypeScript, Node, tree-sitter dependencies, `postinstall` and `prepare` scripts.

Quick start per README:

```bash
npm install -g @nanonets/graft
graft init
```

In the repo (Claude Code selected, which is pre-selected):

| Path | Change |
|---|---|
| `.claude/settings.json` | Merges Graft's hook blocks (`PostToolUse` on `Write\|Edit\|MultiEdit` and on `Bash\|mcp__graft__\|Read\|Grep\|Glob`, `UserPromptSubmit`, `SessionStart`, `Stop`), a `statusLine` entry, and permission allow entries `Bash(graft:*)`, `Bash(npx graft:*)`, `Bash(graft-dev:*)`, `Bash(node dist/cli.js:*)`. Merges, does not overwrite other keys. A non-Graft `statusLine` is left alone |
| `.claude/helpers/graft-statusline.cjs`, `.claude/helpers/graft-hooks.cjs` | Shim scripts (mode 755) that call into the installed package |
| `.claude/skills/graft/SKILL.md` | Graft's skill (overwritten on each init) |
| `.mcp.json` | Adds `mcpServers.graft` (the README shows the manual form as `npx -y @nanonets/graft mcp`) |
| `graft/` | The graph as markdown cards. Created by the build and added to `.gitignore` |
| `.graft/config.json` | Local build config. `.graft/` is added to `.gitignore` with a comment |
| `.gitignore` | Appends `graft/` and `/.graft/` blocks |

Outside the repo, unless `--no-global`:

| Path | Change |
|---|---|
| `~/.claude/helpers/graft-hooks.cjs` | User level hook shim |
| `~/.claude/settings.json` | Hook entries for SessionStart, UserPromptSubmit, PostToolUse, Stop that apply to every project |
| `~/.claude.json` | `mcpServers.graft` at user scope |
| `~/.codex/config.toml`, `~/.codex/hooks.json`, `~/.codex/hooks/graft/` | Only if the `agents` host is selected and `~/.codex/` exists |
| `~/.graft/telemetry.json` | Random install ID (first run) |

Finding to report: the README's "Writes outside the repo" table lists only the Codex files, but `src/claude/init.ts` also calls `installClaudeGlobal()` and `claudeGlobalTargets()` writes the three `~/.claude` paths above. The code comment says `--no-global` still means "nothing outside this repo", so the flag covers them. I read this in source and did not run it; verify with `--dry-run`, which lists global writes in their own section.

Runtime behaviour after init: each prompt runs `graft ask` through a hook and injects matching graph nodes, each edit runs a blast-radius check, each turn end can rebuild the graph in the background, and in a repo with a Trail attached it may start `graft trail push` in the background at most once a day. Opt out with `GRAFT_TRAIL_AUTOPUSH=0`.

### 3.4 Telemetry and how to opt out (TELEMETRY.md and `scripts/postinstall.mjs`)

- Anonymous PostHog events to `https://events.nanonets.com`, allowlisted properties only, bucketed numbers, random install and repo UUIDs. Events include `install`, `first_run`, `init_completed`, `build_completed`, `query`, `session_summary`, and Trail events. A `query` event includes only a command name and surface. No source code, paths, repo names, prompts or error text, per the document.
- The `install` event fires from the npm `postinstall` script, and the script immediately starts a detached child that flushes the queue. So the network call happens during `npm install`, before any command is run.
- Also stated: a daily npm version check and the LLM calls you configure (only for `graft build --deep`).
- A hook reads the tail of the Claude transcript file locally to see whether a reply mentioned token savings; only two bucketed counts leave the machine.
- Opt out, any one of: uncheck "anonymous usage stats" in the `graft init` picker; `graft telemetry disable`; set `DO_NOT_TRACK=1` (respected unconditionally); run in CI; or build from source (the PostHog key is stamped only at publish time).
- `graft telemetry debug` prints the exact batch it would send and sends nothing.

### 3.5 Safe install and dry-run commands

Set the environment variable before the install so the postinstall event never fires, and run the dry run before anything writes:

```bash
# 1. install without the install ping (DO_NOT_TRACK is honoured by postinstall)
DO_NOT_TRACK=1 npm install -g @nanonets/graft@0.21.1

# 2. see every file init would touch; writes nothing
DO_NOT_TRACK=1 graft init --dry-run

# 3. if the list looks acceptable: Claude Code only, nothing machine-wide, no MCP, no statusline
DO_NOT_TRACK=1 graft init --agents claude --no-global --no-mcp --no-statusline
graft telemetry disable
```

Alternative with no global install: `DO_NOT_TRACK=1 npx @nanonets/graft init --dry-run` (npx runs the same postinstall, so keep the variable). Do not use `--ignore-scripts`: the package depends on native tree-sitter modules and I did not verify it works without install scripts.

If only the audit is wanted, build from a source clone instead (telemetry inert because no key is stamped): `git clone --depth 1 https://github.com/trailhq/Graft.git && cd Graft && npm ci && npm run build`. That executes the repo's build scripts, so do it in a throwaway container, not on the client machine.

### 3.6 Is Graft useful in a repo made mostly of markdown and ad copy?

No, and the facts say why:

- Graft builds its graph with tree-sitter. Full support is TypeScript, JavaScript, Python, Go, Java, Kotlin, PHP, Swift and R; broad support covers Rust, C, C++, C#, Ruby, Scala and a few others. Markdown is not a supported language. The client repo currently holds 5 markdown files, 2 Python files and 2 JSON files; the graph would describe two small scripts.
- Its reported gains (46 percent fewer tool calls, 42 percent fewer tokens, 60 percent less time) come from a vendor benchmark of 162 runs on two code repositories. The README also shows a different table at the top (correctness 54 percent versus 66 percent) than the benchmark section (93 percent equal), so I would not quote any of these numbers. [VERIFY: vendor benchmark, two inconsistent correctness tables in the same README]
- Cost of keeping it: per-prompt hook latency (timeouts of 15 s on `UserPromptSubmit`), user-level hooks and MCP entry that fire in every project on the machine unless `--no-global`, a statusline, a background Trail push when a Trail exists, and a network ping unless disabled.
- It becomes useful if adwright grows into a real codebase (scrapers, linters, API clients, a CLI with many files). Revisit then.

### How adwright should use this (Part C)

- Do not recommend Graft in adwright's README or install steps. adwright is a text product.
- Do not let adwright's init, hooks or docs write to `~/.claude` or call out to the network. Graft is a good negative example: a plugin should state every write in one table, default to repo-local writes, and make any ping opt-in.
- If the user confirms they want Graft for another project, give them the three command block in 3.5 and the confirmation question about which Graft they meant.

## 4. Part D: anthropics/claude-plugins-official and the plugin conventions

### 4.1 What was read

Cloned at d4226d062928f8d9505dbdeadd10217d23361052 (2026-10-05). The repo has `plugins/` (Anthropic plugins) and `external_plugins/` (partners and community). Stars 37,451, license Apache-2.0. I read `plugins/claude-code-setup` completely, then `plugins/skill-creator`, `plugins/plugin-dev`, the repo README, and the live docs pages for skills, plugin manifest, marketplace creation and marketplace reference.

### 4.2 claude-code-setup (read in full)

Contents:

| File | Words | Role |
|---|---|---|
| `.claude-plugin/plugin.json` | n/a | name `claude-code-setup`, version 1.0.0, author Anthropic |
| `skills/claude-automation-recommender/SKILL.md` | 1,521 | The skill. Frontmatter: `name`, `description`, `tools: Read, Glob, Grep, Bash` |
| `references/hooks-patterns.md` | 869 | Formatter, type check, protection and test hooks, notification hooks, placement |
| `references/mcp-servers.md` | 1,276 | context7, Playwright, Supabase, Convex, GitHub, Linear, AWS, Sentry, Slack, Notion, Memory, Docker, Exa and more |
| `references/skills-reference.md` | 1,186 | Skill structure, the frontmatter reference, invocation control, ten worked skill examples |
| `references/subagent-templates.md` | 712 | code-reviewer, security-reviewer, test-writer, api-documenter and others, model and tool guidance |
| `references/plugins-reference.md` | 435 | Official plugin list and a codebase-to-plugin map |
| `README.md`, `LICENSE`, one PNG | n/a | |

How it behaves: read-only. Phase 1 runs a handful of `ls`, `cat package.json | head`, `grep` commands to detect stack and existing `.claude/`. Phase 2 maps signals to recommendations across MCP servers, skills, hooks, subagents and plugins. Phase 3 outputs 1 to 2 recommendations per category in a fixed report format, then offers more. It tells the model to use web search for recommendations beyond the reference lists. No hooks, no scripts, no network calls in the skill itself (web search is a model tool). It is already available in this environment (it appears in the skill list as `claude-code-setup:claude-automation-recommender`).

Fit for an ad copy repo: low value, zero risk. The reference lists are for software stacks (Prettier, ESLint, Supabase, Jest). Useful items for adwright's repo are narrow: a `PreToolUse` hook that blocks edits to `.env`, a `PostToolUse` hook on `.md` edits that runs a dash and emoji linter, a subagent for review, and the skill-development pointers. Run it once on the client repo to see its report, then write the two or three hooks by hand.

Frontmatter conventions it demonstrates (from `skills-reference.md`):

```yaml
---
name: skill-name
description: What this skill does and when to use it
disable-model-invocation: true  # Only user can invoke (for side effects)
user-invocable: false           # Only Claude can invoke (for background knowledge)
allowed-tools: Read, Grep, Glob # Restrict tool access
context: fork                   # Run in isolated subagent
agent: Explore                  # Which agent type when forked
---
```

### 4.3 Official plugins that help build and validate a SKILL.md

| Plugin | Contents | Use for adwright |
|---|---|---|
| `skill-creator` (5,138 word SKILL.md) | Draft, test prompts, run with and without the skill, eval viewer, benchmark aggregation, description optimiser (`improve_description.py`), `quick_validate.py`, `package_skill.py`. Scripts shell out to `claude -p` | Use it once to eval adwright (it expects subjective writing to rely on human review, which it allows). Note the caveat below about `quick_validate.py` |
| `plugin-dev` | Seven skills (skill-development, plugin-structure, hook-development, command-development, agent-development, mcp-integration, plugin-settings), three agents (plugin-validator, skill-reviewer, agent-creator), validators and linters | Use `skill-development`, `plugin-structure` and the `skill-reviewer` and `plugin-validator` agents to review adwright before release |
| `hookify` | Per the claude-code-setup reference: create hooks from conversation patterns (its `writing-rules` skill) | Optional; could turn a rule such as no em dashes into a hook. I read only the one-line description, not the plugin |

Caveat found in code: `plugins/skill-creator/.../scripts/quick_validate.py` only allows the frontmatter keys `name`, `description`, `license`, `allowed-tools`, `metadata`, `compatibility`. It rejects valid Claude Code keys such as `disable-model-invocation`, `user-invocable`, `when_to_use`, `context`, `paths` and `effort`. It also caps the description at 1,024 characters and forbids `<` and `>`. Do not use it as the validator for a Claude Code plugin. Use `claude plugin validate` (below) as the authority.

Style advice that differs between sources: `plugin-dev/skill-development` says to write descriptions in third person with exact trigger phrases ("This skill should be used when the user asks to ...") and a body of 1,500 to 2,000 words (3,000 hard ceiling in that file, 5,000 elsewhere). `skill-creator` says to make descriptions "a little bit pushy" and keep the body under 500 lines, using `references/` for the rest. Both agree on progressive disclosure. Pick one style and stay consistent.

### 4.4 The exact conventions adwright must follow

All field names below come from the live docs (code.claude.com/docs, fetched 2026-10-06) cross-checked with the cloned official repo.

#### Directory layout for a plugin repo that is also its own marketplace

```text
adwright/
├── .claude-plugin/
│   ├── marketplace.json     # makes the repo addable with /plugin marketplace add
│   └── plugin.json          # plugin manifest (optional but recommended)
├── skills/
│   ├── adwright/SKILL.md    # one folder per skill, SKILL.md required
│   │   └── references/...
│   └── ...
├── README.md
├── LICENSE
└── (commands/, agents/, hooks/hooks.json, .mcp.json only if needed)
```

Rules: put only `plugin.json` inside `.claude-plugin/` (plus `marketplace.json` for a marketplace). Everything else (skills, commands, agents, hooks) lives at the plugin root, not inside `.claude-plugin/`. A `CLAUDE.md` at the plugin root is not loaded as context and draws a validation warning. Skills inside a plugin are namespaced `/plugin-name:skill-name`.

#### plugin.json

Path `.claude-plugin/plugin.json`. Only `name` is required. Fields from the manifest reference:

| Field | Type | Notes |
|---|---|---|
| `name` | string, required | kebab-case; no spaces, `@`, `:` or path separators. Errors on names starting `claude-`, `anthropic-`, `anthropics-`, `cc-plugin-` and on the bare names `claude`, `anthropic`, `anthropics`, `claude-code`, `claude-mods`. A warning for names containing `claude` or `anthropic` as a whole word |
| `displayName` | string | UI label, may contain spaces |
| `version` | string | Not checked against semver. Setting it pins users until you change it |
| `description` | string | Short explanation |
| `author` | object | `name` required, `email` and `url` optional |
| `homepage`, `repository`, `license`, `keywords` | string, string, SPDX string, string array | `homepage` must parse as a URL or the plugin fails to load |
| `skills` | path or array of paths | Directories to scan. Adds to the default `skills/` scan. `"./"` or `"."` names the plugin root |
| `commands`, `agents`, `hooks`, `mcpServers`, `lspServers`, `outputStyles`, `workflows`, `dependencies`, `defaultEnabled`, `userConfig`, `settings`, `metadata`, `$schema` | various | Not needed for adwright v1 |

Every component path must start with `./`, must exist, and must stay inside the plugin root. Unknown top-level keys are stripped with a validation warning. Environment variables available to hooks and servers: `${CLAUDE_PLUGIN_ROOT}`, `${CLAUDE_PLUGIN_DATA}`, `${CLAUDE_PROJECT_DIR}`.

Recommended adwright manifest:

```json
{
  "name": "adwright",
  "displayName": "adwright",
  "version": "0.1.0",
  "description": "Write honest, human-sounding Meta and X ads with verified specs and a banned-pattern linter.",
  "author": { "name": "Outdoor Norway" },
  "homepage": "https://github.com/<owner>/adwright",
  "repository": "https://github.com/<owner>/adwright",
  "license": "MIT",
  "keywords": ["advertising", "copywriting", "meta-ads", "x-ads", "claude-code-skill"],
  "skills": "./skills"
}
```

(Corey's repo and blader/humanizer use the same pattern: `"skills": "./skills"` and `"skills": ["./"]` respectively.)

#### marketplace.json

Path `.claude-plugin/marketplace.json` at the marketplace root (the directory that contains `.claude-plugin/`). Required top-level keys: `name`, `owner`, `plugins`.

| Field | Type | Rule |
|---|---|---|
| `name` | string, required | letters, digits, `.`, `_`, `-`; must start with a letter or digit; no `..`. Cannot be a reserved name (see below) |
| `owner` | object, required | `name` required; `email`, `url` optional |
| `plugins` | array, required | One object per plugin |
| `description` | string | Warned if missing |
| `version`, `metadata.description`, `metadata.version`, `metadata.pluginRoot` | strings | Optional |
| `$schema`, `forceRemoveDeletedPlugins`, `allowCrossMarketplaceDependenciesOn`, `renames` | various | Optional |

Plugin entry fields: `name` (required, same character rules; must equal the plugin's own `plugin.json` name or `/plugin install` by manifest name fails), `source` (required), `description`, `version`, `category`, `tags`, `strict` (default true), `displayName`, `defaultEnabled`, `dependencies`, `relevance`, `metadata`, plus any `plugin.json` field except the directory-listing ones. Entry `source` forms: a relative path string starting with `./` (the root itself is `"."`), or an object with `source` set to `github` (`repo`, `ref`, `sha`), `url` (`url`, `ref`, `sha`), `git-subdir` (`url`, `path`, `ref`, `sha`), `npm` (`package`, `version`, `registry`), `archive` (`url`, `sha256`) or `command`. A path containing `..` fails validation.

Reserved marketplace names include: `claude-code-marketplace`, `claude-code-plugins`, `claude-plugins-official`, `anthropic-marketplace`, `anthropic-plugins`, `agent-skills`, `anthropic-agent-skills`, `life-sciences`, `knowledge-work-plugins`, `claude-for-legal`, `claude-for-financial-services`, `financial-services-plugins`, `first-party-plugins`, `claude-tag-plugins`, `claude-community`, `claude-plugins-community`, `healthcare`, `inline`, `builtin`, `skills-dir`, `synced`, `claude-plugin-test`, `npm`, `pip`, `uv`, `cargo`, `github`, `gh`, any name starting `claudeai-`, and names that imitate official ones. `adwright` is clear of all of them.

Recommended adwright marketplace file (repo is both marketplace and plugin, so the entry points at the root):

```json
{
  "name": "adwright",
  "description": "Ad copy skills for Meta and X.",
  "owner": { "name": "Outdoor Norway" },
  "plugins": [
    {
      "name": "adwright",
      "source": "./",
      "description": "Write honest, human-sounding Meta and X ads with verified specs and a banned-pattern linter."
    }
  ]
}
```

With `source: "./"` and a `plugin.json` that sets `"skills": "./skills"`, the entry needs no component fields (`strict: true` default, `plugin.json` is the authority). Corey's repo uses this same shape (`"source": "./"` with `skills` in `plugin.json`).

Install flow for users (from the docs):

```text
/plugin marketplace add <owner>/adwright
/plugin install adwright@adwright
```

Shell equivalents: `claude plugin marketplace add <owner>/adwright` and `claude plugin install adwright@adwright`. Skills then run as `/adwright:<skill-folder-name>`. Update after edits with `/reload-plugins`; users on a hosted marketplace get a new version when `version` changes (a set `version` pins users until you bump it).

Validate before every push:

```bash
claude plugin validate ./adwright           # checks marketplace.json and each relative-path plugin.json
claude plugin validate ./adwright --strict  # turn warnings into failures in CI
```

Official validator output ends with a line reading "Validation passed". The marketplace guide notes that validation does not catch a source path that does not exist, nor a failure to fetch a remote source; test with a real install (`claude plugin marketplace add ./adwright` then `claude plugin install adwright@adwright`).

#### SKILL.md frontmatter (Claude Code)

Location per skill: `skills/<skill-name>/SKILL.md`. Must open with `---` on line 1. Unrecognised fields are ignored without error; if the YAML does not parse the skill loads with empty metadata.

| Field | Required | Meaning |
|---|---|---|
| `name` | no | Defaults to the directory name. The Agent Skills spec and the skill-creator validator want kebab-case, at most 64 characters |
| `description` | recommended | What it does and when to use it. If omitted, the first non-empty line is used. The combined `description` and `when_to_use` text is truncated at 1,536 characters in the skill listing, so put the key use case first |
| `when_to_use` | no | Extra trigger phrases; counts toward the 1,536 cap |
| `argument-hint`, `arguments` | no | Autocomplete hint and named positional arguments |
| `disable-model-invocation` | no | `true` means only a user can invoke it |
| `user-invocable` | no | `false` hides it from the `/` menu (Claude only) |
| `allowed-tools`, `disallowed-tools` | no | Tools granted without a prompt, or removed, while the skill is active (space or comma separated, or a YAML list) |
| `model`, `effort`, `context` (`fork`), `agent`, `background`, `hooks`, `paths`, `shell` | no | Run-time controls |
| `metadata`, `license`, `compatibility` | no | Accepted, not acted on (Agent Skills spec; `compatibility` up to 500 characters) |

Reserved: a skill folder named `synced` (any case); a folder or `name` of `anthropic-skills`, or starting `anthropic-skills:`, does not load outside plugins. Layout allowed inside a skill: `SKILL.md`, `reference.md`, `examples.md`, `scripts/`. Skill body style from `skill-creator`: keep SKILL.md under 500 lines, move depth into `references/` with clear "read when" pointers, add a table of contents to references over 300 lines, write instructions in the imperative, explain why instead of issuing heavy-handed orders.

Suggested adwright skill set (each a folder in `skills/`): `ad-brief` (intake and facts), `meta-ads`, `x-ads`, `humanize` (the banned-pattern pass), `verify` (claim check), with shared `references/specs-meta.md`, `references/specs-x.md`, `references/banned-patterns.md`. The slash commands would be `/adwright:meta-ads`, `/adwright:x-ads`, and so on.

#### Submitting to Anthropic's directory (optional)

The official repo README: external plugins go through a submission form; plugin names are immutable slugs once published (rename needs an entry in the marketplace `renames` map); a skill bundle without its own `plugin.json` can be listed with `strict: false` and an explicit `skills` array. Directory listing fields (`icon`, `documentationUrl`, `supportUrl`, `privacyPolicyUrl`, `termsOfServiceUrl`) belong in `plugin.json` only; a marketplace entry that sets them draws an unknown-field warning.

### How adwright should use this (Part D)

- Ship adwright as one repo that is both marketplace and plugin: `.claude-plugin/marketplace.json` with `source: "./"`, `.claude-plugin/plugin.json` with `"skills": "./skills"`, one folder per skill under `skills/`.
- Name the plugin `adwright`. Do not start any name with `claude-` or `anthropic-`; do not use a reserved marketplace name.
- Keep the entry `name` identical to the `plugin.json` `name`.
- Gate every release on `claude plugin validate . --strict` plus a real local `marketplace add` and `install`. Do not rely on `quick_validate.py`.
- Put descriptions first-use-case first and under 1,000 characters so the 1,536 combined cap is never hit. Use `disable-model-invocation: true` on any skill with side effects (none planned) and on borrowed reference skills.
- Add a small repo-level test that fails when em dashes, en dashes, emojis or the banned vocabulary appear in any skill or example file, since the client rules are part of the product.
- Do not use hooks, an MCP server, scripts that call the network, or writes outside the repo in v1. The sections above show that the plugins people distrust are the ones that do those things silently.

## 5. Appendix: scan results for the shortlisted skill folders

For each folder I scanned every file for zero-width and bidirectional control characters, curl-pipe-shell strings, base64 decode and eval, paste-site and tunnel URLs, and phrases such as "ignore previous instructions", "disregard the above", and "do not tell the user". Folders checked: marketingskills (copywriting, ad-creative, marketing-psychology, social, copy-editing, ads), blader/humanizer, stop-slop, copy-that-sells, conversion-copywriter, ogilvy, marketing-os, XZTP, wondelai influence-psychology, gbrain fact-check.

Result: no hidden characters, no pipe-to-shell, no encoded payloads, no exfiltration URLs. One phrase hit, in `marketingskills/skills/ads/references/audit-guardrails.md`, is a defensive rule telling the model not to follow such text found in fetched pages.

Broader repo findings that justify "copy folders, not repos":

- Hooks files (`hooks.json`, `settings.json`, `.mcp.json`) exist in alirezarezvani/claude-skills (eight or more sub-plugins), AEndrix03/Graft (plugin hooks), trailhq/Graft (written by init), and project-management configs. None exist in the shortlisted folders.
- `curl | bash` or `irm | iex` installers: AEndrix03/Graft, tarsluna/my-custom-skills, zubair-trabzada (both repos), Hainrixz/claude-ads, README mentions in AgriciDaniel/claude-ads (which also refuses such installs in its skill text).
- Credential-reading scripts (ad platform or service tokens): ivangfalco/ads-skills, mathiaschu/meta-ads-analyzer, YSY-99 examples, Hainrixz/claude-ads, Sandy-zippy stack, marketingskills `tools/clis`.
- Telemetry: trailhq/Graft (documented, opt-out), vercel-labs/skills (documented, opt-out). Aboudjem/humanizer-skill and the shortlisted skills document or show none. gbrain: none found in source, local-only search telemetry tables.
- Vendor funnel: irinabuht12-oss/marketing-skills (Ryze MCP URL repeated in 101 files).

## 6. Things I could not confirm

- I did not run any skill, script or CLI, so behaviour claims come from reading source and docs. For Graft's `--no-global` coverage of the `~/.claude` writes, the code comment and call site agree, but `graft init --dry-run` is the real proof.
- npm download counts for `@nanonets/graft` and star history were not fetched. The registry's latest version (0.21.1) matches the clone.
- The claim in marketingskills `copywriting` about +81 percent conversions and related figures has no source in the skill. [VERIFY: no source given in the skill]
- Vendor benchmark numbers for Graft and AEndrix03/Graft are vendor claims. [VERIFY: vendor benchmark]
- Spec figures for Reels primary text (44, 72, 40 and 55 characters) are from XZTP and vendor pages and appear in research file 03 as unverified. [VERIFY: only vendor sources]
- The 200 character X card description limit in marketingskills `ad-creative` is not confirmed in research file 03. [VERIFY: not in a primary source I checked]
- I did not find the user's actual definition of "Claude Code Setup" beyond the official claude-code-setup plugin; I assumed that meaning. If the user meant a different bundle, Part D still applies to the official plugin.
