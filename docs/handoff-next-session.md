# Handoff: text-first scripts and the Claude chat package

This file lets a fresh Claude Code session finish the work that was planned on 13 October 2026 for the Outdoor Norway marketing repo, without reading the old conversation. Delete it in the last commit of the work it describes.

## 1. Start here

- Branch: `claude/confident-cannon-1on6av`. Before this file was added it equalled `origin/main` at `f4864d0` (the squash of PR 7). The working tree was clean.
- No implementation file has been changed yet. Everything below is analysis, measurements and design. The only new file is this one.
- Read this file, then only the files named in each work package. `CLAUDE.md` loads by itself.
- One deliverable per session (CLAUDE.md). This deliverable is "text-first scripts plus the Claude chat package", with decisions 1 and 2 attached.
- Do not open a pull request unless the user asks.
- Last known test counts at `f4864d0`: 277 validator tests, 22 repo integrity tests. Rerun both before starting to confirm the baseline.

## 2. What the user asked for

The user's latest instruction, quoted as written:

> lets do 1, 2, 4, we dont need to do anything on clickup so that is unnessary at the moment i have to copy and paste it in google docs and make minor tweaks and then send it to click up. These are own videos and files 6th is just out of no where. 7 unnessary and 8 we dont need to draft a repo the output should be within the cclaude code chat as a text and i want to use this within claude chat as well

Two requirements follow from it:

1. Script output appears in the Claude Code chat as text. Files only when asked.
2. The skill must also work inside claude.ai chat, so it needs a skill zip the user can upload.

## 3. How the eight earlier decisions were read

| # | Decision | Reading | Status |
|---|---|---|---|
| 1 | Deny the Artifact tool | Do it | Not started |
| 2 | Switch off unused plugins and connectors | Do it as a keep-or-disable table with exact steps. Only the user can click it in their own account. No repo commit | Not started |
| 3 | Cheaper model test | The user did not mention it, so it is not done | Dropped |
| 4 | Allow two scripts per run when they share a tour | Do it ("pair mode") | Not started |
| 5 | `/to-clickup` command | The user pastes into Google Docs, tweaks, then sends to ClickUp by hand. ClickUp stays read-only and out of the repo | Dropped |
| 6 | Release scope and counsel | The user says these are their own videos and files | Dropped |
| 7 | Editing app | Unnecessary | Dropped |
| 8 | Publication question about section 2 of `docs/research/ad-copy/07-outdoor-norway-voice-and-category.md` | "we dont need to draft a repo" is read as "not meant to be published, remove it". This reading is ambiguous. Do it as its own commit and flag it | Not started |

## 4. Work packages

Run packages A and B in parallel if a workflow is used. They touch different files. Do C to F yourself afterwards, because they edit shared docs.

### A. Text-first `/script` with pair mode and `save` (decision 4)

Files: `.claude/commands/script.md`, `.claude/commands/review-script.md`, `.claude/agents/script-writer.md`, `.claude/agents/script-reviewer.md`, and step 7 of `.claude/skills/scriptcraft/SKILL.md`.

Design:

- The writer validates in a scratch folder. It makes one with a Python one-liner using `tempfile.mkdtemp`, prints the path, and then uses that literal path. It never builds a path from memory (an earlier run saved files to a mangled absolute path).
- The reply carries the full script in a fenced block, a short notes block (brief, caption, open items by who confirms, assumptions, accepted warnings, one variant hook and one variant CTA with a hypothesis each), and the validator RESULT line with counts and warning ids. No files are written in the user's folder.
- `save` as the last argument writes the script and notes files to `content/scripts/<yyyy-mm-dd>-<slug>.md` and `...-notes.md` with relative paths, then runs `ls -l` once, as the agent does today.
- Pair mode: up to two scripts per run when both use the same tour, for example `/script ski-6day shorts voiceover and reels ugc_talk`. Facts are pulled once with `--tour`, each script has its own validator pass, and both appear in full. A third script, or two different tours, is refused with a one-line reason. This syntax is my design, so confirm it reads well. [VERIFY: user confirms the pair syntax]
- `/review-script` accepts a path or pasted text. Pasted text goes to the scratch folder, then the reviewer works on that path.
- The command prints the script in full. This is the planned exception to the "do not print whole files" token rule. Update CLAUDE.md to say so.
- Keep: the ROOT note, the "## Where files live" heading, `${CLAUDE_PLUGIN_ROOT}`, no `model:` line in agent front matter, `disable-model-invocation: true` in commands.

