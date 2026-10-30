# October 2026 marketing review deck

Ticket: none (monthly company meeting deliverable). Branch: `sameer/busy-archimedes-fmj23y`.

The output is a leadership deck in the September 2026 design, built from ClickUp, HubSpot, the repo, Drive meeting notes, Calendar, Gmail and the owner's pasted session notes. Data and the finished deck hold private company metrics, so they live outside this public repo (session scratchpad, then the owner's Google Drive). Only this plan is committed.

## Phases

### Phase 1: Collect (parallel agents, one file each)
Verified when: every agent has written its JSON or markdown file to the scratchpad `data/` folder and a one-line summary with counts and gaps.
Files to touch: scratchpad `data/*.json`, `data/*.md`.

#### Step 1.1: ClickUp shipped list (Size: S)
- Acceptance: all tasks closed 1 to 31 Oct in the Marketing & Growth and MKT & DESIGN folders, with list, status, assignees, close date and a one-line description from the task body. Grouped into web pages, emails, ads, social, blogs, SEO, other. Owner's tasks flagged.
- Verification: row count matches the filter count (68 at research time).
- Blocked by: none.

#### Step 1.2: HubSpot email performance (Size: S)
- Acceptance: per-email table for every marketing email with October sends (63 at research time): name, send date, type, delivered, open, click, bounce, unsubscribes, replies. Totals and weighted rates. Unsubscribe survey reasons for October. Monthly health score.
- Verification: totals recomputed from rows match within rounding.
- Blocked by: none.

#### Step 1.3: HubSpot outcomes (Size: S)
- Acceptance: deals created and won in October with amount and source; form submissions on brochure and guide downloads; new contacts by source; landing pages and site pages published in October.
- Verification: each number cites the query that produced it.
- Blocked by: none.

#### Step 1.4: Meetings, mail and chat (Size: M)
- Acceptance: challenges, decisions, action items and next-month commitments pulled from the five Drive Gemini notes, October calendar events, Gmail threads and ClickUp DMs the owner took part in. Each item cites its source and date.
- Verification: every bullet has a source line.
- Blocked by: none.

#### Step 1.5: Repo and Claude Code work (Size: S)
- Acceptance: October commits grouped by theme, scripts and copy produced, skills and plugins added, PRs merged, plus the cloud session list from 26 Oct. Placeholder for the owner's local session notes.
- Verification: commit count matches `git log --since=2026-10-01`.
- Blocked by: none.

### Phase 2: Synthesise
Verified when: `data/review.md` exists with every number traced to a Phase 1 file and every gap named.
Files to touch: scratchpad `data/review.md`.

#### Step 2.1: Scorecard against the September deck's five October priorities (Size: S)
- Blocked by: 1.1, 1.4, 1.5.

#### Step 2.2: Wins, challenges, action items, November goals and Q4 to Q1 projection (Size: M)
- Projection is per channel from October baselines, not a revenue forecast.
- Blocked by: 1.2, 1.3, 1.4, 2.1.

### Phase 3: Build the deck
Verified when: the PDF opens, matches the September design tokens, and a fact check passes on every number.
Files to touch: scratchpad `deck/index.html`, `deck/October_2026_Marketing_Review.pdf`.

#### Step 3.1: HTML deck in the September design, exported to PDF with Playwright (Size: M)
- Blocked by: 2.2.

#### Step 3.2: Fact check and gap slide (Size: S)
- Run the fact-check skill over the deck text against the Phase 1 files.
- Blocked by: 3.1.

## Decision log
| Decision | Chosen option | Why |
| --- | --- | --- |
| Where data and deck live | Scratchpad, then Drive | Repo is public; metrics and names are private |
| Design | September 2026 tokens | Continuity for the leadership audience |
| Ads | Creatives created and shared, from ClickUp, no performance | Owner decision, 30 Oct |
| Scope | Whole marketing team, owner's items flagged | Owner decision, 30 Oct |
| Data cut | One pull, through 29 Oct, no refresh | Owner decision, 30 Oct |
| Build order | Slide breakdown in chat, feedback rounds, then build | Owner decision, 30 Oct |
| Email scope | Marketing and download emails only; transactional and 2025 flows excluded | Owner decision, 30 Oct |
| Deliverable count | Tasks with dated October work (33), bulk closes explained in a footer | Default after recheck, 30 Oct |
| Paid media slide | Kept, sourced from the team tracker, platform lead counts withheld | Default after recheck, 30 Oct |

## Not yet specified
- Phase 1: ads performance source (owner export or none).
- Phase 1: owner's local session notes, pasted after collection.
- Phase 3: output format if not an HTML deck to PDF.

## Always / Never
- Always: cite the source for every number; show gaps as gaps; British English; no dashes or emojis.
- Never: commit metrics, names or meeting content to the repo; invent a figure; forecast revenue.

## Progress
| Phase | Status |
| --- | --- |
| 1 Collect | done 29 Oct, v1 then rechecked by 13 Opus agents (v2) |
| 2 Synthesise | done, review_v2.md in scratchpad |
| 3 Build | in progress, 17-slide HTML deck rendered to PDF |
