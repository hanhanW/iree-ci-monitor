# iree-ci-monitor

_Updated: 2026-06-18 12:07 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m33s](https://github.com/iree-org/iree/actions/runs/27754181760/job/82111810223) | [1m33s](https://github.com/iree-org/iree/actions/runs/27754181760/job/82111810223) | 0% (0/1) | 1 |
| `ubuntu-24.04` | github-hosted | 7 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27758970156/job/82128040474) | [8s](https://github.com/iree-org/iree/actions/runs/27754180222/job/82111804348) | 33% (1/3) | 7 |
| `azure-linux-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27754113192/job/82111579338) | [8s](https://github.com/iree-org/iree/actions/runs/27754176204/job/82111789995) | 0% (0/2) | 2 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27769158122/job/82164093982) | [3s](https://github.com/iree-org/iree/actions/runs/27769158990/job/82164045759) | — | 15 |
| `macos-14` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27754158431/job/82111729975) | [3s](https://github.com/iree-org/iree/actions/runs/27754158431/job/82111729975) | 0% (0/1) | 1 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27754139760/job/82111668570) | [3s](https://github.com/iree-org/iree/actions/runs/27754139760/job/82111668570) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m33s](https://github.com/iree-org/iree/actions/runs/27754181760/job/82111810223) | [1m33s](https://github.com/iree-org/iree/actions/runs/27754181760/job/82111810223) | [1m33s](https://github.com/iree-org/iree/actions/runs/27754181760/job/82111810223) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27769158122/job/82164045551) | [9s](https://github.com/iree-org/iree/actions/runs/27759238620/job/82128981080) | [9s](https://github.com/iree-org/iree/actions/runs/27759238620/job/82128981080) | 2 |
| `.github/workflows/ci_linux_x64_clang_byollvm.yml` | linux_x64_clang_byollvm | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27754180222/job/82111804348) | [8s](https://github.com/iree-org/iree/actions/runs/27754180222/job/82111804348) | [8s](https://github.com/iree-org/iree/actions/runs/27754180222/job/82111804348) | 1 |
| `.github/workflows/ci_linux_x64_clang_tsan.yml` | linux_x64_clang_tsan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27754176204/job/82111789995) | [8s](https://github.com/iree-org/iree/actions/runs/27754176204/job/82111789995) | [8s](https://github.com/iree-org/iree/actions/runs/27754176204/job/82111789995) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27759238847/job/82128984744) | [3s](https://github.com/iree-org/iree/actions/runs/27769158990/job/82164045759) | [3s](https://github.com/iree-org/iree/actions/runs/27769158990/job/82164045759) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27769158990/job/82164045837) | [3s](https://github.com/iree-org/iree/actions/runs/27759238847/job/82128984753) | [3s](https://github.com/iree-org/iree/actions/runs/27759238847/job/82128984753) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27769158990/job/82164045981) | [3s](https://github.com/iree-org/iree/actions/runs/27759002193/job/82128157348) | [3s](https://github.com/iree-org/iree/actions/runs/27759002193/job/82128157348) | 3 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27758970156/job/82128040474) | [3s](https://github.com/iree-org/iree/actions/runs/27768668270/job/82162283281) | [3s](https://github.com/iree-org/iree/actions/runs/27768668270/job/82162283281) | 2 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27769158122/job/82164093982) | [3s](https://github.com/iree-org/iree/actions/runs/27759238620/job/82129032616) | [3s](https://github.com/iree-org/iree/actions/runs/27759238620/job/82129032616) | 2 |
| `.github/workflows/ci_linux_x64_gcc.yml` | linux_x64_gcc | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27754184937/job/82111820120) | [3s](https://github.com/iree-org/iree/actions/runs/27754184937/job/82111820120) | [3s](https://github.com/iree-org/iree/actions/runs/27754184937/job/82111820120) | 1 |
| `.github/workflows/ci_macos_arm64_clang.yml` | macos_arm64_clang | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27754158431/job/82111729975) | [3s](https://github.com/iree-org/iree/actions/runs/27754158431/job/82111729975) | [3s](https://github.com/iree-org/iree/actions/runs/27754158431/job/82111729975) | 1 |
| `.github/workflows/ci_macos_x64_clang.yml` | macos_x64_clang | `macos-15-intel` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27754139760/job/82111668570) | [3s](https://github.com/iree-org/iree/actions/runs/27754139760/job/82111668570) | [3s](https://github.com/iree-org/iree/actions/runs/27754139760/job/82111668570) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27759238620/job/82129032630) | [2s](https://github.com/iree-org/iree/actions/runs/27769158122/job/82164093874) | [2s](https://github.com/iree-org/iree/actions/runs/27769158122/job/82164093874) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82127783601) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82127783601) | [2s](https://github.com/iree-org/iree/actions/runs/27741539835/job/82127783601) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27758902755/job/82128017131) | [2s](https://github.com/iree-org/iree/actions/runs/27758902755/job/82128017131) | [2s](https://github.com/iree-org/iree/actions/runs/27758902755/job/82128017131) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27758902755/job/82127810888) | [2s](https://github.com/iree-org/iree/actions/runs/27758902755/job/82127810888) | [2s](https://github.com/iree-org/iree/actions/runs/27758902755/job/82127810888) | 1 |
| `.github/workflows/ci_linux_x64_clang_debug.yml` | linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27754113192/job/82111579338) | [1s](https://github.com/iree-org/iree/actions/runs/27754113192/job/82111579338) | [1s](https://github.com/iree-org/iree/actions/runs/27754113192/job/82111579338) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 171 | 5% (9/171) |  | 21h24m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 229 | 0% (0/229) |  | 21h29m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 175 | 1% (1/175) |  | 21h31m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 164 | 0% (0/164) |  | 21h33m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 52 | 0% (0/52) |  | 21h36m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
