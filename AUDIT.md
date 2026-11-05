# Audit of the "1,684 of 4,866" claim

Run 5 November 2026, after the user asked whether the number was real.

## Verdict

The number was real when reported and stale by the time of the audit. It was the count of
processed names, not of covered names. Those are different things and the difference matters.

## Raw evidence

| check | result |
|---|---|
| lines in `resolve2_done.txt` | 3,216 at audit time |
| rows in `resolve2.jsonl` | 3,216 |
| unique names in JSONL | 3,216 |
| names in done but not in JSONL | 0 |
| names in JSONL but not in done | 0 |
| duplicate rows | 0 |
| done names outside the census org tier | 0 |

So the log and the data agree exactly. Nothing was invented.

## Why the number moved

The resolver was still running when the audit started. It processed 1,684 at the moment of the
report and 3,216 by the audit, 34 minutes later. Both numbers are correct for their timestamp.

## Processed is not covered

- Processed: the resolver attempted a domain guess and wrote a row.
- Covered: a real site was found and its ambassador paths were probed, ending in NONE or FOUND.

| measure | value |
|---|---|
| census org-tier | 5,745 |
| covered | 1,385 (24.1%) |
| processed in resolver v2 | 3,216 |
| resolved sites in v2 | 506 |
| unresolved in v2 | 2,710 |

So 3,216 processed produced only 506 new covered sites, because domain guessing fails for most
names. The 4,866 denominator was also stale; the current uncovered count is 4,360.

## Search resolution attempt

A DuckDuckGo HTML resolver was started to find sites for the unresolved names. DuckDuckGo
returned 202 and no results after the first few queries, and 8 of 8 processed names came back
UNRESOLVED. Automated search without an API is not viable here.

The honest options are a paid search API in batches, or accepting that names with no public
site cannot be checked.

## What this audit changes

- The coverage number is 24.1%, not 34% or whatever "3,216 of 4,866" sounds like.
- The lie detector's coverage failure remains correct.
- Any future number must say processed or covered, never just a fraction.
