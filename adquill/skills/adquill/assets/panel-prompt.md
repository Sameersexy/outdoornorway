# Panel prompt

How to run the three reviewer agents in parallel and merge their verdicts into one. Read it when the user runs the panel command, or when you want a fresh pair of eyes on a draft set before it goes out.

The three reviewers live in agents/ at the repo root:

| Agent | Judges | Wins conflicts about |
|---|---|---|
| direct-response-chief | offer clarity, specificity, objections, CTA, message match, policy risk, testability | facts and policy |
| editorial-director | clarity, voice, rhythm, factual precision, honesty of claims, AI tells | language |
| creative-director | the idea, thumb-stop, distinctiveness, picture and words, platform fit, shareability, range | concept |

All three are read-only. They return a verdict (ship, revise or reject; the agents print these in capitals), an overall score out of 10, a table of dimension scores, numbered blocking issues with exact quotes, and non-blocking suggestions. A ship verdict from them needs a score of 8 or higher and zero blocking issues.

## Why a panel

One author reads their own draft the way they meant it. A reviewer who sees only the draft and the brief reads it the way a stranger will. Three reviewers with different jobs catch different defects: a wrong number, a limp sentence, an idea nobody would remember. The panel is three personas run by the same underlying tool. It catches defects. It does not replace a real test with real spend.

## Step 1. Build the packet

Every reviewer gets the same packet, and nothing else:

1. The brief (assets/brief-template.md, filled).
2. The fact ledger.
3. The drafts exactly as they will be pasted, with slot names and character counts.
4. The linter output for each slot.
5. The policy and fact pass from step 7 of the method.
6. The platform and placement.

Do not include your own opinion of the drafts. Do not say what verdict you hope for. Do not include another reviewer's output in round one, because independence is the point.

## Step 2. Run the three in parallel

In Claude Code, start the three agents in the same step so they run at the same time. In a plugin install they may appear with the plugin prefix (for example adquill:editorial-director). Give all three the same instruction:

```text
Review the attached packet as yourself. Read the brief and the fact ledger first.
Then check every number, date, name and promise in the drafts against the ledger.
Judge the drafts for this platform and placement. Quote exact words for every issue.
Say what is weak and what direction to take, but do not rewrite the ad for me.
Return your normal output format, with a verdict, an overall score, dimension scores,
numbered blocking issues, and non-blocking suggestions. Be honest and specific.
Packet:
<brief>
<ledger>
<drafts with counts>
<lint output>
<policy and fact pass>
```

If the host cannot run subagents (some agents that read this skill cannot), do the three reviews yourself one after another, in this order: direct-response-chief, editorial-director, creative-director. Read each persona file in agents/ before its pass, and clear your view of the previous pass by working only from the packet. Say in the report that the reviews were sequential and less independent.

## Step 3. Merge

Do the merge in this order.

Verdict table. One row per reviewer: verdict, overall score, number of blocking issues. Do not average the scores. Averages hide a failing dimension.

Blocking issues, deduplicated. Two issues are the same when they name the same location and the same defect. Keep one row. List which reviewers raised it. Keep the strictest fix that still respects the ledger. Sort the list with facts and policy first, then language, then concept.

Conflict rule. When reviewers disagree, decide by domain.

- Facts and policy: the direct-response reviewer wins. If it says a number is unsupported or a claim is a policy risk, the line changes, whatever the others think of the rhythm or the idea.
- Language: the editorial reviewer wins. If it says a sentence reads as a machine, the sentence changes, as long as the fact inside it stays.
- Concept: the creative reviewer wins. If it says two variants are one idea, they are merged or one is replaced, as long as the replacement uses only ledger facts.

Examples. Editorial wants to cut "NOK 4,900" from the primary text for rhythm, and direct-response wants it kept for message match: the price stays, and the sentence is rebuilt around it. Creative wants a punchier claim the ledger does not support: the claim goes, and creative gets one more try with a ledger fact. Direct-response wants a longer line that sounds like a brochure: editorial rewrites it, and the fact stays.

Merged verdict. Ship only when all three ship and no blocking issue is open. Revise when any reviewer says revise, or any blocking issue is open. Reject when a reviewer rejects within its own domain. A reject outside a reviewer's domain counts as revise, with a note.

## Step 4. Revise, once

1. Apply the blocking fixes in the order listed.
2. Re-run the linter on every changed slot.
3. Re-run the panel on the changed variants only. This is round two, and the last.
4. If blocking issues remain after round two, stop. Show the user the open issues and the disagreement, and let them decide. More rounds circle the same limits.

Never edit the ledger to make an issue go away. If a reviewer asks for a fact the ledger does not have, ask the user.

## Merged report shape

```text
# Panel report: <offer>
Round: <1 or 2>
Reviews: <parallel | sequential>
Merged verdict: <ship | revise | reject>

| Reviewer | Verdict | Overall | Blocking issues |
|---|---|---|---|
| direct-response-chief | | /10 | n |
| editorial-director | | /10 | n |
| creative-director | | /10 | n |

## Blocking issues (deduplicated, facts and policy first)
1. [variant, slot] "exact quote"
   Raised by: <reviewers>
   Defect: <one line>
   Fix direction: <one line>
   Decided by: <domain rule>

## Disagreements and how they were settled
<each conflict, the rule applied, the outcome>

## Lines to protect
<quotes the reviewers asked to keep>

## Non-blocking suggestions
<grouped by reviewer>

## What changed after round 1
<edits made, lint scores before and after>

## What the panel cannot tell you
It reads the draft. It has no sales data and has seen no real audience. Test the
variants with real spend before you call any of them a winner.
```

## Rules

- Reviewers stay read-only. Edits happen in your own pass, never inside a reviewer.
- Reviewers never see each other's output in round one.
- Quote reviewers accurately in the merged report. Do not soften a verdict.
- Never show reviewer praise to customers as proof. A panel verdict is no testimonial.
- The merged report is for the user. It does not go into the ad.

Sources

- The fresh reader idea (step away, then reread): https://briefercopy.com/blog/david-abbott/
- Reviewer personas and output formats: agents/direct-response-chief.md, agents/editorial-director.md, agents/creative-director.md
