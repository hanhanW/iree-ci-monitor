# iree-ci-monitor

_Updated: 2026-10-29 06:10 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [20m44s](https://github.com/iree-org/iree/actions/runs/40847701207/job/123362379587) | [35m52s](https://github.com/iree-org/iree/actions/runs/40847701207/job/123362379461) | — | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [15m29s](https://github.com/iree-org/iree/actions/runs/40856586135/job/123393214751) | [31m00s](https://github.com/iree-org/iree/actions/runs/40851408208/job/123400807992) | — | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [14m23s](https://github.com/iree-org/iree/actions/runs/40851408208/job/123400808154) | [23m01s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156502) | — | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [14m48s](https://github.com/iree-org/iree/actions/runs/40856586135/job/123393214831) | [19m34s](https://github.com/iree-org/iree/actions/runs/40847701207/job/123362379604) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [8m16s](https://github.com/iree-org/iree/actions/runs/40847701207/job/123362379078) | [15m55s](https://github.com/iree-org/iree/actions/runs/40847701207/job/123362381132) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [11m27s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156444) | [11m30s](https://github.com/iree-org/iree/actions/runs/40851408208/job/123400807757) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [3m12s](https://github.com/iree-org/iree/actions/runs/40847701207/job/123362379456) | [3m19s](https://github.com/iree-org/iree/actions/runs/40856586135/job/123393214745) | — | `shark55-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m37s](https://github.com/iree-org/iree/actions/runs/40848985667/job/123363438662) | [1m37s](https://github.com/iree-org/iree/actions/runs/40848985667/job/123363438662) | 100% (1/1) | 1 |
| `azure-linux-scale` | ossci | 26 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891712) | [40s](https://github.com/iree-org/iree/actions/runs/40856586297/job/123389072281) | 0% (0/2) | 26 |
| `macos-15` | github-hosted | 15 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/40847701163/job/123359243684) | [8s](https://github.com/iree-org/iree/actions/runs/40856586297/job/123389071970) | — | 15 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/40851408033/job/123396556366) | [5s](https://github.com/iree-org/iree/actions/runs/40856586297/job/123389072038) | — | 15 |
| `ubuntu-24.04` | github-hosted | 105 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/40851408208/job/123400807841) | [3s](https://github.com/iree-org/iree/actions/runs/40856586135/job/123393215012) | 20% (1/5) | 98 |
| `windows-2022` | github-hosted | 14 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40847701163/job/123359243836) | [3s](https://github.com/iree-org/iree/actions/runs/40851408033/job/123396556651) | — | 14 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/40856586297/job/123389072282) | [2s](https://github.com/iree-org/iree/actions/runs/40851408033/job/123396556812) | — | 4 |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [17m11s](https://github.com/iree-org/iree/actions/runs/40851408208/job/123400808035) | [35m52s](https://github.com/iree-org/iree/actions/runs/40847701207/job/123362379461) | [35m52s](https://github.com/iree-org/iree/actions/runs/40847701207/job/123362379461) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [24m54s](https://github.com/iree-org/iree/actions/runs/40851408208/job/123400807971) | [35m39s](https://github.com/iree-org/iree/actions/runs/40856586135/job/123393214874) | [35m39s](https://github.com/iree-org/iree/actions/runs/40856586135/job/123393214874) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [21m24s](https://github.com/iree-org/iree/actions/runs/40856586135/job/123393215046) | [31m00s](https://github.com/iree-org/iree/actions/runs/40851408208/job/123400807992) | [31m00s](https://github.com/iree-org/iree/actions/runs/40851408208/job/123400807992) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [15m29s](https://github.com/iree-org/iree/actions/runs/40856586135/job/123393214751) | [28m44s](https://github.com/iree-org/iree/actions/runs/40847701207/job/123362379614) | [28m44s](https://github.com/iree-org/iree/actions/runs/40847701207/job/123362379614) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [14m23s](https://github.com/iree-org/iree/actions/runs/40851408208/job/123400808154) | [23m01s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156502) | [23m01s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156502) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [16m06s](https://github.com/iree-org/iree/actions/runs/40851408208/job/123400807914) | [19m34s](https://github.com/iree-org/iree/actions/runs/40847701207/job/123362379604) | [19m34s](https://github.com/iree-org/iree/actions/runs/40847701207/job/123362379604) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [9m56s](https://github.com/iree-org/iree/actions/runs/40851408208/job/123400807946) | [15m55s](https://github.com/iree-org/iree/actions/runs/40847701207/job/123362381132) | [15m55s](https://github.com/iree-org/iree/actions/runs/40847701207/job/123362381132) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [14m48s](https://github.com/iree-org/iree/actions/runs/40856586135/job/123393214831) | [15m35s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156495) | [15m35s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156495) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [8m16s](https://github.com/iree-org/iree/actions/runs/40847701207/job/123362379078) | [11m57s](https://github.com/iree-org/iree/actions/runs/40851408208/job/123400808194) | [11m57s](https://github.com/iree-org/iree/actions/runs/40851408208/job/123400808194) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [11m27s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156444) | [11m30s](https://github.com/iree-org/iree/actions/runs/40851408208/job/123400807757) | [11m30s](https://github.com/iree-org/iree/actions/runs/40851408208/job/123400807757) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [3m12s](https://github.com/iree-org/iree/actions/runs/40847701207/job/123362379456) | [3m19s](https://github.com/iree-org/iree/actions/runs/40856586135/job/123393214745) | [3m19s](https://github.com/iree-org/iree/actions/runs/40856586135/job/123393214745) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m37s](https://github.com/iree-org/iree/actions/runs/40848985667/job/123363438662) | [1m37s](https://github.com/iree-org/iree/actions/runs/40848985667/job/123363438662) | [1m37s](https://github.com/iree-org/iree/actions/runs/40848985667/job/123363438662) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 4 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/40856586297/job/123389071879) | [1m18s](https://github.com/iree-org/iree/actions/runs/40851408033/job/123396556830) | [1m18s](https://github.com/iree-org/iree/actions/runs/40851408033/job/123396556830) | 4 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123267894141) | [54s](https://github.com/iree-org/iree/actions/runs/40856586135/job/123389074542) | [54s](https://github.com/iree-org/iree/actions/runs/40856586135/job/123389074542) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 4 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891807) | [40s](https://github.com/iree-org/iree/actions/runs/40856586297/job/123389072281) | [40s](https://github.com/iree-org/iree/actions/runs/40856586297/job/123389072281) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/40851408033/job/123396556983) | [11s](https://github.com/iree-org/iree/actions/runs/40856586297/job/123389072252) | [11s](https://github.com/iree-org/iree/actions/runs/40856586297/job/123389072252) | 4 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/40856586297/job/123389072155) | [10s](https://github.com/iree-org/iree/actions/runs/40851408033/job/123396556727) | [10s](https://github.com/iree-org/iree/actions/runs/40851408033/job/123396556727) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/40847701163/job/123359244101) | [10s](https://github.com/iree-org/iree/actions/runs/40851408033/job/123396557164) | [10s](https://github.com/iree-org/iree/actions/runs/40851408033/job/123396557164) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891712) | [10s](https://github.com/iree-org/iree/actions/runs/40856586297/job/123389072446) | [10s](https://github.com/iree-org/iree/actions/runs/40856586297/job/123389072446) | 4 |
| `.github/workflows/ci_linux_x64_clang_tsan.yml` | linux_x64_clang_tsan | `azure-linux-scale` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/40848976837/job/123363408613) | [10s](https://github.com/iree-org/iree/actions/runs/40848976837/job/123363408613) | [10s](https://github.com/iree-org/iree/actions/runs/40848976837/job/123363408613) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 254 | 2% (4/254) |  | 1h52m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 209 | 2% (5/209) |  | 2h07m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
