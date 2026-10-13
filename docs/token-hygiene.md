# Token hygiene: why the session read 37M cached tokens, and what to change

Every model call re-reads the whole conversation from cache. Cost is therefore calls times context size. In the long session that built this repo (measured with `tools/transcript_report.py`):

- 378 model calls, a median of 350k tokens of context per call, a peak of 774k.
- A fixed part is sent on every call: about 59k tokens (51 tool definitions at about 50k, the Artifact tool alone about 14k and never used here, plus about 9k of system prompt).
- The skill and connector listing was injected into the conversation 28 times, about 4.6k tokens each (128k in all), mostly when connectors such as Miro and GitHub reconnected.
- The conversation itself grew to about 1.2M tokens of text: my own messages and tool inputs 512k, tool results 263k. Subagent hand-backs of 10k to 11k tokens each (the validator output printed twice) were the largest single entries.

The usage report's 37M and the transcript's total differ (different windows and counting), but the shape is the same: a big fixed part times a very long conversation.

## What changed in the repo

- `script-writer` and `script-reviewer` now return compact results: the RESULT line, counts and rule ids, not the full validator output and not the whole script. Full text stays in files.
- `SKILL.md` no longer asks for the validator output to be pasted verbatim.
- `tools/transcript_report.py` measures a session, so the effect can be checked.
- `CLAUDE.md` is short on purpose: it loads in every session.

## Measured effect of the thinner commands

The `/script`, `/review-script` and agent files were cut down (the commands carry short instructions, the validator answers `--limits` and `--tour` questions so nobody reads whole rule or tour files). Same requests, plugin install, one run each, `claude -p` with JSON output:

| Run | Cost before | Cost after | Time before | Time after |
|---|---|---|---|---|
| `/script ski-snowshoe-3day reels voiceover` | USD 0.306 | USD 0.238 | 71 s | 47 s |
| `/review-script` on that script | not measured alone | USD 0.240 | not measured alone | 57 s |
| `/script ski-6day shorts voiceover` | not measured | USD 0.224 | not measured | 57 s |

The write run is about 22 percent cheaper and about 34 percent faster. One run each, so treat the percentages as a rough size, not a promise. The turn counts are not comparable: the earlier figure counted every model call including the writer agent, the new figure counts only the main conversation.

Both new scripts passed the validator and each came with a notes file in the right folder. A first version of the thin `/script` command let the writer agent save files under a wrong absolute path. The agent file now says to use relative paths only and to run `ls -l` once, and the second round saved correctly.

## Habits that cut the most

1. One deliverable per session. A fresh session starts at about 70k and the repo notes carry the state. This is the biggest lever: average context per call can fall from about 350k to about 100k to 150k, which is a 2x to 3x cut in cache reads.
2. Compact at about 150k tokens instead of letting a session run to 500k and beyond.
3. Subagents and workflows return paths, scores and short lists. Reports go to files. A workflow script reads from `scriptPath`, not inline.
4. Review depth: one writer and one reviewer, at most two rounds. Run the two skeptic audits once, before publishing, at medium effort. Four rounds on one script moved the mean score only from 5.5 to 6.3.
5. Never print a whole file or a full validator run in the main conversation. Use `| grep -E "FAIL|WARN|RESULT"` and `Read` with an offset and limit.

## Trimming the fixed part (your settings, not applied)

These change which tools you have, so they are left to you. Put them in `.claude/settings.json` and restart the session. [VERIFY: confirm current feature set for Claude Code deny rules removing a tool from the tool list, and for per-project plugin switches]

```json
{
  "permissions": { "deny": ["Artifact"] },
  "enabledPlugins": {
    "<plugin>@<marketplace>": false
  }
}
```

Copy plugin ids from `/plugin`. The plugins this repo does not use are the likely candidates: SEO, data, enterprise search, productivity, product management, Miro and plugin management. Each enabled plugin adds skill descriptions to every call and may add a connector that reconnects mid-session.
