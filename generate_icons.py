"""Generate PWA icons for the Travel Map app.

Produces:
  icons/icon-192.png         — installed-app icon (any purpose)
  icons/icon-512.png         — installed-app icon (any purpose), splash screen
  icons/icon-maskable-512.png — maskable icon with safe-area padding

Run: uv run python generate_icons.py
"""
from pathlib import Path
from PIL import Image, ImageDraw

BG = (13, 17, 23)         # #0d1117 — app background
RING = (30, 42, 64)       # #1e2a40 — card border ring
PIN = (240, 136, 62)      # #F0883E — amber accent
PIN_INNER = (13, 17, 23)  # hole in the pin head

ICONS_DIR = Path(__file__).parent / "icons"
ICONS_DIR.mkdir(exist_ok=True)


def draw_pin(img: Image.Image, cx: int, cy: int, head_r: int, *,
             pin_color=PIN, inner_color=PIN_INNER) -> None:
    """Draw a classic teardrop map pin centered horizontally at cx, head center at cy."""
    draw = ImageDraw.Draw(img)
    # Teardrop tail: triangle pointing down from below the head circle
    tail_h = int(head_r * 1.8)
    tail_w = int(head_r * 1.1)
    tip_y = cy + head_r + tail_h
    draw.polygon(
        [(cx - tail_w // 2, cy + head_r // 2),
         (cx + tail_w // 2, cy + head_r // 2),
         (cx, tip_y)],
        fill=pin_color,
    )
    # Head circle
    draw.ellipse([cx - head_r, cy - head_r, cx + head_r, cy + head_r], fill=pin_color)
    # Inner hole
    inner_r = int(head_r * 0.42)
    draw.ellipse(
        [cx - inner_r, cy - inner_r, cx + inner_r, cy + inner_r],
        fill=inner_color,
    )


def make_icon(size: int, *, maskable: bool = False) -> Image.Image:
    img = Image.new("RGB", (size, size), BG)
    draw = ImageDraw.Draw(img)

    if maskable:
        # Maskable icons need a 10% safe-area on each side; keep art inside the inner 80%.
        ring_r = int(size * 0.36)
        head_r = int(size * 0.13)
        cy = int(size * 0.44)
    else:
        ring_r = int(size * 0.42)
        head_r = int(size * 0.15)
        cy = int(size * 0.46)

    cx = size // 2
    # Subtle ring for visual depth
    ring_width = max(2, size // 64)
    draw.ellipse(
        [cx - ring_r, cy - ring_r, cx + ring_r, cy + ring_r],
        outline=RING, width=ring_width,
    )
    draw_pin(img, cx, cy, head_r)
    return img


if __name__ == "__main__":
    make_icon(192).save(ICONS_DIR / "icon-192.png", optimize=True)
    make_icon(512).save(ICONS_DIR / "icon-512.png", optimize=True)
    make_icon(512, maskable=True).save(ICONS_DIR / "icon-maskable-512.png", optimize=True)
    print(f"Wrote 3 icons to {ICONS_DIR}/")
