---
name: figma-ads
description: Turns one master ad that a person designed in Figma into the other ad sizes (1:1 and 9:16 today) for one or more Outdoor Norway tours. It re-adapts each size (photo crop and focal point, type sizes, line breaks, safe zones, library components and brand variables), gives every tour its own copy from tours.json and its own photo of that tour's activity, then screenshots, self-checks and exports PNGs. Works through the official Figma MCP server. Run it by name on a staging frame; it writes to the Figma file.
disable-model-invocation: true
---

# figma-ads

Sameer or a freelance designer designs one master ad in Figma and puts it in a staging frame. This skill reads that master and builds the missing sizes next to it, for one tour or several. It adapts each size the way a designer would. It never just scales the master.

ROOT is `${CLAUDE_PLUGIN_ROOT}`. If that text does not start with a slash, ROOT is the current folder (a clone of the repo). Repo paths below (`.claude/`, `campaigns/`) are under ROOT.

## Sizes

One table, so a size can be added later with one row. The safe zones are assumptions until someone confirms them against Meta's current guide.

| Ratio | Name tag | Pixels | Safe zone (keep text, logo, price and CTA inside) |
|---|---|---|---|
| 1:1 | `1x1` | 1080 x 1080 | The master's own margins. No platform overlay assumed. |
| 9:16 | `9x16` | 1080 x 1920 | Top 250 px and bottom 340 px kept clear for Stories UI; Reels UI reaches higher, so also keep key text out of the bottom 35 percent. [VERIFY: confirm both zones against Meta's current Stories and Reels safe zone guide] |

Whichever size the master is, build the rows it is not. A master at a size not in the table: stop and ask.

```
NON-NEGOTIABLE RULES
1. Facts (price, days, places, dates) come only from tours.json via the tour id.
   Never invent a fact, a quote or a URL.
2. Check price_basis for the tour. If it holds [VERIFY], the ad must not say
   "per person". List it as an open item for Sameer.
3. Every photo shows that tour's activity. Never reuse one tour's photo for a
   different activity. No matching photo: stop and ask. Never pick one at random.
4. Never use generate_image for tour scenes. Real tour photos only.
5. Logo, badges and CTA are library component instances with brand variables.
   Never draw a copy by hand, never hardcode a brand colour.
6. Load figma-use and figma-generate-design before the first use_figma call,
   and name both in skillNames on every mutating call.
7. Work on a duplicate file or a draft first. Write only inside the staging frame.
8. No em or en dashes, no emojis, British English in all copy.
```

## Before you start

- [ ] The Figma link to the staging frame (file key and node id). Branch links use the branch key.
- [ ] The tour id for each tour in this run. Unknown id: run the `--tour` command below and give the user the list it prints.
- [ ] The approved copy per tour (headline, subline, CTA wording), or a brief to draft it from.
- [ ] The image mode per tour: (a) the photo is already in the master, or (b) pick from the Figma image library (its page or frame link).
- [ ] Seat and plan: writing outside drafts needs a Full seat on a paid Figma plan. Check with `whoami`.
- [ ] Brand fonts are uploaded to the Figma team or organisation. Fonts only on a laptop are not available.
- [ ] Canvas writes are in beta. Figma says output may need cleanup, and the feature will become usage-based paid.
- [ ] A duplicate of the file, or a draft, to test on first.

## Steps

### 1. Facts and copy

1. For each tour run `python3 -I ROOT/.claude/skills/scriptcraft/scripts/script_check.py --tour <tour id>`. Do not read tours.json whole. If the command is missing (the copy-skills plugin installed alone), ask the user for the path to `tours.json`.
2. Read `ROOT/.claude/product-marketing.md`, including the do-not-claim list.
3. Write a copy table: tour id, variant, headline, subline, price line, dates, CTA, and the source of each fact. Use `price_qualifier` as written ("from", "per adult"). Apply rule 2.
4. Run the `fact-check` skill on the table. Show it to the user and wait for approval before any write to Figma.

### 2. Activity per tour

Find the activity tags each tour allows. [references/activity-and-images.md](references/activity-and-images.md) has the mapping and the photo naming convention.

- Multi-day tours: the `kind` values in `itinerary`, without `travel` (ski, snowshoe, aurora).
- Day tours (no itinerary): the activity in the tour `name`.
- The lead photo matches the activity the headline talks about. Unclear: ask.

### 3. Open the file (official MCP order)

1. `create_session` with the file key and a one-line task. Pass its `sessionId` on every later file call.
2. `get_libraries`, then `search_design_system` (one intent per query) for the logo, badges, CTA button, colour, spacing and text styles. Search before building anything.
3. A read-only `use_figma` call on the staging frame: return the master's id, size, children, layer names, text nodes with their fonts, image fills (hash, scale mode, transform) and every instance with its main component key. Return ids; take no screenshot yet.
4. Decide which rows of the Sizes table are missing.

### 4. Photos

- Mode (a): keep the master's image fill (same `imageHash`). Only the crop changes per size.
- Mode (b): a read-only `use_figma` on the library page lists image layers with their own and parent frame names. Keep only names whose tokens match the tour's activity tag. Show the shortlist to the user. No match: stop and ask.
- Copy the chosen `imageHash` into the new frames. Use `upload_assets` only for a photo the user supplies as a file.

### 5. Build each size

For each tour, variant and missing ratio, in one retry-safe `use_figma` call per tour where possible:

1. Clone the master into the staging frame, placed next to it, and name it `<tour-id>_<variant>_<ratio>` (for example `ski-6day_a_9x16`). Resize the clone to the row's pixels.
2. Re-adapt, do not scale. [references/adapting-sizes.md](references/adapting-sizes.md) has the rules: photo crop and focal point, bleed, type sizes, line breaks, text placement, safe zones and components.
3. Text: load every font a text node uses (`getStyledTextSegments(['fontName'])`), await, then set the approved copy. Component text goes through `setProperties()`. Never guess a font style name.
4. Return all created and changed node ids, each frame's bounds, and any text node whose height grew.

Also build the master ratio for any tour other than the master's own tour, with that tour's copy and photo.

### 6. Check, export, hand over

1. `get_screenshot` of each new frame (one composition shot, one more only after a fix). Run the self-check below. Fix with a targeted `use_figma` call.
2. `download_assets` on each finished frame (PNG, the frame's export settings or 1x). The links expire, so save the files at once to `exports/figma-ads/<campaign>/<frame name>.png` in the current folder (`.gitignore` keeps `exports/` out of git) or to the shared drive the user names.
3. Report: frame names and node ids, the PNG paths, the open items and the designer review list.

## Self-check (per frame)

- [ ] Frame name follows `<tour-id>_<variant>_<ratio>` and the size matches the Sizes table.
- [ ] No text is clipped, overflowing or overlapping; no orphan word on its own line in the headline.
- [ ] Nothing important sits in a 9:16 safe zone: text, logo, price, dates, CTA.
- [ ] The subject (skier, snowshoer, guide) is fully in frame and not under text.
- [ ] The photo shows this tour's activity, and no photo is shared across activities.
- [ ] Every fact matches the `--tour` output; no "per person" while price_basis holds [VERIFY].
- [ ] Logo, badges and CTA are library instances; colours and spacing are bound to variables.
- [ ] The fonts on screen are the brand fonts, not a fallback.
- [ ] No leftover placeholder text and no shimmer placeholders.

## For the designer to review

Always list, per frame: the crop and focal point, type fit and line breaks, safe zone placement on 9:16, any text you shortened to fit, any component you could not find in the library, and every [VERIFY] item. Uploading to Meta stays manual.
