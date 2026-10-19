# Video scripts

This folder holds the Outdoor Norway video scripts. Read this page before you add, check or record one.

## File names

Each script is saved with a date and a slug. Write the date as yyyy-mm-dd and the slug as lowercase words joined by hyphens. [VERIFY: confirm whether the date is the day the script is written or a planned shoot date.]

- `<yyyy-mm-dd>-<slug>.md` is the script.
- `<yyyy-mm-dd>-<slug>-notes.md` is the notes file. It holds the brief, the caption text, open items, assumptions, accepted warnings and one variant line with an alternative hook and an alternative call to action.
- `<yyyy-mm-dd>-<slug>-brief.md` is the one-page creator brief. It is written only when someone asks for one, or for any ugc script that a guide or guest will film.

The examples put the tour, the trip length and the platform in the slug. A second style of the same script adds the style to the end of the slug, as in the ugc-talk pair listed below.

## How files get here

Run `/script` with a tour id or topic, a platform and a style:

```
/script <tour id or topic> <platform> [voiceover|ugc_talk|ugc_text]
```

The command passes the request to the script-writer agent. The agent saves the script and its notes file under `content/scripts/` in the folder you run Claude Code from. It replies with the file paths, the beat count, the validator result and the open items, and it does not paste the script.

Run Claude Code from a clone of this repo so the files land next to the ones already here. Files never go into the plugin's own folder.

If the request names a web page, the command first saves that page's text as `content/sources/<slug>.txt`. This repo does not have that folder yet.

Once a script exists, two commands help with the next step:

- `/open-items <file>` lists every placeholder and unverified fact, grouped by who confirms it.
- `/review-script <file>` runs the script-reviewer agent for an independent review of facts, voice and verdict.

## How to validate

Run `/validate <file>` to see the validator's findings in brief form. Flags go after the path.

```
/validate content/scripts/<file>.md
/validate content/scripts/<file>.md --final --strict
```

Outside Claude Code, run the same check from the repo root, with the path relative to that folder:

```
python3 -I .claude/skills/scriptcraft/scripts/script_check.py content/scripts/<file>.md --brief
```

The flags work like this:

- No flag (draft run): placeholders are allowed. Warnings show but do not fail the run.
- `--final`: placeholders and unverified fact rows fail. Run this before a script is recorded or published.
- `--strict`: warnings fail as well.
- `--explain RULE_ID` says what a rule counts.
- `--open-items` lists the placeholders and unverified rows.

A warning can stay when the notes file says in one sentence why it is acceptable.

The validator checks the rules it has. It does not check AI tells or voice, so read the voiceover aloud before a script is called done.

## Scripts in this folder

| Script | Form | Status, as the notes file states it | Notes file |
|---|---|---|---|
| `2026-10-12-northern-lights-7day-youtube.md` | Long, voiceover, YouTube | Passes strict mode with no failures or warnings. `--final` fails on placeholders. The notes say the script is not ready to record or publish. | `2026-10-12-northern-lights-7day-youtube-notes.md` |
| `2026-10-12-northern-lights-7day-youtube-ugc-talk.md` | Long, ugc_talk, YouTube, creator is a guide | Passes draft mode with two warnings, both kept on purpose. `--final` fails on placeholders and on two unverified rows. The hand-edited version has not been scored again by the reviewer. No guide is named yet. | `2026-10-12-northern-lights-7day-youtube-ugc-talk-notes.md` |

The status is what each notes file recorded on its date, as shown in the file names. It is not a live result. [VERIFY: rerun `/validate` on both scripts before relying on this status.]

No creator brief is in this folder. The ugc-talk script has a guide as its creator, and the script-writer rules ask for a brief in that case. [VERIFY: whether a creator brief for the ugc-talk script is still to be written, and who writes it.]

Each notes file lists its open items grouped by who confirms them. Run `/open-items <file>` on a script for the live list.

## Public repo rules

This repo is public and MIT licensed, so every script and notes file is published with it. Keep them free of:

- Personal data about guests, guides, staff or anyone else.
- Supplier terms, such as rates, contract clauses or private agreements.
- Private client information.

Facts come from `campaigns/ski-meta-ads/tours.json`, `.claude/product-marketing.md` or a page the client names. A fact that cannot be traced to one of these is written as `[VERIFY: what to confirm]`, not as a claim.

The repo rules in [CLAUDE.md](../../CLAUDE.md) also apply here: no em or en dashes, no emojis and no model names in any file.

## Related

- [Script writer agent](../../.claude/agents/script-writer.md): the naming, saving and reply rules.
- [Script reviewer agent](../../.claude/agents/script-reviewer.md).
- [How the validator counts](../../.claude/skills/scriptcraft/references/tiers.md), in the references folder of the skill.
- [Review rounds of the script skill](../../docs/script-skill-reviews/README.md).
