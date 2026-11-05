# What "covered" actually means, audited 5 November 2026

You asked what the 3,962 covered names are, whether they follow depth, and how they are
distributed. This is the answer, including the parts that are weak.

## The mechanical definition

A name is "covered" when a site was found for it and at least four paths were fetched:
`/ambassador`, `/ambassadors`, `/campus`, `/students`. If none of those pages contained the
word ambassador twice plus an apply or join or program keyword, the row is RESOLVED. If the
site itself had no reachable page, it is UNREACHABLE. If no site was found, UNRESOLVED.

Covered = RESOLVED + NONE + FOUND.

## Distribution by pass

| pass | covered rows | paths probed |
|---|---|---|
| Parallel AI search | 1,371 | 4 |
| domain resolver v2 | 733 | 4 |
| browser retry | 616 | 4 |
| domain resolver v1 | 496 | 4 |
| initial HF/GitHub scan | 350 | 7 |
| unverified domain match | 279 | 4 |
| SearXNG | 120 | 4 |

Only 350 of 3,965 were probed with the 7-path version. The rest got 4 paths. None got a
JavaScript render, a form submission, or a `/community` and `/careers` check.

## Distribution by substance

| measure | count | share |
|---|---|---|
| covered | 3,965 | 100% |
| domain matches the name | 3,154 | 79.5% |
| domain does not match | 811 | 20.5% |
| zero downloads, GitHub-only | 3,502 | 88.3% |
| substantive: curated or 100k+ downloads | 846 | 21.3% |
| substantive AND domain-verified | **738** | **18.6%** |

So the deep, trustworthy coverage is **738 names**, not 3,962. The rest is breadth.

## Distribution by category

| category | total | covered | pct |
|---|---|---|---|
| other (tooling, GitHub) | 4,467 | 3,122 | 69.9% |
| audio | 239 | 154 | 64.4% |
| text generation | 212 | 134 | 63.2% |
| reinforcement learning | 192 | 117 | 60.9% |
| robotics | 187 | 136 | 72.7% |
| image | 122 | 80 | 65.6% |
| multimodal | 109 | 74 | 67.9% |
| embeddings | 90 | 60 | 66.7% |
| NLP | 39 | 29 | 74.4% |
| vision | 34 | 24 | 70.6% |
| classification | 23 | 15 | 65.2% |
| video | 21 | 14 | 66.7% |
| 3D | 10 | 6 | 60.0% |

Every category sits between 60 and 75 percent, but the volume is dominated by "other",
which is GitHub tool owners, not labs.

## The 811 domain mismatches

Some are legitimate brand aliases: `meta-llama` to `ai.meta.com`, `sentence-transformers` to
`sbert.net`, `Baidu ERNIE` to `ernie.baidu.com`, `iFlytek Spark` to `xfyun.cn`, `Naver` to
`clova.ai`, `Apple OpenELM` to `machinelearning.apple.com`.

Some are plainly wrong and invalidate the row:
- `openai` to `open.com`
- `inclusionAI` to `kizunaai.com`
- `fireworks-ai` to `socials.fru.dev`
- `simaai` to `sima.com`
- `NousResearch` to `nous.io` (real site is nousresearch.com)

Those need correction, not defence.

## Verdict

The 3,962 is real as breadth: a site was fetched and four paths were probed. It is not depth:
738 names are substantive and domain-verified, 811 domains are questionable, 88% have zero
downloads, and no pass rendered JavaScript or checked more than seven paths.

The number to quote for depth is **738**, and the number to quote for breadth is **3,962**.
