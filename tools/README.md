# Tools

| Script | What it does |
|---|---|
| `zafra_render.py` | The render kit. Turns a JSON recipe into a reel, story frame, carousel slide or giveaway slide: held crops, the Zafra grade, logo files, Euclid Flex type, and the carousel label and body layout. `--log` records the asset use in `assets/index.yaml`. |
| `recipes/` | Starting points. Copy the closest one, change `out`, the crop and the text. |

Needs: Python 3 with Pillow and PyYAML, ffmpeg, rsvg-convert.

```
python3 tools/zafra_render.py tools/recipes/r2-desert-camels.json --log
```

| Recipe | Format |
|---|---|
| `r2-beach-shoreline-tight.json` | World reel, the reference crop (label is the logo) |
| `r2-desert-camels.json` | World reel with the cream logo |
| `c-slide-editorial.json` | Carousel inside slide: label + body |

What it enforces:
- every segment is a held crop in the output ratio (no full-frame clips, no animated zoom); warning under 800 px source width
- never the red logo on imagery
- text only in cream #FFF9DA or white; no em dashes; headlines in caps
- a contrast warning when text sits on a light area (under 3:1)
- assets marked "do not reuse" are refused
