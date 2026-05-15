# iree-ci-monitor

_Updated: 2026-05-15 00:29 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 17 | 10 | [10h18m](https://github.com/iree-org/iree/actions/runs/25885460432/job/76077200322) | 2026-05-15 00:28 PDT | 0 | [3h42m](https://github.com/iree-org/iree/actions/runs/25895840584/job/76109960162) | [9h19m](https://github.com/iree-org/iree/actions/runs/25887528933/job/76083779178) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [2h42m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085218877) | [7h15m](https://github.com/iree-org/iree/actions/runs/25887878862/job/76085119912) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 8 | 6 | [10h16m](https://github.com/iree-org/iree/actions/runs/25885469594/job/76077537201) | 2026-05-15 00:28 PDT | 0 | [36m00s](https://github.com/iree-org/iree/actions/runs/25895840584/job/76109960164) | [5h16m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085219079) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 6 | 0 | — | — | 0 | [3h19m](https://github.com/iree-org/iree/actions/runs/25888598131/job/76090093596) | [4h17m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085219027) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [2h36m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085218995) | [3h22m](https://github.com/iree-org/iree/actions/runs/25887528933/job/76083779114) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 7 | 1 | [5h05m](https://github.com/iree-org/iree/actions/runs/25758969066/job/75656279800) | 2026-05-12 18:15 PDT | 0 | [2h14m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085218871) | [3h12m](https://github.com/iree-org/iree/actions/runs/25887528933/job/76083778956) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 6 | 0 | — | — | 0 | [1h28m](https://github.com/iree-org/iree/actions/runs/25887528933/job/76083779113) | [2h37m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085218964) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [1h51m](https://github.com/iree-org/iree/actions/runs/25888598131/job/76090093609) | [2h12m](https://github.com/iree-org/iree/actions/runs/25887528933/job/76083779211) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [1h45m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085219037) | [2h11m](https://github.com/iree-org/iree/actions/runs/25887528933/job/76083779190) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [1h45m](https://github.com/iree-org/iree/actions/runs/25888598131/job/76090093566) | [1h54m](https://github.com/iree-org/iree/actions/runs/25887878862/job/76085119927) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | — | 0 | [1h34m](https://github.com/iree-org/iree/actions/runs/25887528933/job/76083779166) | [1h48m](https://github.com/iree-org/iree/actions/runs/25887528933/job/76083779206) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 6 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25903234352/job/76131849643) | [21m39s](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085219108) | 0% (0/3) | `iree-mi308-1` |
| `windows-2022` | github-hosted | 26 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25888598143/job/76086359518) | [3m27s](https://github.com/iree-org/iree/actions/runs/25887878866/job/76084011340) | 0% (0/9) | 26 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 24 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25903234352/job/76131849626) | [3m02s](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085218959) | 0% (0/12) | 24 |
| `ubuntu-24.04-arm` | github-hosted | 27 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25888598143/job/76086359529) | [1m58s](https://github.com/iree-org/iree/actions/runs/25887872899/job/76083986410) | 0% (0/9) | 27 |
| `ubuntu-24.04` | github-hosted | 153 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25903216018/job/76130967407) | [1m57s](https://github.com/iree-org/iree/actions/runs/25887872899/job/76083986344) | 14% (9/63) | 153 |
| `macos-14` | github-hosted | 26 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25895840590/job/76109241473) | [44s](https://github.com/iree-org/iree/actions/runs/25887878866/job/76084011378) | 0% (0/9) | 26 |
| `azure-linux-scale` | ossci | 44 | 1 | [19m47s](https://github.com/iree-org/iree/actions/runs/25783793136/job/75732425036) | 2026-05-13 00:23 PDT | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25903216039/job/76130989811) | [10s](https://github.com/iree-org/iree/actions/runs/25903216039/job/76130989816) | 21% (4/19) | 43 |
| `ubuntu-latest` | github-hosted | 8 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/25887877485/job/76083974781) | [10s](https://github.com/iree-org/iree/actions/runs/25887870668/job/76083945723) | 0% (0/6) | 8 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25903234352/job/76131849522) | [2s](https://github.com/iree-org/iree/actions/runs/25895840584/job/76109960076) | 0% (0/3) | 6 |
| `azure-windows-scale` | ossci | 8 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25888598143/job/76086359649) | [2s](https://github.com/iree-org/iree/actions/runs/25887878866/job/76084011433) | 33% (1/3) | 8 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [10h18m](https://github.com/iree-org/iree/actions/runs/25885460432/job/76077200322) | 2026-05-15 00:28 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |
| [10h16m](https://github.com/iree-org/iree/actions/runs/25885469594/job/76077537201) | 2026-05-15 00:28 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `main` | push |
| [10h16m](https://github.com/iree-org/iree/actions/runs/25885469594/job/76077537307) | 2026-05-15 00:28 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |
| [9h35m](https://github.com/iree-org/iree/actions/runs/25887528933/job/76083779163) | 2026-05-15 00:28 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `main` | push |
| [9h35m](https://github.com/iree-org/iree/actions/runs/25887528933/job/76083779198) | 2026-05-15 00:28 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |
| [9h26m](https://github.com/iree-org/iree/actions/runs/25887878862/job/76085119922) | 2026-05-15 00:28 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |
| [9h26m](https://github.com/iree-org/iree/actions/runs/25887878862/job/76085119944) | 2026-05-15 00:28 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `main` | push |
| [8h48m](https://github.com/iree-org/iree/actions/runs/25888598131/job/76090093497) | 2026-05-15 00:28 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [8h48m](https://github.com/iree-org/iree/actions/runs/25888598131/job/76090093576) | 2026-05-15 00:28 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `main` | push |
| [8h48m](https://github.com/iree-org/iree/actions/runs/25888598131/job/76090093612) | 2026-05-15 00:28 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |
| [5h05m](https://github.com/iree-org/iree/actions/runs/25758969066/job/75656279800) | 2026-05-12 18:15 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `thread-distribute-scan` | pull_request |
| [5h05m](https://github.com/iree-org/iree/actions/runs/25758969066/job/75656279949) | 2026-05-12 18:15 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `thread-distribute-scan` | pull_request |
| [1h12m](https://github.com/iree-org/iree/actions/runs/25903234352/job/76131849630) | 2026-05-15 00:28 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `subgroup-distribute-scan` | pull_request |
| [1h12m](https://github.com/iree-org/iree/actions/runs/25903234352/job/76131849640) | 2026-05-15 00:28 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `subgroup-distribute-scan` | pull_request |
| [19m47s](https://github.com/iree-org/iree/actions/runs/25783793136/job/75732425036) | 2026-05-13 00:23 PDT | `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 9 | 6 | [10h18m](https://github.com/iree-org/iree/actions/runs/25885460432/job/76077200322) | 2026-05-15 00:28 PDT | [1h58m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085219039) | [3h42m](https://github.com/iree-org/iree/actions/runs/25895840584/job/76109960162) | [3h42m](https://github.com/iree-org/iree/actions/runs/25895840584/job/76109960162) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 8 | 6 | [10h16m](https://github.com/iree-org/iree/actions/runs/25885469594/job/76077537201) | 2026-05-15 00:28 PDT | [36m00s](https://github.com/iree-org/iree/actions/runs/25895840584/job/76109960164) | [5h16m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085219079) | [5h16m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085219079) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 8 | 4 | [8h48m](https://github.com/iree-org/iree/actions/runs/25888598131/job/76090093497) | 2026-05-15 00:28 PDT | [9h16m](https://github.com/iree-org/iree/actions/runs/25887878862/job/76085119995) | [9h19m](https://github.com/iree-org/iree/actions/runs/25887528933/job/76083779178) | [9h19m](https://github.com/iree-org/iree/actions/runs/25887528933/job/76083779178) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [2h42m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085218877) | [7h15m](https://github.com/iree-org/iree/actions/runs/25887878862/job/76085119912) | [7h15m](https://github.com/iree-org/iree/actions/runs/25887878862/job/76085119912) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 7 | 1 | [5h05m](https://github.com/iree-org/iree/actions/runs/25758969066/job/75656279800) | 2026-05-12 18:15 PDT | [2h14m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085218871) | [3h12m](https://github.com/iree-org/iree/actions/runs/25887528933/job/76083778956) | [3h12m](https://github.com/iree-org/iree/actions/runs/25887528933/job/76083778956) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 6 | 0 | — | — | [3h19m](https://github.com/iree-org/iree/actions/runs/25888598131/job/76090093596) | [4h17m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085219027) | [4h17m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085219027) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 6 | 0 | — | — | [2h36m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085218995) | [3h22m](https://github.com/iree-org/iree/actions/runs/25887528933/job/76083779114) | [3h22m](https://github.com/iree-org/iree/actions/runs/25887528933/job/76083779114) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 6 | 0 | — | — | [1h28m](https://github.com/iree-org/iree/actions/runs/25887528933/job/76083779113) | [2h37m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085218964) | [2h37m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085218964) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [1h51m](https://github.com/iree-org/iree/actions/runs/25888598131/job/76090093609) | [2h24m](https://github.com/iree-org/iree/actions/runs/25887878862/job/76085119952) | [2h24m](https://github.com/iree-org/iree/actions/runs/25887878862/job/76085119952) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [1h50m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085219012) | [2h17m](https://github.com/iree-org/iree/actions/runs/25887878862/job/76085119902) | [2h17m](https://github.com/iree-org/iree/actions/runs/25887878862/job/76085119902) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [1h40m](https://github.com/iree-org/iree/actions/runs/25888598131/job/76090093507) | [2h10m](https://github.com/iree-org/iree/actions/runs/25887878862/job/76085119959) | [2h10m](https://github.com/iree-org/iree/actions/runs/25887878862/job/76085119959) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [1h35m](https://github.com/iree-org/iree/actions/runs/25887528933/job/76083779132) | [2h09m](https://github.com/iree-org/iree/actions/runs/25887878862/job/76085119965) | [2h09m](https://github.com/iree-org/iree/actions/runs/25887878862/job/76085119965) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [1h45m](https://github.com/iree-org/iree/actions/runs/25888598131/job/76090093566) | [1h54m](https://github.com/iree-org/iree/actions/runs/25887878862/job/76085119927) | [1h54m](https://github.com/iree-org/iree/actions/runs/25887878862/job/76085119927) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [1h29m](https://github.com/iree-org/iree/actions/runs/25888598131/job/76090093591) | [1h51m](https://github.com/iree-org/iree/actions/runs/25887878862/job/76085119925) | [1h51m](https://github.com/iree-org/iree/actions/runs/25887878862/job/76085119925) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [1h32m](https://github.com/iree-org/iree/actions/runs/25888598131/job/76090093489) | [1h37m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085219004) | [1h37m](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085219004) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 6 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/25903234352/job/76131849643) | [21m39s](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085219108) | [21m39s](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085219108) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 9 | 1 | [19m47s](https://github.com/iree-org/iree/actions/runs/25783793136/job/75732425036) | 2026-05-13 00:23 PDT | [9s](https://github.com/iree-org/iree/actions/runs/25895840590/job/76109241527) | [10s](https://github.com/iree-org/iree/actions/runs/25903216039/job/76130989816) | [10s](https://github.com/iree-org/iree/actions/runs/25903216039/job/76130989816) | 8 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 6 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/25895840584/job/76109960166) | [8m13s](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085218990) | [8m13s](https://github.com/iree-org/iree/actions/runs/25887872894/job/76085218990) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 8 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/25887528911/job/76082853284) | [3m36s](https://github.com/iree-org/iree/actions/runs/25887878866/job/76084011335) | [3m36s](https://github.com/iree-org/iree/actions/runs/25887878866/job/76084011335) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 8 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/25887528911/job/76082853251) | [3m36s](https://github.com/iree-org/iree/actions/runs/25887878866/job/76084011348) | [3m36s](https://github.com/iree-org/iree/actions/runs/25887878866/job/76084011348) | 8 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1203 | 4% (54/1200) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,shark55-ci`, `self-hosted,persistent-cache,Linux,X64` | 914 | 2% (15/914) |  | 44m42s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,shark01-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 981 | 3% (28/981) |  | 45m35s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 1123 | 7% (80/1123) |  | 47m14s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 330 | 2% (7/330) |  | 1h00m ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job observed waiting 10h16m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 10h18m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job observed waiting 5h05m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h54m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h48m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 5h16m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 9h19m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 7h15m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 3h12m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 3h22m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 4h17m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h12m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 2h37m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h11m (> 1h00m)
- **[high-failure-main]** `azure-linux-scale` main-branch failure rate 21% (4/19)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