### B. Claude chat package (requirement 2)

Files: `tools/build_chat_skill.py`, `tools/chat_skill/` (the chat `SKILL.md` and a reviewer rubric reference), `tools/test_build_chat_skill.py`, one line `dist/` added to `.gitignore`.

Design:

- Zip top level is the skill folder: `scriptcraft/SKILL.md`, `scriptcraft/references/`, `scriptcraft/assets/`, `scriptcraft/examples/`, `scriptcraft/scripts/script_check.py`, `brand_rules.json`, `tiers.json`, `scriptcraft/data/tours.json`, and `.claude/product-marketing.md` as a reference file.
- Leave out `test_script_check.py`, `attack_cases.py`, `fixtures/` and `__pycache__`. The skill folder is 1.2M today, of which scripts are 928K, mostly tests and fixtures. Other sizes: references 112K, examples 32K, assets 36K, `tours.json` 20K, `product-marketing.md` 8K.
- In chat the validator runs as `python3 scripts/script_check.py FILE --tours-file data/tours.json`. `TOURS_FILE` near line 33 of `script_check.py` resolves four folders up from the script, which does not exist in a zip, so always pass `--tours-file`. The `--tour TOUR_ID` flag honours it (checked in the argument help). `--tiers` and `--brand` default to files beside the script.
- The chat `SKILL.md` carries the writer and reviewer procedures itself, because agents and slash commands do not exist in claude.ai chat. Source them from `.claude/agents/script-writer.md`, `script-reviewer.md` and the current SKILL.md.
- Name `scriptcraft` (lowercase letters, numbers and hyphens, up to 64 characters, matching the folder). Keep the description at 200 characters or fewer. The specification allows 1,024, but one source said claude.ai limits it to 200 and that is unconfirmed. [VERIFY: description limit in claude.ai]
- Body under 500 lines. Use relative paths such as `scripts/script_check.py`. The whole folder is copied into the code-execution sandbox, and scripts only run where code execution is on.
- Fallback text for chats without code execution: write by the rules, say the validator was not run, and list the checks to do by hand.
- The builder rewrites or avoids repo paths in the copied references (15 occurrences across 6 files, fixtures excluded). A test checks that no `.claude/`, `campaigns/`, `tools/` or `${CLAUDE_PLUGIN_ROOT}` string survives in the built zip.
- Tests: the zip builds; the top level is `scriptcraft/`; the front matter name matches the folder; description length; line count; excluded files are absent; no path leaks; the validator runs from an unzipped copy on a fixture script; no dashes, emoji or model names in built text files.
- Do not commit the zip. Build it, then send it with SendUserFile (display `attach`).

### C. Decision 1: deny the Artifact tool

- `.claude/settings.json` today holds `enabledPlugins` (`claude-code-setup@anthropic-plugin-directory`) and `autoCompactWindow: 200000`. Add `"permissions": {"deny": ["Artifact"]}`.
- Plugin installs do not inherit repo settings, so extend the optional `~/.claude/settings.json` block in `docs/getting-started.md` ("Keep your usage low") with the same deny line for editors.
- In `docs/token-hygiene.md`, the section "Trimming the fixed part (your settings, not applied)" becomes "applied in this repo". Add the measured numbers from section 5.
- Add a test in `tools/test_repo_integrity.py` that `.claude/settings.json` denies `Artifact`.

### D. Decision 2: plugins and connectors

Deliver a keep-or-disable table in the final report and a short note in the guide. Do not commit plugin or connector disables. Table in section 6. Say plainly that the user must do the clicking.

### E. Decision 8: section 2 of file 07 (separate commit)

- In `docs/research/ad-copy/07-outdoor-norway-voice-and-category.md`, section 2 runs from line 150 (heading) to line 192 (a `---` rule). It holds tables 2.1 to 2.3 and a "How adwright should use this" block at lines 186 to 190. Section 3 starts at line 194. Re-check the line numbers before cutting.
- Line 848 is a table row about `utm_source=chatgpt.com` on every ClickUp link. Check it and reword or remove if it quotes the removed section.
- Do not touch `campaigns/ski-meta-ads/03-review-of-first-cut-copy.md`. The page-audit notes in that folder stay public on purpose (owner decision, 12 October 2026). It quotes the same drafts, which the user should know.
- Git history keeps the old text. A full scrub needs a history rewrite. Do not do that without the user's say-so.

