# iree-ci-monitor

_Updated: 2026-06-02 18:31 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [6m07s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617371) | [32m11s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969013) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [29m38s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617752) | [30m32s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969106) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [12m08s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617550) | [29m23s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969068) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [14m11s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617264) | [25m35s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118968894) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [17m26s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617669) | [24m57s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969039) | 0% (0/6) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [10m09s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617472) | [24m02s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118968961) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [19m27s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617655) | [22m51s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969206) | 0% (0/3) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [20m02s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617758) | [20m32s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969126) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [6m07s](https://github.com/iree-org/iree/actions/runs/26846867971/job/79173347862) | [20m15s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969189) | 0% (0/6) | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [5m37s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969077) | [11m05s](https://github.com/iree-org/iree/actions/runs/26846867971/job/79173347789) | 0% (0/3) | `shark01-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 4 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26846867971/job/79173347653) | [8m43s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118968995) | 0% (0/3) | `iree-mi308-1` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26846867971/job/79173347852) | [5m39s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969152) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617753) | [3m10s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969279) | 8% (1/12) | 16 |
| `ubuntu-24.04` | github-hosted | 68 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617527) | [2m21s](https://github.com/iree-org/iree/actions/runs/26832422199/job/79117196069) | 0% (0/54) | 68 |
| `macos-14` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26846867993/job/79168670195) | [2m04s](https://github.com/iree-org/iree/actions/runs/26832422199/job/79117195956) | 0% (0/9) | 9 |
| `azure-linux-scale` | ossci | 20 | 0 | — | — | 0 | [1m42s](https://github.com/iree-org/iree/actions/runs/26832422199/job/79117196099) | [2m00s](https://github.com/iree-org/iree/actions/runs/26846867971/job/79168678028) | 0% (0/19) | 20 |
| `windows-2022` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26832406839/job/79117109726) | [1m30s](https://github.com/iree-org/iree/actions/runs/26832422199/job/79117196039) | 0% (0/9) | 9 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/26832406839/job/79117109701) | [1m24s](https://github.com/iree-org/iree/actions/runs/26832422199/job/79117195718) | 0% (0/9) | 9 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26832403556/job/79117074078) | [1m21s](https://github.com/iree-org/iree/actions/runs/26832416022/job/79117125079) | 0% (0/9) | 9 |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26846867993/job/79168670207) | [2s](https://github.com/iree-org/iree/actions/runs/26832406839/job/79117109897) | 0% (0/3) | 3 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118968849) | [2s](https://github.com/iree-org/iree/actions/runs/26846867971/job/79173347662) | 0% (0/3) | 4 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [6m07s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617371) | [32m11s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969013) | [32m11s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969013) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [29m38s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617752) | [30m32s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969106) | [30m32s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969106) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [28m22s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617420) | [29m23s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969068) | [29m23s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969068) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 4 | 0 | — | — | [14m11s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617264) | [25m35s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118968894) | [25m35s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118968894) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [20m35s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617428) | [24m57s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969039) | [24m57s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969039) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [17m26s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617669) | [24m37s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969121) | [24m37s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969121) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [10m09s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617472) | [24m02s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118968961) | [24m02s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118968961) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [19m27s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617655) | [22m51s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969206) | [22m51s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969206) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [20m02s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617758) | [20m32s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969126) | [20m32s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969126) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [13m16s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617634) | [20m15s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969189) | [20m15s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969189) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [12m08s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617550) | [19m35s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969111) | [19m35s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969111) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [6m07s](https://github.com/iree-org/iree/actions/runs/26846867971/job/79173347862) | [19m20s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969097) | [19m20s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969097) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [5m37s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969077) | [11m05s](https://github.com/iree-org/iree/actions/runs/26846867971/job/79173347789) | [11m05s](https://github.com/iree-org/iree/actions/runs/26846867971/job/79173347789) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 4 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26846867971/job/79173347653) | [8m43s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118968995) | [8m43s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118968995) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [1m56s](https://github.com/iree-org/iree/actions/runs/26846867971/job/79173347905) | [5m39s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969152) | [5m39s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969152) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/26846867971/job/79173347772) | [3m28s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969146) | [3m28s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969146) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 4 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617409) | [3m10s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969279) | [3m10s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969279) | 4 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | 4 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617573) | [2m31s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969004) | [2m31s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969004) | 4 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 4 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26846867971/job/79173347813) | [2m27s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969081) | [2m27s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969081) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26832406839/job/79117109738) | [2m25s](https://github.com/iree-org/iree/actions/runs/26832422199/job/79117196154) | [2m25s](https://github.com/iree-org/iree/actions/runs/26832422199/job/79117196154) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 260 | 5% (12/259) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 287 | 0% (1/287) |  | 4h03m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 195 | 1% (1/195) |  | 4h07m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 65 | 2% (1/65) |  | 4h10m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 207 | 0% (0/207) |  | 4h14m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
