# iree-ci-monitor

_Updated: 2026-07-05 00:27 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 1 | [1m50s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628537) | [1m50s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628537) | — | 1 |
| `ubuntu-24.04` | github-hosted | 17 | 0 | — | — | 4 | [2s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202614890) | [1m49s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628546) | 0% (0/1) | 17 |
| `azure-linux-scale` | ossci | 7 | 0 | — | — | 7 | [49s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628540) | [1m38s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628509) | — | 7 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [6s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628437) | [1m37s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628469) | — | 6 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/28731838272/job/85198852709) | [1m19s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628538) | — | 6 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [53s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628556) | [53s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628556) | — | 1 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 4 | [2s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628450) | [51s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628483) | — | 5 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28733211163/job/85202612632) | [3s](https://github.com/iree-org/iree/actions/runs/28733211163/job/85202612648) | — | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628552) | [1s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628552) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | linux_x64_gcc / linux_x64_gcc | `ubuntu-24.04` | 1 | 0 | — | — | [1m57s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628526) | [1m57s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628526) | [1m57s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628526) | 1 |
| `.github/workflows/ci.yml` | linux_arm64_clang / linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m50s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628537) | [1m50s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628537) | [1m50s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628537) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_byollvm / linux_x64_clang_byollvm | `ubuntu-24.04` | 1 | 0 | — | — | [1m49s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628546) | [1m49s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628546) | [1m49s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628546) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [1m38s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628509) | [1m38s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628509) | [1m38s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628509) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [1m37s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628516) | [1m37s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628516) | [1m37s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628516) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1m37s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628469) | [1m37s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628469) | [1m37s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628469) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 1 | 0 | — | — | [1m30s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628488) | [1m30s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628488) | [1m30s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628488) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_tsan / linux_x64_clang_tsan | `azure-linux-scale` | 1 | 0 | — | — | [1m21s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628530) | [1m21s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628530) | [1m21s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628530) | 1 |
| `.github/workflows/ci.yml` | macos_arm64_clang / macos_arm64_clang | `macos-14` | 1 | 0 | — | — | [1m19s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628538) | [1m19s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628538) | [1m19s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628538) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 1 | 0 | — | — | [1m09s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628472) | [1m09s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628472) | [1m09s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628472) | 1 |
| `.github/workflows/ci.yml` | macos_x64_clang / macos_x64_clang | `macos-15-intel` | 1 | 0 | — | — | [53s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628556) | [53s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628556) | [53s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628556) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 1 | 0 | — | — | [51s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628483) | [51s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628483) | [51s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628483) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [49s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628540) | [49s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628540) | [49s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628540) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 1 | 0 | — | — | [37s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628441) | [37s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628441) | [37s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628441) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [34s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628499) | [34s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628499) | [34s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628499) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/28731838272/job/85198852704) | [7s](https://github.com/iree-org/iree/actions/runs/28731838272/job/85198852704) | [7s](https://github.com/iree-org/iree/actions/runs/28731838272/job/85198852704) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/28731838272/job/85198852739) | [7s](https://github.com/iree-org/iree/actions/runs/28731838272/job/85198852739) | [7s](https://github.com/iree-org/iree/actions/runs/28731838272/job/85198852739) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628492) | [6s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628492) | [6s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628492) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628437) | [6s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628437) | [6s](https://github.com/iree-org/iree/actions/runs/28733212532/job/85202628437) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28731838272/job/85198852710) | [5s](https://github.com/iree-org/iree/actions/runs/28731838272/job/85198852710) | [5s](https://github.com/iree-org/iree/actions/runs/28731838272/job/85198852710) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 244 | 8% (19/244) |  | 1d09h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 191 | 2% (3/191) |  | 1d10h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 271 | 3% (7/271) |  | 1d10h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 213 | 1% (3/213) |  | 1d10h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 64 | 2% (1/64) |  | 1d10h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
