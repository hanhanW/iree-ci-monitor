# iree-ci-monitor

_Updated: 2026-07-14 11:42 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 5 | 0 | — | — | 0 | [19m03s](https://github.com/iree-org/iree/actions/runs/29338251999/job/87104980265) | [59m41s](https://github.com/iree-org/iree/actions/runs/29332513339/job/87090033460) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [28m46s](https://github.com/iree-org/iree/actions/runs/29338251999/job/87104980241) | [55m55s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520690) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [15m07s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093875) | [55m54s](https://github.com/iree-org/iree/actions/runs/29332513339/job/87090033523) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 10 | 0 | — | — | 0 | [12m14s](https://github.com/iree-org/iree/actions/runs/29343276995/job/87125551266) | [55m29s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520811) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 10 | 0 | — | — | 0 | [5m45s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093982) | [46m35s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520718) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 10 | 0 | — | — | 0 | [11m57s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520771) | [46m21s](https://github.com/iree-org/iree/actions/runs/29332513339/job/87090033489) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 5 | 0 | — | — | 0 | [2m10s](https://github.com/iree-org/iree/actions/runs/29338251999/job/87104979962) | [30m13s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520541) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [20m30s](https://github.com/iree-org/iree/actions/runs/29338251999/job/87104980197) | [28m59s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520787) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093781) | [23m48s](https://github.com/iree-org/iree/actions/runs/29338251999/job/87104979990) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 5 | 0 | — | — | 0 | [14m08s](https://github.com/iree-org/iree/actions/runs/29338251999/job/87104980093) | [21m46s](https://github.com/iree-org/iree/actions/runs/29343276995/job/87125551274) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 10 | 0 | — | — | 0 | [7m54s](https://github.com/iree-org/iree/actions/runs/29338251999/job/87104980235) | [21m41s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520668) | 0% (0/4) | `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29338251999/job/87104980023) | [8m12s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520739) | 0% (0/2) | `iree-mi308-1` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m54s](https://github.com/iree-org/iree/actions/runs/29323385260/job/87053786300) | [1m54s](https://github.com/iree-org/iree/actions/runs/29323385260/job/87053786300) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 31 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/29334047559/job/87088817256) | [25s](https://github.com/iree-org/iree/actions/runs/29338252208/job/87102985188) | 0% (0/15) | 31 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/29343277063/job/87120386592) | [8s](https://github.com/iree-org/iree/actions/runs/29321443017/job/87047498822) | 0% (0/6) | 15 |
| `ubuntu-24.04` | github-hosted | 107 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29338252208/job/87102984688) | [4s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520674) | 2% (1/41) | 103 |
| `windows-2022` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29343277063/job/87120386596) | [4s](https://github.com/iree-org/iree/actions/runs/29343277063/job/87120386914) | 0% (0/6) | 15 |
| `macos-14` | github-hosted | 16 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29334047559/job/87088817024) | [4s](https://github.com/iree-org/iree/actions/runs/29338252208/job/87102984986) | 0% (0/7) | 16 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/29323345673/job/87053657031) | [4s](https://github.com/iree-org/iree/actions/runs/29323345673/job/87053657031) | 0% (0/1) | 1 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 5 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29338251999/job/87104980056) | [4s](https://github.com/iree-org/iree/actions/runs/29343276995/job/87125551229) | 0% (0/2) | 5 |
| `ubuntu-latest` | github-hosted | 24 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29338250381/job/87102947119) | [3s](https://github.com/iree-org/iree/actions/runs/29343275738/job/87120339134) | 0% (0/6) | 24 |
| `azure-windows-scale` | ossci | 5 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29334047559/job/87088817225) | [2s](https://github.com/iree-org/iree/actions/runs/29343277063/job/87120387366) | 0% (0/2) | 5 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 5 | 0 | — | — | [19m03s](https://github.com/iree-org/iree/actions/runs/29338251999/job/87104980265) | [59m41s](https://github.com/iree-org/iree/actions/runs/29332513339/job/87090033460) | [59m41s](https://github.com/iree-org/iree/actions/runs/29332513339/job/87090033460) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 5 | 0 | — | — | [28m46s](https://github.com/iree-org/iree/actions/runs/29338251999/job/87104980241) | [55m55s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520690) | [55m55s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520690) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 5 | 0 | — | — | [15m07s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093875) | [55m54s](https://github.com/iree-org/iree/actions/runs/29332513339/job/87090033523) | [55m54s](https://github.com/iree-org/iree/actions/runs/29332513339/job/87090033523) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 5 | 0 | — | — | [7m20s](https://github.com/iree-org/iree/actions/runs/29332513339/job/87090033495) | [55m29s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520811) | [55m29s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520811) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [2m25s](https://github.com/iree-org/iree/actions/runs/29338251999/job/87104980189) | [46m35s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520718) | [46m35s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520718) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [11m57s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520771) | [46m21s](https://github.com/iree-org/iree/actions/runs/29332513339/job/87090033489) | [46m21s](https://github.com/iree-org/iree/actions/runs/29332513339/job/87090033489) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 5 | 0 | — | — | [16m32s](https://github.com/iree-org/iree/actions/runs/29332513339/job/87090033461) | [46m08s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520777) | [46m08s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520777) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [8m42s](https://github.com/iree-org/iree/actions/runs/29343276995/job/87125551285) | [39m38s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520708) | [39m38s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520708) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 5 | 0 | — | — | [2m10s](https://github.com/iree-org/iree/actions/runs/29338251999/job/87104979962) | [30m13s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520541) | [30m13s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520541) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 5 | 0 | — | — | [20m30s](https://github.com/iree-org/iree/actions/runs/29338251999/job/87104980197) | [28m59s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520787) | [28m59s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520787) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [13m19s](https://github.com/iree-org/iree/actions/runs/29343276995/job/87125551313) | [24m07s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520728) | [24m07s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520728) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29321442885/job/87049093781) | [23m48s](https://github.com/iree-org/iree/actions/runs/29338251999/job/87104979990) | [23m48s](https://github.com/iree-org/iree/actions/runs/29338251999/job/87104979990) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 5 | 0 | — | — | [14m08s](https://github.com/iree-org/iree/actions/runs/29338251999/job/87104980093) | [21m46s](https://github.com/iree-org/iree/actions/runs/29343276995/job/87125551274) | [21m46s](https://github.com/iree-org/iree/actions/runs/29343276995/job/87125551274) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [5m39s](https://github.com/iree-org/iree/actions/runs/29343276995/job/87125551284) | [21m41s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520668) | [21m41s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520668) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [16m09s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520720) | [18m44s](https://github.com/iree-org/iree/actions/runs/29343276995/job/87125551398) | [18m44s](https://github.com/iree-org/iree/actions/runs/29343276995/job/87125551398) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29338251999/job/87104980023) | [8m12s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520739) | [8m12s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520739) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m54s](https://github.com/iree-org/iree/actions/runs/29323385260/job/87053786300) | [1m54s](https://github.com/iree-org/iree/actions/runs/29323385260/job/87053786300) | [1m54s](https://github.com/iree-org/iree/actions/runs/29323385260/job/87053786300) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 5 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/29332513435/job/87083677426) | [1m49s](https://github.com/iree-org/iree/actions/runs/29338252208/job/87102985529) | [1m49s](https://github.com/iree-org/iree/actions/runs/29338252208/job/87102985529) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/29343277063/job/87120387256) | [1m44s](https://github.com/iree-org/iree/actions/runs/29338252208/job/87102985253) | [1m44s](https://github.com/iree-org/iree/actions/runs/29338252208/job/87102985253) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29343276995/job/87125551365) | [1m28s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520737) | [1m28s](https://github.com/iree-org/iree/actions/runs/29334047574/job/87090520737) | 5 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 192 | 2% (3/191) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 159 | 10% (16/158) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 161 | 1% (1/160) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 142 | 1% (1/141) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 45 | 11% (5/45) |  | 3h12m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
