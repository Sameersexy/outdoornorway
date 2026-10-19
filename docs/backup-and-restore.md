# Back up and restore the Claude account and tools

This guide is for the repo owner who is moving the Outdoor Norway Claude account to a new login. It covers what lives where, the checks before the switch, the restore steps, a dry run, and what must stay out of this public repo.

The menu paths below come from the Anthropic help pages linked in each step, as read on 19 October 2026. Menus change, so follow the linked page if a name differs.

## What lives where

Six places hold the setup. Each has its own owner and sharing rule.

| Place | What is there | Shared? | How it comes back |
|---|---|---|---|
| Public repo (`Sameersexy/outdoornorway` on GitHub) | The plugin, commands, agents, the scriptcraft skill, vetted third-party skills, two account skills, tour data, scripts and guides | Public, MIT licensed | Clone it, or install the plugin. See [installation.md](installation.md). |
| Claude account | Chat history, custom skills uploaded to the account (the live copy of each account-only skill), connector sign-ins, platform skills | Account owner only | Export before the switch. Upload skills and sign in to connectors again on the new login. |
| Private backup | Chat transcripts (the account data export, and the local Claude Code transcripts copied by hand) and a second copy of the account-only skills | Private | Copy files out of it on the new login. Never merge it into this repo. |
| npm account | The `outdoornorway-marketing` launcher package, after the first publish. It is not on npm yet. | The package is public. The login is the owner's. | Log in to npm on the new machine, then publish from a clean copy of the repo. See [publishing-to-npm.md](publishing-to-npm.md). |
| GitHub account | The login that owns the public repo, the email addresses on it, and any access tokens or SSH keys used to push | Account owner only | Sign in on the new machine, then check the repo address and the commit email. See restore step 7. |
| Local computer | The clone, if there is one. Claude Code transcripts under `~/.claude/projects`, one folder per project. Any `.env` file. | That machine only | Copy by hand. Git does not carry these. |

The private backup holds what the public repo must not hold (chat transcripts and private skills) and is kept outside this repo. [VERIFY: the owner confirms where it is kept and who can open it]

[skills-catalog.md](skills-catalog.md) says which skill lives in which place.

## Before the switch

Work through this list while the old login still works.

1. Confirm the public repo is pushed. From the repo folder, run:

   ```
   git branch --show-current
   git status --short
   git rev-list --count @{u}..HEAD
   git remote -v
   ```

   The first command prints the branch name. The second lists uncommitted files, and no output means there are none. The third counts commits that the remote does not have yet. Push the branch if the count is above zero. If it prints a line that starts with `fatal: no upstream configured for branch`, the branch was never pushed, so run `git push -u origin <branch-name>`. The fourth should show the repo address, `https://github.com/Sameersexy/outdoornorway`, for `origin`, with or without a `.git` ending.

   A push does not send tags. `git tag -l` lists the tags on this computer, and `git ls-remote --tags origin` lists the ones on GitHub. The tag `backup-2026-10-15-pre-docs` exists only on this computer. It marks commit `257ea86`, which is on the remote default branch, so no commit depends on the tag. [VERIFY: the owner decides whether to push the tag with `git push origin backup-2026-10-15-pre-docs` or to leave it on this computer]

