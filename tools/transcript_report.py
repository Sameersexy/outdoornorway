#!/usr/bin/env python3
"""Where did the tokens go? Reads one Claude Code session transcript (.jsonl) and prints
the model calls, the context size per call, and the biggest entries.

    python3 -I tools/transcript_report.py [PATH/TO/SESSION.jsonl]

Without a path it reads the most recently written transcript.

The transcript lives under ~/.claude/projects/<project>/<session id>.jsonl.
Standard library only. Sizes in tokens are estimates at 4 characters per token."""
import collections
import json
import sys


IMAGE_TOKENS = 1600  # an image costs about this much context, whatever its base64 length


def strip_images(obj):
    """Replace base64 image data with a short stand-in, so images are not counted by their encoded size."""
    if isinstance(obj, dict):
        if obj.get("type") == "image" or (isinstance(obj.get("source"), dict) and obj["source"].get("type") == "base64"):
            return "IMAGE " + "x" * (IMAGE_TOKENS * 4)
        return {k: strip_images(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [strip_images(v) for v in obj]
    return obj


def main(path):
    calls, seen = [], set()
    sizes = collections.Counter()
    counts = collections.Counter()
    big = []
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            try:
                j = json.loads(line)
            except ValueError:
                continue
            kind = j.get("type")
            msg = j.get("message") or {}
            usage = msg.get("usage") if isinstance(msg, dict) else None
            if kind == "assistant" and usage and msg.get("id") not in seen:
                seen.add(msg.get("id"))
                calls.append(usage.get("cache_read_input_tokens", 0))
            body = json.dumps(strip_images(j.get("attachment") if kind == "attachment" else msg.get("content")))
            label = kind
            if kind == "attachment":
                label = "attachment:" + str((j.get("attachment") or {}).get("type"))
            elif kind == "user" and "tool_result" in body[:400]:
                label = "tool_result"
            sizes[label] += len(body)
            counts[label] += 1
            big.append((len(body), label, body[:70]))
    print("model calls: %d" % len(calls))
    if calls:
        calls.sort()
        print("context read per call: median %.0fk, max %.0fk, total %.1fM tokens"
              % (calls[len(calls) // 2] / 1e3, calls[-1] / 1e3, sum(calls) / 1e6))
    print("\ntext by kind (estimated tokens):")
    for label, n in sizes.most_common(8):
        print("  %-30s %7.0fk  (%d entries)" % (label, n / 4e3, counts[label]))
    print("\nbiggest single entries:")
    for n, label, head in sorted(big, reverse=True)[:8]:
        print("  %6.0fk  %-26s %s" % (n / 4e3, label, head.replace("\n", " ")))


def latest_transcript():
    """The most recently written transcript under ~/.claude/projects, or None."""
    import glob
    import os
    files = glob.glob(os.path.expanduser("~/.claude/projects/*/*.jsonl"))
    return max(files, key=os.path.getmtime) if files else None


if __name__ == "__main__":
    if len(sys.argv) > 2:
        sys.exit(__doc__)
    target = sys.argv[1] if len(sys.argv) == 2 else latest_transcript()
    if not target:
        sys.exit("no transcript found under ~/.claude/projects")
    print("transcript: " + target)
    main(target)
