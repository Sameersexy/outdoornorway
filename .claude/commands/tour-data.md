---
description: Check campaigns/ski-meta-ads/tours.json against the live Outdoor Norway pages
allowed-tools: Bash(python3 -I campaigns/ski-meta-ads/verify_tours.py:*)
disable-model-invocation: true
---
!`python3 -I campaigns/ski-meta-ads/verify_tours.py`

Say in two lines whether prices, dates and itinerary headings still match. If anything failed, name the tour and the field in tours.json. Never change a price or a date without the user confirming it.
