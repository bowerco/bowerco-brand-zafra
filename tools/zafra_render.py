#!/usr/bin/env python3
"""Zafra render kit (Bower). One way to make every reel, story frame and feed still.

Usage:
    python3 tools/zafra_render.py tools/recipes/<name>.json          # render
    python3 tools/zafra_render.py tools/recipes/<name>.json --log    # render + log asset use in assets/index.yaml

What it guarantees (brand/visual.md):
- Held frames only. Each segment is cropped once and played untouched: no zoom, pan or Ken Burns
  is possible here. To change the view, add another segment (a hard cut).
- The Zafra grade on everything, so pieces read as one feed.
- Logos only from assets/logos/ (cream by default, never red on imagery).
- Headline type only in Euclid Flex, ALL CAPS, one size per piece.

Recipe (JSON):
{
  "out": "content/drafts/media/<piece>/<name>.mp4",      # .mp4 for video, .jpg for a still
  "size": [1080, 1920],                                    # 9:16 reel/story, or [1080, 1350] feed
  "segments": [                                            # one = postcard, several = hard cuts
    {"asset": "zaf-video-007", "use_master": true,         # or "file": "assets/..."
     "in": 1.0, "out": 9.5,                                # seconds (videos). For a still from video: "at": 3.7
     "crop": "900:1600:760:1130",                          # w:h:x:y in the source pixels, held
     "stabilize": false}                                   # only for small handheld drift: check the result
  ],
  "logo": {"file": "zafra-logo-cream.svg", "width": 440, "y": 0.5, "on": "all"},   # or null. on: all | last
  "text": {"lines": ["SERVE CHILLED."], "weight": "Medium", "size": 64, "y": 0.82, "align": "center", "color": "#FFF9DA"},  # or null. align: center|left|right. Colour: cream #FFF9DA or white only. Warns under 3:1 contrast
  "editorial": {"label": "THE THREAD", "body": "Three threads grow in each bloom.",   # carousel inside slides (or null)
                "y": 0.92, "label_size": 30, "body_size": 30, "col": 0.34, "width": 0.60, "color": "#FFF9DA"},
  "audio": false
}
Editorial block (Rhode-style text system, templates/carousel.md): the label sits at the left margin in Euclid Flex caps,
the body runs in a column starting at `col` (share of the width), bottom-aligned at `y`. Set "top": true to hang it
from `y` instead (product stills with space at the top). Body font: Acumin when its files arrive, Euclid Flex Regular
(sentence case) until then.
"""
import json, os, re, subprocess, sys, tempfile, datetime
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
GRADE = 'eq=contrast=0.95:saturation=0.95:gamma=1.02,colorbalance=rs=0.03:bs=-0.03:rm=0.02:bm=-0.02'
FONT_DIR = os.path.join(ROOT, 'assets/fonts/euclid-flex-TRIAL')   # swap to licensed files when they arrive
MIN_CROP_W = 800          # below this the upscale goes soft (brand/visual.md quality floor)
FPS = 30


def run(*a):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', *a], check=True)


def probe(path):
    out = subprocess.check_output(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
                                   'stream=width,height:format=duration', '-of', 'json', path])
    j = json.loads(out)
    s = j['streams'][0]
    return s['width'], s['height'], float(j.get('format', {}).get('duration') or 0)


def load_index():
    import yaml
    with open(os.path.join(ROOT, 'assets/index.yaml')) as f:
        return {a['id']: a for a in yaml.safe_load(f)['assets']}


def source_path(seg, index):
    if 'file' in seg:
        return os.path.join(ROOT, seg['file'])
    a = index[seg['asset']]
    if 'do not reuse' in str(a.get('usage_rule', '')).lower():
        sys.exit(f"{seg['asset']} is marked do not reuse")
    if seg.get('use_master') and a.get('master'):
        return os.path.join(ROOT, 'assets', a['master'])
    return os.path.join(ROOT, a.get('path') or os.path.join('assets', a['file']))


def check_crop(seg, src_w, src_h, size):
    if not seg.get('crop'):
        sys.exit('Every segment needs a held crop (w:h:x:y). Full-frame phone clips are not allowed.')
    w, h, x, y = [int(v) for v in seg['crop'].split(':')]
    if x + w > src_w or y + h > src_h:
        sys.exit(f"crop {seg['crop']} is outside the {src_w}x{src_h} source")
    if abs(w / h - size[0] / size[1]) > 0.01:
        sys.exit(f"crop {seg['crop']} is not the output ratio {size[0]}:{size[1]}")
    if w < MIN_CROP_W:
        print(f"WARNING: crop is {w} px wide: it will be upscaled {size[0]/w:.1f}x. Check it is still sharp, or use a master.")


