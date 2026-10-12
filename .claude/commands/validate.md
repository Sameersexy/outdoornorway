---
description: Run the scriptcraft validator on a script and show only the findings
argument-hint: <path> [--final] [--strict]
allowed-tools: Bash(python3 -I .claude/skills/scriptcraft/scripts/script_check.py:*)
disable-model-invocation: true
---
!`python3 -I .claude/skills/scriptcraft/scripts/script_check.py $ARGUMENTS --brief`

Summarize the result above in two lines. For each FAIL, name the fix in a few words (`--explain RULE_ID` prints what a rule counts). Do not rerun the validator.
