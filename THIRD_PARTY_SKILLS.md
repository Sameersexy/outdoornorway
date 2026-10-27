# Third-party skills in `.claude/skills/`

These skills were copied into the repo as text, from pinned commits. No third-party code runs. Each copy keeps its upstream licence file.
The vetting notes (what was read, what was rejected and why) are in `docs/research/ad-copy/06-skill-vetting.md`.

| Skill | Source | Pinned commit | Licence | Auto-invokes |
|---|---|---|---|---|
| copywriting | coreyhaines31/marketingskills, `skills/copywriting` | dda3841f0b294e01e93b1541486beefbfab0915e | MIT | No (manual) |
| ad-creative | coreyhaines31/marketingskills, `skills/ad-creative` | dda3841f0b294e01e93b1541486beefbfab0915e | MIT | No (manual) |
| social | coreyhaines31/marketingskills, `skills/social` | dda3841f0b294e01e93b1541486beefbfab0915e | MIT | No (manual) |
| marketing-psychology | coreyhaines31/marketingskills, `skills/marketing-psychology` | dda3841f0b294e01e93b1541486beefbfab0915e | MIT | No (manual) |
| seo-audit | coreyhaines31/marketingskills, `skills/seo-audit` | e6c962c051806a0fc20c1c317114ab4f6438eb3a | MIT | Yes |
| ai-seo | coreyhaines31/marketingskills, `skills/ai-seo` | e6c962c051806a0fc20c1c317114ab4f6438eb3a | MIT | Yes |
| schema | coreyhaines31/marketingskills, `skills/schema` | e6c962c051806a0fc20c1c317114ab4f6438eb3a | MIT | Yes |
| ads | coreyhaines31/marketingskills, `skills/ads` | e6c962c051806a0fc20c1c317114ab4f6438eb3a | MIT | No (manual) |
| competitor-profiling | coreyhaines31/marketingskills, `skills/competitor-profiling` | e6c962c051806a0fc20c1c317114ab4f6438eb3a | MIT | Yes |
| video | coreyhaines31/marketingskills, `skills/video` | e6c962c051806a0fc20c1c317114ab4f6438eb3a | MIT | No (manual) |
| humanizer | blader/humanizer, `SKILL.md` | 225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8 | MIT | Yes |
| copy-that-sells | avectats7/copy-that-sells, `skills/copy-that-sells` | aef838698152ef7904d1344a71213721ffe4b474 | MIT | No (manual) |
| conversion-copywriter | mikefutia/conversion-copywriter-skill, `SKILL.md` | f8d30360d38b20ff1f616ff6c4c5d89a764ce9a3 | MIT | No (manual) |
| fact-check | garrytan/gbrain, `skills/fact-check` (rewritten, see below) | 76a9984bdca8183f34965e04e0aad92c85e71ba8 | MIT | Yes |
| ponytail | DietrichGebert/ponytail, `skills/ponytail` | 09c434ab73ca43761c5d8b0c5d341926c2fba710 | MIT | Yes |

This repo's own files are MIT licensed (see `LICENSE`). Each third-party skill keeps the licence of its upstream project, in a `LICENSE-*` file inside its folder.

## Why some are manual only

The writing skills overlap. All of them say "write copy". If they all auto-invoked, they would compete. They carry `disable-model-invocation: true`, so you call them by name (for example `/copywriting`). The ad writer for this repo is `adquill`, and it reads these as references.

`ads` and `video` are manual for the same reason: `ads` overlaps `ad-creative` and `adquill`, and `video` overlaps `scriptcraft`, which writes every video script in this repo. The SEO skills (`seo-audit`, `ai-seo`, `schema`) and `competitor-profiling` do not write copy, so they auto-invoke.

## Local changes to the first nine skills

- Removed upstream eval fixtures, a Spanish reference file, a validator script and a deck renderer that were not copied.
- Replaced em and en dashes with commas and hyphens on every line that was not about dashes themselves.
- Replaced the stale Meta table in `ad-creative/references/platform-specs.md` with the verified one (Facebook feed headline 27, Instagram feed headline field 40 but often hidden, about 125 visible characters of primary text).
- Removed `allowed-tools` and the deck step from `conversion-copywriter`, and a warning-sign emoji from its "The site" bullet.
- `fact-check` is a rewrite: the gbrain database lane and every `gbrain` command were removed, and an ad-copy section with this repo's sources of truth was added.
- Added `disable-model-invocation: true` to the six writing skills.
- Removed `copy-that-sells/examples/` (a fictional mattress brand brief and its output, referenced nowhere). Removed the `cookbook/` bullet and the "spanish file" wording from `copy-that-sells/SKILL.md`, and the browser and `copy-deck.html` sentence from `conversion-copywriter/SKILL.md`, because the files they named were not copied.
- Removed the Claude model names from one heading in `copy-that-sells/references/self-edit.md` and replaced one dash in `ad-creative/references/imessage-video-ads.md`.
- Kept on purpose: quoted dashes and emoji where a file lists them as examples of AI writing to avoid (for example `copywriting/references/ai-tells.md`) or shows an ad format that uses them.

