# Brand assets — NoseyMutt logo

Launch-ready logo files (transparent PNG). Generated from the brand palette + Quicksand Bold (the brand heading font). Replace with a custom logo later if you want — these are good enough to launch.

| File | Size | Use |
|---|---|---|
| `logo-noseymutt.png` | 1338×300 | **Primary wordmark** (Ink text). Shopify header logo, invoices, light backgrounds. |
| `logo-noseymutt-light.png` | 1338×300 | Wordmark with **cream text** for dark/Clay backgrounds (footer, announcement bar). |
| `logo-mark.png` | 600×600 | **Standalone nose badge** — social profile pics, app icons, watermark on photos. |
| `favicon.png` | 512×512 | Browser-tab **favicon** (Shopify auto-resizes). Also fine as a small social avatar. |

## Colors used
Mustard badge `#F2B33D` · Ink nose/text `#2B2A28` · Cream shine/light-text `#FBF6EE` (see `../brand.md`).

## Where they're used in setup
- Shopify **Theme → Logo** → `logo-noseymutt.png`; **Theme → Favicon** → `favicon.png` (Phase 3 of the setup walkthrough).
- Instagram/TikTok/Pinterest profile photo → `logo-mark.png` or `favicon.png`.

## Need a different format?
Some channels want a JPG (no transparency) or a specific size. Regenerate/convert with Pillow:
```bash
python3 - <<'PY'
from PIL import Image
im = Image.open("logo-noseymutt.png").convert("RGBA")
bg = Image.new("RGBA", im.size, (251,246,238,255))  # cream background
Image.alpha_composite(bg, im).convert("RGB").save("logo-noseymutt.jpg", quality=92)
PY
```
The source generator script is in the repo history (commit that added these assets) if you want to tweak the mark.
