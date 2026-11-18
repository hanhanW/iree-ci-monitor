# Status detail

_Updated: 2026-11-17 23:36 PST_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [2h26m](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181395) | 4s | [4s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181431) | [5s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181442) | [5s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181442) | 0% (0/1) | — | 3 |  |
| `ubuntu-24.04` | github-hosted | 15 | 0 | — | — | 2 | [2h26m](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181323) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134575272978) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181398) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181528) | 8% (1/13) | 0% (0/6) | 15 |  |
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [2h26m](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181470) | 3s | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181401) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181470) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181470) | 0% (0/1) | — | 2 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2h26m](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181471) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181471) | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181535) | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181535) | 0% (0/1) | — | 2 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181442) | [5s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181442) | [5s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181442) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181431) | [4s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181431) | [4s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181431) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 1 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181395) | [4s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181395) | [4s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181395) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | github-hosted | 5 | 0 | — | — | 0 | 1s | [2s](https://github.com/iree-org/iree/actions/runs/44101886801/job/134447047576) | [3s](https://github.com/iree-org/iree/actions/runs/44130381409/job/134441097183) | [3s](https://github.com/iree-org/iree/actions/runs/44130381409/job/134441097183) | 5 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181323) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181323) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181323) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181398) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181398) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181398) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181380) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181380) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181380) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181528) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181528) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181528) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181470) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181470) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181470) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181401) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181401) | [3s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181401) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593047805) | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593047805) | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593047805) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181471) | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181471) | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181471) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181535) | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181535) | [2s](https://github.com/iree-org/iree/actions/runs/44242360795/job/134593181535) | 1 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/44228612446/job/134547846965) | [2s](https://github.com/iree-org/iree/actions/runs/44228612446/job/134547846965) | [2s](https://github.com/iree-org/iree/actions/runs/44228612446/job/134547846965) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134572037536) | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134572037536) | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134572037536) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134572037844) | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134572037844) | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134572037844) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134575272978) | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134575272978) | [2s](https://github.com/iree-org/iree/actions/runs/44235959215/job/134575272978) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/44242266866/job/134592747071) | [2s](https://github.com/iree-org/iree/actions/runs/44242266866/job/134592747071) | [2s](https://github.com/iree-org/iree/actions/runs/44242266866/job/134592747071) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 363 | 361 | 0 | 2 | 0% |  | 6h51m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 311 | 306 | 2 | 3 | 1% |  | 12h51m ago |

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
