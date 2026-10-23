# iree-ci-monitor

_Updated: 2026-10-23 04:46 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 8 | 1 | [46m27s](https://github.com/iree-org/iree/actions/runs/39941335491/job/120378155221) | 2026-10-23 04:44 PDT | 1 | [1h20m](https://github.com/iree-org/iree/actions/runs/39936624863/job/120360472890) | [1h30m](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395320) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 16 | 2 | [1h28m](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066974) | 2026-10-23 04:44 PDT | 0 | [50m18s](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395419) | [1h14m](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395434) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 16 | 2 | [46m27s](https://github.com/iree-org/iree/actions/runs/39941335491/job/120378155197) | 2026-10-23 04:44 PDT | 0 | [29m29s](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692549) | [1h11m](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066818) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 16 | 0 | — | — | 0 | [26m28s](https://github.com/iree-org/iree/actions/runs/39936624863/job/120360472859) | [43m16s](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692267) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [26m35s](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395226) | [37m54s](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692107) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 8 | 0 | — | — | 0 | [20m20s](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395459) | [36m28s](https://github.com/iree-org/iree/actions/runs/39941335491/job/120378155092) | 0% (0/3) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 16 | 0 | — | — | 0 | [11m44s](https://github.com/iree-org/iree/actions/runs/39936624863/job/120360472861) | [21m27s](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066891) | 0% (0/6) | `shark55-ci`, `shark75-ci` |
| `windows-2022` | github-hosted | 32 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39941335495/job/120373285320) | [3m20s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882050) | 0% (0/9) | 32 |
| `ubuntu-24.04-arm` | github-hosted | 33 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/39924669265/job/120318404010) | [2m32s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882212) | 0% (0/9) | 33 |
| `macos-15` | github-hosted | 33 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/39936624895/job/120357712483) | [2m15s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882178) | 0% (0/9) | 33 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m47s](https://github.com/iree-org/iree/actions/runs/39932128255/job/120342726602) | [1m47s](https://github.com/iree-org/iree/actions/runs/39932128255/job/120342726602) | 100% (1/1) | 1 |
| `azure-linux-scale` | ossci | 65 | 0 | — | — | 1 | [9s](https://github.com/iree-org/iree/actions/runs/39928692461/job/120331437357) | [1m28s](https://github.com/iree-org/iree/actions/runs/39936937234/job/120358733005) | 4% (1/23) | 65 |
| `ubuntu-24.04` | github-hosted | 217 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/39936624895/job/120357630276) | [1m23s](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331691805) | 0% (0/61) | 206 |
| `ubuntu-latest` | github-hosted | 39 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39936624315/job/120357634856) | [10s](https://github.com/iree-org/iree/actions/runs/39921886772/job/120308830289) | 0% (0/9) | 39 |
| `azure-windows-scale` | ossci | 10 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/39941335495/job/120373285558) | [9s](https://github.com/iree-org/iree/actions/runs/39936937123/job/120358726732) | 0% (0/3) | 10 |
| `Linux,X64,iree-w7900` | self-hosted | 8 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [1h28m](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066974) | 2026-10-23 04:44 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [46m27s](https://github.com/iree-org/iree/actions/runs/39941335491/job/120378155197) | 2026-10-23 04:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [46m27s](https://github.com/iree-org/iree/actions/runs/39941335491/job/120378155221) | 2026-10-23 04:44 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |
| [46m27s](https://github.com/iree-org/iree/actions/runs/39941335491/job/120378155543) | 2026-10-23 04:44 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [46m27s](https://github.com/iree-org/iree/actions/runs/39941335491/job/120378155582) | 2026-10-23 04:44 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 8 | 1 | [46m27s](https://github.com/iree-org/iree/actions/runs/39941335491/job/120378155221) | 2026-10-23 04:44 PDT | [1h20m](https://github.com/iree-org/iree/actions/runs/39936624863/job/120360472890) | [1h30m](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395320) | [1h30m](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395320) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 8 | 2 | [1h28m](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066974) | 2026-10-23 04:44 PDT | [50m18s](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395419) | [1h07m](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692017) | [1h07m](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692017) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 8 | 0 | — | — | [59m52s](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692250) | [1h14m](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395434) | [1h14m](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395434) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 8 | 1 | [46m27s](https://github.com/iree-org/iree/actions/runs/39941335491/job/120378155582) | 2026-10-23 04:44 PDT | [32m52s](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395344) | [1h11m](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066818) | [1h11m](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066818) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [26m28s](https://github.com/iree-org/iree/actions/runs/39936624863/job/120360472859) | [56m32s](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066998) | [56m32s](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066998) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 8 | 1 | [46m27s](https://github.com/iree-org/iree/actions/runs/39941335491/job/120378155197) | 2026-10-23 04:44 PDT | [24m06s](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395534) | [54m44s](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066643) | [54m44s](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066643) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [30m35s](https://github.com/iree-org/iree/actions/runs/39925670084/job/120324381638) | [43m16s](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692267) | [43m16s](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692267) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 8 | 0 | — | — | [26m35s](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395226) | [37m54s](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692107) | [37m54s](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692107) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 8 | 0 | — | — | [20m20s](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395459) | [36m28s](https://github.com/iree-org/iree/actions/runs/39941335491/job/120378155092) | [36m28s](https://github.com/iree-org/iree/actions/runs/39941335491/job/120378155092) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [11m44s](https://github.com/iree-org/iree/actions/runs/39936624863/job/120360472861) | [29m08s](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692110) | [29m08s](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692110) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [11m56s](https://github.com/iree-org/iree/actions/runs/39936624863/job/120360472927) | [21m27s](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066891) | [21m27s](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066891) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39941335495/job/120373285320) | [3m48s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882476) | [3m48s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882476) | 10 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 12 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39943454523/job/120380330758) | [3m39s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882119) | [3m39s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882119) | 10 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39936937123/job/120358726438) | [3m20s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882050) | [3m20s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882050) | 10 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 10 | 0 | — | — | [30s](https://github.com/iree-org/iree/actions/runs/39928692461/job/120331437253) | [3m05s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882146) | [3m05s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882146) | 10 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 10 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/39936937123/job/120358726606) | [2m38s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882241) | [2m38s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882241) | 10 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 10 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/39943454523/job/120380330975) | [2m33s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308881998) | [2m33s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308881998) | 10 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 10 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/39936624895/job/120357712632) | [2m32s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882212) | [2m32s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882212) | 10 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | 12 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39936937123/job/120358665171) | [2m17s](https://github.com/iree-org/iree/actions/runs/39921888835/job/120308832270) | [2m17s](https://github.com/iree-org/iree/actions/runs/39921888835/job/120308832270) | 11 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 10 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/39924669265/job/120318404003) | [2m15s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882178) | [2m15s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882178) | 10 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 385 | 0% (0/384) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 323 | 2% (7/323) |  | 4m12s ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h30m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h11m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h14m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
