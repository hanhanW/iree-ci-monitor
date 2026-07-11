# Status detail

_Updated: 2026-07-11 05:37 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | — | 5s | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674785) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674791) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674791) | 33% (1/3) | — | 3 |  |
| `ubuntu-24.04` | github-hosted | 12 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29151269439/job/86541102903) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674776) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86541037472) | 17% (2/12) | 50% (1/2) | 12 |  |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | — | 2s | [1s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674795) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674804) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674804) | 0% (0/2) | — | 2 |  |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29151452695/job/86541489547) | [3s](https://github.com/iree-org/iree/actions/runs/29151452917/job/86541490028) | [3s](https://github.com/iree-org/iree/actions/runs/29151452917/job/86541490028) | 22% (2/9) | — | 9 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674793) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674797) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674797) | 0% (0/2) | — | 2 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674791) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674791) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674791) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674783) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674783) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674783) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674785) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674785) | [5s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674785) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | github-hosted | 2 | 0 | — | — | 0 | 2s | [1s](https://github.com/iree-org/iree/actions/runs/29089345918/job/86529298845) | [3s](https://github.com/iree-org/iree/actions/runs/29083604698/job/86528350519) | [3s](https://github.com/iree-org/iree/actions/runs/29083604698/job/86528350519) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29151313641/job/86541155351) | [3s](https://github.com/iree-org/iree/actions/runs/29151452917/job/86541490021) | [3s](https://github.com/iree-org/iree/actions/runs/29151452917/job/86541490021) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29151313641/job/86541155347) | [3s](https://github.com/iree-org/iree/actions/runs/29151452917/job/86541490028) | [3s](https://github.com/iree-org/iree/actions/runs/29151452917/job/86541490028) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86541037472) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86541037472) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86541037472) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674776) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674776) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674776) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674774) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674774) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674774) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674804) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674804) | [3s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674804) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29151313641/job/86541155346) | [2s](https://github.com/iree-org/iree/actions/runs/29151452917/job/86541490024) | [2s](https://github.com/iree-org/iree/actions/runs/29151452917/job/86541490024) | 2 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674792) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674792) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674792) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674788) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674788) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674788) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516660522) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516660522) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516660522) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674797) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674797) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674797) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674793) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674793) | [2s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674793) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29151295806/job/86541110474) | [2s](https://github.com/iree-org/iree/actions/runs/29151295806/job/86541110474) | [2s](https://github.com/iree-org/iree/actions/runs/29151295806/job/86541110474) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29141922849/job/86516605989) | [2s](https://github.com/iree-org/iree/actions/runs/29141922849/job/86516605989) | [2s](https://github.com/iree-org/iree/actions/runs/29141922849/job/86516605989) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29151269439/job/86541102903) | [2s](https://github.com/iree-org/iree/actions/runs/29151269439/job/86541102903) | [2s](https://github.com/iree-org/iree/actions/runs/29151269439/job/86541102903) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29151269439/job/86541046853) | [2s](https://github.com/iree-org/iree/actions/runs/29151269439/job/86541046853) | [2s](https://github.com/iree-org/iree/actions/runs/29151269439/job/86541046853) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29151452695/job/86541489547) | [2s](https://github.com/iree-org/iree/actions/runs/29151452695/job/86541489547) | [2s](https://github.com/iree-org/iree/actions/runs/29151452695/job/86541489547) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/29151452695/job/86541498620) | [2s](https://github.com/iree-org/iree/actions/runs/29151452695/job/86541498620) | [2s](https://github.com/iree-org/iree/actions/runs/29151452695/job/86541498620) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674795) | [1s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674795) | [1s](https://github.com/iree-org/iree/actions/runs/29141941573/job/86516674795) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/29151452695/job/86541498607) | [1s](https://github.com/iree-org/iree/actions/runs/29151452695/job/86541498607) | [1s](https://github.com/iree-org/iree/actions/runs/29151452695/job/86541498607) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 159 | 146 | 11 | 1 | 7% | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 202 | 196 | 3 | 2 | 1% | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 162 | 158 | 1 | 2 | 1% | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 150 | 148 | 1 | 0 | 1% | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 47 | 41 | 5 | 1 | 11% |  | 1d00h ago |

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
