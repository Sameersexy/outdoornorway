# Token hygiene: where the tokens go and what to change

This page is for anyone who runs long Claude Code sessions in this repo and wants to keep them cheap. Every model call re-reads the whole conversation from cache. Cost is therefore calls times context size.

Measured example: one long session that built this repo, measured with `tools/transcript_report.py`.

- 378 model calls, a median of 350k tokens of context per call, a peak of 774k.
- A fixed part is sent on every call: about 59k tokens (51 tool definitions at about 50k, the Artifact tool alone about 14k and not used in that session, plus about 9k of system prompt).
- The skill and connector listing was injected into the conversation 28 times, about 4.6k tokens each (128k in all), mostly when connectors such as Miro and GitHub reconnected.
- The conversation itself grew to about 1.2M tokens of text: messages and tool inputs 512k, tool results 263k. Subagent hand-backs of 10k to 11k tokens each were the largest single entries.

The usage report for that session showed 37M cached tokens. It and the transcript's total differ (different windows and counting), but the shape is the same: a big fixed part times a very long conversation.

## What the repo already does

- `script-writer` and `script-reviewer` return compact results: the RESULT line, counts and rule ids, not the full validator output and not the whole script. Full text stays in files.
- `SKILL.md` says to report the RESULT line and the warning ids, and to keep the full validator output in a file.
- `tools/transcript_report.py` measures a session, so the effect can be checked.
- `CLAUDE.md` is short on purpose: it loads in every session.

## Measured effect of the thinner commands

The `/script`, `/review-script` and agent files were cut down (the commands carry short instructions, the validator answers `--limits` and `--tour` questions so nobody reads whole rule or tour files). Same requests, plugin install, one run each, `claude -p` with JSON output:

| Run | Cost before | Cost after | Time before | Time after |
|---|---|---|---|---|
| `/script ski-snowshoe-3day reels voiceover` | USD 0.306 | USD 0.238 | 71 s | 47 s |
| `/review-script` on that script | not measured alone | USD 0.240 | not measured alone | 57 s |
| `/script ski-6day shorts voiceover` | not measured | USD 0.224 | not measured | 57 s |

In these runs the write run was about 22 percent cheaper and about 34 percent faster. One run each, so treat the percentages as a rough size, not a promise.

Both scripts from these runs passed the validator, and each came with a notes file in the right folder. The agent file says to use relative paths only and to run `ls -l` once, because a measured run of an earlier thin `/script` command let the writer agent save files under a wrong absolute path.

## Habits that cut the most

1. One deliverable per session. A fresh session starts near the fixed part (about 59k tokens in the example above), and the repo notes carry the state. This is the biggest lever, because cost is calls times context size and the example's median context was 350k tokens per call.
2. Compact at about 150k tokens instead of letting a session run to 500k and beyond.
3. Subagents and workflows return paths, scores and short lists. Reports go to files. A workflow script reads from `scriptPath`, not inline.
4. Review depth: one writer and one reviewer, at most two rounds. Extra rounds add cost and gain little. In one earlier test, four rounds on one script moved the mean score only from 5.5 to 6.3. [VERIFY: the figures 5.5 and 6.3 have no source file in this repo, the owner confirms them]
5. Never print a whole file or a full validator run in the main conversation. Use `| grep -E "FAIL|WARN|RESULT"` and `Read` with an offset and limit.

## Trimming the fixed part (your settings, not applied)

These change which tools you have, so they are left to you. Put them in `.claude/settings.json` and restart the session. The `enabledPlugins` form is the one this repo already uses in that file. The `permissions` block below is not tested here. Check the current Claude Code settings documentation to see whether a deny rule removes the tool from the tool list, before you rely on it.

```json
{
  "permissions": { "deny": ["Artifact"] },
  "enabledPlugins": {
    "<plugin>@<marketplace>": false
  }
}
```

Copy plugin ids from `/plugin`. The plugins this repo does not use are the likely candidates: SEO, data, enterprise search, productivity, product management, Miro and plugin management. Each enabled plugin adds skill descriptions to every call and may add a connector that reconnects mid-session.
