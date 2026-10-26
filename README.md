# iree-ci-monitor

_Updated: 2026-10-26 06:11 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [32m06s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482438) | [1h33m](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100136) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [1h15m](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482020) | [1h21m](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482227) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [43m53s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100234) | [1h06m](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482187) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100109) | [52m10s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482127) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [6m11s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100168) | [37m26s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482140) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [26m19s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524481960) | [36m58s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100167) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100171) | [28m39s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524481989) | 0% (0/1) | `shark55-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m53s](https://github.com/iree-org/iree/actions/runs/40301079737/job/121498835807) | [1m53s](https://github.com/iree-org/iree/actions/runs/40301079737/job/121498835807) | 100% (1/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521511288) | [11s](https://github.com/iree-org/iree/actions/runs/40305372961/job/121530797265) | 0% (0/3) | 6 |
| `azure-linux-scale` | ossci | 15 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521510957) | [9s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521511166) | 0% (0/9) | 15 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40307879260/job/121521426054) | [3s](https://github.com/iree-org/iree/actions/runs/40307879260/job/121521426214) | 0% (0/3) | 6 |
| `macos-15` | github-hosted | 7 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521510565) | [3s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521510708) | 0% (0/3) | 7 |
| `ubuntu-24.04` | github-hosted | 46 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121535710119) | [2s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121559027637) | 4% (1/24) | 46 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521510560) | [2s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521510853) | 0% (0/3) | 6 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521510887) | [1s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521510887) | 0% (0/1) | 2 |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [32m06s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482438) | [1h33m](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100136) | [1h33m](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100136) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [12m34s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100129) | [1h21m](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482227) | [1h21m](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482227) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [4m54s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100195) | [1h15m](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482020) | [1h15m](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482020) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [43m53s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100234) | [1h06m](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482187) | [1h06m](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482187) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100109) | [52m10s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482127) | [52m10s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482127) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [6m11s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100168) | [37m26s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482140) | [37m26s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482140) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [6m17s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482152) | [36m58s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100167) | [36m58s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100167) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100171) | [28m39s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524481989) | [28m39s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524481989) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [11m28s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100227) | [26m19s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524481960) | [26m19s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524481960) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [6m53s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482177) | [17m05s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100260) | [17m05s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100260) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [15m09s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121524482018) | [16m35s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100368) | [16m35s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121516100368) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m53s](https://github.com/iree-org/iree/actions/runs/40301079737/job/121498835807) | [1m53s](https://github.com/iree-org/iree/actions/runs/40301079737/job/121498835807) | [1m53s](https://github.com/iree-org/iree/actions/runs/40301079737/job/121498835807) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 2 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521510955) | [11s](https://github.com/iree-org/iree/actions/runs/40305372961/job/121530797265) | [11s](https://github.com/iree-org/iree/actions/runs/40305372961/job/121530797265) | 2 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521510897) | [9s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521510897) | [9s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521510897) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521511015) | [9s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521511015) | [9s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521511015) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521511166) | [9s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521511166) | [9s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521511166) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521510933) | [8s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521510933) | [8s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521510933) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521511149) | [8s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521511149) | [8s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521511149) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/40305372942/job/121513132194) | [8s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121521504404) | [8s](https://github.com/iree-org/iree/actions/runs/40307880809/job/121521504404) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521510957) | [8s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521510957) | [8s](https://github.com/iree-org/iree/actions/runs/40307880753/job/121521510957) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 360 | 0% (0/360) |  | 1h09m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 298 | 2% (7/298) |  | 1h15m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h33m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h21m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
