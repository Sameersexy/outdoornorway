# Back up and restore the Claude account and tools

This guide is for the repo owner who is moving the Outdoor Norway Claude account to a new login. It covers what lives where, the checks before the switch, the restore steps, a dry run, and what must stay out of this public repo.

The repo does not record the claude.ai menu paths for the data export, the skills upload and the connectors. [VERIFY: current claude.ai menu paths for the data export, the skills upload and the connectors, and the upload format for custom skills]

## What lives where

Four places hold the setup. Each has its own owner and sharing rule.

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

   The first command lists uncommitted files. The second counts commits that the remote does not have yet. Push the branch if the count is above zero.

2. Export the Claude account data and save the export in the private backup, not in the repo.
3. Copy the account-only skills into the private backup. [skills-catalog.md](skills-catalog.md) lists the account-only skills.
4. Write down the connectors that are switched on, by name only. Never copy tokens or keys.
5. Copy the local Claude Code transcripts into the private backup, as described under [local transcripts](#local-claude-code-transcripts).
6. If you will commit from a new email address, add and verify it on the GitHub account first. `git config user.email` shows the address git uses in this repo. Commits in a public repo show that address.
7. Keep the old login until every restore step below is done.

## Restore on the new account

Work through these steps in order.

1. Sign in to claude.ai and to Claude Code with the new login.
2. Install the plugin. Follow route 1 in [installation.md](installation.md), or run these two commands:

   ```
   claude plugin marketplace add Sameersexy/outdoornorway
   claude plugin install outdoornorway-marketing@outdoornorway
   ```

   Restart Claude Code, then run `claude plugin list` to check that the plugin is enabled.

3. Upload the custom skills from the private backup to the account. Restore only the skills that [skills-catalog.md](skills-catalog.md) lists as account-only. The repo copy of scriptcraft is the canonical one, so upload the account copy only if you want it in chat. Platform skills (docx, pdf, pptx and xlsx) are never in the backup.
4. Sign in to each connector again, using the list you wrote before the switch. Connector sign-ins are kept neither in git nor in the private backup.
5. Copy old transcripts out of the private backup only if you want the token report to read them. The report takes any transcript path, so they can stay outside `~/.claude/projects`.

### Local Claude Code transcripts

Claude Code writes one transcript per session on the computer where the session ran. Each is a JSON Lines file (`.jsonl`) in a folder for its project under `~/.claude/projects`. Subagent transcripts sit in a `subagents` folder inside a folder named after the session. These are local files, so they do not come with the account.

Copy them by hand into the private backup and keep the same layout. The token report ([tools/transcript_report.py](../tools/transcript_report.py)) finds subagent runs through that folder, so a flat copy loses them. Never place a transcript in this repo.

## Restore dry run

Test the restore in a scratch folder before you rely on it. The dry run clones the repo, runs the two test suites and the launcher's doctor, and reads one copied transcript. It does not change the Claude account.

```
mkdir -p ~/restore-dry-run
cd ~/restore-dry-run
git clone https://github.com/Sameersexy/outdoornorway.git
cd outdoornorway
python3 -I tools/test_repo_integrity.py
python3 -I .claude/skills/scriptcraft/scripts/test_script_check.py
node tools/outdoornorway-cli.js doctor
```

Each test run ends with the line `OK` when it passes. [tools/README.md](../tools/README.md) describes the doctor.

Copy one transcript from the private backup to `~/restore-dry-run/sample.jsonl`, outside the clone. Pick one that has model calls, or the report exits with a message. Then run the report on that copy from inside the clone:

```
python3 -I tools/transcript_report.py ~/restore-dry-run/sample.jsonl
```

When you finish, delete the scratch folder:

```
rm -rf ~/restore-dry-run
```

## What must never go in this public repo

The repo is public and MIT licensed. Keep these out of it:

- Chat transcripts and session logs (`*.jsonl`).
- Account data exports, zip and tgz archives, and any `exports/` or `backup/` folder.
- Environment files (`.env`, `.env.*`), tokens, keys and other secrets.
- Supplier skills, and any file with supplier terms, prices, contacts or client detail.
- Email addresses and other personal data.

[CONTRIBUTING.md](../CONTRIBUTING.md#licence-and-private-information) has the full rule.

### What guards these

The ignore rule comes first. `.gitignore` lists `*.jsonl`, `*.zip`, `*.tgz`, `.env`, `.env.*`, `node_modules/`, `backup/` and `exports/`, so git leaves matching files out of commits. An ignore rule does not remove a file that git already tracks, and `git add -f` overrides it.

The second guard is the `PublicRepoGuards` class in `tools/test_repo_integrity.py`. It fails when git tracks a `.jsonl`, `.zip`, `.tgz`, `.env` or `node_modules` file, when `.gitignore` lacks the main patterns, or when a text file in the repo holds an email address or a key-like string. It reads text files only, such as `.md`, `.json`, `.py` and `.js` files, so an untracked transcript is caught by the ignore rule alone.

Nothing automatic checks for supplier skills. Read each one for supplier terms, prices, contacts and client detail before it moves into the repo.
