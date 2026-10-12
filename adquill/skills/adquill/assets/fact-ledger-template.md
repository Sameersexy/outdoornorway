# Fact ledger template

The table adquill builds at step 2 of the method, before it writes a word. Read it when you build a ledger or when you check a draft against one. Copy only gets to use rows where "verified" and "allowed in copy" are both yes.

## Columns

| Column | Meaning |
|---|---|
| fact | One claim, as a short noun phrase. "Price per person" |
| value | The exact value, as it would appear in copy. "NOK 4,900" |
| source | Where it came from: the user's brief, a landing page URL, a booking terms page, a calendar calculation |
| verified | yes or no. Yes means the user supplied it or a source shows it. No means asserted without a source |
| allowed in copy | yes or no. Yes only when verified is yes and the claim is safe to state |

## Rules

1. A fact the user states in the brief counts as verified yes, with source "brief". A fact the user hints at ("our guides really know their stuff") is not a fact. Turn it into a question.
2. Derived facts show their arithmetic in the value column. "8 Saturdays: 9, 16, 23, 30 Jan; 6, 13, 20, 27 Feb". Check weekdays with a calendar calculation.
3. Prices are checked against the landing page. If the brief and the page disagree, mark both rows verified no and ask.
4. Proof rows record what kind of proof it is: review (with link), count (with date), certificate (with number), policy (with page). Proof without a kind and a source is verified no.
5. Scarcity and urgency rows need a count or deadline and the date it was true. Without both, allowed in copy is no.
6. Unknown facts get a row with value [VERIFY: reason] and allowed in copy no. The copy never uses that row. Ask the user instead.
7. A fact can be true and still not allowed. Examples: a claim about a competitor, a health or age statement about the viewer, a promise about snow or weather.
8. Add a row when the copy needs a new fact. Never add it to the copy first.

## Blank ledger

| fact | value | source | verified | allowed in copy |
|---|---|---|---|---|
| offer | | | | |
| price per person | | | | |
| price basis (includes) | | | | |
| price basis (excludes) | | | | |
| dates | | | | |
| group size | | | | |
| level requirement | | | | |
| cancellation policy | | | | |
| weather or safety policy | | | | |
| landing page and its price | | | | |
| proof 1 (kind) | | | | |
| honest limit | | | | |

## Filled example (fictional brief)

This ledger belongs to the fictional brief in assets/brief-template.md. Brekke Ski Guides is invented. Prices and dates are made up.

| fact | value | source | verified | allowed in copy |
|---|---|---|---|---|
| offer | Intro to ski touring, one guided day | brief | yes | yes |
| price per person | NOK 4,900 | brief | yes | yes |
| landing page price | NOK 4,900 per person | brekkeskiguides.example/intro, as pasted by the user | yes | yes |
| price includes | guide, transceiver, probe and shovel loan, route planning | brief | yes | yes |
| price excludes | skis, skins, boots, lunch, travel | brief | yes | yes |
| gear hire | NOK 650 per person for skis, skins and boots | brief | yes | yes |
| where | Sunnmøre Alps, meeting at a car park above Brekke (fictional place in a real region) | brief | yes | yes |
| dates | Saturdays 9 Jan to 27 Feb 2027 | brief, weekday checked by calendar calculation | yes | yes |
| number of departures | 8 (9, 16, 23, 30 Jan; 6, 13, 20, 27 Feb) | derived from dates | yes | yes |
| booking closes | 18:00 on the Thursday before | brief | yes | yes |
| group size | six people per guide, at most | brief, booking terms | yes | yes |
| level requirement | must ski red runs with control | brief | yes | yes |
| what is taught | skins, kick turns, transceiver use | brief | yes | yes |
| typical day | meet 08:30, skins on 09:15, first descent about 11:40, back about 15:30 | brief, owner says conditions can shift it | yes | yes, with "typical" or "about" |
| cancellation | free up to 7 days before | brief | yes | yes |
| weather and safety refund | guide calls day off for avalanche risk, guest picks another Saturday or gets a full refund | brief | yes | yes |
| guide certification | owner says yes, no certificate number | brief | no | no |
| guest reviews | none supplied | brief | no | no |
| seats left | not supplied | none | no | no |
| superlative about the region | not supplied, unprovable | none | no | no |
| honest limit | not for people who have not skied before | brief | yes | yes |

What the ledger changes in the copy:

- The ads may say "six people per guide" and "full refund". They may not claim certified guides, praise from guests, a seat count or a superlative, because none of those has a row marked allowed.
- The typical day is allowed only with a softener ("typical", "about") because the owner said conditions can shift it.
- Every number in the draft ads (NOK 4,900, 9 Jan, 27 Feb, eight Saturdays, 08:30, 7 days) maps to a row above. A number with no row is a defect.

## Open questions list

Keep a short list under the ledger. Each item is a question for the user, not a guess.

```text
1. Guide certificate: which body, which number?
2. Do you have a guest review you may quote, with a link?
3. Is the 08:30 start fixed, or does it move with conditions?
```

Sources

- Fact-bank approach, a paragraph with no checkable detail gets revised: https://github.com/Anbeeld/WRITING.md
- Norwegian rule that marketing must not mislead: https://www.forbrukertilsynet.no/vi-jobber-med/prismarkedsforing/salg-og-bruk-av-forpriser
