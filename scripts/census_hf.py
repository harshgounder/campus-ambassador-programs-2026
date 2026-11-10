import csv
import itertools
import sys
from concurrent.futures import ThreadPoolExecutor

import requests

UA = {"User-Agent": "Mozilla/5.0"}
TAGS = [
    "text-generation",
    "text-to-image",
    "text-to-video",
    "image-text-to-text",
    "automatic-speech-recognition",
    "text-to-speech",
    "feature-extraction",
    "image-classification",
    "object-detection",
    "image-segmentation",
    "depth-estimation",
    "video-classification",
    "audio-classification",
    "translation",
    "summarization",
    "question-answering",
    "fill-mask",
    "sentence-similarity",
    "reranking",
    "text-to-audio",
    "any-to-any",
    "robotics",
    "reinforcement-learning",
    "image-to-image",
    "image-to-video",
    "zero-shot-image-classification",
    "visual-question-answering",
    "document-question-answering",
    "mask-generation",
    "keypoint-detection",
    "zero-shot-object-detection",
    "image-feature-extraction",
    "audio-to-audio",
    "voice-activity-detection",
    "text-to-speech",
    "image-text-retrieval",
    "video-text-to-text",
    "text-to-3d",
    "image-to-3d",
]
SORTS = ["downloads", "likes", "createdAt"]
jobs = list(itertools.product(TAGS, SORTS))


def get(j):
    t, s = j
    try:
        r = requests.get(
            f"https://huggingface.co/api/models?limit=1000&sort={s}&direction=-1&pipeline_tag={t}",
            headers=UA,
            timeout=45,
        )
        return t, s, r.json()
    except Exception:
        return t, s, []


rows = {}
with ThreadPoolExecutor(max_workers=8) as ex:
    for i, (t, s, d) in enumerate(ex.map(get, jobs)):
        for m in d:
            mid = m.get("id", "")
            if "/" not in mid:
                continue
            a = mid.split("/")[0]
            k = a.lower()
            if k not in rows:
                rows[k] = {"name": a, "tags": set(), "downloads": 0, "likes": 0}
            rows[k]["tags"].add(t)
            rows[k]["downloads"] = max(rows[k]["downloads"], int(m.get("downloads") or 0))
            rows[k]["likes"] = max(rows[k]["likes"], int(m.get("likes") or 0))
        if i % 10 == 0:
            print("hf", i, len(rows))
            sys.stdout.flush()
out = []
for v in rows.values():
    v["tags"] = ";".join(sorted(v["tags"]))
    out.append(v)
out.sort(key=lambda x: -x["downloads"])
with open("data/census-hf.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name", "tags", "downloads", "likes"])
    w.writeheader()
    w.writerows(out)
print("HF AUTHORS", len(out))
