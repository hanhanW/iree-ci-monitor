# Status detail

_Updated: 2026-06-27 11:43 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 5 | [3m59s](https://github.com/iree-org/iree/actions/runs/28298243961/job/83841870375) | 27s | [7s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873394) | [1m44s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873372) | [1m44s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873372) | — | — | 5 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | — | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873136) | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873141) | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873141) | 0% (0/3) | — | 3 |  |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28292217526/job/83826041223) | [3s](https://github.com/iree-org/iree/actions/runs/28292217526/job/83826041214) | [4s](https://github.com/iree-org/iree/actions/runs/28292217241/job/83826052391) | 33% (4/12) | — | 12 |  |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | — | 2s | [3s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873143) | [3s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873146) | [3s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873146) | 0% (0/3) | — | 3 |  |
| `ubuntu-24.04` | github-hosted | 13 | 0 | — | — | 1 | [3m57s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873132) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873097) | [2s](https://github.com/iree-org/iree/actions/runs/28298243961/job/83841858393) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83816303965) | 8% (1/12) | 0% (0/1) | 13 |  |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 3 | [3m57s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873093) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873140) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873145) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873145) | — | — | 3 |  |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 1 | [3m57s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873409) | 1s | [1s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873409) | [1s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873409) | [1s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873409) | — | — | 1 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | ossci | 1 | 0 | — | — | 1 | 1m44s | [1m44s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873372) | [1m44s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873372) | [1m44s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873372) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | ossci | 1 | 0 | — | — | 1 | 20s | [20s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873398) | [20s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873398) | [20s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873398) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | ossci | 1 | 0 | — | — | 1 | 7s | [7s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873394) | [7s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873394) | [7s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873394) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | ossci | 1 | 0 | — | — | 1 | 6s | [6s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873382) | [6s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873382) | [6s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873382) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873092) | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873092) | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873092) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873141) | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873141) | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873141) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873136) | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873136) | [5s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873136) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 3s | [2s](https://github.com/iree-org/iree/actions/runs/28288606734/job/83816692575) | [4s](https://github.com/iree-org/iree/actions/runs/28292217241/job/83826052391) | [4s](https://github.com/iree-org/iree/actions/runs/28292217241/job/83826052391) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28288606832/job/83816683755) | [3s](https://github.com/iree-org/iree/actions/runs/28292217526/job/83826041198) | [3s](https://github.com/iree-org/iree/actions/runs/28292217526/job/83826041198) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/28288606832/job/83816683747) | [3s](https://github.com/iree-org/iree/actions/runs/28292217526/job/83826041214) | [3s](https://github.com/iree-org/iree/actions/runs/28292217526/job/83826041214) | 2 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [1s](https://github.com/iree-org/iree/actions/runs/28288606734/job/83816683153) | [3s](https://github.com/iree-org/iree/actions/runs/28292217241/job/83826040933) | [3s](https://github.com/iree-org/iree/actions/runs/28292217241/job/83826040933) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83816303965) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83816303965) | [3s](https://github.com/iree-org/iree/actions/runs/28280906001/job/83816303965) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873146) | [3s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873146) | [3s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873146) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873143) | [3s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873143) | [3s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873143) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28288489550/job/83816387516) | [2s](https://github.com/iree-org/iree/actions/runs/28292065298/job/83825632975) | [2s](https://github.com/iree-org/iree/actions/runs/28292065298/job/83825632975) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28288606832/job/83816683748) | [2s](https://github.com/iree-org/iree/actions/runs/28292217526/job/83826041223) | [2s](https://github.com/iree-org/iree/actions/runs/28292217526/job/83826041223) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28288606734/job/83816692581) | [2s](https://github.com/iree-org/iree/actions/runs/28292217241/job/83826052387) | [2s](https://github.com/iree-org/iree/actions/runs/28292217241/job/83826052387) | 2 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873088) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873088) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873088) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873097) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873097) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873097) | 1 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873093) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873093) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873093) | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873132) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873132) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873132) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873134) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873134) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873134) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873137) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873137) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873137) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873140) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873140) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873140) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873145) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873145) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873145) | 1 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873133) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873133) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873133) | 1 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841858464) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841858464) | [2s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841858464) | 1 |
| `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28298243870/job/83841858042) | [2s](https://github.com/iree-org/iree/actions/runs/28298243870/job/83841858042) | [2s](https://github.com/iree-org/iree/actions/runs/28298243870/job/83841858042) | 1 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28298243961/job/83841858393) | [2s](https://github.com/iree-org/iree/actions/runs/28298243961/job/83841858393) | [2s](https://github.com/iree-org/iree/actions/runs/28298243961/job/83841858393) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28288458973/job/83816310448) | [2s](https://github.com/iree-org/iree/actions/runs/28288458973/job/83816310448) | [2s](https://github.com/iree-org/iree/actions/runs/28288458973/job/83816310448) | 1 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | ossci | 1 | 0 | — | — | 1 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873409) | [1s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873409) | [1s](https://github.com/iree-org/iree/actions/runs/28298243923/job/83841873409) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | ossci | 1 | 0 | — | — | 1 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/28298243961/job/83841870375) | [1s](https://github.com/iree-org/iree/actions/runs/28298243961/job/83841870375) | [1s](https://github.com/iree-org/iree/actions/runs/28298243961/job/83841870375) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/28288458973/job/83816382666) | [1s](https://github.com/iree-org/iree/actions/runs/28288458973/job/83816382666) | [1s](https://github.com/iree-org/iree/actions/runs/28288458973/job/83816382666) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 119 | 119 | 0 | 0 | 0% |  | 23h33m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 95 | 87 | 8 | 0 | 8% |  | 23h43m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 91 | 91 | 0 | 0 | 0% |  | 23h45m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 85 | 85 | 0 | 0 | 0% |  | 23h46m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 26 | 26 | 0 | 0 | 0% |  | 23h54m ago |

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
