# iree-ci-monitor

_Updated: 2026-09-11 21:40 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [13m07s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182159) | [44m42s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227862) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 7 | 1 | [2h00m](https://github.com/iree-org/iree/actions/runs/34581758865/job/103214541971) | 2026-09-11 04:27 PDT | 0 | [16m27s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182100) | [24m10s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227890) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [7m43s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403166135) | [16m47s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182343) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403165970) | [16m04s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227736) | 50% (1/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [2m26s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403166023) | [11m36s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227886) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [6m27s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403165998) | [10m20s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182161) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [6m48s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403165928) | [10m13s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182094) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [3m19s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403166003) | [9m46s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182004) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [7m21s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227921) | [9m42s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403166014) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [5m05s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403166063) | [5m35s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227718) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403165865) | [4m16s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182015) | 100% (1/1) | `shark10-ci` |
| `azure-linux-scale` | ossci | 16 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103400638816) | [1m42s](https://github.com/iree-org/iree/actions/runs/34637491884/job/103388906646) | 0% (0/6) | 16 |
| `macos-14` | github-hosted | 9 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/34637491884/job/103388906415) | [9s](https://github.com/iree-org/iree/actions/runs/34657817116/job/103453943902) | 0% (0/3) | 9 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/34640973125/job/103400817031) | [5s](https://github.com/iree-org/iree/actions/runs/34637491884/job/103388906488) | 0% (0/3) | 9 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34658155135/job/103454900663) | [4s](https://github.com/iree-org/iree/actions/runs/34657815691/job/103453905679) | 0% (0/3) | 9 |
| `ubuntu-24.04` | github-hosted | 66 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103453906812) | [3s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403166113) | 5% (1/20) | 65 |
| `windows-2022` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34657817116/job/103453943753) | [3s](https://github.com/iree-org/iree/actions/runs/34637491884/job/103388906494) | 0% (0/3) | 9 |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/34640973125/job/103400817120) | [1s](https://github.com/iree-org/iree/actions/runs/34657817116/job/103453943871) | 0% (0/1) | 3 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [2h00m](https://github.com/iree-org/iree/actions/runs/34581758865/job/103214541971) | 2026-09-11 04:27 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 1 | [2h00m](https://github.com/iree-org/iree/actions/runs/34581758865/job/103214541971) | 2026-09-11 04:27 PDT | [16m27s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182100) | [18m55s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227751) | [18m55s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227751) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [13m07s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182159) | [44m42s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227862) | [44m42s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227862) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [22m29s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182348) | [24m10s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227890) | [24m10s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227890) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [7m58s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403166030) | [16m47s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182343) | [16m47s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182343) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403165967) | [16m04s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227736) | [16m04s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227736) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [4m39s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182223) | [13m03s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227863) | [13m03s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227863) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [7m43s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403166135) | [12m22s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182181) | [12m22s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182181) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [2m26s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403166023) | [11m36s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227886) | [11m36s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227886) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [5m19s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403166072) | [11m05s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227814) | [11m05s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227814) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [6m27s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403165998) | [10m20s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182161) | [10m20s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182161) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [6m48s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403165928) | [10m13s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182094) | [10m13s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182094) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [3m19s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403166003) | [9m46s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182004) | [9m46s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182004) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [7m21s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227921) | [9m42s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403166014) | [9m42s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403166014) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [5m05s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403166063) | [5m35s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227718) | [5m35s](https://github.com/iree-org/iree/actions/runs/34657817050/job/103455227718) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34640973166/job/103403165865) | [4m16s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182015) | [4m16s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182015) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/34637491884/job/103388906585) | [1m47s](https://github.com/iree-org/iree/actions/runs/34657817116/job/103453943888) | [1m47s](https://github.com/iree-org/iree/actions/runs/34657817116/job/103453943888) | 3 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 3 | 0 | — | — | [1m20s](https://github.com/iree-org/iree/actions/runs/34657817116/job/103453943800) | [1m42s](https://github.com/iree-org/iree/actions/runs/34637491884/job/103388906646) | [1m42s](https://github.com/iree-org/iree/actions/runs/34637491884/job/103388906646) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/34640973125/job/103400817158) | [1m38s](https://github.com/iree-org/iree/actions/runs/34657817116/job/103453943894) | [1m38s](https://github.com/iree-org/iree/actions/runs/34657817116/job/103453943894) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [1m35s](https://github.com/iree-org/iree/actions/runs/34657817116/job/103453944000) | [1m35s](https://github.com/iree-org/iree/actions/runs/34657817116/job/103453944000) | [1m35s](https://github.com/iree-org/iree/actions/runs/34657817116/job/103453944000) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 3 | 0 | — | — | [1m22s](https://github.com/iree-org/iree/actions/runs/34637491884/job/103388906563) | [1m33s](https://github.com/iree-org/iree/actions/runs/34657817116/job/103453943865) | [1m33s](https://github.com/iree-org/iree/actions/runs/34657817116/job/103453943865) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 254 | 8% (20/254) |  | 4h21m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 284 | 1% (4/284) |  | 4h35m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 214 | 1% (3/214) |  | 4h46m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 208 | 1% (2/208) |  | 4h53m ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 2h00m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
