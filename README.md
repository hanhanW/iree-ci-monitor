# iree-ci-monitor

_Updated: 2026-07-15 12:38 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 1 | [6m40s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274928) | [29m20s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036042) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [15m17s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035969) | [25m33s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132689) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [16m16s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035800) | [24m01s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132628) | — | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [5m58s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357133131) | [23m20s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036081) | — | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372275023) | [23m14s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035823) | — | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [10m17s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274956) | [21m30s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035979) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [5m27s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274932) | [21m07s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132726) | — | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [3m26s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372275120) | [18m07s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132913) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [7m55s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274977) | [15m59s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132850) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [4m42s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372275021) | [10m35s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035939) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035996) | [3m28s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132721) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m29s](https://github.com/iree-org/iree/actions/runs/29406218382/job/87322198988) | [1m29s](https://github.com/iree-org/iree/actions/runs/29406218382/job/87322198988) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 17 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/29420096782/job/87370321265) | [1m07s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418149) | 0% (0/2) | 17 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/29420096782/job/87370320756) | [6s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444891931) | — | 9 |
| `windows-2022` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29420096782/job/87370320866) | [4s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418105) | — | 9 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274880) | [4s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035842) | — | 3 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29424369191/job/87382862662) | [4s](https://github.com/iree-org/iree/actions/runs/29424369800/job/87382826166) | — | 9 |
| `ubuntu-24.04` | github-hosted | 67 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444891850) | [3s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036196) | 33% (1/3) | 67 |
| `macos-14` | github-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29420096782/job/87370320777) | [3s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892021) | 0% (0/1) | 10 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274988) | [3s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035904) | — | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892196) | [2s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418372) | — | 3 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29406176816/job/87322065373) | [2s](https://github.com/iree-org/iree/actions/runs/29406176816/job/87322065373) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [6m40s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274928) | [29m20s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036042) | [29m20s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036042) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [15m17s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035969) | [25m33s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132689) | [25m33s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132689) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [16m16s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035800) | [24m01s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132628) | [24m01s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132628) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [17m25s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132863) | [23m20s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036081) | [23m20s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036081) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372275023) | [23m14s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035823) | [23m14s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035823) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [10m17s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274956) | [21m30s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035979) | [21m30s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035979) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [5m27s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274932) | [21m07s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132726) | [21m07s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132726) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [3m26s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372275120) | [18m07s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132913) | [18m07s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132913) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [8m34s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372275205) | [15m59s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132850) | [15m59s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132850) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [7m55s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372274977) | [12m17s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036091) | [12m17s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036091) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [1m33s](https://github.com/iree-org/iree/actions/runs/29420096868/job/87372275025) | [10m35s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035939) | [10m35s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035939) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [4m42s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036183) | [9m24s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132861) | [9m24s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132861) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447036068) | [5m58s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357133131) | [5m58s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357133131) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [5m37s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035848) | [5m53s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132705) | [5m53s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132705) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87447035996) | [3m28s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132721) | [3m28s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87357132721) | 3 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m29s](https://github.com/iree-org/iree/actions/runs/29406218382/job/87322198988) | [1m29s](https://github.com/iree-org/iree/actions/runs/29406218382/job/87322198988) | [1m29s](https://github.com/iree-org/iree/actions/runs/29406218382/job/87322198988) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 3 | 0 | — | — | [19s](https://github.com/iree-org/iree/actions/runs/29412053749/job/87355428100) | [1m23s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87444894476) | [1m23s](https://github.com/iree-org/iree/actions/runs/29442410441/job/87444894476) | 3 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892101) | [1m07s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418149) | [1m07s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418149) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 3 | 0 | — | — | [14s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892136) | [47s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418196) | [47s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418196) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 3 | 0 | — | — | [15s](https://github.com/iree-org/iree/actions/runs/29442410397/job/87444892221) | [42s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418161) | [42s](https://github.com/iree-org/iree/actions/runs/29412053831/job/87355418161) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 159 | 1% (2/158) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 134 | 1% (1/134) |  | 2m29s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 132 | 10% (13/132) |  | 5m21s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 116 | 1% (1/116) |  | 17m19s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 37 | 0% (0/37) |  | 21m51s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
