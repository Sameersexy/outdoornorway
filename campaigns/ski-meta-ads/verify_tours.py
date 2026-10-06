#!/usr/bin/env python3
"""Check tours.json against the live Outdoor Norway pages.

Run:  python3 -I campaigns/ski-meta-ads/verify_tours.py
Exit code 0 means every price, date string and trip length checked out.
Standard library only.
"""
import datetime as dt
import html
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
HUB = "https://www.outdoornorway.com/ski"
UA = {"User-Agent": "Mozilla/5.0 (tour-data-verifier)"}


def fetch(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode("utf-8", "replace")


def norm(s):
    s = html.unescape(s)
    s = s.replace("\u2013", "-").replace("\u2014", "-").replace("\u00a0", " ")
    return re.sub(r"\s+", " ", s).strip()


def page_lines(raw):
    t = re.sub(r"<script.*?</script>|<style.*?</style>|<noscript.*?</noscript>", "", raw, flags=re.S)
    t = re.sub(r"</(p|div|li|h[1-6]|tr|section|span)>", "\n", t)
    t = re.sub(r"<[^>]+>", "\n", t)
    return [norm(x) for x in t.split("\n") if norm(x)]


def money_to_int(text):
    m = re.search(r"NOK\s*([\d,]+)(?:\.\d+)?", text)
    return int(m.group(1).replace(",", "")) if m else None


def main():
    data = json.load(open(os.path.join(HERE, "tours.json"), encoding="utf-8"))
    problems = []
    notes = []

    hub = page_lines(fetch(HUB))
    for t in data["tours"]:
        # 1. hub price: first NOK line within 6 lines after the hub card title
        want = norm(t["hub_name"]).upper()
        idx = next((i for i, l in enumerate(hub) if l.upper() == want), None)
        if idx is None:
            problems.append(f"{t['id']}: hub title not found: {t['hub_name']}")
            continue
        hub_price = next((money_to_int(l) for l in hub[idx + 1: idx + 7] if "NOK" in l), None)
        if hub_price != t["price_nok"]:
            problems.append(f"{t['id']}: hub price {hub_price} != json {t['price_nok']}")

        # 2. tour page
        lines = page_lines(fetch(t["url"]))
        blob = " | ".join(lines)
        for d in t.get("departures", []):
            if d["page_text"] not in blob:
                problems.append(f"{t['id']}: date string not on page: {d['page_text']}")
            a = dt.date.fromisoformat(d["start"])
            b = dt.date.fromisoformat(d["end"])
            span = (b - a).days + 1
            if span != t["days"]:
                problems.append(f"{t['id']}: {d['start']}..{d['end']} spans {span} days, tour is {t['days']}")
            if a < dt.date.fromisoformat(data["as_of"]):
                problems.append(f"{t['id']}: departure {d['start']} is in the past")
            notes.append(f"{t['id']}: {a.strftime('%a %d %b %Y')} to {b.strftime('%a %d %b %Y')}")
        rec = t.get("recurring")
        if rec and rec["page_text"] not in blob:
            problems.append(f"{t['id']}: recurring text not on page: {rec['page_text']}")

        # 3. report what the tour page itself says about price (informational)
        on_page = sorted({money_to_int(l) for l in lines if re.search(r"(from|FROM)\s*(NOK\s*)?[\d,]{4,}", l) and money_to_int(l)})
        raw_from = [l for l in lines if re.match(r"(?i)from\s+[\d,]+\s*\(?NOK", l)]
        if raw_from:
            m = re.search(r"([\d,]{4,})", raw_from[0])
            on_page.append(int(m.group(1).replace(",", "")))
        stale = t.get("stale_page_price_nok")
        notes.append(f"{t['id']}: hub {hub_price} | json {t['price_nok']} | tour page price strings {sorted(set(on_page))}" + (f" | known stale {stale}" if stale else ""))

    print("\n".join(notes))
    print()
    if problems:
        print("FAILED")
        print("\n".join(" - " + p for p in problems))
        return 1
    print(f"OK: {len(data['tours'])} tours verified against live pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())
