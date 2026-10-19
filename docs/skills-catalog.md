# Skills catalog

This page is for anyone who wants to know which skills exist for Outdoor Norway marketing, where each one lives, and which of them are safe to share.

The list below reflects the repo and the Claude account on 15 October 2026. To see the live repo side, run these from the repo folder:

```
ls .claude/skills
ls .claude/agents
ls .claude/commands
ls adquill/agents
```

## How skills are organised

Skills sit in three places, and each place has its own sharing rule.

- **This public repo.** The plugin loads everything under `.claude/` (see `.claude-plugin/plugin.json`). That covers the scriptcraft skill, its two agents, the slash commands and the vendored third-party skills. The paused adquill drafts sit in `adquill/` and are not loaded. The repo is public and MIT licensed, so nothing private goes in.
- **The Claude account's synced skills folder.** Skills the team built in the account, plus skills the platform provides. They work in account chats and are not part of the plugin.
- **The private backup.** A separate private repository, written here as `<your-private-backup-repo>`. It holds chat transcripts and the account-only skills. It is never merged into this repo.

The public repo is the source of truth for anything it contains. The account and the backup hold what the repo cannot.

## Original to this repo

### scriptcraft

The video script skill, at `.claude/skills/scriptcraft/SKILL.md`. It writes and fixes video scripts and creator briefs with enforced length, hook, density, disclosure and brand rules. It has two tiers (short form up to 25 seconds, long form up to 3:20) and three styles (voiceover, ugc_talk and ugc_text). A validator script, `.claude/skills/scriptcraft/scripts/script_check.py`, must pass before a script is final.

| Part | Path | Role |
|---|---|---|
| Agent | `.claude/agents/script-writer.md` | Writes scripts in the scriptcraft format and returns them only after the validator passes. Can add a one-page creator brief. |
| Agent | `.claude/agents/script-reviewer.md` | Independent reviewer. Reruns the validator, checks facts and disclosure, and ends with a verdict (ship, revise or reject). It cannot edit files. |
| Command | `/script` | Calls script-writer once and waits for it. |
| Command | `/review-script` | Calls script-reviewer on a script file. |
| Command | `/validate` | Runs the validator directly and shows only the findings. |
| Command | `/open-items` | Lists every open placeholder and unverified fact row in a script. |

The other commands (`/tour-data`, `/tokens`, `/howto`) do not use these agents. Installed as a plugin, the agents are named `outdoornorway-marketing:script-writer` and `outdoornorway-marketing:script-reviewer`.

### adquill (paused)

A skill and three agents for ad copy on Meta (Facebook and Instagram) and X. The files are drafts. The plugin does not install them, and Claude Code does not load them from `adquill/`. See [../adquill/README.md](../adquill/README.md) for the status.

| Part | Path |
|---|---|
| Skill entry point | `adquill/skills/adquill/SKILL.md` |
| Instructions for any coding agent | `adquill/AGENTS.md` |
| Agent: creative-director | `adquill/agents/creative-director.md` |
| Agent: direct-response-chief | `adquill/agents/direct-response-chief.md` |
| Agent: editorial-director | `adquill/agents/editorial-director.md` |

The three agents are read-only reviewers that score a finished draft.

## Third-party skills vendored in this repo

These were copied into `.claude/skills/` as text from pinned commits. No third-party code runs. Each folder keeps its upstream licence file, named `LICENSE-*`, inside the folder.

| Skill | Upstream project | Licence | Auto-invokes |
|---|---|---|---|
| copywriting | coreyhaines31/marketingskills | MIT | No (manual) |
| ad-creative | coreyhaines31/marketingskills | MIT | No (manual) |
| social | coreyhaines31/marketingskills | MIT | No (manual) |
| marketing-psychology | coreyhaines31/marketingskills | MIT | No (manual) |
| humanizer | blader/humanizer | MIT | Yes |
| copy-that-sells | avectats7/copy-that-sells | MIT | No (manual) |
| conversion-copywriter | mikefutia/conversion-copywriter-skill | MIT | No (manual) |
| fact-check | garrytan/gbrain (rewritten) | MIT | Yes |

