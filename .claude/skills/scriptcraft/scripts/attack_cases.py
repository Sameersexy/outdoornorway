#!/usr/bin/env python3
"""Regression attacks for the scriptcraft validator. Run: python3 -I scripts/attack_cases.py
Each case edits the short example and states whether the validator SHOULD fail it.
A case where expectation and result differ is printed as MISMATCH."""
import os, re, subprocess, sys, tempfile

SK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = open(os.path.join(SK, "examples/short-fictional.md"), encoding="utf-8").read()
CHECK = os.path.join(SK, "scripts/script_check.py")


def set_beat(text, beat, vo=None, facts=None, role=None, visual=None, overlay=None):
    out = []
    for line in text.split("\n"):
        if line.startswith(f"| {beat} |"):
            c = line.split("|")
            # | beat | time | vo | visual | text | role | facts |
            if vo is not None: c[3] = f" {vo} "
            if visual is not None: c[4] = f" {visual} "
            if overlay is not None: c[5] = f" {overlay} "
            if role is not None: c[6] = f" {role} "
            if facts is not None: c[7] = f" {facts} "
            line = "|".join(c)
        out.append(line)
    return "\n".join(out)


def add_fact(text, row):
    return text.replace("## Script", row + "\n## Script", 1)


CASES = [
    # (name, expect_fail, mutated text)
    ("baseline example passes", False, SRC),
    ("aurora: not a chance you miss", True, set_beat(SRC, 5, vo="Not a chance you miss the northern lights.")),
    ("aurora: no question guaranteed", True, set_beat(SRC, 5, vo="The aurora shows up, no question, guaranteed.")),
    ("snow: certain", True, set_beat(SRC, 5, vo="Snow is certain, and you ski down warm.")),
    ("powder every morning", True, set_beat(SRC, 5, vo="Fresh powder every morning. You ski down warm.")),
    ("casual aurora guarantee", True, set_beat(SRC, 5, vo="Honestly you will definitely see the northern lights.")),
    ("slang scarcity", True, set_beat(SRC, 5, vo="Spots are going fast so you ski down warm.")),
    ("invented stat: ninety percent", True, set_beat(SRC, 5, vo="Ninety percent of guests overdress. So you peel one off.")),
    ("invented number: ninety seconds", True, set_beat(SRC, 5, vo="Wet layers chill fast. Ninety seconds and you peel one off.")),
    ("reused digit in new claim", True, set_beat(SRC, 5, vo="10 guides watch your group. You peel one off.", facts="-")),
    ("superlative whitelisted by unrelated fact", True,
     set_beat(add_fact(SRC, "| F9 | Guests say the best part is the waffle | fictional: guest review | yes |"), 5, vo="The best ski guides in Norway keep you warm.")),
    ("two CTAs", True, set_beat(SRC, 3, role="build, cta")),
    ("greeting hook", True, set_beat(SRC, 1, vo="Hey guys, welcome back to the channel.")),
    ("end card with logo (should fail in ugc style)", True, set_beat(SRC, 6, visual="end card with the logo over the snow / logo fades in")),
    ("scarcity: last chance", True, set_beat(SRC, 6, vo="Last chance, send this to your friend.")),
    ("negative framing", True, set_beat(SRC, 4, vo="Only for experts, and you will suffer.")),
    ("overlong beat", True, set_beat(SRC, 2, vo="You start the climb wearing every warm layer you own and then some more besides, plus a scarf and a hat and gloves.")),
    ("ok: casual first person (should pass)", False, set_beat(SRC, 1, vo="I wear too many layers, every single time.")),
]


def run(text):
    d = tempfile.mkdtemp()
    p = os.path.join(d, "t.md")
    open(p, "w", encoding="utf-8").write(text)
    r = subprocess.run(["python3", "-I", CHECK, p], capture_output=True, text=True)
    fails = [l.split(" ")[1] for l in r.stdout.split("\n") if l.startswith("[FAIL]")]
    return r.returncode, fails


mism = 0
for name, expect_fail, text in CASES:
    code, fails = run(text)
    failed = code == 1
    ok = failed == expect_fail
    mism += 0 if ok else 1
    print(f"{'ok      ' if ok else 'MISMATCH'} | expect {'FAIL' if expect_fail else 'PASS'} got {'FAIL' if failed else ('PASS' if code == 0 else 'ERR' + str(code))} | {name} | {','.join(sorted(set(fails)))[:60]}")
print(f"\n{mism} mismatches out of {len(CASES)}")
sys.exit(1 if mism else 0)
