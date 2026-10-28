# iree-ci-monitor

_Updated: 2026-10-27 22:49 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790296) | [5s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790229) | — | 3 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644730190) | [3s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790306) | 0% (0/4) | 9 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790225) | [3s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790247) | — | 2 |
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790353) | [3s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790449) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790229) | [5s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790229) | [5s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790229) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790231) | [4s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790231) | [4s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790231) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790296) | [4s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790296) | [4s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790296) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790306) | [3s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790306) | [3s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790306) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790284) | [3s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790284) | [3s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790284) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790449) | [3s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790449) | [3s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790449) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790353) | [3s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790353) | [3s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790353) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790247) | [3s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790247) | [3s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790247) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790203) | [2s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790203) | [2s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790203) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790213) | [2s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790213) | [2s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790213) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644730190) | [2s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644730190) | [2s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644730190) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790225) | [2s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790225) | [2s](https://github.com/iree-org/iree/actions/runs/40636547653/job/122644790225) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40631443233/job/122628509328) | [2s](https://github.com/iree-org/iree/actions/runs/40631443233/job/122628509328) | [2s](https://github.com/iree-org/iree/actions/runs/40631443233/job/122628509328) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40631443233/job/122631811273) | [2s](https://github.com/iree-org/iree/actions/runs/40631443233/job/122631811273) | [2s](https://github.com/iree-org/iree/actions/runs/40631443233/job/122631811273) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/40636496370/job/122644558961) | [2s](https://github.com/iree-org/iree/actions/runs/40636496370/job/122644558961) | [2s](https://github.com/iree-org/iree/actions/runs/40636496370/job/122644558961) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/40631443233/job/122628508996) | [1s](https://github.com/iree-org/iree/actions/runs/40631443233/job/122628508996) | [1s](https://github.com/iree-org/iree/actions/runs/40631443233/job/122628508996) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 205 | 3% (7/205) |  | 10h58m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 247 | 1% (3/247) |  | 11h01m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
