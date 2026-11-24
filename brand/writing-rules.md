# Writing rules

Hard rules for every caption, on-screen line and alt text. Tone lives in `brand/voice.md`. Banned words and limits are enforced by `./check` from `brand/rules.yaml`.

## Language
- English only.
- In sentences: **Zafra** (capital Z). In an all-caps line: ZAFRA. The logo is a lowercase script: it is artwork, never typed in a font.
- Flavour line as on the label: **Saffron, Rose Water & Lemon**.

## Claims
- Facts only from `brand/facts.md`, `brand/story.md` and `products/`. Anything else goes to `_gaps.md` as a question, never into copy.
- No health or functional claims. **"Naturally uplifting"** is the strongest benefit line.
- Saffron is always **36 mg**. Never 38.
- Pending until Zafra approves in writing: "world's first", "the only drink with real saffron", "Studies suggest...". `./check` blocks them.

## Serve
- Chilled, or over ice, on its own. Never mixed, never a cocktail or mocktail, no stemmed glassware.
- Never call it a soda, soft drink, energy drink or syrup.

## Style
- No em dashes. Use a comma, a full stop or a colon.
- No superlatives ("best", "finest", "high quality").
- No reductive colour words ("golden colour"): say "saffron glow".
- Max 1 exclamation mark per piece. No emoji.
- Never open two pieces in the same week with the same line.

## On-screen text, per format

| Format | Words on screen |
|---|---|
| Product reel | None. The label is the branding. |
| World reel | None. Logo file only. |
| Carousel | Cover: one title, up to 6 words. Inside slides: a label (up to 6 words, Euclid Flex caps) plus body (up to 35 words, Acumin, sentence case). |
| Story set | One line per frame, up to 6 words, the lines build into one sentence across the set. |
| Giveaway | Cover title up to 6 words, then labels and body as a carousel. |

All on-screen text is Soft Cream #FFF9DA or white. Headlines and labels in Euclid Flex ALL CAPS, one size per piece.

## Copy should sell
Every piece ends with one quiet call to action from `brand/rules.yaml` (`calls_to_action.approved`). Until Zafra approves the list, write `CTA: TODO` and the piece stays BLOCKED.

## Captions (reels, carousels, giveaways)
- Line 1: the hook, under 8 words, sensory.
- 1 to 3 short lines: the moment or the fact.
- The CTA line.
- Up to 3 hashtags, `#Zafra` first.
- Alt text on every image and video.

## People
- Everyone in the library is cleared (Emi, 2026-11-17). No names in copy.
- Modest, GCC-respectful styling.

## Prices
Format `AED 24.64`. Only from `products/`, only if `valid_as_of` is under 30 days old. Otherwise leave prices out.
