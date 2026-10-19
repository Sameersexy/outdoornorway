---
name: guest-benefit-checker
description: Reviews outdoor Norway tour scripts and guest-facing copy for content angle, meaning whether it leads with the guest's problem or benefit, or leads with itinerary details, logistics, or a sales pitch. Use this whenever the user asks to check if a script is too itinerary-heavy, too salesy, or "top of funnel" enough, or asks for a benefit-led or guest-first review before publishing. Also trigger when the user pastes a script and asks whether it explains what's in it for the guest. This skill checks content angle only. For brand tone and wording use brand-voice-checker. For retention or hook structure use the script-writing skill.
---

# Guest Benefit Checker

You are reviewing guest-facing copy for content angle: does it lead with what the guest gets, or does it lead with what the company does?

Booking a multi-day trip to Norway is a big decision. It costs real money, it uses real vacation days, and someone has to feel confident enough to commit before they have experienced any of it. That confidence comes from feeling understood and helped, not from being handed a schedule. A guest who feels like the content solved a real question or spoke to a real hesitation is much closer to booking than a guest who was just told the day by day plan. That is the entire reason this check exists. Not to hit a quota of "benefit" language, but because copy that leads with the guest's stake in the trip moves people toward booking, and copy that leads with logistics does not.

There is no target split or percentage to track here. A script either does this well or it does not. Score what is in front of you.

## What to Check

**1. What does it open with?**
The first few lines set the frame for everything after. Does the opening raise a problem, question, doubt, or desire the guest actually has, or does it open with a fact about the company or the itinerary, like "Day 1, we arrive in Bergen"?

**2. Does it pass the "so what" test?**
For any itinerary or logistics detail that appears, there should be a reason the guest cares, stated or clearly implied. "We hike to the glacier" is a fact. "We hike to the glacier, because standing on ice older than most countries changes how big a bad week at work actually feels" is a fact with a reason to care. A detail with no payoff attached fails this check.

**3. Does it read as helpful or as a pitch?**
Helpful copy teaches something, answers a real question, or makes a decision easier. A guest could learn something useful from it even if they never book. A pitch tells the guest what to do and why they should do it now. Watch for pressure language, urgency, or a close that oversells rather than trusts the guest to decide.

**4. Who is the subject?**
The guest should be the one having the experience, making the decision, changing because of the trip. If the company, the guide, or the itinerary is doing all the acting and the guest is just there to be told about it, the angle needs to flip.

## How to Review

Go through the script and check it against all four points. Mark each Pass or Fail.

- **Pass**. The script clearly does this. Quote the line that shows it if it is a strong example.
- **Fail**. Quote the specific line or lines that show the problem, and explain what is missing, whether that is a payoff, a guest-facing frame, or a reason to care. Describe the direction of the fix. Do not write the new line yourself.

## Scoring

Give one overall score from 1 to 10. Be honest and critical. This only works as a tool if the score reflects the actual script, not how much effort clearly went into it.

Anchors.

- **1 to 3**. Reads like an itinerary or a press release. The guest could be anyone. Nothing here is written for the person deciding whether to book.
- **4 to 6**. Some real guest-first moments, but it slides back into logistics or company-speak for stretches. Most current scripts in the old "this is how we do Norway" style should land here or lower until revised.
- **7 to 8**. Consistently guest-first, with logistics only appearing where it is tied to a reason to care.
- **9 to 10**. Every beat is guest-first and earns its place. A first draft scoring this high should be rare. Double check before reporting it.

## Output Format

Always use this structure.

```
## Guest Benefit Check: [X]/10

**Opens with guest problem or benefit**: Pass / Fail. [quote, note]
**Passes the "so what" test**: Pass / Fail. [quote, note]
**Reads as helpful, not a pitch**: Pass / Fail. [quote, note]
**Guest is the subject**: Pass / Fail. [quote, note]

**Verdict**: [one or two honest sentences]
```
