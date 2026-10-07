# iree-ci-monitor

_Updated: 2026-10-07 16:10 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 12 | 1 | [3h50m](https://github.com/iree-org/iree/actions/runs/37672346147/job/112970953313) | 2026-10-07 16:08 PDT | 1 | [8h00m](https://github.com/iree-org/iree/actions/runs/37626670551/job/112829842836) | [9h39m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706816) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 6 | 1 | [3h50m](https://github.com/iree-org/iree/actions/runs/37672346147/job/112970953310) | 2026-10-07 16:08 PDT | 0 | [6h06m](https://github.com/iree-org/iree/actions/runs/37626670551/job/112829842417) | [9h24m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706065) | 100% (1/1) | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 1 | [9h13m](https://github.com/iree-org/iree/actions/runs/37626670551/job/112829842225) | 2026-10-07 16:08 PDT | 0 | [9h06m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706131) | [9h09m](https://github.com/iree-org/iree/actions/runs/37624995356/job/112812640223) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 1 | [3h50m](https://github.com/iree-org/iree/actions/runs/37672346147/job/112970953440) | 2026-10-07 16:08 PDT | 0 | [5h46m](https://github.com/iree-org/iree/actions/runs/37626670551/job/112829842310) | [9h03m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812707092) | 0% (0/3) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [4h51m](https://github.com/iree-org/iree/actions/runs/37652560562/job/112909148272) | [8h39m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706666) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 2 | [9h50m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706240) | 2026-10-07 16:08 PDT | 0 | [6h06m](https://github.com/iree-org/iree/actions/runs/37652560562/job/112909148560) | [8h37m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706512) | 0% (0/2) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [4h09m](https://github.com/iree-org/iree/actions/runs/37626670551/job/112829842325) | [7h49m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706435) | 0% (0/4) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [5h32m](https://github.com/iree-org/iree/actions/runs/37626670551/job/112829842278) | [7h49m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706180) | 0% (0/2) | `shark55-ci` |
| `ubuntu-24.04` | github-hosted | 123 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/37556930700/job/113031408923) | [6m10s](https://github.com/iree-org/iree/actions/runs/37626670352/job/112811962460) | 18% (6/34) | 121 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/37652560827/job/112899482536) | [4m12s](https://github.com/iree-org/iree/actions/runs/37626670352/job/112811962510) | — | 6 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/37672345266/job/112967024663) | [3m20s](https://github.com/iree-org/iree/actions/runs/37626663455/job/112810075078) | 0% (0/3) | 9 |
| `windows-2022` | github-hosted | 12 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/37672346230/job/112967102251) | [2m24s](https://github.com/iree-org/iree/actions/runs/37624995196/job/112809218601) | 0% (0/3) | 12 |
| `azure-linux-scale` | ossci | 25 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/37672346230/job/112967102537) | [2m19s](https://github.com/iree-org/iree/actions/runs/37626670352/job/112811962781) | 0% (0/7) | 25 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [28s](https://github.com/iree-org/iree/actions/runs/37624995196/job/112809218516) | [1m58s](https://github.com/iree-org/iree/actions/runs/37626670352/job/112811962303) | 0% (0/3) | 12 |
| `macos-15` | github-hosted | 7 | 0 | — | — | 0 | [44s](https://github.com/iree-org/iree/actions/runs/37624995196/job/112809218704) | [1m53s](https://github.com/iree-org/iree/actions/runs/37624995196/job/112809218509) | 0% (0/3) | 7 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37652560827/job/112899483179) | [3s](https://github.com/iree-org/iree/actions/runs/37672346230/job/112967102504) | 0% (0/1) | 4 |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [9h50m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706240) | 2026-10-07 16:08 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [9h13m](https://github.com/iree-org/iree/actions/runs/37626670551/job/112829842225) | 2026-10-07 16:08 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `users/roberto-laudani/qdq-per-channel-group` | pull_request |
| [3h50m](https://github.com/iree-org/iree/actions/runs/37672346147/job/112970953310) | 2026-10-07 16:08 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `main` | push |
| [3h50m](https://github.com/iree-org/iree/actions/runs/37672346147/job/112970953313) | 2026-10-07 16:08 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [3h50m](https://github.com/iree-org/iree/actions/runs/37672346147/job/112970953440) | 2026-10-07 16:08 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [3h50m](https://github.com/iree-org/iree/actions/runs/37672346147/job/112970953468) | 2026-10-07 16:08 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 2 | [9h50m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706240) | 2026-10-07 16:08 PDT | [6h06m](https://github.com/iree-org/iree/actions/runs/37652560562/job/112909148560) | [7h02m](https://github.com/iree-org/iree/actions/runs/37624995356/job/112812640264) | [7h02m](https://github.com/iree-org/iree/actions/runs/37624995356/job/112812640264) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 1 | [3h50m](https://github.com/iree-org/iree/actions/runs/37672346147/job/112970953313) | 2026-10-07 16:08 PDT | [8h37m](https://github.com/iree-org/iree/actions/runs/37624995356/job/112812640260) | [9h39m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706816) | [9h39m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706816) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 6 | 1 | [3h50m](https://github.com/iree-org/iree/actions/runs/37672346147/job/112970953310) | 2026-10-07 16:08 PDT | [6h06m](https://github.com/iree-org/iree/actions/runs/37626670551/job/112829842417) | [9h24m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706065) | [9h24m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706065) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 1 | [9h13m](https://github.com/iree-org/iree/actions/runs/37626670551/job/112829842225) | 2026-10-07 16:08 PDT | [9h06m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706131) | [9h09m](https://github.com/iree-org/iree/actions/runs/37624995356/job/112812640223) | [9h09m](https://github.com/iree-org/iree/actions/runs/37624995356/job/112812640223) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [5h13m](https://github.com/iree-org/iree/actions/runs/37626670551/job/112829842713) | [9h03m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812707092) | [9h03m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812707092) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [6h48m](https://github.com/iree-org/iree/actions/runs/37626670551/job/112829842232) | [8h58m](https://github.com/iree-org/iree/actions/runs/37624995356/job/112812640336) | [8h58m](https://github.com/iree-org/iree/actions/runs/37624995356/job/112812640336) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 1 | [3h50m](https://github.com/iree-org/iree/actions/runs/37672346147/job/112970953440) | 2026-10-07 16:08 PDT | [7h51m](https://github.com/iree-org/iree/actions/runs/37624995356/job/112812640208) | [8h49m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706174) | [8h49m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706174) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [4h51m](https://github.com/iree-org/iree/actions/runs/37652560562/job/112909148272) | [8h39m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706666) | [8h39m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706666) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [6h03m](https://github.com/iree-org/iree/actions/runs/37626670551/job/112829842856) | [8h37m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706512) | [8h37m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706512) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [4h09m](https://github.com/iree-org/iree/actions/runs/37626670551/job/112829842325) | [7h49m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706435) | [7h49m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706435) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [5h32m](https://github.com/iree-org/iree/actions/runs/37626670551/job/112829842278) | [7h49m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706180) | [7h49m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706180) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [4h30m](https://github.com/iree-org/iree/actions/runs/37626670551/job/112829842677) | [7h18m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706036) | [7h18m](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706036) | 2 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37652560562/job/112909148237) | [6m40s](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706227) | [6m40s](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706227) | 6 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 4 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37672346230/job/112967102235) | [6m40s](https://github.com/iree-org/iree/actions/runs/37626670352/job/112811962520) | [6m40s](https://github.com/iree-org/iree/actions/runs/37626670352/job/112811962520) | 4 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37672346147/job/112970953159) | [6m32s](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706228) | [6m32s](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706228) | 6 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37652560562/job/112909148607) | [6m16s](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706613) | [6m16s](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706613) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 4 | 0 | — | — | [3m28s](https://github.com/iree-org/iree/actions/runs/37624995196/job/112809218557) | [6m15s](https://github.com/iree-org/iree/actions/runs/37626670352/job/112811962533) | [6m15s](https://github.com/iree-org/iree/actions/runs/37626670352/job/112811962533) | 4 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37672346147/job/112970953516) | [6m10s](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706437) | [6m10s](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812706437) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37672346230/job/112967102347) | [6m10s](https://github.com/iree-org/iree/actions/runs/37626670352/job/112811962460) | [6m10s](https://github.com/iree-org/iree/actions/runs/37626670352/job/112811962460) | 4 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64-baremetal | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37652560562/job/112909148473) | [6m04s](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812705835) | [6m04s](https://github.com/iree-org/iree/actions/runs/37625351063/job/112812705835) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 408 | 0% (1/407) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 179 | 7% (13/179) |  | 2m22s ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 9h50m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job observed waiting 9h13m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 3h50m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 3h50m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 3h50m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 7h49m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 8h37m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 9h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 9h39m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 8h39m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache` p95 queue 9h24m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 9h03m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 7h49m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
