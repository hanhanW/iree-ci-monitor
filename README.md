# iree-ci-monitor

_Updated: 2026-11-27 23:56 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796338) | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796368) | — | 3 |
| `ubuntu-24.04` | github-hosted | 7 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796304) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796359) | 0% (0/1) | 7 |
| `macos-15` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796321) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796410) | — | 2 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796306) | [1s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796357) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796368) | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796368) | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796368) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796317) | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796317) | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796317) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796338) | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796338) | [4s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796338) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796304) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796304) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796304) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796342) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796342) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796342) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796359) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796359) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796359) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796358) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796358) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796358) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796410) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796410) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796410) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796321) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796321) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796321) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873749544) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873749544) | [2s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873749544) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/46110781293/job/140873607434) | [2s](https://github.com/iree-org/iree/actions/runs/46110781293/job/140873607434) | [2s](https://github.com/iree-org/iree/actions/runs/46110781293/job/140873607434) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796306) | [1s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796306) | [1s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796306) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796357) | [1s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796357) | [1s](https://github.com/iree-org/iree/actions/runs/46110824722/job/140873796357) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/46091227293/job/140812338235) | [1s](https://github.com/iree-org/iree/actions/runs/46091227293/job/140812338235) | [1s](https://github.com/iree-org/iree/actions/runs/46091227293/job/140812338235) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 91 | 1% (1/91) |  | 11h33m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 76 | 8% (6/76) |  | 15h20m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
