# iree-ci-monitor

_Updated: 2026-08-03 11:55 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [21m26s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209506) | [28m52s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715579) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [6m46s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715313) | [23m08s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209390) | — | `shark01-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [14m05s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209383) | [22m58s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715320) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209405) | [21m53s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715379) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [14m31s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715417) | [21m03s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209784) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [18m16s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715642) | [18m52s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209416) | — | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [4m03s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209446) | [17m34s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715634) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209774) | [14m51s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715438) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [8m51s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209454) | [14m26s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209476) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715252) | [6m57s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209246) | — | `shark75-ci` |
| `azure-linux-scale` | ossci | 12 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903683) | [1m26s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91691948384) | 0% (0/2) | 12 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m23s](https://github.com/iree-org/iree/actions/runs/30805686015/job/91660398126) | [1m23s](https://github.com/iree-org/iree/actions/runs/30805686015/job/91660398126) | 0% (0/1) | 1 |
| `macos-14` | github-hosted | 7 | 0 | — | — | 0 | [41s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903396) | [45s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903582) | 0% (0/1) | 7 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903551) | [33s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903438) | — | 6 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903427) | [14s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903540) | — | 6 |
| `ubuntu-24.04` | github-hosted | 42 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30805687964/job/91660404214) | [9s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91701890751) | 0% (0/3) | 42 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30826033761/job/91727777310) | [8s](https://github.com/iree-org/iree/actions/runs/30826033761/job/91727777226) | — | 15 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715314) | [7s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209375) | — | `iree-mi308-1` |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30805663080/job/91660323617) | [3s](https://github.com/iree-org/iree/actions/runs/30805663080/job/91660323617) | 0% (0/1) | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715224) | [2s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209242) | — | `shark01-ci`, `shark10-ci` |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [0s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903678) | [0s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903678) | — | 2 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 2 | 2 | [9h37m](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715262) | 2026-08-03 11:55 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [9h37m](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715262) | 2026-08-03 11:55 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `conv-dt-lower-to-ukernel` | pull_request |
| [5h52m](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209322) | 2026-08-03 11:55 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `integrates/llvm-20260731-cleanup` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 2 | [9h37m](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715262) | 2026-08-03 11:55 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [21m26s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209506) | [28m52s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715579) | [28m52s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715579) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [6m46s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715313) | [23m08s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209390) | [23m08s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209390) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [14m05s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209383) | [22m58s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715320) | [22m58s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715320) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209405) | [21m53s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715379) | [21m53s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715379) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [6m15s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715462) | [21m03s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209784) | [21m03s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209784) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [18m16s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715642) | [18m52s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209416) | [18m52s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209416) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [4m03s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209446) | [17m34s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715634) | [17m34s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715634) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [7m48s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715429) | [14m55s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209362) | [14m55s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209362) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209774) | [14m51s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715438) | [14m51s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715438) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [7m04s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209458) | [14m31s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715417) | [14m31s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715417) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715430) | [14m26s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209476) | [14m26s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209476) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [6m33s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715530) | [8m51s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209454) | [8m51s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209454) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715252) | [6m57s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209246) | [6m57s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209246) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [1m26s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91691948384) | [1m26s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91691948384) | [1m26s](https://github.com/iree-org/iree/actions/runs/30815414228/job/91691948384) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m23s](https://github.com/iree-org/iree/actions/runs/30805686015/job/91660398126) | [1m23s](https://github.com/iree-org/iree/actions/runs/30805686015/job/91660398126) | [1m23s](https://github.com/iree-org/iree/actions/runs/30805686015/job/91660398126) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30798185949/job/91686014357) | [1m14s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903753) | [1m14s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903753) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 2 | 0 | — | — | [45s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903582) | [45s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903582) | [45s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903582) | 2 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 2 | 0 | — | — | [41s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903396) | [41s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903396) | [41s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903396) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 2 | 0 | — | — | [33s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903438) | [33s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903438) | [33s](https://github.com/iree-org/iree/actions/runs/30815414300/job/91691903438) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 175 | 0% (0/175) |  | 5h19m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 125 | 1% (1/125) |  | 5h20m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 130 | 1% (1/130) |  | 5h22m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 155 | 3% (4/155) |  | 5h28m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 39 | 3% (1/39) |  | 5h41m ago |

## Alerts

- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job observed waiting 9h37m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
