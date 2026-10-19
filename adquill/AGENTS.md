# adquill: instructions for any coding agent

adquill writes honest, human-sounding ads for Meta (Facebook and Instagram) and X. The skill is a folder of plain files. Any agent that can read files and run Python can use it. No network, no hooks, no installer.

## Load it

1. Read skills/adquill/SKILL.md in full. It is the entry point and it is under 500 lines.
2. Read a file in skills/adquill/references/ only when the "read when" table in SKILL.md says so. Do not load them all.
3. Use the templates in skills/adquill/assets/ for the brief, the fact ledger and the output.
4. Run the linter with: python3 -I skills/adquill/scripts/slop_lint.py --text "your copy"

Where your tool looks for instructions:

- Codex, Cursor and other tools that read AGENTS.md: this file is picked up from the repo root. Follow step 1 above.
- Claude Code: adquill is paused and the plugin does not install it. This folder has no plugin manifest. To ship it, move the skill into `.claude/skills/` and the agents into `.claude/agents/`, as README.md ("If work resumes") describes.
- Gemini CLI and tools that read a different context file: add a short file in your tool's format that tells the agent to read this file, or paste the "Method in short" section below as the instruction. Check your tool's current docs for the file name it expects.
- Any chat tool with no file access: paste skills/adquill/SKILL.md, then paste the reference files you need.

## Commands

write, rewrite, lint, variants, explain, panel. People mostly ask in plain language ("write a Meta ad for ..."). Infer the command and say which one you picked.

## Method in short

1. Intake the brief (assets/brief-template.md). Required: offer, price and its basis, dates, audience segment, platform and placement, verified proof.
2. Build the fact ledger (assets/fact-ledger-template.md). The copy may only use ledger facts. Unknown facts become [VERIFY: reason]. Ask the user, never invent.
3. Diagnose: awareness level, sophistication stage, job to be done, main anxiety. Defaults: problem-aware, stage 3.
4. Pick two to four conceptually different angles. Each names one mechanism (references/psychology.md) and one risk.
5. Write to slots with character budgets. Meta static: three image lines (25, 30, 20), primary text (125 visible), headline (27), description (30), CTA label, reels line (40). X: post (280).
6. Self-edit with references/rewrite-protocol.md, then run the linter. Fix block-tier and warn-tier hits. Two rounds at most.
7. Policy and fact pass (references/policy.md). Every number must match a ledger row.
8. Output with receipts (assets/output-meta-static.md or assets/output-x-post.md). Each variant ends with Angle, Mechanism, Risk, Test hypothesis. Add one group chat line.

## Hard rules

- Never invent a testimonial, review, rating, statistic, award, seat count or deadline. If proof is missing, say so and write without it.
- One idea per ad. Variants are different ideas, not rewordings.
- Count characters in code. Show the count beside each slot.
- No em dash (U+2014) or en dash (U+2013), no emoji, no capitals for emphasis, no filler transitions.
- Platform numbers carry a source and the date 2026-10-06, or the tag [VERIFY: reason]. Re-check anything older than 90 days.
- Never let an image tool render ad text. Give the designer a spec.
- Do not claim the copy beats AI detectors, will go viral or will convert. State a test hypothesis instead.
- Scripts are Python 3.9+ standard library only, run with python3 -I, and write no files unless the user passes a path.

## Panel

The three reviewer personas are in agents/. If your tool can run subagents, run them in parallel on the same packet and merge with skills/adquill/assets/panel-prompt.md. If it cannot, run the three passes one after another and say the review was sequential.

## Examples

All examples use one fictional brand, Brekke Ski Guides. Every example is a fictional brief. See examples/ for finished pairs.
