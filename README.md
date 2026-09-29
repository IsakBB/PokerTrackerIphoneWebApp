# Player Notes (iPhone web app)

Mark live poker players with color labels and notes. Runs as a home-screen
web app (PWA) on iPhone, works offline, and keeps all notes on the phone.
Nothing is uploaded; the website only serves the app itself.

## Layout

```
app/                    <- everything that gets published (the website root)
  index.html            the whole app (HTML, CSS and JS in one file)
  manifest.webmanifest  home-screen name, colors and icons
  sw.js                 service worker: caches the app for offline use
  icons/                app icons (home screen, manifest)
  .nojekyll
docs/HOW-TO-INSTALL.txt original install notes
tools/make-icons.py     regenerates app/icons/ (needs Pillow)
.github/workflows/pages.yml  deploys app/ to GitHub Pages
```

## Publish it (one time)

The iPhone needs to load the app once from an `https://` address.

**GitHub Pages (this repo):**
1. Merge this branch into `main`.
2. On GitHub: **Settings -> Pages -> Build and deployment -> Source: GitHub Actions**.
3. The *Deploy to GitHub Pages* workflow runs on every push to `main`
   (or run it by hand under **Actions**). The link is
   `https://<your-username>.github.io/PokerTrackerIphoneWebApp/`.
   The repository must be public for Pages on a free account.

**Netlify (alternative):** drag the `app/` folder onto https://app.netlify.com/drop.

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

Edit files in `app/`, bump `CACHE` in `app/sw.js` (e.g. `player-notes-v1.3`)
so phones fetch the new version, and push to `main`. The app picks up the
update the next time it is opened with internet.

## Run locally

```
cd app && python3 -m http.server 8000
```
Then open http://localhost:8000 (the service worker works on localhost).
