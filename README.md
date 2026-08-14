# iree-ci-monitor

_Updated: 2026-08-13 19:48 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [8m38s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540967081) | [37m02s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540967235) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [16m57s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712586) | [34m21s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540966978) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [20m00s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712666) | [28m34s](https://github.com/iree-org/iree/actions/runs/31732909884/job/94559912193) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [1m59s](https://github.com/iree-org/iree/actions/runs/31732909884/job/94559912291) | [17m18s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544713023) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31732909884/job/94559912207) | [15m28s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712674) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [4m40s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540967218) | [15m25s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712621) | 0% (0/1) | `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [7m38s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712881) | [13m59s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712584) | 0% (0/2) | `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [7m41s](https://github.com/iree-org/iree/actions/runs/31732909884/job/94559912319) | [12m02s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540967044) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [8m42s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540967011) | [10m35s](https://github.com/iree-org/iree/actions/runs/31732909884/job/94559911992) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [3m31s](https://github.com/iree-org/iree/actions/runs/31732909884/job/94559912316) | [10m18s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712590) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31732909884/job/94559912076) | [6m08s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712874) | 0% (0/1) | `shark10-ci` |
| `azure-linux-scale` | ossci | 21 | 0 | — | — | 0 | [25s](https://github.com/iree-org/iree/actions/runs/31727664756/job/94540048936) | [2m10s](https://github.com/iree-org/iree/actions/runs/31726877684/job/94537390007) | 0% (0/6) | 21 |
| `ubuntu-24.04` | github-hosted | 69 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540967077) | [8s](https://github.com/iree-org/iree/actions/runs/31728290792/job/94542712073) | 6% (1/18) | 69 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/31732909918/job/94557500558) | [5s](https://github.com/iree-org/iree/actions/runs/31732909918/job/94557500577) | 0% (0/3) | 12 |
| `windows-2022` | github-hosted | 12 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31727664756/job/94540048864) | [4s](https://github.com/iree-org/iree/actions/runs/31728290792/job/94542712139) | 33% (1/3) | 12 |
| `macos-14` | github-hosted | 12 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31726877684/job/94537389907) | [3s](https://github.com/iree-org/iree/actions/runs/31732909918/job/94557500634) | 0% (0/3) | 12 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31726877684/job/94537390180) | [2s](https://github.com/iree-org/iree/actions/runs/31728290792/job/94542712247) | 0% (0/1) | 4 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31726876690/job/94537345794) | [2s](https://github.com/iree-org/iree/actions/runs/31726876690/job/94537345855) | 0% (0/3) | 3 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [19m07s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712849) | [37m02s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540967235) | [37m02s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540967235) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [16m57s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712586) | [34m21s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540966978) | [34m21s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540966978) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [20m00s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712666) | [28m34s](https://github.com/iree-org/iree/actions/runs/31732909884/job/94559912193) | [28m34s](https://github.com/iree-org/iree/actions/runs/31732909884/job/94559912193) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540967259) | [17m18s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544713023) | [17m18s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544713023) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31732909884/job/94559912207) | [15m28s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712674) | [15m28s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712674) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [4m40s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540967218) | [15m25s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712621) | [15m25s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712621) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [11m44s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540966976) | [13m59s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712584) | [13m59s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712584) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [7m38s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712881) | [12m45s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540966972) | [12m45s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540966972) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [9m24s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712730) | [12m02s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540967044) | [12m02s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540967044) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [8m42s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540967011) | [10m35s](https://github.com/iree-org/iree/actions/runs/31732909884/job/94559911992) | [10m35s](https://github.com/iree-org/iree/actions/runs/31732909884/job/94559911992) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [3m31s](https://github.com/iree-org/iree/actions/runs/31732909884/job/94559912316) | [10m18s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712590) | [10m18s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712590) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [8m38s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540967081) | [8m54s](https://github.com/iree-org/iree/actions/runs/31732909884/job/94559912245) | [8m54s](https://github.com/iree-org/iree/actions/runs/31732909884/job/94559912245) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [7m41s](https://github.com/iree-org/iree/actions/runs/31732909884/job/94559912319) | [7m48s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540967317) | [7m48s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540967317) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [5m02s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712649) | [6m39s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540967007) | [6m39s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94540967007) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31732909884/job/94559912076) | [6m08s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712874) | [6m08s](https://github.com/iree-org/iree/actions/runs/31728290740/job/94544712874) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 4 | 0 | — | — | [53s](https://github.com/iree-org/iree/actions/runs/31727664769/job/94540062976) | [2m52s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94537403682) | [2m52s](https://github.com/iree-org/iree/actions/runs/31726877685/job/94537403682) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 4 | 0 | — | — | [1m31s](https://github.com/iree-org/iree/actions/runs/31732909918/job/94557500846) | [2m10s](https://github.com/iree-org/iree/actions/runs/31726877684/job/94537390007) | [2m10s](https://github.com/iree-org/iree/actions/runs/31726877684/job/94537390007) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 4 | 0 | — | — | [1m40s](https://github.com/iree-org/iree/actions/runs/31732909918/job/94557500867) | [1m57s](https://github.com/iree-org/iree/actions/runs/31726877684/job/94537390047) | [1m57s](https://github.com/iree-org/iree/actions/runs/31726877684/job/94537390047) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 4 | 0 | — | — | [22s](https://github.com/iree-org/iree/actions/runs/31727664756/job/94540049128) | [1m31s](https://github.com/iree-org/iree/actions/runs/31726877684/job/94537390152) | [1m31s](https://github.com/iree-org/iree/actions/runs/31726877684/job/94537390152) | 4 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 4 | 0 | — | — | [18s](https://github.com/iree-org/iree/actions/runs/31726877684/job/94537389891) | [1m25s](https://github.com/iree-org/iree/actions/runs/31732909918/job/94557500658) | [1m25s](https://github.com/iree-org/iree/actions/runs/31732909918/job/94557500658) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 173 | 8% (14/173) |  | 7h15m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 214 | 0% (0/214) |  | 7h29m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 177 | 5% (9/177) |  | 7h30m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 146 | 12% (17/146) |  | 7h37m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
