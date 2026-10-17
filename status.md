# Status detail

_Updated: 2026-10-17 03:50 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `macos-15` | github-hosted | 2 | 0 | — | — | 0 | — | 6s | [6s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058803) | [7s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058786) | [7s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058786) | 0% (0/2) | — | 2 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | — | 4s | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058721) | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058800) | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058800) | 33% (1/3) | — | 3 |  |
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 1 | [1m19s](https://github.com/iree-org/iree/actions/runs/39026329531/job/117377925622) | 1s | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058812) | [2s](https://github.com/iree-org/iree/actions/runs/39026329531/job/117377925622) | [2s](https://github.com/iree-org/iree/actions/runs/39026329531/job/117377925622) | 0% (0/10) | 0% (0/2) | 11 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058822) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058861) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058861) | 0% (0/2) | — | 2 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | github-hosted | 1 | 0 | — | — | 0 | 7s | [7s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058786) | [7s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058786) | [7s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058786) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | github-hosted | 1 | 0 | — | — | 0 | 6s | [6s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058803) | [6s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058803) | [6s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058803) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058800) | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058800) | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058800) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058721) | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058721) | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058721) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058710) | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058710) | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058710) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117377688428) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117377688428) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117377688428) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058812) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058812) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058812) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058756) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058756) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058756) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058769) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058769) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058769) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058778) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058778) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058778) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058861) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058861) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058861) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058822) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058822) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058822) | 1 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39018618086/job/117355734086) | [2s](https://github.com/iree-org/iree/actions/runs/39018618086/job/117355734086) | [2s](https://github.com/iree-org/iree/actions/runs/39018618086/job/117355734086) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39026329531/job/117377925622) | [2s](https://github.com/iree-org/iree/actions/runs/39026329531/job/117377925622) | [2s](https://github.com/iree-org/iree/actions/runs/39026329531/job/117377925622) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39026251833/job/117377904575) | [2s](https://github.com/iree-org/iree/actions/runs/39026251833/job/117377904575) | [2s](https://github.com/iree-org/iree/actions/runs/39026251833/job/117377904575) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/39026251833/job/117377705328) | [2s](https://github.com/iree-org/iree/actions/runs/39026251833/job/117377705328) | [2s](https://github.com/iree-org/iree/actions/runs/39026251833/job/117377705328) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317025406) | [1s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317025406) | [1s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317025406) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/39005471531/job/117316931820) | [1s](https://github.com/iree-org/iree/actions/runs/39005471531/job/117316931820) | [1s](https://github.com/iree-org/iree/actions/runs/39005471531/job/117316931820) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 261 | 249 | 11 | 1 | 4% |  | 18h28m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 212 | 209 | 2 | 1 | 1% |  | 18h35m ago |

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
