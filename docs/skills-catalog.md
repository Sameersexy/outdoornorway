# Skills catalog

This page is for anyone who wants to know which skills exist for Outdoor Norway marketing, where each one lives, and which of them are safe to share.

## Where skills live

Skills sit in three places, and each place has its own sharing rule.

- **This public repo.** The plugin loads the commands, the two agents and the skills under `.claude/` (see `.claude-plugin/plugin.json`). The paused adquill drafts sit in `adquill/` and are not loaded. The three account skills sit in `account-skills/`. The umbrella plugin does not load them, and the plugin `outdoornorway-account-skills` does. The repo is public and MIT licensed, so nothing private goes in.
- **The Claude account.** Skills the team built in the account, plus skills the platform provides. They work in account chats and are not part of the plugin. The account holds the live copy of each account-only skill.
- **The private backup.** A backup kept outside this repo. It holds chat transcripts and a second copy of the account-only skills, and it is never merged into this repo. [backup-and-restore.md](backup-and-restore.md) covers saving and restoring it.

The public repo is the source of truth for anything it contains. The account and the backup hold what the repo cannot.

### Which plugin ships which skill

The marketplace has four plugins, and only three hold skills. [marketplace.md](marketplace.md) says who each is for and how to install it.

| Plugin | Skills | Folder |
|---|---|---|
| `outdoornorway-marketing` | scriptcraft and the fifteen vendored skills, plus the commands and agents | `.claude/` |
| `outdoornorway-copy-skills` | The fifteen vendored skills only | `.claude/skills/` |
| `outdoornorway-account-skills` | brand-voice-checker, guest-benefit-checker and script-writing | `account-skills/` |

scriptcraft is only in the umbrella plugin, because the validator needs the tour data and the plugin root. Each other skill sits in one folder and is listed in one plugin besides the umbrella.

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

These fifteen skills sit in `.claude/skills/` as text copied from pinned commits. No third-party code runs. All fifteen are MIT licensed, and each folder keeps its upstream licence file, named `LICENSE-*`.

| Skill | What it does | Auto-invokes |
|---|---|---|
| copywriting | Writes, rewrites and improves marketing copy for pages | No (manual) |
| ad-creative | Generates and iterates ad headlines, descriptions and primary text for paid platforms | No (manual) |
| social | Creates and optimises social media content | No (manual) |
| marketing-psychology | Applies psychological principles and mental models to marketing | No (manual) |
| ponytail | Makes the agent write the smallest complete change on coding tasks | Yes |
| humanizer | Rewrites AI-sounding text so it reads like the writer | Yes |
| copy-that-sells | Writes ads, headlines, taglines, long copy and landing pages | No (manual) |
| conversion-copywriter | Writes conversion copy from scratch, with alternates for every headline | No (manual) |
| fact-check | Checks every claim in a piece of copy against a named source before it ships | Yes |
| seo-audit | Audits technical, on-page and local SEO and lists the fixes in priority order | Yes |
| ai-seo | Makes pages easier for AI search engines and assistants to find, quote and recommend | Yes |
| schema | Adds, fixes and checks schema.org structured data (JSON-LD) | Yes |
| ads | Plans, audits and optimises paid campaigns on Google, Meta, LinkedIn and other platforms | No (manual) |
| competitor-profiling | Builds structured competitor profiles from a list of competitor URLs | Yes |
| video | Plans video production with AI generation, avatars and programmatic tools. Scripts stay with scriptcraft | No (manual) |

The eight manual skills carry `disable-model-invocation: true`, so you call them by name, for example `/copywriting`. `ads` is manual because it overlaps ad-creative and adquill, and `video` because scriptcraft writes every video script here. The umbrella plugin loads all fifteen. The plugin `outdoornorway-copy-skills` ships only these fifteen, and its fact-check cannot read the tour data (see [marketplace.md](marketplace.md#the-fact-check-caveat)).

[THIRD_PARTY_SKILLS.md](../THIRD_PARTY_SKILLS.md) has the upstream projects, the pinned commits and the full list of local changes. The vetting notes (what was read, what was rejected and why) are in [research/ad-copy/06-skill-vetting.md](research/ad-copy/06-skill-vetting.md).

The SEO skills and competitor-profiling read web pages. In cloud sessions, the Scrapling MCP server in `.mcp.json` can fetch them (see [repo-map.md](repo-map.md)). The skills are written for SaaS and B2B, so check their examples and benchmarks against `.claude/product-marketing.md` before you use them for tours.

## Account skills in this repo

All three skills were read for supplier terms, prices, contacts, personal data and client facts before they were copied into `account-skills/`. Each is one folder with a `SKILL.md`. The plugin `outdoornorway-account-skills` loads them, and the umbrella plugin does not. [account-skills/README.md](../account-skills/README.md) explains how to install, copy or upload one, and how to add another. An account upload accepts a description of 200 characters at most, and the description of each skill below is longer, so shorten it in the copy you upload. [VERIFY: one official page gives 1,024 characters as the limit, so the owner confirms with a test upload] The command `skills pack` flags any description over 200 characters.

| Skill | What it does | Folder |
|---|---|---|
| brand-voice-checker | Reviews guest-facing copy, such as tour scripts, captions and blog copy, against the brand voice guidelines: tone, language, style, perspective, and mission, vision and values. | `account-skills/brand-voice-checker/` |
| guest-benefit-checker | Reviews guest-facing copy for content angle, meaning whether it leads with the guest's benefit or with itinerary details, logistics or a sales pitch. | `account-skills/guest-benefit-checker/` |
| script-writing | Writes, drafts, improves and reviews video, social media and short-form content scripts. | `account-skills/script-writing/` |

## Account-only skills

These skills live in the Claude account, with a second copy in the private backup. None of them has a copy in `account-skills/`, and no plugin loads an account copy of any of them. The skills are:

- content-qc
- page-intent-audit
- scriptcraft
- supplier-product-intake
- whatsapp-template-writer

For scriptcraft, the maintained copy is `.claude/skills/scriptcraft/` in this repo, which the plugin loads. The account copy is not uploaded to this repo.

Platform skills come with the account. They are not copied into this repo or into the plugin.

Before an account skill moves into the public repo, its owner should read it for supplier terms, prices, contacts and client detail. To restore skills on a new login, follow [backup-and-restore.md](backup-and-restore.md). The plugin side of the setup is in [installation.md](installation.md).
