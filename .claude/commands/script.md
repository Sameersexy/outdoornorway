---
description: Write an Outdoor Norway video script with the scriptcraft rules (Reels, Shorts, TikTok, YouTube)
argument-hint: <tour id or topic> <platform> [voiceover|ugc_talk|ugc_text]
disable-model-invocation: true
---
Write a video script for: $ARGUMENTS

Use the script-writer agent (subagent_type script-writer) and follow `.claude/skills/scriptcraft/SKILL.md`.

1. Work out the brief from the request. Platform reels, shorts or tiktok is tier short (up to 25 s). Youtube is tier long (up to 3:20). Style defaults to voiceover; use ugc_talk or ugc_text only when named. Take the tour from `campaigns/ski-meta-ads/tours.json`. Facts come only from tours.json, `.claude/product-marketing.md` and a page the user names (save its text to a file first and give the agent the path).
2. Ask the user only for what is missing and cannot be defaulted: the tour or topic, the platform, who films (guide, staff or guest) for a ugc style. Do not ask about anything with a default.
3. Give the agent the brief, the sources, and these output rules: save the script to `content/scripts/<yyyy-mm-dd>-<slug>.md`, run the validator in draft and --final mode, and reply compactly with the path, the RESULT lines, open items grouped by who confirms, and one alternative hook and call to action. No pasted script, no full validator output.
4. If the brief has no real moment from a real guide, say so and point to `.claude/skills/scriptcraft/assets/guide-moment-intake.md`.
5. Relay the agent's result in at most 30 lines. Offer `/review-script` as the next step in one short line.
