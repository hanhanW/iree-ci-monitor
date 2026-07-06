# iree-ci-monitor

_Updated: 2026-07-06 00:53 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 1 | [36m01s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452062) | 2026-07-06 00:52 PDT | 1 | [25m08s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452101) | [25m08s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452101) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [19m33s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315451903) | [19m33s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315451903) | — | `shark01-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [17m02s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315451896) | [17m02s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315451896) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [11m00s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452120) | [16m11s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452032) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [13m02s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452023) | [13m02s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452023) | — | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [6m27s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452000) | [9m21s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452035) | — | `shark55-ci`, `shark75-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [34s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452029) | [9m09s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452558) | — | 4 |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452140) | [6m26s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452031) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [5m24s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452107) | [5m24s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452107) | — | `shark10-ci` |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/28772614240/job/85309371674) | [1m23s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314052957) | — | 6 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/28772614240/job/85309371676) | [1m22s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314052990) | — | 5 |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [1m04s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314053041) | [1m19s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85314061573) | — | 5 |
| `ubuntu-24.04` | github-hosted | 36 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314052991) | [3s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314052922) | 50% (2/4) | 34 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314052976) | [3s](https://github.com/iree-org/iree/actions/runs/28772614240/job/85309371684) | — | 5 |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315451984) | [1s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315451984) | — | `shark01-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452028) | [1s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452028) | — | `iree-mi308-1` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452126) | [1s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452126) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452156) | [1s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452156) | — | `shark10-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314053107) | [1s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314053107) | — | 1 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [36m01s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452062) | 2026-07-06 00:52 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `change-to-tosa-level-none` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 1 | [36m01s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452062) | 2026-07-06 00:52 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [25m08s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452101) | [25m08s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452101) | [25m08s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452101) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [19m33s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315451903) | [19m33s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315451903) | [19m33s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315451903) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [17m02s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315451896) | [17m02s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315451896) | [17m02s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315451896) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [16m11s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452032) | [16m11s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452032) | [16m11s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452032) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [13m02s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452023) | [13m02s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452023) | [13m02s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452023) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [11m00s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452120) | [11m00s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452120) | [11m00s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452120) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [9m21s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452035) | [9m21s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452035) | [9m21s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452035) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [9m09s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452558) | [9m09s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452558) | [9m09s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452558) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [6m27s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452000) | [6m27s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452000) | [6m27s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452000) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [6m26s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452031) | [6m26s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452031) | [6m26s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452031) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [5m24s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452107) | [5m24s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452107) | [5m24s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452107) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1m23s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314052957) | [1m23s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314052957) | [1m23s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314052957) | 1 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 1 | 0 | — | — | [1m22s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314052990) | [1m22s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314052990) | [1m22s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314052990) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1m20s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314052982) | [1m20s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314052982) | [1m20s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314052982) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [1m19s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85314061573) | [1m19s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85314061573) | [1m19s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85314061573) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [1m12s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314053098) | [1m12s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314053098) | [1m12s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314053098) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [1m04s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314053041) | [1m04s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314053041) | [1m04s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314053041) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [34s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452029) | [34s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452029) | [34s](https://github.com/iree-org/iree/actions/runs/28774097115/job/85315452029) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [21s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314053027) | [21s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314053027) | [21s](https://github.com/iree-org/iree/actions/runs/28774097086/job/85314053027) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 279 | 3% (7/278) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 198 | 2% (3/198) |  | 7m59s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 219 | 1% (3/219) |  | 13m22s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 252 | 8% (19/252) |  | 13m45s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 66 | 2% (1/66) |  | 25m27s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
