# iree-ci-monitor

_Updated: 2026-06-01 01:13 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [32m45s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697873) | [45m00s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697991) | — | `shark75-ci` |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [30m47s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006401) | [39m13s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78798007582) | — | 5 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [24m26s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697687) | [24m26s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697687) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [18m21s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697747) | [18m21s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697747) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697758) | [14m08s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697941) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [10m14s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697759) | [14m01s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697935) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [12m13s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697783) | [12m13s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697783) | — | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [7m18s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697753) | [7m18s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697753) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697774) | [6m40s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697765) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [5m56s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697670) | [5m56s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697670) | — | `shark10-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697852) | [19s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697974) | — | 4 |
| `ubuntu-24.04` | github-hosted | 29 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697696) | [3s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78807511158) | 50% (2/4) | 29 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26739355888/job/78799450492) | [3s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006282) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006289) | [2s](https://github.com/iree-org/iree/actions/runs/26739355888/job/78799450488) | — | 6 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006355) | [2s](https://github.com/iree-org/iree/actions/runs/26739355888/job/78799450484) | — | 5 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006385) | [1s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006385) | — | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697713) | [1s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697713) | — | 1 |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697799) | [1s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697799) | — | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697828) | [1s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697828) | — | `shark01-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697927) | [1s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697927) | — | `iree-mi308-1` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [45m00s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697991) | [45m00s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697991) | [45m00s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697991) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [39m13s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78798007582) | [39m13s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78798007582) | [39m13s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78798007582) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [35m41s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006400) | [35m41s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006400) | [35m41s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006400) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [32m45s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697873) | [32m45s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697873) | [32m45s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697873) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [30m47s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006401) | [30m47s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006401) | [30m47s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006401) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [30m45s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006386) | [30m45s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006386) | [30m45s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78798006386) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [24m26s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697687) | [24m26s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697687) | [24m26s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697687) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [18m21s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697747) | [18m21s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697747) | [18m21s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697747) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [14m08s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697941) | [14m08s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697941) | [14m08s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697941) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [14m01s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697935) | [14m01s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697935) | [14m01s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697935) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [12m13s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697783) | [12m13s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697783) | [12m13s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697783) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [10m14s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697759) | [10m14s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697759) | [10m14s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697759) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [7m18s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697753) | [7m18s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697753) | [7m18s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697753) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [6m40s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697765) | [6m40s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697765) | [6m40s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697765) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [5m56s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697670) | [5m56s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697670) | [5m56s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697670) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [19s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697974) | [19s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697974) | [19s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697974) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697714) | [8s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697714) | [8s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697714) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697852) | [8s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697852) | [8s](https://github.com/iree-org/iree/actions/runs/26730789190/job/78803697852) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26739355888/job/78799450452) | [3s](https://github.com/iree-org/iree/actions/runs/26739355888/job/78799450452) | [3s](https://github.com/iree-org/iree/actions/runs/26739355888/job/78799450452) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78807511158) | [3s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78807511158) | [3s](https://github.com/iree-org/iree/actions/runs/26730789182/job/78807511158) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 268 | 4% (12/267) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 293 | 1% (3/293) |  | 7m54s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 201 | 1% (3/201) |  | 38m41s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 206 | 0% (0/206) |  | 39m12s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 68 | 1% (1/68) |  | 48m46s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
