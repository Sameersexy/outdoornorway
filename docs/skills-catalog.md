# Skills catalog

This page is for anyone who wants to know which skills exist for Outdoor Norway marketing, where each one lives, and which of them are safe to share.

## Where skills live

Skills sit in three places, and each place has its own sharing rule.

- **This public repo.** The plugin loads the commands, the two agents and the skills under `.claude/` (see `.claude-plugin/plugin.json`). The paused adquill drafts sit in `adquill/` and are not loaded. The two screened account skills sit in `account-skills/`, and the plugin does not load them. The repo is public and MIT licensed, so nothing private goes in.
- **The Claude account.** Skills the team built in the account, plus skills the platform provides. They work in account chats and are not part of the plugin. The account holds the live copy of each account-only skill.
- **The private backup.** A separate private repository kept outside this one. It holds chat transcripts and a second copy of the account-only skills, and it is never merged into this repo. [backup-and-restore.md](backup-and-restore.md) covers saving and restoring it.

The public repo is the source of truth for anything it contains. The account and the backup hold what the repo cannot.

## Original to this repo

### scriptcraft

The video script skill, at `.claude/skills/scriptcraft/SKILL.md`. It writes and fixes video scripts and creator briefs with enforced length, hook, density, disclosure and brand rules. It has two tiers (short form up to 25 seconds, long form up to 3:20) and three styles (voiceover, ugc_talk and ugc_text). A validator script, `.claude/skills/scriptcraft/scripts/script_check.py`, must pass before a script is final.

| Part | Path | Role |
|---|---|---|
| Agent | `.claude/agents/script-writer.md` | Writes scripts in the scriptcraft format and returns them only after the validator passes. Can add a one-page creator brief. |
| Agent | `.claude/agents/script-reviewer.md` | Independent reviewer. Reruns the validator, checks facts and disclosure, and ends with a verdict (ship, revise or reject). Its tools do not include Write or Edit. |
| Command | `/script` | Calls script-writer once and waits for it. |
| Command | `/review-script` | Calls script-reviewer on a script file. |
| Command | `/validate` | Runs the validator directly and shows only the findings. |
| Command | `/open-items` | Lists every open placeholder and unverified fact row in a script. |

The other commands (`/tour-data`, `/tokens`, `/howto`) do not use these agents. Installed as a plugin, the agents are named `outdoornorway-marketing:script-writer` and `outdoornorway-marketing:script-reviewer`.

### adquill (paused)

A skill and three agents for ad copy on Meta (Facebook and Instagram) and X. The files are drafts. The plugin does not install them, and Claude Code does not load them from `adquill/`. [adquill/README.md](../adquill/README.md) has the status and the file list. The three agents, `creative-director`, `direct-response-chief` and `editorial-director`, are read-only reviewers that score a finished draft.

## Third-party skills vendored in this repo

These eight skills sit in `.claude/skills/` as text copied from pinned commits. No third-party code runs. All eight are MIT licensed, and each folder keeps its upstream licence file, named `LICENSE-*`.

| Skill | What it does | Auto-invokes |
|---|---|---|
| copywriting | Writes, rewrites and improves marketing copy for pages | No (manual) |
| ad-creative | Generates and iterates ad headlines, descriptions and primary text for paid platforms | No (manual) |
| social | Creates and optimises social media content | No (manual) |
| marketing-psychology | Applies psychological principles and mental models to marketing | No (manual) |
| humanizer | Rewrites AI-sounding text so it reads like the writer | Yes |
| copy-that-sells | Writes ads, headlines, taglines, long copy and landing pages | No (manual) |
| conversion-copywriter | Writes conversion copy from scratch, with alternates for every headline | No (manual) |
| fact-check | Checks every claim in a piece of copy against a named source before it ships | Yes |

The six manual skills carry `disable-model-invocation: true`, so you call them by name, for example `/copywriting`.

[THIRD_PARTY_SKILLS.md](../THIRD_PARTY_SKILLS.md) has the upstream projects, the pinned commits and the full list of local changes. The vetting notes (what was read, what was rejected and why) are in [research/ad-copy/06-skill-vetting.md](research/ad-copy/06-skill-vetting.md).

## Account skills in this repo

Both skills passed a privacy screen before they were copied into `account-skills/`. Each is one folder with a `SKILL.md`. The plugin does not load them. [account-skills/README.md](../account-skills/README.md) explains how to copy or upload one, and how to add another.

| Skill | What it does | Folder |
|---|---|---|
| brand-voice-checker | Reviews guest-facing copy, such as tour scripts, captions and blog copy, against the brand voice guidelines: tone, language, style, perspective, and mission, vision and values. | `account-skills/brand-voice-checker/` |
| script-writing | Writes, drafts, improves and reviews video, social media and short-form content scripts. | `account-skills/script-writing/` |

## Account-only skills

These skills live in the Claude account, with a second copy in the private backup. None of them is copied into this repo or into the plugin. The reasons differ. Some did not pass the privacy screen, some are private by decision, and for one of them the copy in this repo is the canonical one. The skills are:

- content-qc
- guest-benefit-checker
- page-intent-audit
- scriptcraft (account copy)
- supplier-product-intake
- whatsapp-template-writer

Platform skills come with the account. They are not copied into this repo or into the plugin.

Before an account skill moves into the public repo, its owner should read it for supplier terms, prices, contacts and client detail. To restore skills on a new login, follow [backup-and-restore.md](backup-and-restore.md). The plugin side of the setup is in [installation.md](installation.md).
