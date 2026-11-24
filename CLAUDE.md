# Project instructions

- After finishing any task that changes files in this repo, commit and push the changes without being asked.
- No em dashes anywhere, including in chat replies to Emi.
- No emojis, ever (content and docs).

# Instructions for any AI working in this repo

You are making Instagram and TikTok content for Zafra, a sparkling saffron drink with lemon and rose water, sold in the UAE and Oman. This repo is the only source of truth.

## The system in one table

| Format | Reference | Purpose | Template |
|---|---|---|---|
| Product reel | Erewhon | Make people want the drink: bottle, ingredients, liquid, up close | `templates/reel.md` R1 |
| World reel | Jacquemus | Create the world of Zafra: places, light, mood | `templates/reel.md` R2 |
| Carousel | Rhode | Beauty plus information: why saffron, history, ingredients, heritage, where to buy | `templates/carousel.md` |
| Story set | Limousine stories | One message, one action: a retailer, where to buy, or a lifestyle moment | `templates/story.md` |
| Giveaway | Carousel rules | The only single post: beautiful first, then the information | `templates/giveaway.md` |

No other formats. No single posts except giveaways. No newsletter yet.

## Before writing anything
1. Read `brand/` in full: `story.md`, `facts.md`, `voice.md`, `writing-rules.md`, `audience.md`, `pillars.md`, `visual.md`.
2. Read the template for your format in `templates/`.
3. Read `products/` for every product fact, price and stockist you mention.
4. Check `calendar/` for the slot and `ideas/backlog.md` for the idea.
5. Check `_gaps.md`. If what you need is listed there, do not fill it. Leave a `TODO` and flag it.

## While writing
- English only.
- **Never state a fact that is not in this repo.** That covers ingredients, nutrition, prices, stockists, history, awards, quotes, people and dates.
- **No health or functional claims.** "Naturally uplifting" is the strongest benefit line. Saffron is always 36 mg. Pending claims ("world's first", "the only drink", "studies suggest") can't run.
- Served chilled or over ice, on its own. Never a cocktail, mixer or soda.
- Prices: only from `products/`, only if `valid_as_of` is under 30 days old.
- Copy should sell, in Zafra's quiet voice: no superlatives, no hype.
- References in `ideas/references.md` are reference only. Never copy a line, layout or visual.

## Visuals
- **Held frames only.** The frame never moves while a shot plays: no zoom, pan, tilt, push-in, handheld or Ken Burns, in camera or in the edit. Movement comes from the scene.
- **Zoom in and hold.** Never post a clip or photo at its full frame. Crop into the source (masters in `assets/*/masters/`), hold the crop, cut between held crops.
- **When the bottle is in frame, the label is big and readable** and the movement is right next to it.
- **One source, many pieces.** Start from `assets/reuse-ideas.md` and `assets/video-clips.yaml`; see `templates/repurpose.md`.
- **Render every piece with `tools/zafra_render.py`** from a JSON recipe. It applies the grade, the logo files, the type and the carousel text layout, and refuses full-frame and red-logo-on-photo renders.
- Logos only from `assets/logos/`: cream or yellow on imagery, never red on imagery, never on top of the label's own wordmark. Never type the wordmark in a font.
- **On-screen text is always cream (#FFF9DA) or white.** Titles and labels in Euclid Flex ALL CAPS, one size each. Body in Acumin (Euclid Flex Regular until the files arrive).
- The fonts in `assets/fonts/euclid-flex-TRIAL/` are a trial: drafts only. **Nothing set in them is posted or sent out** until the licensed files replace them.
- **Look at every render** at phone size before it goes to review.

## Assets
- Pick assets from `assets/index.yaml` only. Respect each asset's `usage_rule`. Anything marked "do not reuse" is out.
- **Log every asset used:** `used_in`, `times_used`, `last_used` (`tools/zafra_render.py --log` does this).
- If no suitable asset exists, write `ASSET NEEDED:` with a shot description and add it to `shoots/gaps.md`.

## After writing
- Save to `content/drafts/<format>-<slug>.md`, media in `content/drafts/media/<piece>/`. Front matter: id, title, pillar, format, template, date, source_idea, assets_used, status, version, rules_check (plus `duration_s` for reels, `recipe` for carousels, `set_type` for story sets).
- Run `./check` and fix every FAIL. BLOCKED means waiting on Zafra (for now: approved calls to action).
- Then do the human-judgement items in `checks/rules.md`. Record the result in `rules_check`.
- A draft with any FAIL stays in drafts. Only a human moves files to `content/approved/` (`checks/approvals.md`).
- Update `calendar/` and `ideas/backlog.md` status.

## Style for the user (Bower operator)
No em dashes in anything written. Copy should sell, not just inform. Keep it concise.
