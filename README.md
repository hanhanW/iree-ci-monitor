# iree-ci-monitor

_Updated: 2026-11-12 12:01 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 16 | 0 | — | — | 0 | [1h48m](https://github.com/iree-org/iree/actions/runs/43251411762/job/131302757046) | [4h50m](https://github.com/iree-org/iree/actions/runs/43237498220/job/131253983082) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 16 | 5 | [4h05m](https://github.com/iree-org/iree/actions/runs/43251411762/job/131302756496) | 2026-11-12 11:59 PST | 0 | [1h47m](https://github.com/iree-org/iree/actions/runs/43258466893/job/131337706998) | [4h44m](https://github.com/iree-org/iree/actions/runs/43237498220/job/131253982949) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 32 | 16 | [5h45m](https://github.com/iree-org/iree/actions/runs/43233560835/job/131240491298) | 2026-11-12 11:59 PST | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/43261548327/job/131346738837) | [4h12m](https://github.com/iree-org/iree/actions/runs/43237498220/job/131253983367) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 32 | 21 | [5h45m](https://github.com/iree-org/iree/actions/runs/43233560835/job/131240492109) | 2026-11-12 11:59 PST | 0 | [1h40m](https://github.com/iree-org/iree/actions/runs/43255594461/job/131322762821) | [3h51m](https://github.com/iree-org/iree/actions/runs/43249665616/job/131297764505) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 16 | 3 | [3h11m](https://github.com/iree-org/iree/actions/runs/43258543310/job/131337896694) | 2026-11-12 11:59 PST | 0 | [1h54m](https://github.com/iree-org/iree/actions/runs/43251411762/job/131302757049) | [3h51m](https://github.com/iree-org/iree/actions/runs/43233560835/job/131240491596) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 32 | 20 | [5h45m](https://github.com/iree-org/iree/actions/runs/43233560835/job/131240491357) | 2026-11-12 11:59 PST | 1 | [1h30m](https://github.com/iree-org/iree/actions/runs/43249665616/job/131297765021) | [3h35m](https://github.com/iree-org/iree/actions/runs/43255610511/job/131322583897) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 32 | 0 | — | — | 0 | [1h29m](https://github.com/iree-org/iree/actions/runs/43255594461/job/131322762238) | [2h05m](https://github.com/iree-org/iree/actions/runs/43261531152/job/131342127664) | 0% (0/6) | `shark55-ci`, `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 359 | 0 | — | — | 3 | [3m06s](https://github.com/iree-org/iree/actions/runs/43227558024/job/131214707288) | [19m22s](https://github.com/iree-org/iree/actions/runs/43261531134/job/131342746416) | 0% (0/57) | 342 |
| `azure-windows-scale` | ossci | 18 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/43257707282/job/131323364957) | [8m19s](https://github.com/iree-org/iree/actions/runs/43255610498/job/131313022774) | 0% (0/3) | 18 |
| `macos-15` | github-hosted | 56 | 0 | — | — | 0 | [1m51s](https://github.com/iree-org/iree/actions/runs/43255596104/job/131312971732) | [7m37s](https://github.com/iree-org/iree/actions/runs/43261531134/job/131342746584) | 0% (0/9) | 56 |
| `ubuntu-24.04-arm` | github-hosted | 54 | 0 | — | — | 0 | [1m43s](https://github.com/iree-org/iree/actions/runs/43233560865/job/131234986162) | [7m24s](https://github.com/iree-org/iree/actions/runs/43255610498/job/131313022365) | 0% (0/9) | 53 |
| `windows-2022` | github-hosted | 54 | 0 | — | — | 0 | [2m00s](https://github.com/iree-org/iree/actions/runs/43257707282/job/131323364286) | [7m20s](https://github.com/iree-org/iree/actions/runs/43255610498/job/131313022375) | 0% (0/9) | 53 |
| `ubuntu-latest` | github-hosted | 45 | 0 | — | — | 0 | [15s](https://github.com/iree-org/iree/actions/runs/43258450541/job/131322939337) | [6m49s](https://github.com/iree-org/iree/actions/runs/43256230367/job/131315092878) | 0% (0/9) | 45 |
| `azure-linux-scale` | ossci | 115 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/43260697495/job/131337963557) | [3m54s](https://github.com/iree-org/iree/actions/runs/43255604134/job/131313050387) | 0% (0/21) | 114 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 2 | 0 | — | — | 0 | [1m24s](https://github.com/iree-org/iree/actions/runs/43257707282/job/131323366114) | [1m38s](https://github.com/iree-org/iree/actions/runs/43255600247/job/131312993265) | — | 2 |
| `Linux,X64,iree-w7900` | self-hosted | 15 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [5h45m](https://github.com/iree-org/iree/actions/runs/43233560835/job/131240491298) | 2026-11-12 11:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |
| [5h45m](https://github.com/iree-org/iree/actions/runs/43233560835/job/131240491357) | 2026-11-12 11:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [5h45m](https://github.com/iree-org/iree/actions/runs/43233560835/job/131240491630) | 2026-11-12 11:59 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [5h45m](https://github.com/iree-org/iree/actions/runs/43233560835/job/131240492109) | 2026-11-12 11:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [5h22m](https://github.com/iree-org/iree/actions/runs/43237498220/job/131253983145) | 2026-11-12 11:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |
| [5h22m](https://github.com/iree-org/iree/actions/runs/43237498220/job/131253983212) | 2026-11-12 11:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [5h22m](https://github.com/iree-org/iree/actions/runs/43237498220/job/131253983297) | 2026-11-12 11:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [5h22m](https://github.com/iree-org/iree/actions/runs/43237498220/job/131253983370) | 2026-11-12 11:59 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [5h22m](https://github.com/iree-org/iree/actions/runs/43237498220/job/131253983406) | 2026-11-12 11:59 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [4h13m](https://github.com/iree-org/iree/actions/runs/43249665616/job/131297764375) | 2026-11-12 11:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `perf-torch-python-dialect-registration` | pull_request |
| [4h13m](https://github.com/iree-org/iree/actions/runs/43249665616/job/131297765125) | 2026-11-12 11:59 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `perf-torch-python-dialect-registration` | pull_request |
| [4h05m](https://github.com/iree-org/iree/actions/runs/43251411762/job/131302756496) | 2026-11-12 11:59 PST | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `compiler-python-invocation-phases` | pull_request |
| [4h05m](https://github.com/iree-org/iree/actions/runs/43251411762/job/131302756707) | 2026-11-12 11:59 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `compiler-python-invocation-phases` | pull_request |
| [4h05m](https://github.com/iree-org/iree/actions/runs/43251411762/job/131302756828) | 2026-11-12 11:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `compiler-python-invocation-phases` | pull_request |
| [4h05m](https://github.com/iree-org/iree/actions/runs/43251411762/job/131302756928) | 2026-11-12 11:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `compiler-python-invocation-phases` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 16 | 12 | [5h45m](https://github.com/iree-org/iree/actions/runs/43233560835/job/131240492109) | 2026-11-12 11:59 PST | [1h30m](https://github.com/iree-org/iree/actions/runs/43255610511/job/131322583720) | [3h51m](https://github.com/iree-org/iree/actions/runs/43249665616/job/131297764505) | [3h51m](https://github.com/iree-org/iree/actions/runs/43249665616/job/131297764505) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 16 | 11 | [5h45m](https://github.com/iree-org/iree/actions/runs/43233560835/job/131240491357) | 2026-11-12 11:59 PST | [1h18m](https://github.com/iree-org/iree/actions/runs/43227558155/job/131219255600) | [2h41m](https://github.com/iree-org/iree/actions/runs/43255594461/job/131322762362) | [2h41m](https://github.com/iree-org/iree/actions/runs/43255594461/job/131322762362) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 16 | 9 | [5h45m](https://github.com/iree-org/iree/actions/runs/43233560835/job/131240491298) | 2026-11-12 11:59 PST | [2h14m](https://github.com/iree-org/iree/actions/runs/43258543310/job/131337896991) | [4h13m](https://github.com/iree-org/iree/actions/runs/43249665616/job/131297764382) | [4h13m](https://github.com/iree-org/iree/actions/runs/43249665616/job/131297764382) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 16 | 9 | [5h45m](https://github.com/iree-org/iree/actions/runs/43233560835/job/131240491630) | 2026-11-12 11:59 PST | [1h31m](https://github.com/iree-org/iree/actions/runs/43251411762/job/131302757345) | [3h35m](https://github.com/iree-org/iree/actions/runs/43255610511/job/131322583897) | [3h35m](https://github.com/iree-org/iree/actions/runs/43255610511/job/131322583897) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 16 | 9 | [5h22m](https://github.com/iree-org/iree/actions/runs/43237498220/job/131253983406) | 2026-11-12 11:59 PST | [1h40m](https://github.com/iree-org/iree/actions/runs/43255594461/job/131322762821) | [3h02m](https://github.com/iree-org/iree/actions/runs/43233560835/job/131240491619) | [3h02m](https://github.com/iree-org/iree/actions/runs/43233560835/job/131240491619) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 16 | 0 | — | — | [1h48m](https://github.com/iree-org/iree/actions/runs/43251411762/job/131302757046) | [4h50m](https://github.com/iree-org/iree/actions/runs/43237498220/job/131253983082) | [5h02m](https://github.com/iree-org/iree/actions/runs/43233560835/job/131240491433) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 16 | 5 | [4h05m](https://github.com/iree-org/iree/actions/runs/43251411762/job/131302756496) | 2026-11-12 11:59 PST | [1h47m](https://github.com/iree-org/iree/actions/runs/43258466893/job/131337706998) | [4h44m](https://github.com/iree-org/iree/actions/runs/43237498220/job/131253982949) | [4h44m](https://github.com/iree-org/iree/actions/runs/43237498220/job/131253982949) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 16 | 7 | [4h13m](https://github.com/iree-org/iree/actions/runs/43249665616/job/131297765125) | 2026-11-12 11:59 PST | [1h43m](https://github.com/iree-org/iree/actions/runs/43257708209/job/131326931442) | [4h12m](https://github.com/iree-org/iree/actions/runs/43237498220/job/131253983367) | [4h12m](https://github.com/iree-org/iree/actions/runs/43237498220/job/131253983367) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 16 | 3 | [3h11m](https://github.com/iree-org/iree/actions/runs/43258543310/job/131337896694) | 2026-11-12 11:59 PST | [1h54m](https://github.com/iree-org/iree/actions/runs/43251411762/job/131302757049) | [3h51m](https://github.com/iree-org/iree/actions/runs/43233560835/job/131240491596) | [4h00m](https://github.com/iree-org/iree/actions/runs/43237498220/job/131253983121) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 16 | 0 | — | — | [1h34m](https://github.com/iree-org/iree/actions/runs/43258543310/job/131337896015) | [1h57m](https://github.com/iree-org/iree/actions/runs/43227558155/job/131219251394) | [3h13m](https://github.com/iree-org/iree/actions/runs/43237498220/job/131253982860) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 16 | 0 | — | — | [1h29m](https://github.com/iree-org/iree/actions/runs/43255594461/job/131322762238) | [1h57m](https://github.com/iree-org/iree/actions/runs/43257708209/job/131326931573) | [2h05m](https://github.com/iree-org/iree/actions/runs/43261531152/job/131342127664) | 2 |
| `.github/workflows/clang_tidy.yml` | clang-tidy | `ubuntu-24.04` | 9 | 0 | — | — | [7m50s](https://github.com/iree-org/iree/actions/runs/43256240261/job/131315116381) | [31m00s](https://github.com/iree-org/iree/actions/runs/43258466631/job/131322980862) | [31m00s](https://github.com/iree-org/iree/actions/runs/43258466631/job/131322980862) | 7 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 18 | 0 | — | — | [6m33s](https://github.com/iree-org/iree/actions/runs/43255600247/job/131312992983) | [24m35s](https://github.com/iree-org/iree/actions/runs/43258466678/job/131334829415) | [40m20s](https://github.com/iree-org/iree/actions/runs/43257707282/job/131323364626) | 17 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 20 | 0 | — | — | [4m29s](https://github.com/iree-org/iree/actions/runs/43255596104/job/131312971560) | [24m06s](https://github.com/iree-org/iree/actions/runs/43258466678/job/131334828801) | [29m52s](https://github.com/iree-org/iree/actions/runs/43257707282/job/131323364099) | 17 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 18 | 0 | — | — | [4m39s](https://github.com/iree-org/iree/actions/runs/43255600247/job/131312992922) | [23m39s](https://github.com/iree-org/iree/actions/runs/43258543182/job/131330150104) | [38m06s](https://github.com/iree-org/iree/actions/runs/43257707282/job/131323364537) | 17 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 18 | 0 | — | — | [2m30s](https://github.com/iree-org/iree/actions/runs/43255596104/job/131312972369) | [19m01s](https://github.com/iree-org/iree/actions/runs/43261531134/job/131342746002) | [23m54s](https://github.com/iree-org/iree/actions/runs/43258466678/job/131334828973) | 17 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | 16 | 0 | — | — | [3m36s](https://github.com/iree-org/iree/actions/runs/43255594975/job/131319275071) | [16m25s](https://github.com/iree-org/iree/actions/runs/43258543310/job/131337896053) | [16m29s](https://github.com/iree-org/iree/actions/runs/43255594461/job/131322762863) | 16 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 16 | 0 | — | — | [6m44s](https://github.com/iree-org/iree/actions/runs/43261548327/job/131346738935) | [16m18s](https://github.com/iree-org/iree/actions/runs/43255610511/job/131322583678) | [16m28s](https://github.com/iree-org/iree/actions/runs/43258466893/job/131337707339) | 16 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 16 | 0 | — | — | [4m20s](https://github.com/iree-org/iree/actions/runs/43255594975/job/131319275215) | [16m00s](https://github.com/iree-org/iree/actions/runs/43255610511/job/131322583823) | [19m48s](https://github.com/iree-org/iree/actions/runs/43258466893/job/131337707305) | 16 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 20 | 0 | — | — | [4m48s](https://github.com/iree-org/iree/actions/runs/43255600247/job/131312992399) | [15m23s](https://github.com/iree-org/iree/actions/runs/43257707282/job/131323363925) | [21m20s](https://github.com/iree-org/iree/actions/runs/43261548689/job/131339632308) | 17 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 359 | 1% (2/358) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 317 | 1% (2/316) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 3h11m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 5h45m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 5h45m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job observed waiting 4h05m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 5h45m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 3h51m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 3h35m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 4h50m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 4h12m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 4h44m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 3h51m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h05m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
