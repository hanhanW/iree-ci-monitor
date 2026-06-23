# iree-ci-monitor

_Updated: 2026-06-23 12:01 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [22m35s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815140) | [30m42s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257658) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257362) | [23m23s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815011) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [5m33s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815103) | [21m22s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815151) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [13m15s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257385) | [17m08s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815081) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [6m48s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257438) | [17m00s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815057) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [16m01s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815078) | [16m44s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257387) | 0% (0/1) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [13m08s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257676) | [15m18s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815088) | 0% (0/2) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815086) | [12m21s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257492) | 0% (0/1) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [8m02s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257776) | [9m49s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815159) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 15 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/28021790536/job/82939683036) | [1m46s](https://github.com/iree-org/iree/actions/runs/28019530869/job/82932085450) | 0% (0/9) | 15 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m32s](https://github.com/iree-org/iree/actions/runs/28019544193/job/82932124574) | [1m32s](https://github.com/iree-org/iree/actions/runs/28019544193/job/82932124574) | 0% (0/1) | 1 |
| `macos-14` | github-hosted | 7 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28034874073/job/82985394319) | [46s](https://github.com/iree-org/iree/actions/runs/28021790536/job/82939683021) | 0% (0/4) | 7 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/28034874073/job/82985394264) | [36s](https://github.com/iree-org/iree/actions/runs/28021790536/job/82939683064) | 0% (0/3) | 6 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815112) | [19s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257273) | 0% (0/4) | 8 |
| `ubuntu-24.04` | github-hosted | 46 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257309) | [12s](https://github.com/iree-org/iree/actions/runs/28019542273/job/82932118509) | 5% (1/21) | 46 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/28019510129/job/82932022905) | [6s](https://github.com/iree-org/iree/actions/runs/28019510129/job/82932022905) | 0% (0/1) | 1 |
| `ubuntu-latest` | github-hosted | 21 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28034872716/job/82985360633) | [4s](https://github.com/iree-org/iree/actions/runs/28021785021/job/82939626495) | 0% (0/3) | 21 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/28021790536/job/82939682857) | [4s](https://github.com/iree-org/iree/actions/runs/28021790536/job/82939682915) | 0% (0/3) | 6 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28021790536/job/82939683067) | [2s](https://github.com/iree-org/iree/actions/runs/28034874073/job/82985394486) | 0% (0/1) | 2 |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944814856) | [2s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257154) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944814858) | [2s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257185) | 0% (0/1) | `shark01-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815039) | [2s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257791) | 0% (0/1) | `iree-mi308-1` |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 6 | [22h34m](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161046) | 2026-06-23 12:00 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [22h34m](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161046) | 2026-06-23 12:00 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [21h01m](https://github.com/iree-org/iree/actions/runs/27986362178/job/82830228625) | 2026-06-23 12:00 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `dependabot/github_actions/github-actions-ad4787fcfd` | pull_request |
| [11h48m](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330192) | 2026-06-23 12:00 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [10h31m](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438192) | 2026-06-23 12:00 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `devtbi/tduf` | pull_request |
| [7h23m](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944814860) | 2026-06-23 12:00 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `integrates/llvm-20260623` | pull_request |
| [3h45m](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257221) | 2026-06-23 12:00 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 6 | 6 | [22h34m](https://github.com/iree-org/iree/actions/runs/27981246251/job/82813161046) | 2026-06-23 12:00 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [22m35s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815140) | [30m42s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257658) | [30m42s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257658) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257362) | [23m23s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815011) | [23m23s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815011) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [3m22s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257640) | [21m22s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815151) | [21m22s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815151) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [6m50s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815104) | [19m18s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257589) | [19m18s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257589) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [13m15s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257385) | [17m08s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815081) | [17m08s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815081) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [6m48s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257438) | [17m00s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815057) | [17m00s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815057) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [16m01s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815078) | [16m44s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257387) | [16m44s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257387) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [6m47s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257474) | [15m18s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815088) | [15m18s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815088) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815019) | [13m08s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257676) | [13m08s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257676) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815086) | [12m21s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257492) | [12m21s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257492) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [8m02s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257776) | [9m49s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815159) | [9m49s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815159) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [7m35s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815095) | [7m44s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257460) | [7m44s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257460) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257425) | [5m33s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815103) | [5m33s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944815103) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28021790375/job/82939677051) | [2m06s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82985406580) | [2m06s](https://github.com/iree-org/iree/actions/runs/28034874087/job/82985406580) | 2 |
| `.github/workflows/ci_linux_x64_clang_tsan.yml` | linux_x64_clang_tsan | `azure-linux-scale` | 1 | 0 | — | — | [1m46s](https://github.com/iree-org/iree/actions/runs/28019530869/job/82932085450) | [1m46s](https://github.com/iree-org/iree/actions/runs/28019530869/job/82932085450) | [1m46s](https://github.com/iree-org/iree/actions/runs/28019530869/job/82932085450) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/28021790536/job/82939683036) | [1m44s](https://github.com/iree-org/iree/actions/runs/28034874073/job/82985394483) | [1m44s](https://github.com/iree-org/iree/actions/runs/28034874073/job/82985394483) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/28021790536/job/82939682940) | [1m43s](https://github.com/iree-org/iree/actions/runs/28034874073/job/82985394407) | [1m43s](https://github.com/iree-org/iree/actions/runs/28034874073/job/82985394407) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/28021790536/job/82939683015) | [1m43s](https://github.com/iree-org/iree/actions/runs/28034874073/job/82985394421) | [1m43s](https://github.com/iree-org/iree/actions/runs/28034874073/job/82985394421) | 2 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m32s](https://github.com/iree-org/iree/actions/runs/28019544193/job/82932124574) | [1m32s](https://github.com/iree-org/iree/actions/runs/28019544193/job/82932124574) | [1m32s](https://github.com/iree-org/iree/actions/runs/28019544193/job/82932124574) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 168 | 0% (0/168) |  | 3h09m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 132 | 0% (0/132) |  | 3h23m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 130 | 5% (6/130) |  | 3h24m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 114 | 0% (0/114) |  | 3h28m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 37 | 0% (0/37) |  | 3h34m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 22h34m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
