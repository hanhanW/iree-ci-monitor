# iree-ci-monitor

_Updated: 2026-11-10 22:34 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781055) | [5s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781096) | — | 3 |
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336780977) | [4s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781035) | — | 2 |
| `ubuntu-24.04` | github-hosted | 10 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/42963861847/job/130336433350) | [3s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781036) | 0% (0/4) | 10 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781046) | [2s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781191) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781096) | [5s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781096) | [5s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781096) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781055) | [5s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781055) | [5s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781055) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781037) | [5s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781037) | [5s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781037) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781035) | [4s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781035) | [4s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781035) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336780990) | [3s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336780990) | [3s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336780990) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781036) | [3s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781036) | [3s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781036) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336780976) | [3s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336780976) | [3s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336780976) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336780977) | [3s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336780977) | [3s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336780977) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781727) | [2s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781727) | [2s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781727) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336703319) | [2s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336703319) | [2s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336703319) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781046) | [2s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781046) | [2s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781046) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781191) | [2s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781191) | [2s](https://github.com/iree-org/iree/actions/runs/42963945522/job/130336781191) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42828169383/job/130268411673) | [2s](https://github.com/iree-org/iree/actions/runs/42828169383/job/130268411673) | [2s](https://github.com/iree-org/iree/actions/runs/42828169383/job/130268411673) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42957972056/job/130317505838) | [2s](https://github.com/iree-org/iree/actions/runs/42957972056/job/130317505838) | [2s](https://github.com/iree-org/iree/actions/runs/42957972056/job/130317505838) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42957972056/job/130317505604) | [2s](https://github.com/iree-org/iree/actions/runs/42957972056/job/130317505604) | [2s](https://github.com/iree-org/iree/actions/runs/42957972056/job/130317505604) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42957972056/job/130321098305) | [2s](https://github.com/iree-org/iree/actions/runs/42957972056/job/130321098305) | [2s](https://github.com/iree-org/iree/actions/runs/42957972056/job/130321098305) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42963861847/job/130336433350) | [2s](https://github.com/iree-org/iree/actions/runs/42963861847/job/130336433350) | [2s](https://github.com/iree-org/iree/actions/runs/42963861847/job/130336433350) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 329 | 1% (2/329) |  | 12h02m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 253 | 1% (2/253) |  | 12h29m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
