---
description: Show the quick start for writers and editors (the commands and the first steps)
disable-model-invocation: true
---
Show the quick start below to the user exactly as written. Then say in one line that `docs/getting-started.md` in the Outdoor Norway repo has the full guide, including the setup steps.

## Quick start

1. Install once. The steps are under "Set up (once)" in `docs/getting-started.md`. If you only write or read scripts, choose the plugin.
2. Start Claude Code in any folder you can find again. Files appear there only when you ask for `save`. For a clone, use the repo folder.
3. If the reply ends with ten questions for the guide, copy that block and send it to the tour guide, then give Claude their answers. Skip this only for a quick generic draft.
4. Type `/` and pick a command. To write a script: `/script ski-aurora-7day youtube voiceover`
5. The script comes back in the chat as text, with its notes and what is still open. Copy it into Google Docs and tweak it there. Add the word `save` at the end of the request if you want files in `content/scripts/` as well.
6. The notes under the script list everything that still needs a person: footage, permissions, facts to confirm. For a saved file, `/open-items content/scripts/<file>.md` gives the same list.
7. `/review-script` with the script pasted after it gets an independent second opinion. A saved file path works too.
8. When you are happy, send the script to Sameer. If you cloned the repo and saved files, ask Claude: "commit this and open a pull request".

| Command | Use it to |
|---|---|
| `/script <tour or topic> <platform> [style] [save]` | Write a script as text in the chat. Platform: reels, shorts, tiktok or youtube. Style: voiceover, ugc_talk or ugc_text. Add `save` to also write files. Add `and <platform> <style>` for a second script on the same tour |
| `/review-script <file or pasted script>` | Get a review: facts, voice, verdict, top five fixes |
| `/validate <file>` | Run the checker. Add `--final` before anything is published |
| `/open-items <file>` | List what is still unconfirmed, grouped by who confirms it |
| `/tour-data` | Check our prices and dates against the live website |
| `/howto` | Show this quick start again |

If you installed the plugin, type each command with its full name: `/outdoornorway-marketing:script`, `/outdoornorway-marketing:validate` and so on. The short names above work when you cloned the repo.

To use the same skill in the Claude chat on claude.ai, see "Use it in Claude chat" in `docs/getting-started.md`.
