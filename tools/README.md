# Tools

For contributors who run or change the repo checks: what each file in this folder does and how to run it. The folder holds two Python files, which use only the standard library, and one Node launcher, which uses Node built-ins only.

## test_repo_integrity.py

This is the second of the two main suites. It checks the commands, agents, plugin manifests, licences, packaging, public repo rules and docs links. Run it from the repo root:

```
python3 -I tools/test_repo_integrity.py
```

The last lines show how many tests ran and whether they passed. A failing run exits with a non-zero code. The `-I` flag keeps Python from importing modules from the current folder, so a stray file cannot shadow a standard library module.

The main suites pass on Python 3.11, 3.12 and 3.13. [VERIFY: lowest Python 3 version; adquill's own docs state 3.9 or newer]

What each test class guards:

| Class | What it guards |
|---|---|
| Manifests | `plugin.json` and `marketplace.json` agree on name and version. The licence is MIT. The commands, skills and agents paths exist. |
| Commands | The seven slash commands exist, each with a description and `disable-model-invocation: true`. No command line uses `${`. Script commands use no bare repo paths. `/howto` matches the Quick start in the guide. Each command is listed in the guide and the README. |
| Agents | Each agent has a "Where files live" section and pins no model. |
| Licences | Each third-party skill listed in `THIRD_PARTY_SKILLS.md` has a licence file. Each skill folder is listed there, except `scriptcraft`. |
| Hygiene | Text files have no em or en dash, no emoji, no local scratch path and no model name. The guide has no link placeholders and names the install pages. The guide does not say the repo is private. |
| TranscriptReport | The token report runs on a made-up session. It counts calls, reports the cache hit ratio, skips bad lines and counts an image as a fixed cost. |
| Packaging | `package.json`, the plugin and the marketplace agree on name and version. The launcher has a Node shebang. `package.json` has no dependencies. Every `files` entry exists. The launcher prints its version and install commands and rejects unknown commands. These tests need Node and skip without it. |
| PublicRepoGuards | No transcript, archive, `.env` or `node_modules` file is tracked. `.gitignore` lists the same patterns. No email address or secret-like string appears in the text files. |
| Navigation | The navigation docs exist, this file included. Relative links resolve. Backticked repo paths exist. `docs/README.md` mentions every guide and folder. The root README links the install and map docs. The README has no hand-written test or rule counts. `CLAUDE.md` points at the repo map. The old handoff path is gone. |

The live data check, `campaigns/ski-meta-ads/verify_tours.py`, needs network access and is not part of `test`. See the [campaign folder README](../campaigns/ski-meta-ads/README.md).

## transcript_report.py

This script reads one Claude Code session transcript and shows where the context went. The `/tokens` command runs it. The [token hygiene guide](../docs/token-hygiene.md) covers the habits that cut context and the fixed part sent on every call.

Usage, from the script's docstring:

```
python3 -I tools/transcript_report.py [PATH/TO/SESSION.jsonl]
```

Without a path, it reads the most recently written transcript under `~/.claude/projects`. Transcripts are chat logs. They never belong in this repo, and `.gitignore` blocks `*.jsonl`.

The `/tokens` command runs the script with no path. It turns the output into three lines on the biggest drivers and one change that would cut them. The command advises compacting when the median context per call is above 150k tokens. The command describes its output as counts only.

The report prints:

- model calls and compactions
- context per call: median, mean, max and total
- cache read, cache write, hit ratio and output
- the share of calls and of all context read above 150k and 200k tokens
- the fixed part sent on every call (system prompt and tool definitions), by source and by largest tools
- re-injections
- the entry kinds that are re-read most
- subagent runs

Sizes are estimates at 4 characters per token, and each image counts as 1,600 tokens. The script uses only the standard library. It exits with a message when it finds no transcript or no model calls. Given more than one argument, it prints the usage text.

Do not move this file. `/tokens` runs it by path, and the TranscriptReport test loads it by path.

## outdoornorway-cli.js

This is the launcher for the plugin. It needs Node 18 or newer, as set in `engines` in `package.json`. It uses Node built-ins only and never writes files. The launcher was run on Node 22.

Run it from a clone:

```
node tools/outdoornorway-cli.js <command> [flag]
```

The package scripts call it too: `npm run doctor` and `npm test`.

Without a clone, from GitHub:

```
npx github:Sameersexy/outdoornorway doctor
```

npx reads the default branch of the repo, so this works only once the change set is merged there. [VERIFY: confirm npx runs the bin from a GitHub spec]

Commands and flags:

| Command | Flags | What it does |
|---|---|---|
| `doctor` | none | Checks Node, `python3`, the Claude Code CLI, the required plugin files and the version numbers. Prints `[ok]`, `[warn]` or `[fail]` for each check. |
| `install` | `--run` | Prints the two Claude Code commands and a note to restart. With `--run`, it runs the commands from the repo folder. |
| `update` | `--run` | Prints the two update commands. With `--run`, it runs them from the repo folder. |
| `test` | `--all` | Runs the validator tests and the integrity tests with `python3`. With `--all`, it also runs the adquill linter tests. |
| `version` | none | Prints the version in `package.json`. Also `--version` and `-v`. |
| `help` | none | Prints the usage text. Also `--help` and `-h`. With no command, the launcher prints the usage text. |

The `install` command prints these Claude Code commands. `--run` executes them:

```
claude plugin marketplace add Sameersexy/outdoornorway
claude plugin install outdoornorway-marketing@outdoornorway
```

The `update` command prints these:

```
claude plugin marketplace update outdoornorway
claude plugin update outdoornorway-marketing@outdoornorway
```

Behaviour notes:

- `doctor` warns when Node is older than 18 or the Claude Code CLI is missing. It fails when `python3` is missing, a required file is missing, or the versions in `package.json`, `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` differ. A failure sets exit code 1. Warnings leave the exit code at 0.
- `install --run` and `update --run` need the Claude Code CLI. Without it, they print an error and exit 1. The steps run in order. The first failing step stops the run and sets the exit code.
- `test` needs `python3`. Without it, it prints a message and exits 1.
- Other arguments are ignored. An unknown command prints an error and the usage text to stderr, then exits 1.
- The launcher never writes files. With `--run`, the `claude` CLI changes Claude Code's plugin settings. The test steps can create `__pycache__` folders.
- Git ignores `__pycache__` folders, and `package.json` leaves them out of the npm package.

## Paths that must not move

- `tools/outdoornorway-cli.js`: `package.json` names it in `bin`, and in the `doctor` and `test` scripts. The launcher finds the repo root as the folder above `tools/`.
- `tools/transcript_report.py`: `.claude/commands/tokens.md` runs it by path. Moving it breaks `/tokens`.
- `tools/test_repo_integrity.py`: `CLAUDE.md`, `README.md` and the launcher's `test` step name it. The file also finds the repo root as the folder above `tools/`.
- `tools/README.md`: the Navigation tests check that it exists at this path.

## Related

- [Installation](../docs/installation.md)
- [Token hygiene](../docs/token-hygiene.md)
- [Publishing to npm](../docs/publishing-to-npm.md)
- [Repo map](../docs/repo-map.md)
