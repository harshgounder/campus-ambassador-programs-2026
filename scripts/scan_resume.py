import csv
import json
import os
import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

import requests

UA = {"User-Agent": "Mozilla/5.0 Chrome/131.0"}
try:
    TOK = subprocess.run(
        ["gh", "auth", "token"], capture_output=True, text=True, timeout=10
    ).stdout.strip()
except Exception:
    TOK = ""
GH = {"Authorization": "Bearer " + TOK, "Accept": "application/vnd.github+json"} if TOK else {}
SKIP = (
    "huggingface.co",
    "hf.co",
    "github.com",
    "x.com",
    "twitter.com",
    "linkedin.com",
    "discord",
    "youtube.com",
    "t.me",
    "medium.com",
    "reddit.com",
    "apply.workable.com",
)
PROBE = [
    "/ambassador",
    "/ambassadors",
    "/ambassador-program",
    "/campus",
    "/campus-ambassador",
    "/students",
    "/student-ambassador",
    "/community/ambassadors",
]
DONE = "data/scan_processed.txt"
done = set(open(DONE).read().split("\n")) if os.path.exists(DONE) else set()


def ext(html):
    out = []
    for m in re.finditer(r'href="(https?://[^"]+)"', html):
        d = urlparse(m.group(1)).netloc.lower().replace("www.", "")
        if any(s in d for s in SKIP):
            continue
        out.append("https://" + d)
    return list(dict.fromkeys(out))


def site(r):
    n = r["handle"]
    if "huggingface" in r["sources"]:
        try:
            x = requests.get("https://huggingface.co/" + n, headers=UA, timeout=10)
            links = ext(x.text)
            return links[0] if links else ""
        except Exception:
            return ""
    if "github" in r["sources"] and GH:
        try:
            x = requests.get("https://api.github.com/users/" + n, headers=GH, timeout=10)
            b = x.json().get("blog") or ""
            return b if b.startswith("http") else ("https://" + b if b else "")
        except Exception:
            return ""
    return ""


def probe(s):
    hits = []
    for p in PROBE:
        try:
            x = requests.get(s.rstrip("/") + p, headers=UA, timeout=7, allow_redirects=True)
            if x.status_code == 200:
                t = re.search(r"<title[^>]*>(.*?)</title>", x.text, re.S | re.I)
                title = t.group(1).strip()[:120] if t else ""
                if (
                    re.search(r"ambassador|campus|student", title + x.url, re.I)
                    and "apache" not in title.lower()
                ):
                    hits.append({"url": x.url, "title": title})
        except Exception:
            pass
    return hits


rows = [r for r in csv.DictReader(open("data/ai-notable.csv")) if r["handle"] not in done]
print("remaining", len(rows))
sys.stdout.flush()
out = open("data/scan_hits2.jsonl", "a")
log = open(DONE, "a")


def work(r):
    s = site(r)
    h = probe(s) if s else []
    return r["name"], s, h


n = 0
with ThreadPoolExecutor(max_workers=14) as ex:
    for f in as_completed([ex.submit(work, r) for r in rows]):
        n += 1
        try:
            name, s, h = f.result()
        except Exception:
            continue
        log.write(name + "\n")
        log.flush()
        if h:
            out.write(json.dumps({"name": name, "site": s, "hits": h}) + "\n")
            out.flush()
        if n % 100 == 0:
            print("done", n)
            sys.stdout.flush()
print("FINISHED", n)
