# PayPal buttons — CREATED 2026-09-28

Created in the "Theinternationalporschegarage" business account (theinternationalporschegarage@gmail.com),
visible under PayPal dashboard → Payment Links & Buttons ("Saved links and buttons").
Note: PayPal has retired the classic Seller Tools > PayPal buttons designer (old webscr?cmd=_button-design URL 404s).
These are the new-style **hosted buttons** rendered via the PayPal JS SDK — NOT classic HTML form snippets.

## Shared SDK snippet (paste once in <head>, same for all five buttons)
```html
<script src="https://www.paypal.com/sdk/js?client-id=BAACAXDh_GmUXd4wZb-8EBJlsgw_2A9mJOTpD0rXL8noN7NnNL7IlCgoK8mFamyL8GmLKQq5UxAEnn_iks&components=hosted-buttons&enable-funding=venmo&currency=USD"></script>
```

## Button ID map (created 2026-09-28, all saved first try, no 2FA/CAPTCHA hit)
- porsche: **ZRVBZSAEA2QKS** — "Porsche Workshop Manual — Digital Delivery", $25.49 USD, digital goods (no shipping address, no shipping)
- range-rover: **LTNHLJJWRVLBU** — "Range Rover Workshop Manual — Digital Delivery", $25.49 USD, digital goods
- lotus: **YJ6GJ5DQPMZ3Y** — "Lotus Workshop Manual — Digital Delivery", $25.49 USD, digital goods
- aston-martin: **JULSE3EPZJHMA** — "Aston Martin Workshop Manual — Digital Delivery", $25.49 USD, digital goods
- dvd-addon ($24.99): **4W4AVVSTFPTJ2** — "DVD + USA Shipping Add-on", $24.99 USD, shipping address collected
- bundle ($76.47): **7VCF7JUK8BPQG** — "Any 4 Workshop Manuals - Bundle" (buy 3 get 1 free), $76.47 USD, digital goods (no shipping); created 2026-09-28 via browser task after Peter signed in himself (first attempt failed: saved-login fill ambiguous + session loss)

## Per-button snippet pattern (container id + render call; XXXXX = hosted button ID)
```html
<div id="paypal-container-XXXXX"></div>
<script>
  paypal.HostedButtons({
    hostedButtonId: "XXXXX",
  }).render("#paypal-container-XXXXX")
</script>
```
IMPORTANT: `<script>` injected via innerHTML does NOT execute — pages must create the container
via DOM and call `paypal.HostedButtons(...).render()` from their own script (see render_brand_pages.py
`renderPayPalButton`). The brand pages + admin.html were rewired for this on 2026-09-28:
brand JSONs carry `paypal_button_id` / `dvd_button_id`; the page template loads the SDK in <head>.

## Button slots in the pages (wired 2026-09-28)
Each `brands/<brand>.json` carries `paypal_button_id` (brand) and `dvd_button_id` (shared DVD button).
The admin tool (admin.html) has fields to paste each hosted button ID; pages re-render automatically.
