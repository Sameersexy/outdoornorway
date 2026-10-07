#!/usr/bin/env python3
"""Regression attacks for the scriptcraft validator. Run: python3 -I scripts/attack_cases.py

Each case edits a clean base fixture and states what the validator must do:
  block  exit 1, and the named rule is among the blocking findings
  warn   the named rule is reported as a warning
  pass   exit 0
  clean  exit 0 with no finding at all
  parse  exit 2 (parse error)
A case where expectation and result differ is printed as MISMATCH. test_script_check.py runs
every case, so a mismatch fails the unit tests.

The bases live in fixtures/ (owned with the validator), not in examples/, so a docs edit to an
example cannot change what these cases test."""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FIX = os.path.join(HERE, "fixtures")
CHECK = os.path.join(HERE, "script_check.py")


def base(name):
    with open(os.path.join(FIX, name), encoding="utf-8") as fh:
        return fh.read()


VO = base("valid-voiceover-loop.md")   # voiceover, the 0.2.0 short example (end card allowed)
TALK = base("valid-ugc-talk.md")       # ugc_talk short, a guide on camera, relationship guide
TEXT = base("valid-ugc-text.md")       # ugc_text, a 10 s text-on-screen loop
LONG = base("valid-long.md")


def set_beat(text, beat, vo=None, facts=None, role=None, visual=None, overlay=None):
    out = []
    for line in text.split("\n"):
        if line.startswith("| %d |" % beat):
            c = line.split("|")
            # | beat | time | vo | visual | text | role | facts |
            for i, v in ((3, vo), (4, visual), (5, overlay), (6, role), (7, facts)):
                if v is not None:
                    c[i] = " %s " % v
            line = "|".join(c)
        out.append(line)
    return "\n".join(out)


def set_meta(text, key, value):
    """Set or add a front matter field; value None removes it."""
    head, rest = text.split("\n---\n", 1)
    lines = [x for x in head.split("\n") if not x.startswith(key + ":")]
    if value is not None:
        lines.insert(2, "%s: %s" % (key, value))
    return "\n".join(lines) + "\n---\n" + rest


def set_caption(text, caption):
    return text.split("## Caption")[0] + "## Caption\n" + caption + "\n"


def add_fact(text, row):
    return text.replace("## Script", row + "\n## Script", 1)


def sub(text, old, new):
    assert old in text, old
    return text.replace(old, new)


