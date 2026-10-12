---
description: Independent review of a script file by the script-reviewer agent (facts, voice, verdict)
argument-hint: <path to the script file>
disable-model-invocation: true
---
Review the script at $ARGUMENTS with the script-reviewer agent (subagent_type script-reviewer).

Tell the agent: the file path; the brief the writer worked from, if known (platform, audience, relationship, allowed fact sources, the objection); that it must rerun the validator itself in draft and --final mode; and that it must reply compactly (verdict, the ten scores, blocking findings, the top five fixes, no pasted validator output, no pasted cells). Do not edit the file.

Relay the verdict, the scores and the top five fixes in at most 25 lines. Do not apply any fix unless the user asks.
