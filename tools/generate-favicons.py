#!/usr/bin/env python3
"""Generate website favicon assets from one square source image.

Usage:
  python3 tools/generate-favicons.py path/to/icon.png

Best source: 1024x1024 PNG with transparency, or at least 512x512.
SVG input is supported only if cairosvg, rsvg-convert, or ImageMagick is installed.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
STATIC = ROOT / "static"
BACKGROUND = "#0f0f0f"
THEME_COLOR = "#0f0f0f"

PNG_TARGETS = {
    "favicon-16x16.png": 16,
    "favicon-32x32.png": 32,
    "favicon-96x96.png": 96,
    "android-chrome-192x192.png": 192,
    "android-chrome-512x512.png": 512,
    "apple-touch-icon.png": 180,
}


def rasterize_svg(source: Path) -> Path:
    tmp = Path(tempfile.mkdtemp()) / "icon.png"

    if shutil.which("rsvg-convert"):
        subprocess.run(
            ["rsvg-convert", "-w", "1024", "-h", "1024", str(source), "-o", str(tmp)],
            check=True,
        )
        return tmp

    if shutil.which("magick"):
        subprocess.run(["magick", str(source), "-resize", "1024x1024", str(tmp)], check=True)
        return tmp

    try:
        import cairosvg  # type: ignore
    except Exception as exc:  # pragma: no cover
        raise SystemExit(
            "SVG input needs one of these installed: cairosvg, rsvg-convert, or ImageMagick. "
            "Simplest fix: export your icon as a 1024x1024 PNG and run this script again."
        ) from exc

    cairosvg.svg2png(url=str(source), write_to=str(tmp), output_width=1024, output_height=1024)
    return tmp


def load_source(source: Path) -> Image.Image:
    if source.suffix.lower() == ".svg":
        source = rasterize_svg(source)

    image = Image.open(source).convert("RGBA")

    # Make a square canvas without cropping. Favicons must be square; if the
    # source is rectangular, this preserves the whole image and adds padding.
    side = max(image.size)
    canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    canvas.alpha_composite(image, ((side - image.width) // 2, (side - image.height) // 2))
    return canvas


def save_png(image: Image.Image, path: Path, size: int, *, apple: bool = False) -> None:
    resized = ImageOps.contain(image, (size, size), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    canvas.alpha_composite(resized, ((size - resized.width) // 2, (size - resized.height) // 2))

    # iOS home-screen icons look better and more predictable without alpha.
    if apple:
        bg = Image.new("RGBA", (size, size), BACKGROUND)
        bg.alpha_composite(canvas)
        canvas = bg.convert("RGB")

    canvas.save(path, optimize=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate favicon files into ./static")
    parser.add_argument("source", help="source icon, ideally a 1024x1024 PNG or SVG")
    args = parser.parse_args()

    source = Path(args.source).expanduser().resolve()
    if not source.exists():
        print(f"Source file not found: {source}", file=sys.stderr)
        return 1

    STATIC.mkdir(exist_ok=True)
    image = load_source(source)

    for filename, size in PNG_TARGETS.items():
        save_png(image, STATIC / filename, size, apple=(filename == "apple-touch-icon.png"))

    # Pillow creates the multiple embedded ICO sizes from the source image when
    # the `sizes` parameter is passed directly.
    ico_sizes = [16, 32, 48]
    image.save(STATIC / "favicon.ico", sizes=[(size, size) for size in ico_sizes])

    # Compatibility: the Shibui theme ships old icons under /favicon_io/.
    # Some generated/deployed pages or browser caches may still request those
    # URLs, so we overwrite them too instead of leaving the theme's bear icon
    # available anywhere in the final public site.
    legacy_dir = STATIC / "favicon_io"
    legacy_dir.mkdir(exist_ok=True)
    legacy_targets = {
        "favicon-16x16.png": 16,
        "favicon-32x32.png": 32,
        "favicon-96x96.png": 96,
        "android-icon-36x36.png": 36,
        "android-icon-48x48.png": 48,
        "android-icon-72x72.png": 72,
        "android-icon-96x96.png": 96,
        "android-icon-144x144.png": 144,
        "android-icon-192x192.png": 192,
        "apple-icon-57x57.png": 57,
        "apple-icon-60x60.png": 60,
        "apple-icon-72x72.png": 72,
        "apple-icon-76x76.png": 76,
        "apple-icon-114x114.png": 114,
        "apple-icon-120x120.png": 120,
        "apple-icon-144x144.png": 144,
        "apple-icon-152x152.png": 152,
        "apple-icon-180x180.png": 180,
        "ms-icon-70x70.png": 70,
        "ms-icon-144x144.png": 144,
        "ms-icon-150x150.png": 150,
        "ms-icon-310x310.png": 310,
    }
    for filename, size in legacy_targets.items():
        save_png(image, legacy_dir / filename, size, apple=filename.startswith("apple-icon"))
    image.save(legacy_dir / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])

    # Also update the older /images/favicon.png asset, in case any surface uses it.
    images_dir = STATIC / "images"
    images_dir.mkdir(exist_ok=True)
    save_png(image, images_dir / "favicon.png", 512)

    manifest = {
        "name": "Daniel Panoor",
        "short_name": "Daniel Panoor",
        "icons": [
            {
                "src": "/android-chrome-192x192.png",
                "sizes": "192x192",
                "type": "image/png",
            },
            {
                "src": "/android-chrome-512x512.png",
                "sizes": "512x512",
                "type": "image/png",
            },
        ],
        "theme_color": THEME_COLOR,
        "background_color": THEME_COLOR,
        "display": "standalone",
    }
    (STATIC / "site.webmanifest").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (legacy_dir / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    (legacy_dir / "browserconfig.xml").write_text(
        f'<browserconfig><msapplication><tile><square150x150logo src="/favicon_io/ms-icon-150x150.png"/><TileColor>{THEME_COLOR}</TileColor></tile></msapplication></browserconfig>\n',
        encoding="utf-8",
    )

    print("Generated favicon assets:")
    for name in ["favicon.ico", *PNG_TARGETS.keys(), "site.webmanifest", "images/favicon.png"]:
        print(f"  static/{name}")
    print("  static/favicon_io/*")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