The six manual skills carry `disable-model-invocation: true`, so you call them by name, for example `/copywriting`.

[../THIRD_PARTY_SKILLS.md](../THIRD_PARTY_SKILLS.md) has the pinned commits and the full list of local changes. The vetting notes (what was read, what was rejected and why) are in [research/ad-copy/06-skill-vetting.md](research/ad-copy/06-skill-vetting.md).

## Account skills that are not in this repo

These were found in the Claude account's synced skills folder. A `manifest.json` there lists the name and source of each skill. None of them is copied into this repo or into the plugin. The source value in the manifest sorts them into three groups.

### Custom skills the team built

Manifest source "plugin". Each line is the purpose as the skill states it in its own description.

| Skill | Purpose |
|---|---|
| brand-voice-checker | Reviews tour scripts, captions and other guest-facing copy against the company brand voice. Checks tone and voice only. |
| content-qc | Pre-publish quality control for client-facing assets. Checks claims against a source of truth and the asset against itself, and produces a defect log with severity. |
| guest-benefit-checker | Reviews scripts and guest-facing copy for content angle: whether they lead with the guest's problem or benefit, or with itinerary and sales language. |
| page-intent-audit | Tests whether a page's structure serves search intent and whether its stated audience can complete a purchase. |
| script-writing | General skill for writing, drafting and reviewing video and short-form social scripts. |
| scriptcraft (account copy) | A chat edition of the repo skill that writes and reviews video scripts. It carries the writer and reviewer procedures in one file, with no agents or commands. It differs from the repo copy, and the repo copy is the canonical one. For a video script with a length, the repo skill states that it is preferred over script-writing. |
| supplier-product-intake | Kept private, see the private backup. |
| whatsapp-template-writer | Writes WhatsApp Business message templates and checks character, button, parameter and category rules. It does not set up the API or decide campaign strategy. |

### Platform skills, all rights reserved

Manifest source "anthropic": docx, pdf, pptx and xlsx. Each folder carries a licence that reserves all rights. They cannot be redistributed and are not copied anywhere, so they appear in neither the repo nor the backup.

### Platform example skills

Manifest source "anthropic-example".

- skill-creator, theme-factory and web-artifacts-builder carry an Apache 2.0 `LICENSE.txt` in their folders.
- docs, google-workspace, import-memory and morning have no licence file in their folders. [VERIFY: licence terms for docs, google-workspace, import-memory and morning]

## Which skills live where, and how to restore them

The private backup holds account-only skills, so a skill that lives in the public repo shows n/a in that column.

| Skill | In public repo | In private backup |
|---|---|---|
| scriptcraft | Yes, `.claude/skills/scriptcraft/` (canonical) | [VERIFY: confirm the backup holds the account copy of scriptcraft] |
| adquill | Yes, `adquill/` (paused drafts, not installed by the plugin) | n/a |
| copywriting, ad-creative, social, marketing-psychology, humanizer, copy-that-sells, conversion-copywriter, fact-check | Yes, `.claude/skills/<name>/` | n/a |
| brand-voice-checker | No | Yes |
| content-qc | No | Yes |
| guest-benefit-checker | No | Yes |
| page-intent-audit | No | Yes |
| script-writing | No | Yes |
| supplier-product-intake | No | Yes |
| whatsapp-template-writer | No | Yes |
| docx, pdf, pptx, xlsx | No | No (all rights reserved, never copied) |
| skill-creator, theme-factory, web-artifacts-builder, docs, google-workspace, import-memory, morning | No | [VERIFY: confirm whether the backup holds the platform example skills] |

Account skills stay out of the public repo. Before one moves in, its owner should read it for supplier terms, prices, contacts and client detail, because the repo is public.

To restore, follow [backup-and-restore.md](backup-and-restore.md). The plugin side of the setup is in [installation.md](installation.md).
