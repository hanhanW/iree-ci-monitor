# iree-ci-monitor

_Updated: 2026-05-26 06:23 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `azure-linux-scale` | ossci | 8 | 0 | — | — | 0 | [13m34s](https://github.com/iree-org/iree/actions/runs/26447171971/job/77856404954) | [1h36m](https://github.com/iree-org/iree/actions/runs/26440945369/job/77834985450) | 100% (2/2) | 8 |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [20m39s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639733) | [26m15s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202446) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639612) | [25m00s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202129) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202096) | [19m44s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639652) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639699) | [18m21s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202416) | — | `shark01-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [13m13s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639680) | [17m24s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202411) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [11m05s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202410) | [16m25s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202273) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [11m19s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202296) | [13m28s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639641) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [5m59s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639667) | [7m08s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202108) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [4m33s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639648) | [6m57s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202428) | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [4m11s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639670) | [5m23s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202095) | — | `shark01-ci`, `shark10-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m48s](https://github.com/iree-org/iree/actions/runs/26447167001/job/77856386806) | [1m48s](https://github.com/iree-org/iree/actions/runs/26447167001/job/77856386806) | 100% (1/1) | 1 |
| `windows-2022` | github-hosted | 9 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26440945369/job/77834985438) | [1m07s](https://github.com/iree-org/iree/actions/runs/26445286762/job/77849950094) | — | 9 |
| `macos-14` | github-hosted | 10 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/26440945369/job/77834985488) | [58s](https://github.com/iree-org/iree/actions/runs/26445286762/job/77849950088) | — | 10 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26440945369/job/77834985381) | [28s](https://github.com/iree-org/iree/actions/runs/26445286762/job/77849950091) | — | 12 |
| `ubuntu-24.04` | github-hosted | 55 | 0 | — | — | 4 | [2s](https://github.com/iree-org/iree/actions/runs/26440945369/job/77834985396) | [26s](https://github.com/iree-org/iree/actions/runs/26445286762/job/77849950107) | 50% (2/4) | 54 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639817) | [9s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202622) | — | 8 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [5s](https://github.com/iree-org/iree/actions/runs/26447159437/job/77856359975) | [5s](https://github.com/iree-org/iree/actions/runs/26447159437/job/77856359975) | — | 1 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26445236717/job/77849739532) | [3s](https://github.com/iree-org/iree/actions/runs/26445236717/job/77849739348) | — | 3 |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639632) | [1s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202123) | — | `shark75-ci` |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639634) | [1s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202119) | — | 2 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639644) | [1s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202452) | — | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26440945369/job/77834985460) | [1s](https://github.com/iree-org/iree/actions/runs/26440945369/job/77834985460) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [1h36m](https://github.com/iree-org/iree/actions/runs/26440945369/job/77834985450) | [1h36m](https://github.com/iree-org/iree/actions/runs/26440945369/job/77834985450) | [1h36m](https://github.com/iree-org/iree/actions/runs/26440945369/job/77834985450) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [1h36m](https://github.com/iree-org/iree/actions/runs/26440945369/job/77834985674) | [1h36m](https://github.com/iree-org/iree/actions/runs/26440945369/job/77834985674) | [1h36m](https://github.com/iree-org/iree/actions/runs/26440945369/job/77834985674) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [26m59s](https://github.com/iree-org/iree/actions/runs/26440945369/job/77834985522) | [26m59s](https://github.com/iree-org/iree/actions/runs/26440945369/job/77834985522) | [26m59s](https://github.com/iree-org/iree/actions/runs/26440945369/job/77834985522) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [20m39s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639733) | [26m15s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202446) | [26m15s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202446) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639612) | [25m00s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202129) | [25m00s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202129) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202096) | [19m44s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639652) | [19m44s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639652) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639699) | [18m21s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202416) | [18m21s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202416) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [5m19s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639760) | [17m24s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202411) | [17m24s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202411) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [9m13s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639666) | [16m25s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202273) | [16m25s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202273) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [10m32s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639658) | [13m48s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202399) | [13m48s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202399) | 1 |
| `.github/workflows/ci_linux_x64_clang_tsan.yml` | linux_x64_clang_tsan | `azure-linux-scale` | 1 | 0 | — | — | [13m34s](https://github.com/iree-org/iree/actions/runs/26447171971/job/77856404954) | [13m34s](https://github.com/iree-org/iree/actions/runs/26447171971/job/77856404954) | [13m34s](https://github.com/iree-org/iree/actions/runs/26447171971/job/77856404954) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [11m19s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202296) | [13m28s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639641) | [13m28s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639641) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202325) | [13m13s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639680) | [13m13s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639680) | 2 |
| `.github/workflows/ci_linux_x64_clang_debug.yml` | linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [11m18s](https://github.com/iree-org/iree/actions/runs/26447153358/job/77856339703) | [11m18s](https://github.com/iree-org/iree/actions/runs/26447153358/job/77856339703) | [11m18s](https://github.com/iree-org/iree/actions/runs/26447153358/job/77856339703) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [8m41s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639757) | [11m05s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202410) | [11m05s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202410) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [5m59s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639667) | [7m08s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202108) | [7m08s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202108) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [4m33s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639648) | [6m57s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202428) | [6m57s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202428) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [4m11s](https://github.com/iree-org/iree/actions/runs/26430274090/job/77802639670) | [5m23s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202095) | [5m23s](https://github.com/iree-org/iree/actions/runs/26440945409/job/77839202095) | 2 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m48s](https://github.com/iree-org/iree/actions/runs/26447167001/job/77856386806) | [1m48s](https://github.com/iree-org/iree/actions/runs/26447167001/job/77856386806) | [1m48s](https://github.com/iree-org/iree/actions/runs/26447167001/job/77856386806) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26445836165/job/77851854221) | [1m07s](https://github.com/iree-org/iree/actions/runs/26445286762/job/77849950094) | [1m07s](https://github.com/iree-org/iree/actions/runs/26445286762/job/77849950094) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 240 | 4% (9/239) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 288 | 7% (20/287) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 310 | 2% (7/309) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 229 | 1% (2/228) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 76 | 3% (2/76) |  | 4h24m ago |

## Alerts

- **[queue-starved]** `azure-linux-scale` p95 queue 1h36m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
