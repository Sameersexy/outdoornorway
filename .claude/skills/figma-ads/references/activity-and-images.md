# Activity tags and the photo library

This page is for the figma-ads skill and the designers who keep the Figma image library. It says which photos a tour may use and how to name photos so the skill can find them.

## Activity tags per tour

The tags come from `campaigns/ski-meta-ads/tours.json`. Print one tour with `script_check.py --tour <tour id>`.

| Where the tag comes from | Tag | Notes |
|---|---|---|
| `itinerary` day with kind `ski` | `ski` | Resort skiing. |
| `itinerary` day with kind `snowshoe` | `snowshoe` | |
| `itinerary` day with kind `aurora` | `aurora` | Night sky scenes. Never promise an aurora sighting in the copy (see the do-not-claim list in `.claude/product-marketing.md`). |
| `itinerary` day with kind `travel` | none | Travel days are not an activity. Do not use a transfer or town photo as the lead image. |
| Day tour with no itinerary, name "Backcountry Ski Tour" | `skitouring` | [VERIFY: Sameer confirms that backcountry tours use a separate ski touring tag and not `ski`] |

A tour may have more than one tag (a ski and snowshoe tour has both). The lead photo matches the activity the headline names. A new activity in tours.json gets a new row here before the skill uses it.

## Naming convention for the image library

This is a proposed convention. Agree it with the designers before the first run, then change this page if they want something else.

- Put the photos on one page, for example `Photo library`, with one frame per activity named `photos/<tag>`, for example `photos/ski` and `photos/snowshoe`.
- Name each photo layer `<tag>_<place or subject>_<nn>`, lower case, words joined by hyphens. Examples: `ski_voss-resort_01`, `snowshoe_forest-group_02`.
- One tag per photo. A photo that shows two activities goes in the frame of the one it shows most.
- Add `_portrait` or `_square` at the end when a photo only works in one shape.

## How the skill matches

1. Split the layer name and its parent frame name on `/`, `_` and `-` into tokens.
2. A photo matches when one token equals the tag. Substrings do not count, so `ski` does not match `skitouring`.
3. Prefer a photo with `_portrait` for 9:16 and `_square` for 1:1 when both exist.
4. No match for a tour: stop and ask the user for a photo or a library link. Never fall back to another activity or to a random photo.
5. A photo already used for one tour may be reused for another tour only if both tours have its tag.
