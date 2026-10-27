#!/bin/bash
# Installs the scraping tools (crawl4ai, Scrapling) in cloud sessions only.
# Playwright and Patchright are pinned to 1.63.0 so they use the Chromium
# build pre-installed in the cloud container. If a session reports
# "Executable doesn't exist", the container's browser changed: update the pins.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

python3 -m pip install --quiet --disable-pip-version-check --root-user-action=ignore \
  "crawl4ai" "scrapling[fetchers]" "playwright==1.63.0" "patchright==1.63.0"
