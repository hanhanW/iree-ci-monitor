# iree-ci-monitor

_Updated: 2026-10-08 23:15 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [7s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117147) | [8s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117183) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117194) | [4s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117197) | — | 3 |
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682067414) | [3s](https://github.com/iree-org/iree/actions/runs/37825138381/job/113525381053) | 0% (0/4) | 11 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117143) | [3s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117144) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117183) | [8s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117183) | [8s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117183) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117147) | [7s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117147) | [7s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117147) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117197) | [4s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117197) | [4s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117197) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117173) | [4s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117173) | [4s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117173) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117194) | [4s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117194) | [4s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117194) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117144) | [3s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117144) | [3s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117144) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37825138381/job/113525381053) | [3s](https://github.com/iree-org/iree/actions/runs/37825138381/job/113525381053) | [3s](https://github.com/iree-org/iree/actions/runs/37825138381/job/113525381053) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117177) | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117177) | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117177) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117090) | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117090) | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117090) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117088) | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117088) | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117088) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117262) | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117262) | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117262) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682067414) | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682067414) | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682067414) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117143) | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117143) | [2s](https://github.com/iree-org/iree/actions/runs/37887945260/job/113682117143) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113524914403) | [2s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113524914403) | [2s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113524914403) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37883955891/job/113669667829) | [2s](https://github.com/iree-org/iree/actions/runs/37883955891/job/113669667829) | [2s](https://github.com/iree-org/iree/actions/runs/37883955891/job/113669667829) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37883955891/job/113669667593) | [2s](https://github.com/iree-org/iree/actions/runs/37883955891/job/113669667593) | [2s](https://github.com/iree-org/iree/actions/runs/37883955891/job/113669667593) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37883955891/job/113671753546) | [2s](https://github.com/iree-org/iree/actions/runs/37883955891/job/113671753546) | [2s](https://github.com/iree-org/iree/actions/runs/37883955891/job/113671753546) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37887886688/job/113681879595) | [2s](https://github.com/iree-org/iree/actions/runs/37887886688/job/113681879595) | [2s](https://github.com/iree-org/iree/actions/runs/37887886688/job/113681879595) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 334 | 0% (1/334) |  | 9h46m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 171 | 15% (26/171) |  | 9h51m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
