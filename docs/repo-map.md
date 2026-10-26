# Repo map

This page shows where each folder and file lives, what uses it and whether it can move.

## Start here

The repo is a Claude Code marketplace with four plugins, plus the files they work on. The main plugin, `outdoornorway-marketing`, is the whole repo: its entry in `marketplace.json` points `source` at `./`. Two more ship only skills, from `.claude/skills/` and `account-skills/`, and `repo-band` in `mods/` is a status row mod. [marketplace.md](marketplace.md) describes all four. Writers use slash commands to draft and check video scripts. Tour prices and dates live in one data file. A handful of paths are written into code, tests and manifests, so those stay where they are.

If you write scripts, read [getting-started.md](getting-started.md). If you change the tools, read [CONTRIBUTING.md](../CONTRIBUTING.md). The full docs index is [README.md](README.md).

## Tree

The tree shows two levels. Each folder guide lists the files inside it.

```
outdoornorway/
|-- .claude/                    [fixed]  commands, agents and skills for Claude Code
|   |-- agents/                 [fixed]  script-writer and script-reviewer
|   |-- commands/               [fixed]  the slash commands
|   |-- skills/                 [fixed]  scriptcraft and the vendored skills
|   |-- product-marketing.md             brand facts and the do-not-claim list
|   `-- settings.json           [fixed]  project settings for a clone
|-- .claude-plugin/             [fixed]  plugin and marketplace manifests
|   |-- marketplace.json        [fixed]  marketplace listing
|   `-- plugin.json             [fixed]  plugin manifest
|-- account-skills/                      account skills, shipped by their own plugin
|   |-- brand-voice-checker/             guest-facing copy checked against the brand voice
|   |-- guest-benefit-checker/           guest-facing copy checked for a benefit-led angle
|   |-- README.md                        guide to the account skills
|   `-- script-writing/                  short-form video script craft
|-- adquill/                             paused ad-copy skill, not installed by the plugin
|   |-- agents/                          paused agents
|   |-- skills/                          paused ad-copy skill
|   |-- AGENTS.md                        instructions for other coding agents
|   `-- README.md                        why adquill is paused
|-- campaigns/                  [fixed]  tour data, ski ad notes and email drafts
|   |-- itinerary-download-emails/       follow-up emails after an itinerary download, drafts
|   `-- ski-meta-ads/           [fixed]  tours.json, its checker and the ad notes
|-- content/                    [fixed]  finished and draft video scripts
|   `-- scripts/                [fixed]  scripts, each with a notes file
|-- docs/                       [fixed]  guides, research and review history
|   |-- research/                        research behind the skills
|   |-- script-skill-reviews/            review rounds of the script skill
|   |-- backup-and-restore.md            what to save and how to restore it
|   |-- getting-started.md      [fixed]  guide for writers and editors
|   |-- installation.md                  install, check, update and remove
|   |-- marketplace.md                   the four plugins, installs and releases
|   |-- publishing-to-npm.md             publish the launcher to npm
|   |-- README.md                        docs index
|   |-- repo-map.md                      this page
|   |-- skills-catalog.md                what each skill is for
|   `-- token-hygiene.md        [fixed]  habits that keep sessions cheap
|-- mods/                                a Claude Code mod, shipped as a plugin
|   `-- repo-band/                       status row above the prompt
|-- tools/                      [fixed]  tests, token report, npx launcher and skill packer
|   |-- outdoornorway-cli.js    [fixed]  npx launcher
|   |-- pack_skills.py          [fixed]  packs skills into zips for claude.ai
|   |-- README.md                        guide to the tools
|   |-- test_repo_integrity.py  [fixed]  integrity test
|   `-- transcript_report.py    [fixed]  token report for /tokens
|-- .gitignore                  [fixed]  keeps caches, .env files and transcripts out of git
|-- CHANGELOG.md                         what changed and when
|-- CLAUDE.md                   [fixed]  rules for Claude Code in this repo
|-- CONTRIBUTING.md                      how to change the tools
|-- LICENSE                     [fixed]  MIT licence
|-- package.json                [fixed]  launcher metadata
|-- README.md                   [fixed]  front page
`-- THIRD_PARTY_SKILLS.md       [fixed]  sources and licences of vendored skills
```

[fixed] marks a path that must not move: its row in the next table starts with No. A folder carries the mark when something inside it is fixed. Git and cache folders are left out.

## Paths and whether they can move

Safe to move? has two answers. No means code, tests or manifests name the path. With edits means it can move once you fix the references the row lists.

