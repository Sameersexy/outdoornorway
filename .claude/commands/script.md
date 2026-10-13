---
description: Write an Outdoor Norway video script with the scriptcraft rules. The script comes back as text in the chat (Reels, Shorts, TikTok, YouTube)
argument-hint: <tour id or topic> <platform> [voiceover|ugc_talk|ugc_text] [and <platform> <style>] [save]
disable-model-invocation: true
---
Write a video script for: $ARGUMENTS

Where the files live: ROOT is `${CLAUDE_PLUGIN_ROOT}`. If that text does not start with a slash, ROOT is the current folder (a clone of the repo). The validator, tools and data are under ROOT. Files you save for the user go in the current folder, never under ROOT. When you tell the user about a file under ROOT, write its real path, not the word ROOT.

Do not read, list or grep any file yourself. Call the script-writer agent once, in the foreground, and wait for it (subagent_type `script-writer`; when installed as a plugin its full name is `outdoornorway-marketing:script-writer`). Give it the request exactly as typed and what ROOT is.

Output is text in the chat. The agent validates in a scratch folder and writes no file in the user's folder, unless the request ends with the word `save`. With `save` it writes the script and its notes to `content/scripts/` in the current folder, with relative paths, and replies with the same text plus the paths.

Pair mode: one request may name two scripts when both use the same tour, for example `ski-6day shorts voiceover and reels ugc_talk`. The agent writes both, each with its own validator pass. A third script, or two different tours, is refused by the agent with a one-line reason. Show that reason and stop.

- Ask the user a question only when the tour or the platform is missing from the request. Everything else has a default that the agent knows.
- If the request names a web page, fetch its text first and give the agent the URL and the text as a source. Write no file for it.
- If the agent says the tour id is unknown, show the ids it lists and stop.
- If the request has no real moment from a real guide, add one line pointing to the intake form `ROOT/.claude/skills/scriptcraft/assets/guide-moment-intake.md`.

Print the agent's reply in full, unchanged: each script in its fenced block, then its notes and its validator lines. This is the one place where the repo prints a whole script. Add no summary of your own. Send no progress message, and do not check files afterwards: the agent's validator lines are the proof. End with one line naming the next step: `/review-script` with the script pasted after it.