def svg_png(name, width, tmp):
    out = os.path.join(tmp, f'logo_{width}.png')
    if 'red' in name and 'cream' not in name:
        sys.exit('Never the red logo on imagery (brand/visual.md).')
    subprocess.run(['rsvg-convert', '-w', str(width), os.path.join(ROOT, 'assets/logos', name), '-o', out], check=True)
    return out


TEXT_COLOURS = {'#FFF9DA', '#FFFFFF'}
# The Euclid Flex TRIAL draws most punctuation as a dot (only . and , work). Until the licensed files arrive,
# these characters are drawn from Rubik so drafts read correctly.
TRIAL_MISSING = set('?!:;&%()/+"@#')
FALLBACK_FONT = os.path.join(ROOT, 'assets/fonts/Rubik-VariableFont_wght.ttf')


def _fallback(font):
    fb = ImageFont.truetype(FALLBACK_FONT, font.size)
    w = 500 if 'Medium' in font.path or 'Semi' in font.path or 'Bold' in font.path else 400
    try:
        fb.set_variation_by_axes([w])
    except Exception:
        pass
    return fb


def draw_mixed(d, xy, text, font, fill):
    """Draw text, swapping in the fallback font for punctuation the trial font lacks. Returns the width."""
    if 'TRIAL' not in getattr(font, 'path', '') or not (set(text) & TRIAL_MISSING):
        d.text(xy, text, font=font, fill=fill)
        return d.textlength(text, font=font)
    fb = _fallback(font)
    x, y = xy
    for ch in text:
        f = fb if ch in TRIAL_MISSING else font
        d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f)
    return x - xy[0]


def mixed_len(d, text, font):
    if 'TRIAL' not in getattr(font, 'path', '') or not (set(text) & TRIAL_MISSING):
        return d.textlength(text, font=font)
    fb = _fallback(font)
    return sum(d.textlength(ch, font=fb if ch in TRIAL_MISSING else font) for ch in text)   # on-screen text is always cream or white (Emi, 2026-11-20)


def text_png(t, size, tmp):
    if t.get('color', '#FFF9DA').upper() not in TEXT_COLOURS:
        sys.exit('On-screen text is always cream (#FFF9DA) or white (#FFFFFF).')
    font = ImageFont.truetype(os.path.join(FONT_DIR, f"EuclidFlexTRIAL-{t.get('weight', 'Medium')}.otf"), t.get('size', 64))
    canvas = Image.new('RGBA', tuple(size), (0, 0, 0, 0))
    d = ImageDraw.Draw(canvas)
    lines = [l.upper() for l in t['lines']]
    lh = int(t.get('size', 64) * 1.25)
    y0 = int(size[1] * t.get('y', 0.5)) - lh * len(lines) // 2
    margin = int(size[0] * 0.08)
    align = t.get('align', 'center')          # center | left | right
    boxes = []
    for i, l in enumerate(lines):
        if '\u2014' in l:
            sys.exit('No em dashes.')
        w = mixed_len(d, l, font)
        x = margin if align == 'left' else (size[0] - margin - w if align == 'right' else (size[0] - w) / 2)
        draw_mixed(d, (x, y0 + i * lh), l, font, t.get('color', '#FFF9DA'))
        boxes.append((int(x), y0 + i * lh, int(x + w), y0 + (i + 1) * lh))
    t['_boxes'] = boxes
    out = os.path.join(tmp, 'text.png')
    canvas.save(out)
    return out


BODY_FONT = os.path.join(ROOT, 'assets/fonts/acumin/Acumin-Regular.otf')   # swap in when Zafra sends Acumin


