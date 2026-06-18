# Status detail

_Updated: 2026-06-18 06:30 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | — | 1m33s | [1m33s](https://github.com/iree-org/iree/actions/runs/27754181760/job/82111810223) | [1m33s](https://github.com/iree-org/iree/actions/runs/27754181760/job/82111810223) | [1m33s](https://github.com/iree-org/iree/actions/runs/27754181760/job/82111810223) | 0% (0/1) | 0% (0/1) | 1 |  |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | — | 3s | [2s](https://github.com/iree-org/iree/actions/runs/27759238847/job/82128984744) | [9s](https://github.com/iree-org/iree/actions/runs/27759238620/job/82128981080) | [9s](https://github.com/iree-org/iree/actions/runs/27759238620/job/82128981080) | 22% (2/9) | — | 9 |  |
| `azure-linux-scale` | ossci | 2 | 0 | — | — | 0 | — | 4s | [1s](https://github.com/iree-org/iree/actions/runs/27754113192/job/82111579338) | [8s](https://github.com/iree-org/iree/actions/runs/27754176204/job/82111789995) | [8s](https://github.com/iree-org/iree/actions/runs/27754176204/job/82111789995) | 0% (0/2) | 0% (0/2) | 2 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | — | 5s | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698588) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698596) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698596) | 0% (0/3) | — | 3 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | — | 3s | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698574) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698657) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698657) | 0% (0/2) | — | 2 |  |
| `ubuntu-24.04` | github-hosted | 15 | 0 | — | — | 2 | [2h43m](https://github.com/iree-org/iree/actions/runs/27754180222/job/82111804348) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27758902755/job/82127810888) | [3s](https://github.com/iree-org/iree/actions/runs/27754184937/job/82111820120) | [8s](https://github.com/iree-org/iree/actions/runs/27754180222/job/82111804348) | 15% (2/13) | 50% (2/4) | 15 |  |
| `macos-14` | github-hosted | 3 | 0 | — | — | 1 | [2h44m](https://github.com/iree-org/iree/actions/runs/27754158431/job/82111729975) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698686) | [3s](https://github.com/iree-org/iree/actions/runs/27754158431/job/82111729975) | [3s](https://github.com/iree-org/iree/actions/runs/27754158431/job/82111729975) | 0% (0/2) | — | 3 |  |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [2h44m](https://github.com/iree-org/iree/actions/runs/27754139760/job/82111668570) | 3s | [3s](https://github.com/iree-org/iree/actions/runs/27754139760/job/82111668570) | [3s](https://github.com/iree-org/iree/actions/runs/27754139760/job/82111668570) | [3s](https://github.com/iree-org/iree/actions/runs/27754139760/job/82111668570) | — | — | 1 |  |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | 1m33s | [1m33s](https://github.com/iree-org/iree/actions/runs/27754181760/job/82111810223) | [1m33s](https://github.com/iree-org/iree/actions/runs/27754181760/job/82111810223) | [1m33s](https://github.com/iree-org/iree/actions/runs/27754181760/job/82111810223) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 9s | [9s](https://github.com/iree-org/iree/actions/runs/27759238620/job/82128981080) | [9s](https://github.com/iree-org/iree/actions/runs/27759238620/job/82128981080) | [9s](https://github.com/iree-org/iree/actions/runs/27759238620/job/82128981080) | 1 |
| `.github/workflows/ci_linux_x64_clang_byollvm.yml` | linux_x64_clang_byollvm | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/27754180222/job/82111804348) | [8s](https://github.com/iree-org/iree/actions/runs/27754180222/job/82111804348) | [8s](https://github.com/iree-org/iree/actions/runs/27754180222/job/82111804348) | 1 |
| `.github/workflows/ci_linux_x64_clang_tsan.yml` | linux_x64_clang_tsan | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 8s | [8s](https://github.com/iree-org/iree/actions/runs/27754176204/job/82111789995) | [8s](https://github.com/iree-org/iree/actions/runs/27754176204/job/82111789995) | [8s](https://github.com/iree-org/iree/actions/runs/27754176204/job/82111789995) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698588) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698588) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698588) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698596) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698596) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698596) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698566) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698566) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698566) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698657) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698657) | [5s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698657) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27759002193/job/82128157373) | [3s](https://github.com/iree-org/iree/actions/runs/27759238847/job/82128984753) | [3s](https://github.com/iree-org/iree/actions/runs/27759238847/job/82128984753) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27759238847/job/82128984737) | [3s](https://github.com/iree-org/iree/actions/runs/27759002193/job/82128157348) | [3s](https://github.com/iree-org/iree/actions/runs/27759002193/job/82128157348) | 2 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698620) | [3s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698620) | [3s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698620) | 1 |
| `.github/workflows/ci_linux_x64_gcc.yml` | linux_x64_gcc | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/27754184937/job/82111820120) | [3s](https://github.com/iree-org/iree/actions/runs/27754184937/job/82111820120) | [3s](https://github.com/iree-org/iree/actions/runs/27754184937/job/82111820120) | 1 |
| `.github/workflows/ci_macos_arm64_clang.yml` | macos_arm64_clang | `macos-14` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/27754158431/job/82111729975) | [3s](https://github.com/iree-org/iree/actions/runs/27754158431/job/82111729975) | [3s](https://github.com/iree-org/iree/actions/runs/27754158431/job/82111729975) | 1 |
| `.github/workflows/ci_macos_x64_clang.yml` | macos_x64_clang | `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/27754139760/job/82111668570) | [3s](https://github.com/iree-org/iree/actions/runs/27754139760/job/82111668570) | [3s](https://github.com/iree-org/iree/actions/runs/27754139760/job/82111668570) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/27739499492/job/82063361011) | [3s](https://github.com/iree-org/iree/actions/runs/27739499492/job/82063361011) | [3s](https://github.com/iree-org/iree/actions/runs/27739499492/job/82063361011) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/27739499492/job/82064477870) | [3s](https://github.com/iree-org/iree/actions/runs/27739499492/job/82064477870) | [3s](https://github.com/iree-org/iree/actions/runs/27739499492/job/82064477870) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/27759238620/job/82129032616) | [3s](https://github.com/iree-org/iree/actions/runs/27759238620/job/82129032616) | [3s](https://github.com/iree-org/iree/actions/runs/27759238620/job/82129032616) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27759002193/job/82128157479) | [2s](https://github.com/iree-org/iree/actions/runs/27759238847/job/82128984744) | [2s](https://github.com/iree-org/iree/actions/runs/27759238847/job/82128984744) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82127783601) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82127783601) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82127783601) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698572) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698572) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698572) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698592) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698592) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698592) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698603) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698603) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698603) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698686) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698686) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698686) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069675368) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069675368) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069675368) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698574) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698574) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698574) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27758970156/job/82128040474) | [2s](https://github.com/iree-org/iree/actions/runs/27758970156/job/82128040474) | [2s](https://github.com/iree-org/iree/actions/runs/27758970156/job/82128040474) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27741514631/job/82069586801) | [2s](https://github.com/iree-org/iree/actions/runs/27741514631/job/82069586801) | [2s](https://github.com/iree-org/iree/actions/runs/27741514631/job/82069586801) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27758902755/job/82128017131) | [2s](https://github.com/iree-org/iree/actions/runs/27758902755/job/82128017131) | [2s](https://github.com/iree-org/iree/actions/runs/27758902755/job/82128017131) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27758902755/job/82127810888) | [2s](https://github.com/iree-org/iree/actions/runs/27758902755/job/82127810888) | [2s](https://github.com/iree-org/iree/actions/runs/27758902755/job/82127810888) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/27759238620/job/82129032630) | [2s](https://github.com/iree-org/iree/actions/runs/27759238620/job/82129032630) | [2s](https://github.com/iree-org/iree/actions/runs/27759238620/job/82129032630) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698580) | [1s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698580) | [1s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82069698580) | 1 |
| `.github/workflows/ci_linux_x64_clang_debug.yml` | linux_x64_clang_debug | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/27754113192/job/82111579338) | [1s](https://github.com/iree-org/iree/actions/runs/27754113192/job/82111579338) | [1s](https://github.com/iree-org/iree/actions/runs/27754113192/job/82111579338) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/27739499492/job/82063361021) | [1s](https://github.com/iree-org/iree/actions/runs/27739499492/job/82063361021) | [1s](https://github.com/iree-org/iree/actions/runs/27739499492/job/82063361021) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 171 | 160 | 9 | 2 | 5% |  | 15h47m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 229 | 227 | 0 | 2 | 0% |  | 15h51m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 175 | 172 | 1 | 2 | 1% |  | 15h54m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 164 | 163 | 0 | 1 | 0% |  | 15h55m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 52 | 50 | 0 | 2 | 0% |  | 15h58m ago |

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
