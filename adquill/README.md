# adquill (paused)

This folder holds adquill, a paused skill and three agents that draft ad copy for Meta (Facebook and Instagram) and X. Read this page to learn what is here and why the plugin does not load it.

Work on adquill stopped after the drafts of October 2026, and the files are kept so nothing is lost. The plugin does not install them, and Claude Code does not load them from here. `.claude-plugin/plugin.json` points at `.claude/`, not at this folder. The video script skill is the active work: see the [skills catalog](../docs/skills-catalog.md).

## What is in here

| Path | What it holds |
|---|---|
| `AGENTS.md` | Instructions for any coding agent that wants to use the skill: how to load it, the commands, the method and the hard rules |
| `skills/adquill/SKILL.md` | The skill entry point |
| `skills/adquill/references/` | Reference files, read only when `SKILL.md` says so |
| `skills/adquill/assets/` | Brief, fact ledger and output templates |
| `skills/adquill/scripts/` | `slop_lint.py` (the linter), `rules.json`, `test_slop_lint.py` and fixtures |
| `agents/` | `creative-director`, `direct-response-chief` and `editorial-director` |

Every example in the skill uses an invented company, Brekke Ski Guides. The examples are not Outdoor Norway facts.

`AGENTS.md` explains how an agent loads the skill from this folder. Claude Code does not load it from here, because there is no plugin manifest for it.

## Run the linter and its tests

The linter uses only the Python standard library and needs no network.

```
python3 -I adquill/skills/adquill/scripts/test_slop_lint.py
python3 -I adquill/skills/adquill/scripts/slop_lint.py --text "your copy"
```

`slop_lint.py` needs Python 3.9 or newer. The linter tests pass on Python 3.9 to 3.13 and fail on Python 3.8.

## If work resumes

Read `AGENTS.md` first. Move the skill into `.claude/skills/` and the agents into `.claude/agents/` only when the team decides to ship it, because that changes what the plugin installs. In the same change, add the agents to the list in `.claude-plugin/plugin.json` and adjust `tools/test_repo_integrity.py`, which expects every skill folder other than `scriptcraft` to be listed in `THIRD_PARTY_SKILLS.md`.
