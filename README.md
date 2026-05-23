# iree-ci-monitor

_Updated: 2026-05-22 18:15 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 10 | 0 | — | — | 0 | [20m35s](https://github.com/iree-org/iree/actions/runs/26297816500/job/77416278186) | [1h14m](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720764) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 5 | 0 | — | — | 0 | [32m10s](https://github.com/iree-org/iree/actions/runs/26305080132/job/77440806703) | [1h12m](https://github.com/iree-org/iree/actions/runs/26298915419/job/77419739851) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [11m19s](https://github.com/iree-org/iree/actions/runs/26297816500/job/77416278267) | [56m38s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720700) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 5 | 0 | — | — | 0 | [33m14s](https://github.com/iree-org/iree/actions/runs/26305080132/job/77440806742) | [55m58s](https://github.com/iree-org/iree/actions/runs/26298915419/job/77419740064) | 0% (0/1) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 5 | 0 | — | — | 0 | [26m34s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720745) | [55m14s](https://github.com/iree-org/iree/actions/runs/26297816500/job/77416278310) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 5 | 0 | — | — | 0 | [29m27s](https://github.com/iree-org/iree/actions/runs/26305080132/job/77440806644) | [49m11s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720714) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [2m30s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720789) | [44m51s](https://github.com/iree-org/iree/actions/runs/26298915419/job/77419739999) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 10 | 0 | — | — | 0 | [15m32s](https://github.com/iree-org/iree/actions/runs/26297816500/job/77416278220) | [38m40s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720736) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [13m32s](https://github.com/iree-org/iree/actions/runs/26297816500/job/77416278108) | [34m21s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720727) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 10 | 0 | — | — | 0 | [10m00s](https://github.com/iree-org/iree/actions/runs/26303054797/job/77433998657) | [33m28s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720759) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 10 | 0 | — | — | 0 | [4m24s](https://github.com/iree-org/iree/actions/runs/26298915419/job/77419740018) | [29m53s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720743) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 5 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26303054797/job/77433998621) | [5m07s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720737) | 0% (0/1) | `iree-mi308-1` |
| `azure-linux-scale` | ossci | 27 | 1 | [10m39s](https://github.com/iree-org/iree/actions/runs/26212319110/job/77181582238) | 2026-05-21 06:27 PDT | 0 | [8s](https://github.com/iree-org/iree/actions/runs/26305080132/job/77439707740) | [2m57s](https://github.com/iree-org/iree/actions/runs/26298915294/job/77418758539) | 0% (0/6) | 26 |
| `macos-14` | github-hosted | 15 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26303054760/job/77432938513) | [2m19s](https://github.com/iree-org/iree/actions/runs/26298915294/job/77418758252) | 0% (0/3) | 15 |
| `windows-2022` | github-hosted | 15 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26303054760/job/77432938444) | [1m53s](https://github.com/iree-org/iree/actions/runs/26298915294/job/77418758359) | 0% (0/3) | 15 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26298915445/job/77418757150) | [1m50s](https://github.com/iree-org/iree/actions/runs/26298915294/job/77418758404) | 0% (0/3) | 15 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 20 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/26298915419/job/77419740135) | [1m39s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720747) | 0% (0/4) | 20 |
| `ubuntu-24.04` | github-hosted | 105 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26303054797/job/77433998476) | [30s](https://github.com/iree-org/iree/actions/runs/26298915294/job/77418758244) | 0% (0/18) | 100 |
| `azure-windows-scale` | ossci | 5 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26303054760/job/77432938755) | [8s](https://github.com/iree-org/iree/actions/runs/26298915294/job/77418758870) | 0% (0/1) | 5 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26298912641/job/77418702075) | [3s](https://github.com/iree-org/iree/actions/runs/26303053693/job/77432825342) | 0% (0/3) | 6 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 5 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26305080132/job/77440806622) | [2s](https://github.com/iree-org/iree/actions/runs/26303054797/job/77433998634) | 100% (1/1) | 5 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [10m39s](https://github.com/iree-org/iree/actions/runs/26212319110/job/77181582238) | 2026-05-21 06:27 PDT | `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | `promote-contraction-outputs` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [24m27s](https://github.com/iree-org/iree/actions/runs/26303054797/job/77433998613) | [1h14m](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720764) | [1h14m](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720764) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 5 | 0 | — | — | [32m10s](https://github.com/iree-org/iree/actions/runs/26305080132/job/77440806703) | [1h12m](https://github.com/iree-org/iree/actions/runs/26298915419/job/77419739851) | [1h12m](https://github.com/iree-org/iree/actions/runs/26298915419/job/77419739851) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 5 | 0 | — | — | [11m19s](https://github.com/iree-org/iree/actions/runs/26297816500/job/77416278267) | [56m38s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720700) | [56m38s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720700) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 5 | 0 | — | — | [33m14s](https://github.com/iree-org/iree/actions/runs/26305080132/job/77440806742) | [55m58s](https://github.com/iree-org/iree/actions/runs/26298915419/job/77419740064) | [55m58s](https://github.com/iree-org/iree/actions/runs/26298915419/job/77419740064) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 5 | 0 | — | — | [26m34s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720745) | [55m14s](https://github.com/iree-org/iree/actions/runs/26297816500/job/77416278310) | [55m14s](https://github.com/iree-org/iree/actions/runs/26297816500/job/77416278310) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 5 | 0 | — | — | [29m27s](https://github.com/iree-org/iree/actions/runs/26305080132/job/77440806644) | [49m11s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720714) | [49m11s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720714) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 5 | 0 | — | — | [2m30s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720789) | [44m51s](https://github.com/iree-org/iree/actions/runs/26298915419/job/77419739999) | [44m51s](https://github.com/iree-org/iree/actions/runs/26298915419/job/77419739999) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [13m23s](https://github.com/iree-org/iree/actions/runs/26305080132/job/77440806829) | [41m07s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720735) | [41m07s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720735) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 5 | 0 | — | — | [15m32s](https://github.com/iree-org/iree/actions/runs/26297816500/job/77416278220) | [38m40s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720736) | [38m40s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720736) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 5 | 0 | — | — | [13m32s](https://github.com/iree-org/iree/actions/runs/26297816500/job/77416278108) | [34m21s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720727) | [34m21s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720727) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 5 | 0 | — | — | [18m35s](https://github.com/iree-org/iree/actions/runs/26297816500/job/77416278442) | [33m48s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720772) | [33m48s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720772) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [21m59s](https://github.com/iree-org/iree/actions/runs/26303054797/job/77433998647) | [33m28s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720759) | [33m28s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720759) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [5m14s](https://github.com/iree-org/iree/actions/runs/26303054797/job/77433998537) | [29m53s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720743) | [29m53s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720743) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [9m14s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720718) | [12m24s](https://github.com/iree-org/iree/actions/runs/26298915419/job/77419740012) | [12m24s](https://github.com/iree-org/iree/actions/runs/26298915419/job/77419740012) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [4m01s](https://github.com/iree-org/iree/actions/runs/26298915419/job/77419739985) | [11m15s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720692) | [11m15s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720692) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 6 | 1 | [10m39s](https://github.com/iree-org/iree/actions/runs/26212319110/job/77181582238) | 2026-05-21 06:27 PDT | [8s](https://github.com/iree-org/iree/actions/runs/26298915294/job/77418758422) | [9s](https://github.com/iree-org/iree/actions/runs/26305080102/job/77439706878) | [9s](https://github.com/iree-org/iree/actions/runs/26305080102/job/77439706878) | 5 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 5 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26303054797/job/77433998621) | [5m07s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720737) | [5m07s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77420720737) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 5 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/26305080132/job/77439707740) | [4m52s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77418767127) | [4m52s](https://github.com/iree-org/iree/actions/runs/26298915475/job/77418767127) | 5 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 5 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26303054760/job/77432938444) | [3m34s](https://github.com/iree-org/iree/actions/runs/26298915294/job/77418758356) | [3m34s](https://github.com/iree-org/iree/actions/runs/26298915294/job/77418758356) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 5 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/26298915445/job/77418757320) | [2m57s](https://github.com/iree-org/iree/actions/runs/26298915294/job/77418758539) | [2m57s](https://github.com/iree-org/iree/actions/runs/26298915294/job/77418758539) | 5 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 316 | 2% (5/315) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 281 | 7% (20/280) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 238 | 3% (7/237) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 233 | 1% (2/232) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 74 | 3% (2/74) |  | 6h29m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h14m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h12m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
