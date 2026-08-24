# iree-ci-monitor

_Updated: 2026-08-24 00:30 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [11m38s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713363) | [17m48s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713382) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [14m26s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713371) | [14m26s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713371) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [11m31s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713339) | [11m31s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713339) | — | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713359) | [8m06s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713326) | — | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [7m42s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713344) | [7m42s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713344) | — | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [4m41s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713330) | [4m41s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713330) | — | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713348) | [4m35s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713357) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [3m15s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713396) | [3m15s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713396) | — | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [2m22s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713374) | [2m48s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713355) | — | `shark01-ci`, `shark55-ci` |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988755) | [6s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988894) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988751) | [4s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988972) | — | 3 |
| `ubuntu-24.04` | github-hosted | 22 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713388) | [3s](https://github.com/iree-org/iree/actions/runs/32692975527/job/97329842146) | 0% (0/4) | 22 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988863) | [3s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329989020) | — | 2 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713272) | [1s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713272) | — | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713329) | [1s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713329) | — | `shark01-ci` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [17m48s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713382) | [17m48s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713382) | [17m48s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713382) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [14m26s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713371) | [14m26s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713371) | [14m26s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713371) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [11m38s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713363) | [11m38s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713363) | [11m38s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713363) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [11m31s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713339) | [11m31s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713339) | [11m31s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713339) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [8m06s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713326) | [8m06s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713326) | [8m06s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713326) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [7m42s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713344) | [7m42s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713344) | [7m42s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713344) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [4m41s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713330) | [4m41s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713330) | [4m41s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713330) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [4m35s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713357) | [4m35s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713357) | [4m35s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713357) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [3m15s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713396) | [3m15s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713396) | [3m15s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713396) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [2m48s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713355) | [2m48s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713355) | [2m48s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713355) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [2m22s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713374) | [2m22s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713374) | [2m22s](https://github.com/iree-org/iree/actions/runs/32667669376/job/97264713374) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988894) | [6s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988894) | [6s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988894) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988972) | [4s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988972) | [4s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988972) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988734) | [4s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988734) | [4s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988734) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988751) | [4s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988751) | [4s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988751) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988801) | [3s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988801) | [3s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988801) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988863) | [3s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988863) | [3s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329988863) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329989020) | [3s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329989020) | [3s](https://github.com/iree-org/iree/actions/runs/32693015912/job/97329989020) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32692975527/job/97329842146) | [3s](https://github.com/iree-org/iree/actions/runs/32692975527/job/97329842146) | [3s](https://github.com/iree-org/iree/actions/runs/32692975527/job/97329842146) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32672439743/job/97275181091) | [2s](https://github.com/iree-org/iree/actions/runs/32672442558/job/97275188453) | [2s](https://github.com/iree-org/iree/actions/runs/32672442558/job/97275188453) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 217 | 1% (3/216) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 152 | 0% (0/151) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 205 | 2% (5/204) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 155 | 0% (0/154) | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
