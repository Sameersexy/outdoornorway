# Repo map

This page is for anyone who has just opened the repo and wants to know where things are and what is safe to change.

## Start here

The repo is a Claude Code plugin (`outdoornorway-marketing`) plus the files it works on. The plugin is the whole repo: `marketplace.json` points its `source` at `./`. Writers use slash commands to draft and check video scripts for Outdoor Norway. Tour prices and dates live in one data file. A handful of paths are written into code, tests and manifests, so those folders stay where they are.

If you write scripts, read [getting-started.md](getting-started.md). If you change the tools, read [CONTRIBUTING.md](../CONTRIBUTING.md) first. Come back here when you need a path. The full docs index is [README.md](README.md).

## Tree

```
outdoornorway/  # repo root
|-- .claude/  # project files for Claude Code
|   |-- agents/  # script-writer and script-reviewer [fixed]
|   |-- commands/  # slash commands [fixed]
|   |-- skills/  # video script skill and vendored skills [fixed]
|   |   |-- scriptcraft/  # video script skill
|   |   |   |-- assets/  # templates and intake forms
|   |   |   |-- examples/  # fictional sample scripts and briefs
|   |   |   |-- references/  # guides the skill reads
|   |   |   |-- scripts/  # script_check.py, tiers.json, brand_rules.json, tests
|   |   |   `-- SKILL.md  # skill instructions
|   |   `-- (vendored third-party skills)  # listed in docs/skills-catalog.md
|   |-- product-marketing.md  # brand facts and do-not-claim list
|   `-- settings.json  # project settings for a clone [fixed]
|-- .claude-plugin/  # plugin.json and marketplace.json [fixed]
|-- adquill/  # paused ad-copy skill and agents (drafts)
|   |-- agents/  # paused agents
|   |-- skills/  # paused ad-copy skill
|   |-- AGENTS.md  # instructions for coding agents
|   `-- README.md  # says the skill is paused
|-- campaigns/  # tour data and ski ad notes
|   `-- ski-meta-ads/  # tours.json, its checker and ad notes [fixed]
|-- content/  # finished and draft scripts
|   `-- scripts/  # scripts, each with a notes file
|-- docs/  # guides, research and review history
|   |-- archive/  # retired notes
|   |   `-- handoff-next-session.md  # old handoff note
|   |-- research/  # research behind the skills
|   |   |-- ad-copy/  # ad copy research
|   |   |-- video-scripts/  # video script research
|   |   `-- README.md  # research notes
|   |-- script-skill-reviews/  # how the script skill was reviewed
|   |   |-- e2e-agent-tests.md  # end-to-end agent tests
|   |   |-- README.md  # index of review rounds
|   |   |-- round-1-creative.md  # round 1, creative
|   |   |-- round-1-direct-response.md  # round 1, direct response
|   |   `-- round-1-editorial.md  # round 1, editorial
|   |-- backup-and-restore.md  # what to save and how to restore it
|   |-- getting-started.md  # guide for writers and editors [fixed]
|   |-- installation.md  # install, check, update and remove
|   |-- publishing-to-npm.md  # publish the launcher to npm
|   |-- README.md  # docs index
|   |-- repo-map.md  # this page
|   |-- skills-catalog.md  # what each skill is for
|   `-- token-hygiene.md  # token tips [fixed]
|-- tools/  # integrity test, token report and npx launcher [fixed]
|   |-- outdoornorway-cli.js  # npx launcher
|   |-- README.md  # guide to the tools
|   |-- test_repo_integrity.py  # integrity test
|   `-- transcript_report.py  # token report for /tokens
|-- .gitignore  # keeps caches and local files out of git [fixed]
|-- CHANGELOG.md  # what changed in each version
|-- CLAUDE.md  # rules for Claude Code in this repo [fixed]
|-- CONTRIBUTING.md  # how to change the tools
|-- LICENSE  # MIT licence [fixed]
|-- package.json  # launcher metadata [fixed]
|-- README.md  # front page [fixed]
`-- THIRD_PARTY_SKILLS.md  # sources and licences of vendored skills [fixed]
```

