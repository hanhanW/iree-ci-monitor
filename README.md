# iree-ci-monitor

_Updated: 2026-07-13 11:50 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 10 | 0 | — | — | 0 | [13m51s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86870608906) | [2h43m](https://github.com/iree-org/iree/actions/runs/29243750360/job/86797650618) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 10 | 0 | — | — | 0 | [28m29s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003390) | [2h29m](https://github.com/iree-org/iree/actions/runs/29243750360/job/86797650881) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [14m08s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003238) | [1h45m](https://github.com/iree-org/iree/actions/runs/29243794150/job/86801339113) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 20 | 0 | — | — | 0 | [17m28s](https://github.com/iree-org/iree/actions/runs/29257753159/job/86844582666) | [1h20m](https://github.com/iree-org/iree/actions/runs/29249229887/job/86815044266) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 10 | 0 | — | — | 0 | [5m38s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003418) | [1h17m](https://github.com/iree-org/iree/actions/runs/29243839489/job/86803078482) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 20 | 0 | — | — | 0 | [8m44s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86870609229) | [46m26s](https://github.com/iree-org/iree/actions/runs/29243247292/job/86795238212) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003144) | [40m46s](https://github.com/iree-org/iree/actions/runs/29243839489/job/86803078299) | 100% (1/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [5m18s](https://github.com/iree-org/iree/actions/runs/29240240659/job/86785975877) | [40m03s](https://github.com/iree-org/iree/actions/runs/29249229887/job/86815044321) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 20 | 0 | — | — | 0 | [7m35s](https://github.com/iree-org/iree/actions/runs/29240240659/job/86785975788) | [37m10s](https://github.com/iree-org/iree/actions/runs/29243794150/job/86801339138) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 20 | 0 | — | — | 0 | [10m54s](https://github.com/iree-org/iree/actions/runs/29257753159/job/86844583509) | [29m02s](https://github.com/iree-org/iree/actions/runs/29243839489/job/86803078655) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [8m17s](https://github.com/iree-org/iree/actions/runs/29243247292/job/86795238055) | [11m32s](https://github.com/iree-org/iree/actions/runs/29243750360/job/86797650831) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `ubuntu-24.04-arm` | github-hosted | 30 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/29257751060/job/86842554133) | [8m30s](https://github.com/iree-org/iree/actions/runs/29243750414/job/86795827938) | 0% (0/3) | 30 |
| `ubuntu-24.04` | github-hosted | 199 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29265214106/job/86868570258) | [5m18s](https://github.com/iree-org/iree/actions/runs/29243794143/job/86795812337) | 14% (3/21) | 199 |
| `macos-14` | github-hosted | 31 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29261977977/job/86857428119) | [4m00s](https://github.com/iree-org/iree/actions/runs/29243794143/job/86795812427) | 0% (0/4) | 31 |
| `windows-2022` | github-hosted | 30 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29265214106/job/86868570372) | [3m19s](https://github.com/iree-org/iree/actions/runs/29243794143/job/86795812302) | 0% (0/3) | 30 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 31 | 0 | — | — | 0 | [11s](https://github.com/iree-org/iree/actions/runs/29240240659/job/86785975723) | [3m00s](https://github.com/iree-org/iree/actions/runs/29249229887/job/86815043899) | 0% (0/1) | 31 |
| `azure-linux-scale` | ossci | 53 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/29249229859/job/86813470592) | [1m56s](https://github.com/iree-org/iree/actions/runs/29261977977/job/86857428599) | 0% (0/8) | 53 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m37s](https://github.com/iree-org/iree/actions/runs/29242588393/job/86791910174) | [1m37s](https://github.com/iree-org/iree/actions/runs/29242588393/job/86791910174) | 0% (0/1) | 1 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29243794150/job/86801339100) | [1m13s](https://github.com/iree-org/iree/actions/runs/29243839489/job/86803078569) | 0% (0/1) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 10 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29249229859/job/86813470762) | [4s](https://github.com/iree-org/iree/actions/runs/29261977977/job/86857428489) | 100% (1/1) | 10 |
| `ubuntu-latest` | github-hosted | 19 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29265212867/job/86868534351) | [3s](https://github.com/iree-org/iree/actions/runs/29248384740/job/86810730808) | 0% (0/4) | 19 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29242543435/job/86791764691) | [3s](https://github.com/iree-org/iree/actions/runs/29242543435/job/86791764691) | 0% (0/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 2 | 2 | [7h36m](https://github.com/iree-org/iree/actions/runs/29243794150/job/86801338899) | 2026-07-13 11:50 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [7h36m](https://github.com/iree-org/iree/actions/runs/29243794150/job/86801338899) | 2026-07-13 11:50 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/rvv_tile_size_selection` | pull_request |
| [7h27m](https://github.com/iree-org/iree/actions/runs/29243839489/job/86803078372) | 2026-07-13 11:50 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/rvv_scalable_vectorization` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 2 | 2 | [7h36m](https://github.com/iree-org/iree/actions/runs/29243794150/job/86801338899) | 2026-07-13 11:50 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 10 | 0 | — | — | [13m51s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86870608906) | [2h43m](https://github.com/iree-org/iree/actions/runs/29243750360/job/86797650618) | [2h43m](https://github.com/iree-org/iree/actions/runs/29243750360/job/86797650618) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 10 | 0 | — | — | [28m29s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003390) | [2h29m](https://github.com/iree-org/iree/actions/runs/29243750360/job/86797650881) | [2h29m](https://github.com/iree-org/iree/actions/runs/29243750360/job/86797650881) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 10 | 0 | — | — | [14m08s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003238) | [1h45m](https://github.com/iree-org/iree/actions/runs/29243794150/job/86801339113) | [1h45m](https://github.com/iree-org/iree/actions/runs/29243794150/job/86801339113) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [17m28s](https://github.com/iree-org/iree/actions/runs/29257753159/job/86844582666) | [1h23m](https://github.com/iree-org/iree/actions/runs/29243839489/job/86803078544) | [1h23m](https://github.com/iree-org/iree/actions/runs/29243839489/job/86803078544) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [9m52s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003391) | [1h20m](https://github.com/iree-org/iree/actions/runs/29249229887/job/86815044266) | [1h20m](https://github.com/iree-org/iree/actions/runs/29249229887/job/86815044266) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 10 | 0 | — | — | [5m38s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003418) | [1h17m](https://github.com/iree-org/iree/actions/runs/29243839489/job/86803078482) | [1h17m](https://github.com/iree-org/iree/actions/runs/29243839489/job/86803078482) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 10 | 0 | — | — | [8m44s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86870609229) | [51m45s](https://github.com/iree-org/iree/actions/runs/29243750360/job/86797650987) | [51m45s](https://github.com/iree-org/iree/actions/runs/29243750360/job/86797650987) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [6m49s](https://github.com/iree-org/iree/actions/runs/29240240659/job/86785975909) | [43m29s](https://github.com/iree-org/iree/actions/runs/29243794150/job/86801339037) | [43m29s](https://github.com/iree-org/iree/actions/runs/29243794150/job/86801339037) | 4 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003144) | [40m46s](https://github.com/iree-org/iree/actions/runs/29243839489/job/86803078299) | [40m46s](https://github.com/iree-org/iree/actions/runs/29243839489/job/86803078299) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 10 | 0 | — | — | [5m18s](https://github.com/iree-org/iree/actions/runs/29240240659/job/86785975877) | [40m03s](https://github.com/iree-org/iree/actions/runs/29249229887/job/86815044321) | [40m03s](https://github.com/iree-org/iree/actions/runs/29249229887/job/86815044321) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [7m03s](https://github.com/iree-org/iree/actions/runs/29261977791/job/86859518594) | [37m10s](https://github.com/iree-org/iree/actions/runs/29243794150/job/86801339138) | [37m10s](https://github.com/iree-org/iree/actions/runs/29243794150/job/86801339138) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [4m33s](https://github.com/iree-org/iree/actions/runs/29243794150/job/86801339123) | [32m18s](https://github.com/iree-org/iree/actions/runs/29249229887/job/86815044369) | [32m18s](https://github.com/iree-org/iree/actions/runs/29249229887/job/86815044369) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 10 | 0 | — | — | [7m51s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86870609041) | [29m48s](https://github.com/iree-org/iree/actions/runs/29249229887/job/86815044422) | [29m48s](https://github.com/iree-org/iree/actions/runs/29249229887/job/86815044422) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [12m55s](https://github.com/iree-org/iree/actions/runs/29257753159/job/86844582706) | [29m02s](https://github.com/iree-org/iree/actions/runs/29243839489/job/86803078655) | [29m02s](https://github.com/iree-org/iree/actions/runs/29243839489/job/86803078655) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 10 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29261977977/job/86857428294) | [12m22s](https://github.com/iree-org/iree/actions/runs/29243794143/job/86795812422) | [12m22s](https://github.com/iree-org/iree/actions/runs/29243794143/job/86795812422) | 10 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 10 | 0 | — | — | [8m17s](https://github.com/iree-org/iree/actions/runs/29243247292/job/86795238055) | [11m32s](https://github.com/iree-org/iree/actions/runs/29243750360/job/86797650831) | [11m32s](https://github.com/iree-org/iree/actions/runs/29243750360/job/86797650831) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29261977977/job/86857428244) | [9m35s](https://github.com/iree-org/iree/actions/runs/29243794143/job/86795812394) | [9m35s](https://github.com/iree-org/iree/actions/runs/29243794143/job/86795812394) | 10 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29257753159/job/86842506427) | [9m22s](https://github.com/iree-org/iree/actions/runs/29243839489/job/86795909376) | [9m22s](https://github.com/iree-org/iree/actions/runs/29243839489/job/86795909376) | 10 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 10 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29243247228/job/86794052483) | [9m13s](https://github.com/iree-org/iree/actions/runs/29243794143/job/86795812382) | [9m13s](https://github.com/iree-org/iree/actions/runs/29243794143/job/86795812382) | 10 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 187 | 9% (17/186) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 179 | 1% (1/178) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 241 | 2% (4/240) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 200 | 1% (1/199) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 56 | 9% (5/56) |  | 1h42m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 7h36m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h43m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h45m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 2h29m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h17m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
