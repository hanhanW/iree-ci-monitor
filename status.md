# Status detail

_Updated: 2026-09-07 05:40 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | — | 1m31s | [1m31s](https://github.com/iree-org/iree/actions/runs/34106670660/job/101693165399) | [1m31s](https://github.com/iree-org/iree/actions/runs/34106670660/job/101693165399) | [1m31s](https://github.com/iree-org/iree/actions/runs/34106670660/job/101693165399) | 0% (0/1) | 0% (0/1) | 1 |  |
| `macos-14` | github-hosted | 1 | 0 | — | — | 1 | [3h07m](https://github.com/iree-org/iree/actions/runs/34106658240/job/101693126531) | 8s | [8s](https://github.com/iree-org/iree/actions/runs/34106658240/job/101693126531) | [8s](https://github.com/iree-org/iree/actions/runs/34106658240/job/101693126531) | [8s](https://github.com/iree-org/iree/actions/runs/34106658240/job/101693126531) | — | — | 1 |  |
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 1 | [3h07m](https://github.com/iree-org/iree/actions/runs/34106675608/job/101693181063) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/34092747062/job/101649538002) | [3s](https://github.com/iree-org/iree/actions/runs/34111910863/job/101709857430) | [3s](https://github.com/iree-org/iree/actions/runs/34111910863/job/101709857430) | 30% (3/10) | 50% (3/6) | 11 |  |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711812476) | [3s](https://github.com/iree-org/iree/actions/runs/34112523409/job/101711773910) | [4s](https://github.com/iree-org/iree/actions/runs/34112523409/job/101711773762) | 17% (2/12) | 0% (0/3) | 12 |  |
| `azure-linux-scale` | ossci | 2 | 0 | — | — | 0 | — | 1s | [1s](https://github.com/iree-org/iree/actions/runs/34106590769/job/101692912456) | [1s](https://github.com/iree-org/iree/actions/runs/34106662954/job/101693140736) | [1s](https://github.com/iree-org/iree/actions/runs/34106662954/job/101693140736) | 0% (0/2) | 0% (0/2) | 2 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | 1m31s | [1m31s](https://github.com/iree-org/iree/actions/runs/34106670660/job/101693165399) | [1m31s](https://github.com/iree-org/iree/actions/runs/34106670660/job/101693165399) | [1m31s](https://github.com/iree-org/iree/actions/runs/34106670660/job/101693165399) | 1 |
| `.github/workflows/ci_macos_arm64_clang.yml` | macos_arm64_clang | `macos-14` | github-hosted | 1 | 0 | — | — | 1 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/34106658240/job/101693126531) | [8s](https://github.com/iree-org/iree/actions/runs/34106658240/job/101693126531) | [8s](https://github.com/iree-org/iree/actions/runs/34106658240/job/101693126531) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/34111972445/job/101710056265) | [4s](https://github.com/iree-org/iree/actions/runs/34112523409/job/101711773762) | [4s](https://github.com/iree-org/iree/actions/runs/34112523409/job/101711773762) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | 2s | [3s](https://github.com/iree-org/iree/actions/runs/34087813321/job/101635134204) | [3s](https://github.com/iree-org/iree/actions/runs/34112523409/job/101711773910) | [3s](https://github.com/iree-org/iree/actions/runs/34112523409/job/101711773910) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/34111972445/job/101710056512) | [3s](https://github.com/iree-org/iree/actions/runs/34112523409/job/101711773640) | [3s](https://github.com/iree-org/iree/actions/runs/34112523409/job/101711773640) | 3 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/34092747062/job/101649538002) | [3s](https://github.com/iree-org/iree/actions/runs/34088666173/job/101637554084) | [3s](https://github.com/iree-org/iree/actions/runs/34088666173/job/101637554084) | 2 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/34111910863/job/101709857430) | [3s](https://github.com/iree-org/iree/actions/runs/34111910863/job/101709857430) | [3s](https://github.com/iree-org/iree/actions/runs/34111910863/job/101709857430) | 1 |
| `.github/workflows/ci_linux_x64_clang_byollvm.yml` | linux_x64_clang_byollvm | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/34106675608/job/101693181063) | [2s](https://github.com/iree-org/iree/actions/runs/34106675608/job/101693181063) | [2s](https://github.com/iree-org/iree/actions/runs/34106675608/job/101693181063) | 1 |
| `.github/workflows/ci_linux_x64_gcc.yml` | linux_x64_gcc | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/34106680563/job/101693196548) | [2s](https://github.com/iree-org/iree/actions/runs/34106680563/job/101693196548) | [2s](https://github.com/iree-org/iree/actions/runs/34106680563/job/101693196548) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/34083008531/job/101621747818) | [2s](https://github.com/iree-org/iree/actions/runs/34083008531/job/101621747818) | [2s](https://github.com/iree-org/iree/actions/runs/34083008531/job/101621747818) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/34083008531/job/101621747903) | [2s](https://github.com/iree-org/iree/actions/runs/34083008531/job/101621747903) | [2s](https://github.com/iree-org/iree/actions/runs/34083008531/job/101621747903) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/34083008531/job/101623366660) | [2s](https://github.com/iree-org/iree/actions/runs/34083008531/job/101623366660) | [2s](https://github.com/iree-org/iree/actions/runs/34083008531/job/101623366660) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/34111819315/job/101709821986) | [2s](https://github.com/iree-org/iree/actions/runs/34111819315/job/101709821986) | [2s](https://github.com/iree-org/iree/actions/runs/34111819315/job/101709821986) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711770644) | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711770644) | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711770644) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711812476) | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711812476) | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711812476) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711812655) | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711812655) | [2s](https://github.com/iree-org/iree/actions/runs/34112522800/job/101711812655) | 1 |
| `.github/workflows/ci_linux_x64_clang_debug.yml` | linux_x64_clang_debug | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/34106590769/job/101692912456) | [1s](https://github.com/iree-org/iree/actions/runs/34106590769/job/101692912456) | [1s](https://github.com/iree-org/iree/actions/runs/34106590769/job/101692912456) | 1 |
| `.github/workflows/ci_linux_x64_clang_tsan.yml` | linux_x64_clang_tsan | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/34106662954/job/101693140736) | [1s](https://github.com/iree-org/iree/actions/runs/34106662954/job/101693140736) | [1s](https://github.com/iree-org/iree/actions/runs/34106662954/job/101693140736) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/34107484925/job/101695733703) | [1s](https://github.com/iree-org/iree/actions/runs/34107484925/job/101695733703) | [1s](https://github.com/iree-org/iree/actions/runs/34107484925/job/101695733703) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/34111819315/job/101709574559) | [1s](https://github.com/iree-org/iree/actions/runs/34111819315/job/101709574559) | [1s](https://github.com/iree-org/iree/actions/runs/34111819315/job/101709574559) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 129 | 127 | 2 | 0 | 2% |  | 15h54m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 86 | 86 | 0 | 0 | 0% |  | 16h30m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 107 | 101 | 5 | 1 | 5% |  | 16h37m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 97 | 97 | 0 | 0 | 0% |  | 16h38m ago |

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
