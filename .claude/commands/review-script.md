---
description: Independent review of a script file by the script-reviewer agent (facts, voice, verdict)
argument-hint: <path to the script file>
disable-model-invocation: true
---
Review the script at $ARGUMENTS.

Where the files live: ROOT is `${CLAUDE_PLUGIN_ROOT}`. If that text does not start with a slash, ROOT is the current folder (a clone of the repo). The validator, tools and data are under ROOT. Files you save for the user go in the current folder, never under ROOT. When you tell the user about a file under ROOT, write its real path, not the word ROOT.

Do not read any file yourself. Call the script-reviewer agent once, in the foreground, and wait for it (subagent_type `script-reviewer`; when installed as a plugin its full name is `outdoornorway-marketing:script-reviewer`). Give it the file path as typed (relative to the current folder) and what ROOT is. It reads the notes file beside the script for the brief, reruns the validator itself, and replies compactly: the verdict, the ten scores, blocking findings and the top five fixes, with no pasted validator output or cells. It must not edit the file.

Relay the verdict, the scores and the top five fixes in at most 25 lines. Do not apply any fix unless the user asks. Send no progress message.
