# iree-ci-monitor

_Updated: 2026-06-19 18:23 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m36s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216877) | [1m36s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216877) | — | 1 |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216913) | [9s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216889) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216805) | [5s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216819) | — | 3 |
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388185714) | [3s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216776) | — | 11 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216803) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216809) | — | 3 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216773) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216791) | — | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216923) | [1s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216923) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | linux_arm64_clang / linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m36s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216877) | [1m36s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216877) | [1m36s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216877) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216889) | [9s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216889) | [9s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216889) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216913) | [8s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216913) | [8s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216913) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27833332075/job/82388210406) | [8s](https://github.com/iree-org/iree/actions/runs/27833332075/job/82388210406) | [8s](https://github.com/iree-org/iree/actions/runs/27833332075/job/82388210406) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216838) | [7s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216838) | [7s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216838) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216841) | [7s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216841) | [7s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216841) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216679) | [5s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216679) | [5s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216679) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216805) | [5s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216805) | [5s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216805) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216819) | [5s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216819) | [5s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216819) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216776) | [3s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216776) | [3s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216776) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82395465400) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82395465400) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82395465400) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216670) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216670) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216670) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216671) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216671) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216671) | 1 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216673) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216673) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216673) | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216637) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216637) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216637) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216803) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216803) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216803) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216809) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216809) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216809) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216791) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216791) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216791) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216773) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216773) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388216773) | 1 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388185714) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388185714) | [2s](https://github.com/iree-org/iree/actions/runs/27833331915/job/82388185714) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 156 | 0% (0/156) |  | 10h38m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 118 | 5% (6/118) |  | 10h39m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 128 | 0% (0/128) |  | 10h39m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 112 | 0% (0/112) |  | 10h42m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 35 | 0% (0/35) |  | 10h51m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
