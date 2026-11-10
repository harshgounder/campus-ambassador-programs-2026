import csv
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
]


def get(t):
    try:
        r = requests.get(
            "https://huggingface.co/api/models?limit=1000&sort=downloads&direction=-1&pipeline_tag="
            + t,
            headers=UA,
            timeout=45,
        )
        return t, r.json()
    except Exception:
        return t, []


rows = {}
with ThreadPoolExecutor(max_workers=8) as ex:
    for t, d in ex.map(get, TAGS):
        for m in d:
            mid = m.get("id", "")
            if "/" not in mid:
                continue
            a = mid.split("/")[0]
            k = a.lower()
            if k not in rows:
                rows[k] = {
                    "name": a,
                    "handle": a,
                    "source": "huggingface",
                    "kind": "org",
                    "category": "hf:" + t,
                    "url": "https://huggingface.co/" + a,
                    "metric": 0,
                    "cats": set(),
                }
            rows[k]["cats"].add("hf:" + t)
            dl = int(m.get("downloads") or 0)
            if dl > int(rows[k]["metric"]):
                rows[k]["metric"] = dl
        print(t, len(d), len(rows))
        sys.stdout.flush()
out = []
for v in rows.values():
    v["cats"] = ";".join(sorted(v["cats"]))
    out.append(v)
out.sort(key=lambda x: -int(x["metric"]))
with open("data/ai-hf.csv", "w", newline="") as f:
    w = csv.DictWriter(
        f, fieldnames=["name", "handle", "source", "kind", "category", "url", "metric", "cats"]
    )
    w.writeheader()
    w.writerows(out)
print("TOTAL", len(out))
