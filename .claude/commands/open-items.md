---
description: List every [VERIFY] placeholder and unverified fact row in a script, grouped by who confirms it
argument-hint: <path to the script file>
allowed-tools: Bash(python3 -I *scriptcraft/scripts/script_check.py*)
disable-model-invocation: true
---
Where the files live: ROOT is `${CLAUDE_PLUGIN_ROOT}`. If that text does not start with a slash, ROOT is the current folder (a clone of the repo). The validator, tools and data are under ROOT. Files you save for the user go in the current folder, never under ROOT. When you tell the user about a file under ROOT, write its real path, not the word ROOT.

Run this one command with the Bash tool and nothing else:

`python3 -I ROOT/.claude/skills/scriptcraft/scripts/script_check.py $ARGUMENTS --open-items`

Copy the command's output into your reply as it is (the grouped list is short, and the user cannot see tool output). Then add one line on what blocks `--final` and who is asked most often. Do not edit the script.