B2_GUIDE = "Quick one from me, I guide ski tours for Outdoor Norway."
CASES = [
    # (name, expect, rule, text, extra args)
    # ---- 0.2.0 regressions, voiceover base
    ("baseline voiceover example passes", "pass", None, VO, []),
    ("aurora: not a chance you miss", "block", "BR09", set_beat(VO, 5, vo="Not a chance you miss the northern lights."), []),
    ("aurora: no question guaranteed", "block", "BR09", set_beat(VO, 5, vo="The aurora shows up, no question, guaranteed."), []),
    ("snow: certain", "block", "BR09", set_beat(VO, 5, vo="Snow is certain, and you ski down warm."), []),
    ("powder every morning", "block", "BR09", set_beat(VO, 5, vo="Fresh powder every morning. You ski down warm."), []),
    ("casual aurora guarantee", "block", "BR09", set_beat(VO, 5, vo="Honestly you will definitely see the northern lights."), []),
    ("slang scarcity", "block", "BR04", set_beat(VO, 5, vo="Spots are going fast so you ski down warm."), []),
    ("invented stat: ninety percent", "block", "F04", set_beat(VO, 5, vo="Ninety percent of guests overdress. So you peel one off."), []),
    ("invented number: ninety seconds", "block", "F04", set_beat(VO, 5, vo="Wet layers chill fast. Ninety seconds and you peel one off."), []),
    ("reused digit in new claim", "block", "F04", set_beat(VO, 5, vo="10 guides watch your group. You peel one off.", facts="-"), []),
    ("superlative whitelisted by unrelated fact", "block", "BR11",
     set_beat(add_fact(VO, "| F9 | Guests say the best part is the waffle | fictional: guest review | yes |"), 5,
              vo="The best ski guides in Norway keep you warm."), []),
    ("two CTAs", "block", "C01", set_beat(VO, 3, role="build, cta"), []),
    ("greeting hook", "block", "BR01", set_beat(VO, 1, vo="Hey guys, welcome back to the channel."), []),
    ("scarcity: last chance", "block", "BR04", set_beat(VO, 6, vo="Last chance, send this to your friend."), []),
    ("negative framing", "block", "BR05", set_beat(VO, 4, vo="Only for experts, and you will suffer."), []),
    ("overlong beat", "block", "W03", set_beat(VO, 2, vo="You start the climb wearing every warm layer you own and then some more besides, plus a scarf and a hat and gloves."), []),
    ("ok: casual first person in voiceover", "pass", None, set_beat(VO, 1, vo="I wear too many layers, every single time."), []),
    ("voiceover end card stays allowed", "pass", None,
     set_beat(VO, 6, visual="skier skids to a stop and laughs at the camera / end card with the logo over the snow"), []),

    # ---- ugc_talk and ugc_text: format attacks
    ("ugc end card with logo", "block", "U02",
     set_beat(TALK, 6, visual="skier skids to a stop and laughs at the camera / end card with the logo over the snow"), []),
    ("ugc stock footage and a lower third", "block", "U02",
     set_beat(TALK, 3, visual="stock footage of a mountain range / lower third with the guide's name"), []),
    ("ugc title slide", "block", "U02", set_beat(TALK, 5, visual="a title slide over the ridge / skier drops into the descent"), []),
    ("no person in the first frame", "block", "U01",
     set_beat(TALK, 1, visual="close-up of touring skis leaning on a rack / skins drying on a bench"), []),
    ("text clip opens on landscape only", "block", "U01",
     set_beat(TEXT, 1, visual="wide shot of a snowy ridge at dawn / birch trees under fresh snow"), []),
    ("hook addressing nobody", "warn", "U03",
     set_beat(TALK, 1, vo="Every guest starts this climb a little cold.", overlay="cold on purpose"), []),
    ("capitals for emphasis in the overlay", "warn", "U04", set_beat(TALK, 5, overlay="start COLD, ski warm"), []),
    ("cta is only link in bio", "warn", "U05", set_beat(TALK, 6, vo="Our winter dates are up, link in bio.", overlay="dates up now"), []),
    ("casual marker overload", "warn", "U06",
     set_beat(set_beat(TALK, 2, vo="Okay so, honestly, I guide ski tours for Outdoor Norway."), 5,
              vo="Literally stay dry going up, and you ski down warm."), []),
    ("visual names nobody", "warn", "U07", set_beat(TALK, 3, visual="fleece / trees"), []),
    ("first word after a 2 s pause", "block", "H01", set_beat(TALK, 1, vo="[PAUSE 2] I make every guest start it cold."), []),
    ("emoji in a ugc overlay", "block", "R01", set_beat(TALK, 5, overlay="start cold, ski warm " + chr(0x1F976)), []),
    ("ugc_talk at 90 words", "block", "W01",
     set_beat(set_beat(set_beat(TALK, 3, vo="10 minutes in, you're sweating into every single layer you've got on, top to bottom, and it soaks right through."),
                       4, vo="Wet layers chill you fast at the top, the wind finds every damp spot. So we stop, and you peel one off."),
              5, vo="Stay dry on the way up, keep the puffy in the pack for the top, and you ski down warm and happy."), []),
    ("ugc_text with 30 spoken words", "block", "W01",
     set_beat(set_beat(TEXT, 1, vo="I guide for Outdoor Norway, and here is my rule for you."), 2,
              vo="Start the climb a little cold, peel a layer off at the top, and you ski down warm."), []),
    ("ugc_text with three overlay lines", "block", "O01", set_beat(TEXT, 2, overlay="start cold / peel one off / ski down warm"), []),
    ("ugc_text loop closes before the last beat", "block", "L01",
     sub(TEXT, "| 2 | 5-10 | - | guide peels off a fleece at the top, grinning / skier drops into the descent | start cold, ski down warm | payoff, close:A | - |",
         "| 2 | 5-8 | - | guide peels off a fleece at the top, grinning / skier drops into the descent | start cold, ski down warm | payoff, close:A | - |\n"
         "| 3 | 8-10 | - | skier skids to a stop and laughs at the camera / guide grins | start cold, ski down warm | build | - |"), []),
    ("ugc_text with no overlay in beat 1", "block", "O04", set_beat(TEXT, 1, overlay="-"), []),

    # ---- brand rules in slang
    ("slang aurora guarantee", "block", "BR09", set_beat(TALK, 5, vo="Bro, you will 100 percent see the northern lights up here."), []),
    ("slang powder guarantee", "block", "BR09", set_beat(TALK, 5, vo="You're deffo getting fresh powder on the way down, trust me."), []),
    ("slang scarcity in ugc", "block", "BR04", set_beat(TALK, 5, vo="These dates are going mad fast, so stay dry and ski down warm."), []),
    ("slang negative framing", "block", "BR05", set_beat(TALK, 4, vo="Not gonna lie, this climb will wreck you. So we stop, and you peel one off."), []),
    ("slang: this climb will destroy your legs", "block", "BR05",
     set_beat(TALK, 4, vo="This climb will destroy your legs, I swear. So we stop, and you peel one off."), []),
    ("ski instruction: kill your speed is fine", "clean", None,
     set_beat(TALK, 4, vo="Wet layers chill you fast at the top. So kill your speed, and peel one off."), []),
    ("slang fear framing", "block", "BR05", set_beat(TALK, 4, vo="You'll be dying on this climb, it's brutal. So we stop, and you peel one off."), []),
    ("slang superlative", "block", "BR11", set_beat(TALK, 5, vo="Best guides around, no cap, and you ski down warm."), []),
    ("reused digit in a new ugc claim", "block", "F04", set_beat(TALK, 5, vo="10 guides watch you the whole way up, every day.", facts="-"), []),

    # ---- disclosure and sound
    ("paid guest without Ad in the caption", "block", "D01",
     set_beat(set_meta(TALK, "relationship", "guest_paid"), 2, vo="Quick one: Outdoor Norway paid for this trip, so ad."), []),
    ("paid guest whose disclosure beat does not say paid", "block", "D01",
     set_caption(set_meta(TALK, "relationship", "guest_paid"), "Ad. The layer rule my guide used on every skin track."), []),
    ("gifted guest with no disclosure beat", "block", "D01",
     set_caption(set_beat(set_meta(TALK, "relationship", "guest_gifted"), 2, role="setup"), "#ad The layer rule my guide used."), []),
    ("staff with no disclosure beat", "warn", "D01", set_beat(set_meta(TALK, "relationship", "staff"), 2, role="setup"), []),
    ("staff disclosure beat too late (8 s)", "warn", "D01",
     set_beat(set_beat(set_meta(TALK, "relationship", "staff"), 2, role="setup"), 3, role="build, disclosure"), []),
    ("trending song with a price", "block", "SND01",
     set_beat(add_fact(set_meta(TALK, "sound", "trending"), "| F3 | Day tours from NOK 1,950 per adult | fixture: price list (test data) | yes |"),
              6, overlay="days from NOK 1,950", facts="F3"), []),
    ("trending song with the brand hashtag", "block", "SND01",
     set_caption(set_beat(set_meta(TALK, "sound", "trending"), 2, vo="Quick one from me, I'm a ski guide here."),
                 "The layer rule I use. #outdoornorway"), []),

    # ---- parse errors
    ("invalid style value", "parse", None, set_meta(TALK, "style", "ugc"), []),
    ("old style name polished", "parse", None, set_meta(VO, "style", "polished"), []),
    ("ugc_text in the long tier", "parse", None, set_meta(LONG, "style", "ugc_text"), []),
    ("invalid relationship value", "parse", None, set_meta(TALK, "relationship", "influencer"), []),
    ("invalid sound value", "parse", None, set_meta(TALK, "sound", "viral"), []),

    # ---- must pass
    ("ugc_talk base passes clean", "clean", None, TALK, []),
    ("first-person hook", "clean", None,
     set_beat(TALK, 1, vo="I overdressed on my own first tour, never again."), []),
    ("reply-to-comment format", "clean", None,
     set_beat(TALK, 1, vo="You asked if you'll freeze on the climb. Nope.",
              visual="selfie: guide reads the comment on screen / group skins uphill behind her",
              overlay="replying to: will I freeze?"), []),
    ("guide explains a skill in slang", "clean", None,
     set_beat(TALK, 4, vo="Kick turns are lowkey easy. Plant your pole, swing the ski round, done.", facts="-",
              visual="guide plants a pole on the steep bend / guest swings a ski round, grinning"), []),
    ("a guide says honestly once", "clean", None,
     set_beat(TALK, 5, vo="Honestly, stay dry on the way up, and you ski down warm."), []),
    ("ski move: the guest copies the slide", "clean", None,
     set_beat(TALK, 3, visual="guide's skis glide forward / the guest copies the slide on the skin track"), []),
    ("ski verb slide is not a slide", "clean", None,
     set_beat(TALK, 1, visual="selfie: guide on the skin track / skis on skins slide uphill behind her"), []),
    ("text-only loop clip", "clean", None, TEXT, []),
    ("silent text clip with an unpaid guest", "clean", None,
     set_beat(set_meta(set_meta(TEXT, "relationship", "guest_unpaid"), "creator", "guest"), 1, vo="-", role="hook, open:A"), []),
    ("gifted guest done right", "clean", None,
     set_caption(set_beat(set_meta(TALK, "relationship", "guest_gifted"), 2,
                          vo="Quick one: this trip was gifted, so this is an ad."),
                 "Ad. The layer rule my guide used on every skin track."), []),
    ("trending song with no brand, trip or price", "clean", None,
     set_caption(set_beat(set_meta(TALK, "sound", "trending"), 2, vo="Quick one from me, I'm a ski guide here."),
                 "The layer rule I use on every skin track. #skitouring"), []),
    ("commercial library sound with a price", "pass", None,
     set_beat(add_fact(set_meta(TALK, "sound", "commercial_library"), "| F3 | Day tours from NOK 1,950 per adult | fixture: price list (test data) | yes |"),
              6, overlay="days from NOK 1,950", facts="F3"), []),

    # ---- independent verification round: false negatives and false positives found and fixed
    ("stock footage with a word between", "block", "U02",
     set_beat(TALK, 3, visual="stock drone footage of the fjord / guest grins at the lens"), []),
    ("animated route map", "block", "U02",
     set_beat(TALK, 3, visual="animated route map of the weekend / guest grins at the lens"), []),
    ("closing card with the dates", "block", "U02",
     set_beat(TALK, 6, visual="skier laughs at the camera / closing card with the dates"), []),
    ("paid guest says not paid", "block", "D01",
     set_caption(set_beat(set_meta(TALK, "relationship", "guest_paid"), 2, vo="Quick one, I'm not paid to say this, honestly."),
                 "Ad. My trip."), []),
    ("gifted guest overlay says not an ad", "block", "D01",
     set_caption(set_beat(set_meta(TALK, "relationship", "guest_gifted"), 2, vo="Quick one from me, the guide here was great.",
                          overlay="not an ad"), "#ad my trip"), []),
    ("link-only ask in a story beat", "warn", "U05",
     set_beat(set_beat(TALK, 6, role="build"), 5, vo="Comment link and I'll send you the dates.", role="payoff, close:A"), []),
    ("trending song on a post naming a weekend", "block", "SND01",
     set_beat(set_meta(TALK, "sound", "trending"), 2, vo="Quick one from me, I'm a ski guide on this weekend."), []),
    ("ok: cta points to dates in the caption", "clean", None,
     set_beat(TALK, 6, vo="Dates are in the caption if you're keen.", overlay="-"), []),
    ("ok: how to book is down in the caption", "clean", None,
     set_beat(TALK, 6, vo="How to book is down in the caption.", overlay="-"), []),
    ("ok: gifted guest with a Reklame caption", "clean", None,
     set_caption(set_beat(set_meta(TALK, "relationship", "guest_gifted"), 2, vo="Quick one: this trip was gifted, so it's reklame."),
                 "Reklame. The layer rule my guide used."), []),
    ("ok: paid guest with an Advert caption", "clean", None,
     set_caption(set_beat(set_meta(TALK, "relationship", "guest_paid"), 2, vo="Quick one: I was paid to film this, so it's an ad."),
                 "Advert. The layer rule my guide used."), []),
    ("ok: an animated guest is a person, not a graphic", "clean", None,
     set_beat(TALK, 3, visual="an animated guest laughs at the lens / skin track winds up through birch trees"), []),
    ("ok: final frame cuts back for the loop", "clean", None,
     set_beat(TEXT, 2, visual="guide peels off a fleece at the top / final frame cuts back to the skis"), []),
]


