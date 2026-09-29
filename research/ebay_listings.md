# eBay listing research — theinternationalcargarage
Researched 2026-09-25 (subagent, read-only; eBay blocks direct page fetch — ebay.com/itm pages and the seller store page returned empty 500s to the fetcher, so research used the public search index + the indexed item-description iframe).

## Seller
- Seller ID: `theinternationalcargarage` (99.3% positive, ~1K feedback)
- Store: https://ebay.com/inf/internationalporschegarage

## Verbatim item description (item 116687431554 — Porsche/Lotus digital manual listing)
Fetched from the indexed description iframe (https://itm.ebaydesc.com/itmdesc/116687431554?...seller=theinternationalcargarage...). Peter's own words, used as the copy base for the brand pages:

> Enthusiastic Porsche & Euro Enthusiast? Let Experience Save You Thousands.
>
> | New content 12/25 lifetime access the dealers don't want you to have |
>
> |Secure Electronic Delivery | NO Shipment will take place | Paperless | check your messages once you purchase.|
>
> Supplemental Shipping option DVD - available for an additional $19.99, including shipping to the USA. Please let me know
>
> With over 20 years of hands-on experience buying, servicing, and repairing Porsches and Lotus vehicles and P0rsche ASE Dealer trained to back it up?I understand the real cost of European vehicle repairs. **Shop Service & Repair DIY Compliations is** a go-to guide for owners who want to take control of their vehicle maintenance.
>
> Includes DIY repair 6k pages ( models from 1997-2016 multiple manuals )
>
> DIY repair manuals (x3 different guides to cover the models listed ASE certified) 4000 pages
>
> Parts Manuals
>
> Service information & manuals
>
> Electrical manuals
>
> Lifetime access
>
> Whether you're a passionate car enthusiast or a seasoned mechanic, these manuals provide:
> - Fast access to accurate workshop procedures
> - These manuals will save you on repair bills or negotiating with your local dealer for reduced rates, giving you the information to understand and fix any issues with your p0rsche
> - Verified step-by-step instructions used by professional mechanics
> - Coverage from routine maintenance to complex diagnostics and repairs
>
> Support independent expertise and help keep our workshop lights on. Empower yourself with the knowledge and confidence to maintain and repair your vehicle, without the dealer-sized bill.
>
> With over 20 years of European-trained Mechanic knowledge, I've compiled a workshop of expertise to help you save thousands of dollars on DIY maintenance and repair bills, giving you a competitive edge. Fast electronic delivery? Thousands of pages of comprehensive build, tear down, and DIY information.
>
> |Secure Electronic Delivery | Paperless | check your messages once you purchase
>
> My feedback is 5 stars

NOTE: his live listing still says "$19.99" for the DVD add-on. The site uses the newer approved term **$24.99** per Peter's decision.

## Per-brand listing evidence (from search index)
- **Porsche**: multiple digital manual listings (911 Carrera, Cayman, Cayenne, GT3, Macan, Panamera, 914, 924...). Item 116687431554 (above).
- **Range Rover / Land Rover**: listings seen in index, e.g. "2012 Range Rover" digital manual, "L322 Range Rover" manual, 17–18 sold each, $25.99–$29.99 price band — description iframe for these was NOT in the search index, so copy was adapted from his Porsche/Lotus text with brand names swapped (flagged in BUILD_NOTES; Peter can edit via admin tool).
- **Lotus**: "Lotus Evora" digital manual seen in index; covered by his verbatim text (he mentions Porsches and Lotus vehicles).
- **Aston Martin**: "Aston Martin 4.7 V8 workshop manual & service guide" promo image on file (41-aston-martin-engine-manual.jpg) — description iframe NOT in index; copy adapted as above.
- Known listing IDs supplied: 116770856306, 117116352537 (titles not recoverable — direct fetch blocked).

## Images (all real, from his eBay listing photo set)
Source: `~/workspace/goals/facebook-daily-repost-rotation/hidden_files/ebay_photos/` (his eBay album photos).
Copied + compressed (JPEG q≤82, max dim 1600, each ≤500KB) into staging `assets/brands/<brand>/`:
- **porsche/**: 39 images (cayenne, 911 carrera, cayman 8000 pages, gt3/gt3rs, 914, macan, panamera, 924, 911 classic red, sale badges)
- **range-rover/**: 18 images (range-rover workshop/sport/black/white, discovery, range-rover classic, sale badges)
- **lotus/**: 2 images (45-elise-workshop-manual.jpg, 57-elise-sale-badge.jpg)
- **aston-martin/**: 2 images (41-aston-martin-engine-manual.jpg, 55-aston-martin-engine-sale.jpg)

GAP: only 2 real images each for Lotus and Aston Martin. Peter can add more from his phone via admin.html.
