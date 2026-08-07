# iree-ci-monitor

_Updated: 2026-08-07 06:41 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31176927766/job/92862625286) | [24m53s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622300) | — | `shark01-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [22m16s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622247) | [22m16s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622247) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [16m15s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622324) | [22m16s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622297) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [6m35s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622150) | [17m41s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622248) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [5m50s](https://github.com/iree-org/iree/actions/runs/31176927766/job/92862625365) | [17m13s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622134) | — | `shark01-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622103) | [12m24s](https://github.com/iree-org/iree/actions/runs/31176927766/job/92862625372) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [9m54s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622203) | [11m59s](https://github.com/iree-org/iree/actions/runs/31176927766/job/92862625327) | — | `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [8m29s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622253) | [8m29s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622253) | — | `shark01-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622132) | [6m30s](https://github.com/iree-org/iree/actions/runs/31176927766/job/92862625279) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [4m59s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622316) | [5m43s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622137) | — | `shark10-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 24 | 0 | — | — | 6 | [8s](https://github.com/iree-org/iree/actions/runs/31178720584/job/92867099757) | [2m47s](https://github.com/iree-org/iree/actions/runs/31180795090/job/92873380303) | 0% (0/2) | 24 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m23s](https://github.com/iree-org/iree/actions/runs/31166488477/job/92828382266) | [1m23s](https://github.com/iree-org/iree/actions/runs/31166488477/job/92828382266) | 0% (0/1) | 1 |
| `ubuntu-24.04` | github-hosted | 75 | 0 | — | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/31180795090/job/92873379997) | [9s](https://github.com/iree-org/iree/actions/runs/31176929305/job/92860922776) | 0% (0/5) | 73 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31183205482/job/92881944146) | [6s](https://github.com/iree-org/iree/actions/runs/31176929305/job/92860922877) | — | 15 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31180790423/job/92873315213) | [6s](https://github.com/iree-org/iree/actions/runs/31174499576/job/92853440018) | — | 15 |
| `macos-14` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31183205482/job/92881943955) | [4s](https://github.com/iree-org/iree/actions/runs/31180795090/job/92873380319) | 0% (0/1) | 15 |
| `windows-2022` | github-hosted | 14 | 0 | — | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/31180795090/job/92873380000) | [3s](https://github.com/iree-org/iree/actions/runs/31178720584/job/92867099716) | — | 14 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/31166457150/job/92828289146) | [3s](https://github.com/iree-org/iree/actions/runs/31166457150/job/92828289146) | — | 1 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/31180795090/job/92873380329) | [2s](https://github.com/iree-org/iree/actions/runs/31183205482/job/92881944338) | — | 4 |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868621984) | [2s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868621984) | — | `shark75-ci` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31176927766/job/92862625286) | [24m53s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622300) | [24m53s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622300) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [22m16s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622247) | [22m16s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622247) | [22m16s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622247) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [11m02s](https://github.com/iree-org/iree/actions/runs/31176927766/job/92862625339) | [22m16s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622297) | [22m16s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622297) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [17m41s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622248) | [17m41s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622248) | [17m41s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622248) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [5m50s](https://github.com/iree-org/iree/actions/runs/31176927766/job/92862625365) | [17m13s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622134) | [17m13s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622134) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [13m47s](https://github.com/iree-org/iree/actions/runs/31176927766/job/92862625399) | [16m15s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622324) | [16m15s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622324) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622103) | [12m24s](https://github.com/iree-org/iree/actions/runs/31176927766/job/92862625372) | [12m24s](https://github.com/iree-org/iree/actions/runs/31176927766/job/92862625372) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [9m54s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622203) | [11m59s](https://github.com/iree-org/iree/actions/runs/31176927766/job/92862625327) | [11m59s](https://github.com/iree-org/iree/actions/runs/31176927766/job/92862625327) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [8m29s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622253) | [8m29s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622253) | [8m29s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622253) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31176927766/job/92862625337) | [6m35s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622150) | [6m35s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622150) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622132) | [6m30s](https://github.com/iree-org/iree/actions/runs/31176927766/job/92862625279) | [6m30s](https://github.com/iree-org/iree/actions/runs/31176927766/job/92862625279) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31176927766/job/92862625258) | [5m43s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622137) | [5m43s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622137) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [4m59s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622316) | [4m59s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622316) | [4m59s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622316) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 4 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/31183205110/job/92881438197) | [3m00s](https://github.com/iree-org/iree/actions/runs/31180795081/job/92873391235) | [3m00s](https://github.com/iree-org/iree/actions/runs/31180795081/job/92873391235) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 4 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/31178720584/job/92867099720) | [2m47s](https://github.com/iree-org/iree/actions/runs/31180795090/job/92873380303) | [2m47s](https://github.com/iree-org/iree/actions/runs/31180795090/job/92873380303) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 2 | 0 | — | — | [25s](https://github.com/iree-org/iree/actions/runs/31183205482/job/92881944093) | [1m56s](https://github.com/iree-org/iree/actions/runs/31180795090/job/92873380408) | [1m56s](https://github.com/iree-org/iree/actions/runs/31180795090/job/92873380408) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 4 | 0 | — | — | [25s](https://github.com/iree-org/iree/actions/runs/31183205482/job/92881944063) | [1m44s](https://github.com/iree-org/iree/actions/runs/31180795090/job/92873380406) | [1m44s](https://github.com/iree-org/iree/actions/runs/31180795090/job/92873380406) | 4 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m23s](https://github.com/iree-org/iree/actions/runs/31166488477/job/92828382266) | [1m23s](https://github.com/iree-org/iree/actions/runs/31166488477/job/92828382266) | [1m23s](https://github.com/iree-org/iree/actions/runs/31166488477/job/92828382266) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 4 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/31183205482/job/92881944074) | [54s](https://github.com/iree-org/iree/actions/runs/31180795090/job/92873380239) | [54s](https://github.com/iree-org/iree/actions/runs/31180795090/job/92873380239) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 4 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/31176929305/job/92860922877) | [48s](https://github.com/iree-org/iree/actions/runs/31180795090/job/92873380295) | [48s](https://github.com/iree-org/iree/actions/runs/31180795090/job/92873380295) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 118 | 3% (4/118) |  | 18m32s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 109 | 1% (1/109) |  | 20m27s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 135 | 0% (0/135) |  | 25m53s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 107 | 0% (0/107) |  | 26m56s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 13 | 0% (0/13) |  | 4d00h ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
