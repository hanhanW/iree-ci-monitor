# iree-ci-monitor

_Updated: 2026-09-29 22:38 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [6s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040605) | [7s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040653) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040621) | [5s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040639) | — | 3 |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/36668818730/job/109741498005) | [3s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040705) | 0% (0/4) | 10 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040534) | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040634) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040653) | [7s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040653) | [7s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040653) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040605) | [6s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040605) | [6s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040605) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040639) | [5s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040639) | [5s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040639) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040597) | [4s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040597) | [4s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040597) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040621) | [4s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040621) | [4s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040621) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040705) | [3s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040705) | [3s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040705) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040645) | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040645) | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040645) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040627) | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040627) | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040627) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040571) | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040571) | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040571) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109750990579) | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109750990579) | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109750990579) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040534) | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040534) | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040534) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040634) | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040634) | [2s](https://github.com/iree-org/iree/actions/runs/36672716153/job/109751040634) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36628403833/job/109611160741) | [2s](https://github.com/iree-org/iree/actions/runs/36628403833/job/109611160741) | [2s](https://github.com/iree-org/iree/actions/runs/36628403833/job/109611160741) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36668818730/job/109739205529) | [2s](https://github.com/iree-org/iree/actions/runs/36668818730/job/109739205529) | [2s](https://github.com/iree-org/iree/actions/runs/36668818730/job/109739205529) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36668818730/job/109739205704) | [2s](https://github.com/iree-org/iree/actions/runs/36668818730/job/109739205704) | [2s](https://github.com/iree-org/iree/actions/runs/36668818730/job/109739205704) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36668818730/job/109741498005) | [2s](https://github.com/iree-org/iree/actions/runs/36668818730/job/109741498005) | [2s](https://github.com/iree-org/iree/actions/runs/36668818730/job/109741498005) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/36672667118/job/109750838654) | [1s](https://github.com/iree-org/iree/actions/runs/36672667118/job/109750838654) | [1s](https://github.com/iree-org/iree/actions/runs/36672667118/job/109750838654) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 348 | 1% (4/348) |  | 11h27m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 268 | 4% (12/268) |  | 11h35m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
