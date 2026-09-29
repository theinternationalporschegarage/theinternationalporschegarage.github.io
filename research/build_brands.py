#!/usr/bin/env python3
"""Build brand JSON files + brand HTML pages for the garage site upgrade."""
import json, os

STAGING = os.path.expanduser('~/workspace/site-deploys/garage-brand-pages')
BR = os.path.join(STAGING, 'brands')
ASSETS = os.path.join(STAGING, 'assets', 'brands')

EBAY_STORE = "https://ebay.com/inf/internationalporschegarage?mkcid=1&mkrid=711-53200-19255-0&siteid=0&campid=5339212462&toolid=80008&mkevt=1"

def gallery(brand, files):
    return [{"src": "../assets/brands/%s/%s" % (brand, f),
             "caption": f.replace('-', ' ').replace('.jpg', '')} for f in sorted(files)]

brands = {
  "porsche": {
    "brand": "Porsche",
    "slug": "porsche",
    "tagline": "Porsche workshop manuals — 911, Boxster, Cayman, Cayenne, Panamera, Macan & Taycan. Same-day digital delivery.",
    "hero_image": "../assets/brands/porsche/03-911-carrera-workshop-manual.jpg",
    "description_paragraphs": [
      "Enthusiastic Porsche owner? Let experience save you thousands. Shop Service & Repair DIY Compilations is a go-to guide for owners who want to take control of their vehicle maintenance.",
      "With over 20 years of hands-on experience buying, servicing, and repairing Porsches — and Porsche ASE dealer training to back it up — I understand the real cost of European vehicle repairs.",
      "This is the same depth of information a dealer technician works from: thousands of pages of comprehensive build, tear-down, and DIY information, with new content added — lifetime access to the material the dealers don't want you to have.",
      "Support independent expertise and help keep our workshop lights on. Empower yourself with the knowledge and confidence to maintain and repair your vehicle, without the dealer-sized bill."
    ],
    "bullets": [
      "Includes DIY repair manuals covering 6,000+ pages (models 1997–2016, multiple manuals)",
      "Parts manuals, service information & manuals, electrical manuals",
      "Fast access to accurate workshop procedures",
      "Save on repair bills — or negotiate reduced rates with your dealer",
      "Verified step-by-step instructions used by professional mechanics",
      "Coverage from routine maintenance to complex diagnostics and repairs",
      "Lifetime access"
    ],
    "gallery": gallery("porsche", os.listdir(os.path.join(ASSETS, "porsche"))),
    "products": [
      {"name": "911 Workshop Manual (digital)", "price": "$25.49",
       "description": "Complete 911 service & repair coverage — 964, 993, 996, 997, 991, 992. Delivered digitally the same day.",
       "ebay_link": "https://www.ebay.com/sch/i.html?_ssn=theinternationalcargarage&_nkw=911+workshop+manual"},
      {"name": "Cayenne Workshop Manual (digital)", "price": "$25.49",
       "description": "Cayenne SUV diagnostics, suspension and drivetrain coverage. Delivered digitally the same day.",
       "ebay_link": "https://www.ebay.com/sch/i.html?_ssn=theinternationalcargarage&_nkw=cayenne+workshop+manual"},
      {"name": "Cayman & Boxster Workshop Manual (digital)", "price": "$25.49",
       "description": "Mid-engine service & repair — 986, 987, 981, 718. Delivered digitally the same day.",
       "ebay_link": "https://www.ebay.com/sch/i.html?_ssn=theinternationalcargarage&_nkw=cayman+workshop+manual"},
      {"name": "Macan / Panamera / Taycan Workshop Manual (digital)", "price": "$25.49",
       "description": "Service coverage for Macan, Panamera and Taycan. Delivered digitally the same day.",
       "ebay_link": "https://www.ebay.com/sch/i.html?_ssn=theinternationalcargarage&_nkw=macan+workshop+manual"}
    ],
    "ebay_search_url": "https://www.ebay.com/sch/i.html?_ssn=theinternationalcargarage&_nkw=porsche+workshop+manual",
    "paypal_button_id": "",
    "paypal_button_html": "",
    "direct_price": "$25.49",
    "ebay_price": "$29.99",
    "dvd_addon_price": "$24.99",
    "dvd_button_id": "",
    "dvd_button_html": ""
  },
  "range-rover": {
    "brand": "Range Rover (Land Rover)",
    "slug": "range-rover",
    "tagline": "Range Rover & Land Rover workshop manuals — L322, L405, Sport & Discovery. Same-day digital delivery.",
    "hero_image": "../assets/brands/range-rover/10-range-rover-workshop.jpg",
    "description_paragraphs": [
      "Enthusiastic Land Rover owner? Let experience save you thousands. Shop Service & Repair DIY Compilations is a go-to guide for owners who want to take control of their vehicle maintenance.",
      "With over 20 years of hands-on experience buying, servicing, and repairing European vehicles — and ASE dealer training to back it up — I understand the real cost of keeping a Range Rover on the road.",
      "This is the same depth of information a dealer technician works from: thousands of pages of comprehensive build, tear-down, and DIY information — service schedules, torque specs, wiring diagrams, diagnostic procedures and full rebuild coverage.",
      "Support independent expertise and help keep our workshop lights on. Empower yourself with the knowledge and confidence to maintain and repair your vehicle, without the dealer-sized bill."
    ],
    "bullets": [
      "Complete workshop coverage: L322, L405, Range Rover Sport, Discovery",
      "Engine, gearbox, air suspension, brakes, electrics, bodywork",
      "Parts manuals, service information & manuals, electrical manuals",
      "Fast access to accurate workshop procedures",
      "Verified step-by-step instructions used by professional mechanics",
      "Coverage from routine maintenance to complex diagnostics and repairs",
      "Lifetime access"
    ],
    "gallery": gallery("range-rover", os.listdir(os.path.join(ASSETS, "range-rover"))),
    "products": [
      {"name": "Range Rover Workshop Manual (digital)", "price": "$25.49",
       "description": "Full Range Rover service & repair — L322, L405 and newer. Delivered digitally the same day.",
       "ebay_link": "https://www.ebay.com/sch/i.html?_ssn=theinternationalcargarage&_nkw=range+rover+workshop+manual"},
      {"name": "Range Rover Sport Workshop Manual (digital)", "price": "$25.49",
       "description": "Sport service & repair coverage. Delivered digitally the same day.",
       "ebay_link": "https://www.ebay.com/sch/i.html?_ssn=theinternationalcargarage&_nkw=range+rover+sport+workshop+manual"},
      {"name": "Discovery Workshop Manual (digital)", "price": "$25.49",
       "description": "Discovery service & repair coverage. Delivered digitally the same day.",
       "ebay_link": "https://www.ebay.com/sch/i.html?_ssn=theinternationalcargarage&_nkw=discovery+workshop+manual"}
    ],
    "ebay_search_url": "https://www.ebay.com/sch/i.html?_ssn=theinternationalcargarage&_nkw=range+rover+workshop+manual",
    "paypal_button_id": "",
    "paypal_button_html": "",
    "direct_price": "$25.49",
    "ebay_price": "$29.99",
    "dvd_addon_price": "$24.99",
    "dvd_button_id": "",
    "dvd_button_html": ""
  },
  "lotus": {
    "brand": "Lotus",
    "slug": "lotus",
    "tagline": "Lotus workshop manuals — Elise & Evora service & repair. Same-day digital delivery.",
    "hero_image": "../assets/brands/lotus/45-elise-workshop-manual.jpg",
    "description_paragraphs": [
      "Enthusiastic Lotus owner? Let experience save you thousands. Shop Service & Repair DIY Compilations is a go-to guide for owners who want to take control of their vehicle maintenance.",
      "With over 20 years of hands-on experience buying, servicing, and repairing Porsches and Lotus vehicles — and Porsche ASE dealer training to back it up — I understand the real cost of European vehicle repairs.",
      "This is the same depth of information a dealer technician works from: thousands of pages of comprehensive build, tear-down, and DIY information, with lifetime access to the material the dealers don't want you to have.",
      "Support independent expertise and help keep our workshop lights on. Empower yourself with the knowledge and confidence to maintain and repair your vehicle, without the dealer-sized bill."
    ],
    "bullets": [
      "Complete Lotus workshop coverage: Elise, Evora and more",
      "Engine, gearbox, suspension, brakes, electrics, bodywork",
      "Parts manuals, service information & manuals, electrical manuals",
      "Fast access to accurate workshop procedures",
      "Verified step-by-step instructions used by professional mechanics",
      "Coverage from routine maintenance to complex diagnostics and repairs",
      "Lifetime access"
    ],
    "gallery": gallery("lotus", os.listdir(os.path.join(ASSETS, "lotus"))),
    "products": [
      {"name": "Lotus Elise Workshop Manual (digital)", "price": "$25.49",
       "description": "Complete Elise service & repair coverage. Delivered digitally the same day.",
       "ebay_link": "https://www.ebay.com/sch/i.html?_ssn=theinternationalcargarage&_nkw=lotus+elise+workshop+manual"},
      {"name": "Lotus Evora Workshop Manual (digital)", "price": "$25.49",
       "description": "Complete Evora service & repair coverage. Delivered digitally the same day.",
       "ebay_link": "https://www.ebay.com/sch/i.html?_ssn=theinternationalcargarage&_nkw=lotus+evora+workshop+manual"}
    ],
    "ebay_search_url": "https://www.ebay.com/sch/i.html?_ssn=theinternationalcargarage&_nkw=lotus+workshop+manual",
    "paypal_button_id": "",
    "paypal_button_html": "",
    "direct_price": "$25.49",
    "ebay_price": "$29.99",
    "dvd_addon_price": "$24.99",
    "dvd_button_id": "",
    "dvd_button_html": ""
  },
  "aston-martin": {
    "brand": "Aston Martin",
    "slug": "aston-martin",
    "tagline": "Aston Martin workshop manuals — V8 Vantage service & repair. Same-day digital delivery.",
    "hero_image": "../assets/brands/aston-martin/41-aston-martin-engine-manual.jpg",
    "description_paragraphs": [
      "Enthusiastic Aston Martin owner? Let experience save you thousands. Shop Service & Repair DIY Compilations is a go-to guide for owners who want to take control of their vehicle maintenance.",
      "With over 20 years of hands-on experience buying, servicing, and repairing European vehicles — and ASE dealer training to back it up — I understand the real cost of keeping an Aston Martin on the road.",
      "This is the same depth of information a dealer technician works from: thousands of pages of comprehensive build, tear-down, and DIY information — service schedules, torque specs, wiring diagrams, diagnostic procedures and full rebuild coverage.",
      "Support independent expertise and help keep our workshop lights on. Empower yourself with the knowledge and confidence to maintain and repair your vehicle, without the dealer-sized bill."
    ],
    "bullets": [
      "Aston Martin workshop coverage, including the 4.7 V8 engine & service guide",
      "Engine, gearbox, suspension, brakes, electrics, bodywork",
      "Parts manuals, service information & manuals, electrical manuals",
      "Fast access to accurate workshop procedures",
      "Verified step-by-step instructions used by professional mechanics",
      "Coverage from routine maintenance to complex diagnostics and repairs",
      "Lifetime access"
    ],
    "gallery": gallery("aston-martin", os.listdir(os.path.join(ASSETS, "aston-martin"))),
    "products": [
      {"name": "Aston Martin V8 Workshop Manual (digital)", "price": "$25.49",
       "description": "Aston Martin 4.7 V8 workshop manual & service guide. Delivered digitally the same day.",
       "ebay_link": "https://www.ebay.com/sch/i.html?_ssn=theinternationalcargarage&_nkw=aston+martin+workshop+manual"}
    ],
    "ebay_search_url": "https://www.ebay.com/sch/i.html?_ssn=theinternationalcargarage&_nkw=aston+martin+workshop+manual",
    "paypal_button_id": "",
    "paypal_button_html": "",
    "direct_price": "$25.49",
    "ebay_price": "$29.99",
    "dvd_addon_price": "$24.99",
    "dvd_button_id": "",
    "dvd_button_html": ""
  }
}

for slug, data in brands.items():
    with open(os.path.join(BR, slug + '.json'), 'w') as f:
        json.dump(data, f, indent=2)
    print('wrote', slug + '.json', '-', len(data['gallery']), 'images,', len(data['products']), 'products')