def editorial_png(e, size, tmp):
    if e.get('color', '#FFF9DA').upper() not in TEXT_COLOURS:
        sys.exit('On-screen text is always cream (#FFF9DA) or white (#FFFFFF).')
    for k in ('label', 'body'):
        if '\u2014' in e.get(k, ''):
            sys.exit('No em dashes.')
    lf = ImageFont.truetype(os.path.join(FONT_DIR, 'EuclidFlexTRIAL-Medium.otf'), e.get('label_size', 30))
    bpath = BODY_FONT if os.path.exists(BODY_FONT) else os.path.join(FONT_DIR, 'EuclidFlexTRIAL-Regular.otf')
    bf = ImageFont.truetype(bpath, e.get('body_size', 30))
    canvas = Image.new('RGBA', tuple(size), (0, 0, 0, 0))
    d = ImageDraw.Draw(canvas)
    margin = int(size[0] * 0.06)
    col_x = int(size[0] * e.get('col', 0.34))
    col_w = int(size[0] * e.get('width', 0.60))
    words, lines, cur = e.get('body', '').split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if mixed_len(d, t, bf) > col_w and cur:
            lines.append(cur); cur = w
        else:
            cur = t
    if cur:
        lines.append(cur)
    lh = int(e.get('body_size', 30) * 1.3)
    block_h = max(lh * len(lines), lh)
    y_anchor = int(size[1] * e.get('y', 0.92))
    y0 = y_anchor if e.get('top') else y_anchor - block_h
    col = e.get('color', '#FFF9DA')
    boxes = []
    if e.get('label'):
        lab = e['label'].upper()
        lw = draw_mixed(d, (margin, y0), lab, lf, col)
        boxes.append((margin, y0, int(margin + lw), y0 + lh))
    x_body = col_x if e.get('label') else margin
    for i, l in enumerate(lines):
        bw = draw_mixed(d, (x_body, y0 + i * lh), l, bf, col)
        boxes.append((x_body, y0 + i * lh, int(x_body + bw), y0 + (i + 1) * lh))
    e['_boxes'] = boxes
    if bpath != BODY_FONT:
        print('NOTE: body set in Euclid Flex Regular until the Acumin files arrive.')
    out = os.path.join(tmp, 'editorial.png')
    canvas.save(out)
    return out


def render(recipe_path, log=False):
    r = json.load(open(recipe_path))
    size = r.get('size', [1080, 1920])
    out = os.path.join(ROOT, r['out'])
    os.makedirs(os.path.dirname(out), exist_ok=True)
    index = load_index()
    still = out.lower().endswith(('.jpg', '.png'))
    tmp = tempfile.mkdtemp()
    parts = []
    for n, seg in enumerate(r['segments']):
        src = source_path(seg, index)
        sw, sh, dur = probe(src)
        check_crop(seg, sw, sh, size)
        chain = []
        if seg.get('stabilize'):
            trf = os.path.join(tmp, f's{n}.trf')
            run('-i', src, '-vf', f'vidstabdetect=shakiness=6:accuracy=15:result={trf}', '-f', 'null', '-')
            chain.append(f'vidstabtransform=input={trf}:tripod=1:zoom=0:optzoom=0:interpol=bicubic')
        chain += [f"crop={seg['crop']}", f'scale={size[0]}:{size[1]}:flags=lanczos', GRADE]
        p = os.path.join(tmp, f'p{n}' + ('.png' if still else '.mp4'))
        if still:
            at = ['-ss', str(seg['at'])] if 'at' in seg else []
            run(*at, '-i', src, '-frames:v', '1', '-vf', ','.join(chain), p)
        else:
            t0, t1 = seg.get('in', 0), seg.get('out', dur)
            run('-ss', str(t0), '-t', str(t1 - t0), '-i', src, '-vf', f'fps={FPS},' + ','.join(chain) + ',format=yuv420p',
                '-an', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '16', p)
        parts.append(p)

    base = parts[0]
    if len(parts) > 1:
        if still:
            sys.exit('A still takes one segment.')
        lst = os.path.join(tmp, 'list.txt')
        open(lst, 'w').write(''.join(f"file '{p}'\n" for p in parts))
        base = os.path.join(tmp, 'cut.mp4')
        run('-f', 'concat', '-safe', '0', '-i', lst, '-c', 'copy', base)

    overlays = []
    if r.get('scrim'):
        # Soft dark fade behind story lines (story sets only): {"scrim": {"edge": "top", "opacity": 0.45, "reach": 0.4}}
        sc = r['scrim']
        g = Image.new('RGBA', tuple(size), (0, 0, 0, 0))
        reach = int(size[1] * sc.get('reach', 0.4))
        op = sc.get('opacity', 0.45)
        px = g.load()
        for yy in range(reach):
            a = int(255 * op * (1 - yy / reach) ** 1.6)
            row = yy if sc.get('edge', 'top') == 'top' else size[1] - 1 - yy
            for xx in range(size[0]):
                px[xx, row] = (0, 0, 0, a)
        sp = os.path.join(tmp, 'scrim.png')
        g.save(sp)
        overlays.append((sp, '0:0', 0))
    lg = r.get('logo')
    if lg:
        png = svg_png(lg.get('file', 'zafra-logo-cream.svg'), lg.get('width', 440), tmp)
        start = 0
        if lg.get('on') == 'last' and len(parts) > 1:
            start = sum(probe(p)[2] for p in parts[:-1])
        overlays.append((png, f"(W-w)/2:H*{lg.get('y', 0.5)}-h/2", start))
    if r.get('text'):
        overlays.append((text_png(r['text'], size, tmp), '0:0', 0))
        if not r.get('scrim'):
            warn_contrast(base, r['text'], still, tmp)
    if r.get('editorial'):
        overlays.append((editorial_png(r['editorial'], size, tmp), '0:0', 0))
        warn_contrast(base, r['editorial'], still, tmp)

    inputs, fc, last = ['-i', base], '', '[0:v]'
    for i, (png, pos, start) in enumerate(overlays, 1):
        inputs += ['-i', png]
        en = f":enable='gte(t,{start})'" if start and not still else ''
        fc += f'{last}[{i}:v]overlay={pos}{en}[v{i}];'
        last = f'[v{i}]'
    if still:
        if overlays:
            run(*inputs, '-filter_complex', fc.rstrip(';'), '-map', last, '-frames:v', '1', '-q:v', '2', out)
        else:
            run('-i', base, '-q:v', '2', out)
    else:
        args = [*inputs]
        if overlays:
            args += ['-filter_complex', fc + f'{last}format=yuv420p[out]', '-map', '[out]']
        args += ['-an', '-c:v', 'libx264', '-preset', 'medium', '-crf', '20', '-movflags', '+faststart', out]
        run(*args)
    print('rendered', os.path.relpath(out, ROOT))
    if log:
        log_use(r, index)


