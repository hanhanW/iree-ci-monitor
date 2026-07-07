# iree-ci-monitor

_Updated: 2026-07-07 00:29 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 2 | [6s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485471) | [6s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485477) | — | 3 |
| `ubuntu-24.04` | github-hosted | 9 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550464155) | [4s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485484) | 50% (2/4) | 9 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485472) | [3s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485494) | — | 2 |
| `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28825247906/job/85486692567) | [2s](https://github.com/iree-org/iree/actions/runs/28825985992/job/85489026015) | 0% (0/2) | 2 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485476) | [2s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485496) | — | 2 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659037) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | — | 0 |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659103) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659129) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201` | self-hosted | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659148) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659151) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | — | 0 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659155) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 2 | 2 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659172) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659179) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659317) | 2026-07-06 06:33 PDT | 0 | 0s | 0s | — | 0 |

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

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659037) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659317) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659179) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659164) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659178) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659148) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659151) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659129) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659155) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659172) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659219) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 1 | [57m17s](https://github.com/iree-org/iree/actions/runs/28791438732/job/85372659103) | 2026-07-06 06:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485471) | [6s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485471) | [6s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485471) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485477) | [6s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485477) | [6s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485477) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485482) | [5s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485482) | [5s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485482) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485484) | [4s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485484) | [4s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485484) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485493) | [3s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485493) | [3s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485493) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485503) | [3s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485503) | [3s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485503) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485494) | [3s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485494) | [3s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485494) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485479) | [2s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485479) | [2s](https://github.com/iree-org/iree/actions/runs/28846150703/job/85550485479) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 299 | 3% (8/299) |  | 14h22m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 216 | 1% (3/216) |  | 15h07m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 232 | 1% (3/232) |  | 15h09m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 71 | 1% (1/71) |  | 15h10m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 265 | 8% (21/265) |  | 15h11m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
