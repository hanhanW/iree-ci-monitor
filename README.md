# iree-ci-monitor

_Updated: 2026-10-22 04:59 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 3 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | 0 | [8m08s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868364) | [31m38s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868446) | — | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 2 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | 0 | [18m50s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868197) | [28m08s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868307) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [10m17s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868215) | [25m42s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868309) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [20m34s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868087) | [20m34s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868087) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [14m10s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868147) | [14m10s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868147) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765867940) | [5m05s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868209) | — | `shark55-ci`, `shark75-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m29s](https://github.com/iree-org/iree/actions/runs/39755698707/job/119747023132) | [1m29s](https://github.com/iree-org/iree/actions/runs/39755698707/job/119747023132) | 100% (1/1) | 1 |
| `windows-2022` | github-hosted | 20 | 0 | — | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/39760386742/job/119762892725) | [54s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440445) | — | 20 |
| `azure-linux-scale` | ossci | 39 | 0 | — | — | 7 | [8s](https://github.com/iree-org/iree/actions/runs/39774168875/job/119808891165) | [48s](https://github.com/iree-org/iree/actions/runs/39774168875/job/119808891343) | 0% (0/2) | 39 |
| `macos-15` | github-hosted | 21 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/39750599201/job/119730627472) | [41s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440413) | 0% (0/3) | 21 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/39774168875/job/119808890934) | [5s](https://github.com/iree-org/iree/actions/runs/39760386742/job/119762892711) | 0% (0/3) | 21 |
| `ubuntu-24.04` | github-hosted | 90 | 0 | — | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/39750057557/job/119729147662) | [3s](https://github.com/iree-org/iree/actions/runs/39750057557/job/119730465146) | 0% (0/11) | 88 |
| `ubuntu-latest` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39767303334/job/119785849442) | [3s](https://github.com/iree-org/iree/actions/runs/39767303334/job/119785849437) | 0% (0/3) | 18 |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/39750599201/job/119730627655) | [2s](https://github.com/iree-org/iree/actions/runs/39750057557/job/119729250837) | — | 6 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868156) | [1s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868156) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `fix-spirv-wide-elementwise` | pull_request |
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `fix-spirv-wide-elementwise` | pull_request |
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827580) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `fix-spirv-wide-elementwise` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827580) | 2026-10-19 06:26 PDT | [18m50s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868197) | [18m50s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868197) | [18m50s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868197) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | [8m08s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868364) | [8m08s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868364) | [8m08s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868364) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | [28m08s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868307) | [28m08s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868307) | [28m08s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868307) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [31m38s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868446) | [31m38s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868446) | [31m38s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868446) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [25m42s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868309) | [25m42s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868309) | [25m42s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868309) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [20m34s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868087) | [20m34s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868087) | [20m34s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868087) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [14m10s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868147) | [14m10s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868147) | [14m10s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868147) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [10m17s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868215) | [10m17s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868215) | [10m17s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868215) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [5m05s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868209) | [5m05s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868209) | [5m05s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119765868209) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m29s](https://github.com/iree-org/iree/actions/runs/39755698707/job/119747023132) | [1m29s](https://github.com/iree-org/iree/actions/runs/39755698707/job/119747023132) | [1m29s](https://github.com/iree-org/iree/actions/runs/39755698707/job/119747023132) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 6 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/39750057557/job/119729250310) | [1m22s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440833) | [1m22s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440833) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 6 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/39750057557/job/119729250746) | [1m14s](https://github.com/iree-org/iree/actions/runs/39749195617/job/119725579467) | [1m14s](https://github.com/iree-org/iree/actions/runs/39749195617/job/119725579467) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 6 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/39774168875/job/119808891165) | [1m13s](https://github.com/iree-org/iree/actions/runs/39749195617/job/119725579590) | [1m13s](https://github.com/iree-org/iree/actions/runs/39749195617/job/119725579590) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39750599201/job/119730627562) | [1m06s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440607) | [1m06s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440607) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39760386742/job/119762892725) | [54s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440445) | [54s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440445) | 6 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 6 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/39750599331/job/119730588142) | [45s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119762913000) | [45s](https://github.com/iree-org/iree/actions/runs/39760386375/job/119762913000) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 6 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/39750599201/job/119730627472) | [42s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440441) | [42s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440441) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 6 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/39774168875/job/119808891175) | [41s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440413) | [41s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440413) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 6 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440463) | [23s](https://github.com/iree-org/iree/actions/runs/39774168875/job/119808891246) | [23s](https://github.com/iree-org/iree/actions/runs/39774168875/job/119808891246) | 6 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 6 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/39742635363/job/119703440554) | [19s](https://github.com/iree-org/iree/actions/runs/39750057557/job/119729250434) | [19s](https://github.com/iree-org/iree/actions/runs/39750057557/job/119729250434) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 361 | 0% (0/361) |  | 1h12m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 308 | 2% (7/308) |  | 1h17m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
