# Getting started: scripts with Claude Code

For writers and video editors at Outdoor Norway. You do not need to know how to code.

## What this is

A set of tools that lives in this GitHub repo. It writes and checks video scripts (Reels, Shorts, TikTok, YouTube) for our tours. A checker enforces the rules: length, one idea per video, facts only from our tour data, no promises about snow or the northern lights, and who the person on camera is. Claude does the writing. The checker does not let a script through when it breaks a rule.

## Words used here

- **Claude Code:** the app where you type to Claude. Typing `/` in it opens the list of commands.
- **Terminal:** the window where you type commands. On a Mac it is called Terminal. On Windows, use PowerShell. The [terminal guide](https://code.claude.com/docs/en/terminal-guide) shows how to open one.
- **Plugin:** the tools, installed once from GitHub. It works from any folder. Choose this if you only write or read scripts.
- **Clone:** a full copy of the repo on your computer. Choose this if you also edit the tools or send changes through GitHub.
- **Checker:** the program behind `/validate`. It enforces the rules, so a script cannot pass while it breaks one.
- **Beat:** one step of a script, one row of the table, with its seconds.
- **Placeholder:** a `[VERIFY: what, who]` marker. It means a fact is missing or not confirmed by the named person.
- **Pull request:** a request for Sameer to add your changes to the repo.

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

## Set up (once)

You need three things: a Claude account, Claude Code, and Python 3.

1. **A Claude account.** Claude Code needs a paid Claude plan (Pro, Max, Team or Enterprise) or a Claude Console account, according to the official quickstart.
2. **Claude Code.** Follow Step 1 of the [Claude Code quickstart](https://code.claude.com/docs/en/quickstart). It gives one command for each system (Mac, Linux, Windows). If you have never used a terminal, read the [terminal guide](https://code.claude.com/docs/en/terminal-guide) first. When it is installed, open a new terminal window and run `claude --version`. It should print a version number.
3. **Python 3.** The checker is a Python script. Open a terminal and run `python3 --version`. If it prints a version number, you are set. If it says the command is not found, install Python 3 from the [official Python download page](https://www.python.org/downloads/) and try again. The commands call `python3`, and on Windows that name may not exist. [VERIFY: confirm the checker runs on Windows]

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

What you get is a file in `content/scripts/` with a table of beats (what is said, what is shown, what text is on screen) and a description with chapter lines for YouTube. Claude also lists open items.

Things to know:

- **A guide's words are never invented.** If nobody gave a real moment from a real trip, the script has slots marked `[VERIFY: ...]`. Give the tour guide the intake form `.claude/skills/scriptcraft/assets/guide-moment-intake.md` (ten short questions; you can open it on GitHub) and give Claude their answers.
- **Facts come from `campaigns/ski-meta-ads/tours.json`**, `.claude/product-marketing.md` or a page we name. Do not type prices or dates into a script by hand. If a price looks wrong, run `/tour-data`.
- **Changes:** tell Claude what to change in plain words. It must keep `/validate` passing.
- **Ready to publish** means: `/validate <file> --final --strict` says `RESULT: PASS` and `/open-items <file>` shows nothing open. Until then it is a draft. Do not remove a `[VERIFY]` marker yourself unless the person named in it has confirmed.
- **Cost:** each script runs extra Claude helper sessions (the agents), and they count against your Claude usage limit. One script per session, and run `/review-script` once, not after every edit.

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
- When you change the tools, bump `version` in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` so installed copies update.
