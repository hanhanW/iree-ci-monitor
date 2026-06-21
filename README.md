# iree-ci-monitor

_Updated: 2026-06-21 00:59 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962123) | [5s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962129) | — | 3 |
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962115) | [3s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962136) | 0% (0/1) | 6 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962140) | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962149) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962147) | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962152) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962122) | [5s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962122) | [5s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962122) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962129) | [5s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962129) | [5s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962129) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962123) | [5s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962123) | [5s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962123) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962136) | [3s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962136) | [3s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962136) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962118) | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962118) | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962118) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962115) | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962115) | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962115) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962151) | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962151) | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962151) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962147) | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962147) | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962147) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962152) | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962152) | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962152) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547952770) | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547952770) | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547952770) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962149) | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962149) | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962149) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962140) | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962140) | [2s](https://github.com/iree-org/iree/actions/runs/27896159981/job/82547962140) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27896148390/job/82547915981) | [1s](https://github.com/iree-org/iree/actions/runs/27896148390/job/82547915981) | [1s](https://github.com/iree-org/iree/actions/runs/27896148390/job/82547915981) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 156 | 0% (0/156) |  | 1d17h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 118 | 5% (6/118) |  | 1d17h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 128 | 0% (0/128) |  | 1d17h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 112 | 0% (0/112) |  | 1d17h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 35 | 0% (0/35) |  | 1d17h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