| Path | What it holds | Who uses it | Safe to move? |
|---|---|---|---|
| `.claude-plugin/` | `plugin.json` and `marketplace.json`: plugin names, versions and which folders ship. The marketplace lists four plugins. | The plugin install, the integrity test, `doctor` and `list` in the launcher | No. The test and the launcher open both files by path. |
| `.claude/commands/` | The slash commands | The plugin, the integrity test | No. `plugin.json` names this folder and the test reads every file in it. |
| `.claude/agents/` | `script-writer.md` and `script-reviewer.md` | `/script` and `/review-script` | No. `plugin.json` lists both files by path. |
| `.claude/skills/` | `scriptcraft` (the video script skill, its validator and tests) and the vetted third-party skills. [skills-catalog.md](skills-catalog.md) says what each is for. | The plugins `outdoornorway-marketing` and `outdoornorway-copy-skills`, the commands, the agents | No. `plugin.json` names the folder, the copy-skills entry in `marketplace.json` uses it as its `source`, and the commands and agents call `.claude/skills/scriptcraft/scripts/script_check.py`. |
| `.claude/settings.json` | Project settings for a clone: enabled plugins (including ponytail and repo-band), their marketplaces and the auto-compact window | Claude Code, in a clone | No. Claude Code reads project settings from this path. |
| `.claude/product-marketing.md` | Brand context, confirmed facts and the do-not-claim list | The copy skills and the agents | With edits. CLAUDE.md, the reviewer agent, several skills and the script notes cite this path. |
| `campaigns/ski-meta-ads/` | `tours.json` (prices, dates, day-by-day plans), its checker and the ski ad notes. See [its README](../campaigns/ski-meta-ads/README.md). | The validator (`--tour`), `/tour-data`, `doctor`, both agents | No. `script_check.py` finds `tours.json` by going up four folders from its own folder, so a move breaks `--tour` unless you pass `--tours-file`. `doctor` lists the file as required. |
| `campaigns/itinerary-download-emails/` | Draft follow-up email sequences for the 7-Day Bergen to Tromsø and 6-Day Alta trips, with the reasoning, open decisions and sources. See [its README](../campaigns/itinerary-download-emails/README.md). | Nothing yet; the emails are sent from the mailing tool | Yes, nothing reads it. |
| `content/scripts/` | Finished and draft scripts, each with a notes file. See [its README](../content/scripts/README.md). | `/script` writes here by default | No. The script agents save here by default, and the integrity test lists its README. |
| `docs/getting-started.md`, `docs/token-hygiene.md` | The guide for writers and editors, and the token habits | `/howto`, `/tokens`, the integrity test | No. `/howto` copies the Quick start from the guide and the test reads it. `/tokens` points to the token page. |
| `docs/` | Guides, research and review history. See [README.md](README.md). | Everyone | No. The two files above keep the folder in place, and CLAUDE.md names `docs/repo-map.md`, `docs/README.md` and `docs/token-hygiene.md` by path. Inside it, a guide can move once its links are fixed, and the docs index and the integrity test name most of them. |
| `tools/outdoornorway-cli.js`, `tools/pack_skills.py`, `tools/test_repo_integrity.py`, `tools/transcript_report.py` | The npx launcher, the skill packer, the integrity test and the token report. See [the tools guide](../tools/README.md). | `package.json` (`bin`), the launcher's `skills pack`, CLAUDE.md, `/tokens` | No. Each is named by the file that uses it, and both Python and Node code find the repo root as the folder above `tools/`. |
| `adquill/` | A paused ad-copy skill and three agents (drafts). See [its README](../adquill/README.md). | Nothing at run time. The launcher's `test --all` runs its linter tests. | With edits. The plugin does not install it. A move means updating `files` in `package.json`, the `--all` path in the launcher and the links in the docs. |
| `account-skills/` | Account skills, one folder each with a `SKILL.md`. See [its README](../account-skills/README.md). | The plugin `outdoornorway-account-skills`, `skills pack`, the integrity test | No. The `account-skills` entry in `marketplace.json` uses the folder as its `source`, and `files` in `package.json` lists it. A move also needs new links and a test edit. |
| `mods/repo-band/` | A Claude Code mod: the status row above the prompt, with its types and a test. See [its README](../mods/repo-band/README.md). | The plugin `repo-band`, the integrity test (version and `source`) | With edits. The marketplace entry names the folder as `source`, and `package.json` lists `mods/` under `files`. |
| `README.md` | The front page: install, commands, what is here | Everyone | No. The integrity test reads it. |
| `CLAUDE.md` | Rules and commands for Claude Code working in this repo | Claude Code, in a clone | No. Claude Code loads it from the repo root, and the integrity test reads it. |
| `CONTRIBUTING.md`, `CHANGELOG.md` | How to change the tools, and what changed and when | Contributors, maintainers | With edits. The integrity test lists both, so a move also needs new links and a test edit. |
| `LICENSE`, `THIRD_PARTY_SKILLS.md` | The MIT licence, and the source, pinned commit and licence of each third-party skill | The integrity test | No. The licence checks read both by path. |
| `package.json` | Launcher metadata: `bin`, `files`, Node `engines`, no dependencies | npm, `npx`, the integrity test | No. Keep it at the root. Its `version` must match `plugin.json` and every entry in `marketplace.json`. |
| `.gitignore` | Keeps Python caches, transcripts (`*.jsonl`), archives (`*.zip`, `*.tgz`), `.env` files, `node_modules/`, `backup/`, `exports/` and `dist/` (the zips from `skills pack`) out of git | Git, the integrity test | No. The test checks that the main patterns are listed. |

