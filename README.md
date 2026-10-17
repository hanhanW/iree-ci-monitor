# iree-ci-monitor

_Updated: 2026-10-17 03:50 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `macos-15` | github-hosted | 2 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058803) | [7s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058786) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058721) | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058800) | — | 3 |
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058812) | [2s](https://github.com/iree-org/iree/actions/runs/39026329531/job/117377925622) | 0% (0/2) | 11 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058822) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058861) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058786) | [7s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058786) | [7s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058786) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058803) | [6s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058803) | [6s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058803) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058800) | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058800) | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058800) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058721) | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058721) | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058721) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058710) | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058710) | [4s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058710) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117377688428) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117377688428) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117377688428) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058812) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058812) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058812) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058756) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058756) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058756) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058769) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058769) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058769) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058778) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058778) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058778) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058861) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058861) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058861) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058822) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058822) | [2s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317058822) | 1 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39018618086/job/117355734086) | [2s](https://github.com/iree-org/iree/actions/runs/39018618086/job/117355734086) | [2s](https://github.com/iree-org/iree/actions/runs/39018618086/job/117355734086) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39026329531/job/117377925622) | [2s](https://github.com/iree-org/iree/actions/runs/39026329531/job/117377925622) | [2s](https://github.com/iree-org/iree/actions/runs/39026329531/job/117377925622) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39026251833/job/117377904575) | [2s](https://github.com/iree-org/iree/actions/runs/39026251833/job/117377904575) | [2s](https://github.com/iree-org/iree/actions/runs/39026251833/job/117377904575) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39026251833/job/117377705328) | [2s](https://github.com/iree-org/iree/actions/runs/39026251833/job/117377705328) | [2s](https://github.com/iree-org/iree/actions/runs/39026251833/job/117377705328) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317025406) | [1s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317025406) | [1s](https://github.com/iree-org/iree/actions/runs/39005501044/job/117317025406) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/39005471531/job/117316931820) | [1s](https://github.com/iree-org/iree/actions/runs/39005471531/job/117316931820) | [1s](https://github.com/iree-org/iree/actions/runs/39005471531/job/117316931820) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 261 | 4% (11/261) |  | 18h28m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 212 | 1% (2/212) |  | 18h35m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
