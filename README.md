# iree-ci-monitor

_Updated: 2026-09-02 21:37 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527355) | [9s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527618) | — | 5 |
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527252) | [5s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100421355362) | — | 11 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527313) | [5s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527253) | — | 3 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527320) | [4s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527281) | — | 3 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527250) | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527120) | — | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527389) | [1s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527389) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527618) | [9s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527618) | [9s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527618) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527355) | [8s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527355) | [8s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527355) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527397) | [8s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527397) | [8s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527397) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527343) | [7s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527343) | [7s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527343) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100421355362) | [5s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100421355362) | [5s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100421355362) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527253) | [5s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527253) | [5s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527253) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527281) | [4s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527281) | [4s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527281) | 1 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527208) | [4s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527208) | [4s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527208) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527120) | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527120) | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527120) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527313) | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527313) | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527313) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527320) | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527320) | [3s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527320) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527093) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527093) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527093) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527124) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527124) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527124) | 1 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527126) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527126) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527126) | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527094) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527094) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527094) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527250) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527250) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527250) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527227) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527227) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527227) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527156) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527156) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527156) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527252) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527252) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408527252) | 1 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408461483) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408461483) | [2s](https://github.com/iree-org/iree/actions/runs/33678321456/job/100408461483) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 199 | 0% (0/199) |  | 15h11m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 171 | 4% (7/171) |  | 15h14m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 133 | 0% (0/133) |  | 15h17m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 139 | 1% (1/139) |  | 15h21m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
