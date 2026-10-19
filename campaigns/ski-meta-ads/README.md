# Ski Meta ads folder

This README is for anyone editing the ski ad copy or checking tour prices and dates before an ad goes live.

## Files

Each file is listed with what it does. Run commands from the repo root.

| File | What it does |
|---|---|
| [01-simplified-copy.md](01-simplified-copy.md) | On-image copy for each ski tour: name, dates and price, built from tours.json. |
| [03-review-of-first-cut-copy.md](03-review-of-first-cut-copy.md) | Review of the first-cut copy for nine Meta creatives, checked against the live tour pages, with fixes. |
| [04-questions-for-sameer.md](04-questions-for-sameer.md) | Open questions that stop specific claims from going into ads, with safe wording until each one is answered. |
| [build_simple_copy.py](build_simple_copy.py) | Rebuilds 01-simplified-copy.md from tours.json. |
| [tours.json](tours.json) | Source of truth for prices, dates and day-by-day plans. |
| [verify_tours.py](verify_tours.py) | Checks tours.json against the live hub and tour pages. Needs network access. |
| [README.md](README.md) | This file. |

## Why the folder has this name

The name follows the file contents. The tours are ski trips, and tours.json holds their prices, dates and plans. The ad copy is for Meta, and file 03 reviews nine Meta creatives.

## Why there is no 02 file

Git history has never held a 02 file in this folder. The files that have ever been here are 01, 03, 04, the build script, tours.json and verify_tours.py. No commit deletes a file from the folder. File 01 came in commit 3554144, and files 03 and 04 came in commit d7609ec.

[VERIFY: why there is no 02 file]

## Source of truth

tours.json is the source of truth for prices, dates and day-by-day plans. Its price_source field names the hub page as the price reference, because tour page prices are known to be stale on two tours.

## Check the data

verify_tours.py needs network access to the live site. Run it from the repo root:

```
python3 -I campaigns/ski-meta-ads/verify_tours.py
```

It checks that the hub price matches each tour's price, that each date range spans the tour's trip length, and that each itinerary has one entry per day with its heading on the live page. Exit code 0 means every check passed.

To rebuild the copy in [01-simplified-copy.md](01-simplified-copy.md), run:

```
python3 -I campaigns/ski-meta-ads/build_simple_copy.py
```

This overwrites 01-simplified-copy.md. Run the check first, so the copy comes from data the live pages support.

## Paths that must not move

Keep this folder at `campaigns/ski-meta-ads/`. The validator at `.claude/skills/scriptcraft/scripts/script_check.py` finds tours.json by going up from its own folder to this one, so moving the folder breaks its `--tour` option. Other paths that must not move are listed in the [repo map](../../docs/repo-map.md).

## Page-audit notes

The page-audit notes in this folder stay public on purpose (owner decision, 12 October 2026, recorded in CLAUDE.md). File 03 checks copy against the live pages, and file 04 lists the claims those pages leave open. The repo is public, so add no personal data, contact details or private client information to this folder.

## Open items

File 04 holds the open questions for the owner, each with the safe wording the drafts use until it is answered. This README does not answer them. All guides are listed in [docs/README.md](../../docs/README.md).
