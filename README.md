# outdoornorway

Marketing tools for Outdoor Norway, built for Claude Code: a video script skill with an enforced validator, two agents, slash commands and vetted copywriting skills.

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

**npx (checks your set up and prints the install commands, no clone).**

```
npx github:Sameersexy/outdoornorway doctor
npx github:Sameersexy/outdoornorway install
```

`doctor` checks Node, Python 3, the Claude Code CLI and the repo files. `install` prints the two plugin commands and runs them only when you add `--run`. The same launcher is packaged for npm as `outdoornorway-marketing`. It is not published to the npm registry yet: see [docs/publishing-to-npm.md](docs/publishing-to-npm.md).

Check the packaging with `claude plugin validate .` (it passes; its one warning says the repo's `CLAUDE.md` is not shipped inside the plugin, which is intended).

## Slash commands

| Command | What it does |
|---|---|
| `/script <tour or topic> <platform> [style]` | Writes a script with the script-writer agent, saves it to `content/scripts/`, validates it, and returns a short result |
| `/review-script <file>` | Independent review by the script-reviewer agent: facts, voice, authenticity, verdict, top five fixes |
| `/validate <file> [--final] [--strict]` | Runs the validator and shows only the findings |
| `/open-items <file>` | Lists every `[VERIFY]` placeholder and unverified fact row, grouped by who confirms it |
| `/howto` | Shows the quick start for writers and editors |
| `/tour-data` | Checks `campaigns/ski-meta-ads/tours.json` against the live site |
| `/tokens` | Shows where this session's tokens went |

The commands run only when you type them.

## What is here

```
outdoornorway/
|-- .claude/  # commands, agents and skills for Claude Code
|-- .claude-plugin/  # plugin and marketplace files [fixed]
|-- adquill/  # paused ad-copy skill, not installed by the plugin
|-- campaigns/  # tour prices, dates and ski ad notes
|-- content/  # finished and draft scripts
|-- docs/  # guides, research and review history
|-- tools/  # tests, token report and npx launcher [fixed]
|-- .gitignore  # keeps caches, .env files and transcripts out of git [fixed]
|-- CHANGELOG.md  # what changed in each version
|-- CLAUDE.md  # rules for Claude Code in this repo [fixed]
|-- CONTRIBUTING.md  # how to change the tools
|-- LICENSE  # MIT licence [fixed]
|-- package.json  # launcher metadata [fixed]
|-- README.md  # this page [fixed]
`-- THIRD_PARTY_SKILLS.md  # sources and licences of vendored skills [fixed]
```

[fixed] marks a path that must not move. Folder guides: the [docs index](docs/README.md), the [tools guide](tools/README.md) and the [adquill guide](adquill/README.md).

The [repo map](docs/repo-map.md) explains every folder and marks the paths that must not move, because the plugin and the validator rely on them. The [skills catalog](docs/skills-catalog.md) separates our own skills from the vendored ones.

## Tests

Run both. Each prints how many tests ran, so this page carries no counts that go stale.

```
python3 -I .claude/skills/scriptcraft/scripts/test_script_check.py
python3 -I tools/test_repo_integrity.py
```

The first covers the validator. The second covers the commands, plugin files, licences, the guide, the npm package, the docs links and the public repo guards. With Node installed, `npm test` runs both. `python3 -I adquill/skills/adquill/scripts/test_slop_lint.py` covers the paused adquill linter.

## Backup and restore

Git holds the code. It does not hold your chat history, the skills that live only on the Claude account, connector sign-ins or local Claude Code sessions. [docs/backup-and-restore.md](docs/backup-and-restore.md) lists what to save, where it goes and how to restore it on a new account.

## Licence

MIT, see `LICENSE`. This covers the files in this repo. It does not grant any right to use the Outdoor Norway name or logos. The third-party skills copied into `.claude/skills/` keep their own MIT licences: see `THIRD_PARTY_SKILLS.md` and the `LICENSE-*` file inside each skill folder.
