# iree-ci-monitor

_Updated: 2026-09-24 10:16 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 14 | 0 | — | — | 0 | [2h19m](https://github.com/iree-org/iree/actions/runs/36005877143/job/107657432503) | [3h21m](https://github.com/iree-org/iree/actions/runs/36001194866/job/107646963550) | 0% (0/6) | `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [2h20m](https://github.com/iree-org/iree/actions/runs/36001194866/job/107646963535) | [3h19m](https://github.com/iree-org/iree/actions/runs/36005878026/job/107659184877) | 0% (0/3) | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [2h55m](https://github.com/iree-org/iree/actions/runs/36001194866/job/107646963569) | [3h12m](https://github.com/iree-org/iree/actions/runs/36005877143/job/107657432430) | 0% (0/3) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 14 | 0 | — | — | 0 | [44m36s](https://github.com/iree-org/iree/actions/runs/36005877199/job/107656583808) | [3h05m](https://github.com/iree-org/iree/actions/runs/36005877199/job/107656583997) | 0% (0/6) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 7 | 0 | — | — | 0 | [1h29m](https://github.com/iree-org/iree/actions/runs/36005878026/job/107659183546) | [2h58m](https://github.com/iree-org/iree/actions/runs/36001194866/job/107646963311) | 0% (0/3) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 14 | 0 | — | — | 0 | [1h06m](https://github.com/iree-org/iree/actions/runs/36005870059/job/107656700654) | [2h18m](https://github.com/iree-org/iree/actions/runs/36005870059/job/107656700984) | 0% (0/6) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 14 | 0 | — | — | 0 | [1h04m](https://github.com/iree-org/iree/actions/runs/36001194866/job/107646963924) | [2h18m](https://github.com/iree-org/iree/actions/runs/36005870059/job/107656700985) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [14m47s](https://github.com/iree-org/iree/actions/runs/36001194866/job/107646963461) | [53m47s](https://github.com/iree-org/iree/actions/runs/36005878026/job/107659183889) | 0% (0/3) | `shark75-ci` |
| `ubuntu-24.04` | github-hosted | 158 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/35977303077/job/107560761429) | [11m26s](https://github.com/iree-org/iree/actions/runs/36005877199/job/107656583911) | 0% (0/61) | 158 |
| `ubuntu-24.04-arm` | github-hosted | 24 | 0 | — | — | 0 | [42s](https://github.com/iree-org/iree/actions/runs/36005878020/job/107653896310) | [9m05s](https://github.com/iree-org/iree/actions/runs/36005877151/job/107654518240) | 0% (0/9) | 24 |
| `azure-windows-scale` | ossci | 8 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/36001194726/job/107638042719) | [8m57s](https://github.com/iree-org/iree/actions/runs/36005877151/job/107654518347) | 0% (0/3) | 8 |
| `macos-14` | github-hosted | 25 | 0 | — | — | 0 | [52s](https://github.com/iree-org/iree/actions/runs/36005869493/job/107653819799) | [7m16s](https://github.com/iree-org/iree/actions/runs/36005877151/job/107654518058) | 0% (0/10) | 25 |
| `windows-2022` | github-hosted | 24 | 0 | — | — | 3 | [28s](https://github.com/iree-org/iree/actions/runs/36005878020/job/107653896148) | [4m53s](https://github.com/iree-org/iree/actions/runs/36005877305/job/107654148717) | 0% (0/9) | 24 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m33s](https://github.com/iree-org/iree/actions/runs/35981379841/job/107573832148) | [1m33s](https://github.com/iree-org/iree/actions/runs/35981379841/job/107573832148) | 100% (1/1) | 1 |
| `azure-linux-scale` | ossci | 45 | 0 | — | — | 5 | [9s](https://github.com/iree-org/iree/actions/runs/36005869493/job/107653819721) | [1m28s](https://github.com/iree-org/iree/actions/runs/36001256429/job/107638475591) | 5% (1/20) | 45 |
| `ubuntu-latest` | github-hosted | 33 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/36001192192/job/107637976168) | [1m16s](https://github.com/iree-org/iree/actions/runs/36006513746/job/107656316647) | 0% (0/9) | 33 |
| `Linux,X64,iree-w7900` | self-hosted | 7 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 7 | 0 | — | — | [2h47m](https://github.com/iree-org/iree/actions/runs/36005877199/job/107656583914) | [3h29m](https://github.com/iree-org/iree/actions/runs/36005877143/job/107657432242) | [3h29m](https://github.com/iree-org/iree/actions/runs/36005877143/job/107657432242) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 7 | 0 | — | — | [44m36s](https://github.com/iree-org/iree/actions/runs/36005877199/job/107656583808) | [3h26m](https://github.com/iree-org/iree/actions/runs/36005870059/job/107656700947) | [3h26m](https://github.com/iree-org/iree/actions/runs/36005870059/job/107656700947) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 7 | 0 | — | — | [2h19m](https://github.com/iree-org/iree/actions/runs/36005877143/job/107657432503) | [3h21m](https://github.com/iree-org/iree/actions/runs/36001194866/job/107646963550) | [3h21m](https://github.com/iree-org/iree/actions/runs/36001194866/job/107646963550) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 7 | 0 | — | — | [2h20m](https://github.com/iree-org/iree/actions/runs/36001194866/job/107646963535) | [3h19m](https://github.com/iree-org/iree/actions/runs/36005878026/job/107659184877) | [3h19m](https://github.com/iree-org/iree/actions/runs/36005878026/job/107659184877) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 7 | 0 | — | — | [2h55m](https://github.com/iree-org/iree/actions/runs/36001194866/job/107646963569) | [3h12m](https://github.com/iree-org/iree/actions/runs/36005877143/job/107657432430) | [3h12m](https://github.com/iree-org/iree/actions/runs/36005877143/job/107657432430) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 7 | 0 | — | — | [1h39m](https://github.com/iree-org/iree/actions/runs/36005878026/job/107659183612) | [3h05m](https://github.com/iree-org/iree/actions/runs/36005877199/job/107656583997) | [3h05m](https://github.com/iree-org/iree/actions/runs/36005877199/job/107656583997) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 7 | 0 | — | — | [1h29m](https://github.com/iree-org/iree/actions/runs/36005878026/job/107659183546) | [2h58m](https://github.com/iree-org/iree/actions/runs/36001194866/job/107646963311) | [2h58m](https://github.com/iree-org/iree/actions/runs/36001194866/job/107646963311) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 7 | 0 | — | — | [1h22m](https://github.com/iree-org/iree/actions/runs/36005878026/job/107659183924) | [2h33m](https://github.com/iree-org/iree/actions/runs/36001194866/job/107646963399) | [2h33m](https://github.com/iree-org/iree/actions/runs/36001194866/job/107646963399) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 7 | 0 | — | — | [1h22m](https://github.com/iree-org/iree/actions/runs/36005870059/job/107656701057) | [2h30m](https://github.com/iree-org/iree/actions/runs/36005877199/job/107656583956) | [2h30m](https://github.com/iree-org/iree/actions/runs/36005877199/job/107656583956) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 7 | 0 | — | — | [1h04m](https://github.com/iree-org/iree/actions/runs/36001194866/job/107646963924) | [2h18m](https://github.com/iree-org/iree/actions/runs/36005870059/job/107656700985) | [2h18m](https://github.com/iree-org/iree/actions/runs/36005870059/job/107656700985) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 7 | 0 | — | — | [1h06m](https://github.com/iree-org/iree/actions/runs/36005870059/job/107656700654) | [1h36m](https://github.com/iree-org/iree/actions/runs/36005878026/job/107659183756) | [1h36m](https://github.com/iree-org/iree/actions/runs/36005878026/job/107659183756) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 7 | 0 | — | — | [14m47s](https://github.com/iree-org/iree/actions/runs/36001194866/job/107646963461) | [53m47s](https://github.com/iree-org/iree/actions/runs/36005878026/job/107659183889) | [53m47s](https://github.com/iree-org/iree/actions/runs/36005878026/job/107659183889) | 1 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 8 | 0 | — | — | [58s](https://github.com/iree-org/iree/actions/runs/36005869493/job/107653819325) | [17m32s](https://github.com/iree-org/iree/actions/runs/36005877305/job/107654147949) | [17m32s](https://github.com/iree-org/iree/actions/runs/36005877305/job/107654147949) | 8 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 8 | 0 | — | — | [3m07s](https://github.com/iree-org/iree/actions/runs/36005877305/job/107654147989) | [16m54s](https://github.com/iree-org/iree/actions/runs/36005869493/job/107653819697) | [16m54s](https://github.com/iree-org/iree/actions/runs/36005869493/job/107653819697) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 8 | 0 | — | — | [36s](https://github.com/iree-org/iree/actions/runs/36005878020/job/107653896182) | [16m52s](https://github.com/iree-org/iree/actions/runs/36005877305/job/107654148088) | [16m52s](https://github.com/iree-org/iree/actions/runs/36005877305/job/107654148088) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 8 | 0 | — | — | [2m58s](https://github.com/iree-org/iree/actions/runs/36005878020/job/107653896305) | [13m47s](https://github.com/iree-org/iree/actions/runs/36005869493/job/107653819561) | [13m47s](https://github.com/iree-org/iree/actions/runs/36005869493/job/107653819561) | 8 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 8 | 0 | — | — | [36s](https://github.com/iree-org/iree/actions/runs/36005878020/job/107653896129) | [12m42s](https://github.com/iree-org/iree/actions/runs/36005877151/job/107654517967) | [12m42s](https://github.com/iree-org/iree/actions/runs/36005877151/job/107654517967) | 8 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 7 | 0 | — | — | [1m52s](https://github.com/iree-org/iree/actions/runs/36005878026/job/107659183804) | [12m06s](https://github.com/iree-org/iree/actions/runs/36005870059/job/107656701236) | [12m06s](https://github.com/iree-org/iree/actions/runs/36005870059/job/107656701236) | 7 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 7 | 0 | — | — | [2m39s](https://github.com/iree-org/iree/actions/runs/36005878026/job/107659183845) | [11m39s](https://github.com/iree-org/iree/actions/runs/36005870059/job/107656701072) | [11m39s](https://github.com/iree-org/iree/actions/runs/36005870059/job/107656701072) | 7 |
| `.github/workflows/pkgci.yml` | Unit Test / Linux (x86_64) | `ubuntu-24.04` | 7 | 0 | — | — | [2m47s](https://github.com/iree-org/iree/actions/runs/36005878026/job/107659183478) | [11m26s](https://github.com/iree-org/iree/actions/runs/36005877199/job/107656583588) | [11m26s](https://github.com/iree-org/iree/actions/runs/36005877199/job/107656583588) | 7 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 394 | 1% (5/394) |  | 3m57s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 343 | 2% (8/343) |  | 57m04s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 75 | 0% (0/75) |  | 6d19h ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 3h12m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 3h21m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h18m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h58m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache` p95 queue 3h19m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 3h05m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h18m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-w7900` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
