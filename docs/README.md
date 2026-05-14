# IREE Main Benchmark Dashboard

This directory is the static GitHub Pages payload for the benchmark dashboard.
It is generated from checked-in benchmark result rows under `data/benchmarks/`.
Those rows come from PkgCI summary artifacts such as
`torch_models_amdgpu_mi325_summary.json/job_summary.json`, including entries
like `sdxl/clip_benchmark_mi325.json` and `Current Time (ms)`.

```bash
python3 scripts/dashboard.py --lookback-days 90
```

The scheduled workflow collects recent benchmark artifacts incrementally:

```bash
IREE_BENCHMARK_LOOKBACK_DAYS=3 python3 scripts/benchmark_collect.py
```

The checked-in backfill under `data/benchmarks/` provides the historical window.
The workflow then regenerates `docs/benchmark-data.json`, `docs/index.html`,
and `docs/standalone.html` and deploys the `docs/` directory with GitHub Pages.

For local development, serve the directory with any static file server:

```bash
python3 -m http.server 8000 -d docs
```

Then open <http://localhost:8000/>.

If port forwarding is not available in your environment, open
`docs/standalone.html` directly in a browser. It embeds the generated JSON and
does not need a local server.

Milestone 1 is intentionally static: `index.html` loads `benchmark-data.json`
in the browser and does all filtering/charting locally. GitHub Pages can host
this because it is static HTML, JavaScript, and JSON. There is no backend,
database, server-side query path, or raw log/artifact publication here. The
generated JSON is compact normalized benchmark-result data only.

## Dashboard controls

- `Benchmark` selects a benchmark row name from the summary artifact, for
  example `sdxl/clip_benchmark_mi325.json`.
- `Hardware / labels` selects the summary artifact target, for example
  `torch_models_amdgpu_mi325`.
- `Metric` selects `Current Time`, `Golden Time`, or `Threshold`.
- `Rolling window` controls the purple rolling median line and candidate range
  detection.
- `Success only` filters to passed benchmark rows.

The selected benchmark, target, metric, rolling window, and success-only setting
are saved in browser local storage. Refreshing the page restores the same
selection when it is still present in the latest generated data.

In the chart, the green points/line are raw values for the selected metric.
The purple line is the rolling median over the configured window. Hovering a
point shows benchmark, metric value, commit/run, target, timestamp, status, and
the PR title when it can be derived from the commit message. Clicking a point
pins the tooltip so the commit or run link can be opened; click outside the
tooltip or press Escape to unpin it.

Candidate ranges compare rolling windows and list changes of at least 10%.
Positive changes are shown as regressions for time-based metrics; negative
changes are shown as improvements.

## Suite Coverage

`scripts/benchmark_suite_manifest.py` reads the IREE benchmark suite config from
`tests/external/iree-test-suites` and writes `data/benchmark_suites.json`. The
dashboard uses that manifest to show which configured benchmark suites have
observed result rows.

As of the current manifest, the configured benchmark suites include both
`torch_models` and `sharktank_models`. If a suite has configured benchmark JSON
files but no observed points, the dashboard lists missing examples in the Suite
Coverage table. That usually means the corresponding PkgCI jobs did not upload
a `*_summary.json/job_summary.json` benchmark table in the collected window, or
they use a different result format that needs a parser.