def _lum(rgb):
    def ch(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * ch(rgb[0]) + 0.7152 * ch(rgb[1]) + 0.0722 * ch(rgb[2])


def warn_contrast(base, t, still, tmp):
    """Warn when the cream or white text sits on a background too light to read (WCAG large text: 3:1)."""
    frame = base
    if not still:
        frame = os.path.join(tmp, 'probe.png')
        run('-ss', '1', '-i', base, '-frames:v', '1', frame)
    im = Image.open(frame).convert('RGB')
    x0 = min(b[0] for b in t['_boxes']); y0 = min(b[1] for b in t['_boxes'])
    x1 = max(b[2] for b in t['_boxes']); y1 = max(b[3] for b in t['_boxes'])
    sm = im.crop((max(x0, 0), max(y0, 0), x1, y1)).resize((40, 20))
    px = [sm.getpixel((i, j)) for i in range(40) for j in range(20)]
    bg = _lum(tuple(sorted(c[i] for c in px)[len(px) * 3 // 4] for i in range(3)))   # the lighter areas behind the text
    fg = _lum(tuple(int(t.get('color', '#FFF9DA')[k:k + 2], 16) for k in (1, 3, 5)))
    ratio = (max(fg, bg) + 0.05) / (min(fg, bg) + 0.05)
    if ratio < 3:
        print(f'WARNING: text contrast {ratio:.1f}:1 (under 3:1). Move the text onto a deeper colour area or pick another crop.')
    else:
        print(f'text contrast {ratio:.1f}:1')


def log_use(r, index):
    """Bump times_used / last_used and add the piece to used_in, keeping the file's formatting."""
    piece = r.get('piece') or r['out']
    today = datetime.date.today().isoformat()
    p = os.path.join(ROOT, 'assets/index.yaml')
    txt = open(p).read()
    for aid in {s['asset'] for s in r['segments'] if 'asset' in s}:
        m = re.search(rf'^- id: {re.escape(aid)}\n(.*?)(?=^- id: |\Z)', txt, flags=re.S | re.M)
        block = m.group(0)
        if piece in block:
            continue
        b = re.sub(r'^  used_in: \[\]$', f'  used_in:\n  - {piece}', block, flags=re.M)
        if b == block:
            b = re.sub(r'^  used_in:[ \t]*\n((?:  - .*\n)*)', lambda mm: f'  used_in:\n{mm.group(1)}  - {piece}\n', block, flags=re.M)
        b = re.sub(r'^  times_used: (\d+)$', lambda mm: f'  times_used: {int(mm.group(1)) + 1}', b, flags=re.M)
        b = re.sub(r'^  last_used: .*$', f'  last_used: "{today}"', b, flags=re.M)
        txt = txt.replace(block, b)
    open(p, 'w').write(txt)
    print('logged asset use in assets/index.yaml')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    render(sys.argv[1], log='--log' in sys.argv)
