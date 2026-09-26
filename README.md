# iree-ci-monitor

_Updated: 2026-09-26 09:27 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232986) | [9s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233037) | — | 5 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232914) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232896) | — | 3 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232879) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232888) | — | 3 |
| `ubuntu-24.04` | github-hosted | 13 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232922) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232833) | 0% (0/1) | 12 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232894) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232810) | — | 3 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36247552125/job/108419476940) | [2s](https://github.com/iree-org/iree/actions/runs/36247552292/job/108419445581) | — | 6 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233013) | [1s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233013) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233037) | [9s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233037) | [9s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233037) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232921) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232921) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232921) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233093) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233093) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233093) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232986) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232986) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232986) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232896) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232896) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232896) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232914) | [7s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232914) | [7s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232914) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232815) | [6s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232815) | [6s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232815) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232831) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232831) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232831) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232879) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232879) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232879) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232888) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232888) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232888) | 1 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232810) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232810) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232810) | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232833) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232833) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232833) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232935) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232935) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232935) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108392703866) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108392703866) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108392703866) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232922) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232922) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232922) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232869) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232869) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232869) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232866) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232866) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232866) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232894) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232894) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232894) | 1 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232761) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232761) | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232761) | 1 |
| `.github/workflows/clang_tidy.yml` | clang-tidy | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36235802019/job/108387209437) | [2s](https://github.com/iree-org/iree/actions/runs/36235802019/job/108387209437) | [2s](https://github.com/iree-org/iree/actions/runs/36235802019/job/108387209437) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 307 | 2% (5/307) |  | 22h17m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 230 | 4% (10/230) |  | 22h33m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