### F. Docs and tests that must follow

- `CLAUDE.md`: the token rules say "Do not print whole files". Add the finished script as the exception, and say output is text in chat, files only on `save`.
- `docs/getting-started.md`: new section "Use it in Claude chat" (upload steps, the two links in section 7, `[VERIFY]` on the menu label). Update the `/script` description (text first, `save`, pair mode). If the Quick start changes, regenerate `.claude/commands/howto.md` from the text between `## Quick start` and `## Set up (once)`. The integrity test checks they match.
- `README.md`: command descriptions and the chat package.
- Suggested: bump the plugin version from 0.2.0 to 0.3.0 in `.claude-plugin/plugin.json` and `marketplace.json` (a test checks they match), because command and agent behaviour changes. A same-version edit needs uninstall and reinstall to refresh the plugin cache.
- Extend `tools/test_repo_integrity.py` for: the settings deny rule, the text-first wording in the script command and writer agent, and (through the new test file) the chat package.

## 5. Measurements to cite

Method: `claude -p "Reply with the single word ok." --permission-mode bypassPermissions --output-format json [--settings '<json>']`, then read `usage` (input plus cache creation plus cache read). Cost depends on cache state, so compare token totals, not dollars.

| Run | Input tokens on the first turn |
|---|---|
| Baseline | 41,397 |
| With the Artifact deny rule | 29,994 (down 11,403) |
| Deny rule plus plugin disables via `--settings` | 25,923 (a further 4,071 down) |

The total drop is 15,474 tokens, about 37 percent. These are single runs, and the saving is input tokens, not dollars (cache reads cost far less). The plugin disables were projected at 5.7k and measured at 4.1k. Each test run uses the user's own account limit, and one run already hit the session limit, so keep runs few and small.

## 6. Plugin and connector table (decision 2)

Commands the user runs: `claude plugin details <id>` (inventory and projected always-on tokens), `claude plugin disable <id>`, `claude plugin enable <id>`, `claude plugin list`, and `/plugin` inside Claude Code. For connectors use `/mcp` or https://claude.ai/customize/connectors (a verified URL).

| Plugin | Recommendation |
|---|---|
| `claude-code-setup` | Keep. It costs about 141 tokens |
| `searchfit-seo` | Off |
| `data` | Off |
| `enterprise-search` | Off |
| `product-management` | Off |
| `miro` | Off |
| `marketing`, `productivity`, `cowork-plugin-management` | Optional. Off if unused |

Get per-plugin token numbers from `claude plugin details`. Do not quote numbers that were not measured.

Connected claude.ai connectors in the old session: ClickUp, Gmail, Google Calendar, Google Drive and Miro. Many plugin servers need an OAuth login that a cloud session cannot do, and two failed to connect (`data:definite` and `product-management:asana`). Plugins marked "Synced from claude.ai" in `claude plugin list` come from the account and are re-synced in cloud sessions, so whether a disable persists there is unconfirmed. [VERIFY: persistence of plugin disables in cloud sessions, and the plugin menu location]

Offer, without committing it, a repo-level `enabledPlugins` block with `false` values. Do not add `disableClaudeAiConnectors: true` to project settings, because it would switch off every claude.ai connector for everyone who uses the repo. Prefer the account-level toggles.

## 7. claude.ai skill facts

Sources: https://claude.com/docs/skills/how-to and https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

