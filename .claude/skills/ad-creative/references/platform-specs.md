# Platform Specs Reference

Complete character limits, format requirements, and best practices for each ad platform.

---

## Google Ads

### Responsive Search Ads (RSAs)

| Element | Character Limit | Required | Notes |
|---------|----------------|----------|-------|
| Headline | 30 chars | 3 minimum, 15 max | Any 3 may be shown together |
| Description | 90 chars | 2 minimum, 4 max | Any 2 may be shown together |
| Display path 1 | 15 chars | Optional | Appears after domain in URL |
| Display path 2 | 15 chars | Optional | Appears after path 1 |
| Final URL | No limit | Required | Landing page URL |

**Combination rules:**
- Google selects up to 3 headlines and 2 descriptions to show
- Headlines appear separated by " | " or stacked
- Any headline can appear in any position unless pinned
- Pinning reduces Google's ability to optimize, use sparingly

**Pinning strategy:**
- Pin your brand name to position 1 if brand guidelines require it
- Pin your strongest CTA to position 2 or 3
- Leave most headlines unpinned for machine learning

**Headline mix recommendation (15 headlines):**
- 3-4 keyword-focused (match search intent)
- 3-4 benefit-focused (what they get)
- 2-3 social proof (numbers, awards, customers)
- 2-3 CTA-focused (action to take)
- 1-2 differentiators (why you over competitors)
- 1 brand name headline

**Description mix recommendation (4 descriptions):**
- 1 benefit + proof point
- 1 feature + outcome
- 1 social proof + CTA
- 1 urgency/offer + CTA (if applicable)

### Performance Max

| Element | Character Limit | Notes |
|---------|----------------|-------|
| Headline | 30 chars (5 required) | Short headlines for various placements |
| Long headline | 90 chars (5 required) | Used in display, video, discover |
| Description | 90 chars (1 required, 5 max) | Accompany various ad formats |
| Business name | 25 chars | Required |

### Display Ads

| Element | Character Limit |
|---------|----------------|
| Headline | 30 chars |
| Long headline | 90 chars |
| Description | 90 chars |
| Business name | 25 chars |

---

## Meta Ads (Facebook & Instagram)

Verified against Meta's Ads Guide and Ads Manager previews on 2026-10-06 (see the sources in the adquill research notes). Meta states these as recommendations, not hard caps. The only hard behaviour that matters is truncation.

### Single image / video / carousel

| Element | Facebook feed | Instagram feed | Notes |
|---------|---------------|----------------|-------|
| Primary text | About 125 chars visible on mobile before "See more" (Meta recommends 50 to 150) | 125 chars visible (starts after the account name) | Longer text is allowed. Put price, product and action inside the first 125 |
| Headline | 27 chars recommended | Field allows up to 40, but single-image Instagram feed ads reportedly do not show it | Check the Ads Manager preview. Do not put the only copy of the price in the headline |
| Description | 30 chars | Not shown | Often hidden on mobile feed. Never the only home for a fact |
| Image | 4:5, 1440 x 1800 (1080 x 1350 minimum in practice), JPG or PNG, 30 MB | Same | Official minimum is lower. Keep text off the outer 5 percent |
| Reels and Stories (9:16) | Keep 14 percent of the top, 35 percent of the bottom and 6 percent of each side free of text | Same | On 1080 x 1920 that is 269, 672 and 65 px |

Advantage+ creative can now rewrite text inside your image by default (reported from 27 July 2026). For a price-on-image ad, switch it off per ad.

**Best practices:**
- Front-load the hook, the product and the price in the first 125 chars of primary text
- One idea per ad. Variants must be different ideas, not rewordings
- Price and dates on the ad must match the landing page
- No scarcity or urgency claims unless they are true and provable

### Lead Ads (Instant Form)

| Element | Limit |
|---------|-------|
| Greeting headline | 60 chars |
| Greeting description | 360 chars |
| Privacy policy text | 200 chars |

---

## LinkedIn Ads

### Single Image Ad

| Element | Recommended | Maximum | Notes |
|---------|-------------|---------|-------|
| Intro text | 150 chars | 600 chars | Above the image; truncated after ~150 |
| Headline | 70 chars | 200 chars | Below the image |
| Description | 100 chars | 300 chars | Only shows on Audience Network |

### Carousel Ad

| Element | Limit |
|---------|-------|
| Intro text | 255 chars |
| Card headline | 45 chars |
| Card count | 2-10 cards |

### Message Ad (InMail)

| Element | Limit |
|---------|-------|
| Subject line | 60 chars |
| Message body | 1,500 chars |
| CTA button | 20 chars |

### Text Ad

| Element | Limit |
|---------|-------|
| Headline | 25 chars |
| Description | 75 chars |

**LinkedIn-specific guidelines:**
- Professional tone, but not boring
- Use job-specific language the audience recognizes
- Statistics and data points perform well
- Avoid consumer-style hype ("Amazing!" "Incredible!")
- First-person testimonials from peers resonate

---

## TikTok Ads

### In-Feed Ads

| Element | Recommended | Maximum | Notes |
|---------|-------------|---------|-------|
| Ad text | 80 chars | 100 chars | Above the video |
| Display name | N/A | 40 chars | Brand name |
| CTA button | Platform options | Predefined | Select from TikTok's options |

### Spark Ads (Boosted Organic)

| Element | Notes |
|---------|-------|
| Caption | Uses original post caption |
| CTA button | Added by advertiser |
| Display name | Original creator's handle |

**TikTok-specific guidelines:**
- Native content outperforms polished ads
- First 2 seconds determine if they watch
- Use trending sounds and formats
- Text overlay is essential (most watch with sound off)
- Vertical video only (9:16)

---

## Twitter/X Ads

### Promoted Tweets

| Element | Limit | Notes |
|---------|-------|-------|
| Tweet text | 280 chars | Full tweet with image/video |
| Card headline | 70 chars | Website card |
| Card description | 200 chars | Website card |

### Website Cards

| Element | Limit |
|---------|-------|
| Headline | 70 chars |
| Description | 200 chars |

**Twitter/X-specific guidelines:**
- Conversational, casual tone
- Short sentences work best
- One clear message per tweet
- Hashtags: 1-2 max (0 is often better for ads)
- Threads can work for consideration-stage content

---

## Character Counting Tips

- **Spaces count** as characters on all platforms
- **Emojis** count as 1-2 characters depending on platform
- **Special characters** (|, &, etc.) count as 1 character
- **URLs** in body text count against limits
- **Dynamic keyword insertion** (`{KeyWord:default}`) can exceed limits, set safe defaults
- Always verify in the platform's ad preview before launching

---

## Multi-Platform Creative Adaptation

When creating for multiple platforms simultaneously, start with the most restrictive format:

1. **Google Search headlines** (30 chars), forces the tightest messaging
2. **Expand to Meta headlines** (40 chars), add a word or two
3. **Expand to LinkedIn intro text** (150 chars), add context and proof
4. **Expand to Meta primary text** (125+ chars), full hook and value prop

This cascading approach ensures your core message works everywhere, then gets enriched for platforms that allow more space.
