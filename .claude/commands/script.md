---
description: Write an Outdoor Norway video script with the scriptcraft rules (Reels, Shorts, TikTok, YouTube)
argument-hint: <tour id or topic> <platform> [voiceover|ugc_talk|ugc_text]
disable-model-invocation: true
---
Write a video script for: $ARGUMENTS

Where the files live: ROOT is `${CLAUDE_PLUGIN_ROOT}`. If that text does not start with a slash, ROOT is the current folder (a clone of the repo). The validator, tools and data are under ROOT. Files you save for the user go in the current folder, never under ROOT. When you tell the user about a file under ROOT, write its real path, not the word ROOT.

Do not read, list or grep any file yourself. Call the script-writer agent once, in the foreground, and wait for it (subagent_type `script-writer`; when installed as a plugin its full name is `outdoornorway-marketing:script-writer`). Give it the request exactly as typed and what ROOT is, and tell it to save its files in the current folder with relative paths. It saves the script and a notes file, and replies briefly.

- Ask the user a question only when the tour or the platform is missing from the request. Everything else has a default that the agent knows.
- If the request names a web page, fetch its text first, save it as `content/sources/<slug>.txt` in the current folder, and give the agent that path as a source.
- If the agent says the tour id is unknown, show the ids it lists and stop.
- If the request has no real moment from a real guide, add one line pointing to the intake form `ROOT/.claude/skills/scriptcraft/assets/guide-moment-intake.md`.

Reply once, in at most 15 lines: the agent's short reply and the path of the notes file. Do not paste the script. Send no progress message, and do not check the files afterwards: the agent's validator lines are the proof. Offer `/review-script` as the next step in one short line.
