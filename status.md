# Status detail

_Updated: 2026-06-04 06:28 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | — | 1m25s | [1m25s](https://github.com/iree-org/iree/actions/runs/26946175694/job/79499591877) | [1m25s](https://github.com/iree-org/iree/actions/runs/26946175694/job/79499591877) | [1m25s](https://github.com/iree-org/iree/actions/runs/26946175694/job/79499591877) | 0% (0/1) | 0% (0/1) | 1 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | — | 6s | [6s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277161) | [7s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277202) | [7s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277202) | 0% (0/3) | — | 3 |  |
| `ubuntu-24.04` | github-hosted | 15 | 0 | — | — | 2 | [3h00m](https://github.com/iree-org/iree/actions/runs/26946172053/job/79499580716) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277145) | [3s](https://github.com/iree-org/iree/actions/runs/26949639584/job/79511321449) | [4s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277291) | 23% (3/13) | 50% (2/4) | 15 |  |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26946162366/job/79499547725) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277165) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277165) | 0% (0/3) | 0% (0/1) | 3 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | — | 3s | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277185) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277188) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277188) | 0% (0/2) | — | 2 |  |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26949665050/job/79511415263) | [3s](https://github.com/iree-org/iree/actions/runs/26949665050/job/79511415249) | [3s](https://github.com/iree-org/iree/actions/runs/26949665050/job/79511415249) | 0% (0/3) | — | 3 |  |
| `azure-linux-scale` | ossci | 2 | 0 | — | — | 0 | — | 1s | [1s](https://github.com/iree-org/iree/actions/runs/26946170748/job/79499576084) | [2s](https://github.com/iree-org/iree/actions/runs/26946148701/job/79499500413) | [2s](https://github.com/iree-org/iree/actions/runs/26946148701/job/79499500413) | 0% (0/2) | 0% (0/2) | 2 |  |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [3h00m](https://github.com/iree-org/iree/actions/runs/26946159967/job/79499538990) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26946159967/job/79499538990) | [2s](https://github.com/iree-org/iree/actions/runs/26946159967/job/79499538990) | [2s](https://github.com/iree-org/iree/actions/runs/26946159967/job/79499538990) | — | — | 1 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | 1m25s | [1m25s](https://github.com/iree-org/iree/actions/runs/26946175694/job/79499591877) | [1m25s](https://github.com/iree-org/iree/actions/runs/26946175694/job/79499591877) | [1m25s](https://github.com/iree-org/iree/actions/runs/26946175694/job/79499591877) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 7s | [7s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277202) | [7s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277202) | [7s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277202) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 6s | [6s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277161) | [6s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277161) | [6s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277161) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277226) | [5s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277226) | [5s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277226) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277291) | [4s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277291) | [4s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277291) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277206) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277206) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277206) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277180) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277180) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277180) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277165) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277165) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277165) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277188) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277188) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277188) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277185) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277185) | [3s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277185) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/26949639584/job/79511321449) | [3s](https://github.com/iree-org/iree/actions/runs/26949639584/job/79511321449) | [3s](https://github.com/iree-org/iree/actions/runs/26949639584/job/79511321449) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/26949544597/job/79511005394) | [3s](https://github.com/iree-org/iree/actions/runs/26949544597/job/79511005394) | [3s](https://github.com/iree-org/iree/actions/runs/26949544597/job/79511005394) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/26949665050/job/79511415249) | [3s](https://github.com/iree-org/iree/actions/runs/26949665050/job/79511415249) | [3s](https://github.com/iree-org/iree/actions/runs/26949665050/job/79511415249) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79510982547) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79510982547) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79510982547) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277145) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277145) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277145) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277144) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277144) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463277144) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463251509) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463251509) | [2s](https://github.com/iree-org/iree/actions/runs/26935221744/job/79463251509) | 1 |
| `.github/workflows/ci_linux_x64_clang_debug.yml` | linux_x64_clang_debug | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26946148701/job/79499500413) | [2s](https://github.com/iree-org/iree/actions/runs/26946148701/job/79499500413) | [2s](https://github.com/iree-org/iree/actions/runs/26946148701/job/79499500413) | 1 |
| `.github/workflows/ci_macos_arm64_clang.yml` | macos_arm64_clang | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26946162366/job/79499547725) | [2s](https://github.com/iree-org/iree/actions/runs/26946162366/job/79499547725) | [2s](https://github.com/iree-org/iree/actions/runs/26946162366/job/79499547725) | 1 |
| `.github/workflows/ci_macos_x64_clang.yml` | macos_x64_clang | `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26946159967/job/79499538990) | [2s](https://github.com/iree-org/iree/actions/runs/26946159967/job/79499538990) | [2s](https://github.com/iree-org/iree/actions/runs/26946159967/job/79499538990) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26933406591/job/79457641566) | [2s](https://github.com/iree-org/iree/actions/runs/26933406591/job/79457641566) | [2s](https://github.com/iree-org/iree/actions/runs/26933406591/job/79457641566) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26933406591/job/79457641603) | [2s](https://github.com/iree-org/iree/actions/runs/26933406591/job/79457641603) | [2s](https://github.com/iree-org/iree/actions/runs/26933406591/job/79457641603) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26933406591/job/79458665926) | [2s](https://github.com/iree-org/iree/actions/runs/26933406591/job/79458665926) | [2s](https://github.com/iree-org/iree/actions/runs/26933406591/job/79458665926) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26935194498/job/79463161859) | [2s](https://github.com/iree-org/iree/actions/runs/26935194498/job/79463161859) | [2s](https://github.com/iree-org/iree/actions/runs/26935194498/job/79463161859) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26949544597/job/79511301589) | [2s](https://github.com/iree-org/iree/actions/runs/26949544597/job/79511301589) | [2s](https://github.com/iree-org/iree/actions/runs/26949544597/job/79511301589) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26949665050/job/79511415263) | [2s](https://github.com/iree-org/iree/actions/runs/26949665050/job/79511415263) | [2s](https://github.com/iree-org/iree/actions/runs/26949665050/job/79511415263) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26949665050/job/79511415225) | [2s](https://github.com/iree-org/iree/actions/runs/26949665050/job/79511415225) | [2s](https://github.com/iree-org/iree/actions/runs/26949665050/job/79511415225) | 1 |
| `.github/workflows/ci_linux_x64_clang_byollvm.yml` | linux_x64_clang_byollvm | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/26946172053/job/79499580716) | [1s](https://github.com/iree-org/iree/actions/runs/26946172053/job/79499580716) | [1s](https://github.com/iree-org/iree/actions/runs/26946172053/job/79499580716) | 1 |
| `.github/workflows/ci_linux_x64_clang_tsan.yml` | linux_x64_clang_tsan | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/26946170748/job/79499576084) | [1s](https://github.com/iree-org/iree/actions/runs/26946170748/job/79499576084) | [1s](https://github.com/iree-org/iree/actions/runs/26946170748/job/79499576084) | 1 |
| `.github/workflows/ci_linux_x64_gcc.yml` | linux_x64_gcc | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/26946179588/job/79499604983) | [1s](https://github.com/iree-org/iree/actions/runs/26946179588/job/79499604983) | [1s](https://github.com/iree-org/iree/actions/runs/26946179588/job/79499604983) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 274 | 260 | 11 | 2 | 4% | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 301 | 298 | 1 | 2 | 0% |  | 16h42m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 208 | 204 | 2 | 2 | 1% |  | 16h47m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 212 | 211 | 0 | 1 | 0% |  | 16h56m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 68 | 66 | 1 | 1 | 1% |  | 16h59m ago |

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
