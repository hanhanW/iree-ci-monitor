# Status detail

_Updated: 2026-07-28 05:57 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | — | 2m21s | [2m21s](https://github.com/iree-org/iree/actions/runs/30349494988/job/90243373949) | [2m21s](https://github.com/iree-org/iree/actions/runs/30349494988/job/90243373949) | [2m21s](https://github.com/iree-org/iree/actions/runs/30349494988/job/90243373949) | 0% (0/1) | 0% (0/1) | 1 |  |
| `ubuntu-24.04` | github-hosted | 16 | 0 | — | — | 1 | [2h49m](https://github.com/iree-org/iree/actions/runs/30349495147/job/90243374666) | 3s | [2s](https://github.com/iree-org/iree/actions/runs/30349504039/job/90243402861) | [8s](https://github.com/iree-org/iree/actions/runs/30356232018/job/90264967233) | [9s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993236) | 7% (1/14) | 20% (1/5) | 15 |  |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | — | 4s | [3s](https://github.com/iree-org/iree/actions/runs/30356608481/job/90266171467) | [8s](https://github.com/iree-org/iree/actions/runs/30356275247/job/90265108665) | [8s](https://github.com/iree-org/iree/actions/runs/30356275247/job/90265108665) | 22% (2/9) | — | 9 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993221) | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993235) | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993235) | 0% (0/2) | — | 2 |  |
| `macos-14` | github-hosted | 3 | 0 | — | — | 1 | [2h50m](https://github.com/iree-org/iree/actions/runs/30349471136/job/90243294763) | 2s | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993391) | [3s](https://github.com/iree-org/iree/actions/runs/30349471136/job/90243294763) | [3s](https://github.com/iree-org/iree/actions/runs/30349471136/job/90243294763) | 0% (0/2) | — | 3 |  |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [2h50m](https://github.com/iree-org/iree/actions/runs/30349457314/job/90243249525) | 3s | [3s](https://github.com/iree-org/iree/actions/runs/30349457314/job/90243249525) | [3s](https://github.com/iree-org/iree/actions/runs/30349457314/job/90243249525) | [3s](https://github.com/iree-org/iree/actions/runs/30349457314/job/90243249525) | — | — | 1 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993250) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993260) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993260) | 33% (1/3) | — | 3 |  |
| `azure-linux-scale` | ossci | 2 | 0 | — | — | 0 | — | 1s | [1s](https://github.com/iree-org/iree/actions/runs/30349485701/job/90243342515) | [2s](https://github.com/iree-org/iree/actions/runs/30349405394/job/90243081062) | [2s](https://github.com/iree-org/iree/actions/runs/30349405394/job/90243081062) | 0% (0/2) | 0% (0/2) | 2 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | 2m21s | [2m21s](https://github.com/iree-org/iree/actions/runs/30349494988/job/90243373949) | [2m21s](https://github.com/iree-org/iree/actions/runs/30349494988/job/90243373949) | [2m21s](https://github.com/iree-org/iree/actions/runs/30349494988/job/90243373949) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 9s | [9s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993236) | [9s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993236) | [9s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993236) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 5s | [3s](https://github.com/iree-org/iree/actions/runs/30356608481/job/90266171555) | [8s](https://github.com/iree-org/iree/actions/runs/30356275247/job/90265108559) | [8s](https://github.com/iree-org/iree/actions/runs/30356275247/job/90265108559) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 5s | [3s](https://github.com/iree-org/iree/actions/runs/30356608481/job/90266171451) | [8s](https://github.com/iree-org/iree/actions/runs/30356275247/job/90265108665) | [8s](https://github.com/iree-org/iree/actions/runs/30356275247/job/90265108665) | 2 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993206) | [8s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993206) | [8s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993206) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/30356232018/job/90264967233) | [8s](https://github.com/iree-org/iree/actions/runs/30356232018/job/90264967233) | [8s](https://github.com/iree-org/iree/actions/runs/30356232018/job/90264967233) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90185273679) | [8s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90185273679) | [8s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90185273679) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 7s | [7s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90185273750) | [7s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90185273750) | [7s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90185273750) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/30356607715/job/90266181590) | [5s](https://github.com/iree-org/iree/actions/runs/30356607715/job/90266181590) | [5s](https://github.com/iree-org/iree/actions/runs/30356607715/job/90266181590) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30356275247/job/90265108753) | [3s](https://github.com/iree-org/iree/actions/runs/30356608481/job/90266171467) | [3s](https://github.com/iree-org/iree/actions/runs/30356608481/job/90266171467) | 2 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993391) | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993391) | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993391) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993235) | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993235) | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993235) | 1 |
| `.github/workflows/ci_macos_arm64_clang.yml` | macos_arm64_clang | `macos-14` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/30349471136/job/90243294763) | [3s](https://github.com/iree-org/iree/actions/runs/30349471136/job/90243294763) | [3s](https://github.com/iree-org/iree/actions/runs/30349471136/job/90243294763) | 1 |
| `.github/workflows/ci_macos_x64_clang.yml` | macos_x64_clang | `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/30349457314/job/90243249525) | [3s](https://github.com/iree-org/iree/actions/runs/30349457314/job/90243249525) | [3s](https://github.com/iree-org/iree/actions/runs/30349457314/job/90243249525) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/30356607715/job/90266227764) | [3s](https://github.com/iree-org/iree/actions/runs/30356607715/job/90266227764) | [3s](https://github.com/iree-org/iree/actions/runs/30356607715/job/90266227764) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90264647550) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90264647550) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90264647550) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993245) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993245) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993245) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993260) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993260) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993260) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993250) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993250) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993250) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993293) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993293) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993293) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993203) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993203) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993203) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993226) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993226) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993226) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993221) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993221) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993221) | 1 |
| `.github/workflows/ci_linux_x64_clang_byollvm.yml` | linux_x64_clang_byollvm | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30349495147/job/90243374666) | [2s](https://github.com/iree-org/iree/actions/runs/30349495147/job/90243374666) | [2s](https://github.com/iree-org/iree/actions/runs/30349495147/job/90243374666) | 1 |
| `.github/workflows/ci_linux_x64_clang_debug.yml` | linux_x64_clang_debug | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30349405394/job/90243081062) | [2s](https://github.com/iree-org/iree/actions/runs/30349405394/job/90243081062) | [2s](https://github.com/iree-org/iree/actions/runs/30349405394/job/90243081062) | 1 |
| `.github/workflows/ci_linux_x64_gcc.yml` | linux_x64_gcc | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30349504039/job/90243402861) | [2s](https://github.com/iree-org/iree/actions/runs/30349504039/job/90243402861) | [2s](https://github.com/iree-org/iree/actions/runs/30349504039/job/90243402861) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30333301869/job/90192849746) | [2s](https://github.com/iree-org/iree/actions/runs/30333301869/job/90192849746) | [2s](https://github.com/iree-org/iree/actions/runs/30333301869/job/90192849746) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30356137189/job/90264940770) | [2s](https://github.com/iree-org/iree/actions/runs/30356137189/job/90264940770) | [2s](https://github.com/iree-org/iree/actions/runs/30356137189/job/90264940770) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30356137189/job/90264671939) | [2s](https://github.com/iree-org/iree/actions/runs/30356137189/job/90264671939) | [2s](https://github.com/iree-org/iree/actions/runs/30356137189/job/90264671939) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/30356607715/job/90266227784) | [2s](https://github.com/iree-org/iree/actions/runs/30356607715/job/90266227784) | [2s](https://github.com/iree-org/iree/actions/runs/30356607715/job/90266227784) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192962381) | [1s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192962381) | [1s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192962381) | 1 |
| `.github/workflows/ci_linux_x64_clang_tsan.yml` | linux_x64_clang_tsan | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/30349485701/job/90243342515) | [1s](https://github.com/iree-org/iree/actions/runs/30349485701/job/90243342515) | [1s](https://github.com/iree-org/iree/actions/runs/30349485701/job/90243342515) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90186585501) | [1s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90186585501) | [1s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90186585501) | 1 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0s | 0s | 0 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 328 | 320 | 5 | 3 | 2% |  | 1d01h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 252 | 245 | 2 | 5 | 1% |  | 1d01h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 265 | 248 | 14 | 3 | 5% |  | 1d01h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 238 | 231 | 4 | 3 | 2% |  | 1d01h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 75 | 72 | 2 | 1 | 3% |  | 1d01h ago |

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
