# iree-ci-monitor

_Updated: 2026-11-23 15:59 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [7m23s](https://github.com/iree-org/iree/actions/runs/45249570848/job/137960018215) | [23m00s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058810154) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [10m20s](https://github.com/iree-org/iree/actions/runs/45273635711/job/138043708758) | [20m48s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058810049) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [15m38s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058810046) | [19m02s](https://github.com/iree-org/iree/actions/runs/45225198146/job/137916601802) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [7m45s](https://github.com/iree-org/iree/actions/runs/45225198146/job/137916601535) | [17m18s](https://github.com/iree-org/iree/actions/runs/45249570848/job/137960018350) | 0% (0/2) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [8m21s](https://github.com/iree-org/iree/actions/runs/45225198146/job/137916601570) | [15m51s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058810029) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [8m57s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058810144) | [14m44s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058809865) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/45225198146/job/137916601274) | [4m48s](https://github.com/iree-org/iree/actions/runs/45249570848/job/137960017692) | 0% (0/1) | `shark75-ci` |
| `azure-linux-scale` | ossci | 25 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/45276938665/job/138051586856) | [2m01s](https://github.com/iree-org/iree/actions/runs/45249569915/job/137955486970) | 0% (0/7) | 25 |
| `ubuntu-24.04` | github-hosted | 131 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/45225198146/job/137916601371) | [55s](https://github.com/iree-org/iree/actions/runs/45276939285/job/138051069096) | 0% (0/19) | 105 |
| `macos-15` | github-hosted | 12 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/45273635959/job/138039851758) | [42s](https://github.com/iree-org/iree/actions/runs/45276938665/job/138051586324) | 0% (0/3) | 12 |
| `windows-2022` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/45249569915/job/137955485992) | [15s](https://github.com/iree-org/iree/actions/runs/45276938665/job/138051586254) | 0% (0/3) | 12 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/45225198150/job/137911334446) | [12s](https://github.com/iree-org/iree/actions/runs/45276938665/job/138051586353) | 0% (0/3) | 12 |
| `ubuntu-latest` | github-hosted | 37 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/45274633306/job/138043109357) | [3s](https://github.com/iree-org/iree/actions/runs/45249567938/job/137955327281) | 0% (0/4) | 37 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/45273635959/job/138039852561) | [1s](https://github.com/iree-org/iree/actions/runs/45276938665/job/138051586865) | 0% (0/1) | 4 |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [7m23s](https://github.com/iree-org/iree/actions/runs/45249570848/job/137960018215) | [23m00s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058810154) | [23m00s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058810154) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [10m20s](https://github.com/iree-org/iree/actions/runs/45273635711/job/138043708758) | [20m48s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058810049) | [20m48s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058810049) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [15m38s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058810046) | [19m02s](https://github.com/iree-org/iree/actions/runs/45225198146/job/137916601802) | [19m02s](https://github.com/iree-org/iree/actions/runs/45225198146/job/137916601802) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [17m02s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058809812) | [17m18s](https://github.com/iree-org/iree/actions/runs/45249570848/job/137960018350) | [17m18s](https://github.com/iree-org/iree/actions/runs/45249570848/job/137960018350) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [12m11s](https://github.com/iree-org/iree/actions/runs/45273635711/job/138043708501) | [15m51s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058810029) | [15m51s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058810029) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [8m53s](https://github.com/iree-org/iree/actions/runs/45273635711/job/138043708882) | [14m59s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058809793) | [14m59s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058809793) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [10m43s](https://github.com/iree-org/iree/actions/runs/45249570848/job/137960018422) | [14m44s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058809865) | [14m44s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058809865) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [8m57s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058810144) | [13m18s](https://github.com/iree-org/iree/actions/runs/45225198146/job/137916601890) | [13m18s](https://github.com/iree-org/iree/actions/runs/45225198146/job/137916601890) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [3m17s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138058810168) | [13m02s](https://github.com/iree-org/iree/actions/runs/45249570848/job/137960018060) | [13m02s](https://github.com/iree-org/iree/actions/runs/45249570848/job/137960018060) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [5m32s](https://github.com/iree-org/iree/actions/runs/45225198146/job/137916601684) | [13m00s](https://github.com/iree-org/iree/actions/runs/45273635711/job/138043708941) | [13m00s](https://github.com/iree-org/iree/actions/runs/45273635711/job/138043708941) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/45225198146/job/137916601274) | [4m48s](https://github.com/iree-org/iree/actions/runs/45249570848/job/137960017692) | [4m48s](https://github.com/iree-org/iree/actions/runs/45249570848/job/137960017692) | 1 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | 10 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/45276940739/job/138051534968) | [2m02s](https://github.com/iree-org/iree/actions/runs/45276940455/job/138051667576) | [2m02s](https://github.com/iree-org/iree/actions/runs/45276940455/job/138051667576) | 7 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 4 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/45276938989/job/138051632393) | [2m02s](https://github.com/iree-org/iree/actions/runs/45225198146/job/137911428034) | [2m02s](https://github.com/iree-org/iree/actions/runs/45225198146/job/137911428034) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 4 | 0 | — | — | [1m31s](https://github.com/iree-org/iree/actions/runs/45273635959/job/138039852905) | [2m01s](https://github.com/iree-org/iree/actions/runs/45249569915/job/137955486970) | [2m01s](https://github.com/iree-org/iree/actions/runs/45249569915/job/137955486970) | 4 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 10 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/45276940455/job/138052988507) | [2m00s](https://github.com/iree-org/iree/actions/runs/45276940739/job/138051706617) | [2m00s](https://github.com/iree-org/iree/actions/runs/45276940739/job/138051706617) | 10 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 4 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/45225198150/job/137911334488) | [1m57s](https://github.com/iree-org/iree/actions/runs/45276938665/job/138051586246) | [1m57s](https://github.com/iree-org/iree/actions/runs/45276938665/job/138051586246) | 4 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | 10 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/45276940561/job/138051611671) | [1m51s](https://github.com/iree-org/iree/actions/runs/45276940543/job/138051619745) | [1m51s](https://github.com/iree-org/iree/actions/runs/45276940543/job/138051619745) | 7 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 4 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/45249569915/job/137955486250) | [1m51s](https://github.com/iree-org/iree/actions/runs/45276938665/job/138051586233) | [1m51s](https://github.com/iree-org/iree/actions/runs/45276938665/job/138051586233) | 4 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 10 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/45276940543/job/138052845688) | [1m47s](https://github.com/iree-org/iree/actions/runs/45276940561/job/138051838540) | [1m47s](https://github.com/iree-org/iree/actions/runs/45276940561/job/138051838540) | 10 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 4 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/45225198150/job/137911334497) | [1m44s](https://github.com/iree-org/iree/actions/runs/45276938665/job/138051586203) | [1m44s](https://github.com/iree-org/iree/actions/runs/45276938665/job/138051586203) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 123 | 4% (5/123) |  | 1h06m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 164 | 4% (6/164) |  | 1h18m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
