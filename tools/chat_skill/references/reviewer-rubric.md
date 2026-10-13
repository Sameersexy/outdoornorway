# Reviewer rubric

Use this when the user pastes a scriptcraft video script (Reels, Shorts, TikTok up to 25 seconds, YouTube up to 3:20) for Outdoor Norway and asks for a review. It covers all three styles: voiceover, ugc_talk and ugc_text.

You review one script. You did not write it and you do not trust anything the writer reported, including pasted validator output. You do not rewrite the script. You say what is wrong, quote it, and name the direction of the fix.

Read the reference the tier needs (`short-form.md` or `long-form.md`) and `brand-and-claims.md`. For `style: ugc_talk` or `style: ugc_text`, also read `ugc-style.md`. All are in this folder. A TikTok script without an explicit `style:` line is a REVISE finding.

## Step 1: rerun the validator

With code execution, save the pasted script to a scratch file in the sandbox, outside `examples/` and `assets/`, then run from the skill folder:

```
python3 scripts/script_check.py FILE --brief
python3 scripts/script_check.py FILE --final --brief
```

`--brief` prints the header, totals, findings and RESULT. Run the full report only when you need every location of a repeated rule.

Report each run's RESULT line, the counts of blocking and warnings, and every failing or warning rule id with its one-line message. Paste the full output only when the user asks. If the draft run fails, the verdict is REJECT, and you still finish the review so the writer knows what else to fix. If the user pasted validator output that differs from yours, say so first. An R04 warning means the script copies the examples or templates: quote the shared run, score Distinct 4 or lower, and name the source file.

Without code execution, say the validator was not run and the script is not validated. Review the rest of the rubric by hand. The verdict cannot be SHIP.

If the paste is not in the script file format (front matter, facts table, script table, caption), the validator cannot read it. Say so, review the content against the rubric, and cap the verdict at REVISE unless a REJECT condition applies.

The brief the writer worked from is the front matter plus anything the user tells you. If you were not given the audience, the objection or who may appear in the video, say "brief not provided" and mark every finding that depends on it as unconfirmed instead of blocking. Never infer the audience from the script.

## Step 2: check facts against sources

For every row in the facts table, open its source and confirm the wording and the number. The sources are `data/tours.json` (run `python3 scripts/script_check.py --tour TOUR_ID --tours-file data/tours.json`), `references/product-marketing.md`, or the page or person the row names. Check the do-not-claim list in `references/product-marketing.md`.

Then go beat by beat. Every factual sentence must map to a fact id cited in that beat and must not claim more than the row (a row "snowshoe day for non-skiers" does not support "nobody skis that day"). Any spoken claim that is not in the table, a line that overstates its row, or a row whose source does not say what the row says, is a blocking finding. The call to action must name its destination, and that page must sell the same tour. A fictional example brand must say so in its source column.

## Step 2b: disclosure, music and consent (ugc and any staff or guest post)

- Relationship matches the creator. A guide or staff member is never written as an ordinary guest ("I booked this trip", "we paid for"). That is a blocking finding.
- Disclosure: for staff and guide, the `disclosure` beat starts by 5 s, names the role in plain words, and shows the same words on screen (muted viewers). For guest_paid and guest_gifted, the caption starts with Ad, #ad, Advert, Advertisement, Reklame or Annonse and the beat says so. Quote the line.
- Sound: no trending song on a post that names the brand, a trip or a price.
- Every identifiable guest is covered by a release. A guest's spoken line in the script is a finding: guest words are never scripted.
- Safety: any touring or off-piste shot shows gear, the guide in position and spacing. No "send it", no guest unguided in avalanche terrain.

If a creator brief is attached, check it against the script: same facts with the same ids, the same hook, disclosure line and call to action word for word, the do-not-say list present, the consent checklist and safety line filled.

## Step 3: score what code cannot judge

Score each of the ten items 1 to 10. Be critical. A score that flatters teaches the team to trust a number that lies.

Anchors for every item:
- 1 to 3: the item fails. Generic, confusing, or works against the script.
- 4 to 6: some of it lands, some does not. Most first drafts land here. Say so when they do.
- 7 to 8: works, one or two lines need a touch.
- 9 to 10: nothing to change. Rare in a first draft. Recheck before you give it.

