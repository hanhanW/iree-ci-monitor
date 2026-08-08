# Status detail

_Updated: 2026-08-08 06:13 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | — | 4s | [3s](https://github.com/iree-org/iree/actions/runs/31254589026/job/93096003561) | [9s](https://github.com/iree-org/iree/actions/runs/31254800013/job/93096528880) | [9s](https://github.com/iree-org/iree/actions/runs/31254800013/job/93096528880) | 22% (2/9) | — | 9 |  |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 0 | — | 3s | [2s](https://github.com/iree-org/iree/actions/runs/31254565181/job/93095939908) | [8s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934969) | [8s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934969) | 0% (0/10) | 0% (0/1) | 10 |  |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934984) | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934993) | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934993) | 0% (0/2) | — | 2 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | — | 1s | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934965) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934968) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934968) | 33% (1/3) | — | 3 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | — | 1s | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934970) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934982) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934982) | 0% (0/2) | — | 2 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 9s | [9s](https://github.com/iree-org/iree/actions/runs/31254800013/job/93096528880) | [9s](https://github.com/iree-org/iree/actions/runs/31254800013/job/93096528880) | [9s](https://github.com/iree-org/iree/actions/runs/31254800013/job/93096528880) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934969) | [8s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934969) | [8s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934969) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934967) | [8s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934967) | [8s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934967) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/31254800013/job/93096506855) | [8s](https://github.com/iree-org/iree/actions/runs/31254800013/job/93096506855) | [8s](https://github.com/iree-org/iree/actions/runs/31254800013/job/93096506855) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/31254800013/job/93096528872) | [8s](https://github.com/iree-org/iree/actions/runs/31254800013/job/93096528872) | [8s](https://github.com/iree-org/iree/actions/runs/31254800013/job/93096528872) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93095823835) | [4s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93095823835) | [4s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93095823835) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31254800216/job/93096507485) | [3s](https://github.com/iree-org/iree/actions/runs/31254589026/job/93096003561) | [3s](https://github.com/iree-org/iree/actions/runs/31254589026/job/93096003561) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/31254589026/job/93096003517) | [3s](https://github.com/iree-org/iree/actions/runs/31254800216/job/93096507451) | [3s](https://github.com/iree-org/iree/actions/runs/31254800216/job/93096507451) | 2 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934960) | [3s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934960) | [3s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934960) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/31254522282/job/93095927059) | [3s](https://github.com/iree-org/iree/actions/runs/31254522282/job/93095927059) | [3s](https://github.com/iree-org/iree/actions/runs/31254522282/job/93095927059) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31254589026/job/93096003536) | [2s](https://github.com/iree-org/iree/actions/runs/31254800216/job/93096507442) | [2s](https://github.com/iree-org/iree/actions/runs/31254800216/job/93096507442) | 2 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934971) | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934971) | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934971) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934984) | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934984) | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934984) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934993) | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934993) | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934993) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062917006) | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062917006) | [2s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062917006) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31254565181/job/93095939908) | [2s](https://github.com/iree-org/iree/actions/runs/31254565181/job/93095939908) | [2s](https://github.com/iree-org/iree/actions/runs/31254565181/job/93095939908) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31241383999/job/93062848102) | [2s](https://github.com/iree-org/iree/actions/runs/31241383999/job/93062848102) | [2s](https://github.com/iree-org/iree/actions/runs/31241383999/job/93062848102) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934963) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934963) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934963) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934968) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934968) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934968) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934965) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934965) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934965) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934970) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934970) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934970) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934982) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934982) | [1s](https://github.com/iree-org/iree/actions/runs/31241409864/job/93062934982) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/31254522282/job/93095835448) | [1s](https://github.com/iree-org/iree/actions/runs/31254522282/job/93095835448) | [1s](https://github.com/iree-org/iree/actions/runs/31254522282/job/93095835448) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 102 | 96 | 3 | 3 | 3% |  | 13h54m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 116 | 109 | 4 | 3 | 3% |  | 19h34m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 131 | 130 | 0 | 1 | 0% |  | 19h45m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 100 | 93 | 5 | 2 | 5% |  | 19h49m ago |

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