- Upload a ZIP whose top level is the skill folder. Enable it under Customize > Skills (the how-to page links https://claude.ai/customize/skills; another source said Settings > Features or Capabilities). [VERIFY: confirm current menu label for claude.ai skills]
- Custom skills belong to the individual user. Team and Enterprise plans have Share and Publish controls.
- `SKILL.md` stays under 500 lines. The folder is copied into the code-execution sandbox. Scripts need code execution to be on.

## 8. Repo rules that bite

- Facts come only from `campaigns/ski-meta-ads/tours.json`, `.claude/product-marketing.md` or a page the client names. Never invent a fact, a guide's words or a URL.
- The repo is public and MIT. No supplier terms, personal data or private client information. ClickUp content stays out of the repo. This file therefore names no ClickUp material.
- Integrity tests (`tools/test_repo_integrity.py`) fail on: an em or en dash or emoji in any tracked text file (arrows and check marks in the 2600 to 27BF range count as emoji); the local scratch folder path used by Claude sessions; any Claude model name in any file; a command without `disable-model-invocation: true`; a `!` shell line containing `${`; `ROOT/` used without the ROOT note; a bare `.claude/skills`, `campaigns/ski-meta-ads` or `tools/` path in a command other than `/howto`; `/howto` drifting from the guide's Quick start; a Quick start containing the word "below"; an agent without the "## Where files live" heading or with a `model:` line; the guide saying the repo is private.
- Commands and agents reach repo files through ROOT. Do not add `!` shell lines with `${...}` or bare repo paths to commands.
- Saved files use relative paths in the current folder, never under ROOT.
- Plugin install copies the repo into `~/.claude/plugins/cache/outdoornorway/outdoornorway-marketing/<version>/`. A folder-source marketplace needs uninstall and reinstall to pick up same-version edits. Check with `diff -rq`.
- Writing rules: no em or en dashes, no emojis, no capitals for emphasis, short sentences, no filler transitions, and no "not X but Y" repeats.

## 9. Verification and delivery

1. Run `python3 -I .claude/skills/scriptcraft/scripts/test_script_check.py`, `python3 -I tools/test_repo_integrity.py`, `python3 -I tools/test_build_chat_skill.py` and `claude plugin validate .` (one expected CLAUDE.md warning).
2. One end-to-end run in plugin mode: add the marketplace from the working tree, install, confirm the cache matches with `diff -rq`, then from an empty scratch folder run `claude -p "/outdoornorway-marketing:script <one tour> <platform> <style> and <platform> <style>" --permission-mode bypassPermissions --output-format json`. Pass only if both scripts appear in full in the reply, each shows a validator PASS line, and no files appear in the scratch folder. Record cost and time. Then uninstall and remove the marketplace.
3. Unzip the built chat package into an empty folder and run the validator on a fixture script with `--tours-file data/tours.json`.
4. Three independent reviewers, each told to refute: text-first behaviour and pair mode against the command and agent rules; the chat zip as a standalone skill; repo hygiene, public safety and the writing rules. Fix what they confirm.
5. Commit in two parts, with decision 8 as its own commit. End every commit message with the trailers that the new session's attribution reminder gives (this file must not hold a model name, so it does not repeat them). Push with `git push -u origin claude/confident-cannon-1on6av`, retrying only on network errors at 2, 4, 8 and 16 seconds.
6. Send the zip to the user with SendUserFile.

## 10. Final report to the user

Plain short sentences. Cite the two claude.ai sources as links. List what only the user can do: switch plugins and connectors in their own account, and upload the zip in claude.ai. State these assumptions:

- Decision 8 was read as "remove", the change is a separate commit, git history keeps the old text, and file 03 still quotes the same drafts.
- The Google Docs paste format is my assumption. The chat output is the validator's table format in a fenced block. A plain beat list may paste into Google Docs better. [VERIFY: ask the user which they prefer]
- The claude.ai menu label and the 200-character description limit are unverified.
- Measurements are single runs of input tokens.
- Windows `python3` is untested.
- Changes are not live until a pull request is merged.

No soft closing offer. End with a short summary.

## 11. Open items outside this work

- The aurora `ugc_talk` script still needs an independent review before filming.
- `.claude/skills/scriptcraft/assets/shoot-plan-template.md` keeps a `[VERIFY with counsel]` line about releases. Decision 6 was dropped, so leave it and mention it.
- The `adquill/` skill is paused and not installed by the plugin.
- Earlier PRs 1 to 7 are merged.

## 12. What lives outside the repo

- The old session's scratch notes (cost levers, our flow, production practice and a ClickUp pipeline note, plus the measurement runs) sit in that session's scratchpad folder and may be gone. Everything needed is in sections 3 to 7 above. Do not recreate the ClickUp note in the repo.
- The old transcript, if the container still has it: `/root/.claude/projects/-home-user-outdoornorway/698d341b-36e0-5dc5-a8cb-413a8d3083ac.jsonl`. Search it with grep and read with an offset and limit. Do not read it whole.

## 13. Starter prompt for the new session

```
Read docs/handoff-next-session.md and do the work in it on branch
claude/confident-cannon-1on6av. Packages A and B can run in parallel,
then C to F. Return paths and short status only. Show me the finished
report in chat. Do not open a pull request.
```
