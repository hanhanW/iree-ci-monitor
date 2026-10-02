# iree-ci-monitor

_Updated: 2026-10-02 15:18 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [15m33s](https://github.com/iree-org/iree/actions/runs/37048445138/job/110978403620) | [2h06m](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832398) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [13m22s](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832207) | [1h31m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458868) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [23m22s](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458607) | [1h11m](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832084) | 50% (1/2) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 1 | [27m38s](https://github.com/iree-org/iree/actions/runs/37048445138/job/110978403357) | [1h08m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924459064) | 0% (0/3) | `shark75-ci` |
| `azure-linux-scale` | ossci | 32 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/37067818476/job/111039958615) | [6m10s](https://github.com/iree-org/iree/actions/runs/37031857283/job/110920525734) | 0% (0/14) | 32 |
| `macos-14` | github-hosted | 15 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/37042330699/job/110955301960) | [2m34s](https://github.com/iree-org/iree/actions/runs/37031857283/job/110920525666) | 0% (0/6) | 15 |
| `ubuntu-24.04` | github-hosted | 129 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257508) | [2m16s](https://github.com/iree-org/iree/actions/runs/37031857283/job/110920525597) | 5% (2/38) | 122 |
| `windows-2022` | github-hosted | 15 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/37067818476/job/111039958197) | [57s](https://github.com/iree-org/iree/actions/runs/37031842404/job/110920408923) | 0% (0/6) | 15 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/37067818476/job/111039958097) | [43s](https://github.com/iree-org/iree/actions/runs/37031842404/job/110920408642) | 0% (0/6) | 15 |
| `azure-windows-scale` | ossci | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37042330699/job/110955302316) | [27s](https://github.com/iree-org/iree/actions/runs/37031857283/job/110920526195) | 0% (0/2) | 5 |
| `ubuntu-latest` | github-hosted | 21 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37034032383/job/110927677263) | [3s](https://github.com/iree-org/iree/actions/runs/37067817809/job/111039889170) | 0% (0/6) | 21 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 7 | 5 | [12h36m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654330) | 2026-10-02 15:17 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 14 | 10 | [12h36m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654182) | 2026-10-02 15:17 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 14 | 10 | [12h36m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654291) | 2026-10-02 15:17 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 7 | 5 | [12h36m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654361) | 2026-10-02 15:17 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [12h36m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654182) | 2026-10-02 15:17 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/ziereis/update-torch-mlir` | pull_request |
| [12h36m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654291) | 2026-10-02 15:17 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/ziereis/update-torch-mlir` | pull_request |
| [12h36m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654324) | 2026-10-02 15:17 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/ziereis/update-torch-mlir` | pull_request |
| [12h36m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654330) | 2026-10-02 15:17 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/ziereis/update-torch-mlir` | pull_request |
| [12h36m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654361) | 2026-10-02 15:17 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/ziereis/update-torch-mlir` | pull_request |
| [12h36m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654367) | 2026-10-02 15:17 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `users/ziereis/update-torch-mlir` | pull_request |
| [5h58m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458801) | 2026-10-02 15:17 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `main` | push |
| [5h58m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458926) | 2026-10-02 15:17 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [5h58m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458928) | 2026-10-02 15:17 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |
| [5h58m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458937) | 2026-10-02 15:17 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [5h58m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458964) | 2026-10-02 15:17 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [5h58m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458980) | 2026-10-02 15:17 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [5h55m](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832171) | 2026-10-02 15:17 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [5h55m](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832239) | 2026-10-02 15:17 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [5h55m](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832282) | 2026-10-02 15:17 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 7 | 5 | [12h36m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654182) | 2026-10-02 15:17 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 7 | 5 | [12h36m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654330) | 2026-10-02 15:17 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 7 | 5 | [12h36m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654361) | 2026-10-02 15:17 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 7 | 5 | [12h36m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654324) | 2026-10-02 15:17 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 7 | 5 | [12h36m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654367) | 2026-10-02 15:17 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 7 | 5 | [12h36m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654291) | 2026-10-02 15:17 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [22m22s](https://github.com/iree-org/iree/actions/runs/37005242492/job/110834611957) | [2h06m](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832398) | [2h06m](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832398) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [15m33s](https://github.com/iree-org/iree/actions/runs/37048445138/job/110978403620) | [2h01m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458727) | [2h01m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458727) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [13m22s](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832207) | [1h31m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458868) | [1h31m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458868) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [23m22s](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458607) | [1h11m](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832084) | [1h11m](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832084) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [30m40s](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257466) | [1h08m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924459064) | [1h08m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924459064) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [19m09s](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257558) | [28m20s](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832457) | [28m20s](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832457) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 5 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37067818476/job/111039958498) | [6m11s](https://github.com/iree-org/iree/actions/runs/37031857283/job/110920526228) | [6m11s](https://github.com/iree-org/iree/actions/runs/37031857283/job/110920526228) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 5 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/37048444896/job/110976038301) | [6m11s](https://github.com/iree-org/iree/actions/runs/37031857283/job/110920526255) | [6m11s](https://github.com/iree-org/iree/actions/runs/37031857283/job/110920526255) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 5 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/37067818476/job/111039958256) | [6m10s](https://github.com/iree-org/iree/actions/runs/37031857283/job/110920525734) | [6m10s](https://github.com/iree-org/iree/actions/runs/37031857283/job/110920525734) | 5 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 5 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37042330714/job/110955316848) | [4m42s](https://github.com/iree-org/iree/actions/runs/37031857001/job/110920820047) | [4m42s](https://github.com/iree-org/iree/actions/runs/37031857001/job/110920820047) | 5 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 5 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37042330699/job/110955301973) | [3m13s](https://github.com/iree-org/iree/actions/runs/37031842404/job/110920408674) | [3m13s](https://github.com/iree-org/iree/actions/runs/37031842404/job/110920408674) | 5 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 5 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/37048444896/job/110976038162) | [2m54s](https://github.com/iree-org/iree/actions/runs/37031857283/job/110920525725) | [2m54s](https://github.com/iree-org/iree/actions/runs/37031857283/job/110920525725) | 5 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 7 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37067818476/job/111039958101) | [2m41s](https://github.com/iree-org/iree/actions/runs/37031842404/job/110920408440) | [2m41s](https://github.com/iree-org/iree/actions/runs/37031842404/job/110920408440) | 5 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 5 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37048444896/job/110976037981) | [2m36s](https://github.com/iree-org/iree/actions/runs/37031842404/job/110920408658) | [2m36s](https://github.com/iree-org/iree/actions/runs/37031842404/job/110920408658) | 5 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 276 | 2% (5/275) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 228 | 1% (2/228) |  | 2d01h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 12h36m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 12h36m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 12h36m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 12h36m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h31m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h08m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h11m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h06m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
