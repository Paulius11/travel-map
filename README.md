# Travel Map

Installable PWA that tracks countries you've visited on an interactive dark-themed world map. Works fully offline, shareable via QR link.

**Live:** https://paulius11.github.io/travel-map/

## Features

- Interactive D3 + TopoJSON world map (200+ countries) with pan, zoom, and click-to-toggle.
- Per-continent stats with area-weighted "% of land covered" — not just country count.
- Continent card grid for at-a-glance summary across Africa, Europe, Asia, the Americas, Oceania, Antarctica, and the Caribbean.
- Zoom-revealed country name labels.
- QR + copy-link sharing — state is encoded in the URL hash, so a single link reproduces the exact set of visited countries on another device.
- Single HTML file. No backend. No tracking. No accounts.
- **Installable as a PWA**: works fully offline after the first visit, launches full-screen with its own app icon.

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
