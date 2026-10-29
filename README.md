# iree-ci-monitor

_Updated: 2026-10-28 22:54 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [23m01s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156502) | [23m01s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156502) | — | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [8m48s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156481) | [15m35s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156495) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [11m27s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156444) | [11m27s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156444) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [1m49s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156572) | [11m22s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156644) | — | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156459) | [4m57s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156441) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156442) | [3m14s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156433) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2m37s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156421) | [2m37s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156421) | — | `shark55-ci` |
| `azure-linux-scale` | ossci | 7 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891693) | [10s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891807) | — | 7 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/40821995373/job/123276415642) | [5s](https://github.com/iree-org/iree/actions/runs/40821995373/job/123276415612) | — | 6 |
| `macos-15` | github-hosted | 5 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/40821995373/job/123276415614) | [4s](https://github.com/iree-org/iree/actions/runs/40821995373/job/123276415793) | — | 5 |
| `ubuntu-24.04` | github-hosted | 43 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123282985760) | [3s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891638) | 0% (0/5) | 42 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891718) | [3s](https://github.com/iree-org/iree/actions/runs/40821995373/job/123276415596) | — | 5 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891764) | [1s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891764) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [23m01s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156502) | [23m01s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156502) | [23m01s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156502) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [15m35s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156495) | [15m35s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156495) | [15m35s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156495) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [11m27s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156444) | [11m27s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156444) | [11m27s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156444) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [11m22s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156644) | [11m22s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156644) | [11m22s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156644) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [8m48s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156481) | [8m48s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156481) | [8m48s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156481) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [4m57s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156441) | [4m57s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156441) | [4m57s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156441) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [3m14s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156433) | [3m14s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156433) | [3m14s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156433) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [2m37s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156421) | [2m37s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156421) | [2m37s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156421) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [1m49s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156572) | [1m49s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156572) | [1m49s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123275156572) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891807) | [10s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891807) | [10s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891807) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123267894141) | [9s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123267894141) | [9s](https://github.com/iree-org/iree/actions/runs/40819331440/job/123267894141) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891693) | [9s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891693) | [9s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891693) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891712) | [9s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891712) | [9s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891712) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891705) | [9s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891705) | [9s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891705) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/40821995373/job/123276415612) | [5s](https://github.com/iree-org/iree/actions/runs/40821995373/job/123276415612) | [5s](https://github.com/iree-org/iree/actions/runs/40821995373/job/123276415612) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891637) | [5s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891637) | [5s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891637) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/40821995373/job/123276415720) | [4s](https://github.com/iree-org/iree/actions/runs/40821995373/job/123276415720) | [4s](https://github.com/iree-org/iree/actions/runs/40821995373/job/123276415720) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/40821995373/job/123276415642) | [4s](https://github.com/iree-org/iree/actions/runs/40821995373/job/123276415642) | [4s](https://github.com/iree-org/iree/actions/runs/40821995373/job/123276415642) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/40821995373/job/123276415793) | [4s](https://github.com/iree-org/iree/actions/runs/40821995373/job/123276415793) | [4s](https://github.com/iree-org/iree/actions/runs/40821995373/job/123276415793) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891577) | [4s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891577) | [4s](https://github.com/iree-org/iree/actions/runs/40819331461/job/123267891577) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 196 | 3% (5/196) |  | 20m30s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 234 | 2% (4/234) |  | 29m25s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
