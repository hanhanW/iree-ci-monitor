# iree-ci-monitor

_Updated: 2026-11-12 22:52 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 2 | 1 | [17m59s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733901072) | 2026-11-12 22:51 PST | 1 | [17m45s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900995) | [17m45s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900995) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 1 | [5m05s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900966) | [15m11s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733901038) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900933) | [8m48s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900936) | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [4m11s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733901063) | [4m11s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733901063) | — | `shark55-ci` |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 4 | [1m45s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730668080) | [1m52s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730667898) | — | 6 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730667814) | [1m20s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730667833) | — | 6 |
| `ubuntu-24.04` | github-hosted | 45 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730587490) | [3s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900745) | 0% (0/7) | 44 |
| `macos-15` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730667856) | [3s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730667885) | — | 5 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730667775) | [2s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730667870) | — | 5 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900747) | [2s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900747) | — | `shark75-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730668219) | [1s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730668219) | — | 1 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 2 | [17m59s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900904) | 2026-11-12 22:51 PST | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 1 | [17m59s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733901011) | 2026-11-12 22:51 PST | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [17m59s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900904) | 2026-11-12 22:51 PST | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | `fix-dispatch-fusion-operand-count` | pull_request |
| [17m59s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900913) | 2026-11-12 22:51 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | `fix-dispatch-fusion-operand-count` | pull_request |
| [17m59s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733901011) | 2026-11-12 22:51 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `fix-dispatch-fusion-operand-count` | pull_request |
| [17m59s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733901072) | 2026-11-12 22:51 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `fix-dispatch-fusion-operand-count` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 1 | [17m59s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733901011) | 2026-11-12 22:51 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 1 | [17m59s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900913) | 2026-11-12 22:51 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 1 | [17m59s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733901072) | 2026-11-12 22:51 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 1 | [17m59s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900904) | 2026-11-12 22:51 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [17m45s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900995) | [17m45s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900995) | [17m45s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900995) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [15m11s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733901038) | [15m11s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733901038) | [15m11s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733901038) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [8m48s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900936) | [8m48s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900936) | [8m48s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900936) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [5m05s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900966) | [5m05s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900966) | [5m05s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733900966) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [4m11s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733901063) | [4m11s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733901063) | [4m11s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131733901063) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [1m52s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730667898) | [1m52s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730667898) | [1m52s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730667898) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [1m51s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131730673068) | [1m51s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131730673068) | [1m51s](https://github.com/iree-org/iree/actions/runs/43378521370/job/131730673068) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [1m49s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730668058) | [1m49s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730668058) | [1m49s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730668058) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 1 | 0 | — | — | [1m45s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730668080) | [1m45s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730668080) | [1m45s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730668080) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [1m33s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730668158) | [1m33s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730668158) | [1m33s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730668158) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 1 | 0 | — | — | [1m29s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730667907) | [1m29s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730667907) | [1m29s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730667907) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1m20s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730667833) | [1m20s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730667833) | [1m20s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730667833) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/43370220770/job/131704071932) | [5s](https://github.com/iree-org/iree/actions/runs/43370220770/job/131704071932) | [5s](https://github.com/iree-org/iree/actions/runs/43370220770/job/131704071932) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/43370220770/job/131704072021) | [4s](https://github.com/iree-org/iree/actions/runs/43370220770/job/131704072021) | [4s](https://github.com/iree-org/iree/actions/runs/43370220770/job/131704072021) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/43370220770/job/131704072016) | [4s](https://github.com/iree-org/iree/actions/runs/43370220770/job/131704072016) | [4s](https://github.com/iree-org/iree/actions/runs/43370220770/job/131704072016) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730667814) | [4s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730667814) | [4s](https://github.com/iree-org/iree/actions/runs/43378521333/job/131730667814) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 360 | 1% (2/359) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 297 | 1% (2/296) | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
