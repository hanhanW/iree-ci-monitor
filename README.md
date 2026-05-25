# iree-ci-monitor

_Updated: 2026-05-25 06:29 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m33s](https://github.com/iree-org/iree/actions/runs/26396555310/job/77698492908) | [1m33s](https://github.com/iree-org/iree/actions/runs/26396555310/job/77698492908) | 100% (1/1) | 1 |
| `ubuntu-24.04` | github-hosted | 15 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539927) | [3s](https://github.com/iree-org/iree/actions/runs/26398972680/job/77706439006) | 50% (2/4) | 15 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26399219224/job/77707148780) | [3s](https://github.com/iree-org/iree/actions/runs/26399219490/job/77707126664) | — | 6 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/26396531888/job/77698416930) | [3s](https://github.com/iree-org/iree/actions/runs/26396531888/job/77698416930) | — | 1 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539893) | [2s](https://github.com/iree-org/iree/actions/runs/26396549640/job/77698475014) | — | 3 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539896) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539908) | — | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539912) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539913) | — | 2 |
| `azure-linux-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26396516239/job/77698363588) | [1s](https://github.com/iree-org/iree/actions/runs/26396551209/job/77698479799) | 0% (0/2) | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m33s](https://github.com/iree-org/iree/actions/runs/26396555310/job/77698492908) | [1m33s](https://github.com/iree-org/iree/actions/runs/26396555310/job/77698492908) | [1m33s](https://github.com/iree-org/iree/actions/runs/26396555310/job/77698492908) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/26385356346/job/77662624332) | [4s](https://github.com/iree-org/iree/actions/runs/26385356346/job/77662624332) | [4s](https://github.com/iree-org/iree/actions/runs/26385356346/job/77662624332) | 1 |
| `.github/workflows/ci_macos_x64_clang.yml` | macos_x64_clang | `macos-15-intel` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26396531888/job/77698416930) | [3s](https://github.com/iree-org/iree/actions/runs/26396531888/job/77698416930) | [3s](https://github.com/iree-org/iree/actions/runs/26396531888/job/77698416930) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26398972680/job/77706439006) | [3s](https://github.com/iree-org/iree/actions/runs/26398972680/job/77706439006) | [3s](https://github.com/iree-org/iree/actions/runs/26398972680/job/77706439006) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26399219490/job/77707126664) | [3s](https://github.com/iree-org/iree/actions/runs/26399219490/job/77707126664) | [3s](https://github.com/iree-org/iree/actions/runs/26399219490/job/77707126664) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26399219490/job/77707126635) | [3s](https://github.com/iree-org/iree/actions/runs/26399219490/job/77707126635) | [3s](https://github.com/iree-org/iree/actions/runs/26399219490/job/77707126635) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77706318004) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77706318004) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77706318004) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539895) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539895) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539895) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539896) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539896) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539896) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539908) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539908) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539908) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539886) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539886) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539886) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539918) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539918) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539918) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539927) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539927) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539927) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539920) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539920) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539920) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539893) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539893) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539893) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539890) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539890) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539890) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667524020) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667524020) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667524020) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539913) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539913) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539913) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539912) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539912) | [2s](https://github.com/iree-org/iree/actions/runs/26386958526/job/77667539912) | 1 |
| `.github/workflows/ci_linux_x64_clang_byollvm.yml` | linux_x64_clang_byollvm | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26396552354/job/77698483194) | [2s](https://github.com/iree-org/iree/actions/runs/26396552354/job/77698483194) | [2s](https://github.com/iree-org/iree/actions/runs/26396552354/job/77698483194) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 296 | 2% (5/295) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 266 | 8% (20/265) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 226 | 3% (7/225) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 220 | 1% (2/219) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 70 | 3% (2/70) |  | 2d18h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
