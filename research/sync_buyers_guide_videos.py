#!/usr/bin/env python3
"""APPROVED by Peter 2026-10-07 — successor to the retired
buyers-guide-video-sync cron (removed after its final run on 2026-10-05).

Same as sync_buyers_guide_videos.py, plus: titles mentioning "aston martin"
go to the Aston Martin brand page (brands/aston-martin.json, already live on
the site). Skips the follow-bounce outro and any title matching an already
listed video ID (idempotent, as before).

Proposed schedule: daily@21:08 ET (same slot as the retired job).
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

SKIP_PATTERNS = ("follow bounce", "outro")


def slug_for_title(tl: str):
    if any(p in tl for p in SKIP_PATTERNS):
        return None
    if "l322" in tl:
        return "range-rover"
    if "aston martin" in tl:
        return "aston-martin"
    if "996" in tl:
        return "porsche"
    return None


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
        slug = slug_for_title(title.lower())
        if not slug:
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
