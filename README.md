# iree-ci-monitor

_Updated: 2026-10-03 04:44 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [28m12s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173007) | [37m33s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173121) | — | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [6m58s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173218) | [17m24s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173197) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [11m59s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173128) | [11m59s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173128) | — | `shark75-ci` |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090097) | [1m10s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090053) | — | 6 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37118820192/job/111190745605) | [37s](https://github.com/iree-org/iree/actions/runs/37118820192/job/111190745789) | — | 3 |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 0 | [11s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090235) | [12s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090106) | — | 6 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090090) | [8s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090141) | — | 5 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090096) | [3s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090120) | — | 5 |
| `ubuntu-24.04` | github-hosted | 31 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111148940685) | [2s](https://github.com/iree-org/iree/actions/runs/37118726945/job/111190628501) | 0% (0/2) | 31 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173039) | [1s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173039) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 5 | 5 | [19h25m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458801) | 2026-10-03 04:44 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 10 | 10 | [19h25m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458964) | 2026-10-03 04:44 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 5 | 5 | [19h25m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458928) | 2026-10-03 04:44 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 10 | 10 | [19h25m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458926) | 2026-10-03 04:44 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [0s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090155) | [0s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090155) | — | 1 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [19h25m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458801) | 2026-10-03 04:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `main` | push |
| [19h25m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458926) | 2026-10-03 04:44 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [19h25m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458928) | 2026-10-03 04:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |
| [19h25m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458937) | 2026-10-03 04:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [19h25m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458964) | 2026-10-03 04:44 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [19h25m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458980) | 2026-10-03 04:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [19h21m](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832171) | 2026-10-03 04:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [19h21m](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832239) | 2026-10-03 04:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [19h21m](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832282) | 2026-10-03 04:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [19h21m](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832315) | 2026-10-03 04:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [19h21m](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832370) | 2026-10-03 04:44 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [19h21m](https://github.com/iree-org/iree/actions/runs/37031857001/job/110925832789) | 2026-10-03 04:44 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [14h00m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257364) | 2026-10-03 04:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `main` | push |
| [14h00m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257394) | 2026-10-03 04:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |
| [14h00m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257428) | 2026-10-03 04:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 5 | 5 | [19h25m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458928) | 2026-10-03 04:44 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 5 | 5 | [19h25m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458801) | 2026-10-03 04:44 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 5 | 5 | [19h25m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458980) | 2026-10-03 04:44 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 5 | 5 | [19h25m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458937) | 2026-10-03 04:44 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 5 | 5 | [19h25m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458964) | 2026-10-03 04:44 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 5 | 5 | [19h25m](https://github.com/iree-org/iree/actions/runs/37031842464/job/110924458926) | 2026-10-03 04:44 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [37m33s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173121) | [37m33s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173121) | [37m33s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173121) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [28m12s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173007) | [28m12s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173007) | [28m12s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173007) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [17m24s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173197) | [17m24s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173197) | [17m24s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173197) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [11m59s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173128) | [11m59s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173128) | [11m59s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173128) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [6m58s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173218) | [6m58s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173218) | [6m58s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173218) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1m10s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090053) | [1m10s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090053) | [1m10s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090053) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [37s](https://github.com/iree-org/iree/actions/runs/37118820192/job/111190745789) | [37s](https://github.com/iree-org/iree/actions/runs/37118820192/job/111190745789) | [37s](https://github.com/iree-org/iree/actions/runs/37118820192/job/111190745789) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090106) | [12s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090106) | [12s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090106) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 1 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090240) | [11s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090240) | [11s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090240) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090235) | [11s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090235) | [11s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090235) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111143094274) | [11s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111143094274) | [11s](https://github.com/iree-org/iree/actions/runs/37101946689/job/111143094274) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090210) | [10s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090210) | [10s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090210) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090141) | [8s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090141) | [8s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111143090141) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/37099241046/job/111135372744) | [7s](https://github.com/iree-org/iree/actions/runs/37099241046/job/111135372744) | [7s](https://github.com/iree-org/iree/actions/runs/37099241046/job/111135372744) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 280 | 1% (4/280) |  | 4h47m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 206 | 1% (2/206) |  | 2d15h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 19h25m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 19h25m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 19h25m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 19h25m (> 2h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
