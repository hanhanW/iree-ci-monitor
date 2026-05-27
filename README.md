# iree-ci-monitor

_Updated: 2026-05-27 06:36 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `azure-linux-scale` | ossci | 62 | 0 | — | — | 7 | [24m05s](https://github.com/iree-org/iree/actions/runs/26496087619/job/78024555371) | [2h13m](https://github.com/iree-org/iree/actions/runs/26497809643/job/78030278195) | 0% (0/8) | 56 |
| `Linux,X64,gfx1201` | self-hosted | 14 | 0 | — | — | 0 | [46m07s](https://github.com/iree-org/iree/actions/runs/26497073791/job/78043789579) | [1h51m](https://github.com/iree-org/iree/actions/runs/26497517427/job/78043870350) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 7 | 0 | — | — | 0 | [39m25s](https://github.com/iree-org/iree/actions/runs/26497073791/job/78043789617) | [1h15m](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371065) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 7 | 0 | — | — | 0 | [22m12s](https://github.com/iree-org/iree/actions/runs/26496087619/job/78032596126) | [55m03s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065370905) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [19m05s](https://github.com/iree-org/iree/actions/runs/26497517427/job/78043870284) | [52m59s](https://github.com/iree-org/iree/actions/runs/26497073791/job/78043789606) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [11m11s](https://github.com/iree-org/iree/actions/runs/26496087619/job/78032596169) | [47m20s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371020) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 7 | 0 | — | — | 0 | [16m08s](https://github.com/iree-org/iree/actions/runs/26496087619/job/78032596177) | [45m05s](https://github.com/iree-org/iree/actions/runs/26497517427/job/78043870240) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 14 | 0 | — | — | 0 | [19m28s](https://github.com/iree-org/iree/actions/runs/26496087619/job/78032596315) | [44m32s](https://github.com/iree-org/iree/actions/runs/26497517427/job/78043870278) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 7 | 0 | — | — | 0 | [12m10s](https://github.com/iree-org/iree/actions/runs/26493359398/job/78017086285) | [34m32s](https://github.com/iree-org/iree/actions/runs/26497809642/job/78054136825) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 14 | 0 | — | — | 0 | [13m39s](https://github.com/iree-org/iree/actions/runs/26493359398/job/78017086431) | [30m53s](https://github.com/iree-org/iree/actions/runs/26497517427/job/78043870294) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [7m47s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371027) | [26m34s](https://github.com/iree-org/iree/actions/runs/26497517427/job/78043870369) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 14 | 0 | — | — | 0 | [8m34s](https://github.com/iree-org/iree/actions/runs/26497073791/job/78043789551) | [19m29s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772363) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 7 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371092) | [10m00s](https://github.com/iree-org/iree/actions/runs/26497517427/job/78043869994) | 0% (0/1) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 28 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/26496087619/job/78032596171) | [4m24s](https://github.com/iree-org/iree/actions/runs/26497517427/job/78043870207) | 0% (0/4) | 28 |
| `azure-windows-scale` | ossci | 11 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/26497517424/job/78029369799) | [3m07s](https://github.com/iree-org/iree/actions/runs/26514270484/job/78086877942) | 0% (0/1) | 11 |
| `ubuntu-24.04` | github-hosted | 191 | 0 | — | — | 4 | [2s](https://github.com/iree-org/iree/actions/runs/26502358424/job/78055772391) | [1m35s](https://github.com/iree-org/iree/actions/runs/26507618167/job/78064044840) | 7% (2/29) | 191 |
| `macos-14` | github-hosted | 36 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26507618167/job/78064044818) | [1m29s](https://github.com/iree-org/iree/actions/runs/26497348937/job/78028741524) | 0% (0/6) | 36 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m23s](https://github.com/iree-org/iree/actions/runs/26506124202/job/78058846260) | [1m23s](https://github.com/iree-org/iree/actions/runs/26506124202/job/78058846260) | 100% (1/1) | 1 |
| `windows-2022` | github-hosted | 35 | 0 | — | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/26511684263/job/78077690441) | [1m10s](https://github.com/iree-org/iree/actions/runs/26496087647/job/78024558426) | 0% (0/3) | 35 |
| `ubuntu-24.04-arm` | github-hosted | 36 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26497517424/job/78029369702) | [1m09s](https://github.com/iree-org/iree/actions/runs/26497809643/job/78030278137) | 0% (0/6) | 36 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 7 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26496087619/job/78032596079) | [15s](https://github.com/iree-org/iree/actions/runs/26497809642/job/78054136885) | 0% (0/1) | 7 |
| `ubuntu-latest` | github-hosted | 30 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26509237835/job/78069497234) | [3s](https://github.com/iree-org/iree/actions/runs/26514267845/job/78086834863) | 0% (0/6) | 30 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26506087959/job/78058718749) | [2s](https://github.com/iree-org/iree/actions/runs/26506087959/job/78058718749) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 11 | 0 | — | — | [24m05s](https://github.com/iree-org/iree/actions/runs/26496087619/job/78024555371) | [2h17m](https://github.com/iree-org/iree/actions/runs/26497809642/job/78030279775) | [2h17m](https://github.com/iree-org/iree/actions/runs/26497809642/job/78030279775) | 9 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 11 | 0 | — | — | [1m13s](https://github.com/iree-org/iree/actions/runs/26514270484/job/78086878108) | [2h17m](https://github.com/iree-org/iree/actions/runs/26497809643/job/78030278415) | [2h17m](https://github.com/iree-org/iree/actions/runs/26497809643/job/78030278415) | 10 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 11 | 0 | — | — | [2m23s](https://github.com/iree-org/iree/actions/runs/26492966519/job/78014539773) | [2h14m](https://github.com/iree-org/iree/actions/runs/26497809643/job/78030278339) | [2h14m](https://github.com/iree-org/iree/actions/runs/26497809643/job/78030278339) | 10 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 11 | 0 | — | — | [36s](https://github.com/iree-org/iree/actions/runs/26493359399/job/78015962136) | [2h13m](https://github.com/iree-org/iree/actions/runs/26497809643/job/78030278195) | [2h13m](https://github.com/iree-org/iree/actions/runs/26497809643/job/78030278195) | 10 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 7 | 0 | — | — | [28m25s](https://github.com/iree-org/iree/actions/runs/26497809642/job/78054137085) | [1h51m](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065370903) | [1h51m](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065370903) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 7 | 0 | — | — | [1h00m](https://github.com/iree-org/iree/actions/runs/26497809642/job/78054136956) | [1h51m](https://github.com/iree-org/iree/actions/runs/26497517427/job/78043870350) | [1h51m](https://github.com/iree-org/iree/actions/runs/26497517427/job/78043870350) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 5 | 0 | — | — | [40m47s](https://github.com/iree-org/iree/actions/runs/26496087647/job/78024558411) | [1h42m](https://github.com/iree-org/iree/actions/runs/26497809643/job/78030278417) | [1h42m](https://github.com/iree-org/iree/actions/runs/26497809643/job/78030278417) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 11 | 0 | — | — | [25m13s](https://github.com/iree-org/iree/actions/runs/26496087647/job/78024558284) | [1h42m](https://github.com/iree-org/iree/actions/runs/26497809643/job/78030278335) | [1h42m](https://github.com/iree-org/iree/actions/runs/26497809643/job/78030278335) | 10 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 7 | 0 | — | — | [39m25s](https://github.com/iree-org/iree/actions/runs/26497073791/job/78043789617) | [1h15m](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371065) | [1h15m](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371065) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 7 | 0 | — | — | [22m12s](https://github.com/iree-org/iree/actions/runs/26496087619/job/78032596126) | [55m03s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065370905) | [55m03s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065370905) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 7 | 0 | — | — | [19m05s](https://github.com/iree-org/iree/actions/runs/26497517427/job/78043870284) | [52m59s](https://github.com/iree-org/iree/actions/runs/26497073791/job/78043789606) | [52m59s](https://github.com/iree-org/iree/actions/runs/26497073791/job/78043789606) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 7 | 0 | — | — | [11m11s](https://github.com/iree-org/iree/actions/runs/26496087619/job/78032596169) | [47m20s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371020) | [47m20s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371020) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 7 | 0 | — | — | [19m28s](https://github.com/iree-org/iree/actions/runs/26496087619/job/78032596315) | [46m23s](https://github.com/iree-org/iree/actions/runs/26497517427/job/78043870184) | [46m23s](https://github.com/iree-org/iree/actions/runs/26497517427/job/78043870184) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 7 | 0 | — | — | [16m08s](https://github.com/iree-org/iree/actions/runs/26496087619/job/78032596177) | [45m05s](https://github.com/iree-org/iree/actions/runs/26497517427/job/78043870240) | [45m05s](https://github.com/iree-org/iree/actions/runs/26497517427/job/78043870240) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 7 | 0 | — | — | [24m41s](https://github.com/iree-org/iree/actions/runs/26493359398/job/78017086443) | [44m32s](https://github.com/iree-org/iree/actions/runs/26497517427/job/78043870278) | [44m32s](https://github.com/iree-org/iree/actions/runs/26497517427/job/78043870278) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 7 | 0 | — | — | [14m32s](https://github.com/iree-org/iree/actions/runs/26496087619/job/78032596292) | [41m43s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371091) | [41m43s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371091) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 7 | 0 | — | — | [9m37s](https://github.com/iree-org/iree/actions/runs/26497809642/job/78054137034) | [38m40s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371097) | [38m40s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371097) | 4 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 7 | 0 | — | — | [12m10s](https://github.com/iree-org/iree/actions/runs/26493359398/job/78017086285) | [34m32s](https://github.com/iree-org/iree/actions/runs/26497809642/job/78054136825) | [34m32s](https://github.com/iree-org/iree/actions/runs/26497809642/job/78054136825) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 7 | 0 | — | — | [11m37s](https://github.com/iree-org/iree/actions/runs/26497809642/job/78054137131) | [30m34s](https://github.com/iree-org/iree/actions/runs/26493359398/job/78017086516) | [30m34s](https://github.com/iree-org/iree/actions/runs/26493359398/job/78017086516) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 7 | 0 | — | — | [7m47s](https://github.com/iree-org/iree/actions/runs/26507618165/job/78065371027) | [26m34s](https://github.com/iree-org/iree/actions/runs/26497517427/job/78043870369) | [26m34s](https://github.com/iree-org/iree/actions/runs/26497517427/job/78043870369) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 302 | 2% (6/302) |  | 19m14s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 275 | 6% (17/275) |  | 55m55s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 221 | 4% (8/221) |  | 1h11m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 224 | 1% (2/224) |  | 1h22m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 72 | 3% (2/72) |  | 2h06m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h51m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h15m (> 1h00m)
- **[queue-starved]** `azure-linux-scale` p95 queue 2h13m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
