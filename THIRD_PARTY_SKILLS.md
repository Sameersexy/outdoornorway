# Third-party skills in `.claude/skills/`

These skills were copied into the repo as text, from pinned commits. No third-party code runs. Each copy keeps its upstream licence file.
The vetting notes (what was read, what was rejected and why) are in `docs/research/ad-copy/06-skill-vetting.md`.

| Skill | Source | Pinned commit | Licence | Auto-invokes |
|---|---|---|---|---|
| copywriting | coreyhaines31/marketingskills, `skills/copywriting` | dda3841f0b294e01e93b1541486beefbfab0915e | MIT | No (manual) |
| ad-creative | coreyhaines31/marketingskills, `skills/ad-creative` | dda3841f0b294e01e93b1541486beefbfab0915e | MIT | No (manual) |
| social | coreyhaines31/marketingskills, `skills/social` | dda3841f0b294e01e93b1541486beefbfab0915e | MIT | No (manual) |
| marketing-psychology | coreyhaines31/marketingskills, `skills/marketing-psychology` | dda3841f0b294e01e93b1541486beefbfab0915e | MIT | No (manual) |
| humanizer | blader/humanizer, `SKILL.md` | 225a6f39ac85f76ee48dbad772ea4abe4ed6c9d8 | MIT | Yes |
| avoid-ai-writing | conorbronsdon/avoid-ai-writing, `SKILL.md` and `references/patterns.md` | 209815cdeb4af942616daec89a5e0a706c804e3a | MIT | No (manual) |
| copy-that-sells | avectats7/copy-that-sells, `skills/copy-that-sells` | aef838698152ef7904d1344a71213721ffe4b474 | MIT | No (manual) |
| conversion-copywriter | mikefutia/conversion-copywriter-skill, `SKILL.md` | f8d30360d38b20ff1f616ff6c4c5d89a764ce9a3 | MIT | No (manual) |
| fact-check | garrytan/gbrain, `skills/fact-check` (rewritten, see below) | 76a9984bdca8183f34965e04e0aad92c85e71ba8 | MIT | Yes |
| ponytail | DietrichGebert/ponytail, `skills/ponytail` | 09c434ab73ca43761c5d8b0c5d341926c2fba710 | MIT | Yes |

This repo's own files are MIT licensed (see `LICENSE`). Each third-party skill keeps the licence of its upstream project, in a `LICENSE-*` file inside its folder.

## Why some are manual only

The writing skills overlap. All of them say "write copy". If they all auto-invoked, they would compete. They carry `disable-model-invocation: true`, so you call them by name (for example `/copywriting`). The ad writer for this repo is `adquill`, and it reads these as references.

## Local changes (all of them)

- Removed upstream eval fixtures, a Spanish reference file, a validator script and a deck renderer that were not copied.
- Replaced em and en dashes with commas and hyphens on every line that was not about dashes themselves.
- Replaced the stale Meta table in `ad-creative/references/platform-specs.md` with the verified one (Facebook feed headline 27, Instagram feed headline field 40 but often hidden, about 125 visible characters of primary text).
- Removed `allowed-tools` and the deck step from `conversion-copywriter`, and a warning-sign emoji from its "The site" bullet.
- `fact-check` is a rewrite: the gbrain database lane and every `gbrain` command were removed, and an ad-copy section with this repo's sources of truth was added.
- Added `disable-model-invocation: true` to the six writing skills.
- Removed `copy-that-sells/examples/` (a fictional mattress brand brief and its output, referenced nowhere). Removed the `cookbook/` bullet and the "spanish file" wording from `copy-that-sells/SKILL.md`, and the browser and `copy-deck.html` sentence from `conversion-copywriter/SKILL.md`, because the files they named were not copied.
- Removed the Claude model names from one heading in `copy-that-sells/references/self-edit.md` and replaced one dash in `ad-creative/references/imessage-video-ads.md`.
- `avoid-ai-writing`: copied only `SKILL.md` and `references/patterns.md` (v3.38.0). Not copied: the `scripts/`, `detector/`, `examples/`, `bin/`, `evals/`, `corpus/` and `dist/` folders and the packaging for other tools, because no third-party code runs here. Added `disable-model-invocation: true` so it stays manual next to `humanizer`, removed the emoji from the frontmatter, replaced spaced em dashes with hyphens in `SKILL.md` prose, and added a note under the title that the bundled commands are absent and the manual fallbacks apply. `references/patterns.md` is unchanged.
- Kept on purpose: quoted dashes and emoji where a file lists them as examples of AI writing to avoid (for example `copywriting/references/ai-tells.md`) or shows an ad format that uses them.

## What was deliberately not installed

- **gbrain runtime.** It is a memory runtime (Bun, a local database, optional background services, a daily version check), not a skill pack. Only its `fact-check` skill fits this work, and it was copied by hand.
- **Graft** (trailhq/Graft). It builds a code graph with tree-sitter, which does not read markdown. This repo is markdown and two Python files. Its init writes hooks into `.claude/settings.json` that fire on every prompt.
- 26 other candidates were read and rejected or kept as reading only. Reasons include lead-gen funnels, scripts that read ad account tokens, and curl-pipe installers.

## Upgrading

Diff against upstream before changing anything. Do not run an installer over these folders, because it would overwrite the local changes above.
