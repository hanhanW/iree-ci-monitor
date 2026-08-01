# Status detail

_Updated: 2026-08-01 11:37 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 0 | — | 4s | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91366175468) | [9s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366187044) | [9s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366187044) | 40% (4/10) | 50% (1/2) | 10 |  |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | — | 4s | [3s](https://github.com/iree-org/iree/actions/runs/30699113356/job/91366860038) | [8s](https://github.com/iree-org/iree/actions/runs/30704032983/job/91379944127) | [9s](https://github.com/iree-org/iree/actions/runs/30699113104/job/91366859375) | 27% (4/15) | — | 15 |  |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 4 | [23h55m](https://github.com/iree-org/iree/actions/runs/30655580496/job/91241055463) | 2026-08-01 11:37 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [23h55m](https://github.com/iree-org/iree/actions/runs/30655580496/job/91241055463) | 2026-08-01 11:37 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [23h12m](https://github.com/iree-org/iree/actions/runs/30658571489/job/91250481355) | 2026-08-01 11:37 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [23h09m](https://github.com/iree-org/iree/actions/runs/30658240178/job/91251001169) | 2026-08-01 11:37 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `integrates/llvm-20260731-cleanup` | pull_request |
| [23h08m](https://github.com/iree-org/iree/actions/runs/30658666350/job/91251264223) | 2026-08-01 11:37 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 4 | [23h55m](https://github.com/iree-org/iree/actions/runs/30655580496/job/91241055463) | 2026-08-01 11:37 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | github-hosted | 4 | 0 | — | — | 0 | 4s | [3s](https://github.com/iree-org/iree/actions/runs/30646844543/job/91393372227) | [9s](https://github.com/iree-org/iree/actions/runs/30621832279/job/91356440816) | [9s](https://github.com/iree-org/iree/actions/runs/30621832279/job/91356440816) | 4 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/30704032983/job/91379920356) | [9s](https://github.com/iree-org/iree/actions/runs/30699113104/job/91366859375) | [9s](https://github.com/iree-org/iree/actions/runs/30699113104/job/91366859375) | 2 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 9s | [9s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366187044) | [9s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366187044) | [9s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366187044) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 2 | 0 | — | — | 0 | 5s | [3s](https://github.com/iree-org/iree/actions/runs/30698890796/job/91366289903) | [8s](https://github.com/iree-org/iree/actions/runs/30703843054/job/91379396846) | [8s](https://github.com/iree-org/iree/actions/runs/30703843054/job/91379396846) | 2 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/30699113104/job/91366883255) | [8s](https://github.com/iree-org/iree/actions/runs/30704032983/job/91379944115) | [8s](https://github.com/iree-org/iree/actions/runs/30704032983/job/91379944115) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/30699113104/job/91366883254) | [8s](https://github.com/iree-org/iree/actions/runs/30704032983/job/91379944127) | [8s](https://github.com/iree-org/iree/actions/runs/30704032983/job/91379944127) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | 4s | [3s](https://github.com/iree-org/iree/actions/runs/30698913070/job/91366348697) | [7s](https://github.com/iree-org/iree/actions/runs/30699113356/job/91366860025) | [7s](https://github.com/iree-org/iree/actions/runs/30699113356/job/91366860025) | 3 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366275992) | [4s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366275992) | [4s](https://github.com/iree-org/iree/actions/runs/30698850624/job/91366275992) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30704033068/job/91379920594) | [3s](https://github.com/iree-org/iree/actions/runs/30699113356/job/91366860038) | [3s](https://github.com/iree-org/iree/actions/runs/30699113356/job/91366860038) | 3 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91366175468) | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91366175468) | [3s](https://github.com/iree-org/iree/actions/runs/30686970433/job/91366175468) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30699113356/job/91366860062) | [2s](https://github.com/iree-org/iree/actions/runs/30704033068/job/91379920623) | [2s](https://github.com/iree-org/iree/actions/runs/30704033068/job/91379920623) | 3 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30697447328/job/91362619593) | [2s](https://github.com/iree-org/iree/actions/runs/30697447328/job/91362619593) | [2s](https://github.com/iree-org/iree/actions/runs/30697447328/job/91362619593) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 166 | 166 | 0 | 0 | 0% |  | 22h07m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 118 | 117 | 1 | 0 | 1% |  | 22h19m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 148 | 144 | 4 | 0 | 3% |  | 22h20m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 123 | 121 | 1 | 1 | 1% |  | 22h23m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 37 | 36 | 1 | 0 | 3% |  | 22h38m ago |

## Alerts

- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job observed waiting 23h55m (> 2h00m)

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
