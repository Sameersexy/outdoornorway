# adquill (paused)

This folder holds adquill, a paused skill and three agents that draft ad copy for Meta (Facebook and Instagram) and X. Read this page to learn what is here and why the plugin does not load it.

Work on adquill stopped after the drafts of October 2026, and the files are kept so nothing is lost. The plugin does not install them, and Claude Code does not load them from here. `.claude-plugin/plugin.json` points at `.claude/`, not at this folder. The video script skill is the active work: see the [skills catalog](../docs/skills-catalog.md).

## What is in here

| Path | What it holds |
|---|---|
| [AGENTS.md](AGENTS.md) | Instructions for any coding agent that wants to use the skill: how to load it, the commands, the method and the hard rules |
| [skills/adquill/SKILL.md](skills/adquill/SKILL.md) | The skill entry point |
| `skills/adquill/references/` | Reference files, read only when `SKILL.md` says so: [buyer journey and anxieties](skills/adquill/references/buyer-journey-and-anxieties.md), [craft](skills/adquill/references/craft.md), [hooks and headlines](skills/adquill/references/hooks-and-headlines.md), [Meta](skills/adquill/references/meta.md), [offer and price](skills/adquill/references/offer-and-price.md), [policy](skills/adquill/references/policy.md), [psychology](skills/adquill/references/psychology.md), [sharing and virality](skills/adquill/references/sharing-and-virality.md) and [X](skills/adquill/references/x.md) |
| `skills/adquill/assets/` | Brief, fact ledger and output templates: [brief template](skills/adquill/assets/brief-template.md), [fact ledger template](skills/adquill/assets/fact-ledger-template.md), [Meta static output](skills/adquill/assets/output-meta-static.md), [X post output](skills/adquill/assets/output-x-post.md) and [panel prompt](skills/adquill/assets/panel-prompt.md) |
| `skills/adquill/scripts/` | [slop_lint.py](skills/adquill/scripts/slop_lint.py) (the linter), [rules.json](skills/adquill/scripts/rules.json) (its rules) and [test_slop_lint.py](skills/adquill/scripts/test_slop_lint.py) (its tests) |
| `skills/adquill/scripts/fixtures/` | Sample copy the tests read: [bad-1-meta-primary.txt](skills/adquill/scripts/fixtures/bad-1-meta-primary.txt), [bad-2-policy-risks.txt](skills/adquill/scripts/fixtures/bad-2-policy-risks.txt), [bad-3-chatbot-residue.txt](skills/adquill/scripts/fixtures/bad-3-chatbot-residue.txt), [good-1-meta-primary.txt](skills/adquill/scripts/fixtures/good-1-meta-primary.txt), [good-2-meta-long.txt](skills/adquill/scripts/fixtures/good-2-meta-long.txt) and [good-3-x-post.txt](skills/adquill/scripts/fixtures/good-3-x-post.txt) |
| `agents/` | Three read-only reviewers: [creative-director](agents/creative-director.md), [direct-response-chief](agents/direct-response-chief.md) and [editorial-director](agents/editorial-director.md) |

`SKILL.md` and `AGENTS.md` name two reference files that are not in this folder: `references/rewrite-protocol.md` and `references/voice-and-anti-slop.md`. Git history has no earlier copy of either. The drafts work without them, and anyone who resumes the work should add both files or remove the rows that name them.

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
