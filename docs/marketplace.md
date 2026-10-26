# Plugin marketplace

This page is for marketers who choose and install the Outdoor Norway plugins, and for maintainers who add a skill or cut a release. The marketplace is named `outdoornorway`. It lives in `.claude-plugin/marketplace.json` and lists four plugins.

## The four plugins

| Plugin | Who it is for | What it holds |
|---|---|---|
| `outdoornorway-marketing` | Writers and editors who make video scripts. Most people want this one. | The umbrella plugin: the slash commands, the two agents, scriptcraft with its validator, and the eight copy skills. |
| `outdoornorway-copy-skills` | People who want only the copy skills, with none of the video script tools. | Nine skills: ad-creative, conversion-copywriter, copy-that-sells, copywriting, fact-check, humanizer, marketing-psychology, ponytail and social. |
| `outdoornorway-account-skills` | Anyone who wants the brand and script skills in Claude Code. | Three skills: brand-voice-checker, guest-benefit-checker and script-writing. |
| `repo-band` | Anyone who works in the terminal or the desktop app and wants a status row above the prompt. | A mod, not a skill: cost, context fill, last turn, branch, changed files and the last validator result, with Compact and Hide buttons. See [its README](../mods/repo-band/README.md). |

Every plugin id has the form `NAME@outdoornorway`. The skills in the second and third plugin carry the plugin name, for example `outdoornorway-copy-skills:copywriting` and `outdoornorway-account-skills:brand-voice-checker`.

If you write scripts, install the first plugin. Add the third for the brand checkers. Install the second only if you do not install the first.

scriptcraft, the agents and the commands stay in the umbrella plugin and cannot be split out. The validator finds `tours.json` from the plugin root, and the commands and agents reach their files through the plugin root.

## Install

Pick one route and replace NAME with a plugin name from the table above. Restart Claude Code afterwards.

| Route | Line | Needs |
|---|---|---|
| In Claude Code, one step | `/plugin install NAME --marketplace Sameersexy/outdoornorway` | Claude Code 2.1.275 or later |
| In Claude Code, menu | Type `/plugin` and follow the prompts. The manager has Discover, Installed and Marketplaces tabs. | Any version with plugins |
| Terminal, one step | `claude plugin install NAME --marketplace Sameersexy/outdoornorway` | Claude Code 2.1.292 or later |
| Terminal, two steps | `claude plugin marketplace add Sameersexy/outdoornorway`, then `claude plugin install NAME@outdoornorway` | Any version with plugins |
| npx | `npx github:Sameersexy/outdoornorway install NAME --run` | Node.js 18 or newer, and the launcher on the default branch |

The one-step lines take the bare name. The two-step line needs the `@outdoornorway` ending. The two-step route was tested with real installs on Claude Code 2.1.304. [VERIFY: the one-step lines were not run against this repo, and their syntax comes from the Claude Code docs]

