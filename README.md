# outdoornorway

This repo is for the Outdoor Norway writers, editors and maintainers who use Claude Code. It holds marketing tools: a video script skill with an enforced validator, two agents, slash commands and vetted copywriting skills.

This repo is public and specific to Outdoor Norway. It is MIT licensed (see [Licence](#licence)).

Writers and video editors: start with [docs/getting-started.md](docs/getting-started.md), or run `/howto` (with the plugin, `/outdoornorway-marketing:howto`) in Claude Code.

Looking for something else? The [docs index](docs/README.md) lists every guide, the [repo map](docs/repo-map.md) explains each folder, and [CONTRIBUTING.md](CONTRIBUTING.md) covers how to change things.

## Install

Pick one of three routes. All need [Claude Code](https://code.claude.com/docs/en/quickstart) and [Python 3](https://www.python.org/downloads/) (the validator is a Python script, run as `python3`). The npx route also needs [Node.js](https://nodejs.org/) 18 or newer. Longer steps and troubleshooting are in [docs/installation.md](docs/installation.md).

**Plugin (works from any folder).** In a terminal:

```
claude plugin marketplace add Sameersexy/outdoornorway
claude plugin install outdoornorway-marketing@outdoornorway
```

Restart Claude Code. The commands carry the plugin name: `/outdoornorway-marketing:script`, `/outdoornorway-marketing:validate` and so on. Scripts are saved in the folder where you run Claude Code. Update with `claude plugin marketplace update outdoornorway` and `claude plugin update outdoornorway-marketing@outdoornorway`.

**Clone (best for editing the tools or sending pull requests).**

```
git clone https://github.com/Sameersexy/outdoornorway.git
cd outdoornorway
claude
```

The commands then have short names (`/script`, `/validate`) and the skills and agents in `.claude/` load on their own. Update with `git pull`.

**npx (checks your set up and prints the install commands, no clone, but only once the launcher is on the default branch; it is not on npm yet).**

```
npx github:Sameersexy/outdoornorway doctor
npx github:Sameersexy/outdoornorway install
```

`doctor` checks Node, Python 3, the Claude Code CLI and the repo files. `install` prints the two plugin commands and runs them only when you add `--run`. npx reads the repo's default branch, so the launcher must be on that branch. The package is not on the npm registry yet: see [docs/publishing-to-npm.md](docs/publishing-to-npm.md).

## Slash commands

| Command | What it does |
|---|---|
| `/script <tour or topic> <platform> [style]` | Writes a script with the script-writer agent, saves it to `content/scripts/`, validates it, and returns a short result |
| `/review-script <file>` | Independent review by the script-reviewer agent: facts, voice, authenticity, the top fixes and a verdict |
| `/validate <file> [--final] [--strict]` | Runs the validator and shows only the findings |
| `/open-items <file>` | Lists every `[VERIFY]` placeholder and unverified fact row, grouped by who confirms it |
| `/howto` | Shows the quick start for writers and editors |
| `/tour-data` | Checks `campaigns/ski-meta-ads/tours.json` against the live site |
| `/tokens` | Shows where this session's tokens went |

The commands run only when you type them.

## What is here

```
outdoornorway/
|-- .claude/               [fixed]  commands, agents and skills for Claude Code
|-- .claude-plugin/        [fixed]  plugin and marketplace manifests
|-- account-skills/                 account skills, not loaded by the plugin
|-- adquill/                        paused ad-copy skill, not installed by the plugin
|-- campaigns/             [fixed]  tour data and ski ad notes
|-- content/               [fixed]  finished and draft video scripts
|-- docs/                  [fixed]  guides, research and review history
|-- tools/                 [fixed]  tests, token report and npx launcher
|-- .gitignore             [fixed]  keeps caches, .env files and transcripts out of git
|-- CHANGELOG.md                    what changed and when
|-- CLAUDE.md              [fixed]  rules for Claude Code in this repo
|-- CONTRIBUTING.md                 how to change the tools
|-- LICENSE                [fixed]  MIT licence
|-- package.json           [fixed]  launcher metadata
|-- README.md              [fixed]  front page
`-- THIRD_PARTY_SKILLS.md  [fixed]  sources and licences of vendored skills
```

[fixed] marks a path that must not move. The [repo map](docs/repo-map.md) says why for each one and lists what sits inside every folder. Each folder has its own guide:

- [docs index](docs/README.md) for every guide
- [research notes](docs/research/README.md) and [script skill reviews](docs/script-skill-reviews/README.md) for the sources and review history
- [tools guide](tools/README.md) for the tests, token report and launcher
- [script folder guide](content/scripts/README.md) for finished and draft scripts
- [ski ads guide](campaigns/ski-meta-ads/README.md) for tour data and ad notes
- [account skills guide](account-skills/README.md) for the three account skills
- [adquill guide](adquill/README.md) for the paused ad-copy skill

The [skills catalog](docs/skills-catalog.md) separates our own skills from the vendored ones. The [changelog](CHANGELOG.md) lists what changed and when.

## Tests

```
python3 -I .claude/skills/scriptcraft/scripts/test_script_check.py
python3 -I tools/test_repo_integrity.py
```

Each run prints how many tests ran, so this page carries no counts that go stale. The first covers the validator. The second covers the commands, plugin files, licences, the guide, the npm package, the docs links and the public repo guards. With Node installed, `npm test` runs both. The other checks are in [CONTRIBUTING.md](CONTRIBUTING.md#run-the-tests).

## Backup and restore

Git holds the code. It does not hold your chat history, the skills that live only on the Claude account, connector sign-ins or local Claude Code sessions. The three account skills in `account-skills/` are the exception. [docs/backup-and-restore.md](docs/backup-and-restore.md) lists what to save, where it goes and how to restore it on a new account.

## Licence

MIT, see `LICENSE`. This covers the files in this repo. It does not grant any right to use the Outdoor Norway name or logos. The third-party skills copied into `.claude/skills/` keep their own MIT licences: see `THIRD_PARTY_SKILLS.md` and the `LICENSE-*` file inside each skill folder.
