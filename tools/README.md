# Tools

This page is for contributors who run or change the repo checks. It covers the three files in this folder: the integrity test, the token report and the npx launcher. The folder uses only the Python standard library and Node built-ins.

## test_repo_integrity.py

This is the second of the two main test suites. It checks the commands, agents, plugin manifests, licences, packaging, public repo rules and docs links. Run it from the repo root:

```
python3 -I tools/test_repo_integrity.py
```

The last lines show how many tests ran and whether they passed. A failing run exits with a non-zero code. The `-I` flag keeps Python from importing modules from the current folder, so a stray file cannot shadow a standard library module. The Packaging tests need Node and skip without it.

The other test commands, the live tour data check and the supported Python versions are in [CONTRIBUTING.md](../CONTRIBUTING.md#run-the-tests) and [installation.md](../docs/installation.md#prerequisites).

## transcript_report.py

This script reads one Claude Code session transcript and shows where the context went. The `/tokens` command runs it, and the [token hygiene guide](../docs/token-hygiene.md) explains how to act on the numbers.

```
python3 -I tools/transcript_report.py [PATH/TO/SESSION.jsonl]
```

Without a path, it reads the most recently written transcript under `~/.claude/projects`. Transcripts are chat logs. They never belong in this repo, and `.gitignore` blocks `*.jsonl`.

The report prints:

- model calls and compactions
- context per call: median, mean, max and total
- cache read, cache write, hit ratio and output
- the share of calls and of all context read above 150k and 200k tokens
- the fixed part sent on every call (system prompt and tool definitions), by source and by largest tools
- re-injections
- the entry kinds that are re-read most
- subagent runs

Sizes are estimates at 4 characters per token, and each image counts as 1,600 tokens. The script exits with a message when it finds no transcript or no model calls. Given more than one argument, it prints the usage text.

`/tokens` runs the script with no path and turns the output into three lines on the biggest drivers and one change that would cut them. It advises compacting when the median context per call is above 150k tokens.

## outdoornorway-cli.js

This is the launcher behind `npx` and `npm run`. It needs Node 18 or newer, as `engines` in `package.json` sets, and it never writes files. Run it from a clone:

```
node tools/outdoornorway-cli.js <command> [flag]
```

`npm run doctor` and `npm test` call it too. Without a clone, run it from GitHub:

```
npx github:Sameersexy/outdoornorway doctor
```

npx reads the default branch of the repo, so the launcher runs this way only once it is on that branch. [VERIFY: confirm npx runs the bin from a GitHub spec]

| Command | Flags | What it does |
|---|---|---|
| `doctor` | none | Checks Node, `python3`, the Claude Code CLI, the required plugin files and the version numbers. Prints `[ok]`, `[warn]` or `[fail]` for each check. |
| `install` | `--run` | Prints the two plugin install commands and a note to restart. With `--run`, it runs them from the repo folder. |
| `update` | `--run` | Prints the two update commands. With `--run`, it runs them from the repo folder. |
| `test` | `--all` | Runs the validator tests and the integrity tests with `python3`. With `--all`, it also runs the adquill linter tests. |
| `version` | none | Prints the version in `package.json`. Also `--version` and `-v`. |
| `help` | none | Prints the usage text. Also `--help` and `-h`. With no command, the launcher prints the usage text. |

The commands that `install` and `update` print are in [installation.md](../docs/installation.md).

Behaviour notes:

- `doctor` warns when Node is older than 18 or the Claude Code CLI is missing. It fails when `python3` is missing, a required file is missing, or the versions in `package.json`, `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` differ. A failure sets exit code 1. Warnings leave it at 0.
- `install --run` and `update --run` need the Claude Code CLI. Without it, they print an error and exit 1. The steps run in order, and the first failing step stops the run.
- `test` needs `python3`. Without it, it prints a message and exits 1.
- An unknown command prints an error and the usage text to stderr, then exits 1.
- With `--run`, the `claude` CLI changes Claude Code's plugin settings. The test steps can create `__pycache__` folders, which git ignores and `package.json` leaves out of the npm package.

## Where to go next

The [repo map](../docs/repo-map.md) says why the three files here must not move. [publishing-to-npm.md](../docs/publishing-to-npm.md) covers publishing the launcher.
