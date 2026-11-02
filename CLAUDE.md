# Outdoor Norway marketing repo

What is here
- `.claude/skills/scriptcraft/`: video script skill, validator (`scripts/script_check.py`), fixtures and tests. Agents: `.claude/agents/script-writer.md`, `script-reviewer.md`.
- `campaigns/ski-meta-ads/tours.json`: source of truth for prices, dates and day-by-day plans. Check it with `verify_tours.py`.
- `adquill/`: paused ad-copy skill and agents (drafts, not installed by the plugin).
- `content/scripts/`: finished and draft scripts, each with a notes file. `docs/`: research and test write-ups.
- Folder map, and the paths that must not move: `docs/repo-map.md`. All guides: `docs/README.md`.

Commands
- Tests: `python3 -I .claude/skills/scriptcraft/scripts/test_script_check.py` and `python3 -I tools/test_repo_integrity.py`
- Validate a script: `python3 -I .claude/skills/scriptcraft/scripts/script_check.py FILE [--final] [--strict]`
- Live data check: `python3 -I campaigns/ski-meta-ads/verify_tours.py`
- Slash commands (in `.claude/commands/`): `/script`, `/review-script`, `/validate`, `/open-items`, `/tour-data`, `/tokens`, `/howto`. The validator takes `--brief` for a short report and `--open-items` for the placeholder list.

Rules
- Commands and agents reach repo files through ROOT (`${CLAUDE_PLUGIN_ROOT}`, or the current folder in a clone). Do not add `!` shell lines with `${...}` or bare repo paths to commands. `/howto` embeds the guide's Quick start: after editing it, regenerate `.claude/commands/howto.md` (the integrity test checks they match).
- The repo is public and MIT licensed. Do not add supplier terms, personal data or other private client information. The page-audit notes in `campaigns/ski-meta-ads/` stay public on purpose (owner decision, 12 October 2026).
- Facts come from tours.json, `.claude/product-marketing.md` or a page the client names. Never invent a fact, a guide's words or a URL.
- No model names in any file. No em or en dashes, no emojis.
- Work on the branch the session names. Open a pull request only when asked.

Web scraping
- Read web pages only with `obscura`, `crwl` (Crawl4AI) or `scrapling`, run through Bash. Do not use Firecrawl tools, WebFetch, Playwright MCP or curl for page content.
- Start with `obscura fetch URL --dump markdown`. Use `obscura scrape URL1 URL2` for batches and add `--stealth` if a site blocks it.
- Use `CRAWL4AI_NO_CLOUD_NOTICE=1 crwl crawl URL -o markdown` to crawl a whole site or extract structured data. Local only, never Crawl4AI Cloud.
- Use `scrapling extract get URL out.md` or `scrapling extract fetch URL out.md` for anti-bot pages. Add `-s "css selector"` to keep only matching content.
- Respect robots.txt (`--obey-robots` in Obscura). Save large output to a file and read only what you need.
- If all three tools fail on a page, say so and stop. Web search is not covered, so ask before using a search tool.

Tokens (details in `docs/token-hygiene.md`)
- One deliverable per session. Compact early.
- Subagents and workflows return paths, scores and short lists. Long reports go to files.
- Do not print whole files or full validator output. Filter with grep, or read with an offset and limit.
- Use `script_check.py --brief`, `--limits TIER STYLE` and `--tour TOUR_ID` instead of reading whole rule or tour files.

Compact instructions
- Keep: the script and notes paths, the last RESULT lines, open items and who confirms them, the branch name, and decisions the user made.
- Drop: pasted script text, validator dumps and file contents that are on disk.
