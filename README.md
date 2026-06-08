# iree-ci-monitor

_Updated: 2026-06-08 06:48 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m23s](https://github.com/iree-org/iree/actions/runs/27132797840/job/80077707290) | [1m23s](https://github.com/iree-org/iree/actions/runs/27132797840/job/80077707290) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630461) | [44s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760735) | 0% (0/3) | 6 |
| `azure-linux-scale` | ossci | 8 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760776) | [10s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760851) | 0% (0/8) | 8 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/27132751798/job/80077554342) | [4s](https://github.com/iree-org/iree/actions/runs/27132751798/job/80077554342) | — | 1 |
| `ubuntu-24.04` | github-hosted | 30 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630390) | [3s](https://github.com/iree-org/iree/actions/runs/27132802246/job/80077719285) | 9% (2/22) | 29 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760775) | [3s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630593) | 0% (0/3) | 6 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760714) | [3s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760731) | 0% (0/3) | 5 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27125158943/job/80051730278) | [3s](https://github.com/iree-org/iree/actions/runs/27125158943/job/80051730324) | 0% (0/3) | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760834) | [1s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760834) | 0% (0/1) | 1 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | 0% (0/2) | `shark10-ci`, `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0% (0/1) | `shark01-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0% (0/1) | `shark01-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0% (0/1) | `iree-mi308-1` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0% (0/1) | `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0% (0/1) | `shark01-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0% (0/1) | `shark10-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | 0s | 0s | 0% (0/4) | 4 |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | 0s | 0s | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m23s](https://github.com/iree-org/iree/actions/runs/27132797840/job/80077707290) | [1m23s](https://github.com/iree-org/iree/actions/runs/27132797840/job/80077707290) | [1m23s](https://github.com/iree-org/iree/actions/runs/27132797840/job/80077707290) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 1 | 0 | — | — | [1m05s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760842) | [1m05s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760842) | [1m05s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760842) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [44s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760735) | [44s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760735) | [44s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760735) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760851) | [10s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760851) | [10s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760851) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760765) | [9s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760765) | [9s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760765) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760853) | [9s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760853) | [9s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760853) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760776) | [8s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760776) | [8s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760776) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760724) | [6s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760724) | [6s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760724) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630461) | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630461) | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630461) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630338) | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630338) | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630338) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630367) | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630367) | [5s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630367) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760713) | [5s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760713) | [5s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760713) | 1 |
| `.github/workflows/ci_macos_x64_clang.yml` | macos_x64_clang | `macos-15-intel` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/27132751798/job/80077554342) | [4s](https://github.com/iree-org/iree/actions/runs/27132751798/job/80077554342) | [4s](https://github.com/iree-org/iree/actions/runs/27132751798/job/80077554342) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630340) | [3s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630340) | [3s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630340) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630593) | [3s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630593) | [3s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630593) | 1 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760731) | [3s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760731) | [3s](https://github.com/iree-org/iree/actions/runs/27125160072/job/80051760731) | 1 |
| `.github/workflows/ci_linux_x64_gcc.yml` | linux_x64_gcc | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27132802246/job/80077719285) | [3s](https://github.com/iree-org/iree/actions/runs/27132802246/job/80077719285) | [3s](https://github.com/iree-org/iree/actions/runs/27132802246/job/80077719285) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27125158943/job/80051730324) | [3s](https://github.com/iree-org/iree/actions/runs/27125158943/job/80051730324) | [3s](https://github.com/iree-org/iree/actions/runs/27125158943/job/80051730324) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27125158943/job/80051730278) | [3s](https://github.com/iree-org/iree/actions/runs/27125158943/job/80051730278) | [3s](https://github.com/iree-org/iree/actions/runs/27125158943/job/80051730278) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630390) | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630390) | [2s](https://github.com/iree-org/iree/actions/runs/27120288647/job/80035630390) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 297 | 1% (2/297) |  | 4h28m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 228 | 0% (1/228) |  | 4h44m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 250 | 3% (8/250) |  | 4h50m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 212 | 0% (0/212) |  | 4h52m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 68 | 0% (0/68) |  | 5h04m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
