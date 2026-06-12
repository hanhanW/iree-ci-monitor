# iree-ci-monitor

_Updated: 2026-06-12 12:00 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [18m39s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372452) | [21m27s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650498) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [14m40s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650471) | [16m48s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372317) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [3m01s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650450) | [14m58s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372425) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [7m01s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650444) | [11m07s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372278) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [8m19s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650499) | [8m37s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372327) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [6m28s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650478) | [7m45s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372361) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [5m33s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372359) | [7m24s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650455) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650433) | [6m43s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372316) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650442) | [6m43s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372448) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372234) | [3m52s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650320) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372513) | [3m00s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650483) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m33s](https://github.com/iree-org/iree/actions/runs/27410716048/job/81011012870) | [1m33s](https://github.com/iree-org/iree/actions/runs/27410716048/job/81011012870) | 0% (0/1) | 1 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650502) | [10s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372563) | 25% (1/4) | 8 |
| `azure-linux-scale` | ossci | 7 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81049810380) | [9s](https://github.com/iree-org/iree/actions/runs/27422011567/job/81049819692) | 0% (0/2) | 7 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27424249193/job/81057696569) | [5s](https://github.com/iree-org/iree/actions/runs/27413364206/job/81019861455) | — | 15 |
| `ubuntu-24.04` | github-hosted | 38 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372400) | [3s](https://github.com/iree-org/iree/actions/runs/27422011567/job/81049819622) | 7% (1/14) | 38 |
| `macos-14` | github-hosted | 4 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27422011567/job/81049819696) | [3s](https://github.com/iree-org/iree/actions/runs/27422011567/job/81049819723) | 0% (0/1) | 4 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27410695575/job/81010946472) | [3s](https://github.com/iree-org/iree/actions/runs/27410695575/job/81010946472) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27422011567/job/81049819655) | [3s](https://github.com/iree-org/iree/actions/runs/27422011567/job/81049819527) | — | 3 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27422011567/job/81049819583) | [3s](https://github.com/iree-org/iree/actions/runs/27422011567/job/81049819934) | — | 3 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650319) | [2s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372289) | 0% (0/1) | 2 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650475) | [2s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372390) | 0% (0/1) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27422011567/job/81049819656) | [1s](https://github.com/iree-org/iree/actions/runs/27422011567/job/81049819656) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [18m39s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372452) | [21m27s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650498) | [21m27s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650498) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [14m40s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650471) | [16m48s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372317) | [16m48s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372317) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [3m01s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650450) | [14m58s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372425) | [14m58s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372425) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [8m15s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372427) | [11m56s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650536) | [11m56s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650536) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [7m01s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650444) | [11m07s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372278) | [11m07s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372278) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [8m19s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650499) | [8m37s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372327) | [8m37s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372327) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [6m28s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650478) | [7m45s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372361) | [7m45s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372361) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372286) | [7m24s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650455) | [7m24s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650455) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650442) | [6m43s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372448) | [6m43s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372448) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650433) | [6m43s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372316) | [6m43s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372316) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650539) | [6m14s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372566) | [6m14s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372566) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650682) | [5m33s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372359) | [5m33s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372359) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372234) | [3m52s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650320) | [3m52s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650320) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372513) | [3m00s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650483) | [3m00s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650483) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372412) | [2m10s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650507) | [2m10s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650507) | 2 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m33s](https://github.com/iree-org/iree/actions/runs/27410716048/job/81011012870) | [1m33s](https://github.com/iree-org/iree/actions/runs/27410716048/job/81011012870) | [1m33s](https://github.com/iree-org/iree/actions/runs/27410716048/job/81011012870) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27413619025/job/81020723818) | [15s](https://github.com/iree-org/iree/actions/runs/27413364206/job/81019861449) | [15s](https://github.com/iree-org/iree/actions/runs/27413364206/job/81019861449) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650393) | [10s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372282) | [10s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372282) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650462) | [10s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372336) | [10s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372336) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27405026781/job/80996650502) | [10s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372563) | [10s](https://github.com/iree-org/iree/actions/runs/27422011428/job/81051372563) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 376 | 2% (8/376) |  | 4h04m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 316 | 7% (21/316) |  | 4h05m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 271 | 2% (5/271) |  | 4h11m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 278 | 2% (5/278) |  | 4h12m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 89 | 1% (1/89) |  | 4h14m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
