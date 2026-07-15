# iree-ci-monitor

_Updated: 2026-07-15 07:13 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [1m58s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274863) | [25m33s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132689) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [8m22s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274899) | [24m01s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132628) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [5m27s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274932) | [21m07s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132726) | — | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [9m24s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132861) | [18m07s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132913) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [12m42s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372275261) | [17m25s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132863) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [8m34s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372275205) | [15m59s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132850) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132687) | [10m17s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274956) | — | `shark01-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132703) | [6m40s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274928) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [4m42s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372275021) | [5m53s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132705) | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274934) | [3m28s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132721) | — | `shark10-ci`, `shark55-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m29s](https://github.com/iree-org/iree/actions/runs/29406218382/job/87322198988) | [1m29s](https://github.com/iree-org/iree/actions/runs/29406218382/job/87322198988) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 12 | 0 | — | — | 2 | [9s](https://github.com/iree-org/iree/actions/runs/29420096782/job/87370321265) | [47s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418196) | 0% (0/2) | 12 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355417973) | [5s](https://github.com/iree-org/iree/actions/runs/29420096782/job/87370320783) | — | 9 |
| `windows-2022` | github-hosted | 8 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418014) | [4s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418105) | — | 8 |
| `ubuntu-24.04` | github-hosted | 54 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29420096538/job/87370268172) | [3s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372275629) | 50% (3/6) | 54 |
| `macos-14` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29420096782/job/87370320499) | [3s](https://github.com/iree-org/iree/actions/runs/29420096782/job/87370320838) | 0% (0/1) | 9 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132649) | [3s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274880) | — | 2 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/29420096782/job/87370321215) | [2s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418372) | — | 2 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132691) | [2s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274988) | — | `iree-mi308-1` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132724) | [2s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372275023) | — | `shark10-ci` |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29412072655/job/87341270576) | [2s](https://github.com/iree-org/iree/actions/runs/29412072655/job/87341270583) | — | 3 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29406176816/job/87322065373) | [2s](https://github.com/iree-org/iree/actions/runs/29406176816/job/87322065373) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 0 | — | — | [1m58s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274863) | [25m33s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132689) | [25m33s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132689) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [8m22s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274899) | [24m01s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132628) | [24m01s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132628) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [5m27s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274932) | [21m07s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132726) | [21m07s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132726) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [3m26s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372275120) | [18m07s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132913) | [18m07s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132913) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [12m42s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372275261) | [17m25s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132863) | [17m25s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132863) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [8m34s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372275205) | [15m59s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132850) | [15m59s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132850) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132687) | [10m17s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274956) | [10m17s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274956) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274998) | [9m24s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132861) | [9m24s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132861) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [6m53s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132905) | [7m55s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274977) | [7m55s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274977) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132703) | [6m40s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274928) | [6m40s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274928) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274985) | [5m58s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357133131) | [5m58s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357133131) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [4m42s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372275021) | [5m53s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132705) | [5m53s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132705) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274934) | [3m28s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132721) | [3m28s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132721) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132727) | [1m33s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372275025) | [1m33s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372275025) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m29s](https://github.com/iree-org/iree/actions/runs/29406218382/job/87322198988) | [1m29s](https://github.com/iree-org/iree/actions/runs/29406218382/job/87322198988) | [1m29s](https://github.com/iree-org/iree/actions/runs/29406218382/job/87322198988) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29420096782/job/87370321159) | [1m07s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418149) | [1m07s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418149) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/29420096782/job/87370321997) | [47s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418196) | [47s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418196) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/29420096782/job/87370321185) | [42s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418161) | [42s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418161) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 2 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87370328228) | [19s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87355428100) | [19s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87355428100) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418038) | [9s](https://github.com/iree-org/iree/actions/runs/29420096782/job/87370321265) | [9s](https://github.com/iree-org/iree/actions/runs/29420096782/job/87370321265) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 154 | 1% (2/154) |  | 56s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 128 | 10% (13/128) |  | 1m43s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 130 | 1% (1/130) |  | 3m58s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 36 | 0% (0/36) |  | 6m44s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 114 | 1% (1/114) |  | 7m07s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
