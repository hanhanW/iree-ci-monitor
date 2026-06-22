# iree-ci-monitor

_Updated: 2026-06-22 01:30 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418390) | [5s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418438) | — | 3 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418381) | [4s](https://github.com/iree-org/iree/actions/runs/27934900073/job/82654300278) | 50% (2/4) | 9 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418379) | [3s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418405) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418428) | [3s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418401) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418390) | [5s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418390) | [5s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418390) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418438) | [5s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418438) | [5s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418438) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418370) | [5s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418370) | [5s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418370) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/27934900073/job/82654300278) | [4s](https://github.com/iree-org/iree/actions/runs/27934900073/job/82654300278) | [4s](https://github.com/iree-org/iree/actions/runs/27934900073/job/82654300278) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418448) | [3s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418448) | [3s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418448) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418401) | [3s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418401) | [3s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418401) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418405) | [3s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418405) | [3s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418405) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418413) | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418413) | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418413) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418381) | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418381) | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418381) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418394) | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418394) | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418394) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418428) | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418428) | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418428) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654396564) | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654396564) | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654396564) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418379) | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418379) | [2s](https://github.com/iree-org/iree/actions/runs/27934929794/job/82654418379) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27932838637/job/82648107620) | [2s](https://github.com/iree-org/iree/actions/runs/27932838637/job/82648107620) | [2s](https://github.com/iree-org/iree/actions/runs/27932838637/job/82648107620) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27932838637/job/82648107570) | [2s](https://github.com/iree-org/iree/actions/runs/27932838637/job/82648107570) | [2s](https://github.com/iree-org/iree/actions/runs/27932838637/job/82648107570) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27932838637/job/82649265465) | [2s](https://github.com/iree-org/iree/actions/runs/27932838637/job/82649265465) | [2s](https://github.com/iree-org/iree/actions/runs/27932838637/job/82649265465) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 156 | 0% (0/156) |  | 2d17h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 118 | 5% (6/118) |  | 2d17h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 128 | 0% (0/128) |  | 2d17h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 112 | 0% (0/112) |  | 2d17h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 35 | 0% (0/35) |  | 2d17h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
