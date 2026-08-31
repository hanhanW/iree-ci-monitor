# iree-ci-monitor

_Updated: 2026-08-31 15:54 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [13m28s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026551) | [1h09m](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026644) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [47m20s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026417) | [47m20s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026417) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [16m25s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026393) | [16m25s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026393) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [7m28s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026674) | [13m59s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026531) | 0% (0/2) | `shark01-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [6m30s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026548) | [13m19s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026557) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [11m19s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026423) | [11m19s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026423) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [6m51s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026574) | [6m51s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026574) | 0% (0/1) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026438) | [4m43s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026333) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `azure-linux-scale` | ossci | 11 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405636) | [1m53s](https://github.com/iree-org/iree/actions/runs/33399593166/job/99512418882) | 0% (0/6) | 11 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99511395761) | [1m20s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405424) | 0% (0/3) | 6 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99511396240) | [12s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405510) | 0% (0/1) | 2 |
| `ubuntu-24.04` | github-hosted | 45 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33399593166/job/99515581312) | [4s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99520895758) | 0% (0/18) | 43 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405296) | [4s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405141) | 0% (0/3) | 6 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99511395716) | [4s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405458) | 0% (0/3) | 6 |
| `ubuntu-latest` | github-hosted | 4 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/33399286782/job/99511343302) | [4s](https://github.com/iree-org/iree/actions/runs/33442733891/job/99654566591) | 0% (0/4) | 4 |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026360) | [2s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026360) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026394) | [2s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026394) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026457) | [2s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026457) | 0% (0/1) | `shark01-ci` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [1h09m](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026644) | [1h09m](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026644) | [1h09m](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026644) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [47m20s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026417) | [47m20s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026417) | [47m20s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026417) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [16m25s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026393) | [16m25s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026393) | [16m25s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026393) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [13m59s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026531) | [13m59s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026531) | [13m59s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026531) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [13m28s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026551) | [13m28s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026551) | [13m28s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026551) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [13m19s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026557) | [13m19s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026557) | [13m19s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026557) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [11m19s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026423) | [11m19s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026423) | [11m19s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026423) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [7m28s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026674) | [7m28s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026674) | [7m28s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026674) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [6m51s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026574) | [6m51s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026574) | [6m51s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026574) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [6m30s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026548) | [6m30s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026548) | [6m30s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026548) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [4m43s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026333) | [4m43s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026333) | [4m43s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99514026333) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 2 | 0 | — | — | [1m17s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99511414456) | [1m53s](https://github.com/iree-org/iree/actions/runs/33399593166/job/99512418882) | [1m53s](https://github.com/iree-org/iree/actions/runs/33399593166/job/99512418882) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [1m17s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99511395770) | [1m49s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405775) | [1m49s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405775) | 2 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99511395442) | [1m22s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405147) | [1m22s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405147) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99511395761) | [1m20s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405424) | [1m20s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405424) | 2 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405433) | [1m17s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99511395869) | [1m17s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99511395869) | 2 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99511396240) | [12s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405510) | [12s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405510) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99511395875) | [8s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405431) | [8s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405431) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99511395867) | [8s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405636) | [8s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405636) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99511395889) | [8s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99511395889) | [8s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99511395889) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 317 | 1% (2/317) |  | 7h38m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 224 | 0% (1/224) |  | 8h28m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 223 | 0% (0/223) |  | 8h29m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 272 | 3% (9/272) |  | 8h33m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h09m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
