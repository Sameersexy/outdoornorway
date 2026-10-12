# Getting started: scripts with Claude Code

For writers and video editors at Outdoor Norway. You do not need to know how to code.

## What this is

A set of tools that lives in this GitHub repo. It writes and checks video scripts (Reels, Shorts, TikTok, YouTube) for our tours. A checker enforces the rules: length, one idea per video, facts only from our tour data, no promises about snow or the northern lights, and who the person on camera is. Claude does the writing. The checker does not let a script through when it breaks a rule.

## Quick start

1. Open this repo in Claude Code (setup is below, once).
2. Type `/` and pick a command, or type it. To write a script: `/script ski-aurora-7day youtube voiceover`
3. Claude saves the script in `content/scripts/` and tells you what is still open.
4. `/open-items content/scripts/<file>.md` lists everything that still needs a person: footage, permissions, facts to confirm.
5. `/review-script content/scripts/<file>.md` gets an independent second opinion.
6. When you are happy, ask Claude: "commit this and open a pull request". Sameer reviews it.

| Command | Use it to |
|---|---|
| `/script <tour or topic> <platform> [style]` | Write a script. Platform: reels, shorts, tiktok or youtube. Style: voiceover, ugc_talk or ugc_text |
| `/review-script <file>` | Get a review: facts, voice, verdict, top five fixes |
| `/validate <file>` | Run the checker. Add `--final` before anything is published |
| `/open-items <file>` | List what is still unconfirmed, grouped by who confirms it |
| `/tour-data` | Check our prices and dates against the live website |
| `/howto` | Show this quick start again |

## Set up (once)

1. **GitHub access.** The repo is private. Sameer invites you; accept the email invitation from GitHub. You need a GitHub account.
2. **A Claude account that includes Claude Code.** [VERIFY: confirm which Claude plans include Claude Code]
3. **Pick one way to run it.**
   - Easiest, nothing to install: Claude Code on the web at claude.ai/code. Connect GitHub, choose the repo `Sameersexy/outdoornorway`, start a session. [VERIFY: confirm the current steps in the Claude Code app]
   - Terminal: install Claude Code, then run `git clone https://github.com/Sameersexy/outdoornorway.git`, `cd outdoornorway`, `claude`. Git will ask you to sign in to GitHub.
4. **Check it works.** Type `/`. You should see `/script`, `/review-script`, `/validate`, `/open-items`, `/tour-data` and `/howto`. If not, you are not inside the repo: restart the session from the repo.

To use the same tools in a different project, install the plugin: `/plugin install outdoornorway-marketing --marketplace Sameersexy/outdoornorway`.

## For writers

Ask for one script per session. Examples:

- `/script ski-aurora-7day youtube voiceover` (a long YouTube video, a calm voiceover over footage)
- `/script 3-day ski and snowshoe tiktok ugc_talk` (a short TikTok where a guide talks to the phone)

What you get is a file in `content/scripts/` with a table of beats (what is said, what is shown, what text is on screen) and a description with chapter lines for YouTube. Claude also lists open items.

Things to know:

- **A guide's words are never invented.** If nobody gave a real moment from a real trip, the script has slots marked `[VERIFY: ...]`. Send the guide `.claude/skills/scriptcraft/assets/guide-moment-intake.md` (ten short questions) and give Claude the answers.
- **Facts come from `campaigns/ski-meta-ads/tours.json`**, `.claude/product-marketing.md` or a page we name. Do not type prices or dates into a script by hand. If a price looks wrong, run `/tour-data`.
- **Changes:** tell Claude what to change in plain words. It must keep `/validate` passing.
- **Ready to publish** means: `/validate <file> --final --strict` says `RESULT: PASS` and `/open-items <file>` shows nothing open. Until then it is a draft. Do not remove a `[VERIFY]` marker yourself unless the person named in it has confirmed.
- **Cost:** each script uses the agents, which use real usage. One script per session, and run `/review-script` once, not after every edit.

## For video editors

You can read scripts without Claude. Open `content/scripts/` on GitHub and click a file. Each script has a notes file beside it with open items and shoot notes.

How to read the table:

| Column | Meaning |
|---|---|
| beat, time | The step and its seconds, for example `8-19` |
| voiceover | What is said. `[PAUSE 2]` is two seconds of natural sound |
| visual | What to show. `one take:` is a single continuous shot. `selfie`, `POV` and `chest mount` mean phone footage |
| text | The on-screen text, in sentence case, for viewers watching without sound |
| role | What the beat does (hook, explain, payoff, cta). Chapter beats start a YouTube chapter |
| facts | The source rows behind the claims in that beat |

`[VERIFY: what, who]` means not confirmed. Do not film it, cut it or publish it until the named person has confirmed. Run `/open-items <file>` for the full list.

Editor's checklist for each script:

1. **Who is on camera** and what they say about their role in the first 5 seconds. It must also be on screen.
2. **Releases.** No identifiable guest in a shot without a written release. Under 18 needs a guardian's written consent.
3. **Permissions** for places and operators named in the visuals (resorts, airports, boat, dog yard).
4. **Safety.** Guides film only at a planned stop or with a chest mount while leading a group. No guests at a road edge in the dark.
5. **Sky shots** are filmed as they are. Nothing added, no composited sky.
6. **UGC style:** no logo, no end card, no title card, no stock footage, native text. Natural sound or a licensed track. No trending song on a post that names the brand, a trip or a price.
7. **YouTube:** copy the chapter lines from the description. The first is `0:00`, and each is on a beat start.

## Who does what

| Person | Does |
|---|---|
| Sameer | Confirms facts and `[VERIFY]` items with the client, reviews and merges pull requests, invites people |
| Writer | Runs `/script` and `/review-script`, gets guide answers, fixes the open items |
| Editor | Reads scripts, flags what cannot be filmed, checks releases and permissions, cuts the video |
| Guides | Answer the ten intake questions and film the segments |

## If something goes wrong

- **No commands when you type `/`.** You are not in the repo folder or the session did not start from the repo.
- **"Usage limit reached".** Wait for the reset. Use one script per session next time. See `docs/token-hygiene.md`.
- **`PARSE ERROR line N`.** The script file format is broken at that line. Ask Claude to repair it.
- **`[FAIL] BR13`.** Placeholders are still in the script. Expected until the people named in them confirm.
- **A rule id you do not understand,** for example `F04`: ask Claude "explain rule F04".
- **`/tour-data` cannot reach the site.** The session may block outside websites. [VERIFY: check the session's network setting]

## For Sameer (admin)

- Invite people: on GitHub, repo Settings, Collaborators, Add people. On a personal account a collaborator can push. [VERIFY: confirm the permission level on a personal private repo]
- Ask everyone to work on a branch and open a pull request, then review and merge. Protecting `main` may need a paid GitHub plan for a private repo. [VERIFY: confirm on the current plan]
- When you change the tools, bump `version` in `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` so installed copies update.
