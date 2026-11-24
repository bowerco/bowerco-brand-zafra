# bowerco-brand-zafra

Source of truth for **Zafra** (@drinkzafra), the sparkling saffron drink born in Dubai and produced in Italy, sold in the UAE and Oman. Every piece of content Bower makes for Zafra is built only from what is in this repo.

**Last updated:** 2026-11-24 · **Status:** v1.0, rebuilt from scratch on the brand-limousine structure, with the format system agreed with Emi (reels, carousels, story sets, giveaways). Waiting on Zafra: approved CTAs, licensed fonts, story facts (see `_gaps.md`).

## Channels
Instagram and TikTok. English only. No newsletter yet.

## How Zafra shows up

| Format | Reference | Purpose |
|---|---|---|
| Product reel | Erewhon | Make people want the drink: bottle, ingredients, liquid, up close |
| World reel | Jacquemus | Create the world of Zafra: places, light, mood |
| Carousel | Rhode | Beauty plus information |
| Story set | Limousine stories | One message, one action |
| Giveaway | Carousel rules | The only single post |

## How it's organised

| Folder | What's in it |
|---|---|
| `CLAUDE.md` | Rules for any AI working in this repo. Read first. |
| `ONBOARDING.md` | What's filled in and what's still missing. |
| `check` | Rule checker (Ruby, no install needed on a Mac). |
| `_gaps.md` | Open questions for Zafra. Nothing in here is to be guessed. |
| `brand/` | Story, facts, voice, writing rules, audience, pillars, visual rules, tokens, **`rules.yaml` (machine-checkable rules)** |
| `products/` | Products and where to buy, dated |
| `templates/` | Reels (product, world), carousel, story set, giveaway, repurpose |
| `assets/` | Logos, fonts, photos, videos (+ 4K and full-res masters), `index.yaml` usage log, clip notes, crop ideas |
| `shoots/` | Asset audit per format (`gaps.md`) and the next shoot brief |
| `tools/` | `zafra_render.py` render kit and recipes |
| `content/` | `drafts/` and `approved/`, one file per piece, with front matter |
| `checks/` | `rules.md` (run on every draft) and `approvals.md` |
| `calendar/` | Cadence and monthly calendars |
| `ideas/` | Backlog and references |
| `results/` | Instagram and TikTok performance, lessons |
| `geo/` | Factual summary and FAQ for AI tools and search |

## How to check content

```
./check              # all drafts and approved pieces
./check FILE.md      # one file
```

`./check` reads `brand/rules.yaml` (banned words and claims, saffron amount, em dashes, emoji, prices, links, CTAs, pillars, formats and their limits, camera moves, asset rules). It runs on GitHub on every push (`.github/workflows/check.yml`). Rules that need judgement are in `checks/rules.md`.

## How to render

```
python3 tools/zafra_render.py tools/recipes/<recipe>.json --log
```

## Data formats
Structured data in YAML, guidance in Markdown, design tokens in `brand/tokens.json`. Anything unknown is marked `TODO` and listed in `_gaps.md`.
