# iree-ci-monitor

_Updated: 2026-08-31 06:58 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [26m02s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476113167) | [1h01m](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414568) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414506) | [34m05s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476112876) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [16m32s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476113118) | [26m10s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99445021353) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476112911) | [21m36s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414675) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [13m54s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414530) | [19m48s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99445021151) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [10m12s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99445021556) | [19m47s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476113154) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [13m44s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476113161) | [15m54s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99445021620) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [6m43s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476113064) | [15m21s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414669) | 0% (0/4) | `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [8m38s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476113222) | [14m43s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414740) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [7m29s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414591) | [13m29s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99445021272) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `azure-linux-scale` | ossci | 35 | 0 | — | — | 11 | [9s](https://github.com/iree-org/iree/actions/runs/33387820610/job/99474359790) | [1m53s](https://github.com/iree-org/iree/actions/runs/33399593166/job/99512418882) | 7% (1/14) | 33 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m51s](https://github.com/iree-org/iree/actions/runs/33378152449/job/99444199213) | [1m51s](https://github.com/iree-org/iree/actions/runs/33378152449/job/99444199213) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 20 | 0 | — | — | 6 | [2s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99511395561) | [26s](https://github.com/iree-org/iree/actions/runs/33384557769/job/99464254552) | 0% (0/6) | 20 |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 2 | [1s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99511396240) | [12s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405510) | 0% (0/2) | 6 |
| `ubuntu-latest` | github-hosted | 21 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33387819430/job/99474312917) | [6s](https://github.com/iree-org/iree/actions/runs/33384554403/job/99464123416) | 0% (0/9) | 21 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99511395655) | [5s](https://github.com/iree-org/iree/actions/runs/33359966815/job/99389312245) | 0% (0/9) | 20 |
| `macos-14` | github-hosted | 21 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99511395632) | [4s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405458) | 0% (0/10) | 21 |
| `ubuntu-24.04` | github-hosted | 104 | 0 | — | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476113206) | [3s](https://github.com/iree-org/iree/actions/runs/33399287678/job/99511395648) | 0% (0/48) | 101 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99445021156) | [2s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414542) | 0% (0/2) | `shark01-ci`, `shark55-ci` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [26m02s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476113167) | [1h01m](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414568) | [1h01m](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414568) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414506) | [34m05s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476112876) | [34m05s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476112876) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [22m59s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476113142) | [26m10s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99445021353) | [26m10s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99445021353) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476112911) | [21m36s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414675) | [21m36s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414675) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [13m54s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414530) | [19m48s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99445021151) | [19m48s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99445021151) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [10m27s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414789) | [19m47s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476113154) | [19m47s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476113154) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [8m25s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99445022094) | [16m32s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476113118) | [16m32s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476113118) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [13m44s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476113161) | [15m54s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99445021620) | [15m54s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99445021620) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [6m26s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99445021122) | [15m21s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414669) | [15m21s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414669) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [15m10s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99445021284) | [15m16s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476113157) | [15m16s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476113157) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [13m25s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99445021239) | [14m56s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414528) | [14m56s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414528) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [8m38s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476113222) | [14m43s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414740) | [14m43s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414740) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [7m29s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414591) | [13m29s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99445021272) | [13m29s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99445021272) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33384557685/job/99466414618) | [10m24s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476113095) | [10m24s](https://github.com/iree-org/iree/actions/runs/33387820578/job/99476113095) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 6 | 0 | — | — | [1m17s](https://github.com/iree-org/iree/actions/runs/33399287793/job/99511414456) | [2m08s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99442325528) | [2m08s](https://github.com/iree-org/iree/actions/runs/33377532416/job/99442325528) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 6 | 0 | — | — | [26s](https://github.com/iree-org/iree/actions/runs/33377532332/job/99442317298) | [2m04s](https://github.com/iree-org/iree/actions/runs/33387820610/job/99474360549) | [2m04s](https://github.com/iree-org/iree/actions/runs/33387820610/job/99474360549) | 6 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m51s](https://github.com/iree-org/iree/actions/runs/33378152449/job/99444199213) | [1m51s](https://github.com/iree-org/iree/actions/runs/33378152449/job/99444199213) | [1m51s](https://github.com/iree-org/iree/actions/runs/33378152449/job/99444199213) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 3 | 0 | — | — | [1m27s](https://github.com/iree-org/iree/actions/runs/33377532332/job/99442317205) | [1m33s](https://github.com/iree-org/iree/actions/runs/33387820610/job/99474359789) | [1m33s](https://github.com/iree-org/iree/actions/runs/33387820610/job/99474359789) | 3 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 6 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/33377532332/job/99442317026) | [1m31s](https://github.com/iree-org/iree/actions/runs/33387820610/job/99474359654) | [1m31s](https://github.com/iree-org/iree/actions/runs/33387820610/job/99474359654) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 6 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/33399593222/job/99512405636) | [1m27s](https://github.com/iree-org/iree/actions/runs/33377532332/job/99442317198) | [1m27s](https://github.com/iree-org/iree/actions/runs/33377532332/job/99442317198) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 312 | 1% (2/312) |  | 1h32m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 268 | 3% (9/268) |  | 1h43m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 221 | 0% (1/221) |  | 1h47m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 220 | 0% (0/220) |  | 1h48m ago |

## Alerts

- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h01m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
