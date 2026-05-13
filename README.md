# iree-ci-monitor

_Updated: 2026-05-12 18:18 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 31 | 5 | [8h49m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458265) | 2m25s ago | 1 | [2h15m](https://github.com/iree-org/iree/actions/runs/25760876748/job/75662581375) | [7h47m](https://github.com/iree-org/iree/actions/runs/25749978296/job/75625010185) | 0% (0/4) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 42 | 12 | [8h56m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614252955) | 2m25s ago | 0 | [1h58m](https://github.com/iree-org/iree/actions/runs/25749978296/job/75625010110) | [5h49m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151971) | 67% (2/3) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 84 | 39 | [9h01m](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613328129) | 2m25s ago | 1 | [1h43m](https://github.com/iree-org/iree/actions/runs/25765152239/job/75677000015) | [5h09m](https://github.com/iree-org/iree/actions/runs/25749978296/job/75625010177) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 42 | 10 | [6h50m](https://github.com/iree-org/iree/actions/runs/25753418567/job/75637475646) | 2m25s ago | 0 | [1h37m](https://github.com/iree-org/iree/actions/runs/25763408405/job/75672655355) | [4h30m](https://github.com/iree-org/iree/actions/runs/25757338638/job/75651716526) | 0% (0/5) | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 27 | 7 | [9h01m](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613328155) | 2m25s ago | 0 | [32m26s](https://github.com/iree-org/iree/actions/runs/25743657440/job/75602871116) | [3h30m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151844) | 0% (0/2) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 42 | 6 | [3h39m](https://github.com/iree-org/iree/actions/runs/25763200756/job/75670916723) | 2m25s ago | 0 | [1h11m](https://github.com/iree-org/iree/actions/runs/25763355656/job/75671403706) | [3h07m](https://github.com/iree-org/iree/actions/runs/25764416366/job/75674841820) | 0% (0/8) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 84 | 8 | [2h27m](https://github.com/iree-org/iree/actions/runs/25765602314/job/75680900846) | 2m25s ago | 1 | [49m22s](https://github.com/iree-org/iree/actions/runs/25763200756/job/75670916706) | [2h57m](https://github.com/iree-org/iree/actions/runs/25764416366/job/75674841864) | 0% (0/16) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 42 | 12 | [5h57m](https://github.com/iree-org/iree/actions/runs/25756345869/job/75647201836) | 2m25s ago | 0 | [54m52s](https://github.com/iree-org/iree/actions/runs/25756538530/job/75648574859) | [2h42m](https://github.com/iree-org/iree/actions/runs/25757338638/job/75651716373) | 57% (4/7) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 42 | 8 | [4h29m](https://github.com/iree-org/iree/actions/runs/25760876748/job/75662581345) | 2m25s ago | 0 | [40m14s](https://github.com/iree-org/iree/actions/runs/25753534872/job/75638096032) | [2h40m](https://github.com/iree-org/iree/actions/runs/25765152239/job/75676999898) | 0% (0/7) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 57 | 5 | [2h19m](https://github.com/iree-org/iree/actions/runs/25765901140/job/75681873829) | 2m25s ago | 0 | [40m23s](https://github.com/iree-org/iree/actions/runs/25759270717/job/75658473445) | [2h22m](https://github.com/iree-org/iree/actions/runs/25765152239/job/75677000057) | 0% (0/12) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 84 | 5 | [2h23m](https://github.com/iree-org/iree/actions/runs/25766582410/job/75681459681) | 2m25s ago | 2 | [48m11s](https://github.com/iree-org/iree/actions/runs/25762938040/job/75669682165) | [2h15m](https://github.com/iree-org/iree/actions/runs/25765901140/job/75681873894) | 6% (1/18) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [1h21m](https://github.com/iree-org/iree/actions/runs/25762938040/job/75669682119) | [2h02m](https://github.com/iree-org/iree/actions/runs/25766582410/job/75681459696) | 67% (2/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 42 | 2 | [2h19m](https://github.com/iree-org/iree/actions/runs/25765901140/job/75681873776) | 2m25s ago | 0 | [22m08s](https://github.com/iree-org/iree/actions/runs/25756813207/job/75649398750) | [1h40m](https://github.com/iree-org/iree/actions/runs/25763355656/job/75671403613) | 0% (0/9) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 42 | 0 | — | — | 0 | [10m54s](https://github.com/iree-org/iree/actions/runs/25756345869/job/75647202059) | [28m40s](https://github.com/iree-org/iree/actions/runs/25759270717/job/75658473423) | 0% (0/10) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 168 | 0 | — | — | 0 | [1m16s](https://github.com/iree-org/iree/actions/runs/25753177037/job/75636848566) | [12m27s](https://github.com/iree-org/iree/actions/runs/25766582410/job/75681459705) | 18% (7/40) | 165 |
| `ubuntu-24.04` | github-hosted | 935 | 6 | [3m10s](https://github.com/iree-org/iree/actions/runs/25771897440/job/75696721171) | 2m25s ago | 8 | [10s](https://github.com/iree-org/iree/actions/runs/25751012563/job/75653407178) | [7m32s](https://github.com/iree-org/iree/actions/runs/25747443927/job/75617144070) | 31% (62/203) | 907 |
| `macos-14` | github-hosted | 178 | 1 | [2m54s](https://github.com/iree-org/iree/actions/runs/25771910643/job/75696746597) | 2m25s ago | 3 | [5s](https://github.com/iree-org/iree/actions/runs/25746463499/job/75610983603) | [6m04s](https://github.com/iree-org/iree/actions/runs/25746783817/job/75614549186) | 62% (28/45) | 177 |
| `windows-2022` | github-hosted | 177 | 1 | [2m54s](https://github.com/iree-org/iree/actions/runs/25771910643/job/75696746560) | 2m25s ago | 5 | [5s](https://github.com/iree-org/iree/actions/runs/25751012563/job/75627044929) | [5m58s](https://github.com/iree-org/iree/actions/runs/25746922409/job/75616559821) | 62% (28/45) | 176 |
| `ubuntu-24.04-arm` | github-hosted | 177 | 2 | [2m54s](https://github.com/iree-org/iree/actions/runs/25771910643/job/75696746562) | 2m25s ago | 3 | [19s](https://github.com/iree-org/iree/actions/runs/25746840561/job/75616508221) | [5m11s](https://github.com/iree-org/iree/actions/runs/25746922409/job/75616559881) | 60% (27/45) | 175 |
| `azure-windows-scale` | ossci | 59 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25746783817/job/75614549256) | [4m37s](https://github.com/iree-org/iree/actions/runs/25749978264/job/75623984819) | 60% (9/15) | 59 |
| `ubuntu-latest` | github-hosted | 67 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/25744104548/job/75602427610) | [4m22s](https://github.com/iree-org/iree/actions/runs/25748502308/job/75618204056) | 0% (0/30) | 67 |
| `azure-linux-scale` | ossci | 314 | 0 | — | — | 10 | [10s](https://github.com/iree-org/iree/actions/runs/25763355608/job/75670103521) | [1m58s](https://github.com/iree-org/iree/actions/runs/25758969060/job/75655310076) | 56% (50/90) | 313 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m37s](https://github.com/iree-org/iree/actions/runs/25766582376/job/75680402831) | [1m37s](https://github.com/iree-org/iree/actions/runs/25766582376/job/75680402831) | — | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 42 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25753418567/job/75637475626) | [3s](https://github.com/iree-org/iree/actions/runs/25759261073/job/75657352809) | 50% (5/10) | 41 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25766582376/job/75680402834) | [2s](https://github.com/iree-org/iree/actions/runs/25766582376/job/75680402834) | — | 1 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [9h01m](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613328129) | 2m25s ago | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [9h01m](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613328155) | 2m25s ago | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_O3 | `Linux,X64,rdna3,shark10-ci` | `main` | push |
| [8h56m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614252955) | 2m25s ago | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `main` | push |
| [8h56m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614253069) | 2m25s ago | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [8h56m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614253076) | 2m25s ago | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_O3 | `Linux,X64,rdna3,shark10-ci` | `main` | push |
| [8h49m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458085) | 2m25s ago | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `main` | push |
| [8h49m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458144) | 2m25s ago | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_O3 | `Linux,X64,rdna3,shark10-ci` | `main` | push |
| [8h49m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458152) | 2m25s ago | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [8h49m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458155) | 2m25s ago | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |
| [8h49m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458265) | 2m25s ago | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [6h53m](https://github.com/iree-org/iree/actions/runs/25753177037/job/75636848384) | 2m25s ago | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_O3 | `Linux,X64,rdna3,shark10-ci` | `users/benvanik/fix-main-ci-after-24007` | pull_request |
| [6h53m](https://github.com/iree-org/iree/actions/runs/25753177037/job/75636848411) | 2m25s ago | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `users/benvanik/fix-main-ci-after-24007` | pull_request |
| [6h53m](https://github.com/iree-org/iree/actions/runs/25753177037/job/75636848492) | 2m25s ago | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/benvanik/fix-main-ci-after-24007` | pull_request |
| [6h50m](https://github.com/iree-org/iree/actions/runs/25753418567/job/75637475422) | 2m25s ago | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `main` | push |
| [6h50m](https://github.com/iree-org/iree/actions/runs/25753418567/job/75637475646) | 2m25s ago | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 42 | 22 | [9h01m](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613328129) | 2m25s ago | [1h43m](https://github.com/iree-org/iree/actions/runs/25765152239/job/75677000015) | [5h09m](https://github.com/iree-org/iree/actions/runs/25749978296/job/75625010177) | [5h09m](https://github.com/iree-org/iree/actions/runs/25749978296/job/75625010177) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_O3 | `Linux,X64,rdna3,shark10-ci` | 27 | 7 | [9h01m](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613328155) | 2m25s ago | [32m26s](https://github.com/iree-org/iree/actions/runs/25743657440/job/75602871116) | [3h30m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151844) | [3h30m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151844) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 42 | 12 | [8h56m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614252955) | 2m25s ago | [1h58m](https://github.com/iree-org/iree/actions/runs/25749978296/job/75625010110) | [5h49m](https://github.com/iree-org/iree/actions/runs/25746608261/job/75613151971) | [6h48m](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613327740) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 42 | 17 | [8h49m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458155) | 2m25s ago | [2h21m](https://github.com/iree-org/iree/actions/runs/25756345869/job/75647201844) | [5h02m](https://github.com/iree-org/iree/actions/runs/25758969066/job/75656280106) | [5h10m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614253107) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 28 | 3 | [8h49m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458265) | 2m25s ago | [2h15m](https://github.com/iree-org/iree/actions/runs/25760876748/job/75662581375) | [7h47m](https://github.com/iree-org/iree/actions/runs/25749978296/job/75625010185) | [7h57m](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614253012) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 42 | 10 | [6h50m](https://github.com/iree-org/iree/actions/runs/25753418567/job/75637475646) | 2m25s ago | [1h37m](https://github.com/iree-org/iree/actions/runs/25763408405/job/75672655355) | [4h30m](https://github.com/iree-org/iree/actions/runs/25757338638/job/75651716526) | [6h20m](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458328) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 42 | 12 | [5h57m](https://github.com/iree-org/iree/actions/runs/25756345869/job/75647201836) | 2m25s ago | [54m52s](https://github.com/iree-org/iree/actions/runs/25756538530/job/75648574859) | [2h42m](https://github.com/iree-org/iree/actions/runs/25757338638/job/75651716373) | [3h21m](https://github.com/iree-org/iree/actions/runs/25762938040/job/75669681824) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 42 | 8 | [4h29m](https://github.com/iree-org/iree/actions/runs/25760876748/job/75662581345) | 2m25s ago | [40m14s](https://github.com/iree-org/iree/actions/runs/25753534872/job/75638096032) | [2h40m](https://github.com/iree-org/iree/actions/runs/25765152239/job/75676999898) | [3h23m](https://github.com/iree-org/iree/actions/runs/25763200756/job/75670916622) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 42 | 4 | [2h27m](https://github.com/iree-org/iree/actions/runs/25765602314/job/75680900859) | 2m25s ago | [40m49s](https://github.com/iree-org/iree/actions/runs/25763355656/job/75671403660) | [4h05m](https://github.com/iree-org/iree/actions/runs/25758969066/job/75656279980) | [5h00m](https://github.com/iree-org/iree/actions/runs/25757953441/job/75652658517) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 42 | 6 | [3h39m](https://github.com/iree-org/iree/actions/runs/25763200756/job/75670916723) | 2m25s ago | [1h11m](https://github.com/iree-org/iree/actions/runs/25763355656/job/75671403706) | [3h07m](https://github.com/iree-org/iree/actions/runs/25764416366/job/75674841820) | [3h31m](https://github.com/iree-org/iree/actions/runs/25757953441/job/75652658379) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 42 | 4 | [2h27m](https://github.com/iree-org/iree/actions/runs/25765602314/job/75680900846) | 2m25s ago | [49m22s](https://github.com/iree-org/iree/actions/runs/25763200756/job/75670916706) | [2h26m](https://github.com/iree-org/iree/actions/runs/25764416366/job/75674841897) | [2h40m](https://github.com/iree-org/iree/actions/runs/25759270717/job/75658473471) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 15 | 2 | [1h27m](https://github.com/iree-org/iree/actions/runs/25768725585/job/75687831348) | 2m25s ago | [1h35m](https://github.com/iree-org/iree/actions/runs/25764416366/job/75674841833) | [2h23m](https://github.com/iree-org/iree/actions/runs/25763200756/job/75670916737) | [2h26m](https://github.com/iree-org/iree/actions/runs/25763408405/job/75672655508) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 42 | 3 | [2h23m](https://github.com/iree-org/iree/actions/runs/25766582410/job/75681459681) | 2m25s ago | [42m20s](https://github.com/iree-org/iree/actions/runs/25755952428/job/75645931934) | [1h53m](https://github.com/iree-org/iree/actions/runs/25757953441/job/75652658435) | [3h16m](https://github.com/iree-org/iree/actions/runs/25763355656/job/75671403595) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 15 | 3 | [2h19m](https://github.com/iree-org/iree/actions/runs/25765901140/job/75681873829) | 2m25s ago | [1h18m](https://github.com/iree-org/iree/actions/runs/25765356901/job/75680702085) | [2h22m](https://github.com/iree-org/iree/actions/runs/25765152239/job/75677000057) | [2h22m](https://github.com/iree-org/iree/actions/runs/25765152239/job/75677000057) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 42 | 2 | [2h19m](https://github.com/iree-org/iree/actions/runs/25765901140/job/75681873776) | 2m25s ago | [22m08s](https://github.com/iree-org/iree/actions/runs/25756813207/job/75649398750) | [1h40m](https://github.com/iree-org/iree/actions/runs/25763355656/job/75671403613) | [2h08m](https://github.com/iree-org/iree/actions/runs/25765602314/job/75680900752) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 42 | 2 | [1h27m](https://github.com/iree-org/iree/actions/runs/25768725585/job/75687831437) | 2m25s ago | [49m31s](https://github.com/iree-org/iree/actions/runs/25746734624/job/75614253126) | [2h07m](https://github.com/iree-org/iree/actions/runs/25766582410/job/75681459664) | [2h42m](https://github.com/iree-org/iree/actions/runs/25756345869/job/75647201910) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 11 | 0 | — | — | [1h21m](https://github.com/iree-org/iree/actions/runs/25762938040/job/75669682119) | [2h02m](https://github.com/iree-org/iree/actions/runs/25766582410/job/75681459696) | [2h02m](https://github.com/iree-org/iree/actions/runs/25766582410/job/75681459696) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 2 | [1h27m](https://github.com/iree-org/iree/actions/runs/25768725585/job/75687831418) | 2m25s ago | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_O0 | `Linux,X64,rdna3` | 27 | 0 | — | — | [20m29s](https://github.com/iree-org/iree/actions/runs/25753418567/job/75637475842) | [53m42s](https://github.com/iree-org/iree/actions/runs/25746700586/job/75613328144) | [59m24s](https://github.com/iree-org/iree/actions/runs/25746771816/job/75615458174) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 42 | 0 | — | — | [10m54s](https://github.com/iree-org/iree/actions/runs/25756345869/job/75647202059) | [28m40s](https://github.com/iree-org/iree/actions/runs/25759270717/job/75658473423) | [51m40s](https://github.com/iree-org/iree/actions/runs/25756813207/job/75649398679) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 999 | 8% (83/995) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,shark55-ci`, `self-hosted,persistent-cache,Linux,X64` | 754 | 2% (18/752) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1050 | 5% (49/1048) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,shark01-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 857 | 3% (24/855) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 288 | 3% (10/288) |  | 11m02s ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 2h19m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 2h27m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job observed waiting 6h50m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 9h01m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job observed waiting 8h56m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job observed waiting 5h57m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job observed waiting 4h29m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job observed waiting 8h49m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job observed waiting 9h01m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 2h19m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job observed waiting 3h39m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job observed waiting 2h23m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h40m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h57m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 4h30m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 5h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 5h49m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h42m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 2h40m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 7h47m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache` p95 queue 2h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 3h30m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h22m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 3h07m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h15m (> 1h00m)
- **[high-failure-main]** `azure-linux-scale` main-branch failure rate 56% (50/90)
- **[high-failure-main]** `azure-windows-scale` main-branch failure rate 60% (9/15)
- **[high-failure-main]** `linux-mi35x-1gpu-ossci-iree-org` main-branch failure rate 50% (5/10)
- **[high-failure-main]** `macos-14` main-branch failure rate 62% (28/45)
- **[high-failure-main]** `ubuntu-24.04-arm` main-branch failure rate 60% (27/45)
- **[high-failure-main]** `ubuntu-24.04` main-branch failure rate 31% (62/203)
- **[high-failure-main]** `windows-2022` main-branch failure rate 62% (28/45)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
