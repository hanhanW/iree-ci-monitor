# iree-ci-monitor

_Updated: 2026-07-13 17:50 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [27m58s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967407) | [28m29s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003390) | 0% (0/1) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [7m54s](https://github.com/iree-org/iree/actions/runs/29261977791/job/86859518516) | [24m36s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967590) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [15m28s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86870608922) | [20m24s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967304) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [5m19s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86870609141) | [19m36s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003490) | 0% (0/2) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [9m46s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967570) | [19m11s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003561) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [7m51s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86870609041) | [17m50s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003477) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [9m43s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003335) | [14m16s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967512) | 0% (0/1) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [4m21s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967281) | [13m51s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86870608906) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [3m24s](https://github.com/iree-org/iree/actions/runs/29261977791/job/86859518269) | [11m32s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86870608990) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [5m22s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003316) | [11m06s](https://github.com/iree-org/iree/actions/runs/29261977791/job/86859518374) | 0% (0/1) | `shark75-ci` |
| `azure-linux-scale` | ossci | 21 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/29265214106/job/86868570370) | [1m55s](https://github.com/iree-org/iree/actions/runs/29261977977/job/86857428503) | 0% (0/6) | 21 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/29261977977/job/86857428325) | [6s](https://github.com/iree-org/iree/actions/runs/29267996888/job/86878298958) | 0% (0/3) | 12 |
| `ubuntu-24.04` | github-hosted | 79 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29278671856/job/86919953409) | [5s](https://github.com/iree-org/iree/actions/runs/29267996888/job/86878298854) | 11% (2/19) | 79 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003185) | [5s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967332) | 0% (0/1) | 4 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29278671856/job/86919953956) | [4s](https://github.com/iree-org/iree/actions/runs/29261977977/job/86857428489) | 100% (1/1) | 4 |
| `ubuntu-latest` | github-hosted | 11 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29260516018/job/86852240526) | [4s](https://github.com/iree-org/iree/actions/runs/29265212867/job/86868850446) | 0% (0/5) | 11 |
| `macos-14` | github-hosted | 12 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29261977977/job/86857428344) | [3s](https://github.com/iree-org/iree/actions/runs/29267996888/job/86878298921) | 0% (0/3) | 12 |
| `windows-2022` | github-hosted | 12 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29265214106/job/86868570372) | [3s](https://github.com/iree-org/iree/actions/runs/29267996888/job/86878298966) | 0% (0/3) | 12 |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003144) | [2s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967293) | 100% (1/1) | `shark01-ci`, `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003326) | [2s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967256) | 0% (0/1) | `iree-mi308-1` |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 2 | 2 | [13h36m](https://github.com/iree-org/iree/actions/runs/29243794150/job/86801338899) | 2026-07-13 17:50 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [13h36m](https://github.com/iree-org/iree/actions/runs/29243794150/job/86801338899) | 2026-07-13 17:50 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/rvv_tile_size_selection` | pull_request |
| [13h27m](https://github.com/iree-org/iree/actions/runs/29243839489/job/86803078372) | 2026-07-13 17:50 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/egebeysel/rvv_scalable_vectorization` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 2 | 2 | [13h36m](https://github.com/iree-org/iree/actions/runs/29243794150/job/86801338899) | 2026-07-13 17:50 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [27m58s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967407) | [28m29s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003390) | [28m29s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003390) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [7m54s](https://github.com/iree-org/iree/actions/runs/29261977791/job/86859518516) | [24m36s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967590) | [24m36s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967590) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [15m28s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86870608922) | [20m24s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967304) | [20m24s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967304) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [18m00s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967592) | [19m36s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003490) | [19m36s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003490) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [9m46s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967570) | [19m11s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003561) | [19m11s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003561) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [15m33s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967648) | [17m50s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003477) | [17m50s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003477) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [9m52s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003391) | [14m29s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967494) | [14m29s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967494) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [9m43s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003335) | [14m16s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967512) | [14m16s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967512) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [4m21s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967281) | [13m51s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86870608906) | [13m51s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86870608906) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [7m03s](https://github.com/iree-org/iree/actions/runs/29261977791/job/86859518594) | [11m32s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86870608990) | [11m32s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86870608990) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [4m49s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967530) | [11m25s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003352) | [11m25s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003352) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [5m22s](https://github.com/iree-org/iree/actions/runs/29267996883/job/86880003316) | [11m06s](https://github.com/iree-org/iree/actions/runs/29261977791/job/86859518374) | [11m06s](https://github.com/iree-org/iree/actions/runs/29261977791/job/86859518374) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [5m48s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86921967575) | [7m51s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86870609041) | [7m51s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86870609041) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [3m24s](https://github.com/iree-org/iree/actions/runs/29261977791/job/86859518269) | [7m42s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86870609091) | [7m42s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86870609091) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 4 | 0 | — | — | [46s](https://github.com/iree-org/iree/actions/runs/29267996888/job/86878299076) | [1m56s](https://github.com/iree-org/iree/actions/runs/29261977977/job/86857428599) | [1m56s](https://github.com/iree-org/iree/actions/runs/29261977977/job/86857428599) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 4 | 0 | — | — | [20s](https://github.com/iree-org/iree/actions/runs/29267996888/job/86878299035) | [1m55s](https://github.com/iree-org/iree/actions/runs/29261977977/job/86857428503) | [1m55s](https://github.com/iree-org/iree/actions/runs/29261977977/job/86857428503) | 4 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 4 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/29265214260/job/86868582668) | [1m35s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86919955368) | [1m35s](https://github.com/iree-org/iree/actions/runs/29278671928/job/86919955368) | 4 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/29265214106/job/86868570370) | [41s](https://github.com/iree-org/iree/actions/runs/29261977977/job/86857428472) | [41s](https://github.com/iree-org/iree/actions/runs/29261977977/job/86857428472) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 4 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/29265214106/job/86868570623) | [41s](https://github.com/iree-org/iree/actions/runs/29261977977/job/86857428650) | [41s](https://github.com/iree-org/iree/actions/runs/29261977977/job/86857428650) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 129 | 10% (13/128) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 138 | 1% (1/137) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 162 | 2% (3/161) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 120 | 1% (1/119) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 38 | 13% (5/38) |  | 4h34m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 13h36m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
