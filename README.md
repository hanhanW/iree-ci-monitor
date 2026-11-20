# iree-ci-monitor

_Updated: 2026-11-20 12:27 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [11m30s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133658) | [25m12s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133588) | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [19m08s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133320) | [19m08s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133320) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133302) | [15m41s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133434) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [8m57s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133674) | [12m26s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133340) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [1m43s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133437) | [9m05s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133558) | — | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [5m49s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133284) | [5m49s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133284) | — | `shark75-ci` |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 0 | [2m51s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512441987) | [4m29s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442119) | — | 6 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442067) | [6s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512441839) | — | 3 |
| `macos-15` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512441861) | [5s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442087) | — | 3 |
| `ubuntu-24.04` | github-hosted | 21 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133307) | [3s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133656) | 0% (0/1) | 21 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512441968) | [2s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512443174) | — | 3 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/44750436583/job/136336691132) | [2s](https://github.com/iree-org/iree/actions/runs/44750436985/job/136336597556) | — | 6 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133125) | [1s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133125) | — | `shark75-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442254) | [1s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442254) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [25m12s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133588) | [25m12s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133588) | [25m12s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133588) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [19m08s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133320) | [19m08s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133320) | [19m08s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133320) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [15m41s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133434) | [15m41s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133434) | [15m41s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133434) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [12m26s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133340) | [12m26s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133340) | [12m26s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133340) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [11m30s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133658) | [11m30s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133658) | [11m30s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133658) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [9m05s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133558) | [9m05s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133558) | [9m05s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133558) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [8m57s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133674) | [8m57s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133674) | [8m57s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133674) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [5m49s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133284) | [5m49s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133284) | [5m49s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133284) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [4m29s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442119) | [4m29s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442119) | [4m29s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442119) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 1 | 0 | — | — | [3m13s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442187) | [3m13s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442187) | [3m13s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442187) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [3m10s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442191) | [3m10s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442191) | [3m10s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442191) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [2m51s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512441987) | [2m51s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512441987) | [2m51s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512441987) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [1m43s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133437) | [1m43s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133437) | [1m43s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136516133437) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [20s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442005) | [20s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442005) | [20s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442005) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136512373080) | [8s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136512373080) | [8s](https://github.com/iree-org/iree/actions/runs/44800533612/job/136512373080) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512441839) | [6s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512441839) | [6s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512441839) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512441861) | [5s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512441861) | [5s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512441861) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442087) | [5s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442087) | [5s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442087) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442030) | [4s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442030) | [4s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442030) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442067) | [4s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442067) | [4s](https://github.com/iree-org/iree/actions/runs/44800533323/job/136512442067) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 271 | 2% (5/271) |  | 28m00s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 220 | 2% (4/220) |  | 39m31s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
