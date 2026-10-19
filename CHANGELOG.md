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
- `.gitignore` entries for `*.jsonl`, `*.zip`, `*.tgz`, `.env`, `.env.*`, `node_modules/`, `backup/` and `exports/`.

### Changed

- [README.md](README.md) and [CLAUDE.md](CLAUDE.md) updated.
- The handoff note moved to the archive: [docs/archive/handoff-next-session.md](docs/archive/handoff-next-session.md).

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
