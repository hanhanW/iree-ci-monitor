#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path


def load_dashboard_module():
    dashboard_path = Path(__file__).with_name("dashboard.py")
    spec = importlib.util.spec_from_file_location("dashboard", dashboard_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["dashboard"] = module
    spec.loader.exec_module(module)
    return module


class DashboardDataTest(unittest.TestCase):
    def test_dashboard_prefers_actual_benchmark_result_rows(self):
        dashboard = load_dashboard_module()
        now = datetime(2026, 5, 14, tzinfo=timezone.utc)

        with tempfile.TemporaryDirectory() as td:
            data_dir = Path(td) / "data"
            day = data_dir / "benchmarks" / "2026" / "05" / "13.jsonl"
            day.parent.mkdir(parents=True)
            day.write_text(
                json.dumps(
                    {
                        "run_id": 25753418567,
                        "run_html_url": "https://example.test/run",
                        "workflow_name": "PkgCI",
                        "workflow_path": ".github/workflows/pkgci.yml",
                        "head_branch": "main",
                        "event": "push",
                        "head_sha": "abcdef1234567890",
                        "commit_message": "Tune SDXL clip dispatch (#12345)\n\nMore details.",
                        "run_created_at": "2026-05-13T01:00:00Z",
                        "artifact_id": 6952717694,
                        "artifact_name": "torch_models_amdgpu_mi325_summary.json",
                        "artifact_created_at": "2026-05-13T01:20:00Z",
                        "section": "benchmark",
                        "name": "sdxl/clip_benchmark_mi325.json",
                        "current_time_ms": 7.249,
                        "golden_time_ms": 7.3,
                        "threshold_ms": 8.03,
                        "tolerance_factor": 1.1,
                        "status": "PASSED",
                    }
                )
                + "\n"
            )
            (data_dir / "benchmark_suites.json").write_text(
                json.dumps(
                    {
                        "generated_at": "2026-05-14T00:00:00Z",
                        "suite_root_url": "https://example.test/suites",
                        "suites": [
                            {
                                "name": "torch_models",
                                "html_url": "https://example.test/torch",
                                "configs": [
                                    {
                                        "path": "sdxl/clip_benchmark_mi325.json",
                                        "name": "clip_benchmark_mi325.json",
                                        "kind": "benchmark",
                                    }
                                ],
                            },
                            {
                                "name": "sharktank_models",
                                "html_url": "https://example.test/sharktank",
                                "configs": [
                                    {
                                        "path": "benchmarks/sdxl/clip_rocm.json",
                                        "name": "clip_rocm.json",
                                        "kind": "benchmark",
                                    }
                                ],
                            },
                        ],
                    }
                )
                + "\n"
            )

            data = dashboard.build_dashboard_data(now, lookback_days=7, data_dir=data_dir)

        self.assertEqual(data["metric_contract"]["current_level"], "benchmark_result")
        self.assertEqual(data["metric_contract"]["metrics"][0], "current_time_ms")
        self.assertEqual(data["summary"]["points"], 1)
        point = data["points"][0]
        self.assertEqual(point["benchmark"], "sdxl/clip_benchmark_mi325.json")
        self.assertEqual(point["labels_key"], "torch_models_amdgpu_mi325")
        self.assertEqual(point["current_time_ms"], 7.249)
        self.assertEqual(point["commit_short"], "abcdef123456")
        self.assertEqual(point["commit_subject"], "Tune SDXL clip dispatch (#12345)")
        self.assertEqual(point["pr_title"], "Tune SDXL clip dispatch")
        self.assertNotIn("pr_number", point)
        self.assertNotIn("pr_url", point)
        self.assertEqual(point["suite"], "torch_models")
        coverage = {row["suite"]: row for row in data["suite_coverage"]}
        self.assertEqual(coverage["torch_models"]["observed_configured_benchmarks"], 1)
        self.assertEqual(coverage["torch_models"]["points"], 1)
        self.assertEqual(coverage["sharktank_models"]["configured_benchmarks"], 1)
        self.assertEqual(coverage["sharktank_models"]["points"], 0)
        self.assertEqual(
            coverage["sharktank_models"]["missing_benchmark_examples"],
            ["benchmarks/sdxl/clip_rocm.json"],
        )

    def test_dashboard_uses_main_pkgci_test_jobs_and_exact_labels(self):
        dashboard = load_dashboard_module()
        now = datetime(2026, 5, 14, tzinfo=timezone.utc)

        with tempfile.TemporaryDirectory() as td:
            data_dir = Path(td) / "data"
            day = data_dir / "2026" / "05" / "13.jsonl"
            day.parent.mkdir(parents=True)
            records = [
                {
                    "run_id": 1,
                    "run_attempt": 1,
                    "job_id": 10,
                    "workflow_id": 671,
                    "workflow_name": "PkgCI",
                    "workflow_path": ".github/workflows/pkgci.yml",
                    "run_html_url": "https://example.test/run/1",
                    "head_sha": "abcdef1234567890",
                    "name": "Test Torch / test_torch_ops :: amdgpu_vulkan_O3",
                    "labels": ["Linux", "X64", "rdna3"],
                    "runner_name": "shark01-ci",
                    "status": "completed",
                    "conclusion": "success",
                    "event": "push",
                    "head_branch": "main",
                    "created_at": "2026-05-13T01:00:00Z",
                    "started_at": "2026-05-13T01:05:00Z",
                    "completed_at": "2026-05-13T01:20:00Z",
                },
                {
                    "run_id": 2,
                    "run_attempt": 1,
                    "job_id": 20,
                    "workflow_id": 671,
                    "workflow_name": "PkgCI",
                    "workflow_path": ".github/workflows/pkgci.yml",
                    "name": "Test Torch / test_torch_ops :: amdgpu_vulkan_O3",
                    "labels": ["Linux", "X64", "rdna3", "shark10-ci"],
                    "status": "completed",
                    "conclusion": "success",
                    "event": "push",
                    "head_branch": "main",
                    "created_at": "2026-05-13T02:00:00Z",
                    "started_at": "2026-05-13T02:01:00Z",
                    "completed_at": "2026-05-13T02:11:00Z",
                },
                {
                    "run_id": 3,
                    "run_attempt": 1,
                    "job_id": 30,
                    "workflow_name": "PkgCI",
                    "name": "Test Torch / test_torch_ops :: amdgpu_vulkan_O3",
                    "labels": ["Linux", "X64", "rdna3"],
                    "status": "completed",
                    "conclusion": "success",
                    "event": "pull_request",
                    "head_branch": "feature",
                    "created_at": "2026-05-13T03:00:00Z",
                    "started_at": "2026-05-13T03:01:00Z",
                    "completed_at": "2026-05-13T03:09:00Z",
                },
                {
                    "run_id": 4,
                    "run_attempt": 1,
                    "job_id": 40,
                    "workflow_name": "PkgCI",
                    "name": "setup / setup",
                    "labels": ["ubuntu-24.04"],
                    "status": "completed",
                    "conclusion": "success",
                    "event": "push",
                    "head_branch": "main",
                    "created_at": "2026-05-13T04:00:00Z",
                    "started_at": "2026-05-13T04:01:00Z",
                    "completed_at": "2026-05-13T04:02:00Z",
                },
            ]
            with day.open("w") as f:
                for rec in records:
                    f.write(json.dumps(rec))
                    f.write("\n")

            data = dashboard.build_dashboard_data(now, lookback_days=7, data_dir=data_dir)

        self.assertEqual(data["summary"]["points"], 2)
        self.assertEqual(data["summary"]["groups"], 2)
        labels = {p["labels_key"] for p in data["points"]}
        self.assertEqual(labels, {"Linux,X64,rdna3", "Linux,X64,rdna3,shark10-ci"})
        first = data["points"][0]
        self.assertEqual(first["duration_s"], 900)
        self.assertEqual(first["queue_s"], 300)
        self.assertEqual(first["commit_short"], "abcdef123456")
        self.assertEqual(first["run_url"], "https://example.test/run/1")

    def test_write_dashboard_outputs_pages_assets(self):
        dashboard = load_dashboard_module()
        now = datetime(2026, 5, 14, tzinfo=timezone.utc)

        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            data_dir = root / "data"
            output_dir = root / "docs"
            day = data_dir / "2026" / "05" / "13.jsonl"
            day.parent.mkdir(parents=True)
            day.write_text(
                json.dumps(
                    {
                        "run_id": 1,
                        "run_attempt": 1,
                        "job_id": 10,
                        "workflow_name": "PkgCI",
                        "name": "Test ONNX / test_onnx_models :: cpu_llvm_task",
                        "labels": ["self-hosted", "Linux", "X64"],
                        "status": "completed",
                        "conclusion": "success",
                        "event": "push",
                        "head_branch": "main",
                        "created_at": "2026-05-13T01:00:00Z",
                        "started_at": "2026-05-13T01:02:00Z",
                        "completed_at": "2026-05-13T01:07:00Z",
                    }
                )
                + "\n"
            )

            data = dashboard.write_dashboard(
                output_dir=output_dir,
                lookback_days=7,
                now=now,
                data_dir=data_dir,
            )

            self.assertEqual(data["summary"]["points"], 1)
            self.assertTrue((output_dir / "index.html").exists())
            self.assertTrue((output_dir / "standalone.html").exists())
            self.assertTrue((output_dir / "benchmark-data.json").exists())
            self.assertTrue((output_dir / ".nojekyll").exists())
            self.assertIn("IREE Main Benchmark Dashboard", (output_dir / "index.html").read_text())
            html = (output_dir / "index.html").read_text()
            self.assertIn("Points and raw metric", html)
            self.assertIn("Rolling median", html)
            self.assertIn("Suite Coverage", html)
            self.assertIn("renderSuiteCoverage", html)
            self.assertIn("PR title", html)
            self.assertIn("prTitleFromSubject", html)
            self.assertIn("selectedMetricPoints", html)
            self.assertIn("STORAGE_KEY", html)
            self.assertIn("restoreControls", html)
            self.assertIn("saveControls", html)
            self.assertIn("embedded-data", (output_dir / "standalone.html").read_text())


if __name__ == "__main__":
    unittest.main()
