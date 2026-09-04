# iree-ci-monitor

_Updated: 2026-09-04 09:25 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [11m07s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742566) | [34m24s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994356) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [23m19s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742352) | [26m25s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994141) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [16m57s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742351) | [22m12s](https://github.com/iree-org/iree/actions/runs/33849939944/job/100952463546) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [11m04s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742181) | [21m47s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994232) | 0% (0/2) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [5m19s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994439) | [20m25s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742486) | 0% (0/4) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [5m34s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742252) | [17m39s](https://github.com/iree-org/iree/actions/runs/33849939944/job/100952463592) | 0% (0/4) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [13m52s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742368) | [17m19s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994625) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [4m57s](https://github.com/iree-org/iree/actions/runs/33849939944/job/100952463722) | [16m21s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994308) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [13m53s](https://github.com/iree-org/iree/actions/runs/33849939944/job/100952463475) | [16m10s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742172) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [5m58s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994251) | [14m40s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742409) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [5m14s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994430) | [6m40s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742347) | 0% (0/2) | `shark01-ci` |
| `azure-linux-scale` | ossci | 19 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/33860609319/job/100983979171) | [2m49s](https://github.com/iree-org/iree/actions/runs/33860609319/job/100983978991) | 7% (1/14) | 19 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m26s](https://github.com/iree-org/iree/actions/runs/33858388237/job/100976880518) | [1m26s](https://github.com/iree-org/iree/actions/runs/33858388237/job/100976880518) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33860609319/job/100983978918) | [1m18s](https://github.com/iree-org/iree/actions/runs/33849939917/job/100950255121) | 0% (0/6) | 9 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/33860609319/job/100983979003) | [1m05s](https://github.com/iree-org/iree/actions/runs/33849939917/job/100950254945) | 0% (0/6) | 9 |
| `ubuntu-24.04` | github-hosted | 69 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33860609319/job/100983978881) | [10s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994328) | 5% (2/43) | 68 |
| `macos-14` | github-hosted | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33857302137/job/100974051007) | [8s](https://github.com/iree-org/iree/actions/runs/33860609319/job/100983978992) | 0% (0/7) | 10 |
| `ubuntu-latest` | github-hosted | 28 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33865516692/job/100999359137) | [3s](https://github.com/iree-org/iree/actions/runs/33882127017/job/101053057502) | 0% (0/7) | 28 |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/33857302137/job/100974051097) | [1s](https://github.com/iree-org/iree/actions/runs/33860609319/job/100983979032) | 0% (0/2) | 3 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 3 | 0 | — | — | [1m24s](https://github.com/iree-org/iree/actions/runs/33849939944/job/100950263067) | [41m21s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100983994793) | [41m21s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100983994793) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [17m21s](https://github.com/iree-org/iree/actions/runs/33849939944/job/100952463707) | [34m24s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994356) | [34m24s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994356) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [23m19s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742352) | [26m25s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994141) | [26m25s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994141) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [16m57s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742351) | [22m12s](https://github.com/iree-org/iree/actions/runs/33849939944/job/100952463546) | [22m12s](https://github.com/iree-org/iree/actions/runs/33849939944/job/100952463546) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [11m04s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742181) | [21m47s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994232) | [21m47s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994232) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [5m19s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994439) | [20m25s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742486) | [20m25s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742486) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [5m27s](https://github.com/iree-org/iree/actions/runs/33849939944/job/100952463951) | [19m53s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742313) | [19m53s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742313) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [6m36s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994272) | [17m39s](https://github.com/iree-org/iree/actions/runs/33849939944/job/100952463592) | [17m39s](https://github.com/iree-org/iree/actions/runs/33849939944/job/100952463592) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [13m52s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742368) | [17m19s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994625) | [17m19s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994625) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [4m57s](https://github.com/iree-org/iree/actions/runs/33849939944/job/100952463722) | [16m21s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994308) | [16m21s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994308) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [13m53s](https://github.com/iree-org/iree/actions/runs/33849939944/job/100952463475) | [16m10s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742172) | [16m10s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742172) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742187) | [15m27s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994317) | [15m27s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994317) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [11m34s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994394) | [14m40s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742409) | [14m40s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742409) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [5m58s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994251) | [13m41s](https://github.com/iree-org/iree/actions/runs/33849939944/job/100952463544) | [13m41s](https://github.com/iree-org/iree/actions/runs/33849939944/job/100952463544) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742614) | [12m13s](https://github.com/iree-org/iree/actions/runs/33849939944/job/100952463736) | [12m13s](https://github.com/iree-org/iree/actions/runs/33849939944/job/100952463736) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [5m14s](https://github.com/iree-org/iree/actions/runs/33860609299/job/100996994430) | [6m40s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742347) | [6m40s](https://github.com/iree-org/iree/actions/runs/33857302257/job/100976742347) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 3 | 0 | — | — | [1m39s](https://github.com/iree-org/iree/actions/runs/33857302137/job/100974051134) | [2m49s](https://github.com/iree-org/iree/actions/runs/33860609319/job/100983978991) | [2m49s](https://github.com/iree-org/iree/actions/runs/33860609319/job/100983978991) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 3 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/33860609319/job/100983979119) | [1m26s](https://github.com/iree-org/iree/actions/runs/33849939917/job/100950255266) | [1m26s](https://github.com/iree-org/iree/actions/runs/33849939917/job/100950255266) | 3 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m26s](https://github.com/iree-org/iree/actions/runs/33858388237/job/100976880518) | [1m26s](https://github.com/iree-org/iree/actions/runs/33858388237/job/100976880518) | [1m26s](https://github.com/iree-org/iree/actions/runs/33858388237/job/100976880518) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33860609319/job/100983978939) | [1m23s](https://github.com/iree-org/iree/actions/runs/33849939917/job/100950255197) | [1m23s](https://github.com/iree-org/iree/actions/runs/33849939917/job/100950255197) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 213 | 1% (2/213) |  | 5h00m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 177 | 4% (7/177) |  | 5h12m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 155 | 1% (1/155) |  | 5h15m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 141 | 0% (0/141) |  | 5h23m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
