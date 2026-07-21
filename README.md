# iree-ci-monitor

_Updated: 2026-07-21 11:47 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 44 | 10 | [4h37m](https://github.com/iree-org/iree/actions/runs/29837056622/job/88658267077) | 2026-07-21 11:45 PDT | 1 | [1h58m](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071486) | [5h00m](https://github.com/iree-org/iree/actions/runs/29831130574/job/88642907159) | 0% (0/5) | `shark75-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 22 | 0 | — | — | 0 | [2h25m](https://github.com/iree-org/iree/actions/runs/29831173036/job/88662434255) | [4h40m](https://github.com/iree-org/iree/actions/runs/29826696754/job/88623281316) | 0% (0/5) | 18 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 22 | 0 | — | — | 0 | [2h29m](https://github.com/iree-org/iree/actions/runs/29845395879/job/88686375233) | [4h27m](https://github.com/iree-org/iree/actions/runs/29832385203/job/88647076603) | 0% (0/5) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 22 | 0 | — | — | 0 | [1h07m](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071210) | [3h55m](https://github.com/iree-org/iree/actions/runs/29837098393/job/88658960981) | 0% (0/5) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 22 | 0 | — | — | 0 | [1h52m](https://github.com/iree-org/iree/actions/runs/29838079692/job/88662193279) | [3h09m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671757943) | 0% (0/5) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 22 | 0 | — | — | 0 | [55m34s](https://github.com/iree-org/iree/actions/runs/29826696754/job/88623281289) | [3h01m](https://github.com/iree-org/iree/actions/runs/29834451918/job/88653622356) | 20% (1/5) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 44 | 0 | — | — | 0 | [39m54s](https://github.com/iree-org/iree/actions/runs/29831173036/job/88662434319) | [2h43m](https://github.com/iree-org/iree/actions/runs/29838079692/job/88662193405) | 0% (0/10) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 22 | 0 | — | — | 0 | [44m04s](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672959109) | [2h35m](https://github.com/iree-org/iree/actions/runs/29837056622/job/88658267023) | 0% (0/5) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 44 | 0 | — | — | 0 | [28m52s](https://github.com/iree-org/iree/actions/runs/29832258711/job/88647107396) | [2h32m](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819739) | 0% (0/10) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 22 | 0 | — | — | 0 | [32m16s](https://github.com/iree-org/iree/actions/runs/29849303530/job/88700132081) | [2h20m](https://github.com/iree-org/iree/actions/runs/29831173036/job/88662434247) | 0% (0/5) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 22 | 0 | — | — | 0 | [24m25s](https://github.com/iree-org/iree/actions/runs/29829956804/job/88633904278) | [1h32m](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819373) | 0% (0/5) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 44 | 0 | — | — | 0 | [20m14s](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671757934) | [1h28m](https://github.com/iree-org/iree/actions/runs/29837056622/job/88658266918) | 0% (0/10) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 22 | 0 | — | — | 0 | [5m31s](https://github.com/iree-org/iree/actions/runs/29837056622/job/88658267154) | [35m46s](https://github.com/iree-org/iree/actions/runs/29831173036/job/88662434379) | 0% (0/5) | `iree-mi308-1` |
| `ubuntu-24.04-arm` | github-hosted | 78 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/29834452027/job/88650883767) | [4m19s](https://github.com/iree-org/iree/actions/runs/29826773862/job/88621876316) | 0% (0/15) | 78 |
| `ubuntu-24.04` | github-hosted | 487 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29832258728/job/88639698670) | [4m03s](https://github.com/iree-org/iree/actions/runs/29838192343/job/88662294880) | 6% (5/90) | 473 |
| `macos-14` | github-hosted | 79 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29849302999/job/88697956532) | [3m52s](https://github.com/iree-org/iree/actions/runs/29826773862/job/88621876310) | 0% (0/16) | 78 |
| `windows-2022` | github-hosted | 78 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/29849231784/job/88697626161) | [3m17s](https://github.com/iree-org/iree/actions/runs/29837098344/job/88656893826) | 7% (1/15) | 78 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [2m29s](https://github.com/iree-org/iree/actions/runs/29820807870/job/88602745897) | [2m29s](https://github.com/iree-org/iree/actions/runs/29820807870/job/88602745897) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 139 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/29840946973/job/88669957077) | [2m11s](https://github.com/iree-org/iree/actions/runs/29832385195/job/88640126064) | 12% (4/33) | 139 |
| `ubuntu-latest` | github-hosted | 42 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29826693600/job/88621548720) | [1m02s](https://github.com/iree-org/iree/actions/runs/29837096892/job/88656151822) | 0% (0/15) | 42 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/29820798316/job/88602714944) | [4s](https://github.com/iree-org/iree/actions/runs/29820798316/job/88602714944) | 0% (0/1) | 1 |
| `azure-windows-scale` | ossci | 26 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29841128995/job/88670315495) | [2s](https://github.com/iree-org/iree/actions/runs/29849302999/job/88697956671) | 20% (1/5) | 26 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [4h37m](https://github.com/iree-org/iree/actions/runs/29837056622/job/88658267077) | 2026-07-21 11:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |
| [4h34m](https://github.com/iree-org/iree/actions/runs/29837098393/job/88658961083) | 2026-07-21 11:45 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [4h34m](https://github.com/iree-org/iree/actions/runs/29837098393/job/88658961189) | 2026-07-21 11:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |
| [4h21m](https://github.com/iree-org/iree/actions/runs/29831173036/job/88662434156) | 2026-07-21 11:45 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `fix/23345-custom-op-static-loop-ranges` | pull_request |
| [3h48m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671758164) | 2026-07-21 11:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `vk-local-fallback` | pull_request |
| [3h47m](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819489) | 2026-07-21 11:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `vk-optional-host-pointer-props` | pull_request |
| [3h43m](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672959539) | 2026-07-21 11:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `vk-disable-sparse` | pull_request |
| [3h29m](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071640) | 2026-07-21 11:45 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `egb.fix_rvv_tile_size_selection` | pull_request |
| [2h54m](https://github.com/iree-org/iree/actions/runs/29845395879/job/88686375287) | 2026-07-21 11:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |
| [2h54m](https://github.com/iree-org/iree/actions/runs/29845395879/job/88686375408) | 2026-07-21 11:45 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 22 | 6 | [4h37m](https://github.com/iree-org/iree/actions/runs/29837056622/job/88658267077) | 2026-07-21 11:45 PDT | [1h58m](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071486) | [5h00m](https://github.com/iree-org/iree/actions/runs/29831130574/job/88642907159) | [5h05m](https://github.com/iree-org/iree/actions/runs/29832385203/job/88647076660) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 22 | 0 | — | — | [2h25m](https://github.com/iree-org/iree/actions/runs/29831173036/job/88662434255) | [4h40m](https://github.com/iree-org/iree/actions/runs/29826696754/job/88623281316) | [4h51m](https://github.com/iree-org/iree/actions/runs/29821377902/job/88620860072) | 18 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 22 | 4 | [4h34m](https://github.com/iree-org/iree/actions/runs/29837098393/job/88658961083) | 2026-07-21 11:45 PDT | [2h14m](https://github.com/iree-org/iree/actions/runs/29829956804/job/88633904467) | [4h31m](https://github.com/iree-org/iree/actions/runs/29837056622/job/88658267350) | [4h51m](https://github.com/iree-org/iree/actions/runs/29832385203/job/88647076808) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 22 | 0 | — | — | [2h29m](https://github.com/iree-org/iree/actions/runs/29845395879/job/88686375233) | [4h27m](https://github.com/iree-org/iree/actions/runs/29832385203/job/88647076603) | [4h56m](https://github.com/iree-org/iree/actions/runs/29832258711/job/88647107485) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 22 | 0 | — | — | [1h07m](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071210) | [3h55m](https://github.com/iree-org/iree/actions/runs/29837098393/job/88658960981) | [4h10m](https://github.com/iree-org/iree/actions/runs/29832385203/job/88647076725) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 22 | 0 | — | — | [1h52m](https://github.com/iree-org/iree/actions/runs/29838079692/job/88662193279) | [3h09m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671757943) | [3h30m](https://github.com/iree-org/iree/actions/runs/29831173036/job/88662434237) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 22 | 0 | — | — | [55m34s](https://github.com/iree-org/iree/actions/runs/29826696754/job/88623281289) | [3h01m](https://github.com/iree-org/iree/actions/runs/29834451918/job/88653622356) | [3h03m](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819353) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 22 | 0 | — | — | [26m57s](https://github.com/iree-org/iree/actions/runs/29826696754/job/88623281643) | [2h44m](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071502) | [3h40m](https://github.com/iree-org/iree/actions/runs/29837098393/job/88658961242) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 22 | 0 | — | — | [48m05s](https://github.com/iree-org/iree/actions/runs/29845395879/job/88686375288) | [2h43m](https://github.com/iree-org/iree/actions/runs/29838079692/job/88662193405) | [4h20m](https://github.com/iree-org/iree/actions/runs/29832258711/job/88647107593) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 22 | 0 | — | — | [34m58s](https://github.com/iree-org/iree/actions/runs/29834451918/job/88653622508) | [2h38m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671758041) | [3h23m](https://github.com/iree-org/iree/actions/runs/29837098393/job/88658961148) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 22 | 0 | — | — | [44m04s](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672959109) | [2h35m](https://github.com/iree-org/iree/actions/runs/29837056622/job/88658267023) | [2h51m](https://github.com/iree-org/iree/actions/runs/29837098393/job/88658961155) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 22 | 0 | — | — | [32m16s](https://github.com/iree-org/iree/actions/runs/29849303530/job/88700132081) | [2h20m](https://github.com/iree-org/iree/actions/runs/29831173036/job/88662434247) | [2h49m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671758048) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 22 | 0 | — | — | [31m57s](https://github.com/iree-org/iree/actions/runs/29829360721/job/88631897492) | [2h09m](https://github.com/iree-org/iree/actions/runs/29838079692/job/88662193433) | [2h32m](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819739) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 22 | 0 | — | — | [20m41s](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671758187) | [1h40m](https://github.com/iree-org/iree/actions/runs/29837098393/job/88658961120) | [2h01m](https://github.com/iree-org/iree/actions/runs/29832385203/job/88647076719) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 22 | 0 | — | — | [24m25s](https://github.com/iree-org/iree/actions/runs/29829956804/job/88633904278) | [1h32m](https://github.com/iree-org/iree/actions/runs/29841118280/job/88671819373) | [2h18m](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671758177) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 22 | 0 | — | — | [20m14s](https://github.com/iree-org/iree/actions/runs/29840946798/job/88671757934) | [41m10s](https://github.com/iree-org/iree/actions/runs/29834451918/job/88653622431) | [54m49s](https://github.com/iree-org/iree/actions/runs/29837098393/job/88658961068) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 22 | 0 | — | — | [5m31s](https://github.com/iree-org/iree/actions/runs/29837056622/job/88658267154) | [35m46s](https://github.com/iree-org/iree/actions/runs/29831173036/job/88662434379) | [43m32s](https://github.com/iree-org/iree/actions/runs/29841129262/job/88672959375) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 26 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/29834452027/job/88650883727) | [7m33s](https://github.com/iree-org/iree/actions/runs/29838079545/job/88660738599) | [12m08s](https://github.com/iree-org/iree/actions/runs/29838192632/job/88660534295) | 25 |
| `.github/workflows/pkgci.yml` | Unit Test / Linux (x86_64) | `ubuntu-24.04` | 22 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29842506987/job/88677071022) | [6m44s](https://github.com/iree-org/iree/actions/runs/29838079692/job/88662193105) | [7m11s](https://github.com/iree-org/iree/actions/runs/29831173036/job/88662434357) | 22 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 6 | 0 | — | — | [41s](https://github.com/iree-org/iree/actions/runs/29837098344/job/88656893996) | [6m26s](https://github.com/iree-org/iree/actions/runs/29845395719/job/88684636659) | [6m26s](https://github.com/iree-org/iree/actions/runs/29845395719/job/88684636659) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 278 | 0% (0/277) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 241 | 4% (10/241) |  | 19m30s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 223 | 1% (2/223) |  | 35m40s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 215 | 0% (0/215) |  | 43m40s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 67 | 0% (0/67) |  | 1h50m ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 4h37m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h35m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 5h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 3h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 3h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 3h55m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 4h27m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h43m (> 1h00m)
- **[queue-starved]** `linux-mi325-1gpu-ossci-iree-org` p95 queue 4h40m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 2h20m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h28m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
