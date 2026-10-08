# iree-ci-monitor

_Updated: 2026-10-08 16:24 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [1h22m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166351) | [5h20m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166657) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [4h57m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166160) | [5h18m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166779) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [3h59m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166420) | [4h24m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166309) | — | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113513391787) | [3h31m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166058) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [17m54s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113513391788) | [3h18m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166273) | — | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [23m26s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113513391822) | [2h59m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166342) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [1h14m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166651) | [1h36m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166661) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2m23s](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166562) | [10m22s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113513391794) | — | `shark55-ci` |
| `azure-linux-scale` | ossci | 12 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/37825138381/job/113507491141) | [1m03s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660952) | — | 12 |
| `macos-15` | github-hosted | 6 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660653) | [44s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660597) | — | 6 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/37825138381/job/113507490861) | [36s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660454) | — | 6 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/37825138381/job/113507490860) | [29s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660736) | — | 6 |
| `ubuntu-24.04` | github-hosted | 56 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166633) | [3s](https://github.com/iree-org/iree/actions/runs/37825138381/job/113525381053) | 67% (2/3) | 55 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37785012926/job/113337408061) | [3s](https://github.com/iree-org/iree/actions/runs/37785014831/job/113337414942) | — | 6 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337661028) | [2s](https://github.com/iree-org/iree/actions/runs/37825138381/job/113507491138) | — | 2 |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113513392153) | [5h20m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166657) | [5h20m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166657) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [26m51s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113513391899) | [5h18m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166779) | [5h18m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166779) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [15m30s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113513391608) | [4h57m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166160) | [4h57m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166160) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [3m43s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113513391674) | [4h24m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166309) | [4h24m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166309) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [20m49s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113513391959) | [3h59m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166420) | [3h59m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166420) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113513391787) | [3h31m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166058) | [3h31m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166058) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [17m54s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113513391788) | [3h18m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166273) | [3h18m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166273) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [23m26s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113513391822) | [2h59m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166342) | [2h59m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166342) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [5m50s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113513391651) | [1h36m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166661) | [1h36m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166661) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [12m22s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113513391589) | [1h22m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166351) | [1h22m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166351) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [12m13s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113513391740) | [1h14m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166651) | [1h14m](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166651) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 2 | 0 | — | — | [2m23s](https://github.com/iree-org/iree/actions/runs/37785020465/job/113341166562) | [10m22s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113513391794) | [10m22s](https://github.com/iree-org/iree/actions/runs/37825138362/job/113513391794) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37825138381/job/113507490899) | [1m12s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660728) | [1m12s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660728) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37825138381/job/113507490979) | [1m03s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660952) | [1m03s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660952) | 2 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 2 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/37825138381/job/113507490482) | [44s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660597) | [44s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660597) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37825138381/job/113507490935) | [43s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660658) | [43s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660658) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37825138381/job/113507491130) | [39s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660795) | [39s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660795) | 2 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37825138381/job/113507490438) | [36s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660454) | [36s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660454) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 2 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/37825138381/job/113507490954) | [29s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660736) | [29s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660736) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 2 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/37825138381/job/113507490860) | [27s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660579) | [27s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660579) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 394 | 0% (1/394) |  | 2h55m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 171 | 15% (26/171) |  | 3h01m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 3h18m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 4h24m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h59m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 5h18m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 3h31m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 5h20m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h36m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
