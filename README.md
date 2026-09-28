# iree-ci-monitor

_Updated: 2026-09-28 07:04 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | — | 0 | [32m33s](https://github.com/iree-org/iree/actions/runs/36421209588/job/108934587034) | [2h14m](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823681) | 0% (0/6) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [23m02s](https://github.com/iree-org/iree/actions/runs/36399413356/job/108856595212) | [2h05m](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823711) | 0% (0/6) | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [39m34s](https://github.com/iree-org/iree/actions/runs/36394461539/job/108840220633) | [1h54m](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823556) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36421209588/job/108934587009) | [1h31m](https://github.com/iree-org/iree/actions/runs/36399413356/job/108856594925) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [42m02s](https://github.com/iree-org/iree/actions/runs/36402378243/job/108865433619) | [58m27s](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823704) | 0% (0/3) | `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [32m22s](https://github.com/iree-org/iree/actions/runs/36399413356/job/108856595307) | [58m14s](https://github.com/iree-org/iree/actions/runs/36402378243/job/108865433773) | 0% (0/3) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [22m31s](https://github.com/iree-org/iree/actions/runs/36421209588/job/108934587122) | [55m47s](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823679) | 0% (0/6) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [23m49s](https://github.com/iree-org/iree/actions/runs/36402378243/job/108865433732) | [38m47s](https://github.com/iree-org/iree/actions/runs/36399413356/job/108856594871) | 0% (0/6) | `shark55-ci`, `shark75-ci` |
| `azure-linux-scale` | ossci | 51 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/36402378105/job/108863107041) | [1m40s](https://github.com/iree-org/iree/actions/runs/36421209588/job/108924185751) | 5% (1/20) | 51 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m29s](https://github.com/iree-org/iree/actions/runs/36404802696/job/108870848744) | [1m29s](https://github.com/iree-org/iree/actions/runs/36404802696/job/108870848744) | 100% (1/1) | 1 |
| `windows-2022` | github-hosted | 26 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/36381304814/job/108797495769) | [48s](https://github.com/iree-org/iree/actions/runs/36399771807/job/108854676495) | 0% (0/9) | 26 |
| `macos-14` | github-hosted | 27 | 0 | — | — | 1 | [7s](https://github.com/iree-org/iree/actions/runs/36421209633/job/108924169467) | [10s](https://github.com/iree-org/iree/actions/runs/36389755441/job/108822834276) | 0% (0/9) | 27 |
| `ubuntu-24.04-arm` | github-hosted | 27 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/36421209633/job/108924169320) | [5s](https://github.com/iree-org/iree/actions/runs/36402378105/job/108863106904) | 0% (0/9) | 27 |
| `ubuntu-24.04` | github-hosted | 154 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/36399771807/job/108854676371) | [3s](https://github.com/iree-org/iree/actions/runs/36421209588/job/108956534320) | 0% (0/60) | 152 |
| `azure-windows-scale` | ossci | 8 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/36402378105/job/108863107416) | [3s](https://github.com/iree-org/iree/actions/runs/36389755441/job/108822834489) | 0% (0/3) | 8 |
| `ubuntu-latest` | github-hosted | 24 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/36389750130/job/108822744741) | [3s](https://github.com/iree-org/iree/actions/runs/36421208095/job/108924108178) | 0% (0/9) | 24 |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [1h09m](https://github.com/iree-org/iree/actions/runs/36402378243/job/108865433858) | [2h14m](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823681) | [2h14m](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823681) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [42m48s](https://github.com/iree-org/iree/actions/runs/36421209588/job/108934587414) | [2h05m](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823711) | [2h05m](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823711) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [4m21s](https://github.com/iree-org/iree/actions/runs/36390983793/job/108832411650) | [1h59m](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823777) | [1h59m](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823777) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [39m34s](https://github.com/iree-org/iree/actions/runs/36394461539/job/108840220633) | [1h54m](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823556) | [1h54m](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823556) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [30m49s](https://github.com/iree-org/iree/actions/runs/36394461539/job/108840220623) | [1h49m](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823641) | [1h49m](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823641) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36421209588/job/108934587009) | [1h31m](https://github.com/iree-org/iree/actions/runs/36399413356/job/108856594925) | [1h31m](https://github.com/iree-org/iree/actions/runs/36399413356/job/108856594925) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [23m49s](https://github.com/iree-org/iree/actions/runs/36402378243/job/108865433732) | [1h18m](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823412) | [1h18m](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823412) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [42m02s](https://github.com/iree-org/iree/actions/runs/36402378243/job/108865433619) | [58m27s](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823704) | [58m27s](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823704) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 6 | 0 | — | — | [32m22s](https://github.com/iree-org/iree/actions/runs/36399413356/job/108856595307) | [58m14s](https://github.com/iree-org/iree/actions/runs/36402378243/job/108865433773) | [58m14s](https://github.com/iree-org/iree/actions/runs/36402378243/job/108865433773) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [25m08s](https://github.com/iree-org/iree/actions/runs/36399413356/job/108856594698) | [55m47s](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823679) | [55m47s](https://github.com/iree-org/iree/actions/runs/36399771959/job/108857823679) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [19m25s](https://github.com/iree-org/iree/actions/runs/36394461539/job/108840220615) | [37m51s](https://github.com/iree-org/iree/actions/runs/36402378243/job/108865433825) | [37m51s](https://github.com/iree-org/iree/actions/runs/36402378243/job/108865433825) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [9m50s](https://github.com/iree-org/iree/actions/runs/36390983793/job/108832411421) | [29m12s](https://github.com/iree-org/iree/actions/runs/36402378243/job/108865433720) | [29m12s](https://github.com/iree-org/iree/actions/runs/36402378243/job/108865433720) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 8 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36402378105/job/108863107240) | [2m01s](https://github.com/iree-org/iree/actions/runs/36399413521/job/108853515447) | [2m01s](https://github.com/iree-org/iree/actions/runs/36399413521/job/108853515447) | 8 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 8 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36402378243/job/108863109541) | [2m00s](https://github.com/iree-org/iree/actions/runs/36399413356/job/108853520493) | [2m00s](https://github.com/iree-org/iree/actions/runs/36399413356/job/108853520493) | 8 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m29s](https://github.com/iree-org/iree/actions/runs/36404802696/job/108870848744) | [1m29s](https://github.com/iree-org/iree/actions/runs/36404802696/job/108870848744) | [1m29s](https://github.com/iree-org/iree/actions/runs/36404802696/job/108870848744) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 8 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36390983797/job/108827044207) | [1m28s](https://github.com/iree-org/iree/actions/runs/36421209633/job/108924169604) | [1m28s](https://github.com/iree-org/iree/actions/runs/36421209633/job/108924169604) | 8 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 8 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36421209633/job/108924169281) | [1m23s](https://github.com/iree-org/iree/actions/runs/36399771807/job/108854676581) | [1m23s](https://github.com/iree-org/iree/actions/runs/36399771807/job/108854676581) | 8 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 8 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36389957873/job/108823688698) | [1m06s](https://github.com/iree-org/iree/actions/runs/36421209633/job/108924169424) | [1m06s](https://github.com/iree-org/iree/actions/runs/36421209633/job/108924169424) | 8 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 8 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/36399413521/job/108853515341) | [1m01s](https://github.com/iree-org/iree/actions/runs/36389755441/job/108822834419) | [1m01s](https://github.com/iree-org/iree/actions/runs/36389755441/job/108822834419) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 8 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36390983797/job/108827044247) | [59s](https://github.com/iree-org/iree/actions/runs/36399771807/job/108854676833) | [59s](https://github.com/iree-org/iree/actions/runs/36399771807/job/108854676833) | 8 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 333 | 2% (5/333) |  | 18m34s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 248 | 4% (10/248) |  | 47m15s ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h14m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h54m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h31m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h05m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
