# iree-ci-monitor

_Updated: 2026-08-05 07:35 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [17m03s](https://github.com/iree-org/iree/actions/runs/30993952770/job/92268443156) | [1h10m](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091329) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [19m30s](https://github.com/iree-org/iree/actions/runs/30993952770/job/92268443267) | [57m13s](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091705) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [13m19s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136907) | [25m28s](https://github.com/iree-org/iree/actions/runs/31001826537/job/92294195639) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [13m53s](https://github.com/iree-org/iree/actions/runs/30993952770/job/92268443328) | [24m44s](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091360) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [7m50s](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091257) | [21m45s](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091517) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [16m24s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136913) | [21m04s](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091317) | 0% (0/2) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [6m00s](https://github.com/iree-org/iree/actions/runs/30993952770/job/92268443082) | [17m15s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136974) | 0% (0/4) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [10m03s](https://github.com/iree-org/iree/actions/runs/31001826537/job/92294195691) | [12m55s](https://github.com/iree-org/iree/actions/runs/30993952770/job/92268443070) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [9m27s](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091122) | [10m32s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137087) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [8m41s](https://github.com/iree-org/iree/actions/runs/31001826537/job/92294195731) | [9m26s](https://github.com/iree-org/iree/actions/runs/30993952770/job/92268443142) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [4m32s](https://github.com/iree-org/iree/actions/runs/31001826537/job/92294195909) | [5m41s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136837) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m29s](https://github.com/iree-org/iree/actions/runs/30996148188/job/92273579393) | [1m29s](https://github.com/iree-org/iree/actions/runs/30996148188/job/92273579393) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 25 | 0 | — | — | 0 | [21s](https://github.com/iree-org/iree/actions/runs/31001826527/job/92292312115) | [1m27s](https://github.com/iree-org/iree/actions/runs/30993952783/job/92266480099) | 7% (1/14) | 25 |
| `macos-14` | github-hosted | 15 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/31007239682/job/92310120840) | [56s](https://github.com/iree-org/iree/actions/runs/31007239682/job/92310120698) | 0% (0/7) | 15 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30993952783/job/92266479594) | [50s](https://github.com/iree-org/iree/actions/runs/31001826527/job/92292311846) | 0% (0/6) | 15 |
| `ubuntu-24.04` | github-hosted | 93 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92242673900) | [25s](https://github.com/iree-org/iree/actions/runs/31001826527/job/92292311884) | 0% (0/41) | 92 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31003675918/job/92298330554) | [9s](https://github.com/iree-org/iree/actions/runs/31001821426/job/92292260661) | 0% (0/6) | 15 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/30996099676/job/92273419894) | [4s](https://github.com/iree-org/iree/actions/runs/30996099676/job/92273419894) | — | 1 |
| `windows-2022` | github-hosted | 14 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31001826527/job/92292311815) | [3s](https://github.com/iree-org/iree/actions/runs/31007239682/job/92310120771) | 0% (0/6) | 14 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/31007239682/job/92310121042) | [2s](https://github.com/iree-org/iree/actions/runs/30993952783/job/92266480002) | 0% (0/2) | 4 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [17m03s](https://github.com/iree-org/iree/actions/runs/30993952770/job/92268443156) | [1h10m](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091329) | [1h10m](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091329) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [32m37s](https://github.com/iree-org/iree/actions/runs/31001826537/job/92294195873) | [57m13s](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091705) | [57m13s](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091705) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [13m19s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136907) | [25m28s](https://github.com/iree-org/iree/actions/runs/31001826537/job/92294195639) | [25m28s](https://github.com/iree-org/iree/actions/runs/31001826537/job/92294195639) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [14m54s](https://github.com/iree-org/iree/actions/runs/31001826537/job/92294195925) | [24m44s](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091360) | [24m44s](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091360) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [9m59s](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091315) | [22m04s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137055) | [22m04s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137055) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [20m15s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137180) | [21m45s](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091517) | [21m45s](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091517) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [9m25s](https://github.com/iree-org/iree/actions/runs/30993952770/job/92268443219) | [21m30s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137051) | [21m30s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137051) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [16m24s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136913) | [21m04s](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091317) | [21m04s](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091317) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [14m12s](https://github.com/iree-org/iree/actions/runs/31001826537/job/92294195701) | [17m15s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136974) | [17m15s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136974) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091220) | [15m52s](https://github.com/iree-org/iree/actions/runs/31001826537/job/92294195884) | [15m52s](https://github.com/iree-org/iree/actions/runs/31001826537/job/92294195884) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [10m03s](https://github.com/iree-org/iree/actions/runs/31001826537/job/92294195691) | [12m55s](https://github.com/iree-org/iree/actions/runs/30993952770/job/92268443070) | [12m55s](https://github.com/iree-org/iree/actions/runs/30993952770/job/92268443070) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 4 | 0 | — | — | [9m27s](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091122) | [10m32s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137087) | [10m32s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137087) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [8m41s](https://github.com/iree-org/iree/actions/runs/31001826537/job/92294195731) | [9m26s](https://github.com/iree-org/iree/actions/runs/30993952770/job/92268443142) | [9m26s](https://github.com/iree-org/iree/actions/runs/30993952770/job/92268443142) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [7m50s](https://github.com/iree-org/iree/actions/runs/31007239710/job/92312091257) | [8m20s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137030) | [8m20s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236137030) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [4m32s](https://github.com/iree-org/iree/actions/runs/31001826537/job/92294195909) | [5m41s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136837) | [5m41s](https://github.com/iree-org/iree/actions/runs/30983907181/job/92236136837) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 4 | 0 | — | — | [1m27s](https://github.com/iree-org/iree/actions/runs/30993952783/job/92266480099) | [1m38s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92234266783) | [1m38s](https://github.com/iree-org/iree/actions/runs/30983907206/job/92234266783) | 4 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m29s](https://github.com/iree-org/iree/actions/runs/30996148188/job/92273579393) | [1m29s](https://github.com/iree-org/iree/actions/runs/30996148188/job/92273579393) | [1m29s](https://github.com/iree-org/iree/actions/runs/30996148188/job/92273579393) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 3 | 0 | — | — | [1m16s](https://github.com/iree-org/iree/actions/runs/31007239682/job/92310120946) | [1m26s](https://github.com/iree-org/iree/actions/runs/30993952783/job/92266479857) | [1m26s](https://github.com/iree-org/iree/actions/runs/30993952783/job/92266479857) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 4 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/31001826527/job/92292312168) | [1m25s](https://github.com/iree-org/iree/actions/runs/30993952783/job/92266479846) | [1m25s](https://github.com/iree-org/iree/actions/runs/30993952783/job/92266479846) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 4 | 0 | — | — | [40s](https://github.com/iree-org/iree/actions/runs/31007239682/job/92310120963) | [1m25s](https://github.com/iree-org/iree/actions/runs/30993952783/job/92266479850) | [1m25s](https://github.com/iree-org/iree/actions/runs/30993952783/job/92266479850) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 180 | 0% (0/180) |  | 24m22s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 128 | 0% (0/128) |  | 1h13m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 161 | 2% (3/161) |  | 1h15m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 131 | 1% (1/131) |  | 1h23m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 33 | 0% (0/33) |  | 2d01h ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h10m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
