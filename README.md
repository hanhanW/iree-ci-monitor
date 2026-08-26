# iree-ci-monitor

_Updated: 2026-08-25 19:00 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 28 | 0 | — | — | 0 | [39m28s](https://github.com/iree-org/iree/actions/runs/32877561907/job/97902695745) | [2h02m](https://github.com/iree-org/iree/actions/runs/32877563319/job/97902787639) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 14 | 0 | — | — | 0 | [11m10s](https://github.com/iree-org/iree/actions/runs/32869878602/job/97883908742) | [1h37m](https://github.com/iree-org/iree/actions/runs/32877563092/job/97902549927) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 28 | 0 | — | — | 0 | [17m30s](https://github.com/iree-org/iree/actions/runs/32877562396/job/97902340706) | [1h17m](https://github.com/iree-org/iree/actions/runs/32877563092/job/97902549902) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 28 | 0 | — | — | 0 | [38m47s](https://github.com/iree-org/iree/actions/runs/32877562090/job/97903251221) | [1h13m](https://github.com/iree-org/iree/actions/runs/32877563319/job/97902787601) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 14 | 0 | — | — | 0 | [7m43s](https://github.com/iree-org/iree/actions/runs/32877563092/job/97902549855) | [1h13m](https://github.com/iree-org/iree/actions/runs/32877561907/job/97902695625) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 14 | 0 | — | — | 0 | [41m23s](https://github.com/iree-org/iree/actions/runs/32877561907/job/97902695439) | [1h12m](https://github.com/iree-org/iree/actions/runs/32877563319/job/97902787383) | — | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 14 | 0 | — | — | 0 | [16m15s](https://github.com/iree-org/iree/actions/runs/32870061100/job/97877907766) | [1h11m](https://github.com/iree-org/iree/actions/runs/32877562090/job/97903251034) | — | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 14 | 0 | — | — | 0 | [28m54s](https://github.com/iree-org/iree/actions/runs/32877563092/job/97902549742) | [1h01m](https://github.com/iree-org/iree/actions/runs/32877562396/job/97902340672) | — | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 28 | 0 | — | — | 0 | [8m07s](https://github.com/iree-org/iree/actions/runs/32877562090/job/97903251198) | [58m58s](https://github.com/iree-org/iree/actions/runs/32877562396/job/97902340729) | — | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 14 | 0 | — | — | 0 | [12m09s](https://github.com/iree-org/iree/actions/runs/32877563319/job/97902787265) | [46m53s](https://github.com/iree-org/iree/actions/runs/32877561907/job/97902695809) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 14 | 0 | — | — | 0 | [8m13s](https://github.com/iree-org/iree/actions/runs/32870061100/job/97877907614) | [36m33s](https://github.com/iree-org/iree/actions/runs/32877563092/job/97902549725) | — | `shark01-ci`, `shark10-ci` |
| `ubuntu-24.04` | github-hosted | 413 | 0 | — | — | 0 | [40s](https://github.com/iree-org/iree/actions/runs/32875147107/job/97891178158) | [15m47s](https://github.com/iree-org/iree/actions/runs/32877562090/job/97903251317) | — | 330 |
| `ubuntu-24.04-arm` | github-hosted | 60 | 0 | — | — | 0 | [2m52s](https://github.com/iree-org/iree/actions/runs/32875149212/job/97892527456) | [12m50s](https://github.com/iree-org/iree/actions/runs/32873241973/job/97886145479) | — | 55 |
| `macos-14` | github-hosted | 60 | 0 | — | — | 0 | [2m08s](https://github.com/iree-org/iree/actions/runs/32873242048/job/97885122508) | [11m52s](https://github.com/iree-org/iree/actions/runs/32877562140/job/97900543716) | — | 55 |
| `windows-2022` | github-hosted | 60 | 0 | — | — | 0 | [2m23s](https://github.com/iree-org/iree/actions/runs/32873241973/job/97886145348) | [7m44s](https://github.com/iree-org/iree/actions/runs/32875147643/job/97894064764) | — | 56 |
| `azure-windows-scale` | ossci | 20 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/32877562119/job/97899703690) | [7m30s](https://github.com/iree-org/iree/actions/runs/32873243836/job/97887044844) | — | 20 |
| `azure-linux-scale` | ossci | 103 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/32875149212/job/97892527520) | [2m55s](https://github.com/iree-org/iree/actions/runs/32873242037/job/97886759588) | — | 102 |
| `ubuntu-cca-77785908-7ef3-498a-9ae0-bbebb95125d3` | github-hosted | 1 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/32914766325/job/98016071579) | [4s](https://github.com/iree-org/iree/actions/runs/32914766325/job/98016071579) | — | 1 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32869869077/job/97874021441) | [2s](https://github.com/iree-org/iree/actions/runs/32869869077/job/97874021492) | — | 3 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 14 | 0 | — | — | [39m28s](https://github.com/iree-org/iree/actions/runs/32877561907/job/97902695745) | [2h05m](https://github.com/iree-org/iree/actions/runs/32877562090/job/97903251335) | [2h05m](https://github.com/iree-org/iree/actions/runs/32877562090/job/97903251335) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 14 | 0 | — | — | [1h18m](https://github.com/iree-org/iree/actions/runs/32877562396/job/97902340705) | [1h52m](https://github.com/iree-org/iree/actions/runs/32877563092/job/97902549889) | [1h52m](https://github.com/iree-org/iree/actions/runs/32877563092/job/97902549889) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 14 | 0 | — | — | [11m10s](https://github.com/iree-org/iree/actions/runs/32869878602/job/97883908742) | [1h37m](https://github.com/iree-org/iree/actions/runs/32877563092/job/97902549927) | [1h37m](https://github.com/iree-org/iree/actions/runs/32877563092/job/97902549927) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 14 | 0 | — | — | [1h02m](https://github.com/iree-org/iree/actions/runs/32877562090/job/97903251218) | [1h17m](https://github.com/iree-org/iree/actions/runs/32877563319/job/97902787374) | [1h17m](https://github.com/iree-org/iree/actions/runs/32877563319/job/97902787374) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 14 | 0 | — | — | [7m44s](https://github.com/iree-org/iree/actions/runs/32869878602/job/97883908777) | [1h17m](https://github.com/iree-org/iree/actions/runs/32877563092/job/97902549902) | [1h17m](https://github.com/iree-org/iree/actions/runs/32877563092/job/97902549902) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 14 | 0 | — | — | [50m44s](https://github.com/iree-org/iree/actions/runs/32877562090/job/97903251343) | [1h15m](https://github.com/iree-org/iree/actions/runs/32877561907/job/97902695724) | [1h15m](https://github.com/iree-org/iree/actions/runs/32877561907/job/97902695724) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 14 | 0 | — | — | [7m43s](https://github.com/iree-org/iree/actions/runs/32877563092/job/97902549855) | [1h13m](https://github.com/iree-org/iree/actions/runs/32877561907/job/97902695625) | [1h13m](https://github.com/iree-org/iree/actions/runs/32877561907/job/97902695625) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 14 | 0 | — | — | [41m23s](https://github.com/iree-org/iree/actions/runs/32877561907/job/97902695439) | [1h12m](https://github.com/iree-org/iree/actions/runs/32877563319/job/97902787383) | [1h12m](https://github.com/iree-org/iree/actions/runs/32877563319/job/97902787383) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 14 | 0 | — | — | [16m15s](https://github.com/iree-org/iree/actions/runs/32870061100/job/97877907766) | [1h11m](https://github.com/iree-org/iree/actions/runs/32877562090/job/97903251034) | [1h11m](https://github.com/iree-org/iree/actions/runs/32877562090/job/97903251034) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 14 | 0 | — | — | [38m47s](https://github.com/iree-org/iree/actions/runs/32877562090/job/97903251221) | [1h10m](https://github.com/iree-org/iree/actions/runs/32877563092/job/97902549886) | [1h10m](https://github.com/iree-org/iree/actions/runs/32877563092/job/97902549886) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 14 | 0 | — | — | [28m54s](https://github.com/iree-org/iree/actions/runs/32877563092/job/97902549742) | [1h01m](https://github.com/iree-org/iree/actions/runs/32877562396/job/97902340672) | [1h01m](https://github.com/iree-org/iree/actions/runs/32877562396/job/97902340672) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 14 | 0 | — | — | [17m03s](https://github.com/iree-org/iree/actions/runs/32877563319/job/97902787231) | [1h00m](https://github.com/iree-org/iree/actions/runs/32877561907/job/97902695614) | [1h00m](https://github.com/iree-org/iree/actions/runs/32877561907/job/97902695614) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 14 | 0 | — | — | [8m07s](https://github.com/iree-org/iree/actions/runs/32877562090/job/97903251198) | [58m58s](https://github.com/iree-org/iree/actions/runs/32877562396/job/97902340729) | [58m58s](https://github.com/iree-org/iree/actions/runs/32877562396/job/97902340729) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 14 | 0 | — | — | [12m09s](https://github.com/iree-org/iree/actions/runs/32877563319/job/97902787265) | [46m53s](https://github.com/iree-org/iree/actions/runs/32877561907/job/97902695809) | [46m53s](https://github.com/iree-org/iree/actions/runs/32877561907/job/97902695809) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 14 | 0 | — | — | [8m13s](https://github.com/iree-org/iree/actions/runs/32870061100/job/97877907614) | [36m33s](https://github.com/iree-org/iree/actions/runs/32877563092/job/97902549725) | [36m33s](https://github.com/iree-org/iree/actions/runs/32877563092/job/97902549725) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | 14 | 0 | — | — | [8m21s](https://github.com/iree-org/iree/actions/runs/32875149036/job/97894374291) | [19m08s](https://github.com/iree-org/iree/actions/runs/32877563319/job/97902787643) | [19m08s](https://github.com/iree-org/iree/actions/runs/32877563319/job/97902787643) | 8 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 20 | 0 | — | — | [2m09s](https://github.com/iree-org/iree/actions/runs/32875149783/job/97892441983) | [18m38s](https://github.com/iree-org/iree/actions/runs/32877562119/job/97899703297) | [19m13s](https://github.com/iree-org/iree/actions/runs/32877562424/job/97899534364) | 16 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 14 | 0 | — | — | [5m17s](https://github.com/iree-org/iree/actions/runs/32875147564/job/97895083588) | [18m06s](https://github.com/iree-org/iree/actions/runs/32877563319/job/97902787707) | [18m06s](https://github.com/iree-org/iree/actions/runs/32877563319/job/97902787707) | 9 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 20 | 0 | — | — | [3m15s](https://github.com/iree-org/iree/actions/runs/32873242048/job/97885122346) | [17m26s](https://github.com/iree-org/iree/actions/runs/32877562877/job/97899499500) | [25m09s](https://github.com/iree-org/iree/actions/runs/32877562140/job/97900543615) | 15 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 14 | 0 | — | — | [3m16s](https://github.com/iree-org/iree/actions/runs/32875147564/job/97895083532) | [17m24s](https://github.com/iree-org/iree/actions/runs/32877562090/job/97903251126) | [17m24s](https://github.com/iree-org/iree/actions/runs/32877562090/job/97903251126) | 10 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 276 | 1% (4/275) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 193 | 0% (0/192) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 203 | 0% (0/202) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 244 | 3% (7/243) | yes | running |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h17m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h37m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h11m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h12m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h13m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h13m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `ubuntu-cca-77785908-7ef3-498a-9ae0-bbebb95125d3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
