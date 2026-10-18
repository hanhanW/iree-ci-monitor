# Status detail

_Updated: 2026-10-18 04:14 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `macos-15` | github-hosted | 2 | 0 | — | — | 0 | — | 6s | [5s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694614) | [7s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694588) | [7s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694588) | 0% (0/2) | — | 2 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | — | 4s | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694584) | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694636) | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694636) | 33% (1/3) | — | 3 |  |
| `ubuntu-24.04` | github-hosted | 18 | 0 | — | — | 0 | — | 1s | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694620) | [2s](https://github.com/iree-org/iree/actions/runs/39122038036/job/117659416281) | [3s](https://github.com/iree-org/iree/actions/runs/39107614557/job/117616799835) | 7% (1/15) | 0% (0/1) | 15 |  |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39107612288/job/117616756233) | [2s](https://github.com/iree-org/iree/actions/runs/39107612288/job/117616756260) | [2s](https://github.com/iree-org/iree/actions/runs/39107612288/job/117616756260) | 0% (0/3) | — | 3 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694637) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694652) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694652) | 0% (0/2) | — | 2 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | github-hosted | 1 | 0 | — | — | 0 | 7s | [7s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694588) | [7s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694588) | [7s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694588) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694614) | [5s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694614) | [5s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694614) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694636) | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694636) | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694636) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694550) | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694550) | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694550) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694584) | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694584) | [4s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694584) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/39107614557/job/117616799835) | [3s](https://github.com/iree-org/iree/actions/runs/39107614557/job/117616799835) | [3s](https://github.com/iree-org/iree/actions/runs/39107614557/job/117616799835) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694580) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694580) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694580) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694620) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694620) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694620) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694586) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694586) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694586) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694587) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694587) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694587) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593665274) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593665274) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593665274) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694652) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694652) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694652) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694637) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694637) | [2s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117593694637) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39107614566/job/117616803338) | [2s](https://github.com/iree-org/iree/actions/runs/39107614566/job/117616803338) | [2s](https://github.com/iree-org/iree/actions/runs/39107614566/job/117616803338) | 1 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39107614566/job/117616761827) | [2s](https://github.com/iree-org/iree/actions/runs/39107614566/job/117616761827) | [2s](https://github.com/iree-org/iree/actions/runs/39107614566/job/117616761827) | 1 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39107614557/job/117616761670) | [2s](https://github.com/iree-org/iree/actions/runs/39107614557/job/117616761670) | [2s](https://github.com/iree-org/iree/actions/runs/39107614557/job/117616761670) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39122038036/job/117659416281) | [2s](https://github.com/iree-org/iree/actions/runs/39122038036/job/117659416281) | [2s](https://github.com/iree-org/iree/actions/runs/39122038036/job/117659416281) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39099797306/job/117593542213) | [2s](https://github.com/iree-org/iree/actions/runs/39099797306/job/117593542213) | [2s](https://github.com/iree-org/iree/actions/runs/39099797306/job/117593542213) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39121971417/job/117659394540) | [2s](https://github.com/iree-org/iree/actions/runs/39121971417/job/117659394540) | [2s](https://github.com/iree-org/iree/actions/runs/39121971417/job/117659394540) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39121971417/job/117659229578) | [2s](https://github.com/iree-org/iree/actions/runs/39121971417/job/117659229578) | [2s](https://github.com/iree-org/iree/actions/runs/39121971417/job/117659229578) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39107612288/job/117616756233) | [2s](https://github.com/iree-org/iree/actions/runs/39107612288/job/117616756233) | [2s](https://github.com/iree-org/iree/actions/runs/39107612288/job/117616756233) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39107612288/job/117616756260) | [2s](https://github.com/iree-org/iree/actions/runs/39107612288/job/117616756260) | [2s](https://github.com/iree-org/iree/actions/runs/39107612288/job/117616756260) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39107612288/job/117616756024) | [2s](https://github.com/iree-org/iree/actions/runs/39107612288/job/117616756024) | [2s](https://github.com/iree-org/iree/actions/runs/39107612288/job/117616756024) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117659210558) | [1s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117659210558) | [1s](https://github.com/iree-org/iree/actions/runs/39099837866/job/117659210558) | 1 |
| `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/39107614496/job/117616761233) | [1s](https://github.com/iree-org/iree/actions/runs/39107614496/job/117616761233) | [1s](https://github.com/iree-org/iree/actions/runs/39107614496/job/117616761233) | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/clang_tidy.yml` | clang-tidy | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 0 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 261 | 249 | 11 | 1 | 4% |  | 1d18h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 212 | 209 | 2 | 1 | 1% |  | 1d18h ago |

## Alerts

_No active alerts._

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
