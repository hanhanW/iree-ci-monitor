# Status detail

_Updated: 2026-05-18 00:45 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [1h15m](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426302) | 3s | [3s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426302) | [4s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426317) | [4s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426317) | 0% (0/1) | — | 2 |  |
| `ubuntu-24.04` | github-hosted | 11 | 2 | [4h53m](https://github.com/iree-org/iree/actions/runs/25907295889/job/76143183087) | 2026-05-15 05:58 PDT | 2 | [1h15m](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426299) | 1s | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470402410) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426323) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426323) | 29% (2/7) | 50% (2/4) | 9 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 1 | [1h15m](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426307) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426307) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426324) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426324) | 50% (1/2) | — | 3 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [1h15m](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426320) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426313) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426320) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426320) | 0% (0/1) | — | 2 |  |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [4h53m](https://github.com/iree-org/iree/actions/runs/25907295889/job/76143183087) | 2026-05-15 05:58 PDT | `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | `users/keshavvinayak01/gpuvectoralloc-swizzle` | pull_request |
| [4h53m](https://github.com/iree-org/iree/actions/runs/25907295886/job/76143196900) | 2026-05-15 05:58 PDT | `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | `users/keshavvinayak01/gpuvectoralloc-swizzle` | pull_request |

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | github-hosted | 1 | 1 | [4h53m](https://github.com/iree-org/iree/actions/runs/25907295889/job/76143183087) | 2026-05-15 05:58 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | github-hosted | 1 | 1 | [4h53m](https://github.com/iree-org/iree/actions/runs/25907295886/job/76143196900) | 2026-05-15 05:58 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426317) | [4s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426317) | [4s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426317) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426302) | [3s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426302) | [3s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426302) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426307) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426307) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426307) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426324) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426324) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426324) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426291) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426291) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426291) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426312) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426312) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426312) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426299) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426299) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426299) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426305) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426305) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426305) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426323) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426323) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426323) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470402410) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470402410) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470402410) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426320) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426320) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426320) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426313) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426313) | [2s](https://github.com/iree-org/iree/actions/runs/26017376956/job/76470426313) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26015470241/job/76464514225) | [2s](https://github.com/iree-org/iree/actions/runs/26015470241/job/76464514225) | [2s](https://github.com/iree-org/iree/actions/runs/26015470241/job/76464514225) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26015470241/job/76465397516) | [2s](https://github.com/iree-org/iree/actions/runs/26015470241/job/76465397516) | [2s](https://github.com/iree-org/iree/actions/runs/26015470241/job/76465397516) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26017347263/job/76470307584) | [2s](https://github.com/iree-org/iree/actions/runs/26017347263/job/76470307584) | [2s](https://github.com/iree-org/iree/actions/runs/26017347263/job/76470307584) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/26015470241/job/76464514259) | [1s](https://github.com/iree-org/iree/actions/runs/26015470241/job/76464514259) | [1s](https://github.com/iree-org/iree/actions/runs/26015470241/job/76464514259) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1095 | 1056 | 22 | 15 | 2% | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,shark55-ci`, `self-hosted,persistent-cache,Linux,X64` | 856 | 820 | 11 | 25 | 1% |  | 1d06h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 972 | 898 | 56 | 18 | 6% |  | 1d07h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,shark01-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 892 | 856 | 11 | 25 | 1% |  | 1d07h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 299 | 277 | 5 | 17 | 2% |  | 1d07h ago |

## Alerts

- **[stale-queued]** `ubuntu-24.04` oldest queued job observed waiting 4h53m (> 2h00m)

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
