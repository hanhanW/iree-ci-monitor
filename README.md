# iree-ci-monitor

_Updated: 2026-06-22 18:17 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [24m57s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813160971) | [30m50s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228590) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [13m23s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161143) | [25m23s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228712) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [16m49s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161081) | [19m54s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228643) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [10m10s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222903) | [19m45s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228636) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [10m55s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228614) | [15m10s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813160958) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [9m03s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222561) | [13m31s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161084) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [6m23s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161087) | [13m09s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228665) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [3m34s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161035) | [9m40s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161171) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [1m37s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222932) | [5m39s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228675) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228642) | [5m32s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161076) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `azure-linux-scale` | ossci | 18 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/27964465756/job/82754527906) | [3m21s](https://github.com/iree-org/iree/actions/runs/27981245562/job/82811620402) | 0% (0/6) | 18 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161159) | [1m52s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222804) | 0% (0/2) | `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m29s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716180) | [1m29s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716180) | — | 1 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 12 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161115) | [38s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228720) | 0% (0/4) | 12 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828715933) | [7s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716216) | 0% (0/3) | 9 |
| `macos-14` | github-hosted | 10 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/27981245562/job/82811620312) | [5s](https://github.com/iree-org/iree/actions/runs/27964465756/job/82754527860) | 0% (0/3) | 10 |
| `windows-2022` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27964465756/job/82754527662) | [5s](https://github.com/iree-org/iree/actions/runs/27964465756/job/82754527720) | 0% (0/3) | 9 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [5s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716200) | [5s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716200) | — | 1 |
| `ubuntu-latest` | github-hosted | 17 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27981546370/job/82812667080) | [4s](https://github.com/iree-org/iree/actions/runs/27981546370/job/82812667070) | 0% (0/5) | 17 |
| `ubuntu-24.04` | github-hosted | 63 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161215) | [3s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161062) | 0% (0/20) | 63 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161193) | [2s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228687) | 0% (0/1) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27981245562/job/82811620698) | [2s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716198) | 0% (0/1) | 3 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 5 | 5 | [15h51m](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202183) | 2026-06-22 18:16 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [15h51m](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202183) | 2026-06-22 18:16 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [10h05m](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317105) | 2026-06-22 18:16 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `add-gpu-ada-known-target` | pull_request |
| [9h34m](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756223051) | 2026-06-22 18:16 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `devtbi/tduf` | pull_request |
| [4h51m](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161046) | 2026-06-22 18:16 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [3h18m](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228625) | 2026-06-22 18:16 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `dependabot/github_actions/github-actions-ad4787fcfd` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 5 | 5 | [15h51m](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202183) | 2026-06-22 18:16 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [24m57s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813160971) | [30m50s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228590) | [30m50s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228590) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [13m23s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161143) | [25m23s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228712) | [25m23s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228712) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [16m49s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161081) | [19m54s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228643) | [19m54s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228643) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [10m10s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222903) | [19m45s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228636) | [19m45s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228636) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [13m43s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756223023) | [17m34s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161128) | [17m34s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161128) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [10m55s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228614) | [15m10s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813160958) | [15m10s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813160958) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [9m03s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222561) | [13m31s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161084) | [13m31s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161084) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [6m23s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161087) | [13m09s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228665) | [13m09s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228665) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [6m41s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228724) | [9m40s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161171) | [9m40s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161171) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [2m25s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222969) | [5m39s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228675) | [5m39s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228675) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228642) | [5m32s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161076) | [5m32s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161076) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [3m34s](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161035) | [4m16s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228695) | [4m16s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228695) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [1m37s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222932) | [3m28s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228709) | [3m28s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228709) | 3 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 3 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828715895) | [3m21s](https://github.com/iree-org/iree/actions/runs/27981245562/job/82811620402) | [3m21s](https://github.com/iree-org/iree/actions/runs/27981245562/job/82811620402) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716432) | [3m21s](https://github.com/iree-org/iree/actions/runs/27981245562/job/82811620799) | [3m21s](https://github.com/iree-org/iree/actions/runs/27981245562/job/82811620799) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716245) | [3m20s](https://github.com/iree-org/iree/actions/runs/27981245562/job/82811620678) | [3m20s](https://github.com/iree-org/iree/actions/runs/27981245562/job/82811620678) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716165) | [3m17s](https://github.com/iree-org/iree/actions/runs/27981245562/job/82811620546) | [3m17s](https://github.com/iree-org/iree/actions/runs/27981245562/job/82811620546) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 3 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716077) | [3m15s](https://github.com/iree-org/iree/actions/runs/27981245562/job/82811620354) | [3m15s](https://github.com/iree-org/iree/actions/runs/27981245562/job/82811620354) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228678) | [1m52s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222804) | [1m52s](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756222804) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 150 | 0% (0/150) |  | 2h40m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 116 | 4% (5/116) |  | 2h53m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 100 | 0% (0/100) |  | 2h59m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 118 | 0% (0/118) |  | 3h01m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 33 | 0% (0/33) |  | 3h08m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 15h51m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
