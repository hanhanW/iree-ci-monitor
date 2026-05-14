#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path


def load_module():
    path = Path(__file__).with_name("benchmark_collect.py")
    spec = importlib.util.spec_from_file_location("benchmark_collect", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["benchmark_collect"] = module
    spec.loader.exec_module(module)
    return module


class BenchmarkCollectTest(unittest.TestCase):
    def test_normalizes_benchmark_rows_from_job_summary(self):
        collect = load_module()
        summary = {
            "benchmark": {
                "headers": [
                    "Name",
                    "Current Time (ms)",
                    "Golden Time (ms)",
                    "Tolerance Factor",
                    "Threshold (ms)",
                    "Status",
                ],
                "rows": [
                    [
                        "sdxl/clip_benchmark_mi325.json",
                        "7.249",
                        "7.300",
                        "1.1",
                        "8.030",
                        "PASSED",
                    ]
                ],
            }
        }
        run = {
            "run_id": 25753418567,
            "run_html_url": "https://example.test/run",
            "workflow_name": "PkgCI",
            "workflow_path": ".github/workflows/pkgci.yml",
            "head_branch": "main",
            "event": "push",
            "head_sha": "abcdef1234567890",
            "commit_message": "Tune SDXL clip dispatch\n\nMore details.",
            "run_attempt": 2,
            "created_at": "2026-05-12T18:14:32Z",
        }
        artifact = {
            "id": 6952717694,
            "name": "torch_models_amdgpu_mi325_summary.json",
            "created_at": "2026-05-12T18:36:43Z",
        }
        records = collect.normalized_records_from_summary(
            summary,
            run=run,
            artifact=artifact,
            collected_at=datetime(2026, 5, 14, tzinfo=timezone.utc),
        )

        self.assertEqual(len(records), 1)
        rec = records[0]
        self.assertEqual(rec["name"], "sdxl/clip_benchmark_mi325.json")
        self.assertEqual(rec["current_time_ms"], 7.249)
        self.assertEqual(rec["golden_time_ms"], 7.3)
        self.assertEqual(rec["threshold_ms"], 8.03)
        self.assertEqual(rec["status"], "PASSED")
        self.assertEqual(rec["head_sha"], "abcdef1234567890")
        self.assertEqual(rec["commit_message"], "Tune SDXL clip dispatch\n\nMore details.")
        self.assertEqual(rec["run_attempt"], 2)
        self.assertEqual(rec["artifact_name"], "torch_models_amdgpu_mi325_summary.json")

    def test_existing_artifact_ids_reads_all_benchmark_jsonl_files(self):
        collect = load_module()
        with tempfile.TemporaryDirectory() as td:
            data_dir = Path(td) / "benchmarks"
            day = data_dir / "2026" / "05" / "13.jsonl"
            day.parent.mkdir(parents=True)
            day.write_text(
                json.dumps({"run_id": 1, "artifact_id": 111, "name": "a"}) + "\n"
                + json.dumps({"run_id": 2, "artifact_id": 222, "name": "b"}) + "\n"
            )

            self.assertEqual(collect.existing_artifact_ids(data_dir), {111, 222})

    def test_paginate_follows_next_links(self):
        collect = load_module()
        calls = []

        def fake_response(path_or_url, params=None, raw=False):
            calls.append((path_or_url, params, raw))
            if len(calls) == 1:
                return (
                    {"artifacts": [{"id": 1}]},
                    {"link": '<https://api.github.test/page/2>; rel="next"'},
                )
            return ({"artifacts": [{"id": 2}]}, {})

        collect.gh_response = fake_response

        self.assertEqual(
            list(collect.paginate("/repos/example/actions/runs/1/artifacts")),
            [{"id": 1}, {"id": 2}],
        )
        self.assertEqual(calls[1][0], "https://api.github.test/page/2")


if __name__ == "__main__":
    unittest.main()
