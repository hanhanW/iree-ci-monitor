# Status detail

_Updated: 2026-09-26 09:27 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | — | 6s | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232986) | [9s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233037) | [9s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233037) | 100% (5/5) | — | 5 |  |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | — | 7s | [7s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232914) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232896) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232896) | 0% (0/3) | — | 3 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | — | 5s | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232879) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232888) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232888) | 0% (0/3) | — | 3 |  |
| `ubuntu-24.04` | github-hosted | 13 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232922) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232833) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232935) | 17% (2/12) | 0% (0/1) | 12 |  |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232894) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232810) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232810) | 0% (0/3) | — | 3 |  |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419476940) | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445581) | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445581) | 33% (2/6) | — | 6 |  |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | — | 1s | [1s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233013) | [1s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233013) | [1s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233013) | 100% (1/1) | — | 1 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 9s | [9s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233037) | [9s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233037) | [9s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233037) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232921) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232921) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232921) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233093) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233093) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233093) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232986) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232986) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232986) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232896) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232896) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232896) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 7s | [7s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232914) | [7s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232914) | [7s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232914) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 6s | [6s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232815) | [6s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232815) | [6s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232815) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232831) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232831) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232831) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232879) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232879) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232879) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232888) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232888) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232888) | 1 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232810) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232810) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232810) | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232833) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232833) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232833) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232935) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232935) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232935) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108392703866) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108392703866) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108392703866) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232922) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232922) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232922) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232869) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232869) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232869) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232866) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232866) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232866) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232894) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232894) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232894) | 1 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232761) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232761) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232761) | 1 |
| `.github/workflows/clang_tidy.yml` | clang-tidy | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/36235802019/job/108387209437) | [2s](https://github.com/iree-org/iree/actions/runs/36235802019/job/108387209437) | [2s](https://github.com/iree-org/iree/actions/runs/36235802019/job/108387209437) | 1 |
| `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/36235801979/job/108387209052) | [2s](https://github.com/iree-org/iree/actions/runs/36235801979/job/108387209052) | [2s](https://github.com/iree-org/iree/actions/runs/36235801979/job/108387209052) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/36235802182/job/108388294473) | [2s](https://github.com/iree-org/iree/actions/runs/36235802182/job/108388294473) | [2s](https://github.com/iree-org/iree/actions/runs/36235802182/job/108388294473) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/36247201986/job/108418481995) | [2s](https://github.com/iree-org/iree/actions/runs/36247201986/job/108418481995) | [2s](https://github.com/iree-org/iree/actions/runs/36247201986/job/108418481995) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445557) | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445557) | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445557) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445519) | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445519) | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445519) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445581) | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445581) | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445581) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419445977) | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419445977) | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419445977) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419476826) | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419476826) | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419476826) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419476940) | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419476940) | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419476940) | 1 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387209797) | [1s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387209797) | [1s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387209797) | 1 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233013) | [1s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233013) | [1s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233013) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/36235802182/job/108387231621) | [1s](https://github.com/iree-org/iree/actions/runs/36235802182/job/108387231621) | [1s](https://github.com/iree-org/iree/actions/runs/36235802182/job/108387231621) | 1 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/36235802182/job/108387209824) | [1s](https://github.com/iree-org/iree/actions/runs/36235802182/job/108387209824) | [1s](https://github.com/iree-org/iree/actions/runs/36235802182/job/108387209824) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 0 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 307 | 301 | 5 | 1 | 2% |  | 22h17m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 230 | 220 | 10 | 0 | 4% |  | 22h33m ago |

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
