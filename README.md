# iree-ci-monitor

_Updated: 2026-07-16 01:35 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 1 | [5s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523468) | [6s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523482) | — | 3 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523458) | [3s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546496899) | 50% (2/4) | 9 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523461) | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523477) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523475) | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523478) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523482) | [6s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523482) | [6s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523482) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523468) | [5s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523468) | [5s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523468) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523459) | [5s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523459) | [5s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523459) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546496899) | [3s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546496899) | [3s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546496899) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523458) | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523458) | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523458) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523460) | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523460) | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523460) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523466) | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523466) | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523466) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523465) | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523465) | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523465) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523461) | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523461) | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523461) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523477) | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523477) | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523477) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523475) | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523475) | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523475) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523478) | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523478) | [2s](https://github.com/iree-org/iree/actions/runs/29475164630/job/87546523478) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29473105526/job/87540145408) | [2s](https://github.com/iree-org/iree/actions/runs/29473105526/job/87540145408) | [2s](https://github.com/iree-org/iree/actions/runs/29473105526/job/87540145408) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29473105526/job/87540145525) | [2s](https://github.com/iree-org/iree/actions/runs/29473105526/job/87540145525) | [2s](https://github.com/iree-org/iree/actions/runs/29473105526/job/87540145525) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29473105526/job/87541346281) | [2s](https://github.com/iree-org/iree/actions/runs/29473105526/job/87541346281) | [2s](https://github.com/iree-org/iree/actions/runs/29473105526/job/87541346281) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29475135385/job/87546403093) | [1s](https://github.com/iree-org/iree/actions/runs/29475135385/job/87546403093) | [1s](https://github.com/iree-org/iree/actions/runs/29475135385/job/87546403093) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 159 | 1% (2/159) |  | 12h54m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 134 | 1% (1/134) |  | 12h59m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 132 | 10% (13/132) |  | 13h02m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 116 | 1% (1/116) |  | 13h14m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 37 | 0% (0/37) |  | 13h19m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
