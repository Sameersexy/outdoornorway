---
description: List every [VERIFY] placeholder and unverified fact row in a script, grouped by who confirms it
argument-hint: <path to the script file>
allowed-tools: Bash(python3 -I .claude/skills/scriptcraft/scripts/script_check.py:*)
disable-model-invocation: true
---
!`python3 -I .claude/skills/scriptcraft/scripts/script_check.py $ARGUMENTS --open-items`

Show the list above as it is. Add one line on what blocks `--final` and who is asked most often. Do not edit the script.
