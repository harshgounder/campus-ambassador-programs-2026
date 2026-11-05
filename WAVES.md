# Waves, so nothing gets skipped

Each wave has a definition of done. The checker reads the artifacts, not my word.

| wave | scope | artifacts | status |
|---|---|---|---|
| 1 | AI maker universe, 3 sources | data/ai-universe.csv, data/ai-hf.csv, data/ai-gh.csv, data/ai-curated.csv | DONE 4 Nov |
| 2 | Taxonomy and categorized master list | scope/SCOPE-AI.md, data/master-ai.csv | DONE 5 Nov |
| 3 | Ambassador programs, corporate layer | data/registry.csv, REPORT.md | DONE, 174 rows |
| 4 | Ambassador programs, X and Web3 layer | REPORT.md section, registry rows | DONE, 31 rows |
| 5 | Ambassador scan of the notable 1,097 | data/scan_hits.jsonl, data/scan_hits2.jsonl | DONE 5 Nov, 1,096 of 1,097 processed |
| 6 | Country by country program check | registry region column | INDIA, CHINA, MENA, AFRICA, SEA, LATAM DONE 5 Nov |
| 7 | Open vs soon vs closed recheck at one date | registry status column, last_checked | DONE 5 Nov, 199 rows, 6 status corrections |
| 8 | India eligibility filter for a 2nd year ECE at MUJ | scope/PROFILE.md | PARTIAL |
| 9 | Applied tracker with deadlines and logins | data/tracker.csv | STARTED 5 Nov, 97 open rows |

## Definition of done per wave

- Wave 5 is done when 1,097 of 1,097 have been scanned and every hit has a verified status.
- Wave 6 is done when every country with 5+ orgs in the master list has had its orgs checked for a program.
- Wave 9 is done when every OPEN row has a tracker line with deadline, link and applied yes/no.

| 10 | Check all 4,252 org-tier names one by one | data/scan3758.jsonl | FAILED COVERAGE 5 Nov: 192 of 4,252 reachable and checked, 2,412 no website, 1,359 unreachable, 289 missing |
