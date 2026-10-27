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

## Photo frames

Owner decision (27 October 2026): photos are not renamed. The owner makes one frame per activity and drops photos into it.

- Name each frame after one activity tag, one word, for example `Ski`, `Snowshoe` or `Skitouring`. Case does not matter.
- Drop the photos straight into that frame. Their layer names are ignored.
- A photo that shows two activities goes in the frame of the one it shows most.

## How the skill matches

1. A photo belongs to the activity named by the frame it sits in. Ignore the photo's own layer name.
2. The frame name must equal the tag as a whole word. Substrings do not count, so a `Ski` frame does not match `skitouring`.
3. Pick by shape: for 9:16 prefer a photo taller than it is wide, for 1:1 any photo whose subject survives a square crop. Check with a screenshot.
4. No matching frame or no usable photo for a tour: stop and ask the user for a photo. Never fall back to another activity or to a random photo.
5. A photo already used for one tour may be reused for another tour only if both tours have its tag.
