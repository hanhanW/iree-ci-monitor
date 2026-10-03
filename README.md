# iree-ci-monitor

_Updated: 2026-10-02 22:23 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [23m52s](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257464) | [35m49s](https://github.com/iree-org/iree/actions/runs/37072908779/job/111058407507) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [19m09s](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257558) | [31m21s](https://github.com/iree-org/iree/actions/runs/37072908779/job/111058407629) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [2m20s](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943288) | [15m12s](https://github.com/iree-org/iree/actions/runs/37072908779/job/111058407435) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [9m36s](https://github.com/iree-org/iree/actions/runs/37072908779/job/111058407365) | [13m54s](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257366) | 0% (0/1) | `shark75-ci` |
| `azure-linux-scale` | ossci | 28 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/37072757101/job/111055834690) | [24s](https://github.com/iree-org/iree/actions/runs/37081552804/job/111083016493) | 0% (0/7) | 28 |
| `macos-14` | github-hosted | 14 | 0 | — | — | 1 | [7s](https://github.com/iree-org/iree/actions/runs/37081552804/job/111083016238) | [8s](https://github.com/iree-org/iree/actions/runs/37081552804/job/111083016219) | 0% (0/3) | 14 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 3 | [5s](https://github.com/iree-org/iree/actions/runs/37067818476/job/111039958097) | [5s](https://github.com/iree-org/iree/actions/runs/37099241046/job/111135374844) | 0% (0/3) | 15 |
| `windows-2022` | github-hosted | 14 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/37072908788/job/111056756595) | [4s](https://github.com/iree-org/iree/actions/runs/37067818476/job/111039958197) | 0% (0/3) | 14 |
| `ubuntu-24.04` | github-hosted | 75 | 0 | — | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/37081552804/job/111083016077) | [3s](https://github.com/iree-org/iree/actions/runs/37081552804/job/111083016231) | 5% (1/20) | 75 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/37067817809/job/111039889133) | [3s](https://github.com/iree-org/iree/actions/runs/37067817809/job/111039889170) | 0% (0/3) | 3 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37072757101/job/111055834822) | [2s](https://github.com/iree-org/iree/actions/runs/37081552804/job/111083016454) | 0% (0/1) | 4 |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 6 | 5 | [19h42m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654361) | 2026-10-02 22:23 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 5 | [19h42m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654330) | 2026-10-02 22:23 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 12 | 10 | [19h42m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654291) | 2026-10-02 22:23 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 12 | 10 | [19h42m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654182) | 2026-10-02 22:23 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [19h42m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654182) | 2026-10-02 22:23 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/ziereis/update-torch-mlir` | pull_request |
| [19h42m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654291) | 2026-10-02 22:23 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/ziereis/update-torch-mlir` | pull_request |
| [19h42m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654324) | 2026-10-02 22:23 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/ziereis/update-torch-mlir` | pull_request |
| [19h42m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654330) | 2026-10-02 22:23 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/ziereis/update-torch-mlir` | pull_request |
| [19h42m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654361) | 2026-10-02 22:23 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/ziereis/update-torch-mlir` | pull_request |
| [19h42m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654367) | 2026-10-02 22:23 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `users/ziereis/update-torch-mlir` | pull_request |
| [13h04m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458801) | 2026-10-02 22:23 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `main` | push |
| [13h04m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458926) | 2026-10-02 22:23 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [13h04m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458928) | 2026-10-02 22:23 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |
| [13h04m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458937) | 2026-10-02 22:23 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [13h04m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458964) | 2026-10-02 22:23 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [13h04m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458980) | 2026-10-02 22:23 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [13h01m](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832171) | 2026-10-02 22:23 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [13h01m](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832239) | 2026-10-02 22:23 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [13h01m](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832282) | 2026-10-02 22:23 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 5 | [19h42m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654182) | 2026-10-02 22:23 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 5 | [19h42m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654330) | 2026-10-02 22:23 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 6 | 5 | [19h42m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654361) | 2026-10-02 22:23 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 5 | [19h42m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654324) | 2026-10-02 22:23 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 5 | [19h42m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654367) | 2026-10-02 22:23 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 5 | [19h42m](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654291) | 2026-10-02 22:23 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [23m52s](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257464) | [35m49s](https://github.com/iree-org/iree/actions/runs/37072908779/job/111058407507) | [35m49s](https://github.com/iree-org/iree/actions/runs/37072908779/job/111058407507) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [19m09s](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257558) | [31m21s](https://github.com/iree-org/iree/actions/runs/37072908779/job/111058407629) | [31m21s](https://github.com/iree-org/iree/actions/runs/37072908779/job/111058407629) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [20m13s](https://github.com/iree-org/iree/actions/runs/37072908779/job/111058407491) | [30m40s](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257466) | [30m40s](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257466) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [10m39s](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943490) | [15m12s](https://github.com/iree-org/iree/actions/runs/37072908779/job/111058407435) | [15m12s](https://github.com/iree-org/iree/actions/runs/37072908779/job/111058407435) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [9m36s](https://github.com/iree-org/iree/actions/runs/37072908779/job/111058407365) | [13m54s](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257366) | [13m54s](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257366) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [2m20s](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943288) | [5m04s](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257475) | [5m04s](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257475) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37072757106/job/111055868416) | [1m15s](https://github.com/iree-org/iree/actions/runs/37081552964/job/111083046885) | [1m15s](https://github.com/iree-org/iree/actions/runs/37081552964/job/111083046885) | 4 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943316) | [38s](https://github.com/iree-org/iree/actions/runs/37072908779/job/111058407495) | [38s](https://github.com/iree-org/iree/actions/runs/37072908779/job/111058407495) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37072908788/job/111056756966) | [24s](https://github.com/iree-org/iree/actions/runs/37081552804/job/111083016493) | [24s](https://github.com/iree-org/iree/actions/runs/37081552804/job/111083016493) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 4 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/37067818476/job/111039958256) | [10s](https://github.com/iree-org/iree/actions/runs/37072757101/job/111055834588) | [10s](https://github.com/iree-org/iree/actions/runs/37072757101/job/111055834588) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37081552804/job/111083016530) | [10s](https://github.com/iree-org/iree/actions/runs/37067818476/job/111039958318) | [10s](https://github.com/iree-org/iree/actions/runs/37067818476/job/111039958318) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37072757101/job/111055834918) | [10s](https://github.com/iree-org/iree/actions/runs/37067818476/job/111039958615) | [10s](https://github.com/iree-org/iree/actions/runs/37067818476/job/111039958615) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang / rocjitsu_e2e | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37081552804/job/111083016261) | [10s](https://github.com/iree-org/iree/actions/runs/37072757101/job/111055834545) | [10s](https://github.com/iree-org/iree/actions/runs/37072757101/job/111055834545) | 3 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37072757101/job/111055834690) | [9s](https://github.com/iree-org/iree/actions/runs/37072908788/job/111056756955) | [9s](https://github.com/iree-org/iree/actions/runs/37072908788/job/111056756955) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 274 | 1% (4/274) |  | 4h31m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 206 | 1% (2/206) |  | 2d08h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 19h42m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 19h42m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 19h42m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 19h42m (> 2h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
