# iree-ci-monitor

_Updated: 2026-06-01 07:25 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [18m21s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201519) | [1h12m](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201624) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [25m46s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841306) | [52m50s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201498) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [24m26s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697687) | [37m50s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201285) | 0% (0/1) | `shark75-ci` |
| `azure-linux-scale` | ossci | 23 | 0 | — | — | 0 | [16s](https://github.com/iree-org/iree/actions/runs/26745345644/job/78819331662) | [35m41s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006400) | 0% (0/8) | 23 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [20m42s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201495) | [25m40s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841298) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [6m40s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697765) | [20m33s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201543) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [19m17s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201381) | [19m44s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841326) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [12m13s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697783) | [17m31s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841283) | 0% (0/1) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [10m14s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697759) | [15m54s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201548) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841464) | [14m08s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697941) | 0% (0/2) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [9m36s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201265) | [10m39s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841241) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841392) | [10m17s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201603) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m24s](https://github.com/iree-org/iree/actions/runs/26750748043/job/78837810358) | [1m24s](https://github.com/iree-org/iree/actions/runs/26750748043/job/78837810358) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26743045924/job/78812230172) | [12s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847280974) | 0% (0/3) | 15 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697852) | [9s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201295) | 50% (2/4) | 16 |
| `ubuntu-24.04` | github-hosted | 93 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/26745345690/job/78843479587) | [4s](https://github.com/iree-org/iree/actions/runs/26745345644/job/78819331347) | 14% (3/22) | 93 |
| `macos-14` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847281029) | [3s](https://github.com/iree-org/iree/actions/runs/26745345644/job/78819331448) | 0% (0/4) | 15 |
| `windows-2022` | github-hosted | 14 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26743045924/job/78812230306) | [3s](https://github.com/iree-org/iree/actions/runs/26745345644/job/78819331351) | 0% (0/3) | 14 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26754424996/job/78850475086) | [3s](https://github.com/iree-org/iree/actions/runs/26754424996/job/78850475032) | 0% (0/3) | 9 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847281163) | [2s](https://github.com/iree-org/iree/actions/runs/26745345644/job/78819331530) | 0% (0/1) | 4 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841238) | [2s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201257) | 0% (0/1) | 4 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841413) | [2s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201510) | 0% (0/1) | `iree-mi308-1` |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26750745235/job/78837800862) | [2s](https://github.com/iree-org/iree/actions/runs/26750745235/job/78837800862) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [45m00s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697991) | [1h12m](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201624) | [1h12m](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201624) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [25m46s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841306) | [52m50s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201498) | [52m50s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201498) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 4 | 0 | — | — | [1m57s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78847286246) | [39m13s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78798007582) | [39m13s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78798007582) | 4 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [24m26s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697687) | [37m50s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201285) | [37m50s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201285) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 4 | 0 | — | — | [56s](https://github.com/iree-org/iree/actions/runs/26743045924/job/78812230324) | [35m41s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006400) | [35m41s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006400) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [18m21s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201519) | [32m45s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697873) | [32m45s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697873) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 4 | 0 | — | — | [4m53s](https://github.com/iree-org/iree/actions/runs/26743045924/job/78812230280) | [30m47s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006401) | [30m47s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006401) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 4 | 0 | — | — | [4m57s](https://github.com/iree-org/iree/actions/runs/26743045924/job/78812230444) | [30m45s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006386) | [30m45s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006386) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [20m42s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201495) | [25m40s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841298) | [25m40s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841298) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [12m18s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841454) | [20m33s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201543) | [20m33s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201543) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [19m17s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201381) | [19m44s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841326) | [19m44s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841326) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [12m13s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697783) | [17m31s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841283) | [17m31s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841283) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [14m01s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697935) | [15m54s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201548) | [15m54s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201548) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201491) | [14m12s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841289) | [14m12s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841289) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [7m50s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201404) | [14m08s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697941) | [14m08s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697941) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [10m14s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697759) | [10m57s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201484) | [10m57s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201484) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 4 | 0 | — | — | [9m36s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201265) | [10m39s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841241) | [10m39s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841241) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841392) | [10m17s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201603) | [10m17s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201603) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 4 | 0 | — | — | [1m42s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847281007) | [4m41s](https://github.com/iree-org/iree/actions/runs/26743045924/job/78812230216) | [4m41s](https://github.com/iree-org/iree/actions/runs/26743045924/job/78812230216) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841373) | [1m42s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201609) | [1m42s](https://github.com/iree-org/iree/actions/runs/26743045885/job/78813201609) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 280 | 4% (12/279) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 307 | 1% (3/307) |  | 1h45m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 210 | 1% (3/210) |  | 1h50m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 216 | 0% (0/216) |  | 1h52m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 71 | 1% (1/71) |  | 2h06m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h12m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
