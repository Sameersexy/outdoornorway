# outdoornorway

Marketing tools for Outdoor Norway, built for Claude Code: a video script skill with an enforced validator, two agents, slash commands and vetted copywriting skills.

Writers and video editors: start with [docs/getting-started.md](docs/getting-started.md), or run `/howto` once the repo is open in Claude Code.

## Install

Open this repo in Claude Code and everything loads: the slash commands, the skills and the agents live in `.claude/`.

To use the same tools in another project or on another machine, install the plugin:

```
/plugin install outdoornorway-marketing --marketplace Sameersexy/outdoornorway
```

Or in two steps: `/plugin marketplace add Sameersexy/outdoornorway`, then `/plugin install outdoornorway-marketing@outdoornorway`. Installed commands are namespaced, for example `/outdoornorway-marketing:script`. A private repo needs git access on that machine. [VERIFY: confirm the repo visibility and a clean install on a second machine]

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
