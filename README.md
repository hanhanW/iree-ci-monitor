# iree-ci-monitor

_Updated: 2026-05-21 00:37 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [34m04s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922360) | [34m04s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922360) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926511) | 2026-05-19 06:28 PDT | 0 | [25m38s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922271) | [25m38s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922271) | — | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [18m27s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922308) | [18m27s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922308) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [6m15s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922440) | [17m29s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922307) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922303) | [13m49s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922419) | — | `shark01-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922315) | [13m32s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922389) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926441) | 2026-05-19 06:28 PDT | 0 | [11m05s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922426) | [11m05s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922426) | — | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922320) | [6m58s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922413) | — | `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [6m08s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922291) | [6m08s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922291) | — | `shark01-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [5m26s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922365) | [5m26s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922365) | — | `shark10-ci` |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [30s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295520) | [1m17s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295531) | — | 5 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922296) | [8s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922310) | — | 4 |
| `ubuntu-24.04` | github-hosted | 37 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922304) | [3s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922362) | 50% (3/6) | 37 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26209416097/job/77116552317) | [3s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295403) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295308) | [3s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295409) | — | 6 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295352) | [3s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295411) | — | 5 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922279) | [2s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922279) | — | 1 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922323) | [2s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922323) | — | `iree-mi308-1` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922348) | [2s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922348) | — | `shark55-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295518) | [1s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295518) | — | 1 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926441) | 2026-05-19 06:28 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `new-lds-promotion` | pull_request |
| [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926511) | 2026-05-19 06:28 PDT | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `new-lds-promotion` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [34m04s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922360) | [34m04s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922360) | [34m04s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922360) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926511) | 2026-05-19 06:28 PDT | [25m38s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922271) | [25m38s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922271) | [25m38s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922271) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926441) | 2026-05-19 06:28 PDT | [11m05s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922426) | [11m05s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922426) | [11m05s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922426) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [18m27s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922308) | [18m27s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922308) | [18m27s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922308) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [17m29s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922307) | [17m29s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922307) | [17m29s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922307) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [13m49s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922419) | [13m49s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922419) | [13m49s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922419) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [13m32s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922389) | [13m32s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922389) | [13m32s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922389) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [6m58s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922413) | [6m58s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922413) | [6m58s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922413) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [6m15s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922440) | [6m15s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922440) | [6m15s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922440) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [6m08s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922291) | [6m08s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922291) | [6m08s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922291) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [5m26s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922365) | [5m26s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922365) | [5m26s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922365) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [1m17s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295531) | [1m17s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295531) | [1m17s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295531) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [1m11s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295354) | [1m11s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295354) | [1m11s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295354) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [30s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295520) | [30s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295520) | [30s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295520) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [29s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295408) | [29s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295408) | [29s](https://github.com/iree-org/iree/actions/runs/26204802428/job/77102295408) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922282) | [8s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922282) | [8s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922282) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922310) | [8s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922310) | [8s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922310) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922296) | [8s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922296) | [8s](https://github.com/iree-org/iree/actions/runs/26204802480/job/77102922296) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/26207573017/job/77110676342) | [4s](https://github.com/iree-org/iree/actions/runs/26207573017/job/77110676342) | [4s](https://github.com/iree-org/iree/actions/runs/26207573017/job/77110676342) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26188574886/job/77093042819) | [3s](https://github.com/iree-org/iree/actions/runs/26186931962/job/77091823236) | [3s](https://github.com/iree-org/iree/actions/runs/26186931962/job/77091823236) | 5 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 558 | 2% (10/557) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 438 | 0% (1/437) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 457 | 1% (5/456) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 462 | 6% (28/461) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 140 | 1% (2/140) |  | 3h12m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
