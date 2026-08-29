# Status detail

_Updated: 2026-08-29 00:10 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 1 | [1h56m](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090336) | 4s | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090337) | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090372) | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090372) | 50% (1/2) | — | 3 |  |
| `ubuntu-24.04` | github-hosted | 13 | 7 | [4h28m](https://github.com/iree-org/iree/actions/runs/32985622770/job/98231128361) | 2026-08-26 13:05 PDT | 2 | [1h56m](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090339) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090341) | [3s](https://github.com/iree-org/iree/actions/runs/33235631932/job/99056003516) | [3s](https://github.com/iree-org/iree/actions/runs/33235631932/job/99056003516) | 0% (0/4) | 0% (0/1) | 6 |  |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [1h56m](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090377) | 3s | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090377) | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090379) | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090379) | 0% (0/1) | — | 2 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [1h56m](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090413) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090403) | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090413) | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090413) | 0% (0/1) | — | 2 |  |
| `ubuntu-latest` | github-hosted | 9 | 9 | [4h29m](https://github.com/iree-org/iree/actions/runs/32985518412/job/98231028102) | 2026-08-26 13:05 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [4h29m](https://github.com/iree-org/iree/actions/runs/32985518412/job/98231028102) | 2026-08-26 13:05 PDT | `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | `refs/pull/24852/head` | dynamic |
| [4h29m](https://github.com/iree-org/iree/actions/runs/32985518412/job/98231028148) | 2026-08-26 13:05 PDT | `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | `refs/pull/24852/head` | dynamic |
| [4h29m](https://github.com/iree-org/iree/actions/runs/32985518412/job/98231028155) | 2026-08-26 13:05 PDT | `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | `refs/pull/24852/head` | dynamic |
| [4h28m](https://github.com/iree-org/iree/actions/runs/32985518325/job/98231089680) | 2026-08-26 13:05 PDT | `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | `refs/pull/24851/head` | dynamic |
| [4h28m](https://github.com/iree-org/iree/actions/runs/32985518325/job/98231089764) | 2026-08-26 13:05 PDT | `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | `refs/pull/24851/head` | dynamic |
| [4h28m](https://github.com/iree-org/iree/actions/runs/32985518325/job/98231089780) | 2026-08-26 13:05 PDT | `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | `refs/pull/24851/head` | dynamic |
| [4h28m](https://github.com/iree-org/iree/actions/runs/32985622770/job/98231128361) | 2026-08-26 13:05 PDT | `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | `users/egebeysel/scalable-dist-4-pack-distribution-hints` | pull_request |
| [4h27m](https://github.com/iree-org/iree/actions/runs/32985674221/job/98231234420) | 2026-08-26 13:05 PDT | `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | `users/egebeysel/scalable-dist-5-distribution-tiling-tests` | pull_request |
| [4h27m](https://github.com/iree-org/iree/actions/runs/32985693175/job/98231275534) | 2026-08-26 13:05 PDT | `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | `users/egebeysel/scalable-dist-2-distribution-tile-sizes` | pull_request |
| [4h27m](https://github.com/iree-org/iree/actions/runs/32985674146/job/98231288233) | 2026-08-26 13:05 PDT | `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | `users/egebeysel/scalable-dist-5-distribution-tiling-tests` | pull_request |
| [4h26m](https://github.com/iree-org/iree/actions/runs/32985715581/job/98231323412) | 2026-08-26 13:05 PDT | `.github/workflows/clang_tidy.yml` | clang-tidy | `ubuntu-24.04` | `users/egebeysel/scalable-dist-1-vscale-range-target-field` | pull_request |
| [4h26m](https://github.com/iree-org/iree/actions/runs/32985518655/job/98231324540) | 2026-08-26 13:05 PDT | `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | `refs/pull/24850/head` | dynamic |
| [4h26m](https://github.com/iree-org/iree/actions/runs/32985518655/job/98231324643) | 2026-08-26 13:05 PDT | `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | `refs/pull/24850/head` | dynamic |
| [4h26m](https://github.com/iree-org/iree/actions/runs/32985518655/job/98231324649) | 2026-08-26 13:05 PDT | `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | `refs/pull/24850/head` | dynamic |
| [4h26m](https://github.com/iree-org/iree/actions/runs/32985698522/job/98231380998) | 2026-08-26 13:05 PDT | `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | `users/egebeysel/scalable-dist-5-distribution-tiling-tests` | pull_request |
| [4h25m](https://github.com/iree-org/iree/actions/runs/32985698522/job/98231436267) | 2026-08-26 13:05 PDT | `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | `users/egebeysel/scalable-dist-5-distribution-tiling-tests` | pull_request |

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 3 | 3 | [4h29m](https://github.com/iree-org/iree/actions/runs/32985518412/job/98231028148) | 2026-08-26 13:05 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 3 | 3 | [4h29m](https://github.com/iree-org/iree/actions/runs/32985518412/job/98231028102) | 2026-08-26 13:05 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 3 | 3 | [4h29m](https://github.com/iree-org/iree/actions/runs/32985518412/job/98231028155) | 2026-08-26 13:05 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 1 | [4h28m](https://github.com/iree-org/iree/actions/runs/32985622770/job/98231128361) | 2026-08-26 13:05 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | github-hosted | 2 | 2 | [4h27m](https://github.com/iree-org/iree/actions/runs/32985674221/job/98231234420) | 2026-08-26 13:05 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | github-hosted | 2 | 2 | [4h27m](https://github.com/iree-org/iree/actions/runs/32985674146/job/98231288233) | 2026-08-26 13:05 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/clang_tidy.yml` | clang-tidy | `ubuntu-24.04` | github-hosted | 1 | 1 | [4h26m](https://github.com/iree-org/iree/actions/runs/32985715581/job/98231323412) | 2026-08-26 13:05 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | github-hosted | 1 | 1 | [4h26m](https://github.com/iree-org/iree/actions/runs/32985698522/job/98231380998) | 2026-08-26 13:05 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090372) | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090372) | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090372) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090336) | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090336) | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090336) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090337) | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090337) | [4s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090337) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090377) | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090377) | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090377) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090379) | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090379) | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090379) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090413) | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090413) | [3s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090413) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/33235631932/job/99056003516) | [3s](https://github.com/iree-org/iree/actions/runs/33235631932/job/99056003516) | [3s](https://github.com/iree-org/iree/actions/runs/33235631932/job/99056003516) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090339) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090339) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090339) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090360) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090360) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090360) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090341) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090341) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090341) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090460) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090460) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090460) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056070342) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056070342) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056070342) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090403) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090403) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99056090403) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 307 | 296 | 2 | 9 | 1% |  | 12h38m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 265 | 251 | 8 | 6 | 3% |  | 14h20m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 219 | 211 | 1 | 7 | 0% |  | 14h21m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 215 | 205 | 0 | 10 | 0% |  | 14h29m ago |

## Alerts

- **[stale-queued]** `ubuntu-24.04` oldest queued job observed waiting 4h28m (> 2h00m)
- **[stale-queued]** `ubuntu-latest` oldest queued job observed waiting 4h29m (> 2h00m)

## Methodology

- Window: last 10 hours of job records for queue-time percentiles and failure metrics; queued observations are scanned for 3 days; last 7 days for runner metrics and SPOF.
- Timestamps rendered in `America/Los_Angeles` local time; underlying records are UTC.
- Queue time: `started_at - created_at`. Skipped jobs excluded.
- Queued: jobs with `status == queued` or `waiting` (not yet assigned a runner).
- Running: jobs with `status == in_progress` (runner assigned, executing).
- Oldest queued: `collected_at - created_at` for the oldest job observed with `status == queued` or `waiting`. This is only updated by collection; rerunning the reporter does not inflate stale queued snapshots.
- Workflow/job waiting time: same queue-time definition, grouped by stable workflow id/name + job name + exact label set. Older records collected before `workflow_path` was stored fall back to `workflow_name`.
- All-jobs fail rate: over every completed job (PR + push + schedule).
- Main-only fail rate: subset where `head_branch == main` and `event != pull_request` — post-merge, scheduled, and workflow_dispatch runs. PR noise excluded.
- Runner type:
  - `self-hosted`: persistent physical hosts managed by the IREE infra team (shark fleet, `iree-mi308-1`, etc.). The `runners` count is the number of physical boxes.
  - `github-hosted`: GitHub's standard runner pool (`ubuntu-*`, `macos-*`, `windows-*`) and Actions Hosting partners (`ah-*`). Ephemeral — one worker per job.
  - `ossci`: org-managed autoscaler pools (`azure-*`, `*-ossci-iree-org`). Ephemeral — one worker per job, so the `runners` count here is really "pod spawns in the window" not physical capacity.
- SPOF: label has seen only one distinct `runner_name` in the last 7 days.
- Persistent runner: ran ≥ 5 jobs in the lookback window AND served at least one label with ≤ 15 distinct runners. Ephemeral auto-scaler worker names (which appear once per spawn) are excluded.
- Re-runs: `(job_id, run_attempt)` tuples are distinct; a re-run counts as a new job.

## Alert thresholds

- `queue-starved`: p95 queue > 1h00m
- `stale-queued`: oldest observed queued job (not yet started) > 2h00m
- `high-failure-main`: main-only failure rate > 20% with ≥ 10 completed main-only jobs
- `spof`: only one distinct runner in last 7d
