# iree-ci-monitor

_Updated: 2026-08-07 00:43 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 13 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557272) | [9s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557257) | 33% (2/6) | 11 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557276) | [6s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557307) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557332) | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557251) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557282) | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557271) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557257) | [9s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557257) | [9s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557257) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/31148291642/job/92772381430) | [8s](https://github.com/iree-org/iree/actions/runs/31148291642/job/92772381430) | [8s](https://github.com/iree-org/iree/actions/runs/31148291642/job/92772381430) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/31150989671/job/92780392069) | [8s](https://github.com/iree-org/iree/actions/runs/31150989671/job/92780392069) | [8s](https://github.com/iree-org/iree/actions/runs/31150989671/job/92780392069) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557307) | [6s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557307) | [6s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557307) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557276) | [5s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557276) | [5s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557276) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557264) | [4s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557264) | [4s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557264) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557285) | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557285) | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557285) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557271) | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557271) | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557271) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557251) | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557251) | [3s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557251) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557279) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557279) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557279) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557272) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557272) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557272) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557282) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557282) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557282) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780523930) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780523930) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780523930) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557332) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557332) | [2s](https://github.com/iree-org/iree/actions/runs/31151032922/job/92780557332) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31128374710/job/92709659505) | [2s](https://github.com/iree-org/iree/actions/runs/31128374710/job/92709659505) | [2s](https://github.com/iree-org/iree/actions/runs/31128374710/job/92709659505) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92711543671) | [2s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92711543671) | [2s](https://github.com/iree-org/iree/actions/runs/31128374741/job/92711543671) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31148291642/job/92772381345) | [2s](https://github.com/iree-org/iree/actions/runs/31148291642/job/92772381345) | [2s](https://github.com/iree-org/iree/actions/runs/31148291642/job/92772381345) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31148291642/job/92773904174) | [2s](https://github.com/iree-org/iree/actions/runs/31148291642/job/92773904174) | [2s](https://github.com/iree-org/iree/actions/runs/31148291642/job/92773904174) | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 1 | 0 | — | — | 0s | 0s | 0s | 0 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 1 | 0 | — | — | 0s | 0s | 0s | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 129 | 0% (0/129) |  | 9h38m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 112 | 3% (3/112) |  | 9h40m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 101 | 0% (0/101) |  | 9h43m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 102 | 1% (1/102) |  | 9h44m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 13 | 0% (0/13) |  | 3d18h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
