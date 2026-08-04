# iree-ci-monitor

_Updated: 2026-08-04 11:51 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [10m31s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485422) | [48m40s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946383) | — | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [24m29s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946254) | [30m56s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946357) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [15m35s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647814) | [24m13s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485587) | — | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [18m30s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485502) | [21m21s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648128) | — | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [13m51s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485410) | [20m50s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648265) | — | `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485589) | [18m34s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946261) | — | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [17m06s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485071) | [18m13s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648054) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [8m29s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485366) | [15m03s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946241) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [6m26s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648178) | [14m55s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946337) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [5m02s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485602) | [14m10s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648193) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 18 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/30905381069/job/91979187596) | [1m40s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248949) | 50% (1/2) | 18 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m30s](https://github.com/iree-org/iree/actions/runs/30899387048/job/91959852511) | [1m30s](https://github.com/iree-org/iree/actions/runs/30899387048/job/91959852511) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30905381069/job/91979187593) | [39s](https://github.com/iree-org/iree/actions/runs/30927059906/job/92052044108) | — | 9 |
| `ubuntu-24.04` | github-hosted | 66 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30906549124/job/91982852656) | [9s](https://github.com/iree-org/iree/actions/runs/30911221746/job/92006697225) | 0% (0/3) | 65 |
| `macos-14` | github-hosted | 10 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248861) | [9s](https://github.com/iree-org/iree/actions/runs/30905381069/job/91979187540) | 0% (0/1) | 10 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/30899337842/job/91959692349) | [5s](https://github.com/iree-org/iree/actions/runs/30899337842/job/91959692349) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248671) | [4s](https://github.com/iree-org/iree/actions/runs/30927059906/job/92052043788) | — | 9 |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998249092) | [3s](https://github.com/iree-org/iree/actions/runs/30927059906/job/92052043991) | — | 3 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30921215977/job/92032033991) | [3s](https://github.com/iree-org/iree/actions/runs/30927052389/job/92051968368) | — | 15 |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946150) | [2s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485030) | — | `shark01-ci`, `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 3 | 2 | [5h46m](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946220) | 2026-08-04 11:51 PDT | 0 | 0s | 0s | — | 0 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 1 | 1 | [2h41m](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485324) | 2026-08-04 11:51 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [5h46m](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946220) | 2026-08-04 11:51 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | `decommission-mi325` | pull_request |
| [2h41m](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485324) | 2026-08-04 11:51 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `integrates/llvm-20260731-cleanup` | pull_request |
| [2h41m](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485541) | 2026-08-04 11:51 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | `integrates/llvm-20260731-cleanup` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 3 | 2 | [5h46m](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946220) | 2026-08-04 11:51 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 1 | [2h41m](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485324) | 2026-08-04 11:51 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [10m31s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485422) | [48m40s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946383) | [48m40s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946383) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [6m12s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647927) | [30m56s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946357) | [30m56s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946357) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [25m15s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485289) | [25m17s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647942) | [25m17s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647942) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [15m35s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980647814) | [24m13s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485587) | [24m13s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485587) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [18m30s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485502) | [21m21s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648128) | [21m21s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648128) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [15m18s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485431) | [20m50s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648265) | [20m50s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648265) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485589) | [18m34s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946261) | [18m34s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946261) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [17m06s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485071) | [18m13s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648054) | [18m13s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648054) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [8m29s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485366) | [15m03s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946241) | [15m03s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946241) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [6m44s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485487) | [14m55s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946337) | [14m55s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946337) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [10m16s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946391) | [14m10s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648193) | [14m10s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648193) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [11m19s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946233) | [13m51s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485410) | [13m51s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485410) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [5m02s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92054485602) | [12m08s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648166) | [12m08s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648166) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [6m26s](https://github.com/iree-org/iree/actions/runs/30905381081/job/91980648178) | [8m38s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946193) | [8m38s](https://github.com/iree-org/iree/actions/runs/30911221979/job/92000946193) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 3 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/30927055920/job/92052054852) | [1m54s](https://github.com/iree-org/iree/actions/runs/30911221979/job/91998330308) | [1m54s](https://github.com/iree-org/iree/actions/runs/30911221979/job/91998330308) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 3 | 0 | — | — | [1m27s](https://github.com/iree-org/iree/actions/runs/30905381069/job/91979187652) | [1m40s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248853) | [1m40s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248853) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 3 | 0 | — | — | [1m25s](https://github.com/iree-org/iree/actions/runs/30905381069/job/91979187673) | [1m40s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248945) | [1m40s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248945) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 3 | 0 | — | — | [36s](https://github.com/iree-org/iree/actions/runs/30905381069/job/91979187710) | [1m40s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248949) | [1m40s](https://github.com/iree-org/iree/actions/runs/30911221746/job/91998248949) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 170 | 0% (0/170) |  | 2h11m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 152 | 2% (3/152) |  | 2h13m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 121 | 0% (0/121) |  | 2h15m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 127 | 1% (1/127) |  | 2h17m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 35 | 0% (0/35) |  | 1d05h ago |

## Alerts

- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job observed waiting 2h41m (> 2h00m)
- **[stale-queued]** `nodai-amdgpu-mi308-x86-64` oldest queued job observed waiting 5h46m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