[fixed] = the Safe to move? column says No or keep in place. Git and cache folders are left out.

## Folders

| Path | What it holds | Who uses it | Safe to move? |
|---|---|---|---|
| `.claude-plugin/` | `plugin.json` and `marketplace.json`: plugin name, version and which folders ship | The plugin install, the integrity test, `doctor` in the launcher | No. The test and `doctor` open both files by path. |
| `.claude/commands/` | The slash commands (`/script`, `/validate` and the rest) | The plugin, the integrity test | No. `plugin.json` names this folder and the test reads every file in it. |
| `.claude/agents/` | `script-writer.md` and `script-reviewer.md` | `/script` and `/review-script` | No. `plugin.json` lists both files by path. |
| `.claude/skills/` | `scriptcraft` (the video script skill, its validator and tests) and the vetted third-party skills | The plugin, the commands, the agents | No. `plugin.json` names the folder. The commands and agents call `.claude/skills/scriptcraft/scripts/script_check.py`, and that script finds `tours.json` by going up four folders from its own folder. |
| `.claude/product-marketing.md` | Brand context, confirmed facts and the do-not-claim list | The copy skills and both agents | Avoid. The agents and the script notes cite this path as a source of facts. |
| `.claude/settings.json` | Project settings for a clone: enabled plugins and the auto-compact window | Claude Code, when you work in a clone | Keep it here, since Claude Code reads project settings from this path. |
| `campaigns/ski-meta-ads/` | `tours.json` (prices, dates, day-by-day plans), its checker and the ski ad copy notes. See [its README](../campaigns/ski-meta-ads/README.md). | The validator (`--tour`), `/tour-data`, `doctor`, both agents | No. `script_check.py` builds the path `campaigns/ski-meta-ads/tours.json` from the repo root, so a move breaks `--tour` (unless you pass `--tours-file`). `doctor` lists the file as required. |
| `content/scripts/` | Finished and draft scripts, each with a notes file. See [its README](../content/scripts/README.md). | `/script` writes here by default | Only with edits. The writer agent's default save path and the guides name this folder. |
| `docs/` | Guides, token tips, research, review history. See [README.md](README.md). | `/howto`, `/tokens`, the integrity test | Partly. Keep `docs/getting-started.md` and `docs/token-hygiene.md` in place, because a command and the test name them. Other files can move if you fix every link to the old path. |
| `docs/archive/` | Retired notes, such as the old handoff note | Nobody at run time | Yes. Nothing loads it. |
| `tools/` | The integrity test, the token report and the npx launcher. See [its README](../tools/README.md). | `/tokens`, the tests, `package.json` | No. `/tokens` and the `bin` entry in `package.json` name the files, and both Python and Node code find the repo root as the folder above `tools/`. |
| `adquill/` | A paused ad-copy skill and three agents (drafts). See [its README](../adquill/README.md). | Nothing at run time. The script skill review notes cite its agents, and the launcher's `test --all` runs its linter tests. | Only with edits. The plugin does not install it. A move means updating `files` in `package.json`, the `--all` path in the launcher and the links in the docs. |

## Files at the top level

