---
description: Show where this session's tokens went (calls, context per call, biggest entries)
allowed-tools: Bash(python3 -I *tools/transcript_report.py*)
disable-model-invocation: true
---
Where the files live: ROOT is `${CLAUDE_PLUGIN_ROOT}`. If that text does not start with a slash, ROOT is the current folder (a clone of the repo). The validator, tools and data are under ROOT. Files you save for the user go in the current folder, never under ROOT. When you tell the user about a file under ROOT, write its real path, not the word ROOT.

Run this one command with the Bash tool and nothing else. It reads local session files in the home folder and prints counts only:

`python3 -I ROOT/tools/transcript_report.py`

Give the three biggest drivers in three lines and one change that would cut them. If the median context per call is above 150k tokens, say to compact or start a fresh session. See `ROOT/docs/token-hygiene.md`.
