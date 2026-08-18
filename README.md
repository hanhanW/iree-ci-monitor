# iree-ci-monitor

_Updated: 2026-08-18 06:11 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 10 | 0 | — | — | 0 | [20m40s](https://github.com/iree-org/iree/actions/runs/32110120286/job/95629274313) | [47m22s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622906) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [20m15s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686213895) | [45m29s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896506) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 5 | 0 | — | — | 0 | [27m35s](https://github.com/iree-org/iree/actions/runs/32110120286/job/95629274262) | [39m03s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016500) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 10 | 0 | — | — | 0 | [18m23s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686213858) | [29m11s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896566) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 10 | 0 | — | — | 0 | [16m02s](https://github.com/iree-org/iree/actions/runs/32110120286/job/95629274500) | [28m24s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896454) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 5 | 0 | — | — | 0 | [15m13s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686213747) | [26m27s](https://github.com/iree-org/iree/actions/runs/32110120286/job/95629274128) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 5 | 0 | — | — | 0 | [9m14s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016517) | [25m50s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686213812) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 5 | 0 | — | — | 0 | [4m49s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622844) | [20m02s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016643) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [8m10s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686214058) | [19m33s](https://github.com/iree-org/iree/actions/runs/32110120286/job/95629274452) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 10 | 0 | — | — | 0 | [8m14s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622884) | [18m24s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686214090) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [7m11s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016606) | [11m53s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622664) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m51s](https://github.com/iree-org/iree/actions/runs/32123441543/job/95668703018) | [1m51s](https://github.com/iree-org/iree/actions/runs/32123441543/job/95668703018) | 0% (0/1) | 1 |
| `ubuntu-24.04` | github-hosted | 166 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/32139981962/job/95720828831) | [1m38s](https://github.com/iree-org/iree/actions/runs/32120940648/job/95661025192) | 5% (2/41) | 163 |
| `azure-linux-scale` | ossci | 59 | 0 | — | — | 6 | [8s](https://github.com/iree-org/iree/actions/runs/32139486444/job/95718841068) | [1m32s](https://github.com/iree-org/iree/actions/runs/32120940648/job/95661025715) | 7% (1/14) | 59 |
| `ubuntu-24.04-arm` | github-hosted | 33 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/32128405972/job/95684023018) | [1m29s](https://github.com/iree-org/iree/actions/runs/32120940648/job/95661025061) | 0% (0/6) | 33 |
| `windows-2022` | github-hosted | 32 | 0 | — | — | 3 | [3s](https://github.com/iree-org/iree/actions/runs/32110120271/job/95627567649) | [1m14s](https://github.com/iree-org/iree/actions/runs/32120940648/job/95661025221) | 0% (0/6) | 32 |
| `macos-14` | github-hosted | 33 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/32128405972/job/95684023038) | [1m06s](https://github.com/iree-org/iree/actions/runs/32128405972/job/95684023127) | 0% (0/6) | 33 |
| `azure-windows-scale` | ossci | 10 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/32120938154/job/95661019689) | [6s](https://github.com/iree-org/iree/actions/runs/32120940648/job/95661025772) | 0% (0/2) | 10 |
| `ubuntu-latest` | github-hosted | 30 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32139093430/job/95717231220) | [4s](https://github.com/iree-org/iree/actions/runs/32125902432/job/95676275085) | 0% (0/6) | 30 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [33m59s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896667) | [47m22s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622906) | [47m22s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622906) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 5 | 0 | — | — | [20m15s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686213895) | [45m29s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896506) | [45m29s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896506) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 5 | 0 | — | — | [27m35s](https://github.com/iree-org/iree/actions/runs/32110120286/job/95629274262) | [39m03s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016500) | [39m03s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016500) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 5 | 0 | — | — | [22m18s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686214076) | [29m11s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896566) | [29m11s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896566) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [17m56s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622680) | [28m24s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896454) | [28m24s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896454) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 5 | 0 | — | — | [15m13s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686213747) | [26m27s](https://github.com/iree-org/iree/actions/runs/32110120286/job/95629274128) | [26m27s](https://github.com/iree-org/iree/actions/runs/32110120286/job/95629274128) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 5 | 0 | — | — | [9m14s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016517) | [25m50s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686213812) | [25m50s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686213812) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [5m51s](https://github.com/iree-org/iree/actions/runs/32110120286/job/95629274413) | [25m15s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016628) | [25m15s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016628) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [15m12s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896604) | [24m08s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016695) | [24m08s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016695) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 5 | 0 | — | — | [4m49s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622844) | [20m02s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016643) | [20m02s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016643) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 5 | 0 | — | — | [8m10s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686214058) | [19m33s](https://github.com/iree-org/iree/actions/runs/32110120286/job/95629274452) | [19m33s](https://github.com/iree-org/iree/actions/runs/32110120286/job/95629274452) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 5 | 0 | — | — | [7m52s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016756) | [19m01s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896487) | [19m01s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896487) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [4m51s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016811) | [18m24s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686214090) | [18m24s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686214090) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [8m44s](https://github.com/iree-org/iree/actions/runs/32110120286/job/95629274396) | [13m38s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686213957) | [13m38s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686213957) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 5 | 0 | — | — | [7m11s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016606) | [11m53s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622664) | [11m53s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622664) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 5 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622715) | [4m00s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016746) | [4m00s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016746) | 5 |
| `.github/workflows/pkgci.yml` | Unit Test / Linux (x86_64) | `ubuntu-24.04` | 5 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622657) | [3m24s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016420) | [3m24s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016420) | 5 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 5 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622666) | [3m08s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016570) | [3m08s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016570) | 5 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | 5 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686214092) | [3m06s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016615) | [3m06s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016615) | 5 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622643) | [2m51s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016669) | [2m51s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016669) | 5 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 264 | 0% (1/264) |  | 1h37m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 225 | 5% (11/225) |  | 1h43m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 211 | 3% (6/211) |  | 1h47m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 182 | 5% (10/182) |  | 1h51m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
