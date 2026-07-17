# iree-ci-monitor

_Updated: 2026-07-17 05:43 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29576914390/job/87873389503) | [29m25s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026788) | — | 2 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [22m56s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416460) | [22m56s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416460) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [18m07s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416437) | [20m10s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416573) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [7m19s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416489) | [18m05s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416528) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [15m47s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416388) | [15m47s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416388) | — | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [9m47s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416524) | [12m18s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416534) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [11m06s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416399) | [11m06s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416399) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416385) | [5m03s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416456) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [4m59s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416397) | [4m59s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416397) | — | `shark01-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m26s](https://github.com/iree-org/iree/actions/runs/29571578881/job/87856366233) | [1m26s](https://github.com/iree-org/iree/actions/runs/29571578881/job/87856366233) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/29576914390/job/87873389415) | [40s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026767) | — | 9 |
| `azure-linux-scale` | ossci | 13 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/29576914390/job/87873389423) | [25s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026785) | 50% (1/2) | 13 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29569274131/job/87848982859) | [6s](https://github.com/iree-org/iree/actions/runs/29576164383/job/87871020969) | — | 12 |
| `macos-14` | github-hosted | 9 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026727) | [4s](https://github.com/iree-org/iree/actions/runs/29576914390/job/87873389443) | — | 9 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/29571537612/job/87856234453) | [4s](https://github.com/iree-org/iree/actions/runs/29571537612/job/87856234453) | — | 1 |
| `ubuntu-24.04` | github-hosted | 48 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29575782390/job/87869768881) | [3s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416505) | 50% (3/6) | 46 |
| `windows-2022` | github-hosted | 8 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29576914390/job/87873389446) | [3s](https://github.com/iree-org/iree/actions/runs/29576914390/job/87873389454) | — | 8 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416278) | [3s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416278) | — | 1 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416325) | [2s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416325) | — | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416376) | [2s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416376) | — | `shark01-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416411) | [2s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416411) | — | `iree-mi308-1` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416483) | [2s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416483) | — | `shark10-ci` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29576914390/job/87873389503) | [29m25s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026788) | [29m25s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026788) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [22m56s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416460) | [22m56s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416460) | [22m56s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416460) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [20m10s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416573) | [20m10s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416573) | [20m10s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416573) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [18m07s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416437) | [18m07s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416437) | [18m07s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416437) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [18m05s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416528) | [18m05s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416528) | [18m05s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416528) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [15m47s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416388) | [15m47s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416388) | [15m47s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416388) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [12m18s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416534) | [12m18s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416534) | [12m18s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416534) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [11m06s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416399) | [11m06s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416399) | [11m06s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416399) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [9m47s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416524) | [9m47s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416524) | [9m47s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416524) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [7m19s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416489) | [7m19s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416489) | [7m19s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416489) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [5m03s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416456) | [5m03s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416456) | [5m03s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416456) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [4m59s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416397) | [4m59s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416397) | [4m59s](https://github.com/iree-org/iree/actions/runs/29576914413/job/87875416397) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m26s](https://github.com/iree-org/iree/actions/runs/29571578881/job/87856366233) | [1m26s](https://github.com/iree-org/iree/actions/runs/29571578881/job/87856366233) | [1m26s](https://github.com/iree-org/iree/actions/runs/29571578881/job/87856366233) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/29576914390/job/87873389423) | [47s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026790) | [47s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026790) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 2 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/29576914390/job/87873389415) | [40s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026767) | [40s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026767) | 2 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29576914390/job/87873389439) | [25s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026777) | [25s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026777) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/29576914390/job/87873389486) | [25s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026785) | [25s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026785) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/29569274131/job/87848982852) | [10s](https://github.com/iree-org/iree/actions/runs/29576164383/job/87871020687) | [10s](https://github.com/iree-org/iree/actions/runs/29576164383/job/87871020687) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026763) | [9s](https://github.com/iree-org/iree/actions/runs/29576914390/job/87873389480) | [9s](https://github.com/iree-org/iree/actions/runs/29576914390/job/87873389480) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026809) | [9s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026809) | [9s](https://github.com/iree-org/iree/actions/runs/29569275608/job/87849026809) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 130 | 1% (1/130) |  | 33m58s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 147 | 1% (1/147) |  | 35m04s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 116 | 0% (0/116) |  | 37m52s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 116 | 10% (12/116) |  | 41m40s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 34 | 0% (0/34) |  | 53m16s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
