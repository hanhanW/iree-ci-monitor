# iree-ci-monitor

_Updated: 2026-08-18 11:59 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [20m15s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686213895) | [45m29s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896506) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 7 | 0 | — | — | 0 | [24m47s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896453) | [39m03s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016500) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 14 | 0 | — | — | 0 | [19m10s](https://github.com/iree-org/iree/actions/runs/32139982206/job/95730389888) | [36m47s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016718) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 7 | 0 | — | — | 0 | [9m51s](https://github.com/iree-org/iree/actions/runs/32154709284/job/95773665112) | [25m50s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686213812) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 14 | 0 | — | — | 0 | [10m35s](https://github.com/iree-org/iree/actions/runs/32154709284/job/95773665002) | [25m15s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016628) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 14 | 0 | — | — | 0 | [9m20s](https://github.com/iree-org/iree/actions/runs/32145303242/job/95741708447) | [22m27s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682623155) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 7 | 0 | — | — | 0 | [4m56s](https://github.com/iree-org/iree/actions/runs/32139982206/job/95730389758) | [20m02s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016643) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 14 | 0 | — | — | 0 | [8m11s](https://github.com/iree-org/iree/actions/runs/32139982206/job/95730389873) | [17m20s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896411) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 7 | 0 | — | — | 0 | [6m06s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622747) | [15m39s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896368) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [3m18s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686213971) | [11m53s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622664) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [4m54s](https://github.com/iree-org/iree/actions/runs/32145303242/job/95741708211) | [11m44s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622776) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m51s](https://github.com/iree-org/iree/actions/runs/32123441543/job/95668703018) | [1m51s](https://github.com/iree-org/iree/actions/runs/32123441543/job/95668703018) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 65 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/32128405972/job/95684023040) | [1m32s](https://github.com/iree-org/iree/actions/runs/32145303124/job/95737557546) | 7% (1/14) | 65 |
| `ubuntu-24.04-arm` | github-hosted | 33 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/32138204832/job/95714954200) | [1m29s](https://github.com/iree-org/iree/actions/runs/32120940648/job/95661025061) | 0% (0/6) | 33 |
| `ubuntu-24.04` | github-hosted | 189 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/32127254144/job/95680450255) | [1m15s](https://github.com/iree-org/iree/actions/runs/32120940648/job/95661025200) | 3% (1/39) | 185 |
| `windows-2022` | github-hosted | 33 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/32138204832/job/95714954218) | [1m14s](https://github.com/iree-org/iree/actions/runs/32120940648/job/95661025221) | 0% (0/6) | 33 |
| `macos-14` | github-hosted | 34 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/32128405972/job/95684023038) | [1m06s](https://github.com/iree-org/iree/actions/runs/32128405972/job/95684023127) | 0% (0/7) | 34 |
| `azure-windows-scale` | ossci | 11 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32138204832/job/95714954216) | [6s](https://github.com/iree-org/iree/actions/runs/32120940648/job/95661025772) | 0% (0/2) | 11 |
| `ubuntu-latest` | github-hosted | 42 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32145299105/job/95737482184) | [3s](https://github.com/iree-org/iree/actions/runs/32148573459/job/95748397692) | 0% (0/6) | 42 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 7 | 0 | — | — | [31m31s](https://github.com/iree-org/iree/actions/runs/32139982206/job/95730389879) | [47m22s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622906) | [47m22s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622906) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 7 | 0 | — | — | [20m15s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686213895) | [45m29s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896506) | [45m29s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896506) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 7 | 0 | — | — | [24m47s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896453) | [39m03s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016500) | [39m03s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016500) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 7 | 0 | — | — | [21m27s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016691) | [29m11s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896566) | [29m11s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896566) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 7 | 0 | — | — | [15m35s](https://github.com/iree-org/iree/actions/runs/32145303242/job/95741708448) | [28m24s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896454) | [28m24s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896454) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 7 | 0 | — | — | [9m51s](https://github.com/iree-org/iree/actions/runs/32154709284/job/95773665112) | [25m50s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686213812) | [25m50s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686213812) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 7 | 0 | — | — | [10m35s](https://github.com/iree-org/iree/actions/runs/32154709284/job/95773665002) | [25m15s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016628) | [25m15s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016628) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 7 | 0 | — | — | [15m12s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896604) | [24m08s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016695) | [24m08s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016695) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 7 | 0 | — | — | [4m56s](https://github.com/iree-org/iree/actions/runs/32139982206/job/95730389758) | [20m02s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016643) | [20m02s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016643) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 7 | 0 | — | — | [7m37s](https://github.com/iree-org/iree/actions/runs/32154709284/job/95773665136) | [19m01s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896487) | [19m01s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896487) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 7 | 0 | — | — | [8m11s](https://github.com/iree-org/iree/actions/runs/32139982206/job/95730389873) | [18m24s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686214090) | [18m24s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686214090) | 4 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 7 | 0 | — | — | [6m06s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622747) | [15m39s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896368) | [15m39s](https://github.com/iree-org/iree/actions/runs/32120940627/job/95662896368) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 7 | 0 | — | — | [8m14s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622884) | [13m38s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686213957) | [13m38s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686213957) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 7 | 0 | — | — | [3m18s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686213971) | [11m53s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622664) | [11m53s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622664) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 7 | 0 | — | — | [4m54s](https://github.com/iree-org/iree/actions/runs/32145303242/job/95741708211) | [11m44s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622776) | [11m44s](https://github.com/iree-org/iree/actions/runs/32127254364/job/95682622776) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 7 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32145303242/job/95741708212) | [4m00s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016746) | [4m00s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016746) | 7 |
| `.github/workflows/pkgci.yml` | Unit Test / Linux (x86_64) | `ubuntu-24.04` | 7 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32139982206/job/95730389429) | [3m24s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016420) | [3m24s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016420) | 7 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 7 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32128405893/job/95686214023) | [3m08s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016570) | [3m08s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016570) | 7 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | 7 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32154709284/job/95773665037) | [3m06s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016615) | [3m06s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016615) | 7 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 7 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/32154709284/job/95773665006) | [2m51s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016669) | [2m51s](https://github.com/iree-org/iree/actions/runs/32120938091/job/95663016669) | 7 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 278 | 0% (1/278) |  | 2h48m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 238 | 5% (11/238) |  | 2h55m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 220 | 3% (6/220) |  | 2h59m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 191 | 5% (10/191) |  | 3h02m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
