# Install the Outdoor Norway marketing tools

This guide is for teammates who have never used this repo. It covers the three ways to install the tools for Claude Code, how to check each install, and how to update or remove it.

If you write or edit scripts, read [docs/getting-started.md](getting-started.md) after you install.

## Prerequisites

- **Claude Code.** Follow the [Claude Code quickstart](https://code.claude.com/docs/en/quickstart). Check it with `claude --version`.
- **Python 3.** The script validator and the tests run as `python3`. Check it with `python3 --version`. The main test suites pass on Python 3.11, 3.12 and 3.13. [VERIFY: lowest Python 3 version; adquill's own docs state 3.9 or newer]
- **Git.** Needed for the clone route only. Check it with `git --version`.
- **Node.js 18 or newer.** Optional for the tools themselves. The npx launcher needs it, and so do the `doctor` and `test` commands. The launcher was run on Node 22. Check it with `node --version`.

## Choose a route

| Route | Works from | Best for | You need | Start with |
|---|---|---|---|---|
| Plugin | Any folder | Writing and reading scripts | Claude Code, Python 3 | `claude plugin marketplace add Sameersexy/outdoornorway` |
| Clone | The repo folder | Editing the tools and sending pull requests | Claude Code, Python 3, Git | `git clone https://github.com/Sameersexy/outdoornorway.git` |
| npx launcher | Any folder, no clone | Checking your set up and printing the install commands | Claude Code, Python 3, Node.js 18 or newer | `npx github:Sameersexy/outdoornorway doctor` |

If you only write or read scripts, choose the plugin. The npx launcher is optional. It checks your set up, and it installs nothing unless you add `--run`.

## Route 1: plugin (works from any folder)

### Install

Run these two lines in a terminal:

```
claude plugin marketplace add Sameersexy/outdoornorway
claude plugin install outdoornorway-marketing@outdoornorway
```

Or type `/plugin` inside Claude Code, add the marketplace `Sameersexy/outdoornorway`, then install `outdoornorway-marketing`. A marketplace is a list of plugins kept on GitHub. Restart Claude Code when you are done.

Scripts are saved in the folder where you run Claude Code.

### Confirm it worked

```
claude plugin list
```

Check that `outdoornorway-marketing` is enabled. Then restart Claude Code, type `/`, and look for commands with the plugin name, such as `/outdoornorway-marketing:script` and `/outdoornorway-marketing:validate`.

### Update

```
claude plugin marketplace update outdoornorway
claude plugin update outdoornorway-marketing@outdoornorway
```

Restart Claude Code.

### Uninstall

[VERIFY: uninstall commands]

To switch the plugin off without removing it, run `claude plugin disable outdoornorway-marketing@outdoornorway`. Run `claude plugin enable` with the same name to turn it back on. The [archived handoff note](archive/handoff-next-session.md) names these two commands.

## Route 2: clone (best for editing)

This route works from the repo folder. Choose it if you will edit the tools or send pull requests. The repo is public, so do not add private client information to it.

### Install

```
git clone https://github.com/Sameersexy/outdoornorway.git
cd outdoornorway
claude
```

Start Claude Code inside the repo folder. The commands then have short names, such as `/script` and `/validate`. The skills and agents in `.claude/` load on their own.

### Confirm it worked

```
node tools/outdoornorway-cli.js doctor
```

Lines that start with `[ok]` are good. A `[warn]` line does not fail the check. A `[fail]` line does, and the last line then reads "Some checks failed." Otherwise the last line reads "All required checks passed."

Type `/` in Claude Code and look for `/script` and `/validate`. To run the validator tests and the integrity tests, which need Python 3:

```
node tools/outdoornorway-cli.js test
```

Add `--all` to include the adquill tests. adquill is paused, and the plugin does not install it. See [adquill/README.md](../adquill/README.md).

### Update

```
git pull
node tools/outdoornorway-cli.js doctor
```

If `git pull` stops because of local changes, ask Sameer before you discard anything.

### Uninstall

Delete the cloned folder. Before you do, send or copy any scripts in `content/scripts/` that have not been shared yet. [docs/backup-and-restore.md](backup-and-restore.md) lists what else to keep. If you also installed the plugin, remove it as shown in route 1.

## Route 3: npx launcher (optional)

This route works from any folder, with no clone. The launcher is `tools/outdoornorway-cli.js`. It uses only Node built-ins and never writes files. `install` and `update` print the Claude Code commands, and they run those commands only when you add `--run`.

The commands are:

- `doctor` checks Node, Python 3, the Claude Code CLI, the plugin files, the commands and agents folders, the script skill, `campaigns/ski-meta-ads/tours.json`, and whether the version numbers in `package.json` and the two plugin files match.
- `install` prints the two plugin commands. Add `--run` to run them.
- `update` prints the two update commands. Add `--run` to run them.
- `test` runs the validator tests and the integrity tests. Add `--all` to include the adquill tests.
- `version` prints the package version.
- `help` prints the usage text.

### Install

Check your set up:

```
npx github:Sameersexy/outdoornorway doctor
```

Print the install commands:

```
npx github:Sameersexy/outdoornorway install
```

Run them:

```
npx github:Sameersexy/outdoornorway install --run
```

If the Claude Code CLI is missing, `install --run` stops and says so. Restart Claude Code after the install.

npx reads the repo's default branch. The npx commands on this page work only after this change set is merged there. [VERIFY: confirm npx runs the bin from a GitHub spec] The launcher is not on npm yet. See [docs/publishing-to-npm.md](publishing-to-npm.md).

### Confirm it worked

Run the `doctor` command again and look for "All required checks passed." Then follow the confirm steps in route 1.

### Update

```
npx github:Sameersexy/outdoornorway update
npx github:Sameersexy/outdoornorway update --run
```

The first line prints the update commands. The second runs them.

### Uninstall

The launcher writes no files of its own. If you ran `install --run`, remove the plugin as shown in route 1.

## Troubleshooting

- **No commands when you type `/`.** On the plugin route, restart Claude Code and run `claude plugin list` to check the plugin is enabled. On the clone route, start Claude Code inside the repo folder.
- **A plugin update changed nothing.** An installed copy updates when its version number changes. If a change you expect is missing, tell Sameer.
- **`[fail] python3 not found`.** Install Python 3 from the [official download page](https://www.python.org/downloads/) and try again. On Windows the name `python3` may not exist. [VERIFY: confirm the checker runs on Windows]
- **`[warn] Claude Code CLI not found`.** Install Claude Code from the [quickstart](https://code.claude.com/docs/en/quickstart). `install --run` and `update --run` need it.
- **`[warn] Node` with "the launcher needs 18 or newer".** Install Node.js 18 or newer from [nodejs.org](https://nodejs.org/). Check the version with `node --version`.
- **`[fail] versions differ`.** The version numbers in `package.json` and the two plugin files do not match. Report it on the [issues page](https://github.com/Sameersexy/outdoornorway/issues).
- **The npx commands do not work.** The launcher reads the repo's default branch, and it appears there only after the change set is merged. Use the plugin or clone route until then.
- **"Usage limit reached".** Wait for the reset. Use one script per session. See [docs/token-hygiene.md](token-hygiene.md).
- **`/tour-data` cannot reach the site.** It needs internet access, and so does the live price check, `python3 -I campaigns/ski-meta-ads/verify_tours.py`. If your session blocks outside websites, tell Sameer.
- **Script errors,** such as `PARSE ERROR line N`, `[FAIL] BR13` or a rule id you do not know. These are covered under "If something goes wrong" in [docs/getting-started.md](getting-started.md).

## Where to go next

- Writers: [docs/getting-started.md](getting-started.md).
- The tools and the launcher: [tools/README.md](../tools/README.md).
- Contributors: [CONTRIBUTING.md](../CONTRIBUTING.md).
