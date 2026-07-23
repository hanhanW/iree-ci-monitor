# iree-ci-monitor

_Updated: 2026-07-23 00:11 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [36m43s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060051) | [36m43s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060051) | — | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [34m56s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127059877) | [34m56s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127059877) | — | `shark01-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [28m18s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060059) | [28m18s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060059) | — | `shark01-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [7m53s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060015) | [19m55s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060126) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [5m05s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060078) | [15m23s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060109) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [13m08s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060070) | [13m08s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060070) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060022) | [11m10s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060193) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [8m04s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127059971) | [8m04s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127059971) | — | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060023) | [6m48s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060046) | — | `shark10-ci` |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940361) | [20s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89125959568) | — | 5 |
| `ubuntu-24.04` | github-hosted | 29 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060057) | [3s](https://github.com/iree-org/iree/actions/runs/29981446421/job/89123890659) | 50% (2/4) | 29 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29983858033/job/89131362854) | [3s](https://github.com/iree-org/iree/actions/runs/29983858033/job/89131362842) | — | 5 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29983858033/job/89131362851) | [3s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940362) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29983858033/job/89131362858) | [3s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940245) | — | 6 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940382) | [1s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940382) | — | 1 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127059951) | [1s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127059951) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060016) | [1s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060016) | — | `shark01-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060195) | [1s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060195) | — | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 1 | 1 | [1h37m](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127059930) | 2026-07-23 00:10 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [1h37m](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127059930) | 2026-07-23 00:10 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `pinned-transfer-execution-placement` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 1 | [1h37m](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127059930) | 2026-07-23 00:10 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [36m43s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060051) | [36m43s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060051) | [36m43s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060051) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [34m56s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127059877) | [34m56s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127059877) | [34m56s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127059877) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [28m18s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060059) | [28m18s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060059) | [28m18s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060059) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [19m55s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060126) | [19m55s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060126) | [19m55s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060126) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [15m23s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060109) | [15m23s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060109) | [15m23s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060109) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [13m08s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060070) | [13m08s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060070) | [13m08s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060070) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [11m10s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060193) | [11m10s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060193) | [11m10s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060193) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [8m04s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127059971) | [8m04s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127059971) | [8m04s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127059971) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [7m53s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060015) | [7m53s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060015) | [7m53s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060015) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [6m48s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060046) | [6m48s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060046) | [6m48s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060046) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [5m05s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060078) | [5m05s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060078) | [5m05s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89127060078) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [20s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89125959568) | [20s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89125959568) | [20s](https://github.com/iree-org/iree/actions/runs/29982094414/job/89125959568) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940359) | [10s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940359) | [10s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940359) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940333) | [8s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940333) | [8s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940333) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940361) | [8s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940361) | [8s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940361) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940339) | [8s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940339) | [8s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940339) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29983858033/job/89131362842) | [3s](https://github.com/iree-org/iree/actions/runs/29983858033/job/89131362842) | [3s](https://github.com/iree-org/iree/actions/runs/29983858033/job/89131362842) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89132119317) | [3s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89132119317) | [3s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89132119317) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940245) | [3s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940245) | [3s](https://github.com/iree-org/iree/actions/runs/29982094432/job/89125940245) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 282 | 1% (4/282) |  | 53m00s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 288 | 4% (11/288) |  | 55m19s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 364 | 1% (3/364) |  | 1h05m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 274 | 1% (2/274) |  | 1h16m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 84 | 1% (1/84) |  | 1h26m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
