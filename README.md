# iree-ci-monitor

_Updated: 2026-09-03 14:05 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [7m56s](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252196) | [1h21m](https://github.com/iree-org/iree/actions/runs/33758278663/job/100661130993) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [35m10s](https://github.com/iree-org/iree/actions/runs/33748202390/job/100627747866) | [1h05m](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252233) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [23m58s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476175) | [59m03s](https://github.com/iree-org/iree/actions/runs/33758278663/job/100661131325) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | [6m43s](https://github.com/iree-org/iree/actions/runs/33751321379/job/100638003454) | [36m26s](https://github.com/iree-org/iree/actions/runs/33758278663/job/100661130918) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [10m46s](https://github.com/iree-org/iree/actions/runs/33766944727/job/100691704064) | [28m54s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476196) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 6 | 0 | — | — | 0 | [19m05s](https://github.com/iree-org/iree/actions/runs/33751321379/job/100638003503) | [26m42s](https://github.com/iree-org/iree/actions/runs/33748202390/job/100627747838) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [6m26s](https://github.com/iree-org/iree/actions/runs/33758278663/job/100661130912) | [22m34s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476326) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 6 | 0 | — | — | 0 | [7m09s](https://github.com/iree-org/iree/actions/runs/33766944727/job/100691703682) | [22m14s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476462) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | — | 0 | [10m48s](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252267) | [18m45s](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252626) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [4m26s](https://github.com/iree-org/iree/actions/runs/33758278663/job/100661130839) | [14m28s](https://github.com/iree-org/iree/actions/runs/33751321379/job/100638003685) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [5m20s](https://github.com/iree-org/iree/actions/runs/33751321379/job/100638003544) | [8m25s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476335) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 36 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/33766944727/job/100688799709) | [2m52s](https://github.com/iree-org/iree/actions/runs/33758667503/job/100659341560) | 0% (0/13) | 36 |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/33766944749/job/100687208673) | [1m19s](https://github.com/iree-org/iree/actions/runs/33758667370/job/100659304717) | 0% (0/6) | 18 |
| `macos-14` | github-hosted | 18 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/33766944749/job/100687208740) | [56s](https://github.com/iree-org/iree/actions/runs/33758667370/job/100659304683) | 0% (0/6) | 18 |
| `ubuntu-24.04` | github-hosted | 129 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33766944727/job/100691703660) | [10s](https://github.com/iree-org/iree/actions/runs/33748202390/job/100627747886) | 2% (1/40) | 129 |
| `windows-2022` | github-hosted | 18 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/33758667370/job/100659304785) | [5s](https://github.com/iree-org/iree/actions/runs/33748202197/job/100626318510) | 0% (0/6) | 18 |
| `ubuntu-latest` | github-hosted | 21 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/33748281225/job/100625792353) | [4s](https://github.com/iree-org/iree/actions/runs/33766943379/job/100687137583) | 0% (0/6) | 21 |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/33766944749/job/100687209247) | [2s](https://github.com/iree-org/iree/actions/runs/33760490301/job/100665364408) | 0% (0/2) | 6 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [7m56s](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252196) | [1h21m](https://github.com/iree-org/iree/actions/runs/33758278663/job/100661130993) | [1h21m](https://github.com/iree-org/iree/actions/runs/33758278663/job/100661130993) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [35m10s](https://github.com/iree-org/iree/actions/runs/33748202390/job/100627747866) | [1h05m](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252233) | [1h05m](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252233) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [39m01s](https://github.com/iree-org/iree/actions/runs/33751321379/job/100638003532) | [1h01m](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252522) | [1h01m](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252522) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 6 | 0 | — | — | [6m43s](https://github.com/iree-org/iree/actions/runs/33751321379/job/100638003454) | [36m26s](https://github.com/iree-org/iree/actions/runs/33758278663/job/100661130918) | [36m26s](https://github.com/iree-org/iree/actions/runs/33758278663/job/100661130918) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 6 | 0 | — | — | [10m46s](https://github.com/iree-org/iree/actions/runs/33766944727/job/100691704064) | [28m54s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476196) | [28m54s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476196) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [10m06s](https://github.com/iree-org/iree/actions/runs/33748202390/job/100627747840) | [27m10s](https://github.com/iree-org/iree/actions/runs/33751321379/job/100638003586) | [27m10s](https://github.com/iree-org/iree/actions/runs/33751321379/job/100638003586) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 6 | 0 | — | — | [19m05s](https://github.com/iree-org/iree/actions/runs/33751321379/job/100638003503) | [26m42s](https://github.com/iree-org/iree/actions/runs/33748202390/job/100627747838) | [26m42s](https://github.com/iree-org/iree/actions/runs/33748202390/job/100627747838) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [10m00s](https://github.com/iree-org/iree/actions/runs/33748202390/job/100627747690) | [24m28s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476370) | [24m28s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476370) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [6m26s](https://github.com/iree-org/iree/actions/runs/33758278663/job/100661130912) | [22m34s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476326) | [22m34s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476326) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 6 | 0 | — | — | [7m09s](https://github.com/iree-org/iree/actions/runs/33766944727/job/100691703682) | [22m14s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476462) | [22m14s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476462) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [3m45s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476173) | [21m20s](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252501) | [21m20s](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252501) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33758278663/job/100661131166) | [16m48s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476385) | [16m48s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476385) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [7m51s](https://github.com/iree-org/iree/actions/runs/33766944727/job/100691703999) | [14m59s](https://github.com/iree-org/iree/actions/runs/33748202390/job/100627747808) | [14m59s](https://github.com/iree-org/iree/actions/runs/33748202390/job/100627747808) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [1m49s](https://github.com/iree-org/iree/actions/runs/33758667503/job/100667252248) | [13m41s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476113) | [13m41s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476113) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [5m41s](https://github.com/iree-org/iree/actions/runs/33748202390/job/100627747864) | [8m25s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476335) | [8m25s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100674476335) | 2 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 6 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/33766944749/job/100687208928) | [7m04s](https://github.com/iree-org/iree/actions/runs/33760490301/job/100665364235) | [7m04s](https://github.com/iree-org/iree/actions/runs/33760490301/job/100665364235) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 6 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/33766944749/job/100687209088) | [2m57s](https://github.com/iree-org/iree/actions/runs/33758667370/job/100659305231) | [2m57s](https://github.com/iree-org/iree/actions/runs/33758667370/job/100659305231) | 6 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 6 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/33760490267/job/100665363122) | [2m52s](https://github.com/iree-org/iree/actions/runs/33758667503/job/100659341560) | [2m52s](https://github.com/iree-org/iree/actions/runs/33758667503/job/100659341560) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 6 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/33766944749/job/100687209011) | [1m27s](https://github.com/iree-org/iree/actions/runs/33758667370/job/100659305249) | [1m27s](https://github.com/iree-org/iree/actions/runs/33758667370/job/100659305249) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/33751321219/job/100635361721) | [1m24s](https://github.com/iree-org/iree/actions/runs/33758667370/job/100659305101) | [1m24s](https://github.com/iree-org/iree/actions/runs/33758667370/job/100659305101) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 172 | 1% (1/172) |  | 6h07m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 244 | 1% (2/244) |  | 6h08m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 165 | 0% (0/165) |  | 6h09m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 210 | 4% (9/210) |  | 6h11m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h05m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h21m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
