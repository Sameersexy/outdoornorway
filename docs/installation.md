# Install the Outdoor Norway marketing tools

This guide is for teammates who have never used this repo. It covers the three ways to install the tools for Claude Code, how to check each install, and how to update or remove it.

If you write or edit scripts, read [getting-started.md](getting-started.md) after you install.

## Prerequisites

- **Claude Code.** Follow the [Claude Code quickstart](https://code.claude.com/docs/en/quickstart). Check it with `claude --version`.
- **Python 3.9 or newer.** The validator and the tests run as `python3`, and `python3 --version` shows your version. The two main suites also pass on Python 3.8, but the adquill tests need 3.9.
- **Git.** Needed for the clone route only. Check it with `git --version`.
- **Node.js 18 or newer.** Needed for the npx launcher and for the `doctor` and `test` commands, and optional otherwise. Check it with `node --version`.

## Choose a route

| Route | Works from | Best for | You need | Start with |
|---|---|---|---|---|
| Plugin | Any folder | Writing and reading scripts | Claude Code, Python 3 | `claude plugin marketplace add Sameersexy/outdoornorway` |
| Clone | The repo folder | Editing the tools and sending pull requests | Claude Code, Python 3, Git | `git clone https://github.com/Sameersexy/outdoornorway.git` |
| npx launcher | Any folder, no clone, but only once the launcher is on the default branch (it is not on npm yet) | Checking your set up and printing the install commands | Claude Code, Python 3, Node.js 18 or newer | `npx github:Sameersexy/outdoornorway doctor` |

If you only write or read scripts, choose the plugin. The npx launcher is optional. The plugin route offers four plugins, and route 1 shows how to pick one.

## Route 1: plugin (works from any folder)

### Install

Run these two lines in a terminal:

```
claude plugin marketplace add Sameersexy/outdoornorway
claude plugin install outdoornorway-marketing@outdoornorway
```

You can also type `/plugin` inside Claude Code and follow the prompts. A marketplace is a list of plugins kept on GitHub. Restart Claude Code when you are done. Scripts are saved in the folder where you run Claude Code.

### Choose a plugin

The marketplace has four plugins. Replace the name in the second line above to install another one.

| Plugin | Choose it if you |
|---|---|
| `outdoornorway-marketing` | Write or review video scripts. It holds the commands, the agents, scriptcraft and the eight copy skills. |
| `outdoornorway-copy-skills` | Want only the eight copy skills and none of the script tools. |
| `outdoornorway-account-skills` | Want the brand voice checker, the guest benefit checker and the script-writing skill in Claude Code. |

Claude Code 2.1.292 or later can add the marketplace and install in one line: `claude plugin install NAME --marketplace Sameersexy/outdoornorway`. [VERIFY: the one-step line was not run against this repo] The two-line version above works on every version that has plugins. [marketplace.md](marketplace.md) covers what happens when you install two plugins together, and how a team can prompt its members to install.

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

Restart Claude Code. The first line refreshes the list only. Run the second line once for each plugin you installed, because there is no update-all command.

### Switch off or remove

To switch the plugin off and on without removing it:

```
claude plugin disable outdoornorway-marketing@outdoornorway
claude plugin enable outdoornorway-marketing@outdoornorway
```

To remove it, and then the marketplace entry:

```
claude plugin uninstall outdoornorway-marketing@outdoornorway
claude plugin marketplace remove outdoornorway
```

`marketplace remove` also uninstalls every plugin from this marketplace, so skip it if you want to keep another one.

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

If `git pull` stops because of local changes, ask the repo owner before you discard anything.

### Remove

Delete the cloned folder. Before you do, send or copy any scripts in `content/scripts/` that have not been shared yet. [backup-and-restore.md](backup-and-restore.md) lists what else to keep. If you also installed the plugin, remove it as shown in route 1.

## Route 3: npx launcher (optional)

This route works from any folder, with no clone, but only once the launcher is on the default branch of the repo, and the launcher is not on npm yet. The launcher is `tools/outdoornorway-cli.js`. It never writes files. `install` and `update` print the Claude Code commands and run them only when you add `--run`. [tools/README.md](../tools/README.md) lists every launcher command.

Check your set up, then list the plugins:

```
npx github:Sameersexy/outdoornorway doctor
npx github:Sameersexy/outdoornorway list
```

Print the install commands, then run them:

```
npx github:Sameersexy/outdoornorway install
npx github:Sameersexy/outdoornorway install --run
```

`install` without a name means `outdoornorway-marketing`. Add a plugin name, such as `install outdoornorway-account-skills`, to pick another. `install all` installs the umbrella and the account skills. It leaves out `outdoornorway-copy-skills` and says so, because the umbrella already carries those eight skills. A name that is not on the list stops with the valid names.

If the Claude Code CLI is missing, `install --run` stops and says so. Restart Claude Code after the install. To confirm it worked, run `doctor` again, look for "All required checks passed.", then follow the confirm steps in route 1.

To update, print the commands with `update`, then run them with `update --run`. `update all` covers every plugin.

npx reads the repo's default branch, so these commands work only once the launcher is on that branch. The launcher is not on npm yet: see [publishing-to-npm.md](publishing-to-npm.md).

The launcher writes no files of its own. If you ran `install --run`, remove the plugin as shown in route 1.

## Troubleshooting

- **No commands when you type `/`.** On the plugin route, restart Claude Code and run `claude plugin list` to check the plugin is enabled. On the clone route, start Claude Code inside the repo folder.
- **A plugin update changed nothing.** An installed copy updates when the `version` in the plugin files goes up. If a change you expect is missing, tell the repo owner.
- **`[fail] python3 not found`.** Install Python 3.9 or newer from the [official download page](https://www.python.org/downloads/) and try again. The tools are not tested on Windows. They call `python3` by name, so if that name does not exist on your machine, tell the repo owner.
- **`[warn] Claude Code CLI not found`.** Install Claude Code from the [quickstart](https://code.claude.com/docs/en/quickstart). `install --run` and `update --run` need it.
- **`[warn] Node` with "the launcher needs 18 or newer".** Install Node.js 18 or newer from [nodejs.org](https://nodejs.org/).
- **Each copy skill is listed twice.** You installed `outdoornorway-copy-skills` next to `outdoornorway-marketing`, and both carry the same eight skills. Remove the one you do not need, for example `claude plugin uninstall outdoornorway-copy-skills`.
- **`[fail] versions differ` or `[fail] NAME: version X does not match package.json (Y)`.** The version numbers in `package.json`, the plugin file and the marketplace entries do not match. Report it on the [issues page](https://github.com/Sameersexy/outdoornorway/issues).
- **The npx commands do not work.** Use the plugin or clone route. See the note on the default branch in route 3.
- **"Usage limit reached".** Wait for the reset. Use one script per session. See [token-hygiene.md](token-hygiene.md).
- **`/tour-data` cannot reach the site.** It needs internet access, and so does the live price check, `python3 -I campaigns/ski-meta-ads/verify_tours.py`. If your session blocks outside websites, tell the repo owner.
- **Script errors,** such as `PARSE ERROR line N`, `[FAIL] BR13` or a rule id you do not know. They are covered under "If something goes wrong" in [getting-started.md](getting-started.md).
