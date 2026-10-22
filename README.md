# iree-ci-monitor

_Updated: 2026-10-22 14:41 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 8 | 2 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | 0 | [12m22s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541419) | [25m04s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541623) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [7m27s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977838169) | [23m38s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541809) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 7 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | 0 | [15m16s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119901147003) | [23m03s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977838396) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977837672) | [20m16s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541459) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [12m15s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977837593) | [14m57s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541689) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [3m22s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977837642) | [13m26s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977837626) | 0% (0/4) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [8m45s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541415) | [9m19s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977837618) | 0% (0/2) | `shark75-ci` |
| `azure-linux-scale` | ossci | 27 | 0 | — | — | 6 | [9s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119896465369) | [48s](https://github.com/iree-org/iree/actions/runs/39774168875/job/119808891343) | 0% (0/15) | 21 |
| `macos-15` | github-hosted | 12 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599092) | [6s](https://github.com/iree-org/iree/actions/runs/39799632729/job/119896451190) | 0% (0/9) | 9 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967598840) | [5s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599209) | 0% (0/9) | 9 |
| `ubuntu-24.04` | github-hosted | 69 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119913847542) | [3s](https://github.com/iree-org/iree/actions/runs/39799632729/job/119916488415) | 4% (2/46) | 62 |
| `windows-2022` | github-hosted | 12 | 0 | — | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/39799632729/job/119896451401) | [3s](https://github.com/iree-org/iree/actions/runs/39799632729/job/119896451510) | 17% (1/6) | 10 |
| `ubuntu-latest` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39819724765/job/119967492942) | [3s](https://github.com/iree-org/iree/actions/runs/39820704960/job/119970921432) | 0% (0/6) | 18 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/39799632729/job/119896451937) | [1s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599585) | 0% (0/2) | 3 |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827580) | 2026-10-19 06:26 PDT | [16m16s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119901147784) | [25m04s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541623) | [25m04s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541623) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | [10m46s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119901147145) | [18m43s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977837987) | [18m43s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977837987) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | [12m22s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541419) | [23m52s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977838190) | [23m52s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977838190) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977837731) | [23m38s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541809) | [23m38s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541809) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [16m41s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541483) | [23m03s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977838396) | [23m03s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977838396) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977837672) | [20m16s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541459) | [20m16s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541459) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [12m12s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119901147221) | [20m09s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541495) | [20m09s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541495) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [12m15s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977837593) | [14m57s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541689) | [14m57s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541689) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [5m22s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119901147469) | [13m26s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977837626) | [13m26s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977837626) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [8m45s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541415) | [9m19s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977837618) | [9m19s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977837618) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [3m22s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119977837642) | [3m34s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119901147206) | [3m34s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119901147206) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 4 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/39799632729/job/119896451800) | [59s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599470) | [59s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599470) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599533) | [48s](https://github.com/iree-org/iree/actions/runs/39774168875/job/119808891343) | [48s](https://github.com/iree-org/iree/actions/runs/39774168875/job/119808891343) | 3 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 4 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/39799632729/job/119896451897) | [46s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599478) | [46s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599478) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599416) | [23s](https://github.com/iree-org/iree/actions/runs/39774168875/job/119808891246) | [23s](https://github.com/iree-org/iree/actions/runs/39774168875/job/119808891246) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 3 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599409) | [15s](https://github.com/iree-org/iree/actions/runs/39774168875/job/119808891116) | [15s](https://github.com/iree-org/iree/actions/runs/39774168875/job/119808891116) | 2 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 4 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599544) | [9s](https://github.com/iree-org/iree/actions/runs/39799632729/job/119896451782) | [9s](https://github.com/iree-org/iree/actions/runs/39799632729/job/119896451782) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 4 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599242) | [9s](https://github.com/iree-org/iree/actions/runs/39799632729/job/119896451634) | [9s](https://github.com/iree-org/iree/actions/runs/39799632729/job/119896451634) | 3 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119967578923) | [9s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119896465369) | [9s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119896465369) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 4 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599092) | [6s](https://github.com/iree-org/iree/actions/runs/39799632729/job/119896451190) | [6s](https://github.com/iree-org/iree/actions/runs/39799632729/job/119896451190) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 381 | 0% (0/381) |  | 3h49m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 321 | 2% (7/321) |  | 4h01m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
