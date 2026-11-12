# JP Water Treatment Solutions - how to open the website in VS Code

## What is inside this folder
| Item | What it is |
|---|---|
| `jp-water-site/` | The complete website: 4 pages + privacy policy + 404, all images, CSS, JS, sitemap.xml, robots.txt. This is the folder you upload to hosting. |
| `source/` | The generator script (`build.py`) and notes for a developer. Not for upload. |
| `PREVIEW-open-by-double-click.html` | One-file preview of the whole site (images embedded). Opens by double-click, nothing to install. It is only a preview, not the real website files. |
| `.vscode/` | Settings that make VS Code run the site correctly. |
| `package.json` | Optional: lets you run the site with `npm start` if Node.js is installed. The site itself needs no Node packages. |

Fonts: the site loads Inter and Plus Jakarta Sans from Google Fonts (online). No font files are stored in the project; offline it falls back to Arial and still works.

## Option A (recommended): VS Code + Live Server
1. Extract the ZIP (right-click, Extract All).
2. Open VS Code, choose File, Open Folder, and select the extracted `JP-Water-Website` folder (or the `jp-water-site` folder inside it).
3. Install the extension **Live Server** (publisher: Ritwick Dey): press Ctrl+Shift+X, search "Live Server", click Install. VS Code may also suggest it automatically.
4. In the left Explorer open `jp-water-site`, right-click `index.html`, choose **Open with Live Server**.
5. The site opens in your browser (usually http://127.0.0.1:5500/). Click through Home, Services, About Us, Contact Us.

IMPORTANT: do not double-click `jp-water-site/index.html`. The pages use paths such as `/assets/style.css`, which only work when the site is served by a local server (Live Server does this). Opened directly from the folder, the page loses its styling and images.

## Option B: Python (if installed)
Open a terminal inside `jp-water-site` and run `python -m http.server 8000`, then open http://localhost:8000/

## Option C: Node.js (if installed)
In a terminal opened in this folder run `npm start`. It serves `jp-water-site` at http://localhost:8080/ and opens the browser.

## Option D: no setup at all
Double-click `PREVIEW-open-by-double-click.html`. (Needs internet only for the Google Fonts.)

## Before the site goes live
1. Domain: run `set-domain.sh https://www.yourdomain.com` inside `jp-water-site` (or find and replace `https://YOUR-DOMAIN.com`).
2. Open `jp-water-site/assets/site.js` and set `FORM_ENDPOINT`, `GA4_ID` and `GTM_ID` at the top (see `jp-water-site/SETUP-GUIDE.md` for exact steps and URLs).
3. Create the domain, hosting, Formspree, GA4 and Search Console accounts under the client's own login.
4. Read `jp-water-site/README-SEO.md` for everything that was built, and the list of items the owner must confirm (address, manager WhatsApp, name spellings, real photos for AMC and Industrial Water Treatment).

## Editing
- Page text and layout: edit `source/build.py`, run `python build.py`, then copy the generated files from the new `out` folder into `jp-water-site`. Details are in `source/README-SOURCE.md`.
- Colours, spacing: `jp-water-site/assets/style.css`. Behaviour and settings: `jp-water-site/assets/site.js`.
- If you change style.css or site.js, change `ASSET_V` in `build.py` (and rebuild) so visitors do not see a cached old file.
