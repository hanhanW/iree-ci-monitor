# iree-ci-monitor

_Updated: 2026-08-05 02:07 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [10m57s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137181) | [22m04s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137055) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [6m52s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137045) | [21m30s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137051) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [8m20s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137030) | [20m15s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137180) | — | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136867) | [17m15s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136974) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [16m24s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136913) | [16m24s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136913) | — | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [13m19s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136907) | [13m19s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136907) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [10m32s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137087) | [10m32s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137087) | — | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [5m41s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136837) | [5m41s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136837) | — | `shark10-ci` |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [11s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92234566715) | [1m38s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92234266783) | — | 5 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/30979755618/job/92221489170) | [1m15s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92234266624) | — | 5 |
| `ubuntu-24.04` | github-hosted | 30 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92234266540) | [10s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137019) | 0% (0/4) | 29 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92234266564) | [4s](https://github.com/iree-org/iree/actions/runs/30979755618/job/92221489152) | — | 6 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92234266502) | [2s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92234266572) | — | 5 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136920) | [2s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136920) | — | `shark01-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136931) | [2s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136931) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137016) | [2s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137016) | — | `shark10-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92234266717) | [1s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92234266717) | — | 1 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 1 | 1 | [16h57m](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485324) | 2026-08-05 02:07 PDT | 0 | 0s | 0s | — | 0 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 1 | [16h57m](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485541) | 2026-08-05 02:07 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [16h57m](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485324) | 2026-08-05 02:07 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `integrates/llvm-20260731-cleanup` | pull_request |
| [16h57m](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485541) | 2026-08-05 02:07 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | `integrates/llvm-20260731-cleanup` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 1 | [16h57m](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485324) | 2026-08-05 02:07 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 1 | 1 | [16h57m](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485541) | 2026-08-05 02:07 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [22m04s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137055) | [22m04s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137055) | [22m04s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137055) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [21m30s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137051) | [21m30s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137051) | [21m30s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137051) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [20m15s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137180) | [20m15s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137180) | [20m15s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137180) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [17m15s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136974) | [17m15s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136974) | [17m15s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136974) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [16m24s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136913) | [16m24s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136913) | [16m24s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136913) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [13m19s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136907) | [13m19s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136907) | [13m19s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136907) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [10m57s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137181) | [10m57s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137181) | [10m57s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137181) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [10m32s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137087) | [10m32s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137087) | [10m32s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137087) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [8m20s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137030) | [8m20s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137030) | [8m20s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137030) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [6m52s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137045) | [6m52s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137045) | [6m52s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137045) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [5m41s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136837) | [5m41s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136837) | [5m41s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136837) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [1m38s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92234266783) | [1m38s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92234266783) | [1m38s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92234266783) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [1m17s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92234266647) | [1m17s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92234266647) | [1m17s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92234266647) | 1 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | 1 | 0 | — | — | [1m16s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92234267211) | [1m16s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92234267211) | [1m16s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92234267211) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 1 | 0 | — | — | [1m15s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92234266624) | [1m15s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92234266624) | [1m15s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92234266624) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92234566715) | [11s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92234566715) | [11s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92234566715) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137019) | [10s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137019) | [10s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137019) | 1 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136794) | [9s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136794) | [9s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136794) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 166 | 0% (0/166) |  | 1h15m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 149 | 2% (3/149) |  | 1h15m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 122 | 1% (1/122) |  | 1h23m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 118 | 0% (0/118) |  | 1h24m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 33 | 0% (0/33) |  | 1d19h ago |

## Alerts

- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job observed waiting 16h57m (> 2h00m)
- **[stale-queued]** `nodai-amdgpu-mi308-x86-64` oldest queued job observed waiting 16h57m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
