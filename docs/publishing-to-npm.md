# Publishing to npm

This guide is for the repo owner, who publishes the launcher package to npm from their own npm account. It covers the version bump, the checks, the publish and the git tag.

## What gets published

The npm package is named `outdoornorway-marketing`, as set in [package.json](../package.json). It has one command, `outdoornorway`, which runs `tools/outdoornorway-cli.js`. It has no dependencies and needs Node 18 or newer. npm comes with Node.

The package contains the paths in its `files` list: the plugin manifests, `.claude/`, `adquill/`, `campaigns/`, `content/`, `docs/`, `tools/` and the top-level guides.

npm does not replace the plugin route. Claude Code still installs the plugin from GitHub with `claude plugin marketplace add Sameersexy/outdoornorway`. The npm package adds a second way in, `npx outdoornorway-marketing`.

Publishing needs your npm account. Nothing in this repo runs `npm login`, `npm publish` or a tag push, and the repo has no publishing workflow.

Before any publish, merge the change to the default branch and work from that clean copy. `npm publish` uploads the files in your folder. It does not read a commit, so uncommitted edits would ship.

## 1. Bump the version

Skip this step for the first publish. That publish uses the version already in the manifests, which is 0.2.0 at the time of writing.

The version appears in three files. Change all three in the same commit, to the same value.

| File | Field |
|---|---|
| `package.json` | `version` |
| `.claude-plugin/plugin.json` | `version` |
| `.claude-plugin/marketplace.json` | `version` of the entry in `plugins` |

Check the result:

```bash
grep -n '"version"' package.json .claude-plugin/plugin.json .claude-plugin/marketplace.json
```

Each line should show the same version.

Do not rely on `npm version` alone. It changes `package.json` and leaves the two plugin manifests alone. By default it also makes a git commit and a tag. [VERIFY: npm version behaviour on your npm version, and that it updates only package.json because this repo has no package-lock.json]

Add the change to [CHANGELOG.md](../CHANGELOG.md) in the same commit.

## 2. Check the name is free

```bash
npm view outdoornorway-marketing
```

On 15 October 2026 this returned a 404 error, so the name was free. A printed version number means someone else owns the name. [VERIFY: a free name returns E404 on your npm version, and the name is still free on the day you publish]

## 3. Check the package contents

```bash
npm pack --dry-run 2>&1 | grep -E "backup/|exports/|node_modules/|\.jsonl|\.zip|\.tgz|\.env|__pycache__"
```

The grep prints nothing when the list is clean. It looks for the paths that `.gitignore` keeps out of the repo: backups, exports, transcripts, archives, secrets and dependency folders.

Read the full output once too. The last lines give the file count and sizes. Check the file names for anything that should not be public, such as client names. [VERIFY: npm pack --dry-run writes no tarball on your npm version]

The package includes `adquill/`, which is paused and not installed by the plugin. Remove it from the `files` list in `package.json` if you do not want it on npm.

## 4. Run the checks

```bash
git status --short
node tools/outdoornorway-cli.js doctor
npm test
```

- `git status --short` prints nothing when the copy is clean.
- `doctor` prints `versions match (<version>)` when `package.json`, the plugin manifest and the marketplace manifest agree. It exits with 1 only when a check fails. A warning about Node or the Claude Code CLI does not stop it.
- `npm test` runs the same command as `node tools/outdoornorway-cli.js test`: the validator tests and the repo integrity tests. Add `--all` to include the adquill tests: `node tools/outdoornorway-cli.js test --all`.

The tests need `python3` on your PATH. The main suites passed on Python 3.11, 3.12 and 3.13. [VERIFY: lowest Python 3 version; adquill's own docs state 3.9 or newer]

## 5. Log in

```bash
npm whoami
npm login
```

`npm whoami` prints your npm user name when you are logged in. If it fails, run `npm login`. It asks for your user name, password and email, and for a one-time code when two-factor authentication is on. [VERIFY: npm login prompts on your npm version]

Keep the login out of the repo. The `.gitignore` does not list `.npmrc`, so a token file inside the repo folder could be committed. [VERIFY: where npm keeps the login on your system]

## 6. Publish

For the current unscoped name:

```bash
npm publish
```

For a scoped name, see the section at the end. It needs the public access flag:

```bash
npm publish --access public
```

Then check the result:

```bash
npm view outdoornorway-marketing version
```

It should print the version you just published. [VERIFY: the new version appears in npm view right after publish]

Notes:

- `npm publish` does not run the tests. `package.json` has no lifecycle script that runs them, so run step 4 first.
- A version can be published only once. If the upload has a problem, bump the version (step 1) and publish again. [VERIFY: whether npm unpublish can remove a version on your account, and its time limit]
- After a publish, `npx outdoornorway-marketing doctor` checks the copy that npm installed. [VERIFY: npx runs the package's single bin when the bin name differs from the package name]

## 7. Tag the release

Tag after the publish succeeds, so the tag names a version that exists on npm. Tag the commit you published from.

```bash
git tag -a v<new-version> -m "Release v<new-version>"
git push origin v<new-version>
```

Use the version from `package.json` with a `v` prefix. This is a convention for this repo. npm and git do not require it. `git tag --list` shows the tags that exist. The second command pushes only that one tag.

## Optional: a scoped name

Use a scoped name such as `@<npm-scope>/outdoornorway-marketing` only if the unscoped name is taken before you publish.

- Change `name` in `package.json`. The integrity test in `tools/test_repo_integrity.py` requires the package name to equal the plugin name, `outdoornorway-marketing`. It fails until you change the test as well. Change both in one commit, or keep the unscoped name.
- You need an npm user or organization scope that you own. [VERIFY: the scope is free and your npm account is a member of it]
- Publish with `npm publish --access public`. Scoped packages are private by default. [VERIFY: scoped packages default to restricted access on npm]
- Update the README line that names the npm package, so it shows the new name.
