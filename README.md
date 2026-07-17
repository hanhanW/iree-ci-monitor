# iree-ci-monitor

_Updated: 2026-07-17 00:04 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987530) | [6s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987534) | — | 3 |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/29556591503/job/87809855923) | [3s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987526) | 40% (2/5) | 10 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987535) | [2s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987511) | — | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987518) | [1s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987523) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987534) | [6s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987534) | [6s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987534) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987530) | [5s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987530) | [5s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987530) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987506) | [5s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987506) | [5s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987506) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987526) | [3s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987526) | [3s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987526) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815956167) | [3s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815956167) | [3s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815956167) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987501) | [2s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987501) | [2s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987501) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987511) | [2s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987511) | [2s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987511) | 1 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29556076445/job/87808283687) | [2s](https://github.com/iree-org/iree/actions/runs/29556076445/job/87808283687) | [2s](https://github.com/iree-org/iree/actions/runs/29556076445/job/87808283687) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29556591503/job/87809855923) | [2s](https://github.com/iree-org/iree/actions/runs/29556591503/job/87809855923) | [2s](https://github.com/iree-org/iree/actions/runs/29556591503/job/87809855923) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29556591503/job/87811155791) | [2s](https://github.com/iree-org/iree/actions/runs/29556591503/job/87811155791) | [2s](https://github.com/iree-org/iree/actions/runs/29556591503/job/87811155791) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29558545756/job/87815865666) | [2s](https://github.com/iree-org/iree/actions/runs/29558545756/job/87815865666) | [2s](https://github.com/iree-org/iree/actions/runs/29558545756/job/87815865666) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987514) | [1s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987514) | [1s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987514) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987529) | [1s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987529) | [1s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987529) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987518) | [1s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987518) | [1s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987518) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987523) | [1s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987523) | [1s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987523) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987535) | [1s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987535) | [1s](https://github.com/iree-org/iree/actions/runs/29558575819/job/87815987535) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29556591503/job/87809855928) | [1s](https://github.com/iree-org/iree/actions/runs/29556591503/job/87809855928) | [1s](https://github.com/iree-org/iree/actions/runs/29556591503/job/87809855928) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 143 | 1% (1/143) |  | 11h34m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 112 | 11% (12/112) |  | 11h37m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 126 | 1% (1/126) |  | 11h39m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 113 | 0% (0/113) |  | 11h44m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 33 | 0% (0/33) |  | 11h54m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
