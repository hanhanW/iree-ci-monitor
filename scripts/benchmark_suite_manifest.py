#!/usr/bin/env python3
"""Fetch the IREE benchmark suite config manifest.

The dashboard observes result rows from GitHub Actions artifacts, but the
source of truth for which model suites should exist lives in IREE under
`tests/external/iree-test-suites`. This script records the configured JSON files
so the static dashboard can show observed-vs-configured coverage.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

REPO = os.environ.get("IREE_CI_MONITOR_REPO", "iree-org/iree")
ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SUITE_ROOT = "tests/external/iree-test-suites"
DEFAULT_OUTPUT = ROOT / "data" / "benchmark_suites.json"
RATE_LIMIT_MAX_SLEEP_S = 300
_TOKEN: str | None = None


def log(msg: str) -> None:
    print(f"[benchmark_suite_manifest] {msg}", flush=True)


def fmt_iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def token() -> str | None:
    global _TOKEN
    if _TOKEN is not None:
        return _TOKEN
    env_token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if env_token:
        _TOKEN = env_token
        return _TOKEN
    try:
        _TOKEN = subprocess.check_output(
            ["gh", "auth", "token"], text=True, stderr=subprocess.DEVNULL
        ).strip()
        return _TOKEN
    except (FileNotFoundError, subprocess.CalledProcessError):
        _TOKEN = ""
        return None


def _rate_limit_wait(e: urllib.error.HTTPError) -> int | None:
    if e.code not in (403, 429):
        return None
    retry_after = e.headers.get("Retry-After")
    if retry_after:
        try:
            return min(max(1, int(retry_after)), RATE_LIMIT_MAX_SLEEP_S)
        except ValueError:
            return 60
    if e.headers.get("X-RateLimit-Remaining") == "0":
        reset = e.headers.get("X-RateLimit-Reset")
        if reset:
            try:
                return max(1, min(int(reset) - int(time.time()), RATE_LIMIT_MAX_SLEEP_S))
            except ValueError:
                return 60
    return None


def gh_request(path_or_url: str, params: dict | None = None):
    if path_or_url.startswith("http"):
        url = path_or_url
    else:
        url = f"https://api.github.com{path_or_url}"
    if params:
        sep = "&" if "?" in url else "?"
        url += sep + urllib.parse.urlencode(params)
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "iree-ci-monitor",
    }
    auth_token = token()
    if auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"
    req = urllib.request.Request(url, headers=headers)
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.loads(resp.read())
        except urllib.error.HTTPError as e:
            wait = _rate_limit_wait(e)
            if wait is not None and attempt < 2:
                log(f"rate limited ({e.code}); sleeping {wait}s")
                time.sleep(wait)
                continue
            if e.code in (502, 503, 504) and attempt < 2:
                time.sleep(2**attempt)
                continue
            raise
        except urllib.error.URLError:
            if attempt < 2:
                time.sleep(2**attempt)
                continue
            raise
    raise RuntimeError("unreachable")


def config_kind(path: str) -> str:
    parts = path.split("/")
    filename = parts[-1]
    if "benchmarks" in parts or "benchmark" in filename:
        return "benchmark"
    if "quality_tests" in parts or "quality" in filename:
        return "quality"
    if "modules" in parts:
        return "module"
    if "compstat" in filename:
        return "compilation_stats"
    return "other"


def suite_tree_entries(suite: dict) -> list[dict]:
    tree = gh_request(suite["git_url"], {"recursive": "1"})
    return list(tree.get("tree") or [])


def build_manifest(
    *,
    repo: str = REPO,
    suite_root: str = DEFAULT_SUITE_ROOT,
    ref: str = "main",
    now: datetime | None = None,
) -> dict:
    now = now or datetime.now(timezone.utc)
    root_entries = gh_request(f"/repos/{repo}/contents/{suite_root}", {"ref": ref})
    suites = []
    for suite in sorted(root_entries, key=lambda e: e.get("name", "")):
        if suite.get("type") != "dir":
            continue
        configs = []
        for entry in suite_tree_entries(suite):
            if entry.get("type") != "blob" or not entry.get("path", "").endswith(".json"):
                continue
            path = entry["path"]
            configs.append(
                {
                    "path": path,
                    "name": Path(path).name,
                    "kind": config_kind(path),
                    "size": entry.get("size"),
                    "html_url": f"{suite['html_url']}/{path}",
                }
            )
        kind_counts: dict[str, int] = {}
        for config in configs:
            kind_counts[config["kind"]] = kind_counts.get(config["kind"], 0) + 1
        suites.append(
            {
                "name": suite["name"],
                "path": suite["path"],
                "html_url": suite["html_url"],
                "configs": sorted(configs, key=lambda c: (c["kind"], c["path"])),
                "kind_counts": dict(sorted(kind_counts.items())),
            }
        )
    return {
        "schema_version": 1,
        "generated_at": fmt_iso(now),
        "repo": repo,
        "ref": ref,
        "suite_root": suite_root,
        "suite_root_url": f"https://github.com/{repo}/tree/{ref}/{suite_root}",
        "suites": suites,
    }


def write_manifest(output: Path, manifest: dict) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=REPO)
    parser.add_argument("--ref", default="main")
    parser.add_argument("--suite-root", default=DEFAULT_SUITE_ROOT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    manifest = build_manifest(repo=args.repo, suite_root=args.suite_root, ref=args.ref)
    write_manifest(args.output, manifest)
    benchmark_count = sum(
        suite["kind_counts"].get("benchmark", 0) for suite in manifest["suites"]
    )
    log(
        f"wrote {args.output} with {len(manifest['suites'])} suites "
        f"and {benchmark_count} benchmark configs"
    )


if __name__ == "__main__":
    main()
