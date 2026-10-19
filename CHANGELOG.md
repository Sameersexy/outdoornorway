# Changelog

This file answers one question: what changed in this repo, and when. It follows the Keep a Changelog style. The commits carry no version numbers, so entries are grouped by date and milestone. `git log --format='%h %ad %s' --date=short` lists every commit.

The plugin and marketplace manifests have carried version 0.2.0 since `8d7effb` on 12 October 2026, and `package.json` matches it.

## [Unreleased]

### Added

- Navigation docs: [docs/README.md](docs/README.md) (guide index), [docs/repo-map.md](docs/repo-map.md) (folder map) and [docs/skills-catalog.md](docs/skills-catalog.md).
- Folder README files for `adquill/`, `campaigns/ski-meta-ads/`, `content/scripts/`, `docs/script-skill-reviews/` and `tools/`.
- [Install guide](docs/installation.md), [backup and restore guide](docs/backup-and-restore.md), [publishing guide](docs/publishing-to-npm.md) and [CONTRIBUTING.md](CONTRIBUTING.md).
- `package.json` with zero dependencies, a bin named `outdoornorway`, and Node 18 or newer in `engines`.
- `tools/outdoornorway-cli.js`, a launcher with `doctor`, `install`, `update`, `test`, `version` and `help` commands. `install` and `update` print the Claude Code commands and run them only with `--run`. `test --all` adds the adquill tests. The launcher never writes files.
- Guard-rail tests in `tools/test_repo_integrity.py`.
- A test in `tools/test_repo_integrity.py` that bans GPT model names in our own files.
- `.gitignore` entries for `*.jsonl`, `*.zip`, `*.tgz`, `.env`, `.env.*`, `node_modules/`, `backup/` and `exports/`.
- [account-skills/](account-skills/README.md): two screened account skills, `brand-voice-checker` and `script-writing`, one folder each, with a guide. The plugin does not load them.

### Changed

- [README.md](README.md) and [CLAUDE.md](CLAUDE.md) updated.
- Python 3.9 or newer is the stated minimum, in the [installation guide](docs/installation.md) and the [adquill README](adquill/README.md).
- Some open items closed in the installation, adquill, npm and backup guides. The ski ads guide explains why no file numbered 02 exists.
- The validator tests run most attack cases in one process and keep one real child process for each expected outcome. The suite takes 3.7 s instead of 5.3 s (median of 7 runs).
- The adquill tests call `main()` in the same process for most command line cases and keep five real child processes. The suite takes 1.0 s instead of 2.3 s.
- `tools/test_repo_integrity.py` walks the repo once and shares the file list between its scan tests, which saves about 0.1 s.
- `outdoornorway test` starts the suites together and prints their output in the old order with the same exit codes. On a 4 core machine `test` takes 4.0 s instead of 6.1 s and `test --all` 4.2 s instead of 8.2 s.

### Fixed

- `/review-script`, the script-reviewer agent and the guides now say the review gives the top three fixes. They said five.
- `adquill/AGENTS.md` and the adquill README no longer say to install it as a plugin, because it is paused.
- The skills catalog no longer assigns a privacy screen result to each account-only skill, because the repo holds no record of one. The backup guide, the repo map and CONTRIBUTING.md now agree on where the private copies live.
- The backup guide covers the npm login, and says the restore dry run needs the branch that carries the launcher until it is merged.
- The repo map marks `docs/` as a path that must not move, and the adquill README links every file in the folder and names two reference files that the adquill `SKILL.md` and `adquill/AGENTS.md` cite but the repo does not hold.
- Stray working-note wording removed from the research notes and the token hygiene guide, two table rows with unescaped pipes fixed, and three open markers in the guides rewritten as plain statements or as `[VERIFY: what, who]`.
- The restore dry run in the backup guide now uses one clone and a `git switch` to the launcher branch. A second clone into the same folder failed. The guide also says the token report does not list subagent runs that a workflow started.
- The npm guide and the tools guide say the installed package leaves out `account-skills/` and `.gitignore`, so `outdoornorway test` needs a clone. `doctor` works in both.
- The repo map and CONTRIBUTING.md call the private backup a backup kept outside this repo and no longer call it a repository. CONTRIBUTING.md also says where screened account skills sit.
- Research notes: a company phone number and an AI model name removed, a note added that the ad-copy notes use the earlier name adwright, and the round 1 reviews say their test scripts are not kept here. The docs index says it lists every other file in `docs/`.

