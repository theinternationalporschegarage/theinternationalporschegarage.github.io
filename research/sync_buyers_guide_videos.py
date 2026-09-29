#!/usr/bin/env python3
"""Daily sync: add new 996 / L322 buyers-guide YouTube uploads to brand pages.

Reads the garage channel RSS feed, picks up videos published in the last
WINDOW_HOURS whose title mentions 996 (Porsche page) or L322 (Range Rover
page), appends them to the brand JSON `videos` arrays, re-renders the pages,
and pushes to GitHub Pages. Idempotent: skips video IDs already present.
"""
import json
import os
import subprocess
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHANNEL_ID = "UCKsRwFcj86LNMTGWlxOBOGw"  # @Theinternationalporsche
FEED = f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
WINDOW_HOURS = 30


def main():
    with urllib.request.urlopen(FEED, timeout=30) as r:
        xml = r.read()
    ns = {"a": "http://www.w3.org/2005/Atom",
          "y": "http://www.youtube.com/xml/schemas/2015"}
    root = ET.fromstring(xml)
    cutoff = datetime.now(timezone.utc) - timedelta(hours=WINDOW_HOURS)
    added = []
    for e in root.findall("a:entry", ns):
        vid = e.find("y:videoId", ns).text
        title = (e.find("a:title", ns).text or "").strip()
        pub = datetime.fromisoformat(
            e.find("a:published", ns).text.replace("Z", "+00:00"))
        if pub < cutoff:
            continue
        tl = title.lower()
        if "l322" in tl:
            slug = "range-rover"
        elif "996" in tl:
            slug = "porsche"
        else:
            continue
        jp = os.path.join(BASE, "brands", slug + ".json")
        d = json.load(open(jp))
        if any(v.get("id") == vid for v in d.get("videos", [])):
            continue
        d.setdefault("videos", []).append({"id": vid, "title": title})
        json.dump(d, open(jp, "w"), indent=2)
        added.append((slug, vid, title))
    if not added:
        print("no new buyers-guide videos")
        return
    subprocess.run([sys.executable,
                    os.path.join(BASE, "research", "render_brand_pages.py")],
                   check=True, cwd=BASE)
    push = subprocess.run(
        [sys.executable,
         os.path.expanduser("~/workspace/skills/github/bin/github_sync.py"),
         "theinternationalporschegarage/theinternationalporschegarage.github.io",
         BASE,
         "--exclude", "research",
         "--exclude", "BUILD_NOTES.md",
         "--exclude", "assets/brands/porsche/36-macan-sale-badge.jpg",
         "--message", "Sync new buyers-guide videos to brand pages"],
        capture_output=True, text=True, cwd=BASE)
    print(push.stdout[-1500:])
    if push.returncode != 0:
        print(push.stderr[-1500:])
        sys.exit(1)
    for slug, vid, title in added:
        print(f"ADDED {slug}: {vid} — {title}")


if __name__ == "__main__":
    main()