Chat transcripts are not in this repo. Three account skills are, in [account-skills/](../account-skills/README.md). The other account-only skills stay in the Claude account, with a second copy in a private backup kept outside this repo. [backup-and-restore.md](backup-and-restore.md) has the steps.

## Where do I find...

| I want | Go to |
|---|---|
| A finished or draft script | `content/scripts/`. Each script has a notes file beside it. |
| Tour prices, dates and day-by-day plans | `campaigns/ski-meta-ads/tours.json`. To print one tour, run `python3 -I .claude/skills/scriptcraft/scripts/script_check.py --tour ski-aurora-7day`. A wrong id prints the list of valid ids. |
| The validator | `.claude/skills/scriptcraft/scripts/script_check.py`. Its limits are in `tiers.json` and its brand rules in `brand_rules.json`, both in the same folder. |
| The slash commands | `.claude/commands/`. The list with one line each is in the root [README](../README.md). |
| The agents | `.claude/agents/` |
| Brand facts and the do-not-claim list | `.claude/product-marketing.md` |
| Third-party skills and their licences | `THIRD_PARTY_SKILLS.md`, and the `LICENSE-*` file inside each skill folder under `.claude/skills/` |
| Account skills that can be installed, copied or uploaded | [account-skills/README.md](../account-skills/README.md) |
| Install, update or uninstall the plugin | [installation.md](installation.md) |
| Choose among the four plugins, add a skill or cut a release | [marketplace.md](marketplace.md) |
| Back up or restore transcripts and account-only skills | [backup-and-restore.md](backup-and-restore.md) |
| Publish the launcher to npm | [publishing-to-npm.md](publishing-to-npm.md) |
| Test and check commands | [CONTRIBUTING.md](../CONTRIBUTING.md#run-the-tests) |
| Token tips | [token-hygiene.md](token-hygiene.md), the `/tokens` command, and the Tokens section of `CLAUDE.md` |
| How the script skill was reviewed | [script-skill-reviews/README.md](script-skill-reviews/README.md) |
| Research behind the skills | [research/README.md](research/README.md) |
| The paused ad-copy skill | [adquill/README.md](../adquill/README.md) |
| What changed and when | [CHANGELOG.md](../CHANGELOG.md) |

## How the pieces connect

Commands call agents or tools. Agents call the validator. The validator reads its own rule files. Data comes from one place.

```
/script           -> script-writer agent   -> script_check.py
/review-script    -> script-reviewer agent -> script_check.py
/validate, /open-items                     -> script_check.py
/tour-data                                 -> verify_tours.py (compares tours.json with the live site)
/tokens                                    -> transcript_report.py
```

- The writer agent follows `.claude/skills/scriptcraft/SKILL.md`, runs `script_check.py` for limits (`--limits`), for one tour's facts (`--tour`) and for the check itself (`--brief`, then `--final`), and saves the script and its notes file.
- The reviewer agent reruns the validator itself, then opens each source named in the script's facts table.
- The validator reads `tiers.json` (limits) and `brand_rules.json` (brand rules) from its own folder. It opens `tours.json` only for `--tour`. A normal check does not compare a script's numbers with `tours.json`. The writer builds the facts table from the `--tour` output, and the reviewer checks each row against its source.
- `verify_tours.py` is the only thing that compares `tours.json` with the live site, so it needs network access.
- Every command and agent finds repo files through ROOT: `${CLAUDE_PLUGIN_ROOT}` when installed as a plugin, or the current folder in a clone. Files they save for you go in the current folder, never under ROOT.
