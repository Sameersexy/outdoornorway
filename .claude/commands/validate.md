---
description: Run the scriptcraft validator on a script and show only the findings
argument-hint: <path> [--final] [--strict]
allowed-tools: Bash(python3 -I *scriptcraft/scripts/script_check.py*)
disable-model-invocation: true
---
Where the files live: ROOT is `${CLAUDE_PLUGIN_ROOT}`. If that text does not start with a slash, ROOT is the current folder (a clone of the repo). The validator, tools and data are under ROOT. Files you save for the user go in the current folder, never under ROOT. When you tell the user about a file under ROOT, write its real path, not the word ROOT.

If no file path was given, ask for the path of the script file and stop without running anything. Otherwise run this one command with the Bash tool and nothing else:

`python3 -I ROOT/.claude/skills/scriptcraft/scripts/script_check.py $ARGUMENTS --brief`

If the output says the file cannot be read, say the file was not found and name the path. Otherwise summarize the result in two lines. For each FAIL, name the fix in a few words (`--explain RULE_ID` prints what a rule counts). Do not paste the full output and do not rerun the validator.
