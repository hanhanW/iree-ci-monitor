# iree-ci-monitor

_Updated: 2026-06-23 00:34 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 1 | [20m57s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330160) | [30m50s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228590) | — | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 1 | [21m17s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330276) | 2026-06-23 00:33 PDT | 0 | [9m19s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228654) | [25m23s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228712) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 1 | [21m17s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330325) | 2026-06-23 00:33 PDT | 0 | [19m54s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228643) | [19m54s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228643) | — | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330289) | [19m45s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228636) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 1 | [10m19s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330283) | [16m54s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330370) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [6m39s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330288) | [13m09s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228665) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [5m39s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228675) | [12m36s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330342) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228678) | [11m37s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330176) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330097) | [10m55s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228614) | 0% (0/1) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228642) | [10m28s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330230) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228661) | [5m30s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330168) | 0% (0/1) | `shark10-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m29s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716180) | [1m29s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716180) | — | 1 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 2 | [6s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828715918) | [1m12s](https://github.com/iree-org/iree/actions/runs/28008559577/job/82896102986) | 0% (0/3) | 9 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228672) | [39s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228682) | 0% (0/4) | 8 |
| `macos-14` | github-hosted | 9 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716103) | [39s](https://github.com/iree-org/iree/actions/runs/28008559577/job/82896102987) | 0% (0/3) | 9 |
| `azure-linux-scale` | ossci | 13 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716245) | [13s](https://github.com/iree-org/iree/actions/runs/28008559577/job/82896103095) | 0% (0/6) | 13 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716200) | [5s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716200) | — | 1 |
| `windows-2022` | github-hosted | 8 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/28006849909/job/82890706668) | [4s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828715867) | 0% (0/3) | 8 |
| `ubuntu-24.04` | github-hosted | 48 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/28006849909/job/82890679500) | [3s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330205) | 10% (2/21) | 48 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228687) | [2s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330198) | 0% (0/1) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28008559577/job/82896103198) | [2s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716198) | 0% (0/1) | 2 |
| `ubuntu-latest` | github-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28008558248/job/82896074610) | [2s](https://github.com/iree-org/iree/actions/runs/28008558248/job/82896074613) | 0% (0/4) | 4 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 6 | [22h07m](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202183) | 2026-06-23 00:33 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [22h07m](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202183) | 2026-06-23 00:33 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [16h21m](https://github.com/iree-org/iree/actions/runs/27962454635/job/82749317105) | 2026-06-23 00:33 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `add-gpu-ada-known-target` | pull_request |
| [15h51m](https://github.com/iree-org/iree/actions/runs/27964465747/job/82756223051) | 2026-06-23 00:33 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `devtbi/tduf` | pull_request |
| [11h07m](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161046) | 2026-06-23 00:33 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [9h34m](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228625) | 2026-06-23 00:33 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `dependabot/github_actions/github-actions-ad4787fcfd` | pull_request |
| [21m18s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330192) | 2026-06-23 00:33 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [21m17s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330276) | 2026-06-23 00:33 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |
| [21m17s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330325) | 2026-06-23 00:33 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 6 | 6 | [22h07m](https://github.com/iree-org/iree/actions/runs/27942341280/job/82680202183) | 2026-06-23 00:33 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [20m57s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330160) | [30m50s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228590) | [30m50s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228590) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [5m54s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330345) | [25m23s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228712) | [25m23s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228712) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 1 | [21m17s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330325) | 2026-06-23 00:33 PDT | [19m54s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228643) | [19m54s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228643) | [19m54s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228643) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 1 | [21m17s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330276) | 2026-06-23 00:33 PDT | [9m19s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228654) | [9m19s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228654) | [9m19s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228654) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330289) | [19m45s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228636) | [19m45s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228636) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [6m41s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228724) | [16m54s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330370) | [16m54s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330370) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [6m39s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330288) | [13m09s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228665) | [13m09s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228665) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [3m28s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228709) | [12m36s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330342) | [12m36s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330342) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228678) | [11m37s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330176) | [11m37s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330176) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330097) | [10m55s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228614) | [10m55s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228614) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228642) | [10m28s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330230) | [10m28s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330230) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [4m16s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228695) | [10m19s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330283) | [10m19s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330283) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330300) | [5m39s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228675) | [5m39s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228675) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228661) | [5m30s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330168) | [5m30s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330168) | 1 |
| `.github/workflows/ci.yml` | linux_arm64_clang / linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m29s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716180) | [1m29s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716180) | [1m29s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716180) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 2 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828715918) | [1m12s](https://github.com/iree-org/iree/actions/runs/28008559577/job/82896102986) | [1m12s](https://github.com/iree-org/iree/actions/runs/28008559577/job/82896102986) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828715952) | [1m03s](https://github.com/iree-org/iree/actions/runs/28008559577/job/82896102933) | [1m03s](https://github.com/iree-org/iree/actions/runs/28008559577/job/82896102933) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27986362190/job/82828716059) | [39s](https://github.com/iree-org/iree/actions/runs/28008559577/job/82896102987) | [39s](https://github.com/iree-org/iree/actions/runs/28008559577/job/82896102987) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330228) | [39s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228682) | [39s](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228682) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 154 | 0% (0/153) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 121 | 0% (0/120) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 119 | 4% (5/119) |  | 27s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 103 | 0% (0/103) |  | 3m54s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 34 | 0% (0/34) |  | 11m16s ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 22h07m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
