# Status detail

_Updated: 2026-10-16 04:30 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | — | 1m27s | [1m27s](https://github.com/iree-org/iree/actions/runs/38880538118/job/116905924365) | [1m27s](https://github.com/iree-org/iree/actions/runs/38880538118/job/116905924365) | [1m27s](https://github.com/iree-org/iree/actions/runs/38880538118/job/116905924365) | 100% (1/1) | 100% (1/1) | 1 |  |
| `macos-15` | github-hosted | 3 | 0 | — | — | 1 | [2h03m](https://github.com/iree-org/iree/actions/runs/38880503077/job/116905814179) | 7s | [8s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914572) | [9s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914622) | [9s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914622) | 0% (0/2) | — | 3 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | — | 4s | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914490) | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914547) | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914547) | 33% (1/3) | — | 3 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914514) | [3s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914553) | [3s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914553) | 0% (0/2) | — | 2 |  |
| `ubuntu-24.04` | github-hosted | 15 | 0 | — | — | 2 | [2h03m](https://github.com/iree-org/iree/actions/runs/38880544587/job/116905946887) | 1s | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914463) | [2s](https://github.com/iree-org/iree/actions/runs/38889579599/job/116935541697) | [3s](https://github.com/iree-org/iree/actions/runs/38889459393/job/116935497970) | 0% (0/13) | 0% (0/4) | 15 |  |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/38889652351/job/116935775545) | [2s](https://github.com/iree-org/iree/actions/runs/38889652351/job/116935775598) | [2s](https://github.com/iree-org/iree/actions/runs/38889652351/job/116935775598) | 0% (0/3) | — | 3 |  |
| `azure-linux-scale` | ossci | 2 | 0 | — | — | 0 | — | 1s | [1s](https://github.com/iree-org/iree/actions/runs/38880407535/job/116905500361) | [1s](https://github.com/iree-org/iree/actions/runs/38880527065/job/116905889447) | [1s](https://github.com/iree-org/iree/actions/runs/38880527065/job/116905889447) | 50% (1/2) | 50% (1/2) | 2 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | 1m27s | [1m27s](https://github.com/iree-org/iree/actions/runs/38880538118/job/116905924365) | [1m27s](https://github.com/iree-org/iree/actions/runs/38880538118/job/116905924365) | [1m27s](https://github.com/iree-org/iree/actions/runs/38880538118/job/116905924365) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | github-hosted | 1 | 0 | — | — | 0 | 9s | [9s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914622) | [9s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914622) | [9s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914622) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | github-hosted | 1 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914572) | [8s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914572) | [8s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914572) | 1 |
| `.github/workflows/ci_macos_arm64_clang.yml` | macos_arm64_clang | `macos-15` | github-hosted | 1 | 0 | — | — | 1 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/38880503077/job/116905814179) | [5s](https://github.com/iree-org/iree/actions/runs/38880503077/job/116905814179) | [5s](https://github.com/iree-org/iree/actions/runs/38880503077/job/116905814179) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914547) | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914547) | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914547) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914485) | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914485) | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914485) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914490) | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914490) | [4s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914490) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914553) | [3s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914553) | [3s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914553) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/38889459393/job/116935497970) | [3s](https://github.com/iree-org/iree/actions/runs/38889459393/job/116935497970) | [3s](https://github.com/iree-org/iree/actions/runs/38889459393/job/116935497970) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116935108768) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116935108768) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116935108768) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914463) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914463) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914463) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914509) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914509) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914509) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914541) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914541) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914541) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914462) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914462) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914462) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914514) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914514) | [2s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823914514) | 1 |
| `.github/workflows/ci_linux_x64_clang_byollvm.yml` | linux_x64_clang_byollvm | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/38880544587/job/116905946887) | [2s](https://github.com/iree-org/iree/actions/runs/38880544587/job/116905946887) | [2s](https://github.com/iree-org/iree/actions/runs/38880544587/job/116905946887) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/38889579599/job/116935541697) | [2s](https://github.com/iree-org/iree/actions/runs/38889579599/job/116935541697) | [2s](https://github.com/iree-org/iree/actions/runs/38889579599/job/116935541697) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/38850278649/job/116809753046) | [2s](https://github.com/iree-org/iree/actions/runs/38850278649/job/116809753046) | [2s](https://github.com/iree-org/iree/actions/runs/38850278649/job/116809753046) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/38850278649/job/116809753158) | [2s](https://github.com/iree-org/iree/actions/runs/38850278649/job/116809753158) | [2s](https://github.com/iree-org/iree/actions/runs/38850278649/job/116809753158) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/38850278649/job/116811684268) | [2s](https://github.com/iree-org/iree/actions/runs/38850278649/job/116811684268) | [2s](https://github.com/iree-org/iree/actions/runs/38850278649/job/116811684268) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/38854772710/job/116823673860) | [2s](https://github.com/iree-org/iree/actions/runs/38854772710/job/116823673860) | [2s](https://github.com/iree-org/iree/actions/runs/38854772710/job/116823673860) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/38889459393/job/116935147978) | [2s](https://github.com/iree-org/iree/actions/runs/38889459393/job/116935147978) | [2s](https://github.com/iree-org/iree/actions/runs/38889459393/job/116935147978) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/38889652351/job/116935775598) | [2s](https://github.com/iree-org/iree/actions/runs/38889652351/job/116935775598) | [2s](https://github.com/iree-org/iree/actions/runs/38889652351/job/116935775598) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/38889652351/job/116935775545) | [2s](https://github.com/iree-org/iree/actions/runs/38889652351/job/116935775545) | [2s](https://github.com/iree-org/iree/actions/runs/38889652351/job/116935775545) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/38889652351/job/116935775325) | [2s](https://github.com/iree-org/iree/actions/runs/38889652351/job/116935775325) | [2s](https://github.com/iree-org/iree/actions/runs/38889652351/job/116935775325) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823860960) | [1s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823860960) | [1s](https://github.com/iree-org/iree/actions/runs/38854834447/job/116823860960) | 1 |
| `.github/workflows/ci_linux_x64_clang_debug.yml` | linux_x64_clang_debug | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/38880407535/job/116905500361) | [1s](https://github.com/iree-org/iree/actions/runs/38880407535/job/116905500361) | [1s](https://github.com/iree-org/iree/actions/runs/38880407535/job/116905500361) | 1 |
| `.github/workflows/ci_linux_x64_clang_tsan.yml` | linux_x64_clang_tsan | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/38880527065/job/116905889447) | [1s](https://github.com/iree-org/iree/actions/runs/38880527065/job/116905889447) | [1s](https://github.com/iree-org/iree/actions/runs/38880527065/job/116905889447) | 1 |
| `.github/workflows/ci_linux_x64_gcc.yml` | linux_x64_gcc | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/38880558912/job/116905992658) | [1s](https://github.com/iree-org/iree/actions/runs/38880558912/job/116905992658) | [1s](https://github.com/iree-org/iree/actions/runs/38880558912/job/116905992658) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 243 | 240 | 2 | 1 | 1% |  | 12h04m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 303 | 284 | 18 | 1 | 6% |  | 12h12m ago |

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
