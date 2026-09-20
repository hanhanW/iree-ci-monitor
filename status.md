# Status detail

_Updated: 2026-09-19 21:58 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04` | github-hosted | 3 | 0 | — | — | 0 | — | 3s | [2s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105959169291) | [4s](https://github.com/iree-org/iree/actions/runs/35416725134/job/106012960458) | [4s](https://github.com/iree-org/iree/actions/runs/35416725134/job/106012960458) | 100% (2/2) | 100% (1/1) | 2 |  |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 1 | [14h20m](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640040) | 2026-09-19 21:58 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 1 | [14h20m](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640153) | 2026-09-19 21:58 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 | yes |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [14h20m](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640040) | 2026-09-19 21:58 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `stream-flush-invalidate-lowering` | pull_request |
| [14h20m](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640153) | 2026-09-19 21:58 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `stream-flush-invalidate-lowering` | pull_request |

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | self-hosted | 1 | 1 | [14h20m](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640040) | 2026-09-19 21:58 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 1 | [14h20m](https://github.com/iree-org/iree/actions/runs/35444212759/job/105913640153) | 2026-09-19 21:58 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | github-hosted | 2 | 0 | — | — | 0 | 3s | [2s](https://github.com/iree-org/iree/actions/runs/35388676282/job/105959169291) | [4s](https://github.com/iree-org/iree/actions/runs/35416725134/job/106012960458) | [4s](https://github.com/iree-org/iree/actions/runs/35416725134/job/106012960458) | 2 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 0 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 322 | 320 | 1 | 1 | 0% |  | 13h32m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 359 | 355 | 3 | 1 | 1% |  | 13h36m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 230 | 225 | 4 | 1 | 2% |  | 2d07h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 17 | 15 | 2 | 0 | 12% |  | 5d13h ago |

## Alerts

- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job observed waiting 14h20m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job observed waiting 14h20m (> 2h00m)
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

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