The npx launcher is not on npm yet, so it works only from GitHub, as [installation.md](installation.md#route-3-npx-launcher-optional) explains. These commands cover the three cases:

```
npx github:Sameersexy/outdoornorway list
npx github:Sameersexy/outdoornorway install outdoornorway-account-skills
npx github:Sameersexy/outdoornorway install all --run
```

`list` prints each plugin with its version, description and install line. `install` without `--run` prints the steps and runs nothing. `install all` covers every plugin except `outdoornorway-copy-skills`, which it leaves out and says so, because the umbrella already carries those skills. `install` alone means `outdoornorway-marketing`. An unknown name stops with the list of valid names. With `--run`, a marketplace that is already added counts as success. Set `OUTDOORNORWAY_MARKETPLACE` to use a fork or a local folder as the marketplace source instead of `Sameersexy/outdoornorway`.

## Installed alone or together

- **The umbrella alone.** You get the commands, the agents, scriptcraft and the eight copy skills. This is the full toolset for writers.
- **Copy skills alone.** You get the eight skills and nothing else. Without the umbrella, the skills register as `outdoornorway-copy-skills:<skill>`.
- **Copy skills next to the umbrella.** Each of the eight skills is listed twice, once as `outdoornorway-marketing:<skill>` and once as `outdoornorway-copy-skills:<skill>`, because both plugins carry them. Nothing breaks, but the list gets longer and each skill uses description space twice. Install the umbrella alone, or the copy skills alone. A local folder marketplace hides the second copy, so the doubling shows only on a GitHub install.
- **Account skills next to the umbrella.** The two do not overlap. The umbrella does not load `account-skills/`, so this install adds three skills.

## The fact-check caveat

The fact-check skill names `campaigns/ski-meta-ads/tours.json` and `verify_tours.py` as its source of truth for tour prices and dates. Those files exist only in the umbrella plugin and in a clone. With `outdoornorway-copy-skills` alone, fact-check cannot read them, so name another source of truth when you run it, or install the umbrella. The other copy skills only optionally read `.claude/product-marketing.md`.

## Update and uninstall

Updating takes two steps, because refreshing the marketplace does not update the plugins.

```
claude plugin marketplace update outdoornorway
claude plugin update NAME@outdoornorway
```

There is no update-all command, so run the second line once per plugin. The launcher does the same with `npx github:Sameersexy/outdoornorway update all --run`. Claude Code offers a new version only when the plugin's version string changes, so a change that is merged without a version bump does not reach anyone.

Auto-update is off by default for a third-party marketplace. Switch it on with `autoUpdate` in the team settings below, or with the toggle in `/plugin`.

To remove one plugin, or the whole marketplace:

```
claude plugin uninstall NAME@outdoornorway
claude plugin marketplace remove outdoornorway
```

`marketplace remove` also uninstalls every plugin from that marketplace. `claude plugin marketplace list` shows the marketplaces you have added, and `claude plugin list` shows the installed plugins.

## Prompt a team through project settings

A team can have Claude Code offer the marketplace to every member who opens the team's repo. Put this in `.claude/settings.json` in that repo:

```json
{
  "extraKnownMarketplaces": {
    "outdoornorway": {
      "source": { "source": "github", "repo": "Sameersexy/outdoornorway" },
      "autoUpdate": true
    }
  },
  "enabledPlugins": {
    "outdoornorway-marketing@outdoornorway": true
  }
}
```

- The key under `extraKnownMarketplaces` must equal the marketplace `name`, which is `outdoornorway`. Each key under `enabledPlugins` is `NAME@outdoornorway`, so add a line per plugin you want on.
- Members get the offer after they accept the workspace trust dialog for the folder. In a folder they have not trusted, Claude Code ignores the entries without a message.
- All four plugins use relative paths, so they load from the marketplace copy and members need no separate install step.
- `autoUpdate: true` makes Claude Code refresh the marketplace and update its installed plugins in the background after startup.
- Project settings beat user settings. A plugin someone set to false in `~/.claude/settings.json` still loads if the project enables it.

This page makes no promise about cloud sessions. [VERIFY: whether cloud sessions load plugins that a repo's `.claude/settings.json` enables]

## Add a skill

1. Read the skill first. The repo is public, so check it for supplier terms, prices, contacts, personal data and private client facts.
2. Create the folder and give it a `SKILL.md` with a `name` that equals the folder name and a `description`. An account skill goes in `account-skills/<name>/` and holds only `SKILL.md`. A vendored copy goes in `.claude/skills/<name>/` and needs a row in [THIRD_PARTY_SKILLS.md](../THIRD_PARTY_SKILLS.md).
3. Add `./<name>` to the `skills` list of the matching entry in `.claude-plugin/marketplace.json`: `outdoornorway-account-skills` for a folder in `account-skills/`, `outdoornorway-copy-skills` for a folder in `.claude/skills/`. Each skill sits in exactly one of those two lists. scriptcraft sits in neither, because the umbrella carries it. The umbrella loads every folder in `.claude/skills/` without a list, because `plugin.json` names that folder.
4. Leave the umbrella entry without component lists. An entry with `source "./"`, `strict: false` and a component list fails to load with "Plugin <name> has conflicting manifests: both plugin.json and marketplace entry specify components", and `claude plugin validate` still passes. The integrity test checks for it.
5. Run the checks:

   ```
   python3 -I tools/test_repo_integrity.py
   node tools/outdoornorway-cli.js doctor
   claude plugin validate .
   ```

6. Add the skill to the table in [account-skills/README.md](../account-skills/README.md) or [skills-catalog.md](skills-catalog.md). Do not bump versions yet. A release does that.

## Cut a release

A release changes five version fields in three files. Set them all to the same value in one commit.

| File | Field |
|---|---|
| `package.json` | `version` |
| `.claude-plugin/plugin.json` | `version` |
| `.claude-plugin/marketplace.json` | `version` of each of the four entries |

For the umbrella, the manifest value wins over the entry value, and `claude plugin validate` warns if they differ. The two subfolder entries have no manifest, so their entry version is the only one.

1. Bump the five fields, then check them. The command prints five lines with one value:

   ```
   grep -n '"version"' package.json .claude-plugin/plugin.json .claude-plugin/marketplace.json
   ```

2. Add the change to [CHANGELOG.md](../CHANGELOG.md) in the same commit.
3. Run the integrity test, `doctor` and `claude plugin validate .` as in the previous section.
4. Merge to the default branch. People then get the release with the update lines above, or in the background if `autoUpdate` is on.
5. Publishing to npm and the git tag follow [publishing-to-npm.md](publishing-to-npm.md).

## What only the owner can do

These steps need the owner's own accounts.

- **Publish to npm.** It needs the owner's npm login. See [publishing-to-npm.md](publishing-to-npm.md).
- **Submit to the Anthropic directory.** This is optional. A marketplace on GitHub needs no submission, and Anthropic does not review third-party marketplaces. The submission portal is at https://claude.ai/directory/manage: choose Submit new, then Plugin bundle. It needs a Pro, Max, Team or Enterprise plan, and a connected GitHub account with push access to the repo. Skills alone are not a submission type. The checks are in the [pre-submission checklist](https://claude.com/docs/plugins/pre-submission-checklist). They allow one plugin per submission, one submission per repo folder, and a `.claude-plugin/plugin.json` in the plugin folder. The umbrella has one at the repo root. The two subfolder plugins have none. [VERIFY: whether the portal accepts a marketplace entry with `strict: false` and no `plugin.json` in its folder]
- **Upload a skill to claude.ai.** Open Customize, then Skills, then +, then + Create skill, then Upload a skill. Code execution and file creation must be on. The zip needs the skill folder as its root, so `<skill>/SKILL.md`. Build the zips with `node tools/outdoornorway-cli.js skills pack --out DIR`. It prints each zip's size and description length, and flags any description over 200 characters. The two official pages disagree on the limit, 200 or 1,024 characters. [VERIFY: the owner confirms the limit with a test upload] The rest of the upload steps are in [backup-and-restore.md](backup-and-restore.md#restore-on-the-new-account) and [account-skills/README.md](../account-skills/README.md).
