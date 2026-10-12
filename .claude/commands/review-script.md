---
description: Independent review of a script file by the script-reviewer agent (facts, voice, verdict)
argument-hint: <path to the script file>
disable-model-invocation: true
---
Where the files live: ROOT is `${CLAUDE_PLUGIN_ROOT}`. If that text does not start with a slash, ROOT is the current folder (a clone of the repo). The validator, tools and data are under ROOT. Files you save for the user go in the current folder, never under ROOT. When you tell the user about a file under ROOT, write its real path, not the word ROOT.

Review the script at $ARGUMENTS with the script-reviewer agent (subagent_type `script-reviewer`; when installed as a plugin its full name is `outdoornorway-marketing:script-reviewer`). Tell the agent what ROOT is.

Tell the agent: the file path; the brief the writer worked from, if known (platform, audience, relationship, allowed fact sources, the objection); that it must rerun the validator itself in draft and --final mode; and that it must reply compactly (verdict, the ten scores, blocking findings, the top five fixes, no pasted validator output, no pasted cells). Do not edit the file.

Relay the verdict, the scores and the top five fixes in at most 25 lines. Do not apply any fix unless the user asks.

Do not send a progress message such as "the agent is working". Wait for the agent, then reply once with the result.
