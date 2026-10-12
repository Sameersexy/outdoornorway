---
description: Show where this session's tokens went (calls, context per call, biggest entries)
allowed-tools: Bash(python3 -I tools/transcript_report.py:*)
disable-model-invocation: true
---
!`python3 -I tools/transcript_report.py`

Give the three biggest drivers in three lines and one change that would cut them. If the median context per call is above 150k tokens, say to compact or start a fresh session. See `docs/token-hygiene.md`.
