# iree-ci-monitor

_Updated: 2026-11-03 22:33 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524950) | [15s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524859) | — | 3 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [1s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401525032) | [12s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401525009) | 0% (0/4) | 9 |
| `macos-15` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524927) | [3s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401525098) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524936) | [1s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524942) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [15s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524859) | [15s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524859) | [15s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524859) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401525009) | [12s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401525009) | [12s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401525009) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524908) | [4s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524908) | [4s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524908) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524950) | [4s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524950) | [4s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524950) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401525098) | [3s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401525098) | [3s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401525098) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/41771967185/job/126383505349) | [3s](https://github.com/iree-org/iree/actions/runs/41771967185/job/126383505349) | [3s](https://github.com/iree-org/iree/actions/runs/41771967185/job/126383505349) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401525102) | [2s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401525102) | [2s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401525102) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524927) | [2s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524927) | [2s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524927) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41771967185/job/126386801848) | [2s](https://github.com/iree-org/iree/actions/runs/41771967185/job/126386801848) | [2s](https://github.com/iree-org/iree/actions/runs/41771967185/job/126386801848) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524980) | [1s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524980) | [1s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524980) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401525032) | [1s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401525032) | [1s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401525032) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401455477) | [1s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401455477) | [1s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401455477) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524936) | [1s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524936) | [1s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524936) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524942) | [1s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524942) | [1s](https://github.com/iree-org/iree/actions/runs/41777592370/job/126401524942) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/41771967185/job/126383505716) | [1s](https://github.com/iree-org/iree/actions/runs/41771967185/job/126383505716) | [1s](https://github.com/iree-org/iree/actions/runs/41771967185/job/126383505716) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/41777509998/job/126401198063) | [1s](https://github.com/iree-org/iree/actions/runs/41777509998/job/126401198063) | [1s](https://github.com/iree-org/iree/actions/runs/41777509998/job/126401198063) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 482 | 2% (9/482) |  | 10h52m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 399 | 1% (5/399) |  | 11h48m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
