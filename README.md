# iree-ci-monitor

_Updated: 2026-06-15 18:32 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442599) | [19m37s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419574) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442560) | [12m57s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419559) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [8m11s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419710) | [12m30s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419701) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [9m17s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419719) | [10m57s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442799) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [6m17s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419634) | [10m17s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419743) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419609) | [7m03s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442775) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [1m59s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442762) | [5m41s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442703) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [3m22s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419678) | [5m21s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442705) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442769) | [4m28s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419671) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419624) | [2m54s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442770) | 0% (0/1) | `shark75-ci` |
| `windows-2022` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27568261118/job/81497852948) | [31s](https://github.com/iree-org/iree/actions/runs/27565887881/job/81489905056) | 0% (0/3) | 9 |
| `macos-14` | github-hosted | 9 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/27568261118/job/81497852930) | [16s](https://github.com/iree-org/iree/actions/runs/27565887881/job/81489905224) | 0% (0/3) | 9 |
| `azure-linux-scale` | ossci | 17 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27568261118/job/81497853027) | [14s](https://github.com/iree-org/iree/actions/runs/27565887881/job/81489905243) | 0% (0/6) | 17 |
| `ubuntu-24.04` | github-hosted | 59 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27566276308/job/81497714514) | [10s](https://github.com/iree-org/iree/actions/runs/27568261118/job/81497852894) | 0% (0/19) | 59 |
| `ubuntu-latest` | github-hosted | 10 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/27559165937/job/81466216383) | [9s](https://github.com/iree-org/iree/actions/runs/27578342453/job/81532300793) | 0% (0/4) | 10 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 12 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442800) | [8s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419708) | 25% (1/4) | 12 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27566276308/job/81491453969) | [3s](https://github.com/iree-org/iree/actions/runs/27568261118/job/81497852943) | 0% (0/3) | 9 |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27566276308/job/81491454104) | [2s](https://github.com/iree-org/iree/actions/runs/27568261118/job/81497853256) | 0% (0/1) | 3 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442565) | [2s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419550) | 0% (0/1) | 3 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442757) | [1s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419651) | 0% (0/1) | `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442712) | [1s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419693) | 0% (0/1) | `iree-mi308-1` |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442599) | [19m37s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419574) | [19m37s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419574) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442560) | [12m57s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419559) | [12m57s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419559) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [1m40s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442788) | [12m30s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419701) | [12m30s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419701) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [9m17s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419719) | [10m57s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442799) | [10m57s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442799) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [3m24s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442780) | [10m17s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419743) | [10m17s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419743) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [7m18s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442833) | [8m11s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419710) | [8m11s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419710) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419609) | [7m03s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442775) | [7m03s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442775) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [6m07s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442798) | [6m17s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419634) | [6m17s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419634) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [4m13s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419783) | [5m41s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442703) | [5m41s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442703) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [3m22s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419678) | [5m21s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442705) | [5m21s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442705) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [4m29s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442830) | [5m00s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419687) | [5m00s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419687) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442769) | [4m28s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419671) | [4m28s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419671) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419624) | [2m54s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442770) | [2m54s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442770) | 1 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419700) | [2m02s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442698) | [2m02s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442698) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81499419696) | [1m59s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442762) | [1m59s](https://github.com/iree-org/iree/actions/runs/27566278011/job/81492442762) | 2 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 3 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/27568261118/job/81497852894) | [1m54s](https://github.com/iree-org/iree/actions/runs/27566276308/job/81491453834) | [1m54s](https://github.com/iree-org/iree/actions/runs/27566276308/job/81491453834) | 3 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27568261118/job/81497853033) | [31s](https://github.com/iree-org/iree/actions/runs/27565887881/job/81489905056) | [31s](https://github.com/iree-org/iree/actions/runs/27565887881/job/81489905056) | 3 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27568261162/job/81497843200) | [24s](https://github.com/iree-org/iree/actions/runs/27565887873/job/81489928048) | [24s](https://github.com/iree-org/iree/actions/runs/27565887873/job/81489928048) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 3 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/27566276308/job/81491454033) | [16s](https://github.com/iree-org/iree/actions/runs/27565887881/job/81489905224) | [16s](https://github.com/iree-org/iree/actions/runs/27565887881/job/81489905224) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/27568261118/job/81497852949) | [14s](https://github.com/iree-org/iree/actions/runs/27565887881/job/81489905243) | [14s](https://github.com/iree-org/iree/actions/runs/27565887881/job/81489905243) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 251 | 2% (5/251) |  | 6h17m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 170 | 2% (4/170) |  | 6h23m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 184 | 3% (5/184) |  | 6h23m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 216 | 8% (18/216) |  | 6h23m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 58 | 2% (1/58) |  | 6h32m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
