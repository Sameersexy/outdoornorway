# Script skill review rounds

This index is for anyone who asks how the scriptcraft skill was reviewed, and what each review found.

These are historical review rounds of the script skill. Nothing at run time depends on them. The skill, the validator, the agents and the commands do not read this folder, and no file outside it names these files. The integrity test lists this index by name and checks that it exists and that its links resolve.

## Files

- `e2e-agent-tests.md`: a test of the script writer and script reviewer agents on four scripts. The file states its aim as seeing what the validator catches, what only a reviewer catches, and whether a rewrite loop converges. It gives a score for each item, and it says its evidence is limited to four scripts with one reviewer run each.
- `round-1-creative.md`: the first creative review, by the composite creative director persona from `adquill/agents/creative-director.md`. Verdict Revise, 7 out of 10. It asks whether the method gives distinctive short and long scripts.
- `round-1-direct-response.md`: the first direct-response review, with an attack on the validator's rules, by the persona from `adquill/agents/direct-response-chief.md`. Dated 2026-10-07. Verdict Revise, 7 out of 10.
- `round-1-editorial.md`: the first editorial review, by the persona from `adquill/agents/editorial-director.md`. Dated 2026-10-07. Verdict Revise, 7 out of 10.

No round 2 file is in this folder. The round reviews use composite personas defined in the paused `adquill/` folder.

To see what changed in the skill since these were written, run `git log -- .claude/skills/scriptcraft/`.

## Related

- [Content scripts](../../content/scripts/README.md)
- [Docs index](../README.md)
- [Scriptcraft skill](../../.claude/skills/scriptcraft/SKILL.md)
