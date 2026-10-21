# Tools

This page is for contributors who run or change the repo checks. It covers the four files in this folder: the integrity test, the token report, the npx launcher and the skill packer. The folder uses only the Python standard library and Node built-ins.

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

## pack_skills.py

This script zips skills for upload to claude.ai, one zip per skill. The launcher runs it for `skills pack`. It needs Python 3.9 or newer. Run it from the repo root:

```
python3 -I tools/pack_skills.py [--out DIR] [--list] [NAME ...]
```

It packs every folder that has a `SKILL.md` under `account-skills/` and `.claude/skills/`, except `scriptcraft`. That skill needs the validator and `tours.json`, so it ships only in the plugin. With one or more names, it packs only those. An unknown name, or `scriptcraft`, prints the valid names and exits 1. `--list` prints the names and source folders and writes nothing.

- Each zip is `DIR/<skill>.zip`. `DIR` defaults to `dist/skills` and is resolved against the current folder. `.gitignore` lists `dist/`, so the zips stay out of git. The script refuses an `--out` folder inside `account-skills/` or `.claude/skills/`.
- Each zip holds one top folder named after the skill, so `<skill>/SKILL.md` is the instructions file. Entries are sorted, timestamps are fixed at 1980-01-01 and modes are 0644. `__pycache__` folders, `*.pyc` and `.DS_Store` are left out.
- Two runs give the same bytes on the same Python and zlib build. Compare the sha256 column to check.
- The script never changes the skill text. A symbolic link to a file or to a folder inside a skill folder stops the run with exit code 1.

It prints one line per zip: the name, the size in bytes, the first 12 characters of the sha256, and the length of the `description` in the front matter. A description over 200 characters gets the note `description over 200 characters`. The 200 character limit for a claude.ai upload is not confirmed [VERIFY: the owner confirms the limit with a test upload]. The note only warns. The zip still holds the full description.

## outdoornorway-cli.js

This is the launcher behind `npx` and `npm run`. It needs Node 18 or newer, as `engines` in `package.json` sets. It writes no files itself. The only files that appear come from `skills pack`, which writes zips into its `--out` folder. Run it from a clone:

```
node tools/outdoornorway-cli.js <command> [flag]
```

`npm run doctor` and `npm test` call it too. Without a clone, run it from GitHub:

```
npx github:Sameersexy/outdoornorway doctor
```

npx reads the default branch of the repo, so the launcher runs this way only once it is on that branch.

| Command | Flags and arguments | What it does |
|---|---|---|
| `list` | none | Lists each plugin in `.claude-plugin/marketplace.json` with its version, description and install line `claude plugin install NAME@outdoornorway`. |
| `install [NAME\|all]` | `--run` | Prints `claude plugin marketplace add SOURCE`, then one `claude plugin install NAME@outdoornorway` per plugin, and a note to restart. `NAME` defaults to `outdoornorway-marketing`. `all` means every plugin except `outdoornorway-copy-skills`, which is left out with a note because the default plugin already carries those skills and both together list each skill twice. With `--run`, it runs the steps from the repo folder. |
| `update [NAME\|all]` | `--run` | Prints `claude plugin marketplace update outdoornorway`, then one `claude plugin update NAME@outdoornorway` per plugin. With `--run`, it runs the steps from the repo folder. |
| `skills list` | none | Prints one line per skill folder: the skill name, the plugins that ship it, the folder, and whether `skills pack` can zip it. |
| `skills pack` | `--out DIR`, `--list`, `NAME...` | Runs `python3 -I tools/pack_skills.py` with the same arguments. See the section above. |
| `doctor` | none | Checks Node, `python3`, the Claude Code CLI, the required plugin files, the version numbers and every marketplace entry. Prints `[ok]`, `[warn]` or `[fail]` for each check. |
| `test` | `--all` | Runs the validator tests and the integrity tests with `python3`. With `--all`, it also runs the adquill linter tests. |
| `version` | none | Prints the version in `package.json`. Also `--version` and `-v`. |
| `help` | none | Prints the usage text. Also `--help` and `-h`. With no command, the launcher prints the usage text. |

`npm run list`, `npm run pack`, `npm run doctor` and `npm test` call the same commands.

The commands that `install` and `update` print are in [installation.md](../docs/installation.md).

Behaviour notes:

- `install` and `update` read the plugin names from `.claude-plugin/marketplace.json`. An unknown `NAME` prints the valid names and exits 1, and so does an unknown option or more than one name.
- `OUTDOORNORWAY_MARKETPLACE` sets the marketplace source for `install`. `update` ignores it, because it refreshes the marketplace Claude Code already has. The default is `Sameersexy/outdoornorway`. Set it to a fork or to a local folder, such as the clone. A path that starts with `./` or `../` is resolved against the folder you run the launcher from. A Claude Code marketplace has one source per name, so adding a different source for `outdoornorway` repoints the marketplace you already have. Test with an isolated `CLAUDE_CONFIG_DIR` to leave your own settings alone.
- `doctor` warns when Node is older than 18 or the Claude Code CLI is missing. It fails when `python3` is missing, a required file is missing, or `package.json` and `.claude-plugin/plugin.json` differ in version. It then checks every marketplace entry: the source folder exists and stays inside the repo, every `skills` path has a `SKILL.md` whose `name` equals the folder name, and the entry version equals the package version. It fails an entry that has `source "./"` together with `strict false` and a component list, because Claude Code refuses to load that combination. A failure sets exit code 1. Warnings leave it at 0. A missing or broken file is a `[fail]` line, never a crash.
- `install --run` and `update --run` need the Claude Code CLI. Without it, they print an error and exit 1. The steps run in order, and the first failing step stops the run. For `install --run`, a step that reports the marketplace or plugin as already added or installed counts as done. Claude Code 2.1.304 exits 0 in that case. The launcher also accepts an older CLI that exits non-zero with the same message.
- `update all --run` stops at the first plugin that is not installed, because `claude plugin update` fails for it. Update the plugins you have by name.
- `test` needs `python3`. Without it, it prints a message and exits 1.
- `test` needs a clone. The npm package leaves out `.gitignore`, so the integrity test fails there. `doctor` works in both.
- `skills pack` needs `python3`. Without it, the launcher prints a message and exits 1. The packer exits 1 for an unknown skill name.
- An unknown command prints an error and the usage text to stderr, then exits 1.
- With `--run`, the `claude` CLI changes Claude Code's plugin settings. The test steps can create `__pycache__` folders, which git ignores and `package.json` leaves out of the npm package.

## Where to go next

The [repo map](../docs/repo-map.md) says why the files here must not move. [publishing-to-npm.md](../docs/publishing-to-npm.md) covers publishing the launcher.
