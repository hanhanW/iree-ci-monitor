# iree-ci-monitor

_Updated: 2026-07-08 05:51 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m38s](https://github.com/iree-org/iree/actions/runs/28934106212/job/85840086488) | [1m38s](https://github.com/iree-org/iree/actions/runs/28934106212/job/85840086488) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/28921222282/job/85798729804) | [5s](https://github.com/iree-org/iree/actions/runs/28921222282/job/85798729835) | — | 3 |
| `ubuntu-24.04` | github-hosted | 12 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28921222282/job/85798729812) | [4s](https://github.com/iree-org/iree/actions/runs/28919129322/job/85793506912) | 60% (3/5) | 11 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/28934083402/job/85840012165) | [3s](https://github.com/iree-org/iree/actions/runs/28934083402/job/85840012165) | — | 1 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28921222282/job/85798729830) | [2s](https://github.com/iree-org/iree/actions/runs/28921222282/job/85798729787) | — | 2 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28921222282/job/85798729884) | [2s](https://github.com/iree-org/iree/actions/runs/28934088958/job/85840028716) | — | 3 |
| `azure-linux-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28934068377/job/85839957917) | [1s](https://github.com/iree-org/iree/actions/runs/28934100372/job/85840066365) | 0% (0/2) | 2 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659037) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | — | 0 |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659103) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659129) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659148) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659151) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | — | 0 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 3 | 3 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659155) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659172) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659179) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659317) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659037) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659103) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659129) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659148) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659151) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659155) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659164) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659172) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659178) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659179) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659219) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `convert-broadcast-batch-matmul` | pull_request |
| [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659317) | 2026-07-06 06:33 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `convert-broadcast-batch-matmul` | pull_request |
| [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620205987) | 2026-07-07 06:05 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | `integrates/llvm-20260707` | pull_request |
| [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206031) | 2026-07-07 06:05 PDT | `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | `integrates/llvm-20260707` | pull_request |
| [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206069) | 2026-07-07 06:05 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `integrates/llvm-20260707` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659317) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659179) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659129) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659155) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659103) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659037) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659164) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659178) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659148) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659151) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659172) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659219) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 1 | [19m09s](https://github.com/iree-org/iree/actions/runs/28865440225/job/85620206069) | 2026-07-07 06:05 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m38s](https://github.com/iree-org/iree/actions/runs/28934106212/job/85840086488) | [1m38s](https://github.com/iree-org/iree/actions/runs/28934106212/job/85840086488) | [1m38s](https://github.com/iree-org/iree/actions/runs/28934106212/job/85840086488) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28921222282/job/85798729835) | [5s](https://github.com/iree-org/iree/actions/runs/28921222282/job/85798729835) | [5s](https://github.com/iree-org/iree/actions/runs/28921222282/job/85798729835) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28921222282/job/85798729766) | [5s](https://github.com/iree-org/iree/actions/runs/28921222282/job/85798729766) | [5s](https://github.com/iree-org/iree/actions/runs/28921222282/job/85798729766) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28921222282/job/85798729804) | [5s](https://github.com/iree-org/iree/actions/runs/28921222282/job/85798729804) | [5s](https://github.com/iree-org/iree/actions/runs/28921222282/job/85798729804) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/28919129322/job/85793506912) | [4s](https://github.com/iree-org/iree/actions/runs/28919129322/job/85793506912) | [4s](https://github.com/iree-org/iree/actions/runs/28919129322/job/85793506912) | 1 |
| `.github/workflows/ci_linux_x64_clang_byollvm.yml` | linux_x64_clang_byollvm | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28934105523/job/85840084430) | [3s](https://github.com/iree-org/iree/actions/runs/28934105523/job/85840084430) | [3s](https://github.com/iree-org/iree/actions/runs/28934105523/job/85840084430) | 1 |
| `.github/workflows/ci_macos_x64_clang.yml` | macos_x64_clang | `macos-15-intel` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28934083402/job/85840012165) | [3s](https://github.com/iree-org/iree/actions/runs/28934083402/job/85840012165) | [3s](https://github.com/iree-org/iree/actions/runs/28934083402/job/85840012165) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 295 | 3% (9/294) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 229 | 1% (3/228) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 250 | 8% (20/249) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 218 | 1% (3/217) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 70 | 9% (6/70) |  | 13h38m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
