# iree-ci-monitor

_Updated: 2026-09-30 15:22 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 18 | 0 | — | — | 0 | [3h43m](https://github.com/iree-org/iree/actions/runs/36744576359/job/109991533868) | [5h53m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603821) | — | `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [1h07m](https://github.com/iree-org/iree/actions/runs/36737467639/job/109966848280) | [5h09m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603685) | — | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 18 | 0 | — | — | 0 | [1h51m](https://github.com/iree-org/iree/actions/runs/36741548409/job/109980387208) | [5h00m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603700) | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [17m05s](https://github.com/iree-org/iree/actions/runs/36744576359/job/109991533930) | [4h46m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603795) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 18 | 0 | — | — | 0 | [1h49m](https://github.com/iree-org/iree/actions/runs/36744576359/job/109991534234) | [3h07m](https://github.com/iree-org/iree/actions/runs/36737467639/job/109966848390) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 18 | 0 | — | — | 0 | [33m09s](https://github.com/iree-org/iree/actions/runs/36714204474/job/109886366256) | [3h00m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603744) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [2h26m](https://github.com/iree-org/iree/actions/runs/36737467639/job/109966848362) | [2h31m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603679) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 9 | 0 | — | — | 0 | [22m19s](https://github.com/iree-org/iree/actions/runs/36744576359/job/109991533698) | [1h06m](https://github.com/iree-org/iree/actions/runs/36737467639/job/109966847952) | — | `shark75-ci` |
| `azure-linux-scale` | ossci | 70 | 1 | [5h48m](https://github.com/iree-org/iree/actions/runs/36744576058/job/109988469732) | 2026-09-30 15:20 PDT | 0 | [1m00s](https://github.com/iree-org/iree/actions/runs/36742836369/job/109983637942) | [10m10s](https://github.com/iree-org/iree/actions/runs/36714189625/job/109884721317) | — | 56 |
| `ubuntu-24.04` | github-hosted | 250 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/36741548524/job/109977026804) | [2m52s](https://github.com/iree-org/iree/actions/runs/36702830424/job/109912483999) | 0% (0/3) | 235 |
| `macos-14` | github-hosted | 42 | 0 | — | — | 0 | [11s](https://github.com/iree-org/iree/actions/runs/36736581970/job/109960539477) | [2m48s](https://github.com/iree-org/iree/actions/runs/36744576058/job/109988470018) | — | 39 |
| `ubuntu-24.04-arm` | github-hosted | 42 | 0 | — | — | 0 | [24s](https://github.com/iree-org/iree/actions/runs/36738886967/job/109968550795) | [2m39s](https://github.com/iree-org/iree/actions/runs/36715547504/job/109888419445) | — | 39 |
| `windows-2022` | github-hosted | 42 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/36742836369/job/109983637323) | [2m01s](https://github.com/iree-org/iree/actions/runs/36714204481/job/109883434257) | — | 40 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [23s](https://github.com/iree-org/iree/actions/runs/36736573899/job/109959730589) | [1m03s](https://github.com/iree-org/iree/actions/runs/36714199478/job/109883511689) | — | 12 |
| `azure-windows-scale` | ossci | 14 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36715547504/job/109888419361) | [3s](https://github.com/iree-org/iree/actions/runs/36737467666/job/109963682213) | — | 14 |
| `Linux,X64,iree-w7900` | self-hosted | 9 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [5h48m](https://github.com/iree-org/iree/actions/runs/36744576058/job/109988469732) | 2026-09-30 15:20 PDT | `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | `users/ziereis/qdq-reshape-propagation` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 9 | 0 | — | — | [3h41m](https://github.com/iree-org/iree/actions/runs/36741548409/job/109980387717) | [5h53m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603821) | [5h53m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603821) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 14 | 1 | [5h48m](https://github.com/iree-org/iree/actions/runs/36744576058/job/109988469732) | 2026-09-30 15:20 PDT | [9s](https://github.com/iree-org/iree/actions/runs/36736581970/job/109960539497) | [7m37s](https://github.com/iree-org/iree/actions/runs/36740427565/job/109973852554) | [7m37s](https://github.com/iree-org/iree/actions/runs/36740427565/job/109973852554) | 10 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 9 | 0 | — | — | [1h07m](https://github.com/iree-org/iree/actions/runs/36737467639/job/109966848280) | [5h09m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603685) | [5h09m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603685) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [46m38s](https://github.com/iree-org/iree/actions/runs/36744576359/job/109991534351) | [5h00m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603700) | [5h00m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603700) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 9 | 0 | — | — | [17m05s](https://github.com/iree-org/iree/actions/runs/36744576359/job/109991533930) | [4h46m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603795) | [4h46m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603795) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 9 | 0 | — | — | [3h47m](https://github.com/iree-org/iree/actions/runs/36737467639/job/109966848459) | [4h05m](https://github.com/iree-org/iree/actions/runs/36741548409/job/109980387213) | [4h05m](https://github.com/iree-org/iree/actions/runs/36741548409/job/109980387213) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [2h27m](https://github.com/iree-org/iree/actions/runs/36741548409/job/109980387442) | [3h07m](https://github.com/iree-org/iree/actions/runs/36737467639/job/109966848390) | [3h07m](https://github.com/iree-org/iree/actions/runs/36737467639/job/109966848390) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [1h00m](https://github.com/iree-org/iree/actions/runs/36744576359/job/109991533650) | [3h00m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603744) | [3h00m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603744) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 9 | 0 | — | — | [2h26m](https://github.com/iree-org/iree/actions/runs/36737467639/job/109966848362) | [2h31m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603679) | [2h31m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603679) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [1h52m](https://github.com/iree-org/iree/actions/runs/36744576359/job/109991533889) | [2h05m](https://github.com/iree-org/iree/actions/runs/36737467639/job/109966848533) | [2h05m](https://github.com/iree-org/iree/actions/runs/36737467639/job/109966848533) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [1h49m](https://github.com/iree-org/iree/actions/runs/36744576359/job/109991534234) | [2h00m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603577) | [2h00m](https://github.com/iree-org/iree/actions/runs/36714189625/job/109891603577) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [33m09s](https://github.com/iree-org/iree/actions/runs/36714204474/job/109886366256) | [1h09m](https://github.com/iree-org/iree/actions/runs/36714178175/job/109886208792) | [1h09m](https://github.com/iree-org/iree/actions/runs/36714178175/job/109886208792) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 9 | 0 | — | — | [22m19s](https://github.com/iree-org/iree/actions/runs/36744576359/job/109991533698) | [1h06m](https://github.com/iree-org/iree/actions/runs/36737467639/job/109966847952) | [1h06m](https://github.com/iree-org/iree/actions/runs/36737467639/job/109966847952) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 14 | 0 | — | — | [2m08s](https://github.com/iree-org/iree/actions/runs/36744576058/job/109988469595) | [20m18s](https://github.com/iree-org/iree/actions/runs/36715547504/job/109888419342) | [20m18s](https://github.com/iree-org/iree/actions/runs/36715547504/job/109888419342) | 11 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 14 | 0 | — | — | [1m07s](https://github.com/iree-org/iree/actions/runs/36743742092/job/109985099468) | [7m37s](https://github.com/iree-org/iree/actions/runs/36740427565/job/109973852990) | [12m36s](https://github.com/iree-org/iree/actions/runs/36741548524/job/109977026532) | 12 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | 9 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36744576359/job/109991534391) | [5m07s](https://github.com/iree-org/iree/actions/runs/36714204474/job/109886366411) | [5m07s](https://github.com/iree-org/iree/actions/runs/36714204474/job/109886366411) | 8 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 9 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36737467639/job/109966848127) | [4m53s](https://github.com/iree-org/iree/actions/runs/36714204474/job/109886366293) | [4m53s](https://github.com/iree-org/iree/actions/runs/36714204474/job/109886366293) | 8 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64-baremetal | `ubuntu-24.04` | 9 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36714178175/job/109886209162) | [4m47s](https://github.com/iree-org/iree/actions/runs/36714204474/job/109886366071) | [4m47s](https://github.com/iree-org/iree/actions/runs/36714204474/job/109886366071) | 9 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | 9 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36744576359/job/109991534214) | [4m04s](https://github.com/iree-org/iree/actions/runs/36714204474/job/109886366381) | [4m04s](https://github.com/iree-org/iree/actions/runs/36714204474/job/109886366381) | 9 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 9 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36737467639/job/109966847994) | [3m55s](https://github.com/iree-org/iree/actions/runs/36714204474/job/109886366061) | [3m55s](https://github.com/iree-org/iree/actions/runs/36714204474/job/109886366061) | 8 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 439 | 1% (4/439) |  | 1h51m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 338 | 4% (12/338) |  | 3h26m ago |

## Alerts

- **[stale-queued]** `azure-linux-scale` oldest queued job observed waiting 5h48m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 4h46m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 5h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h31m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 3h07m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache` p95 queue 5h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 5h53m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 3h00m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
