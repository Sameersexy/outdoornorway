# Outdoor Norway marketing repo

What is here
- `.claude/skills/scriptcraft/`: video script skill, validator (`scripts/script_check.py`), fixtures and tests. Agents: `.claude/agents/script-writer.md`, `script-reviewer.md`.
- `campaigns/ski-meta-ads/tours.json`: source of truth for prices, dates and day-by-day plans. Check it with `verify_tours.py`.
- `content/scripts/`: finished and draft scripts, each with a notes file. `docs/`: research and test write-ups.

Commands
- Tests: `python3 -I .claude/skills/scriptcraft/scripts/test_script_check.py`
- Validate a script: `python3 -I .claude/skills/scriptcraft/scripts/script_check.py FILE [--final] [--strict]`
- Live data check: `python3 -I campaigns/ski-meta-ads/verify_tours.py`
- Slash commands (in `.claude/commands/`): `/script`, `/review-script`, `/validate`, `/open-items`, `/tour-data`, `/tokens`. The validator takes `--brief` for a short report and `--open-items` for the placeholder list.

Rules
- Facts come from tours.json, `.claude/product-marketing.md` or a page the client names. Never invent a fact, a guide's words or a URL.
- No model names in any file. No em or en dashes, no emojis.
- Work on the branch the session names. Open a pull request only when asked.

Tokens (details in `docs/token-hygiene.md`)
- One deliverable per session. Compact early.
- Subagents and workflows return paths, scores and short lists. Long reports go to files.
- Do not print whole files or full validator output. Filter with grep, or read with an offset and limit.
