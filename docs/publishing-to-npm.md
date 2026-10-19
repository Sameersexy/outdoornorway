# Publishing to npm

This guide is for the repo owner, who publishes the launcher package to npm from their own npm account. It covers the version bump, the checks, the publish and the git tag.

## What gets published

The package is named `outdoornorway-marketing`, as set in [package.json](../package.json). It has one command, `outdoornorway`, which runs `tools/outdoornorway-cli.js`. It has no dependencies and needs Node 18 or newer. npm comes with Node.

The package holds the paths in the `files` list of `package.json`: the plugin manifests, `.claude/`, `adquill/`, `campaigns/`, `content/`, `docs/`, `tools/` and the top-level guides and licence files.

npm adds a second way in, `npx outdoornorway-marketing`. It does not replace the plugin route: Claude Code still installs the plugin from GitHub, as [installation.md](installation.md) shows.

Publishing needs your npm account. Nothing in this repo runs `npm login`, `npm publish` or a tag push, and the repo has no publishing workflow.

Merge the change to the default branch first and work from that clean copy. `npm publish` uploads the files in your folder and does not read a commit, so uncommitted edits would ship.

## 1. Bump the version

Skip this step for the first publish, which uses the version already in the manifests.

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

Do not rely on `npm version`. It edits only `package.json`, since this repo has no package-lock.json, and it leaves the two plugin manifests alone. Inside a git repository it also makes a commit and a tag by default.

Add the change to [CHANGELOG.md](../CHANGELOG.md) in the same commit.

## 2. Check the name is free

```bash
npm view outdoornorway-marketing
```

A free name returns an `E404` error. A printed version number means someone else owns the name.

## 3. Check the package contents

```bash
npm pack --dry-run --json 2>/dev/null | grep -E '"path": ".*(backup/|exports/|node_modules/|\.jsonl|\.zip|\.tgz|\.env|__pycache__)'
```

The command prints nothing when the list is clean. It looks for the paths that `.gitignore` keeps out of the repo: backups, exports, transcripts, archives, secrets and dependency folders. `--dry-run` writes no tarball.

Read the file names once too, for anything that should not be public, such as client names. `npm pack --dry-run` prints them.

The package includes `adquill/`, which is paused and not installed by the plugin. Remove it from the `files` list if you do not want it on npm.

## 4. Run the checks

```bash
git status --short
node tools/outdoornorway-cli.js doctor
npm test
```

- `git status --short` prints nothing when the copy is clean.
- `doctor` prints `versions match (<version>)` when `package.json` and the two plugin manifests agree. It exits with 1 only when a check fails. A warning about Node or the Claude Code CLI does not stop it.
- `npm test` runs `node tools/outdoornorway-cli.js test`, which covers the validator tests and the repo integrity tests. Add `--all` to include the adquill tests.

The tests need `python3` on your PATH. [installation.md](installation.md#prerequisites) lists the Python versions.

## 5. Log in

```bash
npm whoami
```

It prints your npm user name when you are logged in. If it fails, run `npm login`. Keep any `.npmrc` that holds a token out of the repo folder, because `.gitignore` does not list it.

## 6. Publish

```bash
npm publish
npm view outdoornorway-marketing version
```

The second command should print the version you just published.

- `npm publish` does not run the tests, and `package.json` has no lifecycle script that does, so run step 4 first.
- A version can be published only once. If the upload has a problem, bump the version (step 1) and publish again.
- After a publish, `npx outdoornorway-marketing doctor` checks the copy that npm installed. npm 10.9.4 runs the package's single `outdoornorway` bin under the package name, as a test against a local stand-in for the npm registry showed (`npx --yes outdoornorway-marketing version` printed `0.2.0`). [VERIFY: run `npx outdoornorway-marketing doctor` from an empty folder after the first publish, because the name is not on npmjs.com before then]

## 7. Tag the release

Tag after the publish succeeds, on the commit you published from:

```bash
git tag -a v<new-version> -m "Release v<new-version>"
git push origin v<new-version>
```

Use the version from `package.json`. The second command pushes only that one tag.

## Optional: a scoped name

Use a scoped name such as `@<npm-scope>/outdoornorway-marketing` only if the unscoped name is taken before you publish.

- Change `name` in `package.json`. `tools/test_repo_integrity.py` requires the package name to equal the plugin name, `outdoornorway-marketing`, so change the test in the same commit or keep the unscoped name.
- You need an npm scope that you own.
- Publish with `npm publish --access public`, because scoped packages are private by default. The npm 10.9.4 docs confirm that scoped packages default to restricted access and that the flag is needed only on the first publish.
