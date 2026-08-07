# Status detail

_Updated: 2026-08-07 00:43 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04` | github-hosted | 13 | 0 | — | — | 2 | [2h09m](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557257) | 3s | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557272) | [9s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557257) | [9s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557257) | 22% (2/9) | 33% (2/6) | 11 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [2h09m](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557264) | 5s | [5s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557276) | [6s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557307) | [6s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557307) | 0% (0/1) | — | 3 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2h09m](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557332) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557332) | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557251) | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557251) | 0% (0/1) | — | 2 |  |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2h09m](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557282) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557282) | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557271) | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557271) | 0% (0/1) | — | 2 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 9s | [9s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557257) | [9s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557257) | [9s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557257) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/31148291642/job/92772381430) | [8s](https://github.com/iree-org/iree/actions/runs/31148291642/job/92772381430) | [8s](https://github.com/iree-org/iree/actions/runs/31148291642/job/92772381430) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/31150989671/job/92780392069) | [8s](https://github.com/iree-org/iree/actions/runs/31150989671/job/92780392069) | [8s](https://github.com/iree-org/iree/actions/runs/31150989671/job/92780392069) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 6s | [6s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557307) | [6s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557307) | [6s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557307) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557276) | [5s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557276) | [5s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557276) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557264) | [4s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557264) | [4s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557264) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557285) | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557285) | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557285) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557271) | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557271) | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557271) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557251) | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557251) | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557251) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557279) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557279) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557279) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557272) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557272) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557272) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557282) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557282) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557282) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780523930) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780523930) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780523930) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557332) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557332) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557332) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31128374710/job/92709659505) | [2s](https://github.com/iree-org/iree/actions/runs/31128374710/job/92709659505) | [2s](https://github.com/iree-org/iree/actions/runs/31128374710/job/92709659505) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92711543671) | [2s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92711543671) | [2s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92711543671) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31148291642/job/92772381345) | [2s](https://github.com/iree-org/iree/actions/runs/31148291642/job/92772381345) | [2s](https://github.com/iree-org/iree/actions/runs/31148291642/job/92772381345) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31148291642/job/92773904174) | [2s](https://github.com/iree-org/iree/actions/runs/31148291642/job/92773904174) | [2s](https://github.com/iree-org/iree/actions/runs/31148291642/job/92773904174) | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 0 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 129 | 129 | 0 | 0 | 0% |  | 9h38m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 112 | 108 | 3 | 1 | 3% |  | 9h40m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 101 | 100 | 0 | 1 | 0% |  | 9h43m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 102 | 100 | 1 | 1 | 1% |  | 9h44m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 13 | 13 | 0 | 0 | 0% |  | 3d18h ago |

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
