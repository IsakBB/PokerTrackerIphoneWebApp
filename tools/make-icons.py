"""Generate the app icons in icons/ (poker chip on the app's dark background).

Usage: pip install pillow && python3 tools/make-icons.py
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw

BG = (16, 18, 22)        # --bg   #101216
RED = (224, 38, 58)      # --accent #e0263a
DARK_RED = (170, 22, 40)
WHITE = (238, 240, 244)  # --text #eef0f4
OUT = Path(__file__).resolve().parent.parent / "icons"
SS = 4  # supersampling factor for smooth edges


def chip(size, chip_ratio, rounded):
    s = size * SS
    img = Image.new("RGBA", (s, s), BG + (255,) if not rounded else (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if rounded:
        d.rounded_rectangle([0, 0, s - 1, s - 1], radius=int(s * 0.22), fill=BG)
    c = s / 2
    r = s * chip_ratio / 2
    d.ellipse([c - r, c - r, c + r, c + r], fill=RED)
    # edge stripes
    for i in range(6):
        a = math.radians(i * 60)
        w = math.radians(12)
        pts = [(c, c)]
        for k in range(9):
            t = a - w + 2 * w * k / 8
            pts.append((c + r * math.cos(t), c + r * math.sin(t)))
        d.polygon(pts, fill=WHITE)
    ri = r * 0.78
    d.ellipse([c - ri, c - ri, c + ri, c + ri], fill=DARK_RED)
    ri2 = r * 0.70
    d.ellipse([c - ri2, c - ri2, c + ri2, c + ri2], fill=RED)
    # note lines in the centre
    lw = r * 0.09
    for j, frac in enumerate((0.75, 0.75, 0.5)):
        y = c + (j - 1) * r * 0.26
        half = r * 0.45 * frac
        x0 = c - r * 0.45
        d.rounded_rectangle([x0, y - lw / 2, x0 + 2 * half, y + lw / 2], radius=lw / 2, fill=WHITE)
    return img.resize((size, size), Image.LANCZOS)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    # iOS applies its own rounded mask, so the apple icon is a full square.
    chip(180, 0.74, False).convert("RGB").save(OUT / "apple-touch-icon.png")
    chip(192, 0.80, True).save(OUT / "icon-192.png")
    chip(512, 0.80, True).save(OUT / "icon-512.png")
    # Maskable: keep content inside the 80% safe zone on a full-bleed background.
    chip(512, 0.62, False).convert("RGB").save(OUT / "icon-maskable-512.png")


if __name__ == "__main__":
    main()
