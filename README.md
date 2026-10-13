# outdoornorway

Marketing tools for Outdoor Norway, built for Claude Code: a video script skill with an enforced validator, two agents, slash commands and vetted copywriting skills.

This repo is public and specific to Outdoor Norway. It is MIT licensed (see [Licence](#licence)).

Writers and video editors: start with [docs/getting-started.md](docs/getting-started.md), or run `/howto` (with the plugin, `/outdoornorway-marketing:howto`) in Claude Code.

## Install

Pick one. Both need [Claude Code](https://code.claude.com/docs/en/quickstart) and [Python 3](https://www.python.org/downloads/) (the validator is a Python script, run as `python3`).

**Plugin (works from any folder).** In a terminal:

```
claude plugin marketplace add Sameersexy/outdoornorway
claude plugin install outdoornorway-marketing@outdoornorway
```

Restart Claude Code. The commands carry the plugin name: `/outdoornorway-marketing:script`, `/outdoornorway-marketing:validate` and so on. Scripts are saved in the folder where you run Claude Code. Update with `claude plugin marketplace update outdoornorway` and `claude plugin update outdoornorway-marketing@outdoornorway`.

**Clone (best for editing the tools or sending pull requests).**

```
git clone https://github.com/Sameersexy/outdoornorway.git
cd outdoornorway
claude
```

The commands then have short names (`/script`, `/validate`) and the skills and agents in `.claude/` load on their own. Update with `git pull`.

Check the packaging with `claude plugin validate .` (it passes; its one warning says the repo's `CLAUDE.md` is not shipped inside the plugin, which is intended).

## Slash commands

| Command | What it does |
|---|---|
| `/script <tour or topic> <platform> [style]` | Writes a script with the script-writer agent, saves it to `content/scripts/`, validates it, and returns a short result |
| `/review-script <file>` | Independent review by the script-reviewer agent: facts, voice, authenticity, verdict, top five fixes |
| `/validate <file> [--final] [--strict]` | Runs the validator and shows only the findings |
| `/open-items <file>` | Lists every `[VERIFY]` placeholder and unverified fact row, grouped by who confirms it |
| `/howto` | Shows the quick start for writers and editors |
| `/tour-data` | Checks `campaigns/ski-meta-ads/tours.json` against the live site |
| `/tokens` | Shows where this session's tokens went |

The commands run only when you type them.

## What is here

- `.claude/skills/scriptcraft/`: the script skill. Two tiers (short up to 25 s, long up to 3:20), three styles (voiceover, ugc_talk, ugc_text), a validator with 61 rules (47 structural, 14 brand), fixtures and 277 tests.
- `.claude/agents/`: `script-writer` and `script-reviewer`.
- `campaigns/ski-meta-ads/tours.json`: prices, dates and day-by-day plans, checked by `verify_tours.py`.
- `content/scripts/`: scripts, each with a notes file. `docs/`: research and test write-ups, `docs/token-hygiene.md`.
- `adquill/`: a paused ad-copy skill and agents (drafts). The plugin does not install it.
- `THIRD_PARTY_SKILLS.md`: the vetted third-party skills, their sources and licenses.

Tests: `python3 -I .claude/skills/scriptcraft/scripts/test_script_check.py` (validator) and `python3 -I tools/test_repo_integrity.py` (commands, plugin files, licences, guide).

## Licence

MIT, see `LICENSE`. This covers the files in this repo. It does not grant any right to use the Outdoor Norway name or logos. The third-party skills copied into `.claude/skills/` keep their own MIT licences: see `THIRD_PARTY_SKILLS.md` and the `LICENSE-*` file inside each skill folder.
