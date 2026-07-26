# Status detail

_Updated: 2026-07-26 05:41 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550890) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762534108) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762534108) | 0% (0/10) | 0% (0/1) | 10 |  |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550857) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550868) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550868) | 0% (0/2) | — | 2 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550882) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550871) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550871) | 0% (0/3) | — | 3 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550896) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550918) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550918) | 0% (0/2) | — | 2 |  |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30201166036/job/89791232654) | [3s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791246729) | [3s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791246729) | 33% (2/6) | — | 6 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550871) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550871) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550871) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550868) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550868) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550868) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762534108) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762534108) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762534108) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550918) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550918) | [3s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550918) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791246729) | [3s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791246729) | [3s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791246729) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791246703) | [3s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791246703) | [3s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791246703) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89790618255) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89790618255) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89790618255) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550882) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550882) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550882) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550879) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550879) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550879) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550887) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550887) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550887) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550877) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550877) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550877) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550890) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550890) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550890) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550864) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550864) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550864) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550857) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550857) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550857) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550896) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550896) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89762550896) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30200981179/job/89790751679) | [2s](https://github.com/iree-org/iree/actions/runs/30200981179/job/89790751679) | [2s](https://github.com/iree-org/iree/actions/runs/30200981179/job/89790751679) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30190387204/job/89762484443) | [2s](https://github.com/iree-org/iree/actions/runs/30190387204/job/89762484443) | [2s](https://github.com/iree-org/iree/actions/runs/30190387204/job/89762484443) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30200932816/job/89790742626) | [2s](https://github.com/iree-org/iree/actions/runs/30200932816/job/89790742626) | [2s](https://github.com/iree-org/iree/actions/runs/30200932816/job/89790742626) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30200932816/job/89790627825) | [2s](https://github.com/iree-org/iree/actions/runs/30200932816/job/89790627825) | [2s](https://github.com/iree-org/iree/actions/runs/30200932816/job/89790627825) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30201166036/job/89791232679) | [2s](https://github.com/iree-org/iree/actions/runs/30201166036/job/89791232679) | [2s](https://github.com/iree-org/iree/actions/runs/30201166036/job/89791232679) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30201166036/job/89791232654) | [2s](https://github.com/iree-org/iree/actions/runs/30201166036/job/89791232654) | [2s](https://github.com/iree-org/iree/actions/runs/30201166036/job/89791232654) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30201166036/job/89791232641) | [2s](https://github.com/iree-org/iree/actions/runs/30201166036/job/89791232641) | [2s](https://github.com/iree-org/iree/actions/runs/30201166036/job/89791232641) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791231661) | [2s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791231661) | [2s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791231661) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 269 | 263 | 3 | 3 | 1% |  | 1d20h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 368 | 360 | 5 | 3 | 1% |  | 1d20h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 300 | 283 | 14 | 3 | 5% |  | 1d20h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 281 | 274 | 2 | 5 | 1% |  | 1d20h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 84 | 82 | 1 | 1 | 1% |  | 1d20h ago |

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