2. Export the Claude account data and save the export in the private backup, not in the repo. On a personal Free, Pro or Max account, open Settings > Privacy and click Export data. Exports can't be started from the iOS or Android apps. The download link arrives by email, needs a signed-in session, and expires 24 hours after delivery. Team and Enterprise members can export their own data only after an owner turns on Allow members to export their own data. Primary Owners export the whole organization's data from Organization settings > Data and privacy. See [Export your Claude data](https://support.claude.com/en/articles/9450526-export-your-claude-data).
3. Copy the account-only skills into the private backup, one zip or folder per skill, named after the skill. The skills are content-qc, guest-benefit-checker, page-intent-audit, scriptcraft, supplier-product-intake and whatsapp-template-writer, as [skills-catalog.md](skills-catalog.md) lists them. The help page [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) describes only how to delete a custom skill in Customize > Skills, so a download button is not confirmed. If you still have the folder each skill was written in, copy that folder. [VERIFY: the owner confirms whether Customize > Skills can download a custom skill, and what the button is called] The maintained copy of scriptcraft is `.claude/skills/scriptcraft/` in this repo, so its account copy matters only if you use it in chat. Do not copy any of these skills into this repo.
4. Write down the connectors that are switched on, by name only, from Customize > Connectors. Never copy tokens or keys.
5. Copy the local Claude Code transcripts into the private backup, as described under [local transcripts](#local-claude-code-transcripts). Open `~/.claude/projects`. Each project has one folder there, named after the project path with the slashes replaced by hyphens, so a clone at `/home/me/outdoornorway` has a folder named `-home-me-outdoornorway`. Copy the whole folder, because the `subagents` folders sit inside it. Copy it with `cp -R ~/.claude/projects/<project-folder> <backup-folder>/`.
6. If you will commit from a new email address, add and verify it on the GitHub account first. In the account's email settings on GitHub, add the address and follow the link in the verification email. [VERIFY: the owner confirms the current name of the GitHub email settings page, and whether commits should show this address or a GitHub no-reply address] `git config user.email` shows the address git uses in this repo, and `git log -1 --format=%ae` shows the address on the latest commit. To change it for this repo only, run `git config user.email <new-address>`. Commits in a public repo show that address.
7. Keep the old login until every restore step below is done.

## Restore on the new account

Work through these steps in order.

1. Sign in to claude.ai and to Claude Code with the new login.
2. If the account is on a Team or Enterprise plan, check the allowed email domains before you add the new login. On an organization that does not use domain capture, an owner opens Organization settings > Identity and access, clicks Add or edit domains in the Domains section, enters the domain in the Update organization email domains window, clicks +, and then clicks Save. The trash can icon beside a domain removes it. The owner's own domain is listed automatically. See [Account management FAQs](https://support.claude.com/en/articles/13325567-account-management-faqs). A second help page, [Find and join a Team or Enterprise organization](https://support.claude.com/en/articles/13566435-find-and-join-a-team-or-enterprise-organization), names the section Organization and access and a + Add domain button, and it says personal email providers and education domains can't be added to the allowed list. [VERIFY: which section and button the current admin screen shows for allowed email domains, whether public email providers can be added (the two pages disagree), and how to change an existing domain (neither page covers it)]
3. Install the plugin. Follow route 1 in [installation.md](installation.md), or run these two commands:

   ```
   claude plugin marketplace add Sameersexy/outdoornorway
   claude plugin install outdoornorway-marketing@outdoornorway
   ```

   Restart Claude Code, then run `claude plugin list` to check that the plugin is enabled.

4. Upload the custom skills from the private backup to the account. Restore only the skills that [skills-catalog.md](skills-catalog.md) lists as account-only. The repo copy of scriptcraft, `.claude/skills/scriptcraft/`, is the canonical one, so upload the account copy only if you want it in chat. Platform skills, such as docx, pdf, pptx and xlsx, are never in the backup. In Customize > Skills, click the + button, then + Create skill, then Upload a skill, and choose a zip file. The skill folder must be the root of the zip, and its name should match the skill's name. To zip a skill from a clone, run `python3 -I -m zipfile -c ~/<skill-name>.zip <skill-name>` from the folder that holds the skill folder, which is `account-skills/` for the two skills in this repo. The folder becomes the root of the zip, and the zip lands in your home folder, outside the clone. Inside the folder, the instructions file is named skill.md, and it starts with frontmatter that sets name (64 characters at most) and description (200 characters at most). Check the description length of every skill before you zip it, because a description over 200 characters can be refused. The two skills in `account-skills/` have longer descriptions, and so may the account-only ones. Shorten the description in the copy you zip. Keep the backup copy as it is. Free, Pro and Max users can upload after they enable code execution. On Team and Enterprise, members can upload once the organization has skills enabled, and owners can turn user-created skills off or provision a skill for everyone. See [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) and [How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills). [VERIFY: the help page names the file skill.md in lowercase, but the Claude Code skills page at https://code.claude.com/docs/en/skills says SKILL.md; check which name the upload accepts before you upload]

   The two account skills are also in [account-skills/](../account-skills/README.md) in the public repo, and you can upload them from there. The steps are in [how to use a skill](../account-skills/README.md#how-to-use-a-skill).

5. Sign in to each connector again, using the list you wrote before the switch. Connector sign-ins are kept neither in git nor in the private backup. To reconnect, open Customize > Connectors, select the service and disconnect it. Then click + next to Connectors, select the connector, click Connect or Install, and finish the authentication prompts. The help page does not name the disconnect button. [VERIFY: the owner confirms the name of the disconnect control in Customize > Connectors] On Team and Enterprise, an owner adds a connector from Organization settings > Connectors by clicking Browse connectors and then Add to your team. Each member still signs in on their own account. Custom remote connectors are available on Free, Pro, Max, Team and Enterprise, and Free users are limited to one. See [Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities).
6. Copy old transcripts out of the private backup only if you want the token report to read them. The report takes any transcript path, so they can stay outside `~/.claude/projects`.
7. Sign in to GitHub with the owner's account, then run `git remote -v` in the clone. It should still show the repo address from the table above. If the repo moves to another GitHub account, run `git remote set-url origin <new-address>`. [VERIFY: the owner confirms whether the repo stays under the same GitHub account after the switch] Check the commit email as well, as in before-the-switch step 6.
8. If you publish the launcher, log in to npm with the owner's npm account. `npm whoami` prints the user name when the login works. The rest is in [publishing-to-npm.md](publishing-to-npm.md#5-log-in).

Two items have no restore step. Platform skills, such as docx, pdf, pptx and xlsx, come with the new account, so there is nothing to upload. The help page [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude) says Anthropic's built-in skills are available to all users, and that Claude uses them when code execution and file creation is on. Chat history stays in the export you saved before the switch. This guide has no step that moves it into the new account.

### Local Claude Code transcripts

Claude Code writes one transcript per session on the computer where the session ran. Each is a JSON Lines file (`.jsonl`) in a folder for its project under `~/.claude/projects`. Subagent transcripts sit in a `subagents` folder inside a folder named after the session. These are local files, so they do not come with the account.

Copy them by hand into the private backup and keep the same layout. The token report ([tools/transcript_report.py](../tools/transcript_report.py)) lists the subagent runs it finds directly under `subagents/` as `agent-*.jsonl` files, so a flat copy loses them. It does not list runs that a workflow started, which sit one level deeper in `subagents/workflows/<workflow id>/`. Never place a transcript in this repo.

## Restore dry run

Test the restore in a scratch folder before you rely on it. The dry run clones the repo, runs the two test suites and the launcher's doctor, and reads one copied transcript. It does not change the Claude account.

```
mkdir -p ~/restore-dry-run
cd ~/restore-dry-run
git clone https://github.com/Sameersexy/outdoornorway.git
cd outdoornorway
ls tools/outdoornorway-cli.js
```

The doctor step needs `tools/outdoornorway-cli.js`, and the default branch does not have that file until the branch that adds it is merged. If the `ls` line reports no such file, switch to that branch inside the same clone. Until it is merged, it is `claude/optimistic-cannon-rzksgv`. After it is merged, the default branch has the file, so skip the switch. Git creates the local branch from the remote one.

```
git switch <branch>
```

Stay in this clone. A second clone into the scratch folder fails, because the `outdoornorway` folder already exists. Then run the checks:

```
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
