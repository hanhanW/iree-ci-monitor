#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path


def load_report_module():
    report_path = Path(__file__).with_name("report.py")
    spec = importlib.util.spec_from_file_location("report", report_path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["report"] = module
    spec.loader.exec_module(module)
    return module


class WorkflowQueueAggregationTest(unittest.TestCase):
    def test_workflow_job_waits_and_live_queue_use_exact_labels(self):
        report = load_report_module()
        now = datetime(2026, 4, 24, 21, 0, tzinfo=timezone.utc)

        with tempfile.TemporaryDirectory() as td:
            old_data_dir = report.DATA_DIR
            try:
                report.DATA_DIR = Path(td)
                day = report.DATA_DIR / "2026" / "04" / "24.jsonl"
                day.parent.mkdir(parents=True)
                records = [
                    {
                        "run_id": 1,
                        "run_attempt": 1,
                        "job_id": 10,
                        "workflow_id": 671,
                        "workflow_name": "PkgCI",
                        "workflow_path": ".github/workflows/pkgci_test_torch.yml",
                        "name": "Test Torch / test_torch_ops :: amdgpu_vulkan_O3",
                        "labels": ["Linux", "X64", "rdna3", "shark10-ci"],
                        "status": "queued",
                        "conclusion": None,
                        "event": "pull_request",
                        "head_branch": "pr-branch",
                        "created_at": "2026-04-24T19:00:00Z",
                        "started_at": "2026-04-24T19:00:00Z",
                        "completed_at": None,
                        "collected_at": "2026-04-24T20:00:00Z",
                    },
                    {
                        "run_id": 1,
                        "run_attempt": 1,
                        "job_id": 10,
                        "workflow_id": 671,
                        "workflow_name": "PkgCI",
                        "workflow_path": ".github/workflows/pkgci_test_torch.yml",
                        "name": "Test Torch / test_torch_ops :: amdgpu_vulkan_O3",
                        "labels": ["Linux", "X64", "rdna3", "shark10-ci"],
                        "status": "queued",
                        "conclusion": None,
                        "event": "pull_request",
                        "head_branch": "pr-branch",
                        "created_at": "2026-04-24T19:00:00Z",
                        "started_at": "2026-04-24T19:00:00Z",
                        "completed_at": None,
                        "collected_at": "2026-04-24T20:30:00Z",
                    },
                    {
                        "run_id": 4,
                        "run_attempt": 1,
                        "job_id": 40,
                        "workflow_id": 671,
                        "workflow_name": "PkgCI",
                        "workflow_path": ".github/workflows/pkgci_test_torch.yml",
                        "name": "Test Torch / test_torch_ops :: amdgpu_vulkan_O3",
                        "labels": ["Linux", "X64", "rdna3", "shark10-ci"],
                        "status": "queued",
                        "conclusion": None,
                        "event": "pull_request",
                        "head_branch": "old-pr-branch",
                        "created_at": "2026-04-24T09:00:00Z",
                        "started_at": "2026-04-24T09:00:00Z",
                        "completed_at": None,
                        "collected_at": "2026-04-24T21:00:00Z",
                    },
                    {
                        "run_id": 2,
                        "run_attempt": 1,
                        "job_id": 20,
                        "workflow_id": 671,
                        "workflow_name": "PkgCI",
                        "name": "Test Torch / test_torch_ops :: amdgpu_vulkan_O3",
                        "labels": ["Linux", "X64", "rdna3", "shark10-ci"],
                        "runner_name": "shark10-ci-2",
                        "status": "completed",
                        "conclusion": "success",
                        "event": "push",
                        "head_branch": "main",
                        "created_at": "2026-04-24T18:00:00Z",
                        "started_at": "2026-04-24T20:30:00Z",
                        "completed_at": "2026-04-24T20:45:00Z",
                    },
                    {
                        "run_id": 6,
                        "run_attempt": 1,
                        "job_id": 60,
                        "workflow_id": 671,
                        "workflow_name": "PkgCI",
                        "workflow_path": ".github/workflows/pkgci_test_torch.yml",
                        "name": "Test Torch / test_torch_ops :: amdgpu_vulkan_O3",
                        "labels": ["Linux", "X64", "rdna3", "shark10-ci"],
                        "status": "queued",
                        "conclusion": None,
                        "event": "pull_request",
                        "head_branch": "finished-pr",
                        "created_at": "2026-04-24T18:15:00Z",
                        "started_at": "2026-04-24T18:15:00Z",
                        "completed_at": None,
                        "collected_at": "2026-04-24T19:00:00Z",
                    },
                    {
                        "run_id": 6,
                        "run_attempt": 1,
                        "job_id": 60,
                        "workflow_id": 671,
                        "workflow_name": "PkgCI",
                        "workflow_path": ".github/workflows/pkgci_test_torch.yml",
                        "name": "Test Torch / test_torch_ops :: amdgpu_vulkan_O3",
                        "labels": ["Linux", "X64", "rdna3", "shark10-ci"],
                        "runner_name": "shark10-ci-2",
                        "status": "completed",
                        "conclusion": "success",
                        "event": "pull_request",
                        "head_branch": "finished-pr",
                        "created_at": "2026-04-24T18:15:00Z",
                        "started_at": "2026-04-24T19:15:00Z",
                        "completed_at": "2026-04-24T19:30:00Z",
                    },
                    {
                        "run_id": 5,
                        "run_attempt": 1,
                        "job_id": 50,
                        "workflow_id": 671,
                        "workflow_name": "PkgCI",
                        "workflow_path": ".github/workflows/pkgci_test_torch.yml",
                        "name": "Test Torch / test_torch_ops :: amdgpu_vulkan_O3",
                        "labels": ["Linux", "X64", "rdna3", "shark10-ci"],
                        "runner_name": "",
                        "status": "completed",
                        "conclusion": "cancelled",
                        "event": "pull_request",
                        "head_branch": "cancelled-pr",
                        "created_at": "2026-04-24T20:00:00Z",
                        "started_at": "2026-04-24T20:00:00Z",
                        "completed_at": "2026-04-24T20:00:30Z",
                    },
                    {
                        "run_id": 3,
                        "run_attempt": 1,
                        "job_id": 30,
                        "workflow_id": 671,
                        "workflow_name": "PkgCI",
                        "workflow_path": ".github/workflows/pkgci_test_torch.yml",
                        "name": "Test Torch / test_torch_ops :: amdgpu_vulkan_O3",
                        "labels": ["Linux", "X64", "rdna3"],
                        "runner_name": "shark01-ci",
                        "status": "completed",
                        "conclusion": "success",
                        "event": "push",
                        "head_branch": "main",
                        "created_at": "2026-04-24T18:30:00Z",
                        "started_at": "2026-04-24T18:45:00Z",
                        "completed_at": "2026-04-24T18:50:00Z",
                    },
                ]
                with day.open("w") as f:
                    for rec in records:
                        f.write(json.dumps(rec))
                        f.write("\n")

                workflow_jobs = report.aggregate_workflow_jobs(now, 10)
                pinned = workflow_jobs[
                    (
                        "id:671",
                        "Test Torch / test_torch_ops :: amdgpu_vulkan_O3",
                        "Linux,X64,rdna3,shark10-ci",
                    )
                ]

                self.assertEqual(pinned.workflow, ".github/workflows/pkgci_test_torch.yml")
                self.assertEqual(pinned.total, 5)
                self.assertEqual(pinned.queued, 2)
                self.assertEqual(pinned.completed, 3)
                self.assertEqual(pinned.oldest_queued_s, 43200)
                self.assertEqual(
                    pinned.oldest_queued_seen_at,
                    datetime(2026, 4, 24, 21, 0, tzinfo=timezone.utc),
                )
                self.assertEqual(pinned.p50, 3600)
                self.assertEqual(pinned.p95, 9000)
                self.assertEqual(pinned.runners, {"shark10-ci-2"})

                label_stats = report.aggregate(now, 10)["Linux,X64,rdna3,shark10-ci"]
                self.assertEqual(label_stats.total, 5)
                self.assertEqual(label_stats.queued, 2)
                self.assertEqual(label_stats.oldest_queued_s, 43200)
                self.assertEqual(
                    label_stats.oldest_queued_seen_at,
                    datetime(2026, 4, 24, 21, 0, tzinfo=timezone.utc),
                )
                self.assertEqual(label_stats.p50, 3600)

                live_queue = report.queued_jobs(now, report.LIVE_STATE_LOOKBACK_DAYS)
                self.assertEqual(len(live_queue), 2)
                self.assertEqual(live_queue[0].labels, "Linux,X64,rdna3,shark10-ci")
                self.assertEqual(live_queue[0].wait_s, 43200)
                self.assertEqual(
                    live_queue[0].observed_at,
                    datetime(2026, 4, 24, 21, 0, tzinfo=timezone.utc),
                )
                self.assertEqual(live_queue[0].workflow, ".github/workflows/pkgci_test_torch.yml")
                self.assertEqual(live_queue[1].wait_s, 5400)
                self.assertEqual(
                    live_queue[1].observed_at,
                    datetime(2026, 4, 24, 20, 30, tzinfo=timezone.utc),
                )
            finally:
                report.DATA_DIR = old_data_dir


if __name__ == "__main__":
    unittest.main()
