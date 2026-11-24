# Carousel template

**Purpose:** carousels bring both reel worlds together: the beauty of the world reel, the product focus of the product reel, plus the information. Each carousel tells one short story, mixing photo and video. Reference: Rhode (structure and text system only).

**Front matter:** `format: carousel`, `template: C1 Carousel` and `recipe:` (one of the recipes below).
**Size:** 1080x1350 (4:5), 4 to 6 slides, at least one video slide. Video slides are held frames: a still camera with movement from the subject, 2 to 20 s.

## Slide kit

Every carousel is built from these slide types.

| Slide | What it shows | Media | Text |
|---|---|---|---|
| **Cover** | The bottle in a hand or in a scene, or a strong colour field | Photo (or a short loop) | Title, up to 6 words |
| **Lifestyle moment** | A held crop of a beach, desert, city or saffron-field clip | Video, 3 to 10 s | Label + body |
| **Real person** | Someone drinking Zafra in a real place, camera fixed | Video, 5 to 20 s | Label + body, or none |
| **Colour field** | Macro of the saffron glow, bubbles, threads bleeding into water, desert ripples | Photo or a 2 to 3 s loop | Label + body |
| **Ritual loop** | Pour over ice, bubbles rising, a lemon being cut | Video, 2 to 3 s | Label + body |
| **Ingredient** | Saffron, lemon or rose water on a cream or coloured field | Photo | Label + body |
| **Product still** | The bottle or the four-pack, glossy, with space for text | Photo | Label + body |

## Text system

The same on every slide, so every carousel reads like a page of the same magazine.
- **Cover title:** one line, up to 6 words, Euclid Flex caps, in the empty space. Never on the label or a face.
- **Inside slides:** a small label (Euclid Flex caps, up to 6 words) and up to 35 words of body (Acumin, sentence case) in a column beside it.
- **Position:** bottom left by default. Move to wherever the empty space is (top left on a product still).
- Cream #FFF9DA or white only. One title size, one label size, one body size across the carousel.
- Every fact in body text comes from `brand/facts.md`, `brand/story.md` or `products/`.

## Recipes

| Recipe | Slides | Use for |
|---|---|---|
| **Story** | Cover, lifestyle moment, colour field, ritual loop (+ product still) | A moment or season: beach season, Ramadan, gifting |
| **Product feature** | Cover, product still, ritual loop, real person (+ colour field) | The bottle itself: how it looks, how to serve |
| **Explainer** | Cover, ingredient or colour field, lifestyle moment, product still (+ ritual loop) | Why saffron, the ingredients, history, heritage |
| **Where to buy** | Cover, product still, lifestyle moment, product still | Stockists by country, delivery apps |

## Topics

| Topic | Recipe | Example labels | Facts from |
|---|---|---|---|
| Why saffron? | Explainer | WHY SAFFRON? / THE THREAD / 36 MG / IN EVERY BOTTLE | facts.md (Saffron) |
| The ingredients | Explainer | WHAT'S INSIDE / SAFFRON / LEMON / ROSE WATER | products.yaml |
| The story of saffron | Explainer | THREE THREADS / BY HAND / ACROSS CENTURIES | facts.md (Meet saffron). Anything more: `_gaps.md` |
| Born in Dubai | Explainer | BORN IN DUBAI / PRODUCED IN ITALY / THE GULF TABLE | story.md, facts.md |
| Where to find us | Where to buy | IN THE UAE / IN OMAN / IN MINUTES | where-to-buy.yaml |
| How to serve | Product feature | CHILL. POUR. SIP. / OVER ICE / ON ITS OWN | facts.md |
| Naturally uplifting | Story | Only "naturally uplifting" until Zafra approves more | facts.md (Health claims) |
| Season notes | Story | ZAFRA NOTES: BEACH SEASON | audience.md (occasions) |

A recurring series name for seasonal story carousels: **ZAFRA NOTES** (proposal, Emi to confirm).

## Draft layout
```
## Slide 1 (cover, photo)
Visual: asset id, crop, what it shows.
Title: WHY SAFFRON?

## Slide 2 (colour field, video 3 s)
Visual: ...
Label: THE THREAD
Body: Just three threads grow in each bloom, harvested by hand.

...

## Caption
...
```
`./check` reads `Title:`, `Label:` and `Body:` lines, counts `## Slide N` headings and needs at least one heading marked `video`.

## Caption
Hook under 8 words, 1 to 3 short lines, the CTA line, up to 3 hashtags with `#Zafra` first. Alt text per slide.
