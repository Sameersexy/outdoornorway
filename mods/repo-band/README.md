# repo-band

A status row above the prompt in Claude Code on the terminal and the desktop app. It shows the session cost, how full the context is, the time and tool calls of the last turn, the branch with the number of changed files, and the last `RESULT:` line from the scriptcraft validator. A Compact button runs `/compact` and a Hide button folds the row to a single Show band button.

It does not draw on vscode or mobile, and not in `claude -p`.

## Install

```
/plugin marketplace add Sameersexy/outdoornorway
/plugin install repo-band@outdoornorway
```

To try it from a clone without installing: `claude --plugin-dir mods/repo-band`.

## What it reads

- Cost and context fill come from the session itself.
- Branch and changed files come from `git branch --show-current` and `git status --porcelain`, refreshed when a turn ends. Outside a git folder that part is left out.
- The check result is read from the output of a Bash call that runs `script_check.py`. It stays empty until the validator has run once in the session.

Nothing leaves the machine and nothing is written to disk.

## Test

```
claude plugin test mods/repo-band
```
