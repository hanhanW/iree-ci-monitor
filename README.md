# iree-ci-monitor

_Updated: 2026-07-23 17:52 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 3 | 0 | — | — | 0 | [1h17m](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054268) | [4h18m](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530616) | — | 3 |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [10m18s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262811943) | [28m10s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530726) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [8m30s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812215) | [23m12s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530732) | — | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [8m20s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530744) | [20m46s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054173) | — | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [9m30s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812371) | [18m39s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054300) | — | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [1m07s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812333) | [17m11s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054239) | — | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [6m42s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812417) | [14m22s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530837) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054254) | [11m53s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812044) | — | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [5m19s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530739) | [10m17s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054212) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [3m54s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054169) | [10m00s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530816) | — | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [3m14s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812355) | [8m22s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530797) | — | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [4m10s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054102) | [6m43s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812234) | — | `shark01-ci`, `shark10-ci` |
| `macos-14` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30023956159/job/89264398888) | [35s](https://github.com/iree-org/iree/actions/runs/30035269375/job/89324265346) | — | 9 |
| `azure-linux-scale` | ossci | 15 | 0 | — | — | 0 | [18s](https://github.com/iree-org/iree/actions/runs/30020118178/job/89260477307) | [23s](https://github.com/iree-org/iree/actions/runs/30035269375/job/89324265536) | — | 15 |
| `windows-2022` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30035269375/job/89324265361) | [6s](https://github.com/iree-org/iree/actions/runs/30020118178/job/89260477332) | — | 9 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30020118178/job/89260477310) | [5s](https://github.com/iree-org/iree/actions/runs/30023956159/job/89264398824) | — | 9 |
| `ubuntu-24.04` | github-hosted | 64 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89324222018) | [4s](https://github.com/iree-org/iree/actions/runs/30023956159/job/89264398825) | 33% (1/3) | 63 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812527) | [2s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054369) | — | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30023956159/job/89264399225) | [2s](https://github.com/iree-org/iree/actions/runs/30035269375/job/89324265592) | — | 3 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 3 | 0 | — | — | [1h17m](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054268) | [4h18m](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530616) | [4h18m](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530616) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [10m18s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262811943) | [28m10s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530726) | [28m10s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530726) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [8m30s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812215) | [23m12s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530732) | [23m12s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530732) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [18m39s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530868) | [20m46s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054173) | [20m46s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054173) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [9m30s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812371) | [18m39s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054300) | [18m39s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054300) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [2m44s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812350) | [17m11s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054239) | [17m11s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054239) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812356) | [14m22s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530837) | [14m22s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530837) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [1m07s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812333) | [12m38s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054358) | [12m38s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054358) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054254) | [11m53s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812044) | [11m53s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812044) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [5m19s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530739) | [10m17s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054212) | [10m17s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054212) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [3m54s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054169) | [10m00s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530816) | [10m00s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530816) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [8m20s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530744) | [10m00s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054258) | [10m00s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054258) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [8m30s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054354) | [9m34s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530792) | [9m34s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530792) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [4m22s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054260) | [8m22s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530797) | [8m22s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530797) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [4m10s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054102) | [6m43s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812234) | [6m43s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812234) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812351) | [5m07s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530866) | [5m07s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530866) | 2 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812217) | [38s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054150) | [38s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054150) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 3 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/30023956159/job/89264398844) | [35s](https://github.com/iree-org/iree/actions/runs/30035269375/job/89324265346) | [35s](https://github.com/iree-org/iree/actions/runs/30035269375/job/89324265346) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30023956159/job/89264398888) | [32s](https://github.com/iree-org/iree/actions/runs/30035269375/job/89324265377) | [32s](https://github.com/iree-org/iree/actions/runs/30035269375/job/89324265377) | 3 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530772) | [32s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054257) | [32s](https://github.com/iree-org/iree/actions/runs/30035269414/job/89326054257) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 286 | 1% (3/286) |  | 3h53m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 373 | 1% (5/373) |  | 3h54m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 303 | 5% (14/303) |  | 3h55m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 275 | 1% (3/275) |  | 3h56m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 86 | 1% (1/86) |  | 4h06m ago |

## Alerts

- **[queue-starved]** `linux-mi325-1gpu-ossci-iree-org` p95 queue 4h18m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
