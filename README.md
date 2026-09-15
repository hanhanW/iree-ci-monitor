# iree-ci-monitor

_Updated: 2026-09-15 10:05 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 16 | 0 | — | — | 0 | [3h55m](https://github.com/iree-org/iree/actions/runs/34965376327/job/104373285943) | [7h41m](https://github.com/iree-org/iree/actions/runs/34944316463/job/104302548391) | 0% (0/4) | `shark01-ci` |
| `Linux,X64,gfx1201` | self-hosted | 32 | 0 | — | — | 0 | [3h37m](https://github.com/iree-org/iree/actions/runs/34965375421/job/104373115668) | [6h55m](https://github.com/iree-org/iree/actions/runs/34952538791/job/104329835557) | 0% (0/8) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 16 | 0 | — | — | 0 | [4h04m](https://github.com/iree-org/iree/actions/runs/34965376327/job/104373285865) | [6h36m](https://github.com/iree-org/iree/actions/runs/34948043226/job/104317981054) | 0% (0/4) | `shark01-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 16 | 0 | — | — | 0 | [1h57m](https://github.com/iree-org/iree/actions/runs/34948043640/job/104319468198) | [4h23m](https://github.com/iree-org/iree/actions/runs/34965376327/job/104373285921) | 0% (0/4) | `shark01-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 16 | 0 | — | — | 0 | [1h29m](https://github.com/iree-org/iree/actions/runs/34948033003/job/104315872835) | [3h43m](https://github.com/iree-org/iree/actions/runs/34966732511/job/104377683558) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 32 | 0 | — | — | 0 | [2h08m](https://github.com/iree-org/iree/actions/runs/34948041578/job/104317351136) | [3h18m](https://github.com/iree-org/iree/actions/runs/34965374250/job/104376661424) | 0% (0/8) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 32 | 0 | — | — | 0 | [51m08s](https://github.com/iree-org/iree/actions/runs/34948033003/job/104315873058) | [2h59m](https://github.com/iree-org/iree/actions/runs/34966732511/job/104377683705) | 0% (0/8) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 16 | 0 | — | — | 0 | [1h39m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281309) | [2h58m](https://github.com/iree-org/iree/actions/runs/34948033003/job/104315872809) | 0% (0/4) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 32 | 0 | — | — | 0 | [45m15s](https://github.com/iree-org/iree/actions/runs/34948043640/job/104319468223) | [2h11m](https://github.com/iree-org/iree/actions/runs/34965375421/job/104373115758) | 0% (0/8) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 16 | 0 | — | — | 0 | [1h01m](https://github.com/iree-org/iree/actions/runs/34948043640/job/104319468446) | [1h57m](https://github.com/iree-org/iree/actions/runs/34965376327/job/104373285947) | 0% (0/4) | `shark01-ci`, `shark55-ci` |
| `ubuntu-24.04` | github-hosted | 364 | 0 | — | — | 0 | [5m00s](https://github.com/iree-org/iree/actions/runs/34948033003/job/104315872884) | [16m10s](https://github.com/iree-org/iree/actions/runs/34948043633/job/104314556499) | 4% (3/69) | 331 |
| `macos-14` | github-hosted | 46 | 0 | — | — | 0 | [3m54s](https://github.com/iree-org/iree/actions/runs/34948043248/job/104313883378) | [10m06s](https://github.com/iree-org/iree/actions/runs/34948041383/job/104313033097) | 0% (0/10) | 46 |
| `windows-2022` | github-hosted | 45 | 0 | — | — | 0 | [1m57s](https://github.com/iree-org/iree/actions/runs/34965375511/job/104373127194) | [9m18s](https://github.com/iree-org/iree/actions/runs/34966732501/job/104374489399) | 0% (0/9) | 45 |
| `ubuntu-24.04-arm` | github-hosted | 45 | 0 | — | — | 0 | [1m51s](https://github.com/iree-org/iree/actions/runs/34948041383/job/104313033254) | [9m03s](https://github.com/iree-org/iree/actions/runs/34966732501/job/104374489343) | 0% (0/9) | 45 |
| `ubuntu-latest` | github-hosted | 75 | 0 | — | — | 0 | [38s](https://github.com/iree-org/iree/actions/runs/34948581356/job/104313815620) | [6m20s](https://github.com/iree-org/iree/actions/runs/34965367942/job/104368435927) | 0% (0/9) | 75 |
| `azure-windows-scale` | ossci | 15 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/34965376519/job/104377146328) | [4m40s](https://github.com/iree-org/iree/actions/runs/34948043248/job/104313884345) | 67% (2/3) | 15 |
| `azure-linux-scale` | ossci | 85 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/34966732501/job/104374489549) | [2m40s](https://github.com/iree-org/iree/actions/runs/34948043248/job/104313885105) | 0% (0/20) | 85 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m33s](https://github.com/iree-org/iree/actions/runs/34952901461/job/104327870221) | [1m33s](https://github.com/iree-org/iree/actions/runs/34952901461/job/104327870221) | 0% (0/1) | 1 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 17 | 17 | [19h05m](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736563) | 2026-09-15 10:03 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [19h05m](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736563) | 2026-09-15 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `dependabot/github_actions/github-actions-177be4f125` | pull_request |
| [9h52m](https://github.com/iree-org/iree/actions/runs/34939788399/job/104287645155) | 2026-09-15 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [8h57m](https://github.com/iree-org/iree/actions/runs/34944316463/job/104302548194) | 2026-09-15 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `topo-fix` | pull_request |
| [8h12m](https://github.com/iree-org/iree/actions/runs/34948033003/job/104315872885) | 2026-09-15 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [8h10m](https://github.com/iree-org/iree/actions/runs/34948041452/job/104316497120) | 2026-09-15 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/ziereis/qdq-integer-contractions` | pull_request |
| [8h07m](https://github.com/iree-org/iree/actions/runs/34948041578/job/104317351086) | 2026-09-15 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/ziereis/qdq-drop-zero-zp` | pull_request |
| [8h05m](https://github.com/iree-org/iree/actions/runs/34948043226/job/104317980560) | 2026-09-15 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/ziereis/qdq-reshape-propagation` | pull_request |
| [8h01m](https://github.com/iree-org/iree/actions/runs/34948043640/job/104319468643) | 2026-09-15 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/ziereis/qdq-torch-conversion` | pull_request |
| [7h26m](https://github.com/iree-org/iree/actions/runs/34952538791/job/104329835370) | 2026-09-15 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [5h16m](https://github.com/iree-org/iree/actions/runs/34964409308/job/104367867490) | 2026-09-15 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-1` | pull_request |
| [4h58m](https://github.com/iree-org/iree/actions/runs/34965375421/job/104373115642) | 2026-09-15 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-3` | pull_request |
| [4h58m](https://github.com/iree-org/iree/actions/runs/34965376327/job/104373285946) | 2026-09-15 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-7` | pull_request |
| [4h55m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281264) | 2026-09-15 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-5` | pull_request |
| [4h47m](https://github.com/iree-org/iree/actions/runs/34965374250/job/104376661365) | 2026-09-15 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-2` | pull_request |
| [4h44m](https://github.com/iree-org/iree/actions/runs/34966732511/job/104377683509) | 2026-09-15 10:03 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 17 | 17 | [19h05m](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736563) | 2026-09-15 10:03 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 16 | 0 | — | — | [3h55m](https://github.com/iree-org/iree/actions/runs/34965376327/job/104373285943) | [7h41m](https://github.com/iree-org/iree/actions/runs/34944316463/job/104302548391) | [7h44m](https://github.com/iree-org/iree/actions/runs/34948043640/job/104319468210) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 16 | 0 | — | — | [4h26m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281604) | [6h59m](https://github.com/iree-org/iree/actions/runs/34948043226/job/104317981028) | [7h42m](https://github.com/iree-org/iree/actions/runs/34948041578/job/104317351182) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 16 | 0 | — | — | [4h04m](https://github.com/iree-org/iree/actions/runs/34965376327/job/104373285865) | [6h36m](https://github.com/iree-org/iree/actions/runs/34948043226/job/104317981054) | [6h45m](https://github.com/iree-org/iree/actions/runs/34948041452/job/104316496966) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 16 | 0 | — | — | [2h56m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281293) | [6h25m](https://github.com/iree-org/iree/actions/runs/34948041452/job/104316497176) | [6h35m](https://github.com/iree-org/iree/actions/runs/34952538791/job/104329835187) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 16 | 0 | — | — | [1h57m](https://github.com/iree-org/iree/actions/runs/34948043640/job/104319468198) | [4h23m](https://github.com/iree-org/iree/actions/runs/34965376327/job/104373285921) | [4h33m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281393) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 16 | 0 | — | — | [1h29m](https://github.com/iree-org/iree/actions/runs/34948033003/job/104315872835) | [3h43m](https://github.com/iree-org/iree/actions/runs/34966732511/job/104377683558) | [4h14m](https://github.com/iree-org/iree/actions/runs/34965375421/job/104373115687) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 16 | 0 | — | — | [2h08m](https://github.com/iree-org/iree/actions/runs/34948041578/job/104317351136) | [3h18m](https://github.com/iree-org/iree/actions/runs/34965374250/job/104376661424) | [3h23m](https://github.com/iree-org/iree/actions/runs/34948041452/job/104316497413) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 16 | 0 | — | — | [2h08m](https://github.com/iree-org/iree/actions/runs/34965376327/job/104373285983) | [3h09m](https://github.com/iree-org/iree/actions/runs/34965375385/job/104381340911) | [6h19m](https://github.com/iree-org/iree/actions/runs/34948041452/job/104316497117) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 16 | 0 | — | — | [49m57s](https://github.com/iree-org/iree/actions/runs/34964409308/job/104367867831) | [2h59m](https://github.com/iree-org/iree/actions/runs/34966732511/job/104377683705) | [3h15m](https://github.com/iree-org/iree/actions/runs/34965373801/job/104378181247) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 16 | 0 | — | — | [1h39m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281309) | [2h58m](https://github.com/iree-org/iree/actions/runs/34948033003/job/104315872809) | [3h43m](https://github.com/iree-org/iree/actions/runs/34965374250/job/104376661572) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 16 | 0 | — | — | [1h01m](https://github.com/iree-org/iree/actions/runs/34965373801/job/104378181491) | [2h50m](https://github.com/iree-org/iree/actions/runs/34965375385/job/104381340895) | [3h31m](https://github.com/iree-org/iree/actions/runs/34965376301/job/104374281379) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 16 | 0 | — | — | [48m29s](https://github.com/iree-org/iree/actions/runs/34948043640/job/104319468436) | [2h11m](https://github.com/iree-org/iree/actions/runs/34965375421/job/104373115758) | [2h21m](https://github.com/iree-org/iree/actions/runs/34965375385/job/104381341033) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 16 | 0 | — | — | [45m15s](https://github.com/iree-org/iree/actions/runs/34948043640/job/104319468223) | [2h09m](https://github.com/iree-org/iree/actions/runs/34965375385/job/104381340892) | [3h08m](https://github.com/iree-org/iree/actions/runs/34965374250/job/104376661461) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 16 | 0 | — | — | [1h01m](https://github.com/iree-org/iree/actions/runs/34948043640/job/104319468446) | [1h57m](https://github.com/iree-org/iree/actions/runs/34965376327/job/104373285947) | [2h00m](https://github.com/iree-org/iree/actions/runs/34948043226/job/104317980662) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 15 | 0 | — | — | [14m02s](https://github.com/iree-org/iree/actions/runs/34965376519/job/104377146230) | [21m52s](https://github.com/iree-org/iree/actions/runs/34948043248/job/104313883630) | [22m03s](https://github.com/iree-org/iree/actions/runs/34948032913/job/104312072280) | 15 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 7 | 0 | — | — | [4m39s](https://github.com/iree-org/iree/actions/runs/34948041029/job/104312047643) | [19m32s](https://github.com/iree-org/iree/actions/runs/34965375100/job/104368463676) | [19m32s](https://github.com/iree-org/iree/actions/runs/34965375100/job/104368463676) | 7 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 15 | 0 | — | — | [12m27s](https://github.com/iree-org/iree/actions/runs/34965375508/job/104370707412) | [17m18s](https://github.com/iree-org/iree/actions/runs/34948041142/job/104312435043) | [19m02s](https://github.com/iree-org/iree/actions/runs/34965375511/job/104373127145) | 15 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 15 | 0 | — | — | [15m14s](https://github.com/iree-org/iree/actions/runs/34965374321/job/104368786489) | [16m59s](https://github.com/iree-org/iree/actions/runs/34948041142/job/104312434900) | [22m46s](https://github.com/iree-org/iree/actions/runs/34948043248/job/104313884418) | 15 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 16 | 0 | — | — | [5m23s](https://github.com/iree-org/iree/actions/runs/34965375385/job/104381340924) | [14m31s](https://github.com/iree-org/iree/actions/runs/34965373801/job/104378181410) | [15m15s](https://github.com/iree-org/iree/actions/runs/34966732511/job/104377683683) | 16 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 374 | 1% (5/374) |  | 10m46s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 304 | 2% (5/304) |  | 17m52s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 284 | 1% (3/284) |  | 1h23m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 263 | 8% (22/263) |  | 1d01h ago |

## Alerts

- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job observed waiting 19h05m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h57m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 3h18m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 3h43m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 6h55m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h58m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 4h23m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 7h41m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h59m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 6h36m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h11m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
