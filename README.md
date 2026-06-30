# iree-ci-monitor

_Updated: 2026-06-30 00:37 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [20m02s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750976) | [30m42s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229751021) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [3m45s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531069) | [17m28s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750955) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [12m11s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531068) | [16m18s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750910) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [4m56s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531099) | [14m19s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750926) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750903) | [11m16s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531086) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [7m05s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531101) | [10m22s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750938) | — | `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750987) | [8m59s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750944) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [7m34s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531088) | [8m54s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531118) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [4m49s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750923) | [8m53s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531106) | — | `shark01-ci`, `shark10-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | — | 0 | [1m06s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531154) | [2m53s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229751031) | — | 8 |
| `azure-linux-scale` | ossci | 12 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265394) | [2m05s](https://github.com/iree-org/iree/actions/runs/28422172141/job/84228785862) | — | 12 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m20s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265100) | [1m20s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265100) | — | 1 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/28422172141/job/84228785769) | [1m17s](https://github.com/iree-org/iree/actions/runs/28422172141/job/84228785738) | — | 9 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265343) | [5s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265343) | — | 1 |
| `ubuntu-24.04` | github-hosted | 51 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750864) | [4s](https://github.com/iree-org/iree/actions/runs/28422172141/job/84234732662) | 50% (2/4) | 51 |
| `windows-2022` | github-hosted | 8 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28422172141/job/84228785772) | [3s](https://github.com/iree-org/iree/actions/runs/28425015458/job/84226074982) | — | 8 |
| `macos-14` | github-hosted | 9 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/28425015458/job/84226074974) | [3s](https://github.com/iree-org/iree/actions/runs/28425015458/job/84226074958) | — | 9 |
| `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28404603415/job/84164070978) | [3s](https://github.com/iree-org/iree/actions/runs/28404602848/job/84164069541) | 0% (0/2) | 2 |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750836) | [2s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166530955) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750861) | [2s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166530971) | — | `shark01-ci`, `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750962) | [2s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531061) | — | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265434) | [1s](https://github.com/iree-org/iree/actions/runs/28422172141/job/84228785934) | — | 2 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 1 | [23h43m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002334980) | 2026-06-30 00:37 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [23h43m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002334980) | 2026-06-30 00:37 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `implement-fpowi-in-vm` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 1 | 1 | [23h43m](https://github.com/iree-org/iree/actions/runs/28353471331/job/84002334980) | 2026-06-30 00:37 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [3m40s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531087) | [30m42s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229751021) | [30m42s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229751021) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [7m28s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531136) | [20m02s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750976) | [20m02s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750976) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [3m45s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531069) | [17m28s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750955) | [17m28s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750955) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [12m11s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531068) | [16m18s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750910) | [16m18s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750910) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [4m56s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531099) | [14m19s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750926) | [14m19s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750926) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750903) | [11m16s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531086) | [11m16s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531086) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [7m05s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531101) | [10m22s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750938) | [10m22s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750938) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531093) | [8m59s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750944) | [8m59s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750944) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [7m27s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750928) | [8m54s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531118) | [8m54s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531118) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [4m49s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750923) | [8m53s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531106) | [8m53s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531106) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [5m05s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750999) | [7m34s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531088) | [7m34s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531088) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [1m43s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531045) | [5m55s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750933) | [5m55s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750933) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531095) | [2m53s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229751031) | [2m53s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229751031) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265218) | [2m06s](https://github.com/iree-org/iree/actions/runs/28422172141/job/84228785885) | [2m06s](https://github.com/iree-org/iree/actions/runs/28422172141/job/84228785885) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265242) | [2m05s](https://github.com/iree-org/iree/actions/runs/28422172141/job/84228785862) | [2m05s](https://github.com/iree-org/iree/actions/runs/28422172141/job/84228785862) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265241) | [2m04s](https://github.com/iree-org/iree/actions/runs/28422172141/job/84228785857) | [2m04s](https://github.com/iree-org/iree/actions/runs/28422172141/job/84228785857) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 0 | — | — | [57s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750935) | [2m01s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531052) | [2m01s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531052) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 0 | — | — | [1m06s](https://github.com/iree-org/iree/actions/runs/28404964046/job/84166531154) | [1m29s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750963) | [1m29s](https://github.com/iree-org/iree/actions/runs/28422172163/job/84229750963) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28404964078/job/84165265164) | [1m27s](https://github.com/iree-org/iree/actions/runs/28422172141/job/84228785703) | [1m27s](https://github.com/iree-org/iree/actions/runs/28422172141/job/84228785703) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 187 | 0% (0/187) |  | 4m27s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 143 | 0% (0/143) |  | 17m23s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 148 | 7% (11/148) |  | 20m09s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 144 | 0% (0/144) |  | 21m48s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 42 | 0% (0/42) |  | 30m18s ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 23h43m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
