# Player Notes (iPhone web app)

Mark live poker players with color labels and notes. Runs as a home-screen
web app (PWA) on iPhone, works offline, and keeps all notes on the phone.
Nothing is uploaded; the website only serves the app itself.

## Layout

The repo root is the website, so GitHub Pages serves the app whether its
source is set to "Deploy from a branch" or "GitHub Actions".

```
index.html              the whole app (HTML, CSS and JS in one file)
manifest.webmanifest    home-screen name, colors and icons
sw.js                   service worker: caches the app for offline use
icons/                  app icons (home screen, manifest)
.nojekyll               serve files as-is (no Jekyll processing)
docs/HOW-TO-INSTALL.txt original install notes
tools/make-icons.py     regenerates icons/ (needs Pillow)
.github/workflows/pages.yml  deploys the site to GitHub Pages
```

## Publish it

The site is live at https://isakbb.github.io/PokerTrackerIphoneWebApp/ and
updates on every push to `main`. Recommended Pages setting:
**Settings -> Pages -> Source: GitHub Actions** (the repo must be public on a
free account).

**Netlify (alternative):** drag a folder with `index.html`,
`manifest.webmanifest`, `sw.js` and `icons/` onto https://app.netlify.com/drop.

## Install on the iPhone

1. Open the link in **Safari** (it must be Safari).
2. Tap **Share** (square with an up arrow) -> **Add to Home Screen** -> **Add**.
3. Always open Player Notes from the home-screen icon. Notes added in a Safari
   tab are stored separately from the home-screen app.

## Where notes are saved

In the home-screen app's own storage (IndexedDB + localStorage), saved
instantly. Deleting the icon, "Clear History and Website Data" or resetting
the phone erases them, so use **Save backup to Files** (Labels tab) now and
then; **Import backup** restores it.

## Updating the app

Edit the app files, bump `CACHE` in `sw.js` (e.g. `player-notes-v1.5`)
so phones fetch the new version, and push to `main`. The app picks up the
update the next time it is opened with internet.

## Run locally

```
python3 -m http.server 8000
```
Then open http://localhost:8000 (the service worker works on localhost).
