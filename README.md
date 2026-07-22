# iree-ci-monitor

_Updated: 2026-07-21 17:53 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 16 | 0 | — | — | 0 | [2h55m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671758004) | [4h31m](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819489) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 8 | 0 | — | — | 0 | [2h29m](https://github.com/iree-org/iree/actions/runs/29845395879/job/88686375233) | [3h18m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671758137) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 8 | 0 | — | — | 0 | [2h24m](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672958761) | [3h09m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671757943) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 8 | 0 | — | — | 0 | [58m15s](https://github.com/iree-org/iree/actions/runs/29845395879/job/88686375072) | [3h03m](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819353) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 8 | 0 | — | — | 0 | [32m16s](https://github.com/iree-org/iree/actions/runs/29849303530/job/88700132081) | [2h49m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671758048) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [1h07m](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071210) | [2h47m](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672958836) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 16 | 0 | — | — | 0 | [54m05s](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071320) | [2h33m](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071543) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 16 | 0 | — | — | 0 | [54m11s](https://github.com/iree-org/iree/actions/runs/29849303530/job/88700132364) | [2h32m](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819739) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [56m56s](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672959412) | [2h18m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671758177) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | — | 0 | [1h24m](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071116) | [1h43m](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819290) | 0% (0/1) | 8 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [44m04s](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672959109) | [1h17m](https://github.com/iree-org/iree/actions/runs/29845395879/job/88686375099) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 16 | 0 | — | — | 0 | [25m01s](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819782) | [50m38s](https://github.com/iree-org/iree/actions/runs/29845395879/job/88686375111) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 8 | 0 | — | — | 0 | [13m56s](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671757931) | [43m32s](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672959375) | 0% (0/1) | `iree-mi308-1` |
| `ubuntu-24.04` | github-hosted | 157 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29860291954/job/88745752827) | [2m25s](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672959028) | 9% (2/22) | 155 |
| `azure-linux-scale` | ossci | 31 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/29860291954/job/88745752861) | [56s](https://github.com/iree-org/iree/actions/runs/29842506987/job/88674727233) | 0% (0/6) | 31 |
| `windows-2022` | github-hosted | 18 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29849302999/job/88697956429) | [40s](https://github.com/iree-org/iree/actions/runs/29842506614/job/88674720741) | 0% (0/3) | 18 |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/29849231784/job/88697626320) | [23s](https://github.com/iree-org/iree/actions/runs/29842506614/job/88674720811) | 0% (0/3) | 18 |
| `macos-14` | github-hosted | 18 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29845395719/job/88684636324) | [4s](https://github.com/iree-org/iree/actions/runs/29858138632/job/88740684980) | 0% (0/3) | 18 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29845393435/job/88684589254) | [4s](https://github.com/iree-org/iree/actions/runs/29845393435/job/88684589216) | 0% (0/3) | 3 |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29842506614/job/88674720954) | [2s](https://github.com/iree-org/iree/actions/runs/29858138632/job/88740685101) | 0% (0/1) | 6 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [4h06m](https://github.com/iree-org/iree/actions/runs/29845395879/job/88686375287) | [4h35m](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672959539) | [4h35m](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672959539) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [2h55m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671758004) | [4h28m](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071640) | [4h28m](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071640) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 8 | 0 | — | — | [2h29m](https://github.com/iree-org/iree/actions/runs/29845395879/job/88686375233) | [3h18m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671758137) | [3h18m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671758137) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 8 | 0 | — | — | [2h24m](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672958761) | [3h09m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671757943) | [3h09m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671757943) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 8 | 0 | — | — | [58m15s](https://github.com/iree-org/iree/actions/runs/29845395879/job/88686375072) | [3h03m](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819353) | [3h03m](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819353) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 8 | 0 | — | — | [32m16s](https://github.com/iree-org/iree/actions/runs/29849303530/job/88700132081) | [2h49m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671758048) | [2h49m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671758048) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 8 | 0 | — | — | [1h07m](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071210) | [2h47m](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672958836) | [2h47m](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672958836) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 8 | 0 | — | — | [2h06m](https://github.com/iree-org/iree/actions/runs/29845395879/job/88686375304) | [2h44m](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071502) | [2h44m](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071502) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 8 | 0 | — | — | [59m12s](https://github.com/iree-org/iree/actions/runs/29849303530/job/88700132114) | [2h38m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671758041) | [2h38m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671758041) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 8 | 0 | — | — | [48m58s](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672959283) | [2h33m](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071543) | [2h33m](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071543) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 8 | 0 | — | — | [45m52s](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672959295) | [2h32m](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819739) | [2h32m](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819739) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 8 | 0 | — | — | [56m56s](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672959412) | [2h18m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671758177) | [2h18m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671758177) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 8 | 0 | — | — | [1h24m](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071116) | [1h43m](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819290) | [1h43m](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819290) | 8 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 8 | 0 | — | — | [44m04s](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672959109) | [1h17m](https://github.com/iree-org/iree/actions/runs/29845395879/job/88686375099) | [1h17m](https://github.com/iree-org/iree/actions/runs/29845395879/job/88686375099) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [20m41s](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671758187) | [54m35s](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071549) | [54m35s](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071549) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 8 | 0 | — | — | [13m56s](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671757931) | [43m32s](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672959375) | [43m32s](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672959375) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [33m06s](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071232) | [38m14s](https://github.com/iree-org/iree/actions/runs/29858138647/job/88744048727) | [38m14s](https://github.com/iree-org/iree/actions/runs/29858138647/job/88744048727) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [6m26s](https://github.com/iree-org/iree/actions/runs/29845395719/job/88684636659) | [6m26s](https://github.com/iree-org/iree/actions/runs/29845395719/job/88684636659) | [6m26s](https://github.com/iree-org/iree/actions/runs/29845395719/job/88684636659) | 1 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 8 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29858138647/job/88744048731) | [3m51s](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819721) | [3m51s](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819721) | 8 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 8 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29858138647/job/88744048707) | [3m44s](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819440) | [3m44s](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819440) | 8 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 266 | 0% (1/266) |  | 3h43m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 219 | 4% (8/219) |  | 3h52m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 207 | 1% (2/207) |  | 4h11m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 200 | 0% (0/200) |  | 4h19m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 62 | 0% (0/62) |  | 4h39m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 2h18m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h17m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 4h31m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 3h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 3h03m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 2h47m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 3h18m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h33m (> 1h00m)
- **[queue-starved]** `linux-mi325-1gpu-ossci-iree-org` p95 queue 1h43m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 2h49m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
