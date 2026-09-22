# iree-ci-monitor

_Updated: 2026-09-21 22:04 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [42m47s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241297) | [1h15m](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241091) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [9m32s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444415) | [1h03m](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477240767) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [26m58s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241375) | [1h00m](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241013) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [38m34s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241062) | [45m21s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241314) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [18m10s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444562) | [34m23s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477240982) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [19m45s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444628) | [23m09s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241237) | 100% (1/1) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [3m14s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241093) | [19m19s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444682) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477240961) | [17m50s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444661) | 0% (0/1) | `shark75-ci` |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531013001) | [9s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531013152) | — | 3 |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531013092) | [7s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531013122) | — | 5 |
| `ubuntu-24.04` | github-hosted | 40 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477240972) | [5s](https://github.com/iree-org/iree/actions/runs/35677015002/job/106585536425) | 6% (1/17) | 39 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531012938) | [5s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531013044) | — | 3 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531012969) | [2s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531013003) | — | 3 |
| `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35658724365/job/106528614688) | [2s](https://github.com/iree-org/iree/actions/runs/35658724365/job/106528614688) | 0% (0/1) | 1 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531013133) | [1s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531013133) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 1 | [19h41m](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438335) | 2026-09-21 22:03 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 1 | [19h41m](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438527) | 2026-09-21 22:03 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [19h41m](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438335) | 2026-09-21 22:03 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `users/ziereis/qdq-integer-contractions` | pull_request |
| [19h41m](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438527) | 2026-09-21 22:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/ziereis/qdq-integer-contractions` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 1 | [19h41m](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438335) | 2026-09-21 22:03 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 1 | [19h41m](https://github.com/iree-org/iree/actions/runs/35581982869/job/106279438527) | 2026-09-21 22:03 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [7m21s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444569) | [1h15m](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241091) | [1h15m](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241091) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [9m32s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444415) | [1h03m](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477240767) | [1h03m](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477240767) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444643) | [1h00m](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241013) | [1h00m](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241013) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [16m39s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444640) | [45m21s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241314) | [45m21s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241314) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [21m59s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444672) | [42m47s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241297) | [42m47s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241297) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [21m08s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444741) | [38m34s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241062) | [38m34s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241062) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [18m10s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444562) | [34m23s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477240982) | [34m23s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477240982) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [21m09s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444762) | [26m58s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241375) | [26m58s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241375) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 2 | 0 | — | — | [19m45s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444628) | [23m09s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241237) | [23m09s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241237) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477240965) | [19m19s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444682) | [19m19s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444682) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477240961) | [17m50s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444661) | [17m50s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444661) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444665) | [3m14s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241093) | [3m14s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241093) | 2 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 2 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444410) | [58s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241267) | [58s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241267) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 2 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/35659448436/job/106533444735) | [26s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241019) | [26s](https://github.com/iree-org/iree/actions/runs/35642312119/job/106477241019) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531013152) | [9s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531013152) | [9s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531013152) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531013001) | [9s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531013001) | [9s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531013001) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531012892) | [8s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531012892) | [8s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531012892) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531013122) | [7s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531013122) | [7s](https://github.com/iree-org/iree/actions/runs/35659448491/job/106531013122) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 353 | 1% (3/353) |  | 6h37m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 325 | 1% (2/325) |  | 6h42m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 214 | 1% (3/214) |  | 4d07h ago |

## Alerts

- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job observed waiting 19h41m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job observed waiting 19h41m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h15m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h03m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h00m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-w7900` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
