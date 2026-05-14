#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import sys
import unittest
from datetime import datetime, timezone
from pathlib import Path


def load_module():
    path = Path(__file__).with_name("benchmark_suite_manifest.py")
    spec = importlib.util.spec_from_file_location("benchmark_suite_manifest", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["benchmark_suite_manifest"] = module
    spec.loader.exec_module(module)
    return module


class BenchmarkSuiteManifestTest(unittest.TestCase):
    def test_classifies_config_kinds(self):
        manifest = load_module()

        self.assertEqual(
            manifest.config_kind("benchmarks/sdxl/clip_rocm.json"),
            "benchmark",
        )
        self.assertEqual(
            manifest.config_kind("sdxl/clip_benchmark_mi325.json"),
            "benchmark",
        )
        self.assertEqual(
            manifest.config_kind("quality_tests/sdxl/clip_rocm.json"),
            "quality",
        )
        self.assertEqual(
            manifest.config_kind("sdxl/modules/clip_cpu.json"),
            "module",
        )

    def test_build_manifest_from_github_tree_shape(self):
        manifest = load_module()

        root_entries = [
            {
                "name": "sharktank_models",
                "path": "tests/external/iree-test-suites/sharktank_models",
                "type": "dir",
                "html_url": "https://example.test/sharktank",
                "git_url": "https://api.example.test/sharktank-tree",
            },
            {
                "name": "torch_models",
                "path": "tests/external/iree-test-suites/torch_models",
                "type": "dir",
                "html_url": "https://example.test/torch",
                "git_url": "https://api.example.test/torch-tree",
            },
        ]
        trees = {
            "https://api.example.test/sharktank-tree": {
                "tree": [
                    {"type": "blob", "path": "benchmarks/sdxl/clip_rocm.json", "size": 1},
                    {"type": "blob", "path": "quality_tests/sdxl/clip_rocm.json", "size": 1},
                ]
            },
            "https://api.example.test/torch-tree": {
                "tree": [
                    {"type": "blob", "path": "sdxl/clip_benchmark_mi325.json", "size": 1},
                    {"type": "blob", "path": "sdxl/modules/clip_cpu.json", "size": 1},
                ]
            },
        }

        def fake_request(path_or_url, params=None):
            if path_or_url.endswith("/contents/tests/external/iree-test-suites"):
                return root_entries
            return trees[path_or_url]

        manifest.gh_request = fake_request

        data = manifest.build_manifest(
            repo="iree-org/iree",
            now=datetime(2026, 5, 14, tzinfo=timezone.utc),
        )

        suites = {suite["name"]: suite for suite in data["suites"]}
        self.assertEqual(suites["sharktank_models"]["kind_counts"]["benchmark"], 1)
        self.assertEqual(suites["torch_models"]["kind_counts"]["benchmark"], 1)
        self.assertEqual(
            suites["sharktank_models"]["configs"][0]["html_url"],
            "https://example.test/sharktank/benchmarks/sdxl/clip_rocm.json",
        )


if __name__ == "__main__":
    unittest.main()
