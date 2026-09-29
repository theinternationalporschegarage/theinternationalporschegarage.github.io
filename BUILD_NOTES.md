# BUILD NOTES — International Porsche Garage brand pages + PayPal + admin tool
Staging dir: `/home/hatch/workspace/site-deploys/garage-brand-pages/` (copied from `garage-new-home`, NOT deployed).
Built 2026-09-25 by subagent. Parent handles deploy + verification.

## What was built

**Brand pages (JSON-driven):**
- `brands/porsche.html` — 39 gallery images, 4 products
- `brands/range-rover.html` — 18 gallery images, 3 products
- `brands/lotus.html` — 2 gallery images, 2 products
- `brands/aston-martin.html` — 2 gallery images, 1 product
- Each page: hero (brand name + tagline + hero photo), description (Peter's eBay copy, lightly formatted), ✓ bullet list, "Buy Direct & Save 15%" section ($25.49 direct vs $29.99 eBay, PayPal button slot), same-day digital delivery explainer, DVD add-on upsell ($24.99), manual gallery, eBay link.
- Content source of truth: `brands/<slug>.json` (editable). Pages render via `fetch(<slug>.json)` with the JSON also inlined as fallback so they work on file:// and GitHub Pages.
- Regeneration scripts: `research/build_brands.py` (writes JSON) + `research/render_brand_pages.py` (writes HTML). Re-run both after hand-editing JSON.

**Homepage:** `index.html` is now a 4-brand hub (brand cards with photos → brand pages). Kept the Pelican Parts / Rexing affiliate section and the delivery explainer.

**manuals.html:** kept working; banner added linking to the new Porsche brand page.

**SEO:** `sitemap.xml` + `robots.txt` now use `https://theinternationalporschegarage.github.io/` (Peter's chosen clean URL). Includes all 4 brand pages + admin.html.

**Admin tool:** `admin.html` — phone-friendly, single file, passcode-gated (set on first visit, stored in localStorage).
Per brand: edit name, tagline, description paragraphs, bullets, products (name/price/description/eBay link), gallery (add from phone, remove, ★ set top image), PayPal button HTML fields.
Two save paths: (A) **Download updated files** → saves the JSON + new pictures to his device to send to Edison; (B) **Publish live now** → commits JSON/images to the GitHub repo via the Contents API using a personal access token stored only in his browser's localStorage (one-time setup instructions on the page). Token is never sent anywhere except api.github.com on publish.
NOTE: admin.html must be opened from the live site (http/https) — brand JSONs can't load from file://.

## PayPal buttons — NOT done (blocked, needs parent)
The build subagent cannot run signed-in browser tasks, so no buttons were created.
Required (browser task, PayPal signed in via Secure Vault credential fill):
1. 4 × hosted "Buy Now" buttons — digital goods, no shipping — $25.49 USD:
   - "Porsche Workshop Manual — Digital Delivery"
   - "Range Rover Workshop Manual — Digital Delivery"
   - "Lotus Workshop Manual — Digital Delivery"
   - "Aston Martin Workshop Manual — Digital Delivery"
2. 1 × $24.99 "DVD + USA Shipping Add-on" button.
3. Record button IDs + HTML snippets in `research/paypal_buttons.md` (slots ready).
Until buttons exist, brand pages show an eBay-buy fallback — no dead checkout path. Paste the HTML into each brand's PayPal fields via admin.html (or hand-edit the JSON) once created. On any PayPal 2FA/CAPTCHA/security check: STOP, Peter handles it himself.

## Content provenance (what came from which eBay listing)
- Verbatim description base: Peter's live eBay listing **116687431554** (indexed description iframe; seller=theinternationalcargarage) — "Enthusiastic Porsche & Euro Enthusiast? Let Experience Save You Thousands…" — used nearly as-is for Porsche & Lotus (his text covers both). Light fixes: "Compliations"→"Compilations"; DVD price updated from his listing's old $19.99 to the approved $24.99.
- Range Rover + Aston Martin copy: adapted from the same text with brand names swapped — their description iframes were NOT in the search index and eBay blocked direct fetches (ebay.com/itm pages + store page returned empty 500s to the fetcher). Peter can correct wording via admin.html.
- Listing IDs 116770856306 / 117116352537: titles not recoverable (fetch blocked); not quoted anywhere on the site.
- Images: all real, from his eBay photo album (`~/workspace/goals/facebook-daily-repost-rotation/hidden_files/ebay_photos/`, captions from `ebay_content.json` titles). Compressed to ≤500KB JPEGs in `assets/brands/<brand>/`. Gallery counts: Porsche 39, Range Rover 18, Lotus 2, Aston Martin 2.
- GAP: only 2 real images each for Lotus and Aston Martin. Peter can add more from his phone via admin.html.

## Approved terms used (exact)
"Buy Direct & Save 15%", direct $25.49, eBay $29.99, "same-day digital delivery" (never "instant"), base product digital/nothing shipped, DVD + USA shipping $24.99 add-on, access instructions delivered manually to the buyer's PayPal email.

## Validation
- Local http.server: all 9 pages + 4 JSONs return 200; all 61 gallery images resolve via HTTP; every local link/image referenced from every page resolves (no broken links).
- Brand JSONs parse; inline fallback JSON in each HTML matches its .json file exactly.
- JS syntax-checked with node --check (admin.html, brand page template).
- No screenshots taken — subagent has no browser; parent should eyeball pages before deploy.

## Deploy checklist for parent
1. Create the 5 PayPal buttons (see above); record IDs.
2. Visual check of brand pages + admin.html on staging.
3. Deploy staging to the renamed repo; verify https://theinternationalporschegarage.github.io/brands/porsche.html etc.
4. Give Peter the admin.html URL + his PayPal button HTML to paste in.
