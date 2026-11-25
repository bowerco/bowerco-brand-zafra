# Reel templates

Two reel types with two different jobs. Alternate them so the feed is never all product or all mood.
All reels: 1080x1920, 30 fps, held frames only (the frame never moves while a shot plays), rendered with `tools/zafra_render.py`. No full-frame phone clips: every shot is a held crop of the source (use the master in `assets/*/masters/` for tight crops).

| Code | Name | Reference | Purpose | Length |
|---|---|---|---|---|
| R1 | **Product reel** | Erewhon | Make people want the drink: bottle, ingredients, liquid, up close | 7 to 11 s |
| R2 | **World reel** | Jacquemus | Create the world of Zafra: places, light, mood | 6 to 12 s |

---

## R1 Product reel

**Front matter:** `format: product reel`, `template: R1 Product reel`.

### Structure
| Part | Shots | Each | What |
|---|---|---|---|
| Fast cuts | 6 to 10 | about 0.6 s (0.5 to 1 s) | Alternate the three shot types below, never two of the same type in a row |
| Hero | 1 | 2 to 4 s | The bottle upright and centred on a plain field (coral, red or cream), label big and readable |

### Shot types
| Type | Zafra version |
|---|---|
| **Ingredient** | Saffron: a pinch of threads, threads falling, colour bleeding into water. Lemon: whole, halved, a slice in light. Rose water: drops falling, a small glass bottle, a ripple in a dish (petals only as a prop beside it). |
| **Bottle, extreme close** | The zafra script on the label (so tight it's almost abstract), the flower, the red cap and its script, "NATURALLY UPLIFTING", condensation. |
| **Liquid** | The saffron glow through glass, bubbles rising, ice, the pour. |

### Look
- Plain seamless background, one colour family per reel, soft even light, macro.
- Movement comes from the subject: a drip, bubbles, the pour, a thread falling.
- **No text on screen and no logo overlay.** The label is the branding. (`./check` fails an R1 with on-screen lines.)

### Draft layout
```
## Shots
1. (0.6 s) Ingredient: ... (asset id, crop)
2. (0.6 s) Bottle: ...
...
9. (3 s) Hero: ...

## Caption
...
```

---

## R2 World reel

**Front matter:** `format: world reel`, `template: R2 World reel`.

### Structure
| Part | Detail |
|---|---|
| Shot | **One** held shot, no cuts |
| Length | 6 to 12 s |
| Movement | From the scene only: a wave, wind in sand, camels walking, water light, people passing |
| Logo | Only when the bottle is **not** in frame: cream logo file (`zafra-logo-cream.svg`), always dead centre of the frame (Emi, 2026-11-25: even when it crosses the subject), about half the frame width (440 to 540 px), on for the whole clip. When the bottle is in frame, the label is the logo: no overlay (two wordmarks stacked look wrong, tested 2026-11-24). |
| Text | None besides the logo |
| Camera check | Contact-sheet the clip (1 frame a second) before choosing it. If the horizon or subject shifts between frames, it isn't held. |

### Places
Beach, desert, city, saffron fields, pool. Clean and slightly abstract. The bottle can appear but often doesn't; when it does, the label is big and readable and the movement is right next to it.

### Seasons
Beach season and pool from spring to autumn; desert, dunes and heritage around Ramadan and Eid; saffron fields for the harvest story.

### Draft layout
```
## Shot
(9 s) zaf-video-045 master, crop w:h:x:y, sun path on the sea, waves breaking. Cream logo centred, 480 px.

## Caption
...
```

---

## Captions (both)
Hook under 8 words, 1 to 3 short lines, the CTA line, up to 3 hashtags with `#Zafra` first. Alt text describing the shot.

## Before you render
1. Pick the source from `assets/video-clips.yaml` (`postcard: true` for R2) and check `times_used`.
2. Find the crop in `assets/reuse-ideas.md` or make a new one. Same output ratio, at least 800 px wide in the source.
3. Copy the closest recipe in `tools/recipes/` and render. `--log` records the asset use.
4. Look at the render: is the label readable, is the frame still, does it hold up on a phone?
