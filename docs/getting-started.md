# Getting started: scripts with Claude Code

For writers and video editors at Outdoor Norway. You do not need to know how to code.

## What this is

A set of tools that lives in this GitHub repo. It writes and checks video scripts (Reels, Shorts, TikTok, YouTube) for our tours. A checker enforces the rules: length, one idea per video, facts only from our tour data, no promises about snow or the northern lights, and who the person on camera is. Claude does the writing. The checker does not let a script through when it breaks a rule.

## Words used here

- **Claude Code:** the app where you type to Claude. Typing `/` in it opens the list of commands.
- **Terminal:** the window where you type commands. On a Mac it is called Terminal. On Windows, use PowerShell. The [terminal guide](https://code.claude.com/docs/en/terminal-guide) shows how to open one.
- **Plugin:** the tools, installed once from GitHub. It works from any folder. Choose this if you only write or read scripts.
- **Clone:** a full copy of the repo on your computer. Choose this if you also edit the tools or send changes through GitHub.
- **Claude chat:** the chat on claude.ai, in the browser or the app. It has no slash commands. See "Use it in Claude chat".
- **Checker:** the program behind `/validate`. It enforces the rules, so a script cannot pass while it breaks one.
- **Beat:** one step of a script, one row of the table, with its seconds.
- **Placeholder:** a `[VERIFY: what, who]` marker. It means a fact is missing or not confirmed by the named person.
- **Pull request:** a request for Sameer to add your changes to the repo.

## Quick start

1. Install once. The steps are under "Set up (once)" in `docs/getting-started.md`. If you only write or read scripts, choose the plugin.
2. Start Claude Code in any folder you can find again. Files appear there only when you ask for `save`. For a clone, use the repo folder.
3. Ask the tour guide the ten questions on the intake form (see "For writers") and keep their answers. Skip this only for a quick generic draft.
4. Type `/` and pick a command. To write a script: `/script ski-aurora-7day youtube voiceover`
5. The script comes back in the chat as text, with its notes and what is still open. Copy it into Google Docs and tweak it there. Add the word `save` at the end of the request if you want files in `content/scripts/` instead.
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

## Set up (once)

You need three things: a Claude account, Claude Code, and Python 3.

1. **A Claude account.** Claude Code needs a paid Claude plan (Pro, Max, Team or Enterprise) or a Claude Console account, according to the official quickstart.
2. **Claude Code.** Follow Step 1 of the [Claude Code quickstart](https://code.claude.com/docs/en/quickstart). It gives one command for each system (Mac, Linux, Windows). If you have never used a terminal, read the [terminal guide](https://code.claude.com/docs/en/terminal-guide) first. When it is installed, open a new terminal window and run `claude --version`. It should print a version number.
3. **Python 3.** The checker is a Python script. Open a terminal and run `python3 --version`. If it prints a version number, you are set. If it says the command is not found, install Python 3 from the [official Python download page](https://www.python.org/downloads/) and try again. The commands call `python3`, and on Windows that name may not exist. [VERIFY: confirm the checker runs on Windows]

Optional, keeps usage down: cap how long a session can grow, and remove the Artifact tool, which this work never uses. Put this in the file `settings.json` inside the `.claude` folder in your home folder (create the file if it is not there):

```
{ "autoCompactWindow": 200000, "permissions": { "deny": ["Artifact"] } }
```

If the file already has settings, add the two entries inside the existing braces with commas. If it already has a `permissions` entry, add `"Artifact"` to its `deny` list. Claude Code then summarises a long conversation at about 200k tokens, and the first step of every session reads about 11,000 fewer tokens (one measured run). Restart Claude Code after the change.

Then pick one way to add our tools.

**Option A: install the plugin (works from any folder).** In a terminal, run these two lines:

```
claude plugin marketplace add Sameersexy/outdoornorway
claude plugin install outdoornorway-marketing@outdoornorway
```

Or type `/plugin` inside Claude Code and add the marketplace `Sameersexy/outdoornorway`, then install `outdoornorway-marketing`. (A marketplace is a list of plugins that lives on GitHub.) Restart Claude Code. To update later: `claude plugin marketplace update outdoornorway`, then `claude plugin update outdoornorway-marketing@outdoornorway`, then restart Claude Code.

**Option B: clone the repo (best if you will also edit files and send pull requests).** Run:

```
git clone https://github.com/Sameersexy/outdoornorway.git
cd outdoornorway
claude
```

Update later with `git pull`. The commands work in the repo folder. Start Claude Code there.

**Check it works.** Type `/`. You should see `/script`, `/review-script`, `/validate`, `/open-items`, `/tour-data` and `/howto`.

The repo is public: you can read and clone it without an invitation. To save work back you need a GitHub account and either an invitation from Sameer (to push a branch) or your own fork. See "Without write access". Do not put anything confidential in this repo: everyone can read it.

You do not need `npx` or any other package manager. The two plugin lines above are the whole install.

## Without write access

If Sameer has not added you as a collaborator, you cannot push a branch here. The easiest route is to send the script file to Sameer. If you want to use GitHub: click Fork on the repo's page, work in your fork, then open a pull request (a request for Sameer to add your changes). Scripts for real tours are drafts until Sameer confirms the facts, so send them even if open items remain.

## For writers

Ask for one script per session. Examples:

- `/script ski-aurora-7day youtube voiceover` (a long YouTube video, a calm voiceover over footage)
- `/script 3-day ski and snowshoe tiktok ugc_talk` (a short TikTok where a guide talks to the phone)

What you get is the script as text in the chat. It has a table of beats (what is said, what is shown, what text is on screen) and a description with chapter lines for YouTube. Under it come the notes: the brief, the open items by who confirms them, assumptions and one alternative hook, then the checker's result lines. Copy it into Google Docs from there.

- **Two scripts for one tour:** `/script ski-6day shorts voiceover and reels ugc_talk`. Both come back in one reply, each with its own checker result. A third script, or a second tour in the same request, is refused. Run `/script` again for that.
- **Files:** end the request with `save`, for example `/script ski-aurora-7day youtube voiceover save`. Claude then writes the script and a notes file (same name, ending `-notes.md`) in `content/scripts/` in the current folder.
- **Creator brief:** ask for it when a guide or guest will film the video. It is not added by default.

Things to know:

- **A guide's words are never invented.** If nobody gave a real moment from a real trip, the script has slots marked `[VERIFY: ...]`. Give the tour guide the intake form `.claude/skills/scriptcraft/assets/guide-moment-intake.md` (ten short questions; you can open it on GitHub) and give Claude their answers.
- **Facts come from `campaigns/ski-meta-ads/tours.json`**, `.claude/product-marketing.md` or a page we name. Do not type prices or dates into a script by hand. If a price looks wrong, run `/tour-data`.
- **Changes:** tell Claude what to change in plain words. It runs the checker again and must keep it passing.
- **Ready to publish** means: the checker says `RESULT: PASS` in final mode and nothing is still open. For a saved file, that is `/validate <file> --final --strict` and `/open-items <file>`. Until then it is a draft. Do not remove a `[VERIFY]` marker yourself unless the person named in it has confirmed.
- **Cost:** see "Keep your usage low" below.

## Use it in Claude chat

The same writing and checking rules work in the Claude chat on claude.ai. Chat has no slash commands. You upload the skill once as a zip file, then ask for a script in plain words.

Sameer sends you the zip (`scriptcraft.zip`). If you cloned the repo, you can build it yourself with `python3 -I tools/build_chat_skill.py`. It is written to `dist/scriptcraft.zip` and is not stored in the repo.

Upload it once:

1. Open claude.ai and go to Customize, then Skills. [VERIFY: confirm current menu label for claude.ai skills. The how-to page links to a Customize page for skills, and another source says Settings, then Features or Capabilities]
2. Upload the zip as it is. Do not unzip it first.
3. Switch the skill on.
4. Check that code execution is on in your settings. The checker is a Python script and only runs there. [VERIFY: confirm the setting name and plan availability]

Use it: start a new chat and ask in plain words, for example "Write a Reels voiceover script for ski-6day". The script comes back in the chat with its notes and the checker's result. To get a review, say "review this script" and paste it.

If code execution is off, the skill still writes by the rules. It says the checker was not run and lists the checks to do by hand. Treat that as a draft.

Good to know:

- The facts in the zip are a snapshot of `campaigns/ski-meta-ads/tours.json` from the day the zip was built. After prices or dates change, build a new zip and upload it again.
- A custom skill belongs to your own account. Team and Enterprise plans have Share and Publish controls.
- Sources: the [Claude skills how-to](https://claude.com/docs/skills/how-to) and the [Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).

## Keep your usage low

Claude Code reads the whole conversation again on every step, so a long session costs far more than a short one. These habits cut the most:

- One script per session. Start a new session for the next one.
- Run `/review-script` once per script, after the checks pass, not after every edit.
- Do not resume yesterday's session. Start a new one and paste the script, or point Claude at the saved script file and its notes file.
- If Claude gets something wrong twice in a row, type `/clear` and ask again with the fix in your first sentence.
- Type `/context` to see how full the session is. Above about 150k tokens, type `/compact`.
- Do not use workflows or agent teams for one script.
- Switch off plugins and connectors you do not use, because each one adds text to every step. `claude plugin list` shows them and `claude plugin details <plugin id>` shows what each adds. `claude plugin disable <plugin id>` turns one off. For connectors, use `/mcp` or the connector settings on claude.ai. Only you can do this, in your own account.
- If you cloned the repo and only need pass or fail, run the checker in a terminal, with no Claude: `python3 -I .claude/skills/scriptcraft/scripts/script_check.py content/scripts/<file>.md --brief`

## For video editors

You can read scripts without Claude. Open `content/scripts/` on GitHub and click a file. Each script has a notes file beside it with open items and shoot notes.

How to read the table:

| Column | Meaning |
|---|---|
| beat, time | The step and its seconds, for example `8-19` |
| voiceover | What is said. `[PAUSE 2]` is two seconds of natural sound |
| visual | What to show. `one take:` is a single continuous shot. `selfie`, `POV` and `chest mount` mean phone footage |
| text | The on-screen text, in sentence case, for viewers watching without sound |
| role | What the beat does (hook, explain, payoff, cta). A tag like `ch:2` puts the beat in YouTube chapter 2 |
| facts | The source rows behind the claims in that beat |

`[VERIFY: what, who]` means not confirmed. Do not film it, cut it or publish it until the named person has confirmed. Run `/open-items <file>` for the full list.

Editor's checklist for each script:

1. **Who is on camera** and what they say about their role in the first 5 seconds. It must also be on screen.
2. **Releases.** No identifiable guest in a shot without a written release. Under 18 needs a guardian's written consent. [VERIFY with counsel]
3. **Permissions** for places and operators named in the visuals (resorts, airports, boat, dog yard).
4. **Safety.** Off-piste or touring clips show beacon, shovel and probe, the guide in position and spacing on slopes. No closed terrain, no jumps with guests, no helmets off in moving shots, no guest unguided in avalanche terrain. Details: section "Safety on camera" in `.claude/skills/scriptcraft/references/ugc-style.md`.
5. **Sky shots** are real evenings. No composited or AI sky (see the shoot notes beside the aurora script).
6. **UGC style:** no logo, no end card, no title card, no stock footage, native text. Natural sound or a licensed track. No trending song on a post that names the brand, a trip or a price.
7. **YouTube:** copy the chapter lines from the description (the caption block of the script). There are at least three, the first is `0:00`, each is at least 10 seconds after the last, each starts on a beat, and each has a title.

## Who does what

| Person | Does |
|---|---|
| Sameer | Confirms facts and `[VERIFY]` items with the client, reviews and merges pull requests, invites people |
| Writer | Runs `/script` and `/review-script`, gets guide answers, fixes the open items |
| Editor | Reads scripts, flags what cannot be filmed, checks releases and permissions, cuts the video |
| Guides | Answer the ten intake questions and film the segments |

## If something goes wrong

- **No commands when you type `/`.** If you installed the plugin, restart Claude Code and run `claude plugin list` to check it is enabled. If you cloned the repo, start Claude Code inside the repo folder.
- **"Usage limit reached".** Wait for the reset. Use one script per session next time. See `docs/token-hygiene.md`.
- **`PARSE ERROR line N`.** The script file format is broken at that line. Ask Claude to repair it.
- **`[FAIL] BR13`.** Placeholders (the `[VERIFY: ...]` markers) are still in the script, and BR13 is the check that blocks the final version until they are gone. Expected until the people named in them confirm.
- **A rule id you do not understand,** for example `F04`: ask Claude "explain rule F04".
- **`/tour-data` cannot reach the site.** It needs internet access to the Outdoor Norway pages. If your session blocks outside websites, tell Sameer.

## For Sameer (admin)

- Invite people who need to push: on GitHub, repo Settings, Collaborators, Add people. On a personal account a collaborator can push.
- Ask everyone to work on a branch and open a pull request, then review and merge. Branch protection on `main` is available for public repos on the free plan. [VERIFY: confirm on the current plan]
- The repo is public. Do not add supplier terms, customer or staff personal data, or other private client information. The existing page-audit notes in `campaigns/ski-meta-ads/` stay public on purpose (owner decision, 12 October 2026).
- Your own usage: long sessions and the plugins and connectors that add overhead to every step cost the most. Settings to review (auto-compact window, plugins and connectors to switch off, the Artifact tool) are in `docs/token-hygiene.md`.
- Build the Claude chat zip with `python3 -I tools/build_chat_skill.py` and send `dist/scriptcraft.zip` to the writers. Rebuild it when `tours.json`, the rules or the skill text change.
- When you change the tools, bump `version` in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` so installed copies update.
