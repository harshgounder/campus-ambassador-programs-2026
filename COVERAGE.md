# Coverage, audited 5 November 2026 14:50 IST

Six passes merged: initial scan, domain resolver v1, v2, DuckDuckGo, SearXNG, Parallel AI.

## Denominator

5,745 org-tier names in `data/ai-orgs-census.csv`.

## Result

| measure | value |
|---|---|
| names with at least one result row | **5,745 (100%)** |
| **covered: a real site was found and probed** | **2,526 (44.0%)** |
| not covered | 3,219 |

## What blocks the remaining 3,219

| status | count | meaning |
|---|---|---|
| UNRESOLVED | 1,105 | no site found by any method |
| UNREACHABLE | 912 | site found but blocked bots, DNS or timeout |
| UNVERIFIED | 910 | site found but the name was not confirmed on the page |
| NO_SITE | 292 | no domain guess at all |

## FOUND rows

42 raw hits across all passes. 28 survived content validation (word ambassador twice plus an
apply or join keyword). After deduplication and domain matching, about 15 unique programs,
almost all already in the registry: Kiro, Anthropic campus, Cursor, Datadog, ElevenLabs,
Solace, Ultralytics, CAMEL-AI, Edge Impulse, Firecrawl, Fish Audio, Marimo, MLflow, TinyFish.
Rejected: linktr.ee and ko-fi pages, a Microsoft student page matched for intfloat, a personal
music site.

## Spend

Parallel AI: about 2,450 searches at roughly $0.001 each, so about **$2.45 so far**, projected
**$4.30** for the full 4,322.

## Honest summary

Every name has a row. 44% have a real site probed. The rest need a browser retry for the
unreachable, a manual look for the unverified, and either a search or an accepted gap for the
unresolved. 44% is the number, not 100%.
