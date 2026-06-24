# iree-ci-monitor

_Updated: 2026-06-23 18:15 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990378) | [10m53s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409923) | — | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [6m49s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990403) | [7m28s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409799) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [6m05s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409811) | [7m06s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990477) | — | `shark01-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [1m58s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409911) | [6m38s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990594) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990418) | [5m10s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409863) | — | `shark01-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [54s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409932) | [4m37s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990397) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2m52s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409871) | [3m49s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990387) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409560) | [3m49s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990392) | — | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [2m07s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990453) | [3m15s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409790) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [2m16s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990505) | [2m24s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409900) | — | `shark55-ci` |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/28054996758/job/83055009750) | [2m15s](https://github.com/iree-org/iree/actions/runs/28054997114/job/83055027273) | — | 6 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/28054996758/job/83055009911) | [2m10s](https://github.com/iree-org/iree/actions/runs/28054997114/job/83055027213) | — | 6 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 0 | [46s](https://github.com/iree-org/iree/actions/runs/28054996758/job/83055009758) | [2m08s](https://github.com/iree-org/iree/actions/runs/28054997114/job/83055027215) | — | 6 |
| `ubuntu-24.04` | github-hosted | 49 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28054996949/job/83054973944) | [2m04s](https://github.com/iree-org/iree/actions/runs/28054997114/job/83055027016) | 0% (0/2) | 47 |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409548) | [56s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990430) | — | `shark75-ci` |
| `azure-linux-scale` | ossci | 10 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/28054996758/job/83055009757) | [9s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83055011930) | — | 10 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990509) | [9s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409847) | — | 8 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28054996758/job/83055009995) | [3s](https://github.com/iree-org/iree/actions/runs/28054997114/job/83055027504) | — | 2 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28054993434/job/83054967169) | [3s](https://github.com/iree-org/iree/actions/runs/28054993434/job/83054966967) | — | 3 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409865) | [2s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990452) | — | `iree-mi308-1` |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 6 | [18h02m](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330192) | 2026-06-23 18:15 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [18h02m](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330192) | 2026-06-23 18:15 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [16h46m](https://github.com/iree-org/iree/actions/runs/28012486060/job/82910438192) | 2026-06-23 18:15 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `devtbi/tduf` | pull_request |
| [13h38m](https://github.com/iree-org/iree/actions/runs/28021790375/job/82944814860) | 2026-06-23 18:15 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `integrates/llvm-20260623` | pull_request |
| [9h59m](https://github.com/iree-org/iree/actions/runs/28034874087/job/82990257221) | 2026-06-23 18:15 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |
| [4h37m](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409541) | 2026-06-23 18:15 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/bjacob/cpu-ukernel-pipeline-test` | pull_request |
| [4h24m](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990411) | 2026-06-23 18:15 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `users/bjacob/cpu-ukernel-bodies` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 6 | 6 | [18h02m](https://github.com/iree-org/iree/actions/runs/28008559490/job/82897330192) | 2026-06-23 18:15 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990378) | [10m53s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409923) | [10m53s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409923) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [6m49s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990403) | [7m28s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409799) | [7m28s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409799) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [6m05s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409811) | [7m06s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990477) | [7m06s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990477) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [1m58s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409911) | [6m38s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990594) | [6m38s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990594) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [1m15s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990383) | [5m34s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409884) | [5m34s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409884) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [4m23s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409817) | [5m29s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990515) | [5m29s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990515) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990418) | [5m10s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409863) | [5m10s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409863) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [54s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409932) | [4m37s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990397) | [4m37s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990397) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409560) | [3m49s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990392) | [3m49s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990392) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [2m52s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409871) | [3m49s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990387) | [3m49s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990387) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [2m07s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990453) | [3m15s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409790) | [3m15s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409790) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [2m16s](https://github.com/iree-org/iree/actions/runs/28054997071/job/83058990505) | [2m24s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409900) | [2m24s](https://github.com/iree-org/iree/actions/runs/28054996720/job/83056409900) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 2 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28054996758/job/83055009750) | [2m15s](https://github.com/iree-org/iree/actions/runs/28054997114/job/83055027273) | [2m15s](https://github.com/iree-org/iree/actions/runs/28054997114/job/83055027273) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 2 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28054996758/job/83055009746) | [2m12s](https://github.com/iree-org/iree/actions/runs/28054997114/job/83055027195) | [2m12s](https://github.com/iree-org/iree/actions/runs/28054997114/job/83055027195) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 2 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/28054996758/job/83055009911) | [2m10s](https://github.com/iree-org/iree/actions/runs/28054997114/job/83055027213) | [2m10s](https://github.com/iree-org/iree/actions/runs/28054997114/job/83055027213) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 2 | 0 | — | — | [46s](https://github.com/iree-org/iree/actions/runs/28054996758/job/83055009758) | [2m08s](https://github.com/iree-org/iree/actions/runs/28054997114/job/83055027215) | [2m08s](https://github.com/iree-org/iree/actions/runs/28054997114/job/83055027215) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 2 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28054996758/job/83055009760) | [2m08s](https://github.com/iree-org/iree/actions/runs/28054997114/job/83055027201) | [2m08s](https://github.com/iree-org/iree/actions/runs/28054997114/job/83055027201) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28054996758/job/83055009730) | [2m08s](https://github.com/iree-org/iree/actions/runs/28054997114/job/83055027177) | [2m08s](https://github.com/iree-org/iree/actions/runs/28054997114/job/83055027177) | 2 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/28054996758/job/83055009546) | [2m04s](https://github.com/iree-org/iree/actions/runs/28054997114/job/83055027016) | [2m04s](https://github.com/iree-org/iree/actions/runs/28054997114/job/83055027016) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 130 | 0% (0/130) |  | 4h10m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 89 | 0% (0/89) |  | 4h11m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 102 | 0% (0/102) |  | 4h12m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 29 | 0% (0/29) |  | 4h14m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 103 | 3% (3/103) |  | 4h17m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 18h02m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
