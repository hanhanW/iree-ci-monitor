#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path


def load_collect_module():
    collect_path = Path(__file__).with_name("collect.py")
    spec = importlib.util.spec_from_file_location("collect", collect_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["collect"] = module
    spec.loader.exec_module(module)
    return module


class CollectSnapshotTest(unittest.TestCase):
    def test_queued_snapshots_are_not_deduped(self):
        collect = load_collect_module()
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "day.jsonl"
            path.write_text(
                json.dumps(
                    {
                        "job_id": 1,
                        "run_attempt": 1,
                        "status": "queued",
                    }
                )
                + "\n"
                + json.dumps(
                    {
                        "job_id": 2,
                        "run_attempt": 1,
                        "status": "completed",
                    }
                )
                + "\n"
            )

            keys = collect.existing_keys_for_day(path)

        self.assertNotIn((1, 1, "queued"), keys)
        self.assertIn((2, 1, "completed"), keys)

    def test_normalize_job_records_collection_time(self):
        collect = load_collect_module()
        collected_at = datetime(2026, 5, 12, 23, 1, 2, tzinfo=timezone.utc)
        job = {
            "id": 1,
            "run_id": 2,
            "run_attempt": 1,
            "name": "job",
            "labels": ["Linux"],
            "status": "queued",
            "created_at": "2026-05-12T23:00:00Z",
            "started_at": "2026-05-12T23:00:00Z",
        }
        run = {
            "workflow_id": 3,
            "name": "CI",
            "path": ".github/workflows/ci.yml",
            "html_url": "https://example.test/run/2",
            "head_sha": "abcdef1234567890",
            "head_commit": {"message": "Tune SDXL clip dispatch\n\nMore details."},
            "event": "pull_request",
            "head_branch": "branch",
        }

        rec = collect.normalize_job(job, run, collected_at)

        self.assertEqual(rec["collected_at"], "2026-05-12T23:01:02Z")
        self.assertEqual(rec["workflow_path"], ".github/workflows/ci.yml")
        self.assertEqual(rec["run_html_url"], "https://example.test/run/2")
        self.assertEqual(rec["head_sha"], "abcdef1234567890")
        self.assertEqual(rec["commit_message"], "Tune SDXL clip dispatch\n\nMore details.")


if __name__ == "__main__":
    unittest.main()
