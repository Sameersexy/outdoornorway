---
name: figma-email
description: Designs an Outdoor Norway marketing email in Figma first, from the existing Figma email components and brand variables, and after Sameer approves the Figma design, builds it as a HubSpot draft that reuses the matching HubSpot custom modules. Facts come from tours.json. Never sends or schedules. Uses the official Figma MCP server and the HubSpot connector (manage_marketing_email). Run it by name; it writes to Figma and HubSpot.
disable-model-invocation: true
---

# figma-email

Two phases with a gate between them. Phase 1 builds the email in Figma from library components. Sameer approves it. Phase 2 builds the same email in HubSpot from the custom modules that match those components, as a draft. No MJML, React Email, Maizzle or hand-written HTML email.

ROOT is `${CLAUDE_PLUGIN_ROOT}`. If that text does not start with a slash, ROOT is the current folder (a clone of the repo). Repo paths below (`.claude/`, `campaigns/`) are under ROOT.

```
NON-NEGOTIABLE RULES
1. Figma first. Nothing is built in HubSpot until Sameer approves the Figma
   design in this session, in his own words.
2. Build only from library components and brand variables. Never draw a copy of
   a component, never hardcode a brand colour.
3. In HubSpot, reuse the custom module mapped to each Figma component. Never
   invent a module name, and never swap a custom module for raw HTML.
4. Draft only. Never send, schedule, publish or set recipients.
5. Facts come only from tours.json and .claude/product-marketing.md. Never
   invent a fact, a quote or a URL. A price_basis with [VERIFY] means no
   "per person".
6. Load figma-use and figma-generate-design before the first use_figma call.
   Call HubSpot tool_guidance for manage_marketing_email before using it.
7. Every HubSpot write is shown to the user and confirmed first.
8. No em or en dashes, no emojis, British English.
```

## Before you start

- [ ] The Figma file link and the page or frame for email drafts. Work on a duplicate or a draft first.
- [ ] The tour ids and the goal of the email (one line from the user).
- [ ] Seat and plan: Figma writes outside drafts need a Full seat on a paid plan (`whoami`). Brand fonts uploaded to the Figma account. Canvas writes are beta.
- [ ] HubSpot access through the connector, and the brand, template, subscription type and from address the user wants (the tool lists them; ask, do not pick).
- [ ] The component to module mapping below is filled in. If not, fill it with the user first.
- [ ] Public image URLs, or time for someone to upload images to HubSpot File Manager.

## Component to module mapping

Fill this on first use, with the user, from the real names in Figma (`search_design_system`) and in HubSpot (the module paths that `GET_CONTENT` or `GET_TEMPLATE` shows). Add a row per component. Leave a cell as `[VERIFY]` until someone confirms it.

| Figma component | HubSpot custom module path | Fields to fill | Confirmed by |
|---|---|---|---|

## Phase 1: design in Figma

1. Facts: for each tour run `python3 -I ROOT/.claude/skills/scriptcraft/scripts/script_check.py --tour <tour id>`. Do not read tours.json whole. Read `ROOT/.claude/product-marketing.md` and its do-not-claim list.
2. Write the copy per section (subject, preview text, headline, body, CTA) with the source of each fact. Run the `fact-check` skill on it. Get the user's approval of the copy.
3. `create_session` with the file key and a one-line task. Pass its `sessionId` on every later file call.
4. `get_libraries`, then `search_design_system` (one intent per query) for each email component (for example hero, tour card, CTA, footer) and for colour, spacing and text styles.
5. A read-only `use_figma` call: inventory any existing email in the file (component keys, variables, text styles) and match its width and conventions.
6. Build: one wrapper frame named `email_<campaign>_<yyyy-mm-dd>`, then one instance per section in order. Load fonts before any text edit; set text through `setProperties()`. Photos: reuse library photos whose names match the tour's activity (the figma-ads naming convention), never `generate_image`. No match: ask.
7. `get_screenshot` of the wrapper. Run the Figma part of the self-check. Fix with a targeted call.
8. Show Sameer the screenshot and the frame link. Stop here until he approves. Record his words and the date in the report.

## Phase 2: build in HubSpot

1. Call `tool_guidance` with `manage_marketing_email`. Follow it where it differs from this page.
2. Images: `download_assets` on each image node (the export links expire, so save the files at once to `exports/figma-email/<campaign>/`). HubSpot image modules need a public URL, and the connector has no file upload. Ask the user to upload the files to HubSpot File Manager and paste the public URLs.
3. Create the draft. `LIST_TEMPLATES` and `LIST_SUBSCRIPTION_TYPES`, `LIST_FROM_ADDRESSES`, then ask the user for the template, brand and settings. Template and brand cannot change later. Prefer a template, or `CLONE` of an existing email, that already holds the mapped custom modules. `CREATE` (or `CLONE`), then `POLL_EMAIL_CREATION` if it is pending.
4. `GET_CONTENT`. Match each section to the Figma frame through the mapping table.
5. Arrange: with `EDIT_CONTENT`, keep, order and remove sections so they follow the Figma design, and resubmit the full layout with every id. Show the plan and get confirmation first.
6. Fill the custom modules. The connector schema read on 27 October 2026 says custom modules come back as `UnknownModule`, which can be kept, moved or removed but whose content cannot be changed through the tool. [VERIFY: check tool_guidance for a way to set custom module fields] If there is none, write a fill sheet (section, module, field, value, source) and hand it to the user to paste in the HubSpot editor. Do not rebuild a custom module from native modules to get around it.
7. `PREVIEW_CONTENT` (set `textOnly` to false for the HTML). Run the HubSpot part of the self-check.
8. Report and stop. Sending a test email, choosing recipients and scheduling stay with Sameer.

## Self-check

Figma
- [ ] Every section is a library instance; colours, spacing and type are bound to variables or styles.
- [ ] No clipped or overlapping text, no placeholder text, brand fonts on screen.
- [ ] Photos match each tour's activity.
- [ ] Every fact matches the `--tour` output and the do-not-claim list.

HubSpot
- [ ] The email is a draft. Nothing was sent, scheduled or given recipients.
- [ ] Section order matches the approved Figma frame, and each section is the mapped custom module.
- [ ] Subject, preview text and every fact match the approved copy.
- [ ] Every image URL is public and every link is a real page the client named or tours.json holds.
- [ ] The preview text and HTML show no leftover template copy.

## Report

Return: the Figma frame link and node id, Sameer's approval words and date, the HubSpot email name and id, the fill sheet path if one was written, the image file paths, and the open items with who confirms each.