def run_case(text, args=()):
    """(exit code, blocking rule ids, warning rule ids) for one script text."""
    import tempfile
    d = tempfile.mkdtemp()
    p = os.path.join(d, "t.md")
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(text)
    r = subprocess.run([sys.executable, "-I", CHECK, p, "--json"] + list(args), capture_output=True, text=True)
    os.remove(p)
    os.rmdir(d)
    try:
        data = json.loads(r.stdout)
    except ValueError:
        return r.returncode, set(), set()
    found = data.get("findings", [])
    return (r.returncode, {f["id"] for f in found if f["severity"] == "block"},
            {f["id"] for f in found if f["severity"] == "warn"})


def judge(expect, rule, code, blocks, warns):
    if expect == "block":
        return code == 1 and (rule is None or rule in blocks)
    if expect == "warn":
        return rule in warns
    if expect == "pass":
        return code == 0
    if expect == "clean":
        return code == 0 and not blocks and not warns
    if expect == "parse":
        return code == 2
    raise ValueError(expect)


def run_all(verbose=True):
    """Run every case; returns the names of the mismatches."""
    bad = []
    for name, expect, rule, text, args in CASES:
        code, blocks, warns = run_case(text, args)
        ok = judge(expect, rule, code, blocks, warns)
        if not ok:
            bad.append(name)
        if verbose:
            got = "exit %d" % code
            print("%s | expect %-5s %-6s got %s | %s | block %s warn %s"
                  % ("ok      " if ok else "MISMATCH", expect, rule or "", got, name,
                     ",".join(sorted(blocks)) or "-", ",".join(sorted(warns)) or "-"))
    if verbose:
        print("\n%d mismatches out of %d" % (len(bad), len(CASES)))
    return bad


if __name__ == "__main__":
    sys.exit(1 if run_all() else 0)
