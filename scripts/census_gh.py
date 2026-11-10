import csv
import json
import subprocess
import sys

TOPICS = [
    "llm",
    "llm-inference",
    "ai-agents",
    "rag",
    "text-to-image",
    "diffusion-models",
    "world-models",
    "speech-recognition",
    "vector-database",
    "mcp",
    "agent-framework",
    "fine-tuning",
    "llmops",
    "evaluation",
    "guardrails",
    "embeddings",
    "multimodal",
    "vision-language-model",
    "model-serving",
    "prompt-engineering",
    "ai-gateway",
    "observability",
    "dataset",
    "inference-engine",
    "local-llm",
    "text-to-speech",
    "image-generation",
    "video-generation",
    "ai",
    "machine-learning",
    "deep-learning",
    "transformers",
    "generative-ai",
    "chatbot",
    "llmops",
    "ai-safety",
    "robotics",
    "autonomous-vehicles",
    "speech-synthesis",
    "ocr",
    "recommendation-system",
    "knowledge-graph",
    "synthetic-data",
    "reinforcement-learning",
    "computer-vision",
    "nlp",
    "ai-tools",
    "ai-assistant",
    "openai",
    "claude",
]
rows = {}
for t in TOPICS:
    try:
        out = subprocess.run(
            [
                "gh",
                "search",
                "repos",
                "--topic",
                t,
                "--limit",
                "1000",
                "--json",
                "owner,stargazersCount",
            ],
            capture_output=True,
            text=True,
            timeout=120,
        )
        d = json.loads(out.stdout or "[]")
    except Exception as e:
        print("fail", t, e)
        continue
    for r in d:
        o = r.get("owner") or {}
        login = o.get("login") or ""
        if not login:
            continue
        k = login.lower()
        if k not in rows:
            rows[k] = {"name": login, "topics": set(), "stars": 0, "kind": o.get("type", "")}
        rows[k]["topics"].add(t)
        rows[k]["stars"] = max(rows[k]["stars"], int(r.get("stargazersCount") or 0))
    print("gh", t, len(d), len(rows))
    sys.stdout.flush()
out = []
for v in rows.values():
    v["topics"] = ";".join(sorted(v["topics"]))
    out.append(v)
out.sort(key=lambda x: -x["stars"])
with open("data/census-gh.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["name", "topics", "stars", "kind"])
    w.writeheader()
    w.writerows(out)
print("GH OWNERS", len(out))
