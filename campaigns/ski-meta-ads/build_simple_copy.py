#!/usr/bin/env python3
"""Build the simplified on-image copy (name, dates, price) from tours.json.

Run:  python3 -I campaigns/ski-meta-ads/build_simple_copy.py
Writes campaigns/ski-meta-ads/01-simplified-copy.md

Every number comes from tours.json, which verify_tours.py checks against the live pages.
The layout follows the 3-Day Autumn Getaway ad that the client's audit found performs:
line 1 name, line 2 dates, line 3 price pill.
"""
import datetime as dt
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
MON = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
MON_FULL = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
LINE_BUDGET = 30  # characters, research heuristic for one on-image line at large size


def money(n):
    return f"{n:,}"


def start_dates_line(departures):
    """Compact start-date line grouped by month, e.g. JAN 30 | FEB 11, 20 | MAR 13."""
    groups = {}
    for d in departures:
        s = dt.date.fromisoformat(d["start"])
        groups.setdefault(s.month, []).append(s.day)
    parts = [f"{MON[m - 1]} {', '.join(str(x) for x in days)}" for m, days in sorted(groups.items())]
    return " | ".join(parts)


def range_text(d):
    a = dt.date.fromisoformat(d["start"])
    b = dt.date.fromisoformat(d["end"])
    if a.month == b.month:
        return f"{a.day} to {b.day} {MON_FULL[b.month - 1]}"
    return f"{a.day} {MON_FULL[a.month - 1]} to {b.day} {MON_FULL[b.month - 1]}"


def short_dates(t):
    n = len(t["departures"])
    a = dt.date.fromisoformat(t["departures"][0]["start"])
    b = dt.date.fromisoformat(t["departures"][-1]["end"])
    first = MON[a.month - 1]
    last = MON[b.month - 1]
    span = first if first == last else f"{first} TO {last}"
    return f"{n} DEPARTURES, {span} 2027"


def price_line(t):
    if t["price_qualifier"] == "from":
        return f"STARTING FROM NOK {money(t['price_nok'])}"
    return f"NOK {money(t['price_nok'])} PER ADULT"


def main():
    data = json.load(open(os.path.join(HERE, "tours.json"), encoding="utf-8"))
    names = data["display_name_lines"]
    out = []
    out.append("# Simplified ski copy: tour name, dates, price\n")
    out.append(f"Built from `tours.json` (as of {data['as_of']}, season {data['season']}). Prices are the confirmed hub prices in NOK. "
               "Layout follows the 3-Day Autumn Getaway ad that the client audit found performs best: name on top, date line with a calendar icon, "
               "price in a white pill.\n")
    out.append("How to read the dates: the compact line lists **start dates**, the same convention as the winning ad (`SEP 11,18, 25 | OCT 02`). "
               "The trip length is in the name, so the end date is implied. Full ranges are listed under each tour for the designer and for the landing page.\n")
    out.append("## At a glance\n")
    out.append("| Tour | Dates (start dates, 2027) | Price |")
    out.append("|---|---|---|")
    for t in data["tours"]:
        dates = start_dates_line(t["departures"]) if t["kind"] == "multi-day" else "EVERY SAT + SUN | JAN TO APR"
        table_price = f"from NOK {money(t['price_nok'])}" if t["price_qualifier"] == "from" else f"NOK {money(t['price_nok'])} per adult"
        out.append(f"| {t['name']} | {dates.replace('|', '/')} | {table_price} |")
    out.append("")
    out.append("## Per tour, ready for the designer\n")
    warnings = []
    for t in data["tours"]:
        lines = names[t["id"]]
        if t["kind"] == "multi-day":
            dates_compact = start_dates_line(t["departures"])
            dates_short = short_dates(t)
        else:
            dates_compact = "EVERY SAT + SUN | JAN TO APR"
            dates_short = "SAT + SUN, JAN TO APR"
        price = price_line(t)
        out.append(f"### {t['name']}\n")
        out.append("On-image text (3 blocks):\n")
        out.append("```")
        for ln in lines:
            out.append(ln)
        out.append(f"[calendar icon] {dates_compact}")
        out.append(f"[pill] {price}")
        out.append("```\n")
        counts = [("Name line 1", lines[0]), ("Name line 2", lines[1]), ("Dates", dates_compact), ("Price pill", price)]
        out.append("Character counts: " + ", ".join(f"{k} {len(v)}" for k, v in counts) + ".\n")
        for k, v in counts:
            if len(v) > LINE_BUDGET:
                warnings.append((t["name"], k, len(v)))
        if len(dates_compact) > LINE_BUDGET:
            out.append(f"Dates line is over {LINE_BUDGET} characters. Short alternative if it will not fit at a readable size: `{dates_short}`.\n")
        out.append(f"Link: {t['url']}\n")
        if t["kind"] == "multi-day":
            out.append("Full departures (start to end, 2027):\n")
            for d in t["departures"]:
                a = dt.date.fromisoformat(d["start"])
                b = dt.date.fromisoformat(d["end"])
                tag = f" ({d['label']})" if d.get("label") else ""
                out.append(f"- {range_text(d)} ({a.strftime('%a')} to {b.strftime('%a')}){tag}")
            out.append("")
        else:
            out.append(f"Dates: {t['recurring']['text']}. Private departures on request.\n")
        out.append(f"Price note: {t['price_basis']}\n")
        if t.get("stale_page_price_nok"):
            out.append(f"Data warning: the tour page still shows NOK {money(t['stale_page_price_nok'])}. Use NOK {money(t['price_nok'])}.\n")
    out.append("## Rules used\n")
    out.append("- Prices are the confirmed hub prices. The two 3-day tour pages show stale prices and must not be used.\n"
               "- Only 2027 departures are listed. The 3-Day Winter Multi-Sport page still shows past 2026 dates.\n"
               "- Day tours say per adult because youth is NOK 1,753 and the page quotes lower open group prices that need three guests.\n"
               "- No scarcity wording. The hub shows a \"Few Slots left\" badge, but live availability is not confirmed.\n"
               "- UTM: add Meta UTMs to the links. The ClickUp links carried `utm_source=chatgpt.com`, which mislabels paid traffic.\n")
    if warnings:
        out.append("## Lines over the character heuristic\n")
        for n, k, c in warnings:
            out.append(f"- {n}: {k} is {c} characters")
        out.append("")
    path = os.path.join(HERE, "01-simplified-copy.md")
    open(path, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("wrote", path)


if __name__ == "__main__":
    main()
