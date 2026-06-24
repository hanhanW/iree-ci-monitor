# iree-ci-monitor

_Updated: 2026-06-24 11:56 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 6 | 0 | — | — | 0 | [28m04s](https://github.com/iree-org/iree/actions/runs/28107886109/job/83228909213) | [34m08s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554303) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [4m15s](https://github.com/iree-org/iree/actions/runs/28101697435/job/83220582077) | [32m22s](https://github.com/iree-org/iree/actions/runs/28102210744/job/83208735576) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [15m37s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261825) | [30m44s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184606) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [15m37s](https://github.com/iree-org/iree/actions/runs/28107886109/job/83228909126) | [28m56s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184635) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [5m53s](https://github.com/iree-org/iree/actions/runs/28102210744/job/83208735731) | [25m40s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554191) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | [9m05s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261653) | [24m21s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184284) | 0% (0/3) | `shark01-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | — | 0 | [12m46s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261732) | [21m56s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184554) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [9m34s](https://github.com/iree-org/iree/actions/runs/28101697435/job/83220582221) | [17m46s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554210) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 6 | 0 | — | — | 0 | [2m18s](https://github.com/iree-org/iree/actions/runs/28101697435/job/83220582119) | [15m34s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261770) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [7m36s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554108) | [10m15s](https://github.com/iree-org/iree/actions/runs/28101697435/job/83220582113) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [4m36s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554134) | [9m03s](https://github.com/iree-org/iree/actions/runs/28101697435/job/83220582095) | 33% (2/6) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28107886210/job/83227053945) | [5m27s](https://github.com/iree-org/iree/actions/runs/28102340259/job/83207384329) | 0% (0/3) | 6 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554150) | [4m09s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184392) | 0% (0/3) | `iree-mi308-1` |
| `azure-linux-scale` | ossci | 35 | 0 | — | — | 0 | [27s](https://github.com/iree-org/iree/actions/runs/28102210763/job/83206944267) | [3m23s](https://github.com/iree-org/iree/actions/runs/28102340259/job/83207384403) | 0% (0/20) | 35 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 24 | 0 | — | — | 0 | [19s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261647) | [3m13s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261817) | 0% (0/12) | 24 |
| `windows-2022` | github-hosted | 18 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28101697372/job/83219071528) | [2m18s](https://github.com/iree-org/iree/actions/runs/28102340259/job/83207384128) | 0% (0/9) | 18 |
| `macos-14` | github-hosted | 19 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28102210763/job/83206944205) | [2m15s](https://github.com/iree-org/iree/actions/runs/28102340259/job/83207384194) | 0% (0/10) | 19 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m28s](https://github.com/iree-org/iree/actions/runs/28091828575/job/83171474390) | [1m28s](https://github.com/iree-org/iree/actions/runs/28091828575/job/83171474390) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/28101697372/job/83219071418) | [1m14s](https://github.com/iree-org/iree/actions/runs/28090664452/job/83178150313) | 0% (0/9) | 18 |
| `ubuntu-24.04` | github-hosted | 135 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28107886109/job/83228909246) | [27s](https://github.com/iree-org/iree/actions/runs/28102341524/job/83207426815) | 9% (5/57) | 131 |
| `ubuntu-latest` | github-hosted | 27 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28095981924/job/83185471581) | [11s](https://github.com/iree-org/iree/actions/runs/28107959907/job/83227276140) | 0% (0/9) | 27 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28091803077/job/83171386382) | [3s](https://github.com/iree-org/iree/actions/runs/28091803077/job/83171386382) | 0% (0/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 7 | 7 | [22h18m](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409541) | 2026-06-24 11:56 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [22h18m](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409541) | 2026-06-24 11:56 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/bjacob/cpu-ukernel-pipeline-test` | pull_request |
| [7h31m](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261695) | 2026-06-24 11:56 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `flow_empty_fold` | pull_request |
| [6h50m](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554091) | 2026-06-24 11:56 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [5h16m](https://github.com/iree-org/iree/actions/runs/28102210744/job/83208735459) | 2026-06-24 11:56 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [5h10m](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184300) | 2026-06-24 11:56 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/bjacob/cpu-ukernel-bodies` | pull_request |
| [4h24m](https://github.com/iree-org/iree/actions/runs/28101697435/job/83220582315) | 2026-06-24 11:56 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `fix-24624-raise-special-ops-memref-crash` | pull_request |
| [3h49m](https://github.com/iree-org/iree/actions/runs/28107886109/job/83228908779) | 2026-06-24 11:56 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 7 | 7 | [22h18m](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409541) | 2026-06-24 11:56 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [10m59s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261830) | [38m04s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184612) | [38m04s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184612) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 6 | 0 | — | — | [28m04s](https://github.com/iree-org/iree/actions/runs/28107886109/job/83228909213) | [34m08s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554303) | [34m08s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554303) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [4m15s](https://github.com/iree-org/iree/actions/runs/28101697435/job/83220582077) | [32m22s](https://github.com/iree-org/iree/actions/runs/28102210744/job/83208735576) | [32m22s](https://github.com/iree-org/iree/actions/runs/28102210744/job/83208735576) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [11m22s](https://github.com/iree-org/iree/actions/runs/28101697435/job/83220582013) | [30m44s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184606) | [30m44s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184606) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [15m37s](https://github.com/iree-org/iree/actions/runs/28107886109/job/83228909126) | [28m56s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184635) | [28m56s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184635) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 6 | 0 | — | — | [5m53s](https://github.com/iree-org/iree/actions/runs/28102210744/job/83208735731) | [25m40s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554191) | [25m40s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554191) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 6 | 0 | — | — | [9m05s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261653) | [24m21s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184284) | [24m21s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184284) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [8m24s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261818) | [23m23s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184628) | [23m23s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184628) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [12m46s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261732) | [22m05s](https://github.com/iree-org/iree/actions/runs/28102210744/job/83208735632) | [22m05s](https://github.com/iree-org/iree/actions/runs/28102210744/job/83208735632) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [5m57s](https://github.com/iree-org/iree/actions/runs/28101697435/job/83220582237) | [17m38s](https://github.com/iree-org/iree/actions/runs/28102210744/job/83208735732) | [17m38s](https://github.com/iree-org/iree/actions/runs/28102210744/job/83208735732) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [9m19s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554121) | [17m33s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184589) | [17m33s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184589) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261692) | [16m36s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184454) | [16m36s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184454) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 6 | 0 | — | — | [2m18s](https://github.com/iree-org/iree/actions/runs/28101697435/job/83220582119) | [15m34s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261770) | [15m34s](https://github.com/iree-org/iree/actions/runs/28090664399/job/83182261770) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [7m36s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554108) | [10m15s](https://github.com/iree-org/iree/actions/runs/28101697435/job/83220582113) | [10m15s](https://github.com/iree-org/iree/actions/runs/28101697435/job/83220582113) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [4m36s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554134) | [9m03s](https://github.com/iree-org/iree/actions/runs/28101697435/job/83220582095) | [9m03s](https://github.com/iree-org/iree/actions/runs/28101697435/job/83220582095) | 4 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 6 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28107886210/job/83227053945) | [5m27s](https://github.com/iree-org/iree/actions/runs/28102340259/job/83207384329) | [5m27s](https://github.com/iree-org/iree/actions/runs/28102340259/job/83207384329) | 6 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28096680153/job/83189554150) | [4m09s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184392) | [4m09s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83210184392) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 6 | 0 | — | — | [1m34s](https://github.com/iree-org/iree/actions/runs/28101697372/job/83219071600) | [3m55s](https://github.com/iree-org/iree/actions/runs/28102340259/job/83207384458) | [3m55s](https://github.com/iree-org/iree/actions/runs/28102340259/job/83207384458) | 6 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28102210744/job/83206937179) | [3m53s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83207394700) | [3m53s](https://github.com/iree-org/iree/actions/runs/28102340241/job/83207394700) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 125 | 6% (7/125) |  | 3h18m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 114 | 0% (0/114) |  | 3h26m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 161 | 0% (0/161) |  | 3h30m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 129 | 0% (0/129) |  | 3h33m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 36 | 0% (0/36) |  | 3h39m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 22h18m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
