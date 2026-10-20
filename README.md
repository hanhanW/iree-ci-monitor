# iree-ci-monitor

_Updated: 2026-10-19 21:56 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 4 | 2 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | 0 | [1s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290600977) | [20m56s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601234) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [16m12s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290602251) | [16m12s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290602251) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 3 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | 0 | [13m20s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601062) | [15m45s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290600928) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [14m14s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290600939) | [14m14s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290600939) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [2m42s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601061) | [8m22s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601037) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290600918) | [7m01s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601023) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [5m06s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601232) | [5m06s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601232) | 0% (0/1) | `shark75-ci` |
| `azure-linux-scale` | ossci | 7 | 0 | — | — | 0 | [30s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309368) | [1m25s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309214) | 0% (0/7) | 7 |
| `macos-15` | github-hosted | 3 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287308999) | [9s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287308886) | 0% (0/3) | 3 |
| `ubuntu-latest` | github-hosted | 4 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/39318806867/job/118287181358) | [8s](https://github.com/iree-org/iree/actions/runs/39318806867/job/118287181597) | 0% (0/4) | 4 |
| `ubuntu-24.04` | github-hosted | 26 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601214) | [8s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118287173364) | 5% (1/22) | 25 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287308972) | [4s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309199) | 0% (0/3) | 3 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287308927) | [2s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309237) | 0% (0/3) | 3 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309191) | [1s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309191) | 100% (1/1) | 1 |
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
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827580) | 2026-10-19 06:26 PDT | [1s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290600977) | [1s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290600977) | [1s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290600977) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | [15m45s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290600928) | [15m45s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290600928) | [15m45s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290600928) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | [20m56s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601234) | [20m56s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601234) | [20m56s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601234) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [16m12s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290602251) | [16m12s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290602251) | [16m12s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290602251) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [14m14s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290600939) | [14m14s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290600939) | [14m14s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290600939) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [13m20s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601062) | [13m20s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601062) | [13m20s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601062) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [8m22s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601037) | [8m22s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601037) | [8m22s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601037) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [7m01s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601023) | [7m01s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601023) | [7m01s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601023) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [5m06s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601232) | [5m06s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601232) | [5m06s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601232) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [2m42s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601061) | [2m42s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601061) | [2m42s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601061) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [1m25s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309214) | [1m25s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309214) | [1m25s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309214) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 1 | 0 | — | — | [1m03s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309442) | [1m03s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309442) | [1m03s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309442) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [42s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287308994) | [42s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287308994) | [42s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287308994) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [30s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309368) | [30s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309368) | [30s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309368) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [28s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309367) | [28s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309367) | [28s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309367) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [15s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309161) | [15s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309161) | [15s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309161) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287308886) | [9s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287308886) | [9s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287308886) | 1 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287173653) | [9s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287173653) | [9s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287173653) | 1 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118287173364) | [8s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118287173364) | [8s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118287173364) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/39318806867/job/118287181154) | [8s](https://github.com/iree-org/iree/actions/runs/39318806867/job/118287181154) | [8s](https://github.com/iree-org/iree/actions/runs/39318806867/job/118287181154) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 355 | 2% (6/355) |  | 8h04m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 303 | 1% (2/303) |  | 8h05m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
