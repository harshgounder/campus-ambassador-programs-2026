import tempfile
import unittest
from pathlib import Path

from scripts.validate_archive import validate_csv


class CsvHeaderTests(unittest.TestCase):
    def test_accepts_utf8_bom_and_named_columns(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "valid.csv"
            path.write_text("\ufeffname,region\nAda,India\n", encoding="utf-8")

            row_count, issues = validate_csv(path)

        self.assertEqual(row_count, 1)
        self.assertEqual(issues, [])

    def test_reports_duplicate_header_names(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.csv"
            path.write_text("name,name\nAda,India\n", encoding="utf-8")

            _, issues = validate_csv(path)

        self.assertIn("duplicate header name 'name'", issues[0])

    def test_reports_empty_header_names(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "empty-name.csv"
            path.write_text("name,\nAda,India\n", encoding="utf-8")

            _, issues = validate_csv(path)

        self.assertIn("empty header name at column 2", issues[0])

    def test_reports_file_without_header(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "empty.csv"
            path.write_text("", encoding="utf-8")

            row_count, issues = validate_csv(path)

        self.assertEqual(row_count, 0)
        self.assertEqual(issues, ["empty.csv: file has no header row"])
