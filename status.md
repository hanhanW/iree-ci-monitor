# Status detail

_Updated: 2026-08-09 06:17 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192026) | [4s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238205510) | [4s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238205510) | 33% (2/6) | — | 6 |  |
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31300078753/job/93211336687) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93237398831) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93237398831) | 0% (0/11) | 0% (0/1) | 11 |  |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625407) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625403) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625403) | 0% (0/2) | — | 2 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | — | 1s | [1s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625456) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625414) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625414) | 0% (0/3) | — | 3 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | — | 1s | [1s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625451) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625427) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625427) | 0% (0/2) | — | 2 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238205510) | [4s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238205510) | [4s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238205510) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93237398831) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93237398831) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93237398831) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625387) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625387) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625387) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625403) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625403) | [3s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625403) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/31296581323/job/93202535787) | [3s](https://github.com/iree-org/iree/actions/runs/31296581323/job/93202535787) | [3s](https://github.com/iree-org/iree/actions/runs/31296581323/job/93202535787) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192054) | [3s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192054) | [3s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192054) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625414) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625414) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625414) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625433) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625433) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625433) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625420) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625420) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625420) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625407) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625407) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625407) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202607167) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202607167) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202607167) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625427) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625427) | [2s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625427) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31310511395/job/93237511997) | [2s](https://github.com/iree-org/iree/actions/runs/31310511395/job/93237511997) | [2s](https://github.com/iree-org/iree/actions/runs/31310511395/job/93237511997) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31300078753/job/93211336687) | [2s](https://github.com/iree-org/iree/actions/runs/31300078753/job/93211336687) | [2s](https://github.com/iree-org/iree/actions/runs/31300078753/job/93211336687) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31310469503/job/93237501391) | [2s](https://github.com/iree-org/iree/actions/runs/31310469503/job/93237501391) | [2s](https://github.com/iree-org/iree/actions/runs/31310469503/job/93237501391) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192036) | [2s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192036) | [2s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192036) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192026) | [2s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192026) | [2s](https://github.com/iree-org/iree/actions/runs/31310785620/job/93238192026) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238190872) | [2s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238190872) | [2s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238190872) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238205522) | [2s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238205522) | [2s](https://github.com/iree-org/iree/actions/runs/31310785289/job/93238205522) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625456) | [1s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625456) | [1s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625456) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625391) | [1s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625391) | [1s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625391) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625416) | [1s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625416) | [1s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625416) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625451) | [1s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625451) | [1s](https://github.com/iree-org/iree/actions/runs/31296607043/job/93202625451) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/31310469503/job/93237410616) | [1s](https://github.com/iree-org/iree/actions/runs/31310469503/job/93237410616) | [1s](https://github.com/iree-org/iree/actions/runs/31310469503/job/93237410616) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 102 | 96 | 3 | 3 | 3% |  | 1d13h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 116 | 109 | 4 | 3 | 3% |  | 1d19h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 131 | 130 | 0 | 1 | 0% |  | 1d19h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 100 | 93 | 5 | 2 | 5% |  | 1d19h ago |

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
