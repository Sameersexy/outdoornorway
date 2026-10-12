# outdoornorway

Marketing tools for Outdoor Norway, built for Claude Code: a video script skill with an enforced validator, two agents, slash commands and vetted copywriting skills.

This repo is public and specific to Outdoor Norway. No licence has been chosen, so all rights are reserved by default. [VERIFY: owner to choose a licence]

Writers and video editors: start with [docs/getting-started.md](docs/getting-started.md), or run `/howto` once the repo is open in Claude Code.

## Install

Open this repo in Claude Code and everything loads: the slash commands, the skills and the agents live in `.claude/`.

On another machine, clone the repo and start `claude` inside it. The commands and agents look for files at this repo's own paths, so they work inside a clone.

A plugin package exists (`/plugin install outdoornorway-marketing --marketplace Sameersexy/outdoornorway`), but installing it into a different project is untested and the commands would not find the validator there. [VERIFY: test a clean install in an empty folder, and whether `${CLAUDE_PLUGIN_ROOT}` paths in the commands fix it]

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

The commands are user-invoked only, so they add nothing to the model's context until you run one.

## What is here

- `.claude/skills/scriptcraft/`: the script skill. Two tiers (short up to 25 s, long up to 3:20), three styles (voiceover, ugc_talk, ugc_text), a validator with 61 rules (47 structural, 14 brand), fixtures and 269 tests.
- `.claude/agents/`: `script-writer` and `script-reviewer`.
- `campaigns/ski-meta-ads/tours.json`: prices, dates and day-by-day plans, checked by `verify_tours.py`.
- `content/scripts/`: scripts, each with a notes file. `docs/`: research and test write-ups, `docs/token-hygiene.md`.
- `THIRD_PARTY_SKILLS.md`: the vetted third-party skills, their sources and licenses.

Tests: `python3 -I .claude/skills/scriptcraft/scripts/test_script_check.py`
