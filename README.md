# iree-ci-monitor

_Updated: 2026-11-21 22:57 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304519) | [4s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304540) | — | 3 |
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304533) | [3s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304553) | — | 2 |
| `ubuntu-24.04` | github-hosted | 7 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304510) | [2s](https://github.com/iree-org/iree/actions/runs/44990780936/job/137111153448) | 0% (0/1) | 7 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304506) | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304543) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304540) | [4s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304540) | [4s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304540) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304519) | [4s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304519) | [4s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304519) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304508) | [4s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304508) | [4s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304508) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304553) | [3s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304553) | [3s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304553) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304513) | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304513) | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304513) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304510) | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304510) | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304510) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304551) | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304551) | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304551) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304489) | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304489) | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304489) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304533) | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304533) | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304533) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103230992) | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103230992) | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103230992) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304506) | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304506) | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304506) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304543) | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304543) | [2s](https://github.com/iree-org/iree/actions/runs/44988172438/job/137103304543) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44990780936/job/137111153448) | [2s](https://github.com/iree-org/iree/actions/runs/44990780936/job/137111153448) | [2s](https://github.com/iree-org/iree/actions/runs/44990780936/job/137111153448) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44988127940/job/137103091275) | [2s](https://github.com/iree-org/iree/actions/runs/44988127940/job/137103091275) | [2s](https://github.com/iree-org/iree/actions/runs/44988127940/job/137103091275) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 151 | 3% (5/151) |  | 1d10h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 114 | 3% (3/114) |  | 1d11h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
