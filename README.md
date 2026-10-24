# Travel Map

Installable PWA that tracks countries you've visited on an interactive dark-themed world map. Works fully offline, shareable via QR link.

**Live:** https://paulius11.github.io/travel-map/

## Features

- **Progress hero** — on open you see "N / total countries visited" with a progress ring, % of world land and regions covered. It counts up as you add countries and celebrates 10/25/50/100/150.
- Interactive D3 + TopoJSON world map with pan, zoom, +/- controls and click-to-toggle. On touch screens the first tap opens a country card, so stray taps never change anything.
- **Search that navigates** — type a country, press Enter to fly to it and open its card; arrow keys and Space work from the keyboard.
- **Visited / Not yet / All** tabs, grouped by region, plus a region chip strip with per-region progress.
- Undo for every add, remove and "Clear all".
- Swipeable mobile bottom sheet (peek / half / full) that keeps your count and search visible.
- QR + copy-link sharing — state lives in the URL hash. Opening someone else's link shows a banner and never overwrites your saved map unless you choose "Save as mine".
- Export / import JSON (round-trips its own export; also reads photo-pipeline output).
- Single HTML file. No backend. No tracking. No accounts.
- **Installable as a PWA**: works fully offline after the first visit, with an "update available" prompt.

## Install on your phone

1. Open https://paulius11.github.io/travel-map/ in Chrome (Android) or Safari (iOS).
2. **Android:** menu → *Install app* (or accept the install prompt).
   **iOS:** Share → *Add to Home Screen*.
3. Launches like a native app from your home screen; no network needed after the first load.

## Run locally

The app is a single static file with no build step. Open it through any HTTP server — `file://` works for most features, but service workers require `http://` or `https://`:

```bash
python3 -m http.server 8000
# then open http://localhost:8000/
```

## Regenerate icons

Icons live in [`icons/`](icons/) and are produced by [`generate_icons.py`](generate_icons.py) (requires Pillow):

```bash
pip install Pillow
python3 generate_icons.py
```

## Updating the deployed app

`sw.js` precaches the app shell, so installed clients keep serving the cached copy until the service worker updates. To force a refresh on next online launch:

1. Make your changes to `index.html` (or any precached file).
2. Bump `CACHE_VERSION` in [`sw.js`](sw.js).
3. Commit + push to `main`. GitHub Pages redeploys automatically.

## Tech

- [D3.js](https://d3js.org/) v7 — SVG rendering, zoom/pan, projection.
- [TopoJSON](https://github.com/topojson/topojson) `world-atlas@2 countries-110m` — embedded inline, no network fetch.
- [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator) — share-link QR codes.
- All three libs are inlined into `index.html`, so the app works offline from the very first load.

## License

[GPL-3.0](LICENSE)