## Local changes to the six skills pinned at e6c962c (October 2026)

`seo-audit`, `ai-seo`, `schema`, `ads`, `competitor-profiling` and `video` were copied from commit `e6c962c051806a0fc20c1c317114ab4f6438eb3a`. Every file was read before it was copied. No script runs. The changes:

- Not copied: the `evals/` folder of each skill, and `video/references/product-demo-recording.md` (a Playwright and ffmpeg recorder guide for web apps that installs tools and points at upstream scripts to copy). The `video` description lost the three triggers that only that file served, and `video/SKILL.md` lost the paragraph that linked it.
- Replaced em and en dashes with commas, colons and hyphens on every line, except the quoted examples in `seo-audit/references/ai-writing-detection.md`, which list dashes as an AI tell. One wiki link in `ads/SKILL.md` was updated to match its heading.
- Removed model version names: "ChatGPT 5.6" and "5.6" in `ai-seo/SKILL.md` and `ai-seo/references/format-volatility.md` now read "the August 2026 ChatGPT update"; "Veo 3", "Runway Gen-4", "Kling 2.5/3.0", "Pika 2.x" and "Wan 2" in `video/SKILL.md` and `video/references/ai-video-prompting.md` now carry no version; "built on the Muse Spark model" was cut from `ai-seo/references/platform-ranking-factors.md`. Product and platform names (ChatGPT, Claude, Gemini, Perplexity, Copilot, Veo, Kling) stay, because the skills are about those platforms.
- Removed emoji: two check marks in the tool table of `ads/SKILL.md` (now "Yes") and a thumbs up and down pair in `ads/references/abm-playbook.md` (now words).
- Removed a shell loop in `ai-seo/references/linkedin-ai-citations.md` that fetched a LinkedIn article with spoofed crawler user agents, and put a one-line manual check in its place.
- Tool names: `web_fetch` became `WebFetch` (four places in `seo-audit/SKILL.md`). `competitor-profiling/SKILL.md` gained a paragraph saying that this repo's `.mcp.json` starts a Scrapling MCP server in cloud sessions, which can stand in for WebFetch.
- Links to upstream skills that are not vendored: `ads/references/creative-research-automation.md` linked `customer-research` and `product-marketing` skill files, and `ads/references/google-ads-audit-checklist.md` linked a `conversion-tracking.md` that does not exist. They are now plain text that says the skill is not vendored, and product marketing points at `.claude/product-marketing.md`. `video/SKILL.md` and `video/references/edit-anatomy.md` name the upstream `watch-video` and `social-fetch` skills; a note now says they are not vendored and to ask the user for the file or screenshots.
- `video/SKILL.md` step 1 of the product demo workflow now sends scripts to `scriptcraft` instead of `copywriting`.
- `ads/references/ad-copy-templates.md`: the Meta headline line said 40 characters recommended. It now matches the verified table in `ad-creative/references/platform-specs.md` (27 in the Facebook feed, field allows 40, often hidden on Instagram feed).
- Added `disable-model-invocation: true` to `ads` and `video`.
- `ai-seo/SKILL.md`: the sample `/pricing.md` gave a placeholder sales email address. It now says "contact sales (email on the contact page)", because the integrity test bans email addresses in the repo.
- Left as upstream wrote them: the "Related Skills" lists and the "see X" pointers in descriptions name upstream skills that are not installed here (for example `programmatic-seo`, `cro`, `marketing-loops`, `conversion-tracking`). Links to the upstream tool guides on GitHub are upstream's own. The examples and benchmarks are written for SaaS and B2B, not for a tour operator, so check them against `.claude/product-marketing.md` before use. `competitor-profiling` saves raw scrapes to `competitor-profiles/` at the repo root; this repo is public, so keep that folder out of commits unless the owner agrees.

## What was deliberately not installed

- **gbrain runtime.** It is a memory runtime (Bun, a local database, optional background services, a daily version check), not a skill pack. Only its `fact-check` skill fits this work, and it was copied by hand.
- **Graft** (trailhq/Graft). It builds a code graph with tree-sitter, which does not read markdown. This repo is markdown and two Python files. Its init writes hooks into `.claude/settings.json` that fire on every prompt.
- 26 other candidates were read and rejected or kept as reading only. Reasons include lead-gen funnels, scripts that read ad account tokens, and curl-pipe installers.

## Upgrading

Diff against upstream before changing anything. Do not run an installer over these folders, because it would overwrite the local changes above.
