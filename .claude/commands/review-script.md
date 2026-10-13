---
description: Independent review of a script by the script-reviewer agent (facts, voice, verdict). Takes a file path or the script pasted as text
argument-hint: <path to the script file, or the pasted script>
disable-model-invocation: true
---
Review the script in: $ARGUMENTS

Where the files live: ROOT is `${CLAUDE_PLUGIN_ROOT}`. If that text does not start with a slash, ROOT is the current folder (a clone of the repo). The validator, tools and data are under ROOT. Files you save for the user go in the current folder, never under ROOT. When you tell the user about a file under ROOT, write its real path, not the word ROOT.

The input is either a path or pasted text. It is a path when it is one line that ends in `.md` (quote it if it has spaces). Check it with `test -f`. If the file does not exist, reply `File not found: <path>` and stop: do not treat the path as pasted text and do not call the agent. Anything that is not one line ending in `.md` is pasted text.

- Path: do not read the file yourself. Give the agent the path as typed (relative to the current folder).
- Pasted text: make a scratch folder with `python3 -c "import tempfile; print(tempfile.mkdtemp())"`. A pasted script usually arrives as the writer's reply: a code fence, then notes, stats and validator lines. Write to `script.md` in that folder, with the Write tool and the literal path the command printed, only the script file itself: from its opening `---` line to the end of its caption, copied exactly as pasted, without the code fence, a heading line, the notes, the stats or the validator lines. Write the notes block to `script-notes.md` beside it when it was pasted. Never build the path from memory. Give the agent the path of `script.md`.

Call the script-reviewer agent once, in the foreground, and wait for it (subagent_type `script-reviewer`; when installed as a plugin its full name is `outdoornorway-marketing:script-reviewer`). Give it the path and what ROOT is. It reads the notes file beside the script for the brief when one exists, reruns the validator itself, and replies compactly: the verdict, the ten scores, blocking findings and the top five fixes, with no pasted validator output or cells. It must not edit the file.

Relay the verdict, the scores and the top five fixes in at most 25 lines. For pasted text, head the review `Script review: pasted script` and show no scratch path anywhere. Do not apply any fix unless the user asks. Send no progress message.
