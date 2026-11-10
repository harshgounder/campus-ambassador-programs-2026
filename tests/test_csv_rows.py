import tempfile
import unittest
from pathlib import Path

from scripts.validate_archive import validate_csv


class CsvRowTests(unittest.TestCase):
    def test_counts_data_rows_and_ignores_blank_lines(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.csv"
            path.write_text('name,note\nAda,"quoted, value"\n\nLin,plain\n', encoding="utf-8")

            row_count, issues = validate_csv(path)

        self.assertEqual(row_count, 2)
        self.assertEqual(issues, [])

    def test_reports_short_and_long_rows(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "ragged.csv"
            path.write_text("name,region\nAda\nLin,India,extra\n", encoding="utf-8")

            row_count, issues = validate_csv(path)

        self.assertEqual(row_count, 2)
        self.assertEqual(len(issues), 2)
        self.assertIn("row 2 has 1 columns; expected 2", issues[0])
        self.assertIn("row 3 has 3 columns; expected 2", issues[1])

    def test_reports_malformed_csv_quotes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "malformed.csv"
            path.write_text('name,note\nAda,"never closed\n', encoding="utf-8")

            _, issues = validate_csv(path)

        self.assertIn("could not parse CSV", issues[0])
