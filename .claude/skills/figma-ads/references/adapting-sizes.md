# Adapting a master ad to another size

This page is for the figma-ads skill. It lists what changes between sizes and how to do it with the Plugin API. Read the figma-use skill for the general rules (fonts, colours in the 0 to 1 range, returning node ids).

## Photo

- Keep the same `imageHash`. Change only how it fills the new frame.
- Find the subject first: in the master screenshot, note where the skier, snowshoer or guide is, as a share of width and height.
- Use scale mode `CROP` with an `imageTransform`, or `FILL` on a photo layer sized and placed so the subject lands in the visual centre of the area that is free of text. From square to tall, the crop gets narrower: move it sideways so the subject stays whole.
- Photos that should bleed to the edge in the master bleed in every size. Extend the photo layer to the new frame edges; never leave a gap or a stretched edge.
- Never stretch a photo. If the photo is too small for 1080 x 1920 without visible softness, list it for the designer.

## Type

- Start from the master's text styles. If the library has a size for the new ratio, use it; otherwise scale the headline by eye and stay within the brand ramp.
- 9:16 has more height and the same width, so the headline usually keeps its size and gains a line. 1:1 from 9:16 usually needs a shorter line or a smaller step in the ramp.
- Set wrapping text to `textAutoResize = 'HEIGHT'` with a fixed width. Rebreak lines so no headline line holds a single word, and keep a price and its qualifier on one line ("from NOK 28,896").
- Never shorten approved copy to fit without telling the user. List every shortened line.

## Placement

- Rebuild the layout for the ratio. On 9:16, stack headline, details and CTA inside the safe area, usually with the photo subject above or between them. On 1:1, keep the master's grid.
- Use auto layout for the text block and bind padding and gaps to spacing variables.
- Read the Sizes table in SKILL.md for the safe zones. Nothing that carries meaning goes in them.

## Components

- Logo, badges ("Small groups", "Certified guides") and the CTA button are instances of library components. Keep the instance from the clone, or import by key from `search_design_system`. Swap to the variant made for the size if the library has one.
- Bind fills and strokes to brand colour variables with `setBoundVariableForPaint`. A hardcoded hex value is a defect.
- If a component is missing from the library, leave the master's instance in place, do not draw a copy, and list it for the designer.

## Retry-safe build

- One `use_figma` call per tour builds all its missing sizes, unless a call fails. Return every created id, each frame's bounds, and each text node whose height changed.
- On an error, follow `safeToRetryWithoutCanvasRead`. If it is false, read the staging frame before writing again.
