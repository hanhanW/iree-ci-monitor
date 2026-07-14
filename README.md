# iree-ci-monitor

_Updated: 2026-07-14 05:45 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [11m53s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907481) | [22m10s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093684) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [6m07s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093965) | [21m21s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036256129) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [7m51s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907573) | [19m44s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093971) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [15m24s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093922) | [19m07s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036255888) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [4m49s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907523) | [18m38s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093859) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [4m33s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907452) | [17m50s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036255894) | 50% (1/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [10m16s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907522) | [15m59s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036256070) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [3m54s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907512) | [15m07s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093875) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [10m51s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907532) | [14m14s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036256089) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [8m30s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093811) | [13m50s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036256128) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093829) | [7m16s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907620) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m54s](https://github.com/iree-org/iree/actions/runs/29323385260/job/87053786300) | [1m54s](https://github.com/iree-org/iree/actions/runs/29323385260/job/87053786300) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 14 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29321443017/job/87047498832) | [42s](https://github.com/iree-org/iree/actions/runs/29317512731/job/87034855533) | 0% (0/6) | 14 |
| `azure-linux-scale` | ossci | 25 | 0 | — | — | 6 | [8s](https://github.com/iree-org/iree/actions/runs/29321443017/job/87047499006) | [13s](https://github.com/iree-org/iree/actions/runs/29317512731/job/87034855541) | 0% (0/14) | 25 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/29332513435/job/87083677182) | [8s](https://github.com/iree-org/iree/actions/runs/29321443017/job/87047498822) | 0% (0/6) | 15 |
| `ubuntu-24.04` | github-hosted | 81 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093912) | [4s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093749) | 10% (4/41) | 79 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/29323345673/job/87053657031) | [4s](https://github.com/iree-org/iree/actions/runs/29323345673/job/87053657031) | — | 1 |
| `macos-14` | github-hosted | 15 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/29317512731/job/87034855563) | [3s](https://github.com/iree-org/iree/actions/runs/29323357427/job/87053696130) | 0% (0/6) | 15 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907415) | [3s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093654) | 0% (0/2) | 3 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907611) | [3s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093869) | 0% (0/2) | `iree-mi308-1` |
| `ubuntu-latest` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29329535999/job/87073883931) | [3s](https://github.com/iree-org/iree/actions/runs/29329535999/job/87073912459) | 0% (0/6) | 18 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/29321443017/job/87047499022) | [1s](https://github.com/iree-org/iree/actions/runs/29332513435/job/87083677526) | 0% (0/2) | 4 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [11m53s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907481) | [22m10s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093684) | [22m10s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093684) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [11m21s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093777) | [21m21s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036256129) | [21m21s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036256129) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [9m07s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907548) | [19m44s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093971) | [19m44s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093971) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [15m24s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093922) | [19m07s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036255888) | [19m07s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036255888) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [8m34s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907601) | [18m38s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093859) | [18m38s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093859) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [4m33s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907452) | [17m50s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036255894) | [17m50s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036255894) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [10m16s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907522) | [15m59s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036256070) | [15m59s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036256070) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [3m54s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907512) | [15m07s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093875) | [15m07s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093875) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [10m51s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907532) | [14m14s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036256089) | [14m14s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036256089) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [8m30s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093811) | [13m50s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036256128) | [13m50s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036256128) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [4m49s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907523) | [9m46s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036256051) | [9m46s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036256051) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [7m51s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907573) | [9m36s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093826) | [9m36s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093826) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [6m07s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093965) | [9m03s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907556) | [9m03s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907556) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [5m45s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093982) | [7m16s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907620) | [7m16s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907620) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093829) | [4m52s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036256145) | [4m52s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036256145) | 2 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m54s](https://github.com/iree-org/iree/actions/runs/29323385260/job/87053786300) | [1m54s](https://github.com/iree-org/iree/actions/runs/29323385260/job/87053786300) | [1m54s](https://github.com/iree-org/iree/actions/runs/29323385260/job/87053786300) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 4 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/29332513339/job/87083678218) | [1m50s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87009646410) | [1m50s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87009646410) | 4 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093861) | [1m24s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907624) | [1m24s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907624) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 4 | 0 | — | — | [25s](https://github.com/iree-org/iree/actions/runs/29332513435/job/87083677240) | [1m08s](https://github.com/iree-org/iree/actions/runs/29317512731/job/87034855595) | [1m08s](https://github.com/iree-org/iree/actions/runs/29317512731/job/87034855595) | 4 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29317512791/job/87036256017) | [53s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907599) | [53s](https://github.com/iree-org/iree/actions/runs/29309357812/job/87010907599) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 175 | 2% (3/174) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 128 | 1% (1/127) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 142 | 10% (14/141) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 149 | 1% (1/148) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 41 | 12% (5/41) |  | 3h02m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