| Path | What it holds | Who uses it | Safe to move? |
|---|---|---|---|
| `README.md` | The front page: install, commands, what is here | Everyone | No. The integrity test reads it. |
| `CLAUDE.md` | Rules and commands for Claude Code working in this repo | Claude Code, in a clone | Keep at the root. The plugin does not ship it. |
| `CONTRIBUTING.md` | How to change the tools and send a pull request. See [CONTRIBUTING.md](../CONTRIBUTING.md). | Contributors | Yes, if you fix the links. |
| `CHANGELOG.md` | What changed in each version. See [CHANGELOG.md](../CHANGELOG.md). | Maintainers | Yes, if you fix the links. |
| `LICENSE` | The MIT licence for this repo | The integrity test | No. The test reads it by path. |
| `THIRD_PARTY_SKILLS.md` | Source, pinned commit and licence of each third-party skill | The integrity test, anyone checking a licence | No. The test checks every listed skill has its licence file, and every skill folder is listed or original. |
| `package.json` | Package metadata for the launcher: `bin`, `files`, Node `engines`, no dependencies | npm, `npx`, the integrity test | No. Keep it at the root. Its `version` must match `plugin.json` and `marketplace.json`. |
| `.gitignore` | Keeps Python caches, transcripts (`*.jsonl`), archives (`*.zip`, `*.tgz`), `.env` files, `node_modules/`, `backup/` and `exports/` out of git | Git, the integrity test | No. The test checks that the main patterns are listed. |

Chat transcripts and account-only skills are not in this repo. They go in a separate private backup repository (`<your-private-backup-repo>`). [backup-and-restore.md](backup-and-restore.md) has the steps.

## Where do I find...

| I want | Go to |
|---|---|
| A finished or draft script | `content/scripts/`. Each script has a notes file beside it. |
| Tour prices, dates and day-by-day plans | `campaigns/ski-meta-ads/tours.json`. To print one tour, run `python3 -I .claude/skills/scriptcraft/scripts/script_check.py --tour ski-aurora-7day`. A wrong id prints the list of valid ids. |
| The validator | `.claude/skills/scriptcraft/scripts/script_check.py`. Its limits are in `tiers.json` and its brand rules in `brand_rules.json`, both in the same folder. |
| The slash commands | `.claude/commands/`. The list with one line each is in the root [README](../README.md). |
| The agents | `.claude/agents/` (`script-writer.md` and `script-reviewer.md`) |
| Brand facts and the do-not-claim list | `.claude/product-marketing.md` |
| Third-party skills and their licences | `THIRD_PARTY_SKILLS.md`, and the `LICENSE-*` file inside each skill folder under `.claude/skills/`. [skills-catalog.md](skills-catalog.md) says what each skill is for. |
| Install, update or uninstall the plugin | [installation.md](installation.md) |
| Back up or restore transcripts and account-only skills | [backup-and-restore.md](backup-and-restore.md) |
| Publish the launcher to npm | [publishing-to-npm.md](publishing-to-npm.md) |
| Test commands | The block under [Test and check commands](#test-and-check-commands) |
| Token tips | [token-hygiene.md](token-hygiene.md), the `/tokens` command, and the Tokens section of `CLAUDE.md` |
| How the script skill was reviewed | [script-skill-reviews/README.md](script-skill-reviews/README.md) |
| Research behind the skills | `docs/research/` |
| The paused ad-copy skill | [adquill/README.md](../adquill/README.md) |

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

## Test and check commands

```
python3 -I .claude/skills/scriptcraft/scripts/test_script_check.py
python3 -I tools/test_repo_integrity.py
python3 -I adquill/skills/adquill/scripts/test_slop_lint.py
python3 -I campaigns/ski-meta-ads/verify_tours.py
```

The first two are the main suites. The third covers the paused adquill linter. The fourth needs network access. If Node is installed, `node tools/outdoornorway-cli.js test` runs the first two and adds the third with `--all`.

## What is safe to change

- Add scripts and notes under `content/scripts/`. Edit prose docs freely, and run the integrity test afterwards.
- Change a price or a date in `tours.json` only after the owner confirms it, then run `verify_tours.py`.
- After editing the Quick start in `docs/getting-started.md`, regenerate `.claude/commands/howto.md`. The integrity test checks the two match.
- Do not add `!` shell lines with `${...}` or bare repo paths to a command. Commands reach files through ROOT.
- When you change the tools, bump `version` in `plugin.json`, `marketplace.json` and `package.json` together, so installed copies update.
- The repo is public and MIT licensed. Do not add supplier terms, personal data or private client information.
