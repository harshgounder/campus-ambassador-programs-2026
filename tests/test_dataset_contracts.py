import csv
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_csv(path):
    with (ROOT / path).open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames, list(reader)


class DatasetContractTests(unittest.TestCase):
    def test_program_registry_keeps_required_review_fields(self):
        headers, rows = read_csv("data/registry.csv")

        self.assertTrue({"name", "status", "deadline", "apply_url", "last_checked"} <= set(headers))
        self.assertGreater(len(rows), 0)
        self.assertTrue(all(row["name"].strip() and row["status"].strip() for row in rows))

    def test_application_tracker_has_submission_and_follow_up_fields(self):
        headers, rows = read_csv("data/tracker.csv")

        self.assertTrue({"program", "applied", "notes", "last_checked"} <= set(headers))
        self.assertGreater(len(rows), 0)
        self.assertTrue(all(row["program"].strip() for row in rows))

    def test_ai_priority_ledger_has_status_fit_and_evidence_fields(self):
        path = "research/2026-11-09/outputs/ai-ml-priority-verification-delta-2026-11-09.csv"
        headers, rows = read_csv(path)

        self.assertTrue(
            {
                "program",
                "opportunity_type",
                "status_as_of_2026_11_09",
                "geography_and_eligibility",
                "fit_for_MUJ_ECE_2029",
                "official_evidence_urls",
                "dedupe_and_uncertainty",
            }
            <= set(headers)
        )
        self.assertGreater(len(rows), 0)