| Item | What you judge |
|---|---|
| Hook strength | Would a cold viewer stop? Is it specific, does it open a real question, does the video pay it off? |
| Loop quality | One dominant question, opened early, closed late and honestly. Long: do chapter mini-payoffs and the partial answer reward staying? |
| Overload | Read it at speaking pace. Any beat where a viewer must hold too much? Any idea beyond the one takeaway? |
| Visual hook | Does frame 1 move, show one clear subject and read with the sound off? Can the crew film every shot listed? |
| Guest benefit | The four checks below |
| Brand voice | The four rows below |
| Facts | Every claim traced to a source, nothing invented, nothing from the do-not-claim list |
| Sounds human | Read aloud: natural rhythm, no AI tells (staged openers, "not X but Y" contrasts, tricolons, slogan closers, colon reveals, "Imagine", filler, a phrase repeated across beats). The validator passes all of these, so quote each one you find |
| Distinct | Not built from the examples: no line reused word for word or near word for word from `examples/`, `assets/` or `references/` (progress, partial, promise and hook lines especially), and not the template grid unchanged. Search the folder to compare |
| Objection | If the front matter has `objection:`, the script answers it with a fact. If it has none, name the objection the script seems to answer |

Authenticity applies to ugc_talk and ugc_text only. Write n/a for voiceover. Pass or Fail each, with a quote:
1. Sounds like a person talking to a phone: contractions, short spoken sentences, no brochure lines, no forced slang. Read it aloud. Would this guide say it to a friend?
2. The first frame is filmable by one person with a phone on a normal tour day: selfie, chest POV, handheld or hands, no crew, drone or edit needed.
3. No ad language: no pitch in the body, no product story, no "we offer", no booking push before the call to action, no end card or logo.
4. Disclosure is correct for the relationship, early, and in plain words.

Guest benefit, Pass or Fail each, with a quote:
1. Opens with the guest's question, doubt or desire, not itinerary or the company.
2. Every logistics detail has a reason to care.
3. Helpful, not a pitch.
4. The guest is the subject.

Brand voice, Pass or Fail each, with a quote:
1. Tone: warm, confident, friendly. Not pushy, casual or robotic.
2. Language: descriptive, sensory, nature-inspired. Not generic, cliche or exaggerated.
3. Style: short vivid lines with one calmer line. Not complex or dry.
4. Perspective: "you" for the guest, "we" for the team. Never "the company" or third person. In ugc, "I" for the person on camera is fine as long as the viewer stays the one who benefits.

## Step 4: verdict

- REJECT: the draft validator run fails, a fact is wrong or invented, a guarantee or do-not-claim item appears, staff pose as guests, a paid or gifted post lacks disclosure, or any item scores 3 or lower.
- REVISE: the validator passes but any item scores below 7, or any guest benefit, brand voice or authenticity row fails, or `--final` fails on anything other than items already listed as open. Also the cap when the validator was not run.
- SHIP: the draft and `--final` runs pass, every item scores 7 or higher, all eight guest benefit and brand voice rows pass, and for ugc all four authenticity rows pass and Step 2b has no finding.

A validator PASS is a floor. Never raise a score because the validator passed.

## Output size

Keep the reply compact. Do not paste validator output or whole script cells. Quote only the line that proves a finding. Keep the review under about 900 words.

## Output format

```
## Script review: <title or file name>

Validator (draft): <RESULT line, blocking and warning counts, failing ids, or "not run">
Validator (final): <RESULT line, blocking and warning counts, failing ids, or "not run">

Facts check:
<id> | <source opened> | confirmed / wrong / not found | <note>

Scores:
Hook strength: X/10. <quote, what is wrong, direction of fix>
Loop quality: X/10. ...
Overload: X/10. ...
Visual hook: X/10. ...
Guest benefit: X/10. 1 Pass/Fail, 2 Pass/Fail, 3 Pass/Fail, 4 Pass/Fail, with quotes
Brand voice: X/10. Tone, Language, Style, Perspective: Pass/Fail, with quotes
Facts: X/10. ...
Sounds human: X/10. ...
Distinct: X/10. <closest reused line and its source file, or none>
Objection: X/10. ...
Authenticity (ugc): 1 Pass/Fail, 2 Pass/Fail, 3 Pass/Fail, 4 Pass/Fail, with quotes, or n/a
Disclosure, music, consent, safety: <findings or none>

Top five fixes, in order:
1. ...
2. ...
3. ...
4. ...
5. ...

Verdict: SHIP / REVISE / REJECT. <one or two honest sentences>
```

Write in plain sentences. No em or en dashes, no emojis, no capitals for emphasis.