### Removed

- The retired handoff note, `docs/archive/handoff-next-session.md`, and its archive folder.

## 13 October 2026: command changes

### Added

- Handoff note for text-first scripts and the Claude chat package (#8, `257ea86`).

### Changed

- Thinner script commands, validator shortcuts and usage guidance (#7, `f4864d0`).

## 12 October 2026: plugin and onboarding

### Added

- Slash commands and an installable plugin, with validator `--brief` and `--open-items` options (`5dd7f5b`).
- Token hygiene: compact agent output, a session measurement tool and CLAUDE.md (`e166974`).
- Team onboarding: getting-started guide and `/howto` command (`54bbf08`).
- MIT licence added, and the plugin works outside a clone (`8d7effb`).

### Changed

- Commands show real paths to the user instead of ROOT (`3641622`).
- Guide and README add the Claude Code and Python install links (`c8d1663`).
- Guide lists Python 3 as a prerequisite (`3b5d40a`).
- Guide fixes the plugin troubleshooting line and explains three terms (`ade1c3c`).

### Fixed

- Public repo fixes from the audit (`f5c9342`).
- QA fixes and wider hygiene checks (`b650168`).
- Fixes from the three-part QA pass (`7a472f6`).

### Merged pull requests

- Pull requests #1 to #6 were merged on this day: `5301fe0`, `64bc5ee`, `8651edc`, `e03d977`, `b81390c`, `f76b71b`.

## 12 October 2026: YouTube scripts

### Added

- YouTube script for the 7 Day Northern Lights tour, a draft that needs guide and client input (`5789a3e`).
- Aurora YouTube script, with reviewer fixes and open-items notes (`1aa4966`).
- ugc_talk (guide to camera) version of the Northern Lights YouTube script, as a draft, and notes for it (`b963998`, `98b8ab1`).

### Changed

- scriptcraft treats a logistics line that points to the description as a soft call to action (`42db634`).

## 7 and 8 October 2026: scriptcraft skill and validator

### Added

- scriptcraft skill, validator and script agents, then the tier table and brand rules (`029e004`, `e7e79e1`).
- Panel review files and in-flight revisions (`7c2f3bb`), then the panel revision applied with regression attack cases added (`2dda9de`).
- Research notes kept in the repo (`1252066`).
- TikTok UGC style and creator briefs, with individual-creator research applied (`a527cd8`).
- Validator rules and checks from 8 October: chapter timestamps no longer count as numbers under the C06 YouTube chapters rule (`ac09ca8`); BR13 also blocks placeholders in visual cells under `--final` (`910b2bd`); F06 requires a quote when a row is verified yes from a brief (`bfc2d6f`); a shot-level near-copy check, a caption placeholders block in final and a relationship info line (`0d0cdef`); an R04 example-copy warning, an on-screen disclosure line (D01) and a thin-brief protocol (`cc5087d`).
- Guide intake form and end-to-end test results (`2f62cce`).
- tours.json: day-by-day itinerary for the five multi-day tours, checked against the live pages (`3eae9ea`).

## 6 and 7 October 2026: adquill drafts

### Added

- Initial commit (`1e4955f`).
- Ski ad data layer, reviewer personas and the Claude Code Setup plugin (`e047552`).
- Simplified ski copy generator, and the project renamed to adquill (`3554144`).
- Vetted copywriting skills and Outdoor Norway brand context (`951ae0e`).
- Review of a first-cut ski copy draft, with open questions (`d7609ec`).
- adquill skill drafts: the build workflow (`de4dbfc`), a second and third snapshot with platform references (`9f741be`, `29f0399`), and a snapshot after a usage-limit interruption with a linter draft (`56eee5f`).

### Changed

- adquill paused: a snapshot taken at the pause on 7 October (`8c77860`).
