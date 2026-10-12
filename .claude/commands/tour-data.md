---
description: Check the tour prices and dates in tours.json against the live Outdoor Norway pages
allowed-tools: Bash(python3 -I *ski-meta-ads/verify_tours.py*)
disable-model-invocation: true
---
Where the files live: ROOT is `${CLAUDE_PLUGIN_ROOT}`. If that text does not start with a slash, ROOT is the current folder (a clone of the repo). The validator, tools and data are under ROOT. Files you save for the user go in the current folder, never under ROOT. When you tell the user about a file under ROOT, write its real path, not the word ROOT.

Run this one command with the Bash tool and nothing else:

`python3 -I ROOT/campaigns/ski-meta-ads/verify_tours.py`

Say in two lines whether prices, dates and itinerary headings still match. If anything failed, name the tour and the field in `ROOT/campaigns/ski-meta-ads/tours.json`. Never change a price or a date without the user confirming it. If the check cannot reach the website, say so and stop.
