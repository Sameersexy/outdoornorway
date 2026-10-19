# adquill (paused)

This folder is for anyone who wants to know what adquill is and why the plugin does not load it.

adquill is a skill and three agents that write honest, human-sounding ad copy for Meta (Facebook and Instagram) and X. Work on it stopped after the drafts in October 2026. It is kept in the repo so nothing is lost. The plugin does not install it, and Claude Code does not load it from here.

## Status

- Paused. The files are drafts, not a finished product.
- Not installed by the plugin. `.claude-plugin/plugin.json` points at `.claude/`, not at this folder.
- The video script skill is the active work: see [docs/skills-catalog.md](../docs/skills-catalog.md).

## What is in here

| Path | What it holds |
|---|---|
| `AGENTS.md` | Instructions for any coding agent that wants to use the skill: how to load it, the commands, the method and the hard rules |
| `skills/adquill/SKILL.md` | The skill entry point |
| `skills/adquill/references/` | Reference files, read only when `SKILL.md` says so |
| `skills/adquill/assets/` | Brief, fact ledger and output templates |
| `skills/adquill/scripts/` | `slop_lint.py` (the linter), `rules.json`, `test_slop_lint.py` and fixtures |
| `agents/` | `creative-director`, `direct-response-chief` and `editorial-director` |

All examples in the skill use one invented brand. They are not Outdoor Norway facts.

## Run the linter and its tests

The linter is Python standard library only, with no network access.

```
python3 -I adquill/skills/adquill/scripts/test_slop_lint.py
python3 -I adquill/skills/adquill/scripts/slop_lint.py --text "your copy"
```

`slop_lint.py` states that it needs Python 3.9 or newer. [VERIFY: confirm the linter on Python 3.9, only 3.11 to 3.13 were available when this file was written]

## If work resumes

Read `AGENTS.md` first. Move the skill into `.claude/skills/` and the agents into `.claude/agents/` only when the team decides to ship it. That move changes what the plugin installs. In the same change, add the agents to the list in `.claude-plugin/plugin.json` and adjust `tools/test_repo_integrity.py`, which expects every skill folder other than `scriptcraft` to be listed in `THIRD_PARTY_SKILLS.md`.
