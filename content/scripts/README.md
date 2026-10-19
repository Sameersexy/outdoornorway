# Video scripts

This folder holds the Outdoor Norway video scripts and the notes that go with them. Read this page before you add, check or record one.

## File names

Each script is saved with a date and a slug. Write the date as yyyy-mm-dd and the slug as lowercase words joined by hyphens. The two scripts here carry 2026-10-12, the day they were first committed.

- `<yyyy-mm-dd>-<slug>.md` is the script.
- `<yyyy-mm-dd>-<slug>-notes.md` is the notes file. It holds the brief, the caption text, open items, assumptions, accepted warnings and one variant line with an alternative hook and an alternative call to action.
- `<yyyy-mm-dd>-<slug>-brief.md` is the one-page creator brief. The writer agent makes it when you ask for one, and for any ugc script that a guide or guest will film.

The slug names the tour, the trip length and the platform. A second style of the same script adds the style to the end of the slug.

## Scripts in this folder

| Script | Form | Notes file |
|---|---|---|
| [2026-10-12-northern-lights-7day-youtube.md](2026-10-12-northern-lights-7day-youtube.md) | Long, voiceover, YouTube | [notes](2026-10-12-northern-lights-7day-youtube-notes.md) |
| [2026-10-12-northern-lights-7day-youtube-ugc-talk.md](2026-10-12-northern-lights-7day-youtube-ugc-talk.md) | Long, ugc_talk, YouTube, creator is a guide | [notes](2026-10-12-northern-lights-7day-youtube-ugc-talk-notes.md) |

Both are drafts. Each notes file says what is still open and who confirms it, and `/open-items <file>` prints the live list. The ugc-talk script has no creator brief yet.

## Add a script

Run `/script` with a tour id or topic, a platform and a style:

```
/script <tour id or topic> <platform> [voiceover|ugc_talk|ugc_text]
```

The command passes the request to the script-writer agent. The agent saves the script and its notes file under `content/scripts/` in the folder you run Claude Code from. It replies with the file paths, the beat count, the validator result and the open items, and it does not paste the script. Run Claude Code from a clone of this repo so the files land next to the ones already here. The agent never saves under the plugin's own folder.

If the request names a web page, the command first saves that page's text as `content/sources/<slug>.txt` and gives the agent that path as a source.

Two commands help with the next step:

- `/open-items <file>` lists every placeholder and unverified fact, grouped by who confirms it.
- `/review-script <file>` runs the script-reviewer agent for an independent review of facts, voice and verdict.

## Validate a script

Run `/validate <file>` to see the findings in brief form. Flags go after the path.

```
/validate content/scripts/<file>.md
/validate content/scripts/<file>.md --final --strict
```

Outside Claude Code, run the same check from the repo root:

```
python3 -I .claude/skills/scriptcraft/scripts/script_check.py content/scripts/<file>.md --brief
```

The flags:

- No flag (draft run): placeholders are allowed. Warnings show but do not fail the run.
- `--final`: placeholders and unverified fact rows fail. Run this before a script is recorded or published.
- `--strict`: warnings fail as well.
- `--explain RULE_ID`: says what a rule counts.
- `--open-items`: lists the placeholders and unverified rows.

A warning can stay when the notes file says in one sentence why it is acceptable.

The validator checks limits, structure, placeholders and banned wording. It does not judge rhythm or voice. Read the voiceover aloud, and run `/review-script` for the "Sounds human" check, before you call a script done.

## Public repo rules

Every script and notes file is published with the repo. Keep them free of personal data, supplier terms and private client information, as [CONTRIBUTING.md](../../CONTRIBUTING.md#licence-and-private-information) says. Facts come from `campaigns/ski-meta-ads/tours.json`, `.claude/product-marketing.md` or a page the client names. A fact that cannot be traced to one of these gets a `[VERIFY: what to confirm]` placeholder in its place.

## Related

- [Script writer agent](../../.claude/agents/script-writer.md): the naming, saving and reply rules.
- [Script reviewer agent](../../.claude/agents/script-reviewer.md)
- [How the validator counts](../../.claude/skills/scriptcraft/references/tiers.md)
- [Review rounds of the script skill](../../docs/script-skill-reviews/README.md)
