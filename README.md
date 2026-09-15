# iree-ci-monitor

_Updated: 2026-09-15 14:25 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 8 | 0 | — | — | 0 | [4h02m](https://github.com/iree-org/iree/actions/runs/34965375421/job/104373115816) | [4h46m](https://github.com/iree-org/iree/actions/runs/34964409308/job/104367867664) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,gfx1201` | self-hosted | 16 | 0 | — | — | 0 | [3h58m](https://github.com/iree-org/iree/actions/runs/34965375385/job/104381340889) | [4h46m](https://github.com/iree-org/iree/actions/runs/34965375421/job/104373115906) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 8 | 0 | — | — | 0 | [3h33m](https://github.com/iree-org/iree/actions/runs/34965374250/job/104376661315) | [4h33m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281393) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [2h55m](https://github.com/iree-org/iree/actions/runs/34965373801/job/104378181313) | [4h14m](https://github.com/iree-org/iree/actions/runs/34965375421/job/104373115687) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [3h49m](https://github.com/iree-org/iree/actions/runs/34965375421/job/104373115620) | [3h55m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281308) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 8 | 0 | — | — | 0 | [1h39m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281309) | [3h43m](https://github.com/iree-org/iree/actions/runs/34965374250/job/104376661572) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 16 | 0 | — | — | 0 | [1h34m](https://github.com/iree-org/iree/actions/runs/34966732511/job/104377683473) | [3h15m](https://github.com/iree-org/iree/actions/runs/34965373801/job/104378181247) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 16 | 0 | — | — | 0 | [2h24m](https://github.com/iree-org/iree/actions/runs/34965375421/job/104373115783) | [3h09m](https://github.com/iree-org/iree/actions/runs/34965375385/job/104381340911) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 16 | 0 | — | — | 0 | [1h18m](https://github.com/iree-org/iree/actions/runs/34966732511/job/104377683500) | [2h21m](https://github.com/iree-org/iree/actions/runs/34965375385/job/104381341033) | 0% (0/2) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [1h06m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281323) | [1h57m](https://github.com/iree-org/iree/actions/runs/34965376327/job/104373285947) | 0% (0/1) | `shark01-ci`, `shark55-ci` |
| `ubuntu-24.04` | github-hosted | 194 | 0 | — | — | 0 | [7m01s](https://github.com/iree-org/iree/actions/runs/34965375421/job/104373115511) | [16m13s](https://github.com/iree-org/iree/actions/runs/34965375508/job/104370707533) | 0% (0/19) | 171 |
| `macos-14` | github-hosted | 24 | 0 | — | — | 0 | [3m27s](https://github.com/iree-org/iree/actions/runs/34965376285/job/104371823404) | [11m28s](https://github.com/iree-org/iree/actions/runs/34966732501/job/104374489348) | 0% (0/3) | 24 |
| `windows-2022` | github-hosted | 24 | 0 | — | — | 0 | [1m56s](https://github.com/iree-org/iree/actions/runs/34965373848/job/104369608500) | [10m12s](https://github.com/iree-org/iree/actions/runs/34966732501/job/104374489391) | 0% (0/3) | 24 |
| `ubuntu-24.04-arm` | github-hosted | 24 | 0 | — | — | 0 | [2m02s](https://github.com/iree-org/iree/actions/runs/34965373848/job/104369608453) | [9m31s](https://github.com/iree-org/iree/actions/runs/34966732501/job/104374489382) | 0% (0/3) | 24 |
| `azure-windows-scale` | ossci | 8 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/34966732501/job/104374489688) | [6m52s](https://github.com/iree-org/iree/actions/runs/34965373848/job/104369608731) | 0% (0/1) | 8 |
| `ubuntu-latest` | github-hosted | 42 | 0 | — | — | 0 | [1m11s](https://github.com/iree-org/iree/actions/runs/34965368796/job/104368437060) | [6m20s](https://github.com/iree-org/iree/actions/runs/34965367942/job/104368435927) | 0% (0/3) | 42 |
| `azure-linux-scale` | ossci | 46 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/34965376519/job/104377146396) | [1m33s](https://github.com/iree-org/iree/actions/runs/34965376285/job/104371823728) | 0% (0/6) | 46 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 17 | 17 | [23h26m](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736563) | 2026-09-15 14:24 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [23h26m](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736563) | 2026-09-15 14:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `dependabot/github_actions/github-actions-177be4f125` | pull_request |
| [14h13m](https://github.com/iree-org/iree/actions/runs/34939788399/job/104287645155) | 2026-09-15 14:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [13h18m](https://github.com/iree-org/iree/actions/runs/34944316463/job/104302548194) | 2026-09-15 14:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `topo-fix` | pull_request |
| [12h34m](https://github.com/iree-org/iree/actions/runs/34948033003/job/104315872885) | 2026-09-15 14:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [12h31m](https://github.com/iree-org/iree/actions/runs/34948041452/job/104316497120) | 2026-09-15 14:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/ziereis/qdq-integer-contractions` | pull_request |
| [12h29m](https://github.com/iree-org/iree/actions/runs/34948041578/job/104317351086) | 2026-09-15 14:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/ziereis/qdq-drop-zero-zp` | pull_request |
| [12h26m](https://github.com/iree-org/iree/actions/runs/34948043226/job/104317980560) | 2026-09-15 14:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/ziereis/qdq-reshape-propagation` | pull_request |
| [12h22m](https://github.com/iree-org/iree/actions/runs/34948043640/job/104319468643) | 2026-09-15 14:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/ziereis/qdq-torch-conversion` | pull_request |
| [11h47m](https://github.com/iree-org/iree/actions/runs/34952538791/job/104329835370) | 2026-09-15 14:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [9h37m](https://github.com/iree-org/iree/actions/runs/34964409308/job/104367867490) | 2026-09-15 14:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-1` | pull_request |
| [9h19m](https://github.com/iree-org/iree/actions/runs/34965375421/job/104373115642) | 2026-09-15 14:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-3` | pull_request |
| [9h19m](https://github.com/iree-org/iree/actions/runs/34965376327/job/104373285946) | 2026-09-15 14:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-7` | pull_request |
| [9h16m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281264) | 2026-09-15 14:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-5` | pull_request |
| [9h08m](https://github.com/iree-org/iree/actions/runs/34965374250/job/104376661365) | 2026-09-15 14:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-2` | pull_request |
| [9h05m](https://github.com/iree-org/iree/actions/runs/34966732511/job/104377683509) | 2026-09-15 14:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 17 | 17 | [23h26m](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736563) | 2026-09-15 14:24 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [4h26m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281604) | [4h48m](https://github.com/iree-org/iree/actions/runs/34965376327/job/104373285962) | [4h48m](https://github.com/iree-org/iree/actions/runs/34965376327/job/104373285962) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 8 | 0 | — | — | [4h02m](https://github.com/iree-org/iree/actions/runs/34965375421/job/104373115816) | [4h46m](https://github.com/iree-org/iree/actions/runs/34964409308/job/104367867664) | [4h46m](https://github.com/iree-org/iree/actions/runs/34964409308/job/104367867664) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 8 | 0 | — | — | [3h33m](https://github.com/iree-org/iree/actions/runs/34965374250/job/104376661315) | [4h33m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281393) | [4h33m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281393) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [3h19m](https://github.com/iree-org/iree/actions/runs/34965375385/job/104381340941) | [4h24m](https://github.com/iree-org/iree/actions/runs/34966732511/job/104377683475) | [4h24m](https://github.com/iree-org/iree/actions/runs/34966732511/job/104377683475) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 8 | 0 | — | — | [2h55m](https://github.com/iree-org/iree/actions/runs/34965373801/job/104378181313) | [4h14m](https://github.com/iree-org/iree/actions/runs/34965375421/job/104373115687) | [4h14m](https://github.com/iree-org/iree/actions/runs/34965375421/job/104373115687) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 8 | 0 | — | — | [3h49m](https://github.com/iree-org/iree/actions/runs/34965375421/job/104373115620) | [3h55m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281308) | [3h55m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281308) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 8 | 0 | — | — | [1h39m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281309) | [3h43m](https://github.com/iree-org/iree/actions/runs/34965374250/job/104376661572) | [3h43m](https://github.com/iree-org/iree/actions/runs/34965374250/job/104376661572) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 8 | 0 | — | — | [1h34m](https://github.com/iree-org/iree/actions/runs/34966732511/job/104377683473) | [3h31m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281379) | [3h31m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281379) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 8 | 0 | — | — | [2h49m](https://github.com/iree-org/iree/actions/runs/34965375421/job/104373115696) | [3h18m](https://github.com/iree-org/iree/actions/runs/34965374250/job/104376661424) | [3h18m](https://github.com/iree-org/iree/actions/runs/34965374250/job/104376661424) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 8 | 0 | — | — | [2h18m](https://github.com/iree-org/iree/actions/runs/34965375385/job/104381340927) | [3h15m](https://github.com/iree-org/iree/actions/runs/34965373801/job/104378181247) | [3h15m](https://github.com/iree-org/iree/actions/runs/34965373801/job/104378181247) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 8 | 0 | — | — | [2h17m](https://github.com/iree-org/iree/actions/runs/34965374250/job/104376661775) | [3h09m](https://github.com/iree-org/iree/actions/runs/34965375385/job/104381340911) | [3h09m](https://github.com/iree-org/iree/actions/runs/34965375385/job/104381340911) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [1h18m](https://github.com/iree-org/iree/actions/runs/34966732511/job/104377683500) | [3h08m](https://github.com/iree-org/iree/actions/runs/34965374250/job/104376661461) | [3h08m](https://github.com/iree-org/iree/actions/runs/34965374250/job/104376661461) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [1h25m](https://github.com/iree-org/iree/actions/runs/34965374250/job/104376661404) | [2h21m](https://github.com/iree-org/iree/actions/runs/34965375385/job/104381341033) | [2h21m](https://github.com/iree-org/iree/actions/runs/34965375385/job/104381341033) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 8 | 0 | — | — | [1h06m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281323) | [1h57m](https://github.com/iree-org/iree/actions/runs/34965376327/job/104373285947) | [1h57m](https://github.com/iree-org/iree/actions/runs/34965376327/job/104373285947) | 2 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | 13 | 0 | — | — | [3m09s](https://github.com/iree-org/iree/actions/runs/34965375508/job/104369721569) | [25m01s](https://github.com/iree-org/iree/actions/runs/34965376519/job/104369437510) | [25m01s](https://github.com/iree-org/iree/actions/runs/34965376519/job/104369437510) | 8 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | 8 | 0 | — | — | [7m33s](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281739) | [20m35s](https://github.com/iree-org/iree/actions/runs/34965376327/job/104373285989) | [20m35s](https://github.com/iree-org/iree/actions/runs/34965376327/job/104373285989) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 8 | 0 | — | — | [14m02s](https://github.com/iree-org/iree/actions/runs/34965376519/job/104377146230) | [20m19s](https://github.com/iree-org/iree/actions/runs/34965376285/job/104371823331) | [20m19s](https://github.com/iree-org/iree/actions/runs/34965376285/job/104371823331) | 8 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 5 | 0 | — | — | [4m10s](https://github.com/iree-org/iree/actions/runs/34965374406/job/104368464819) | [19m32s](https://github.com/iree-org/iree/actions/runs/34965375100/job/104368463676) | [19m32s](https://github.com/iree-org/iree/actions/runs/34965375100/job/104368463676) | 5 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 8 | 0 | — | — | [12m27s](https://github.com/iree-org/iree/actions/runs/34965375508/job/104370707412) | [19m02s](https://github.com/iree-org/iree/actions/runs/34965375511/job/104373127145) | [19m02s](https://github.com/iree-org/iree/actions/runs/34965375511/job/104373127145) | 8 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 374 | 1% (5/374) |  | 4h30m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 304 | 2% (5/304) |  | 4h37m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 284 | 1% (3/284) |  | 5h43m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 263 | 8% (22/263) |  | 1d05h ago |

## Alerts

- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job observed waiting 23h26m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h57m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 3h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 4h14m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 4h46m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 3h43m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 4h33m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 3h55m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 3h15m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 4h46m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h21m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
