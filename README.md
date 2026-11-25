# iree-ci-monitor

_Updated: 2026-11-25 00:43 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 6 | [7s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193500) | [9s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193549) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193227) | [6s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542244) | — | 6 |
| `macos-15` | github-hosted | 5 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193226) | [4s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193501) | — | 5 |
| `ubuntu-24.04` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/45545543388/job/138976819770) | [3s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542240) | 0% (0/4) | 18 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542255) | [3s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193190) | — | 5 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193506) | [1s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193506) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193494) | [9s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193494) | [9s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193494) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193549) | [9s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193549) | [9s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193549) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193694) | [8s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193694) | [8s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193694) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193500) | [7s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193500) | [7s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193500) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542244) | [6s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542244) | [6s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542244) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193543) | [6s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193543) | [6s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193543) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193352) | [5s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193352) | [5s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193352) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193227) | [5s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193227) | [5s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193227) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193389) | [5s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193389) | [5s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193389) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542329) | [4s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542329) | [4s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542329) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542256) | [4s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542256) | [4s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542256) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193226) | [4s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193226) | [4s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193226) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193501) | [4s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193501) | [4s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193501) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193497) | [4s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193497) | [4s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193497) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542267) | [3s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542267) | [3s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542267) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542240) | [3s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542240) | [3s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542240) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542299) | [3s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542299) | [3s](https://github.com/iree-org/iree/actions/runs/45551789268/job/138994542299) | 1 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193190) | [3s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193190) | [3s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193190) | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193101) | [3s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193101) | [3s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193101) | 1 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193092) | [3s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193092) | [3s](https://github.com/iree-org/iree/actions/runs/45529744348/job/139077193092) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 72 | 8% (6/72) |  | 13h14m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 104 | 6% (6/104) |  | 13h29m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
