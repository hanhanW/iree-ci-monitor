# iree-ci-monitor

_Updated: 2026-06-01 12:57 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [25m46s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841306) | [25m46s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841306) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [25m40s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841298) | [25m40s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841298) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [19m44s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841326) | [19m44s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841326) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [17m31s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841283) | [17m31s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841283) | 0% (0/1) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [12m18s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841454) | [14m12s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841289) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [8m16s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841407) | [13m53s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841450) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [10m39s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841241) | [10m39s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841241) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [4m45s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841405) | [6m17s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841498) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 8 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847281094) | [1m57s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78847286246) | 0% (0/3) | 8 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m24s](https://github.com/iree-org/iree/actions/runs/26750748043/job/78837810358) | [1m24s](https://github.com/iree-org/iree/actions/runs/26750748043/job/78837810358) | 0% (0/1) | 1 |
| `macos-14` | github-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847281029) | [1m12s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847281005) | 0% (0/1) | 4 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847281006) | [12s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847280974) | — | 3 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841244) | [8s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841451) | 50% (2/4) | 8 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26766665391/job/78894816354) | [3s](https://github.com/iree-org/iree/actions/runs/26766664674/job/78894850355) | — | 12 |
| `ubuntu-24.04` | github-hosted | 38 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841304) | [3s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841462) | 7% (1/14) | 38 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847280969) | [2s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847281019) | — | 3 |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841392) | [2s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841392) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26750745235/job/78837800862) | [2s](https://github.com/iree-org/iree/actions/runs/26750745235/job/78837800862) | 0% (0/1) | 1 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847281163) | [1s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847281163) | — | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841238) | [1s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841238) | 0% (0/1) | 2 |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841253) | [1s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841253) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841373) | [1s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841464) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841413) | [1s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841413) | 0% (0/1) | `iree-mi308-1` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [25m46s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841306) | [25m46s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841306) | [25m46s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841306) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [25m40s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841298) | [25m40s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841298) | [25m40s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841298) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [19m44s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841326) | [19m44s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841326) | [19m44s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841326) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [17m31s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841283) | [17m31s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841283) | [17m31s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841283) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [14m12s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841289) | [14m12s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841289) | [14m12s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841289) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [13m53s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841450) | [13m53s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841450) | [13m53s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841450) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [12m18s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841454) | [12m18s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841454) | [12m18s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841454) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 0 | — | — | [10m39s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841241) | [10m39s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841241) | [10m39s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841241) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [8m16s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841407) | [8m16s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841407) | [8m16s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841407) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [6m17s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841498) | [6m17s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841498) | [6m17s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841498) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [4m45s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841405) | [4m45s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841405) | [4m45s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841405) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 2 | 0 | — | — | [1m57s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78847286246) | [1m57s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78847286246) | [1m57s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78847286246) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [1m42s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847281007) | [1m42s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847281007) | [1m42s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847281007) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m24s](https://github.com/iree-org/iree/actions/runs/26750748043/job/78837810358) | [1m24s](https://github.com/iree-org/iree/actions/runs/26750748043/job/78837810358) | [1m24s](https://github.com/iree-org/iree/actions/runs/26750748043/job/78837810358) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 1 | 0 | — | — | [1m12s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847281005) | [1m12s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847281005) | [1m12s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847281005) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 1 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847280974) | [12s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847280974) | [12s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847280974) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847281129) | [10s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847281129) | [10s](https://github.com/iree-org/iree/actions/runs/26753506606/job/78847281129) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841466) | [8s](https://github.com/iree-org/iree/actions/runs/26745345690/job/78842358530) | [8s](https://github.com/iree-org/iree/actions/runs/26745345690/job/78842358530) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841451) | [8s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841451) | [8s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841451) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26745345690/job/78842358507) | [8s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841396) | [8s](https://github.com/iree-org/iree/actions/runs/26753506608/job/78848841396) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 280 | 4% (12/279) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 307 | 1% (3/307) |  | 7h17m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 210 | 1% (3/210) |  | 7h22m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 216 | 0% (0/216) |  | 7h24m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 71 | 1% (1/71) |  | 7h38m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
