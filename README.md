# iree-ci-monitor

_Updated: 2026-10-23 10:13 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [1h01m](https://github.com/iree-org/iree/actions/runs/39925670084/job/120324381522) | [1h30m](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395320) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 22 | 0 | — | — | 0 | [34m21s](https://github.com/iree-org/iree/actions/runs/39936624863/job/120360472795) | [1h14m](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395434) | 0% (0/8) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 22 | 0 | — | — | 0 | [19m41s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628570) | [1h06m](https://github.com/iree-org/iree/actions/runs/39941335491/job/120378155582) | 0% (0/8) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 22 | 0 | — | — | 0 | [20m05s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446571347) | [43m16s](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692267) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [12m51s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628803) | [37m54s](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692107) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 11 | 0 | — | — | 0 | [19m01s](https://github.com/iree-org/iree/actions/runs/39920869270/job/120308146484) | [36m28s](https://github.com/iree-org/iree/actions/runs/39941335491/job/120378155092) | 0% (0/4) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 22 | 0 | — | — | 0 | [8m26s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628650) | [21m27s](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066891) | 0% (0/8) | `shark55-ci`, `shark75-ci` |
| `ubuntu-24.04-arm` | github-hosted | 39 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/39936624895/job/120357712632) | [2m15s](https://github.com/iree-org/iree/actions/runs/39928692461/job/120331437242) | 8% (1/12) | 39 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m47s](https://github.com/iree-org/iree/actions/runs/39932128255/job/120342726602) | [1m47s](https://github.com/iree-org/iree/actions/runs/39932128255/job/120342726602) | 100% (1/1) | 1 |
| `azure-linux-scale` | ossci | 85 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/39941335495/job/120373285632) | [1m29s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498214611) | 3% (1/30) | 85 |
| `windows-2022` | github-hosted | 39 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498214588) | [1m23s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882130) | 0% (0/12) | 39 |
| `ubuntu-24.04` | github-hosted | 276 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39953532423/job/120413621987) | [1m16s](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362067029) | 2% (2/81) | 262 |
| `macos-15` | github-hosted | 40 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/39941335495/job/120373285276) | [1m03s](https://github.com/iree-org/iree/actions/runs/39920869144/job/120305567107) | 0% (0/13) | 40 |
| `ubuntu-latest` | github-hosted | 57 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39943451523/job/120380247967) | [15s](https://github.com/iree-org/iree/actions/runs/39921758986/job/120308409884) | 0% (0/12) | 57 |
| `azure-windows-scale` | ossci | 13 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/39943454523/job/120380331303) | [9s](https://github.com/iree-org/iree/actions/runs/39936937123/job/120358726732) | 0% (0/4) | 13 |
| `Linux,X64,iree-w7900` | self-hosted | 11 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 11 | 0 | — | — | [34m21s](https://github.com/iree-org/iree/actions/runs/39936624863/job/120360472795) | [1h33m](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066974) | [1h33m](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066974) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 11 | 0 | — | — | [1h01m](https://github.com/iree-org/iree/actions/runs/39925670084/job/120324381522) | [1h30m](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395320) | [1h30m](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395320) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 11 | 0 | — | — | [38m34s](https://github.com/iree-org/iree/actions/runs/39941335491/job/120378155166) | [1h14m](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395434) | [1h14m](https://github.com/iree-org/iree/actions/runs/39921765533/job/120311395434) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 11 | 0 | — | — | [19m41s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628570) | [1h11m](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066818) | [1h11m](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066818) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 11 | 0 | — | — | [15m16s](https://github.com/iree-org/iree/actions/runs/39925670084/job/120324381531) | [56m32s](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066998) | [56m32s](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066998) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 11 | 0 | — | — | [12m22s](https://github.com/iree-org/iree/actions/runs/39978153928/job/120508233531) | [56m20s](https://github.com/iree-org/iree/actions/runs/39941335491/job/120378155197) | [56m20s](https://github.com/iree-org/iree/actions/runs/39941335491/job/120378155197) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 11 | 0 | — | — | [20m05s](https://github.com/iree-org/iree/actions/runs/39962359084/job/120446571347) | [43m16s](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692267) | [43m16s](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692267) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 11 | 0 | — | — | [12m51s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628803) | [37m54s](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692107) | [37m54s](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692107) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 11 | 0 | — | — | [19m01s](https://github.com/iree-org/iree/actions/runs/39920869270/job/120308146484) | [36m28s](https://github.com/iree-org/iree/actions/runs/39941335491/job/120378155092) | [36m28s](https://github.com/iree-org/iree/actions/runs/39941335491/job/120378155092) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 11 | 0 | — | — | [2m46s](https://github.com/iree-org/iree/actions/runs/39925670084/job/120324381611) | [29m08s](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692110) | [29m08s](https://github.com/iree-org/iree/actions/runs/39927712593/job/120331692110) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 11 | 0 | — | — | [8m26s](https://github.com/iree-org/iree/actions/runs/39975607288/job/120517628650) | [21m27s](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066891) | [21m27s](https://github.com/iree-org/iree/actions/runs/39936937234/job/120362066891) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 13 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39975607072/job/120513781977) | [3m48s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882476) | [3m48s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882476) | 13 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 15 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39975607072/job/120513781490) | [3m39s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882119) | [3m39s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882119) | 13 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 13 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/39975607072/job/120513781827) | [3m05s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882146) | [3m05s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882146) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 13 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/39941335495/job/120373285276) | [2m38s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882241) | [2m38s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882241) | 13 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 13 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/39975607072/job/120513781752) | [2m33s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308881998) | [2m33s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308881998) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 13 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/39936624895/job/120357712632) | [2m32s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882212) | [2m32s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882212) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 13 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/39924669265/job/120318404003) | [2m15s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882178) | [2m15s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882178) | 13 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 15 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39962359052/job/120443374091) | [2m14s](https://github.com/iree-org/iree/actions/runs/39928692461/job/120331437409) | [2m14s](https://github.com/iree-org/iree/actions/runs/39928692461/job/120331437409) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 13 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39978153994/job/120498214536) | [2m12s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882179) | [2m12s](https://github.com/iree-org/iree/actions/runs/39921765670/job/120308882179) | 13 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 408 | 0% (0/408) |  | 47m45s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 338 | 2% (7/338) |  | 54m06s ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h30m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h14m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
