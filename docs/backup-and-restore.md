# Back up and restore the Claude account and tools

This guide is for the repo owner who is moving the Outdoor Norway Claude account to a new login, for example when the email domain changes. It covers what lives where, the checks before the switch, the restore steps on the new account, a dry run, and what must stay out of this public repo.

## What lives where

Four places hold the setup. Each one has its own owner and sharing rule.

| Place | What is there | Shared? | How it comes back |
|---|---|---|---|
| Public repo (`Sameersexy/outdoornorway` on GitHub) | The plugin, commands, agents, the scriptcraft skill, vetted third-party skills, tour data, scripts and guides | Public, MIT licensed | Clone it, or install the plugin. See [installation.md](installation.md). |
| Claude account | Chat history, custom skills uploaded to the account, connector sign-ins, platform skills | Account owner only | Export before the switch. Upload skills and sign in to connectors again on the new login. |
| Private backup (`<your-private-backup-repo>`) | Chat transcripts, account-only skills, local Claude Code transcripts copied by hand | Private | Copy files out of it on the new login. Never merge it into this repo. |
| Local computer | The clone, if there is one. Claude Code transcripts under `~/.claude/projects`. Any `.env` file. | That machine only | Copy by hand. Git does not carry these. |

[skills-catalog.md](skills-catalog.md) says which skill lives in which place.

## Before the switch

Work through this list while the old login still works.

1. Confirm the public repo is pushed. From the repo folder, run:

```
git status --short
git rev-list --count @{u}..HEAD
```

The first command lists uncommitted files. The second counts commits that the remote does not have yet. Push the branch if the count is not zero.

2. Export the Claude account data. Save the export in the private backup, not in the repo. [VERIFY: confirm current menu path for the data export and what it includes]

3. Copy the account-only skills into the private backup. [VERIFY: confirm how to download a skill from the account] The table in [skills-catalog.md](skills-catalog.md) marks which skills are account-only.

4. Write down the connectors that are switched on, by name only. Do not copy tokens or keys. The connector settings are at https://claude.ai/customize/connectors [VERIFY: confirm current menu path].

5. Copy the local Claude Code transcripts into the private backup. The steps are in the local transcripts section below.

6. Add the new email address to the GitHub account and verify it. Then run `git config user.email` in the repo to see which address git uses here. [VERIFY: confirm that commits from the new address link to the GitHub account]

7. Team plan owners only: add the new email domain as a second allowed domain. [VERIFY: confirm current menu path for allowed domains on a Team plan]

8. Keep the old login until every restore step below is done. Do not cancel the old account or remove the old address before then.

## Restore on the new account

Work through these steps in order.

1. Sign in to the claude.ai account with the new login, then sign in to Claude Code with the same account. [VERIFY: confirm current sign-in steps for claude.ai and Claude Code]

2. Install the plugin. Follow route 1 in [installation.md](installation.md), or run these two commands:

```
claude plugin marketplace add Sameersexy/outdoornorway
claude plugin install outdoornorway-marketing@outdoornorway
```

Restart Claude Code, then run `claude plugin list` to check that the plugin is enabled.

3. Re-upload the custom skills from the private backup. The skills area is at https://claude.ai/customize/skills [VERIFY: confirm current menu path]. Upload each skill as a zip whose top level is the skill folder [VERIFY: confirm current upload format]. Restore only the skills that [skills-catalog.md](skills-catalog.md) lists as account-only.

   - The repo copy of scriptcraft is the canonical one. The account copy is a chat edition that differs from it, so upload it only if you want it in chat. [VERIFY: confirm the backup holds the account copy of scriptcraft]
   - Platform skills (docx, pdf, pptx and xlsx) are never in the backup. Do not look for them there.

4. Reconnect the connectors. Connector sign-ins are not kept in git or in the private backup. Sign in to each connector again, using the list you wrote before the switch, on the connectors page at https://claude.ai/customize/connectors [VERIFY: confirm current menu path].

5. Check the local transcripts. This step is only for sessions that ran on a local computer.

### Local Claude Code transcripts

Claude Code writes a transcript for each session on the computer where the session ran. Each transcript is a JSON Lines file (`.jsonl`). These are local files, so they do not come with the account. The token report reads them from `~/.claude/projects` ([tools/transcript_report.py](../tools/transcript_report.py)). Each session is a `.jsonl` file inside a folder for its project. Subagent transcripts sit in a `subagents` folder inside a folder named after the session. [VERIFY: confirm this folder layout on the current Claude Code version]

Copy the files by hand into the private backup and keep the same layout. The token report looks for the `subagents` folder inside the session's own folder, so a flat copy loses that link.

Do not place any transcript in this repo. The ignore rule covers `*.jsonl`, as described below.

## Restore dry run

Test the restore in a scratch folder before you rely on it. The dry run clones the repo, runs the tests, runs the launcher's doctor and reads one copied transcript. It does not change the Claude account.

```
mkdir -p ~/restore-dry-run
cd ~/restore-dry-run
git clone https://github.com/Sameersexy/outdoornorway.git
cd outdoornorway
python3 -I tools/test_repo_integrity.py
python3 -I .claude/skills/scriptcraft/scripts/test_script_check.py
node tools/outdoornorway-cli.js doctor
```

Each test run ends with the line `OK` when it passes. The doctor checks Node, Python 3, the Claude Code CLI and the repo files. It needs Node 18 or newer, and the launcher never writes files.

Copy one transcript from the private backup to `~/restore-dry-run/sample.jsonl`, outside the clone. Use a transcript that has model calls, or the report exits with a message. Then run the report on that copy from inside the clone:

```
python3 -I tools/transcript_report.py ~/restore-dry-run/sample.jsonl
```

The report prints the transcript path and counts only. When you finish, delete the scratch folder:

```
rm -rf ~/restore-dry-run
```

## What must never go in this public repo

The repo is public and MIT licensed. Keep these out of it:

- Chat transcripts and session logs (`*.jsonl`).
- Account data exports, zip and tgz archives, and any `exports/` or `backup/` folder.
- Environment files (`.env`, `.env.*`), tokens, keys and other secrets.
- Supplier skills, and any file with supplier terms, prices, contacts or client detail. [skills-catalog.md](skills-catalog.md) explains the rule.
- Email addresses and other personal data.

### What guards these

The ignore rule comes first. `.gitignore` lists `*.jsonl`, `*.zip`, `*.tgz`, `.env`, `.env.*`, `node_modules/`, `backup/` and `exports/`, so git leaves matching files out of commits. An ignore rule does not remove a file that git already tracks, and `git add -f` overrides it.

The second guard is the `PublicRepoGuards` class in `tools/test_repo_integrity.py`. It fails when git tracks a `.jsonl`, `.zip`, `.tgz`, `.env` or `node_modules` file, when `.gitignore` lacks the main patterns, or when a text file in the repo holds an email address or a key-like string. The test reads text files only, such as `.md`, `.json`, `.py` and `.js` files. It does not read the contents of `.jsonl` files, so an untracked transcript is caught by the ignore rule alone.

Nothing automatic checks for supplier skills. Read each one for supplier terms, prices, contacts and client detail before it moves into the repo. [VERIFY: decide whether a test should check supplier skills by name]

## Related

- [skills-catalog.md](skills-catalog.md) lists which skill lives where.
- [installation.md](installation.md) covers the three install routes.
- [repo-map.md](repo-map.md) lists the paths that must not move.
- [tools/README.md](../tools/README.md) describes the token report and the tests.
