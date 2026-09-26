# iree-ci-monitor

_Updated: 2026-09-26 04:30 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232986) | [9s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387233037) | — | 5 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007642) | [8s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232896) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007600) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232888) | — | 6 |
| `ubuntu-24.04` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36235802019/job/108387209437) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232833) | 0% (0/1) | 17 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232866) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232810) | — | 5 |
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
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007642) | [7s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007642) | [7s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007642) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232914) | [7s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232914) | [7s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232914) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232815) | [6s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232815) | [6s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232815) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007537) | [5s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007537) | [5s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007537) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232831) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232831) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232831) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232879) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232879) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232879) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232888) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232888) | [5s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232888) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007520) | [4s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007520) | [4s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007520) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007600) | [4s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007600) | [4s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007600) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007498) | [4s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007498) | [4s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007498) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007516) | [3s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007516) | [3s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007516) | 1 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232810) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232810) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232810) | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232833) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232833) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232833) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232935) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232935) | [3s](https://github.com/iree-org/iree/actions/runs/36235802180/job/108387232935) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007550) | [2s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007550) | [2s](https://github.com/iree-org/iree/actions/runs/36220232873/job/108344007550) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 307 | 2% (5/307) |  | 17h20m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 230 | 4% (10/230) |  | 17h35m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
