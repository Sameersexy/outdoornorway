#!/usr/bin/env python3
"""Where did the tokens go? Reads one Claude Code session transcript (.jsonl) and prints
the model calls, the cache hit ratio, the fixed part sent on every call, how much of the
context read each kind of entry is responsible for, and the subagent runs.

    python3 -I tools/transcript_report.py [PATH/TO/SESSION.jsonl]

Without a path it reads the most recently written transcript.
Standard library only. Sizes in tokens are estimates at 4 characters per token."""
import collections
import glob
import json
import os
import statistics
import sys

IMAGE_TOKENS = 1600


def strip_images(obj):
    if isinstance(obj, dict):
        if obj.get("type") == "image" or (isinstance(obj.get("source"), dict) and obj["source"].get("type") == "base64"):
            return "IMAGE " + "x" * (IMAGE_TOKENS * 4)
        return {k: strip_images(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [strip_images(v) for v in obj]
    return obj


def size(obj):
    return len(json.dumps(strip_images(obj))) / 4.0


def read_session(path):
    """Return calls (context size per call), entries (kind, tokens, calls so far), compaction call
    indexes, injection counts and the largest prompt snapshot."""
    calls, seen, entries, bounds = [], set(), [], []
    usage_sum = collections.Counter()
    inject = collections.Counter()
    snapshot = None
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            try:
                j = json.loads(line)
            except ValueError:
                continue
            kind, msg = j.get("type"), j.get("message") or {}
            usage = msg.get("usage") if isinstance(msg, dict) else None
            if kind == "assistant" and usage and msg.get("id") not in seen:
                seen.add(msg.get("id"))
                read, make = usage.get("cache_read_input_tokens", 0), usage.get("cache_creation_input_tokens", 0)
                calls.append(read + make + usage.get("input_tokens", 0))
                usage_sum.update(read=read, create=make, output=usage.get("output_tokens", 0))
            if kind == "system" and j.get("subtype") == "compact_boundary":
                bounds.append(len(calls))
            if kind == "attachment":
                a = j.get("attachment") or {}
                t = a.get("type")
                if t == "prompt_snapshot":
                    if snapshot is None or size(a) > size(snapshot):
                        snapshot = a
                    continue
                if t == "skill_listing":
                    inject["skill listing, full" if a.get("isInitial") else "skill listing, delta"] += 1
                if t == "deferred_tools_delta":
                    inject["connector tool-list change"] += 1
                entries.append(("attachment:" + str(t), size(a.get("content", a)), len(calls)))
            elif kind in ("user", "assistant"):
                body = msg.get("content")
                label = "tool_result" if kind == "user" and "tool_result" in json.dumps(body)[:400] else kind
                entries.append((label, size(body), len(calls)))
    return calls, entries, bounds, inject, usage_sum, snapshot


def main(path):
    calls, entries, bounds, inject, use, snap = read_session(path)
    n = len(calls)
    if not n:
        sys.exit("no model calls in this transcript")
    total = sum(calls)
    print("model calls: %d   compactions: %d" % (n, len(bounds)))
    print("context per call: median %.0fk, mean %.0fk, max %.0fk, total %.1fM tokens"
          % (statistics.median(calls) / 1e3, total / n / 1e3, max(calls) / 1e3, total / 1e6))
    hit = use["read"] / max(1, use["read"] + use["create"])
    print("cache read %.1fM, cache write %.2fM, hit ratio %.1f%%, output %.2fM"
          % (use["read"] / 1e6, use["create"] / 1e6, 100 * hit, use["output"] / 1e6))
    for cap in (150e3, 200e3):
        above = sum(max(0, c - cap) for c in calls)
        print("context above %dk: %d%% of calls, %d%% of all context read"
              % (cap / 1e3, 100 * sum(c > cap for c in calls) / n, 100 * above / total))
    fixed = 0
    if snap:
        tools = snap.get("tools") or []
        fixed = size(snap.get("systemPrompt")) + sum(size(t) for t in tools)
        groups = collections.Counter()
        for t in tools:
            name = t.get("name", "?") if isinstance(t, dict) else "?"
            groups["mcp:" + name.split("__")[1] if name.startswith("mcp__") else "built-in"] += size(t)
        top = sorted(((size(t), t.get("name")) for t in tools if isinstance(t, dict)), reverse=True)[:4]
        print("\nfixed part on every call: about %.0fk (%d%% of all context read)" % (fixed / 1e3, 100 * fixed * n / total))
        print("  by source: " + ", ".join("%s %.0fk" % (g, v / 1e3) for g, v in groups.most_common(4)))
        print("  largest tools: " + ", ".join("%s %.1fk" % (name, s / 1e3) for s, name in top))
    print("\nre-injections: " + (", ".join("%s %d" % kv for kv in inject.most_common()) or "none"))

    def later(i):
        end = next((b for b in bounds if b >= i), n)
        return max(0, end - i)

    weight = collections.Counter()
    for label, tok, i in entries:
        weight[label] += tok * later(i)
    conv = max(1, total - fixed * n)
    scale = conv / max(1.0, sum(weight.values()))
    print("\nwhat is re-read most (entry size times the later calls that carry it, until the next compaction):")
    for label, w in weight.most_common(7):
        print("  %-34s %4.0f%% of all context read" % (label, 100 * w * scale / total))

    subs = sorted(glob.glob(os.path.join(path[:-6], "subagents", "agent-*.jsonl")))
    if subs:
        print("\nsubagent runs:")
        for f in subs:
            try:
                meta = json.load(open(f[:-6] + ".meta.json", encoding="utf-8"))
            except (OSError, ValueError):
                meta = {}
            c, _, _, _, u, _ = read_session(f)
            if c:
                print("  %-18s %3d calls, first context %4.0fk, median %4.0fk, cache read %.2fM"
                      % (meta.get("agentType", "?")[:18], len(c), c[0] / 1e3, statistics.median(c) / 1e3, u["read"] / 1e6))


def latest_transcript():
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
