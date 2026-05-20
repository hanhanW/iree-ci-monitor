# iree-ci-monitor

_Updated: 2026-05-20 00:32 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [42m34s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967077) | [42m34s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967077) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [24m59s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967095) | [36m14s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967225) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926511) | 2026-05-19 06:28 PDT | 0 | [17m32s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967004) | [17m32s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967004) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [17m28s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967074) | [17m28s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967074) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [15m29s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967088) | [15m29s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967088) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967182) | [13m17s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967102) | 0% (0/2) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967119) | [10m33s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967070) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967091) | [10m25s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967196) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [9m57s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967142) | [9m57s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967142) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [6m52s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967133) | [6m52s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967133) | 0% (0/1) | `shark55-ci` |
| `azure-linux-scale` | ossci | 6 | 0 | — | — | 0 | [1m59s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521767) | [3m31s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76899526180) | 0% (0/6) | 6 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [24s](https://github.com/iree-org/iree/actions/runs/26145536772/job/76900281440) | [1m11s](https://github.com/iree-org/iree/actions/runs/26145537149/job/76900137998) | 0% (0/3) | 9 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967137) | [9s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967181) | 0% (0/4) | 4 |
| `ubuntu-24.04` | github-hosted | 31 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967117) | [3s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521631) | 22% (5/23) | 31 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521638) | [3s](https://github.com/iree-org/iree/actions/runs/26145454092/job/76899882138) | 0% (0/3) | 6 |
| `macos-14` | github-hosted | 5 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521700) | [3s](https://github.com/iree-org/iree/actions/runs/26145454092/job/76899882122) | 0% (0/3) | 5 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521695) | [2s](https://github.com/iree-org/iree/actions/runs/26145454092/job/76899882129) | 0% (0/3) | 5 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521716) | [1s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521716) | 0% (0/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900966990) | [1s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900966990) | 0% (0/1) | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926441) | 2026-05-19 06:28 PDT | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900966991) | [1s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900966991) | 100% (1/1) | `shark01-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967114) | [1s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967114) | 0% (0/1) | `iree-mi308-1` |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926441) | 2026-05-19 06:28 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `new-lds-promotion` | pull_request |
| [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926511) | 2026-05-19 06:28 PDT | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `new-lds-promotion` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [42m34s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967077) | [42m34s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967077) | [42m34s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967077) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [36m14s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967225) | [36m14s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967225) | [36m14s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967225) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [24m59s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967095) | [24m59s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967095) | [24m59s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967095) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926511) | 2026-05-19 06:28 PDT | [17m32s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967004) | [17m32s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967004) | [17m32s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967004) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926441) | 2026-05-19 06:28 PDT | [1s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900966991) | [1s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900966991) | [1s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900966991) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [17m28s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967074) | [17m28s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967074) | [17m28s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967074) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 0 | — | — | [15m29s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967088) | [15m29s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967088) | [15m29s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967088) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [13m17s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967102) | [13m17s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967102) | [13m17s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967102) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [10m33s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967070) | [10m33s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967070) | [10m33s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967070) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [10m25s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967196) | [10m25s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967196) | [10m25s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967196) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [9m57s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967142) | [9m57s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967142) | [9m57s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967142) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [6m52s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967133) | [6m52s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967133) | [6m52s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76900967133) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 1 | 0 | — | — | [3m31s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76899526180) | [3m31s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76899526180) | [3m31s](https://github.com/iree-org/iree/actions/runs/26145340265/job/76899526180) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [2m50s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521707) | [2m50s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521707) | [2m50s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521707) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [2m24s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521770) | [2m24s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521770) | [2m24s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521770) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [1m59s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521767) | [1m59s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521767) | [1m59s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521767) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [1m50s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521721) | [1m50s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521721) | [1m50s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521721) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [1m33s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521633) | [1m33s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521633) | [1m33s](https://github.com/iree-org/iree/actions/runs/26145340264/job/76899521633) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/26145339528/job/76899501339) | [1m11s](https://github.com/iree-org/iree/actions/runs/26145537149/job/76900137998) | [1m11s](https://github.com/iree-org/iree/actions/runs/26145537149/job/76900137998) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26145339528/job/76899501321) | [1m07s](https://github.com/iree-org/iree/actions/runs/26145537149/job/76900138023) | [1m07s](https://github.com/iree-org/iree/actions/runs/26145537149/job/76900138023) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 782 | 2% (13/781) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 647 | 1% (7/646) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 633 | 0% (1/632) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 684 | 5% (35/683) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 216 | 0% (0/216) |  | 46m28s ago |

## Alerts

- **[high-failure-main]** `ubuntu-24.04` main-branch failure rate 22% (5/23)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
