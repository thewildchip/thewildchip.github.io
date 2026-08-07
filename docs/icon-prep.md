# Website icon prep

## Best source file

Use one master icon file:

- Best: `1024x1024` PNG with transparent background.
- Also good: square SVG, if exported cleanly.
- Minimum: `512x512` PNG.
- Avoid: tiny 32x32 images, screenshots, JPEGs, text-heavy logos, and detailed drawings.

For this site, a simple high-contrast mark works best because favicons are often displayed at only 16x16 or 32x32 pixels.

## What the site needs

Browsers and devices need several derived files, not just one image:

- `favicon.ico` for classic browser support.
- `favicon-16x16.png`, `favicon-32x32.png`, `favicon-96x96.png` for browser tabs/search surfaces.
- `apple-touch-icon.png` for iPhone/iPad home-screen bookmarks.
- `android-chrome-192x192.png`, `android-chrome-512x512.png` for Android/PWA metadata.
- `site.webmanifest` to describe the larger icons.

These are generated automatically by `tools/generate-favicons.py`.

## How to use when the final icon is ready

From the project root, run:

```bash
python3 tools/generate-favicons.py /path/to/your/icon.png
hugo --cleanDestinationDir --gc --minify
```

Then commit the changed files under `static/`, plus the favicon partial if not already committed.

## Design advice

A good favicon is more like an app icon than a poster:

- Use one bold symbol or 1-2 letters.
- Keep generous padding around the mark.
- Test it at 16x16 before deciding.
- Prefer strong silhouette over small details.
- For your current site style, a minimal `twc`, chip, spark, or monogram mark would fit better than a complex illustration.
