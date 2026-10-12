---
description: Show the quick start for writers and editors (the commands and the first steps)
disable-model-invocation: true
---
Show the quick start below to the user exactly as written. Then say in one line that `docs/getting-started.md` in the Outdoor Norway repo has the full guide, including the setup steps.

## Quick start

1. Install once. The steps are under "Set up (once)" in `docs/getting-started.md`. If you only write or read scripts, choose the plugin.
2. Start Claude Code in the folder where you want your scripts saved. For a clone, that is the repo folder.
3. Type `/` and pick a command. To write a script: `/script ski-aurora-7day youtube voiceover`
4. Claude saves the script in `content/scripts/` and tells you what is still open.
5. `/open-items content/scripts/<file>.md` lists everything that still needs a person: footage, permissions, facts to confirm.
6. `/review-script content/scripts/<file>.md` gets an independent second opinion.
7. When you are happy, send the script to Sameer. If you cloned the repo, ask Claude: "commit this and open a pull request".

| Command | Use it to |
|---|---|
| `/script <tour or topic> <platform> [style]` | Write a script. Platform: reels, shorts, tiktok or youtube. Style: voiceover, ugc_talk or ugc_text |
| `/review-script <file>` | Get a review: facts, voice, verdict, top five fixes |
| `/validate <file>` | Run the checker. Add `--final` before anything is published |
| `/open-items <file>` | List what is still unconfirmed, grouped by who confirms it |
| `/tour-data` | Check our prices and dates against the live website |
| `/howto` | Show this quick start again |

If you installed the plugin, type each command with its full name: `/outdoornorway-marketing:script`, `/outdoornorway-marketing:validate` and so on. The short names above work when you cloned the repo.
