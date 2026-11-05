# Checker

You asked for a way to catch me skipping instructions. This is it. It reads the artifacts on
disk, not my summary.

## Run it

```bash
cd ~/campus-ambassador-hunt
python3 scripts/check.py
```

Exit code 0 means every required artifact exists and is above the size floor. Exit code 1 means
at least one line says FAIL, and the failed line names the file or the count.

## What it checks

| check | why it exists |
|---|---|
| scope file exists | the taxonomy has to be written before the list |
| 20+ categories defined | a scope with 5 buckets is not a scope |
| master list 400+ orgs | stops me returning 40 names and calling it a list |
| every scope category appears in the list | stops silent gaps like "I forgot robotics" |
| every row has a country | the country split was an explicit instruction |
| every category has 5+ entries | stops one token entry per category |
| 20+ countries represented | stops a US-only list |
| registry 150+ programs | stops a thin program list |
| registry has OPEN rows | a list with nothing open is not an answer |
| registry has India-eligible rows | the applicant is in India |
| reports and universe exist | the readable and raw layers both have to be there |
| waves tracker exists | the plan of record, so a skipped wave is visible |

## Instruction to artifact map

| what you asked | where it lives | checked |
|---|---|---|
| define categories first | `scope/SCOPE-AI.md` | yes, 24 codes |
| list every company under each category | `data/master-ai.csv` | yes, 486 rows |
| all countries and regions, plus global | country column, 34 values | yes |
| big global list | `data/ai-universe.csv`, 13,981 rows | yes, floor 10,000 |
| then check campus ambassador programs | `data/registry.csv`, `REPORT.md` | yes, 174 rows |
| open now or soon | status column | yes |
| for us in India | region column and `scope/PROFILE.md` | yes |
| do not skip waves | `WAVES.md` | yes |

## Rule

If the checker prints any FAIL, do not accept the answer. The failed line tells you which
instruction was skipped. If it prints all PASS but the content still looks thin, the floors are
too low and they should be raised, which is a one-line edit in `scripts/check.py`.
