# Docs index

This page is for anyone looking for a guide in this repo. It lists every file and folder in `docs/`, who each one is for, and when to read it. For a folder-by-folder map of the whole repo, read [repo-map.md](repo-map.md).

## Start here

| If you want to... | Read |
|---|---|
| Write or edit a video script with Claude Code (no coding needed) | [getting-started.md](getting-started.md) |
| Install the plugin, clone the repo or run it with npx | [installation.md](installation.md) |
| Find out what is in each folder and which paths must not move | [repo-map.md](repo-map.md) |
| See which skills are ours, which are vendored and which live only on the account | [skills-catalog.md](skills-catalog.md) |

## Guides

| File | For | What it covers |
|---|---|---|
| [getting-started.md](getting-started.md) | Writers and video editors | Quick start, one-time set up, separate sections for writers and editors, who does what, what to do when something goes wrong |
| [installation.md](installation.md) | Anyone installing | Three install routes (plugin, clone, npx), updating, checking the install |
| [repo-map.md](repo-map.md) | Maintainers | Every folder, what it is for, what breaks if it moves |
| [skills-catalog.md](skills-catalog.md) | Maintainers | Own skills, vendored third-party skills, account-only skills (names only) |
| [backup-and-restore.md](backup-and-restore.md) | The account owner | What is backed up, where it lives, how to restore it on a new account |
| [publishing-to-npm.md](publishing-to-npm.md) | Maintainers | How to check the package and publish it to npm from your own npm account |
| [token-hygiene.md](token-hygiene.md) | Anyone running long Claude Code sessions | Why sessions get expensive, what changed in the repo, and the habits that cut the most |

## Folders

| Folder | What it holds |
|---|---|
| [research/](research/) | Sourced research behind the skills: ad copy (adquill, paused) and video scripts (scriptcraft). Has its own index in [research/README.md](research/README.md) |
| [script-skill-reviews/](script-skill-reviews/) | Reviews and test write-ups of the scriptcraft skill. Has its own index in [script-skill-reviews/README.md](script-skill-reviews/README.md) |
| [archive/](archive/) | Old handoff notes kept for history. Nothing in the repo depends on them |

## Other places to look

- Rules for contributors: [../CONTRIBUTING.md](../CONTRIBUTING.md)
- What changed and when: [../CHANGELOG.md](../CHANGELOG.md)
- Project rules for Claude Code: [../CLAUDE.md](../CLAUDE.md)
- Folder READMEs: [../tools/README.md](../tools/README.md), [../content/scripts/README.md](../content/scripts/README.md), [../campaigns/ski-meta-ads/README.md](../campaigns/ski-meta-ads/README.md), [../adquill/README.md](../adquill/README.md)

## Keeping this index current

Add a line here whenever you add a file or folder to `docs/`. The repo integrity test fails if a docs file or folder is not mentioned on this page.
