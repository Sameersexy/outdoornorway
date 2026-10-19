# Ski Meta ads folder

This folder holds the tour data (`tours.json`), the script that checks it against the live site and the ski ad copy notes. Read it before you edit the copy or confirm a price or date for an ad. Run every command from the repo root.

| File | What it does |
|---|---|
| [tours.json](tours.json) | Source of truth for prices, dates and day-by-day plans |
| [verify_tours.py](verify_tours.py) | Checks `tours.json` against the live hub and tour pages. Needs network access |
| [build_simple_copy.py](build_simple_copy.py) | Rebuilds `01-simplified-copy.md` from `tours.json` |
| [01-simplified-copy.md](01-simplified-copy.md) | On-image copy for each ski tour: name, dates and price |
| [03-review-of-first-cut-copy.md](03-review-of-first-cut-copy.md) | Review of the first-cut copy for nine Meta creatives, checked against the live tour pages, with fixes |
| [04-questions-for-sameer.md](04-questions-for-sameer.md) | Open questions that keep specific claims out of ads, with the safe wording until each one is answered |

## Source of truth

`tours.json` holds the prices, dates and day-by-day plans. Its `price_source` field names the hub page as the price reference, because tour page prices are stale on two tours. The validator reads the file through `script_check.py --tour TOUR_ID`.

## Check the data

Run this after you change `tours.json`:

```
python3 -I campaigns/ski-meta-ads/verify_tours.py
```

For each tour it checks that:

- the hub price matches `price_nok`;
- each date string appears on the tour page, each date range spans the tour's trip length and no departure is before `as_of`;
- the itinerary has one entry per day, and each day heading appears on the live page.

Exit code 0 means every check passed. A failure prints the problems after `FAILED`.

To rebuild the copy in [01-simplified-copy.md](01-simplified-copy.md), run the check first, then:

```
python3 -I campaigns/ski-meta-ads/build_simple_copy.py
```

The script overwrites `01-simplified-copy.md`.

## Public notes

The page-audit notes (files 03 and 04) stay public on purpose. This is an owner decision of 12 October 2026, recorded in [CLAUDE.md](../../CLAUDE.md). Add no personal data, contact details or private client information to this folder.

## Paths that must not move

Keep this folder at `campaigns/ski-meta-ads/`. `script_check.py` finds `tours.json` by going up four folders from its own folder, so a move breaks `--tour` unless you pass `--tours-file`. The [repo map](../../docs/repo-map.md) lists the other paths that stay put.
