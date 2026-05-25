# Status detail

_Updated: 2026-05-25 06:29 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | — | 1m33s | [1m33s](https://github.com/iree-org/iree/actions/runs/26396555310/job/77698492908) | [1m33s](https://github.com/iree-org/iree/actions/runs/26396555310/job/77698492908) | [1m33s](https://github.com/iree-org/iree/actions/runs/26396555310/job/77698492908) | 100% (1/1) | 100% (1/1) | 1 |  |
| `ubuntu-24.04` | github-hosted | 15 | 0 | — | — | 2 | [2h42m](https://github.com/iree-org/iree/actions/runs/26396552354/job/77698483194) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539927) | [3s](https://github.com/iree-org/iree/actions/runs/26398972680/job/77706439006) | [4s](https://github.com/iree-org/iree/actions/runs/26385356346/job/77662624332) | 15% (2/13) | 50% (2/4) | 15 |  |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26399219224/job/77707148780) | [3s](https://github.com/iree-org/iree/actions/runs/26399219490/job/77707126664) | [3s](https://github.com/iree-org/iree/actions/runs/26399219490/job/77707126664) | 33% (2/6) | — | 6 |  |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [2h43m](https://github.com/iree-org/iree/actions/runs/26396531888/job/77698416930) | 3s | [3s](https://github.com/iree-org/iree/actions/runs/26396531888/job/77698416930) | [3s](https://github.com/iree-org/iree/actions/runs/26396531888/job/77698416930) | [3s](https://github.com/iree-org/iree/actions/runs/26396531888/job/77698416930) | — | — | 1 |  |
| `macos-14` | github-hosted | 3 | 0 | — | — | 1 | [2h42m](https://github.com/iree-org/iree/actions/runs/26396549640/job/77698475014) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539893) | [2s](https://github.com/iree-org/iree/actions/runs/26396549640/job/77698475014) | [2s](https://github.com/iree-org/iree/actions/runs/26396549640/job/77698475014) | 0% (0/2) | — | 3 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539896) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539908) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539908) | 33% (1/3) | — | 3 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539912) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539913) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539913) | 0% (0/2) | — | 2 |  |
| `azure-linux-scale` | ossci | 2 | 0 | — | — | 0 | — | 1s | [1s](https://github.com/iree-org/iree/actions/runs/26396516239/job/77698363588) | [1s](https://github.com/iree-org/iree/actions/runs/26396551209/job/77698479799) | [1s](https://github.com/iree-org/iree/actions/runs/26396551209/job/77698479799) | 0% (0/2) | 0% (0/2) | 2 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | 1m33s | [1m33s](https://github.com/iree-org/iree/actions/runs/26396555310/job/77698492908) | [1m33s](https://github.com/iree-org/iree/actions/runs/26396555310/job/77698492908) | [1m33s](https://github.com/iree-org/iree/actions/runs/26396555310/job/77698492908) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/26385356346/job/77662624332) | [4s](https://github.com/iree-org/iree/actions/runs/26385356346/job/77662624332) | [4s](https://github.com/iree-org/iree/actions/runs/26385356346/job/77662624332) | 1 |
| `.github/workflows/ci_macos_x64_clang.yml` | macos_x64_clang | `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/26396531888/job/77698416930) | [3s](https://github.com/iree-org/iree/actions/runs/26396531888/job/77698416930) | [3s](https://github.com/iree-org/iree/actions/runs/26396531888/job/77698416930) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/26398972680/job/77706439006) | [3s](https://github.com/iree-org/iree/actions/runs/26398972680/job/77706439006) | [3s](https://github.com/iree-org/iree/actions/runs/26398972680/job/77706439006) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/26399219490/job/77707126664) | [3s](https://github.com/iree-org/iree/actions/runs/26399219490/job/77707126664) | [3s](https://github.com/iree-org/iree/actions/runs/26399219490/job/77707126664) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/26399219490/job/77707126635) | [3s](https://github.com/iree-org/iree/actions/runs/26399219490/job/77707126635) | [3s](https://github.com/iree-org/iree/actions/runs/26399219490/job/77707126635) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77706318004) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77706318004) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77706318004) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539895) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539895) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539895) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539896) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539896) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539896) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539908) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539908) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539908) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539886) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539886) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539886) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539918) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539918) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539918) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539927) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539927) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539927) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539920) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539920) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539920) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539893) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539893) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539893) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539890) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539890) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539890) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667524020) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667524020) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667524020) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539913) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539913) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539913) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539912) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539912) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539912) | 1 |
| `.github/workflows/ci_linux_x64_clang_byollvm.yml` | linux_x64_clang_byollvm | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26396552354/job/77698483194) | [2s](https://github.com/iree-org/iree/actions/runs/26396552354/job/77698483194) | [2s](https://github.com/iree-org/iree/actions/runs/26396552354/job/77698483194) | 1 |
| `.github/workflows/ci_linux_x64_gcc.yml` | linux_x64_gcc | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26396558441/job/77698502223) | [2s](https://github.com/iree-org/iree/actions/runs/26396558441/job/77698502223) | [2s](https://github.com/iree-org/iree/actions/runs/26396558441/job/77698502223) | 1 |
| `.github/workflows/ci_macos_arm64_clang.yml` | macos_arm64_clang | `macos-14` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26396549640/job/77698475014) | [2s](https://github.com/iree-org/iree/actions/runs/26396549640/job/77698475014) | [2s](https://github.com/iree-org/iree/actions/runs/26396549640/job/77698475014) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26399011385/job/77706456458) | [2s](https://github.com/iree-org/iree/actions/runs/26399011385/job/77706456458) | [2s](https://github.com/iree-org/iree/actions/runs/26399011385/job/77706456458) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26385356346/job/77662624331) | [2s](https://github.com/iree-org/iree/actions/runs/26385356346/job/77662624331) | [2s](https://github.com/iree-org/iree/actions/runs/26385356346/job/77662624331) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26385356346/job/77663453566) | [2s](https://github.com/iree-org/iree/actions/runs/26385356346/job/77663453566) | [2s](https://github.com/iree-org/iree/actions/runs/26385356346/job/77663453566) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26386935891/job/77667448820) | [2s](https://github.com/iree-org/iree/actions/runs/26386935891/job/77667448820) | [2s](https://github.com/iree-org/iree/actions/runs/26386935891/job/77667448820) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26398972680/job/77706332571) | [2s](https://github.com/iree-org/iree/actions/runs/26398972680/job/77706332571) | [2s](https://github.com/iree-org/iree/actions/runs/26398972680/job/77706332571) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26399219490/job/77707126696) | [2s](https://github.com/iree-org/iree/actions/runs/26399219490/job/77707126696) | [2s](https://github.com/iree-org/iree/actions/runs/26399219490/job/77707126696) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26399219224/job/77707126399) | [2s](https://github.com/iree-org/iree/actions/runs/26399219224/job/77707126399) | [2s](https://github.com/iree-org/iree/actions/runs/26399219224/job/77707126399) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26399219224/job/77707148780) | [2s](https://github.com/iree-org/iree/actions/runs/26399219224/job/77707148780) | [2s](https://github.com/iree-org/iree/actions/runs/26399219224/job/77707148780) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/26399219224/job/77707148760) | [2s](https://github.com/iree-org/iree/actions/runs/26399219224/job/77707148760) | [2s](https://github.com/iree-org/iree/actions/runs/26399219224/job/77707148760) | 1 |
| `.github/workflows/ci_linux_x64_clang_debug.yml` | linux_x64_clang_debug | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/26396516239/job/77698363588) | [1s](https://github.com/iree-org/iree/actions/runs/26396516239/job/77698363588) | [1s](https://github.com/iree-org/iree/actions/runs/26396516239/job/77698363588) | 1 |
| `.github/workflows/ci_linux_x64_clang_tsan.yml` | linux_x64_clang_tsan | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/26396551209/job/77698479799) | [1s](https://github.com/iree-org/iree/actions/runs/26396551209/job/77698479799) | [1s](https://github.com/iree-org/iree/actions/runs/26396551209/job/77698479799) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 296 | 285 | 5 | 5 | 2% | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 266 | 240 | 20 | 5 | 8% | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 226 | 214 | 7 | 4 | 3% | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 220 | 210 | 2 | 7 | 1% | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 70 | 65 | 2 | 3 | 3% |  | 2d18h ago |

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
