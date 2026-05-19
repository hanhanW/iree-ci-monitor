# iree-ci-monitor

_Updated: 2026-05-19 00:33 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 1 | [27m22s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045506) | [27m22s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045506) | — | `shark01-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 1 | [22m14s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045410) | [22m14s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045410) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045627) | [20m09s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045656) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045654) | [17m17s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045676) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [8m11s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045714) | [14m13s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045635) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [14m04s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045593) | [14m04s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045593) | — | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [10m51s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045606) | [10m51s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045606) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [7m40s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045537) | [7m40s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045537) | — | `shark01-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [1m58s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045562) | [2m16s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045612) | — | 4 |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 1 | [1m33s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772318) | [2m05s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76683771928) | — | 5 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772454) | [4s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772294) | — | 5 |
| `ubuntu-24.04` | github-hosted | 27 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772344) | [3s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045866) | 50% (2/4) | 27 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772311) | [3s](https://github.com/iree-org/iree/actions/runs/26080314298/job/76680227522) | — | 5 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/26080314298/job/76680227453) | [3s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772277) | — | 6 |
| `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26081177502/job/76682967064) | [3s](https://github.com/iree-org/iree/actions/runs/26081177502/job/76682967064) | 0% (0/1) | 1 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045524) | [2s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045524) | — | `iree-mi308-1` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045544) | [2s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045561) | — | `shark01-ci`, `shark10-ci` |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045564) | [2s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045564) | — | 1 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772308) | [1s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772308) | — | 1 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 1 | [28m37s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045416) | 2026-05-19 00:32 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 1 | [28m37s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045630) | 2026-05-19 00:32 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [28m37s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045416) | 2026-05-19 00:32 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | `dependabot/github_actions/github-actions-a21b3a5a8e` | pull_request |
| [28m37s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045630) | 2026-05-19 00:32 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `dependabot/github_actions/github-actions-a21b3a5a8e` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 1 | [28m37s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045630) | 2026-05-19 00:32 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 1 | [28m37s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045416) | 2026-05-19 00:32 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [27m22s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045506) | [27m22s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045506) | [27m22s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045506) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [22m14s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045410) | [22m14s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045410) | [22m14s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045410) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [20m09s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045656) | [20m09s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045656) | [20m09s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045656) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [17m17s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045676) | [17m17s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045676) | [17m17s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045676) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [14m13s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045635) | [14m13s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045635) | [14m13s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045635) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [14m04s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045593) | [14m04s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045593) | [14m04s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045593) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [10m51s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045606) | [10m51s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045606) | [10m51s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045606) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [8m11s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045714) | [8m11s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045714) | [8m11s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045714) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [7m40s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045537) | [7m40s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045537) | [7m40s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045537) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [2m16s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045612) | [2m16s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045612) | [2m16s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045612) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [2m05s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76683771928) | [2m05s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76683771928) | [2m05s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76683771928) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [1m58s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045562) | [1m58s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045562) | [1m58s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045562) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [1m57s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772305) | [1m57s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772305) | [1m57s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772305) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 1 | 0 | — | — | [1m52s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045585) | [1m52s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045585) | [1m52s](https://github.com/iree-org/iree/actions/runs/26081417837/job/76685045585) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [1m33s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772318) | [1m33s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772318) | [1m33s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772318) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [1m18s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772296) | [1m18s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772296) | [1m18s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772296) | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 1 | 0 | — | — | [57s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772273) | [57s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772273) | [57s](https://github.com/iree-org/iree/actions/runs/26081417906/job/76683772273) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/26080314298/job/76680227551) | [4s](https://github.com/iree-org/iree/actions/runs/26080314298/job/76680227551) | [4s](https://github.com/iree-org/iree/actions/runs/26080314298/job/76680227551) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 770 | 1% (11/769) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 934 | 2% (19/932) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 819 | 5% (44/818) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 751 | 1% (8/751) |  | 3m34s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 258 | 1% (3/258) |  | 18m13s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
