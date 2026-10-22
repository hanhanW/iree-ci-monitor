# iree-ci-monitor

_Updated: 2026-10-22 10:15 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 7 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | 0 | [10m46s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119901147145) | [31m38s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868446) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 2 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | 0 | [16m16s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119901147784) | [28m08s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868307) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [12m12s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119901147221) | [25m42s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868309) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [8m45s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541415) | [20m34s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868087) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [14m10s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868147) | [20m16s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541459) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [10m34s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119901147256) | [14m57s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541689) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541510) | [5m22s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119901147469) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m29s](https://github.com/iree-org/iree/actions/runs/39755698707/job/119747023132) | [1m29s](https://github.com/iree-org/iree/actions/runs/39755698707/job/119747023132) | 100% (1/1) | 1 |
| `windows-2022` | github-hosted | 27 | 0 | — | — | 6 | [2s](https://github.com/iree-org/iree/actions/runs/39774168875/job/119886280676) | [54s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440445) | 0% (0/3) | 25 |
| `azure-linux-scale` | ossci | 59 | 0 | — | — | 13 | [8s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599544) | [48s](https://github.com/iree-org/iree/actions/runs/39774168875/job/119808891343) | 0% (0/10) | 53 |
| `macos-15` | github-hosted | 28 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/39760386742/job/119762892684) | [41s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440413) | 0% (0/10) | 25 |
| `ubuntu-24.04-arm` | github-hosted | 27 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/39750057557/job/119729250107) | [5s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599209) | 0% (0/9) | 24 |
| `ubuntu-24.04` | github-hosted | 128 | 0 | — | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/39760386742/job/119778753470) | [3s](https://github.com/iree-org/iree/actions/runs/39799632729/job/119896451195) | 0% (0/33) | 119 |
| `ubuntu-latest` | github-hosted | 33 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/39819724765/job/119967492809) | [3s](https://github.com/iree-org/iree/actions/runs/39793337593/job/119874644282) | 0% (0/6) | 33 |
| `azure-windows-scale` | ossci | 9 | 0 | — | — | 2 | [1s](https://github.com/iree-org/iree/actions/runs/39774168875/job/119808891194) | [2s](https://github.com/iree-org/iree/actions/runs/39750057557/job/119729250837) | 0% (0/1) | 8 |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827580) | 2026-10-19 06:26 PDT | [18m50s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868197) | [25m04s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541623) | [25m04s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541623) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | [8m08s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868364) | [10m46s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119901147145) | [10m46s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119901147145) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | [12m22s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541419) | [28m08s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868307) | [28m08s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868307) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [16m41s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541483) | [31m38s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868446) | [31m38s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868446) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [20m09s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541495) | [25m42s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868309) | [25m42s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868309) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [10m17s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868215) | [23m38s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541809) | [23m38s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541809) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [8m45s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541415) | [20m34s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868087) | [20m34s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868087) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [14m10s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868147) | [20m16s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541459) | [20m16s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541459) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [10m34s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119901147256) | [14m57s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541689) | [14m57s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541689) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39774168952/job/119812541510) | [5m22s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119901147469) | [5m22s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119901147469) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [3m34s](https://github.com/iree-org/iree/actions/runs/39799632637/job/119901147206) | [5m05s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868209) | [5m05s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868209) | 2 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m29s](https://github.com/iree-org/iree/actions/runs/39755698707/job/119747023132) | [1m29s](https://github.com/iree-org/iree/actions/runs/39755698707/job/119747023132) | [1m29s](https://github.com/iree-org/iree/actions/runs/39755698707/job/119747023132) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 9 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/39750599201/job/119730627448) | [1m22s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440833) | [1m22s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440833) | 8 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 9 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/39799632729/job/119896451834) | [1m14s](https://github.com/iree-org/iree/actions/runs/39749195617/job/119725579467) | [1m14s](https://github.com/iree-org/iree/actions/runs/39749195617/job/119725579467) | 8 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 9 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/39750599201/job/119730627725) | [1m13s](https://github.com/iree-org/iree/actions/runs/39749195617/job/119725579590) | [1m13s](https://github.com/iree-org/iree/actions/runs/39749195617/job/119725579590) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599042) | [1m06s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440607) | [1m06s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440607) | 8 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 9 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/39750599201/job/119730627894) | [59s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599470) | [59s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599470) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39799632729/job/119896451401) | [54s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440445) | [54s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440445) | 8 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 9 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/39750057557/job/119729250083) | [46s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599478) | [46s](https://github.com/iree-org/iree/actions/runs/39819725225/job/119967599478) | 8 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 8 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/39819725777/job/119967578923) | [45s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119762913000) | [45s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119762913000) | 8 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 374 | 0% (0/374) |  | 1h51m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 317 | 2% (7/317) |  | 2h00m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
