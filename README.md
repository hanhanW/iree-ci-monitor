# iree-ci-monitor

_Updated: 2026-05-21 18:20 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 28 | 0 | — | — | 0 | [41m22s](https://github.com/iree-org/iree/actions/runs/26258672591/job/77288096907) | [2h41m](https://github.com/iree-org/iree/actions/runs/26246079836/job/77245860333) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 14 | 0 | — | — | 0 | [45m53s](https://github.com/iree-org/iree/actions/runs/26240827394/job/77227846560) | [2h17m](https://github.com/iree-org/iree/actions/runs/26242793965/job/77247541064) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 14 | 0 | — | — | 0 | [34m35s](https://github.com/iree-org/iree/actions/runs/26238648585/job/77220351846) | [1h58m](https://github.com/iree-org/iree/actions/runs/26246079367/job/77246047231) | 0% (0/1) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 14 | 0 | — | — | 0 | [30m22s](https://github.com/iree-org/iree/actions/runs/26258672591/job/77288096873) | [1h42m](https://github.com/iree-org/iree/actions/runs/26246079836/job/77245860258) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 28 | 0 | — | — | 0 | [23m57s](https://github.com/iree-org/iree/actions/runs/26246079998/job/77246020149) | [1h38m](https://github.com/iree-org/iree/actions/runs/26242793965/job/77247540872) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 28 | 0 | — | — | 0 | [13m46s](https://github.com/iree-org/iree/actions/runs/26240827394/job/77227846933) | [1h33m](https://github.com/iree-org/iree/actions/runs/26242793965/job/77247541210) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 15 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926441) | 2026-05-19 06:28 PDT | 0 | [10m41s](https://github.com/iree-org/iree/actions/runs/26240588555/job/77226962737) | [1h27m](https://github.com/iree-org/iree/actions/runs/26246874148/job/77249069781) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 14 | 0 | — | — | 0 | [28m04s](https://github.com/iree-org/iree/actions/runs/26228441233/job/77221057161) | [1h27m](https://github.com/iree-org/iree/actions/runs/26246079836/job/77245860177) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `azure-windows-scale` | ossci | 16 | 0 | — | — | 1 | [3m22s](https://github.com/iree-org/iree/actions/runs/26246079412/job/77244707241) | [1h23m](https://github.com/iree-org/iree/actions/runs/26240827522/job/77227094166) | 100% (1/1) | 15 |
| `Linux,X64,iree-r9700` | self-hosted | 15 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926511) | 2026-05-19 06:28 PDT | 0 | [9m40s](https://github.com/iree-org/iree/actions/runs/26258840912/job/77288939807) | [1h20m](https://github.com/iree-org/iree/actions/runs/26246079367/job/77246047081) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 28 | 0 | — | — | 0 | [7m44s](https://github.com/iree-org/iree/actions/runs/26237184723/job/77215975224) | [1h08m](https://github.com/iree-org/iree/actions/runs/26242793965/job/77247540893) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 14 | 0 | — | — | 0 | [4m59s](https://github.com/iree-org/iree/actions/runs/26246079836/job/77245861147) | [1h03m](https://github.com/iree-org/iree/actions/runs/26242793965/job/77247540934) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 14 | 0 | — | — | 0 | [3m10s](https://github.com/iree-org/iree/actions/runs/26258840912/job/77288940020) | [12m51s](https://github.com/iree-org/iree/actions/runs/26246874148/job/77249070102) | 0% (0/1) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 56 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/26237184723/job/77215975384) | [8m08s](https://github.com/iree-org/iree/actions/runs/26246079998/job/77246019962) | 0% (0/4) | 56 |
| `windows-2022` | github-hosted | 48 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/26258840909/job/77287598697) | [4m10s](https://github.com/iree-org/iree/actions/runs/26242793963/job/77246929584) | 0% (0/3) | 45 |
| `macos-14` | github-hosted | 48 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26258672613/job/77287319081) | [4m09s](https://github.com/iree-org/iree/actions/runs/26246874213/job/77247738556) | 0% (0/3) | 45 |
| `ubuntu-24.04-arm` | github-hosted | 48 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26240827522/job/77227093963) | [4m00s](https://github.com/iree-org/iree/actions/runs/26246079412/job/77244706991) | 0% (0/3) | 45 |
| `ubuntu-24.04` | github-hosted | 315 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26237184724/job/77214564134) | [3m44s](https://github.com/iree-org/iree/actions/runs/26246079367/job/77246047238) | 6% (1/18) | 299 |
| `azure-linux-scale` | ossci | 81 | 1 | [10m39s](https://github.com/iree-org/iree/actions/runs/26212319110/job/77181582238) | 2026-05-21 06:27 PDT | 1 | [9s](https://github.com/iree-org/iree/actions/runs/26246080006/job/77244692895) | [1m51s](https://github.com/iree-org/iree/actions/runs/26239628202/job/77222213458) | 0% (0/6) | 77 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 14 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26239628064/job/77223559392) | [15s](https://github.com/iree-org/iree/actions/runs/26228441233/job/77221057133) | 0% (0/1) | 14 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26246076678/job/77244652692) | [4s](https://github.com/iree-org/iree/actions/runs/26240587533/job/77225551806) | 0% (0/3) | 6 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926441) | 2026-05-19 06:28 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `new-lds-promotion` | pull_request |
| [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926511) | 2026-05-19 06:28 PDT | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `new-lds-promotion` | pull_request |
| [10m39s](https://github.com/iree-org/iree/actions/runs/26212319110/job/77181582238) | 2026-05-21 06:27 PDT | `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | `promote-contraction-outputs` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 14 | 0 | — | — | [41m43s](https://github.com/iree-org/iree/actions/runs/26240588555/job/77226962839) | [2h41m](https://github.com/iree-org/iree/actions/runs/26246079836/job/77245860333) | [2h41m](https://github.com/iree-org/iree/actions/runs/26246079836/job/77245860333) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 14 | 0 | — | — | [26m20s](https://github.com/iree-org/iree/actions/runs/26240588555/job/77226962754) | [2h39m](https://github.com/iree-org/iree/actions/runs/26242793965/job/77247540920) | [2h42m](https://github.com/iree-org/iree/actions/runs/26246874148/job/77249070003) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 14 | 0 | — | — | [45m53s](https://github.com/iree-org/iree/actions/runs/26240827394/job/77227846560) | [2h17m](https://github.com/iree-org/iree/actions/runs/26242793965/job/77247541064) | [2h19m](https://github.com/iree-org/iree/actions/runs/26246079367/job/77246047242) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 14 | 0 | — | — | [34m35s](https://github.com/iree-org/iree/actions/runs/26238648585/job/77220351846) | [1h58m](https://github.com/iree-org/iree/actions/runs/26246079367/job/77246047231) | [2h00m](https://github.com/iree-org/iree/actions/runs/26242793965/job/77247540927) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 14 | 0 | — | — | [30m22s](https://github.com/iree-org/iree/actions/runs/26258672591/job/77288096873) | [1h42m](https://github.com/iree-org/iree/actions/runs/26246079836/job/77245860258) | [1h45m](https://github.com/iree-org/iree/actions/runs/26246874148/job/77249069894) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 14 | 0 | — | — | [24m28s](https://github.com/iree-org/iree/actions/runs/26258672591/job/77288096958) | [1h38m](https://github.com/iree-org/iree/actions/runs/26242793965/job/77247540872) | [1h49m](https://github.com/iree-org/iree/actions/runs/26246079836/job/77245860254) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 15 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926441) | 2026-05-19 06:28 PDT | [10m41s](https://github.com/iree-org/iree/actions/runs/26240588555/job/77226962737) | [1h27m](https://github.com/iree-org/iree/actions/runs/26246874148/job/77249069781) | [1h45m](https://github.com/iree-org/iree/actions/runs/26242793965/job/77247540773) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 14 | 0 | — | — | [10m32s](https://github.com/iree-org/iree/actions/runs/26239628064/job/77223559668) | [1h27m](https://github.com/iree-org/iree/actions/runs/26246079367/job/77246047241) | [1h33m](https://github.com/iree-org/iree/actions/runs/26246079836/job/77245860256) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 14 | 0 | — | — | [28m04s](https://github.com/iree-org/iree/actions/runs/26228441233/job/77221057161) | [1h27m](https://github.com/iree-org/iree/actions/runs/26246079836/job/77245860177) | [1h36m](https://github.com/iree-org/iree/actions/runs/26246079367/job/77246047253) | 2 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 16 | 0 | — | — | [3m22s](https://github.com/iree-org/iree/actions/runs/26246079412/job/77244707241) | [1h23m](https://github.com/iree-org/iree/actions/runs/26240827522/job/77227094166) | [1h25m](https://github.com/iree-org/iree/actions/runs/26240588557/job/77225592055) | 15 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 15 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926511) | 2026-05-19 06:28 PDT | [9m40s](https://github.com/iree-org/iree/actions/runs/26258840912/job/77288939807) | [1h20m](https://github.com/iree-org/iree/actions/runs/26246079367/job/77246047081) | [2h14m](https://github.com/iree-org/iree/actions/runs/26246874148/job/77249069669) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 14 | 0 | — | — | [20m14s](https://github.com/iree-org/iree/actions/runs/26246079998/job/77246019959) | [1h12m](https://github.com/iree-org/iree/actions/runs/26246079367/job/77246047276) | [1h33m](https://github.com/iree-org/iree/actions/runs/26242793965/job/77247541210) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 14 | 0 | — | — | [7m44s](https://github.com/iree-org/iree/actions/runs/26237184723/job/77215975224) | [1h08m](https://github.com/iree-org/iree/actions/runs/26242793965/job/77247540893) | [1h13m](https://github.com/iree-org/iree/actions/runs/26246079998/job/77246019766) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 14 | 0 | — | — | [4m59s](https://github.com/iree-org/iree/actions/runs/26246079836/job/77245861147) | [1h03m](https://github.com/iree-org/iree/actions/runs/26242793965/job/77247540934) | [1h17m](https://github.com/iree-org/iree/actions/runs/26246079998/job/77246019706) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 14 | 0 | — | — | [23m57s](https://github.com/iree-org/iree/actions/runs/26246079998/job/77246020149) | [1h01m](https://github.com/iree-org/iree/actions/runs/26246874148/job/77249070031) | [1h02m](https://github.com/iree-org/iree/actions/runs/26246079367/job/77246047306) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 14 | 0 | — | — | [6m42s](https://github.com/iree-org/iree/actions/runs/26238648585/job/77220351734) | [36m16s](https://github.com/iree-org/iree/actions/runs/26246874148/job/77249070015) | [40m23s](https://github.com/iree-org/iree/actions/runs/26258672591/job/77288096867) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 14 | 0 | — | — | [3m10s](https://github.com/iree-org/iree/actions/runs/26258840912/job/77288940020) | [12m51s](https://github.com/iree-org/iree/actions/runs/26246874148/job/77249070102) | [40m47s](https://github.com/iree-org/iree/actions/runs/26246079367/job/77246047294) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 17 | 1 | [10m39s](https://github.com/iree-org/iree/actions/runs/26212319110/job/77181582238) | 2026-05-21 06:27 PDT | [9s](https://github.com/iree-org/iree/actions/runs/26242793963/job/77246929740) | [1m04s](https://github.com/iree-org/iree/actions/runs/26238648581/job/77219237663) | [2m03s](https://github.com/iree-org/iree/actions/runs/26239628202/job/77222213434) | 15 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 14 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/26237184723/job/77215975384) | [8m08s](https://github.com/iree-org/iree/actions/runs/26246079998/job/77246019962) | [13m33s](https://github.com/iree-org/iree/actions/runs/26246079367/job/77246047282) | 14 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 14 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26258672591/job/77288096843) | [5m12s](https://github.com/iree-org/iree/actions/runs/26246079998/job/77246019691) | [7m14s](https://github.com/iree-org/iree/actions/runs/26246079367/job/77246047164) | 14 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 454 | 1% (6/453) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 386 | 6% (24/385) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 356 | 1% (5/355) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 356 | 1% (2/355) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 113 | 2% (2/113) |  | 1h34m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h03m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h38m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h17m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h41m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h27m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h27m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h58m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h33m (> 1h00m)
- **[queue-starved]** `azure-windows-scale` p95 queue 1h23m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h42m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h08m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
