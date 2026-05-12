# iree-ci-monitor

_Updated: 2026-05-12 15:46 PDT_ — `iree-org/iree`, queue samples last 10h; live queued up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 21 | 11 | [7h42m](https://github.com/iree-org/iree/actions/runs/25742691185/job/75599029409) | 0 | [1h44m](https://github.com/iree-org/iree/actions/runs/25746463459/job/75616179880) | [3h27m](https://github.com/iree-org/iree/actions/runs/25741726937/job/75596052295) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 20 | 6 | [6h32m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151844) | 0 | [32m26s](https://github.com/iree-org/iree/actions/runs/25743657440/job/75602871116) | [3h12m](https://github.com/iree-org/iree/actions/runs/25744106132/job/75604859711) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 21 | 8 | [6h32m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151971) | 1 | [28m25s](https://github.com/iree-org/iree/actions/runs/25743657440/job/75602870943) | [2h45m](https://github.com/iree-org/iree/actions/runs/25744106132/job/75604859431) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 42 | 17 | [6h32m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613152005) | 0 | [24m34s](https://github.com/iree-org/iree/actions/runs/25743657440/job/75602871113) | [2h11m](https://github.com/iree-org/iree/actions/runs/25742691185/job/75599029407) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 21 | 3 | [4h21m](https://github.com/iree-org/iree/actions/runs/25753418567/job/75637474930) | 0 | [38m08s](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613327629) | [1h56m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458139) | 80% (4/5) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 21 | 6 | [6h20m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458328) | 0 | [1h02m](https://github.com/iree-org/iree/actions/runs/25742723361/job/75599900824) | [1h44m](https://github.com/iree-org/iree/actions/runs/25742691185/job/75599029620) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 21 | 3 | [4h21m](https://github.com/iree-org/iree/actions/runs/25753418567/job/75637475501) | 0 | [9m13s](https://github.com/iree-org/iree/actions/runs/25743657440/job/75602871013) | [1h30m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614252973) | 0% (0/5) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 21 | 4 | [4h24m](https://github.com/iree-org/iree/actions/runs/25753177037/job/75636848383) | 0 | [25m26s](https://github.com/iree-org/iree/actions/runs/25743657440/job/75602871002) | [1h18m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458058) | 0% (0/5) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 21 | 1 | [4h11m](https://github.com/iree-org/iree/actions/runs/25754050386/job/75639336268) | 0 | [13m53s](https://github.com/iree-org/iree/actions/runs/25742663953/job/75601214617) | [1h13m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614253006) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 42 | 2 | [4h24m](https://github.com/iree-org/iree/actions/runs/25753177037/job/75636848572) | 2 | [12m50s](https://github.com/iree-org/iree/actions/runs/25743657440/job/75602871032) | [1h11m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458269) | 9% (1/11) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 42 | 3 | [4h17m](https://github.com/iree-org/iree/actions/runs/25753534872/job/75638096167) | 1 | [12m44s](https://github.com/iree-org/iree/actions/runs/25741726937/job/75596052438) | [1h00m](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613328122) | 0% (0/12) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 22 | 4 | [4h24m](https://github.com/iree-org/iree/actions/runs/25753177037/job/75636848529) | 0 | [10m56s](https://github.com/iree-org/iree/actions/runs/25748901327/job/75621350984) | [53m42s](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613328144) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 21 | 0 | — | 1 | [6m33s](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614253056) | [21m37s](https://github.com/iree-org/iree/actions/runs/25743657440/job/75602871081) | 0% (0/6) | `iree-mi308-1` |
| `ubuntu-24.04` | github-hosted | 487 | 0 | — | 0 | [19s](https://github.com/iree-org/iree/actions/runs/25751058313/job/75627332288) | [10m22s](https://github.com/iree-org/iree/actions/runs/25746783817/job/75614549042) | 42% (59/139) | 479 |
| `macos-14` | github-hosted | 96 | 0 | — | 0 | [20s](https://github.com/iree-org/iree/actions/runs/25748901330/job/75620434727) | [6m46s](https://github.com/iree-org/iree/actions/runs/25746922409/job/75616559947) | 82% (27/33) | 96 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 84 | 0 | — | 0 | [1m06s](https://github.com/iree-org/iree/actions/runs/25736102690/job/75575129790) | [6m41s](https://github.com/iree-org/iree/actions/runs/25754050386/job/75639336303) | 29% (7/24) | 84 |
| `windows-2022` | github-hosted | 96 | 0 | — | 0 | [24s](https://github.com/iree-org/iree/actions/runs/25741727052/job/75593719166) | [6m23s](https://github.com/iree-org/iree/actions/runs/25747443927/job/75617144102) | 82% (27/33) | 96 |
| `ubuntu-24.04-arm` | github-hosted | 96 | 0 | — | 0 | [44s](https://github.com/iree-org/iree/actions/runs/25753534888/job/75635921647) | [5m49s](https://github.com/iree-org/iree/actions/runs/25746922409/job/75616559790) | 82% (27/33) | 96 |
| `azure-windows-scale` | ossci | 32 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25746771810/job/75613364170) | [4m37s](https://github.com/iree-org/iree/actions/runs/25749978264/job/75623984819) | 82% (9/11) | 32 |
| `ubuntu-latest` | github-hosted | 48 | 0 | — | 0 | [28s](https://github.com/iree-org/iree/actions/runs/25746606852/job/75611444826) | [4m24s](https://github.com/iree-org/iree/actions/runs/25746784334/job/75612076468) | 0% (0/22) | 48 |
| `azure-linux-scale` | ossci | 172 | 0 | — | 1 | [15s](https://github.com/iree-org/iree/actions/runs/25746608281/job/75611565749) | [1m16s](https://github.com/iree-org/iree/actions/runs/25747011862/job/75616891587) | 76% (50/66) | 172 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 21 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458102) | [4s](https://github.com/iree-org/iree/actions/runs/25742723361/job/75599901632) | 67% (4/6) | 21 |

## Longest queued jobs (live, last 3d)

| wait | workflow | job | labels | branch | event |
|---:|---|---|---|---|---|
| [7h42m](https://github.com/iree-org/iree/actions/runs/25742691185/job/75599029409) | `PkgCI` | Test ONNX / test_onnx_models :: amdgpu_vulkan | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `swizzled-async-dma-lowering` | pull_request |
| [7h23m](https://github.com/iree-org/iree/actions/runs/25743657440/job/75602870978) | `PkgCI` | Test ONNX / test_onnx_models :: amdgpu_vulkan | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `maxbitsshuffle-amdgpu-squashed` | pull_request |
| [6h32m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151844) | `PkgCI` | Test Torch / test_torch_ops :: amdgpu_vulkan_O3 | `Linux,X64,rdna3,shark10-ci` | `main` | push |
| [6h32m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151919) | `PkgCI` | Test ONNX / test_onnx_models :: amdgpu_vulkan | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [6h32m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151971) | `PkgCI` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `main` | push |
| [6h32m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613152005) | `PkgCI` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |
| [6h32m](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613327740) | `PkgCI` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `main` | push |
| [6h32m](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613328088) | `PkgCI` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |
| [6h32m](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613328129) | `PkgCI` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [6h32m](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613328141) | `PkgCI` | Test ONNX / test_onnx_models :: amdgpu_vulkan | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [6h32m](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613328155) | `PkgCI` | Test Torch / test_torch_ops :: amdgpu_vulkan_O3 | `Linux,X64,rdna3,shark10-ci` | `main` | push |
| [6h27m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614252955) | `PkgCI` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `main` | push |
| [6h27m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614253012) | `PkgCI` | Test ONNX / test_onnx_models :: amdgpu_vulkan | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [6h27m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614253069) | `PkgCI` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [6h27m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614253076) | `PkgCI` | Test Torch / test_torch_ops :: amdgpu_vulkan_O3 | `Linux,X64,rdna3,shark10-ci` | `main` | push |

## Workflow/job waiting time (samples last 10h, live queued up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| `PkgCI` | Test ONNX / test_onnx_models :: amdgpu_vulkan | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 21 | 11 | [7h42m](https://github.com/iree-org/iree/actions/runs/25742691185/job/75599029409) | [1h44m](https://github.com/iree-org/iree/actions/runs/25746463459/job/75616179880) | [3h27m](https://github.com/iree-org/iree/actions/runs/25741726937/job/75596052295) | [3h27m](https://github.com/iree-org/iree/actions/runs/25741726937/job/75596052295) | 1 |
| `PkgCI` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 21 | 8 | [6h32m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151971) | [28m25s](https://github.com/iree-org/iree/actions/runs/25743657440/job/75602870943) | [2h45m](https://github.com/iree-org/iree/actions/runs/25744106132/job/75604859431) | [2h45m](https://github.com/iree-org/iree/actions/runs/25744106132/job/75604859431) | 1 |
| `PkgCI` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 21 | 8 | [6h32m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613152005) | [26m43s](https://github.com/iree-org/iree/actions/runs/25739782401/job/75588249835) | [2h11m](https://github.com/iree-org/iree/actions/runs/25742691185/job/75599029407) | [2h11m](https://github.com/iree-org/iree/actions/runs/25742691185/job/75599029407) | 1 |
| `PkgCI` | Test Torch / test_torch_ops :: amdgpu_vulkan_O3 | `Linux,X64,rdna3,shark10-ci` | 20 | 6 | [6h32m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151844) | [32m26s](https://github.com/iree-org/iree/actions/runs/25743657440/job/75602871116) | [3h12m](https://github.com/iree-org/iree/actions/runs/25744106132/job/75604859711) | [3h12m](https://github.com/iree-org/iree/actions/runs/25744106132/job/75604859711) | 1 |
| `PkgCI` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 21 | 9 | [6h32m](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613328129) | [20m11s](https://github.com/iree-org/iree/actions/runs/25742663953/job/75601214955) | [2h42m](https://github.com/iree-org/iree/actions/runs/25742301702/job/75598103695) | [2h42m](https://github.com/iree-org/iree/actions/runs/25742301702/job/75598103695) | 1 |
| `PkgCI` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 21 | 6 | [6h20m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458328) | [1h02m](https://github.com/iree-org/iree/actions/runs/25742723361/job/75599900824) | [1h44m](https://github.com/iree-org/iree/actions/runs/25742691185/job/75599029620) | [2h19m](https://github.com/iree-org/iree/actions/runs/25741726937/job/75596052373) | 1 |
| `PkgCI` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 21 | 4 | [4h24m](https://github.com/iree-org/iree/actions/runs/25753177037/job/75636848383) | [25m26s](https://github.com/iree-org/iree/actions/runs/25743657440/job/75602871002) | [1h18m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458058) | [1h53m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151798) | 2 |
| `PkgCI` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 21 | 2 | [4h24m](https://github.com/iree-org/iree/actions/runs/25753177037/job/75636848572) | [13m39s](https://github.com/iree-org/iree/actions/runs/25744106132/job/75604859567) | [1h05m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458045) | [1h13m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613152006) | 4 |
| `PkgCI` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_O0 | `Linux,X64,rdna3` | 20 | 2 | [4h24m](https://github.com/iree-org/iree/actions/runs/25753177037/job/75636848529) | [10m56s](https://github.com/iree-org/iree/actions/runs/25748901327/job/75621350984) | [53m42s](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613328144) | [59m24s](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458174) | 3 |
| `PkgCI` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 21 | 3 | [4h21m](https://github.com/iree-org/iree/actions/runs/25753418567/job/75637474930) | [38m08s](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613327629) | [1h56m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458139) | [1h57m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614252942) | 2 |
| `PkgCI` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 21 | 3 | [4h21m](https://github.com/iree-org/iree/actions/runs/25753418567/job/75637475501) | [9m13s](https://github.com/iree-org/iree/actions/runs/25743657440/job/75602871013) | [1h30m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614252973) | [1h46m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458038) | 2 |
| `PkgCI` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 21 | 2 | [4h17m](https://github.com/iree-org/iree/actions/runs/25753534872/job/75638096167) | [17m18s](https://github.com/iree-org/iree/actions/runs/25743657440/job/75602871204) | [1h34m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458237) | [1h37m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614253149) | 3 |
| `PkgCI` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 1 | [4h17m](https://github.com/iree-org/iree/actions/runs/25753534872/job/75638096113) | 0s | 0s | 0s | 0 |
| `PkgCI` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 1 | [4h17m](https://github.com/iree-org/iree/actions/runs/25753534872/job/75638096259) | 0s | 0s | 0s | 0 |
| `PkgCI` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 21 | 1 | [4h11m](https://github.com/iree-org/iree/actions/runs/25754050386/job/75639336268) | [13m53s](https://github.com/iree-org/iree/actions/runs/25742663953/job/75601214617) | [1h13m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614253006) | [1h26m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458293) | 3 |
| `PkgCI` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 21 | 1 | [4h11m](https://github.com/iree-org/iree/actions/runs/25754050386/job/75639336370) | [11m29s](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151876) | [57m43s](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614253171) | [1h00m](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613328122) | 3 |
| `PkgCI` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 21 | 0 | — | [7m29s](https://github.com/iree-org/iree/actions/runs/25741726937/job/75596052381) | [1h11m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458269) | [1h12m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614253191) | 4 |
| `PkgCI` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 21 | 0 | — | [6m33s](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614253056) | [21m37s](https://github.com/iree-org/iree/actions/runs/25743657440/job/75602871081) | [44m28s](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151985) | 1 |
| `CI` | setup / setup | `ubuntu-24.04` | 34 | 0 | — | [12s](https://github.com/iree-org/iree/actions/runs/25743657367/job/75600809264) | [20m45s](https://github.com/iree-org/iree/actions/runs/25746922409/job/75612565586) | [21m57s](https://github.com/iree-org/iree/actions/runs/25746840561/job/75612278349) | 32 |
| `PkgCI` | setup / setup | `ubuntu-24.04` | 34 | 0 | — | [16s](https://github.com/iree-org/iree/actions/runs/25743657440/job/75600808718) | [19m30s](https://github.com/iree-org/iree/actions/runs/25747011909/job/75612884544) | [22m10s](https://github.com/iree-org/iree/actions/runs/25746840602/job/75612278638) | 32 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,shark55-ci`, `self-hosted,persistent-cache,Linux,X64` | 788 | 2% (12/785) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,shark01-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 905 | 3% (26/902) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 1070 | 9% (92/1066) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 298 | 3% (8/296) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1138 | 4% (49/1135) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job waiting 4h11m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 4h17m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 6h20m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 6h32m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 6h32m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 4h21m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 4h21m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 7h42m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 6h32m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job waiting 4h24m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 4h24m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job waiting 4h24m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h13m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h44m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h11m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h45m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h56m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h30m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 3h27m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 3h12m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h18m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h11m (> 1h00m)
- **[high-failure-main]** `azure-linux-scale` main-branch failure rate 76% (50/66)
- **[high-failure-main]** `azure-windows-scale` main-branch failure rate 82% (9/11)
- **[high-failure-main]** `linux-mi325-1gpu-ossci-iree-org` main-branch failure rate 29% (7/24)
- **[high-failure-main]** `macos-14` main-branch failure rate 82% (27/33)
- **[high-failure-main]** `ubuntu-24.04-arm` main-branch failure rate 82% (27/33)
- **[high-failure-main]** `ubuntu-24.04` main-branch failure rate 42% (59/139)
- **[high-failure-main]** `windows-2022` main-branch failure rate 82% (27/33)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
