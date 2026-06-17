# iree-ci-monitor

_Updated: 2026-06-17 01:13 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [15m26s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714895) | [20m45s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714983) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [7m23s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714861) | [19m29s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714975) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [15m57s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714862) | [15m57s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714862) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [7m30s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833715055) | [14m58s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714904) | — | `shark01-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [13m11s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714958) | [13m11s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714958) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [10m37s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714970) | [10m37s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714970) | — | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [6m14s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714856) | [6m14s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714856) | — | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714866) | [5m17s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714971) | — | `shark55-ci` |
| `azure-linux-scale` | ossci | 16 | 0 | — | — | 6 | [8s](https://github.com/iree-org/iree/actions/runs/27670250131/job/81833086093) | [2m21s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559418) | — | 16 |
| `macos-14` | github-hosted | 11 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/27669973842/job/81831955595) | [10s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559165) | 0% (0/3) | 11 |
| `ubuntu-24.04` | github-hosted | 47 | 0 | — | — | 3 | [3s](https://github.com/iree-org/iree/actions/runs/27670250131/job/81833086042) | [9s](https://github.com/iree-org/iree/actions/runs/27670250146/job/81832775088) | 20% (2/10) | 47 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714863) | [9s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714858) | — | 4 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559177) | [6s](https://github.com/iree-org/iree/actions/runs/27670250131/job/81833086006) | 0% (0/3) | 12 |
| `windows-2022` | github-hosted | 11 | 0 | — | — | 4 | [2s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559291) | [6s](https://github.com/iree-org/iree/actions/runs/27669973842/job/81831955586) | — | 11 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27674844937/job/81847531855) | [2s](https://github.com/iree-org/iree/actions/runs/27674844937/job/81847531894) | 0% (0/3) | 3 |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/27670250131/job/81833086134) | [1s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559490) | — | 3 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714837) | [1s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714837) | — | 1 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714838) | [1s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714838) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714844) | [1s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714844) | — | `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714914) | [1s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714914) | — | `iree-mi308-1` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714968) | [1s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714968) | — | `shark01-ci` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [20m45s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714983) | [20m45s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714983) | [20m45s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714983) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [19m29s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714975) | [19m29s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714975) | [19m29s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714975) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [15m57s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714862) | [15m57s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714862) | [15m57s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714862) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [15m26s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714895) | [15m26s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714895) | [15m26s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714895) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [14m58s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714904) | [14m58s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714904) | [14m58s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714904) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [13m11s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714958) | [13m11s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714958) | [13m11s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714958) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [10m37s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714970) | [10m37s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714970) | [10m37s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714970) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [7m30s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833715055) | [7m30s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833715055) | [7m30s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833715055) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [7m23s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714861) | [7m23s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714861) | [7m23s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714861) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [6m14s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714856) | [6m14s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714856) | [6m14s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714856) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [5m17s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714971) | [5m17s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714971) | [5m17s](https://github.com/iree-org/iree/actions/runs/27670250133/job/81833714971) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 3 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27669973842/job/81831955670) | [2m28s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559579) | [2m28s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559579) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27669973842/job/81831955584) | [2m21s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559418) | [2m21s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559418) | 3 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 3 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27670250131/job/81833086057) | [2m03s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559368) | [2m03s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559368) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [1m12s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559422) | [1m12s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559422) | [1m12s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559422) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27670250131/job/81833086081) | [1m08s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559240) | [1m08s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559240) | 3 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27670250131/job/81833085994) | [1m07s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559238) | [1m07s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559238) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27669973842/job/81831955559) | [43s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559478) | [43s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559478) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27669973842/job/81831955668) | [36s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559266) | [36s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559266) | 3 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27670250131/job/81833086005) | [10s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559165) | [10s](https://github.com/iree-org/iree/actions/runs/27674846738/job/81847559165) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 237 | 0% (1/237) |  | 1h06m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 164 | 0% (0/164) |  | 1h08m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 175 | 1% (2/175) |  | 1h12m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 187 | 5% (10/187) |  | 1h16m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 54 | 0% (0/54) |  | 1h27m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
