# iree-ci-monitor

_Updated: 2026-07-04 00:17 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [6s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761311) | [6s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761333) | — | 6 |
| `ubuntu-24.04` | github-hosted | 16 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761321) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761330) | 50% (1/2) | 16 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761319) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761332) | — | 5 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761317) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761324) | — | 6 |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 0 | 0s | 0s | — | 6 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 1 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | 0s | 0s | — | 1 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761311) | [6s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761311) | [6s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761311) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761333) | [6s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761333) | [6s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761333) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761323) | [5s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761323) | [5s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761323) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761327) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761327) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761327) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761330) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761330) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761330) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761324) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761324) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761324) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761332) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761332) | [3s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761332) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28681975304/job/85073851481) | [3s](https://github.com/iree-org/iree/actions/runs/28681975304/job/85073851481) | [3s](https://github.com/iree-org/iree/actions/runs/28681975304/job/85073851481) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761328) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761328) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761328) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761321) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761321) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761321) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761317) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761317) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761317) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761319) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761319) | [2s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108761319) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28646265418/job/85085643887) | [2s](https://github.com/iree-org/iree/actions/runs/28646265418/job/85085643887) | [2s](https://github.com/iree-org/iree/actions/runs/28646265418/job/85085643887) | 1 |
| `.github/workflows/ci.yml` | linux_x64_gcc / linux_x64_gcc | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28646265418/job/85075502056) | [2s](https://github.com/iree-org/iree/actions/runs/28646265418/job/85075502056) | [2s](https://github.com/iree-org/iree/actions/runs/28646265418/job/85075502056) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108751298) | [1s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108751298) | [1s](https://github.com/iree-org/iree/actions/runs/28697170732/job/85108751298) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28697155118/job/85108706031) | [1s](https://github.com/iree-org/iree/actions/runs/28697155118/job/85108706031) | [1s](https://github.com/iree-org/iree/actions/runs/28697155118/job/85108706031) | 1 |
| `.github/workflows/ci.yml` | linux_arm64_clang / linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | 0s | 0s | 0s | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | 0s | 0s | 0s | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 271 | 7% (20/271) |  | 9h45m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 210 | 1% (3/210) |  | 9h52m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 301 | 2% (7/301) |  | 9h53m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 234 | 1% (3/234) |  | 9h55m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 71 | 1% (1/71) |  | 10h13m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
