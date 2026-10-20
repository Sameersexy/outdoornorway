# Account skills

This page is for writers and maintainers who want to reuse an account skill. It answers what is in this folder, how to use one and how to add one.

## What is here

| Skill | What it does |
|---|---|
| [brand-voice-checker](brand-voice-checker/SKILL.md) | Reviews guest-facing copy, such as tour scripts, captions and blog copy, against the brand voice guidelines. |
| [guest-benefit-checker](guest-benefit-checker/SKILL.md) | Reviews guest-facing copy for content angle, meaning whether it leads with the guest's benefit or with itinerary details, logistics or a sales pitch. |
| [script-writing](script-writing/SKILL.md) | Writes, drafts, improves and reviews video and short-form social scripts. |

All three were read for supplier terms, prices, contacts, personal data and client facts before they were copied here.

The plugin does not load this folder. It sits outside `.claude/`, so nothing here is a command or an agent. Skills under `.claude/skills/` load automatically, and these do not.

## How to use a skill

Pick one of two routes.

- **In one project.** Copy the skill folder into your project under `.claude/skills/`. Claude Code then finds it in that project.
- **In the Claude account.** Upload the folder as a custom skill. The upload steps are in the restore section of the [backup and restore guide](../docs/backup-and-restore.md#restore-on-the-new-account).

The account upload limits a skill name to 64 characters and a description to 200. The description in each of the three skills here is longer than 200 characters. Shorten it in the copy you zip, and leave the file in this repo as it is. The help page on [custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) names the instructions file `skill.md` in lowercase, while Claude Code reads `SKILL.md`. [VERIFY: the owner confirms which file name the account upload accepts, and whether it rejects a description over 200 characters]

## Skills that are not here

Supplier and private skills are never in this public repo. The full list of account skills, including the ones that stay private, is in the [skills catalog](../docs/skills-catalog.md).

## Adding a skill

1. Read the skill before anything else. Check it for supplier terms, prices, contacts, personal data and private client facts.
2. Create one folder per skill, named after the skill. Put a `SKILL.md` in it, with a `name` that matches the folder and a `description`. Keep the name to 64 characters and the description to 200, so the skill can also be uploaded to an account.
3. Add nothing else to the skill folder. The only other file allowed here is this README.
4. Add a row to the table above, then run the integrity test. It checks the folder names, the front matter and the files.
