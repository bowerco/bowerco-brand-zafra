# Story set template

**Purpose:** every story set has one message and one action. Reference: the Limousine story sets (one line per frame, the lines build into a sentence, one link sticker throughout).

**Front matter:** `format: story set`, `template: S1 Story set`, `set_type:` (retailer, where-to-find-us or lifestyle).
**Size:** 1080x1920, 3 to 5 frames (4 by default), 5 to 7 s each. Keep text and stickers inside the safe zone (250 px clear top and bottom).

## Every set
- One line per frame, up to 6 words, Euclid Flex caps, cream or white, same size and position on every frame.
- The lines build: read in order, they make one sentence or one thought.
- One link sticker, same spot on every frame, so people can act at any point (lifestyle sets may skip it).
- Images build too: a detail, closer, the bottle, then the payoff on the last frame.
- If a background is light where the line sits, add the render `scrim` (a soft dark fade from the top) rather than moving the line. Same scrim on every frame of the set.
- Logo file on the last frame only (cream or yellow on imagery).
- Backgrounds: held video crops or stills from `assets/index.yaml`. Never a full-frame phone clip.

## Set types

| Set | Purpose | Link sticker | Example lines |
|---|---|---|---|
| **Retailer push** | Send people to one retailer | That retailer (approved links only) | TOO HOT OUT? / KEEP IT CHILLED. / OVER ICE. / ON TALABAT. |
| **Where to find us** | Every place Zafra is sold, by country | Website, or a delivery app | IN THE UAE. / the retailers / IN OMAN. / the retailers |
| **Lifestyle** | Build the Zafra world, one place per set | Optional | One held crop per frame (beach, desert, city), logo on the last |

### Retailer push, frame by frame
1. **Detail:** condensation on the bottle, or a held crop of the sea.
2. **Closer:** the glow in the glass, ice.
3. **The bottle:** label big and readable.
4. **Payoff:** the bottle with the retailer's name in the line; the sticker does the work.

### Where to find us
Lists only stockists from `products/where-to-buy.yaml`. One country per two frames: the line, then the names set small in Acumin (the only frame type allowed more than 6 words; names do not count toward the limit when written as `Stockists:`).

## Draft layout
```
## Frame 1 (detail)
Visual: asset id, crop.
Line: TOO HOT OUT?
Sticker: link "CTA: TODO" -> approved link

## Frame 2 (closer)
...
```

## Rules
- Link stickers use approved CTA wording only (`brand/rules.yaml`). Until Zafra approves the list, write `link "CTA: TODO"` and the set stays BLOCKED.
- Prices only from `products/`, under 30 days old.
- Seasonal lines (beach season, Ramadan, Eid) follow `calendar/`.
