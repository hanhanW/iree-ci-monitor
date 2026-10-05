# Status detail

_Updated: 2026-10-04 22:47 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [16m52s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187670) | 7s | [7s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187668) | [7s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187670) | [7s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187670) | 0% (0/1) | — | 2 |  |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 3 | [16m52s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187564) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187564) | [4s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111616357388) | [4s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111616357388) | 14% (1/7) | 0% (0/4) | 10 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [16m52s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187620) | 4s | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187620) | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187648) | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187648) | 0% (0/1) | — | 3 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 2 | [16m52s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187659) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187659) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187742) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187742) | — | — | 2 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 1 | 7s | [7s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187670) | [7s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187670) | [7s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187670) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 7s | [7s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187668) | [7s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187668) | [7s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187668) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187620) | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187620) | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187620) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187648) | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187648) | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187648) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187582) | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187582) | [4s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187582) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111616357388) | [4s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111616357388) | [4s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111616357388) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111618270081) | [3s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111618270081) | [3s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111618270081) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187564) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187564) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187564) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187680) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187680) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187680) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187596) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187596) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187596) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187656) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187656) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187656) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629145544) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629145544) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629145544) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187659) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187659) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187659) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187742) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187742) | [2s](https://github.com/iree-org/iree/actions/runs/37268119191/job/111629187742) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111523208388) | [2s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111523208388) | [2s](https://github.com/iree-org/iree/actions/runs/37150894632/job/111523208388) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111616357217) | [2s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111616357217) | [2s](https://github.com/iree-org/iree/actions/runs/37263829508/job/111616357217) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/37268057383/job/111628965884) | [2s](https://github.com/iree-org/iree/actions/runs/37268057383/job/111628965884) | [2s](https://github.com/iree-org/iree/actions/runs/37268057383/job/111628965884) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 296 | 284 | 4 | 8 | 1% |  | 1d09h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 206 | 203 | 2 | 1 | 1% |  | 4d09h ago |

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
