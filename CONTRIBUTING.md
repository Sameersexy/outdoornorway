# Contributing

This guide is for anyone who sends a change to this repo, whether the change is a script, a command, an agent, a guide or a test. Read [CLAUDE.md](CLAUDE.md) first. It holds the rules that Claude Code follows here, and this page explains them for people.

## Get the repo

```
git clone https://github.com/Sameersexy/outdoornorway.git
```

[docs/repo-map.md](docs/repo-map.md) shows where each folder and file lives. [docs/README.md](docs/README.md) lists every guide.

## Run the tests

Run both main suites before you send a change.

```
python3 -I .claude/skills/scriptcraft/scripts/test_script_check.py
python3 -I tools/test_repo_integrity.py
```

If you change anything in `adquill/`, also run its linter tests. adquill is paused, and the plugin does not install it.

```
python3 -I adquill/skills/adquill/scripts/test_slop_lint.py
```

The repo uses only the Python standard library, and [installation.md](docs/installation.md#prerequisites) lists the Python versions. Node is optional. `node tools/outdoornorway-cli.js test` runs the same suites, and [tools/README.md](tools/README.md) lists every launcher command.

To check the plugin manifests with Claude Code itself, run this from the repo root:

```
claude plugin validate .
```

It passes. Its one warning says that CLAUDE.md at the plugin root is not loaded as project context. The warning can stay, because CLAUDE.md guides work in a clone. Do not add `--strict` to this command, because it turns the warning into an error and the run then fails.

### Validate a script

```
python3 -I .claude/skills/scriptcraft/scripts/script_check.py FILE [--final] [--strict]
```

Replace `FILE` with the script path. The square brackets mark optional flags. The validator takes `--brief` for a short report and `--open-items` for the placeholder list.

### Check tour data

Run this after you change `campaigns/ski-meta-ads/tours.json`. It needs network access.

```
python3 -I campaigns/ski-meta-ads/verify_tours.py
```

It checks `tours.json` against the live Outdoor Norway pages. Exit code 0 means every price, date string and trip length checked out.

## Hygiene rules

The integrity test checks some of these rules. Check the rest yourself.

- No em dash and no en dash. Use parentheses, commas or a new sentence. A plain hyphen inside a compound word is fine.
- No emojis.
- No AI model names in any file, in any spelling.
- No paths from a local machine, such as a scratch folder.
- No email addresses, tokens or private keys.
- No ALL CAPS for emphasis. Bold a noun, or rewrite the sentence.
- Never invent a fact, a URL, a version number, a command or a guide's words.
- Where you cannot check a claim, write `[VERIFY: what to confirm]` in its place.
- Do not hand-write counts of tests, rules or files. Counts drift.

Third-party skill copies listed in [THIRD_PARTY_SKILLS.md](THIRD_PARTY_SKILLS.md) keep their upstream text, so the dash and emoji check skips them.

## Facts and sources

Facts come from three places:

- Prices, dates and day-by-day plans: `campaigns/ski-meta-ads/tours.json`.
- Product and brand facts: `.claude/product-marketing.md`.
- Anything else: a page the client names.

## Commands and agents

Commands and agents reach repo files through ROOT. In the plugin, ROOT is `${CLAUDE_PLUGIN_ROOT}`. In a clone, ROOT is the current folder.

- Do not add `!` shell lines that use `${...}`. A clone has no plugin root, so the integrity test fails on them.
- Do not add bare repo paths to commands. Paths such as `tools/` or `campaigns/ski-meta-ads/` must go through ROOT.
- A command that uses ROOT must carry the ROOT note. The integrity test checks for it.
- Each command sets `disable-model-invocation: true` in its frontmatter.
- A new command must appear in the README and in [docs/getting-started.md](docs/getting-started.md). The guide check does not apply to `/tokens`.
- Each agent has a `## Where files live` section that uses `${CLAUDE_PLUGIN_ROOT}`. Agents have no `model:` line in their frontmatter.
- Put a file in `.claude/commands/` or `.claude/skills/` only if it is a command or a skill. Those folders load automatically.
- Every skill folder except `scriptcraft` needs a row in [THIRD_PARTY_SKILLS.md](THIRD_PARTY_SKILLS.md). A row with a 40-character commit hash also needs a licence file in its folder.

## Howto

The Quick start in [docs/getting-started.md](docs/getting-started.md) is what `/howto` shows. After you edit it, update `.claude/commands/howto.md` to match.

- Keep the frontmatter and the first paragraph of `howto.md`.
- After them, put the Quick start text, from its `## Quick start` heading to the line before `## Set up (once)`. The file must end with that text and one newline.
- The Quick start must not use the word "below", and it must name the "Set up (once)" section.
- Run the integrity test to confirm the two match.

## Moving files

Several paths are load-bearing. Read the "Safe to move?" column in [docs/repo-map.md](docs/repo-map.md) before you move, rename or delete anything.

## Licence and private information

- The repo is public and MIT licensed. See [LICENSE](LICENSE).
- Do not add supplier terms, personal data or other private client information.
- The page-audit notes in `campaigns/ski-meta-ads/` stay public. The owner decided this on 12 October 2026.
- `.gitignore` blocks transcripts (`*.jsonl`), archives (`*.zip`, `*.tgz`), `.env` files, `node_modules/`, `backup/` and `exports/`. Do not work around it.
- Two account skills sit in [account-skills/](account-skills/README.md). They were read for supplier terms, prices, contacts, personal data and client facts before they were copied there. The other account skills live in the Claude account, with a second copy in a private backup kept outside this repo. Chat transcripts are kept the same way. [docs/backup-and-restore.md](docs/backup-and-restore.md) says how the private backup is handled.

## Writing style

- Start each new doc with one sentence that says who it is for or what question it answers.
- Use sentence case headings and fenced code blocks for commands.
- Keep sentences short and direct, and vary their length.
- Cut filler transitions, stock phrases, closing offers and closing questions.

## Before you send a change

1. Run both main test suites, and the adquill tests if you changed `adquill/`.
2. Run `verify_tours.py` if you changed `tours.json`.
3. Regenerate `howto.md` if you edited the Quick start.
4. Check the hygiene rules above.
5. Work on the branch you were given, and open a pull request only when someone asks for one.
