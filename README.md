# iree-ci-monitor

_Updated: 2026-10-13 15:49 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [15m21s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712710) | [59m29s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712357) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [12m10s](https://github.com/iree-org/iree/actions/runs/38402100476/job/115315577158) | [59m13s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712546) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [23m09s](https://github.com/iree-org/iree/actions/runs/38406694165/job/115331356422) | [44m40s](https://github.com/iree-org/iree/actions/runs/38406694165/job/115331356325) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [6m44s](https://github.com/iree-org/iree/actions/runs/38440632755/job/115450850597) | [27m49s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712674) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [21m31s](https://github.com/iree-org/iree/actions/runs/38406694165/job/115331355971) | [23m40s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712340) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [8m01s](https://github.com/iree-org/iree/actions/runs/38402100476/job/115315576766) | [19m28s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712413) | 0% (0/4) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [5m19s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712343) | [5m22s](https://github.com/iree-org/iree/actions/runs/38440632755/job/115450850726) | 0% (0/2) | `shark55-ci` |
| `macos-15` | github-hosted | 24 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/38409797849/job/115339949579) | [2m18s](https://github.com/iree-org/iree/actions/runs/38405847702/job/115325207675) | 0% (0/6) | 24 |
| `ubuntu-24.04-arm` | github-hosted | 24 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/38406697790/job/115329151923) | [2m15s](https://github.com/iree-org/iree/actions/runs/38405847702/job/115325207666) | 0% (0/6) | 24 |
| `windows-2022` | github-hosted | 24 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/38406694431/job/115328867280) | [2m02s](https://github.com/iree-org/iree/actions/runs/38406697790/job/115329152275) | 0% (0/6) | 24 |
| `azure-linux-scale` | ossci | 50 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/38409506387/job/115337915085) | [1m38s](https://github.com/iree-org/iree/actions/runs/38409506387/job/115337915075) | 0% (0/14) | 50 |
| `ubuntu-24.04` | github-hosted | 134 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38409507648/job/115337803108) | [1m21s](https://github.com/iree-org/iree/actions/runs/38406697790/job/115329152239) | 0% (0/41) | 133 |
| `azure-windows-scale` | ossci | 8 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/38440632841/job/115446059557) | [47s](https://github.com/iree-org/iree/actions/runs/38409797849/job/115339949856) | 0% (0/2) | 7 |
| `ubuntu-latest` | github-hosted | 33 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/38406593130/job/115327709416) | [3s](https://github.com/iree-org/iree/actions/runs/38441400723/job/115448616241) | 0% (0/6) | 33 |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [17m36s](https://github.com/iree-org/iree/actions/runs/38402100476/job/115315577054) | [59m29s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712357) | [59m29s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712357) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [18m27s](https://github.com/iree-org/iree/actions/runs/38406694165/job/115331356163) | [59m13s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712546) | [59m13s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712546) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [11m14s](https://github.com/iree-org/iree/actions/runs/38402100476/job/115315576762) | [44m40s](https://github.com/iree-org/iree/actions/runs/38406694165/job/115331356325) | [44m40s](https://github.com/iree-org/iree/actions/runs/38406694165/job/115331356325) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [25m54s](https://github.com/iree-org/iree/actions/runs/38402100476/job/115315577172) | [29m03s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712614) | [29m03s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712614) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [6m44s](https://github.com/iree-org/iree/actions/runs/38440632755/job/115450850597) | [27m49s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712674) | [27m49s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712674) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [21m31s](https://github.com/iree-org/iree/actions/runs/38406694165/job/115331355971) | [23m40s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712340) | [23m40s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712340) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [9m06s](https://github.com/iree-org/iree/actions/runs/38406694165/job/115331356244) | [20m56s](https://github.com/iree-org/iree/actions/runs/38402100476/job/115315576846) | [20m56s](https://github.com/iree-org/iree/actions/runs/38402100476/job/115315576846) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [8m28s](https://github.com/iree-org/iree/actions/runs/38440632755/job/115450850676) | [19m28s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712413) | [19m28s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712413) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [15m21s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712710) | [19m09s](https://github.com/iree-org/iree/actions/runs/38440632755/job/115450850739) | [19m09s](https://github.com/iree-org/iree/actions/runs/38440632755/job/115450850739) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [6m44s](https://github.com/iree-org/iree/actions/runs/38406694165/job/115331355920) | [15m13s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712337) | [15m13s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712337) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [5m19s](https://github.com/iree-org/iree/actions/runs/38409505983/job/115341712343) | [5m22s](https://github.com/iree-org/iree/actions/runs/38440632755/job/115450850726) | [5m22s](https://github.com/iree-org/iree/actions/runs/38440632755/job/115450850726) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 8 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/38440632841/job/115446059471) | [2m41s](https://github.com/iree-org/iree/actions/runs/38405847702/job/115325207748) | [2m41s](https://github.com/iree-org/iree/actions/runs/38405847702/job/115325207748) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 8 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/38409797849/job/115339949635) | [2m38s](https://github.com/iree-org/iree/actions/runs/38405847702/job/115325207708) | [2m38s](https://github.com/iree-org/iree/actions/runs/38405847702/job/115325207708) | 8 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 8 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/38405811674/job/115325117294) | [2m22s](https://github.com/iree-org/iree/actions/runs/38405847702/job/115325207480) | [2m22s](https://github.com/iree-org/iree/actions/runs/38405847702/job/115325207480) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 8 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38406697790/job/115329152069) | [2m18s](https://github.com/iree-org/iree/actions/runs/38405847702/job/115325207675) | [2m18s](https://github.com/iree-org/iree/actions/runs/38405847702/job/115325207675) | 8 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 8 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38409797849/job/115339949213) | [2m17s](https://github.com/iree-org/iree/actions/runs/38405847702/job/115325207589) | [2m17s](https://github.com/iree-org/iree/actions/runs/38405847702/job/115325207589) | 8 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 8 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38406697790/job/115329152619) | [2m15s](https://github.com/iree-org/iree/actions/runs/38409797849/job/115339949877) | [2m15s](https://github.com/iree-org/iree/actions/runs/38409797849/job/115339949877) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 8 | 0 | — | — | [29s](https://github.com/iree-org/iree/actions/runs/38405847702/job/115325207661) | [2m15s](https://github.com/iree-org/iree/actions/runs/38406697790/job/115329152775) | [2m15s](https://github.com/iree-org/iree/actions/runs/38406697790/job/115329152775) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 8 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/38409797849/job/115339949456) | [2m15s](https://github.com/iree-org/iree/actions/runs/38405847702/job/115325207666) | [2m15s](https://github.com/iree-org/iree/actions/runs/38405847702/job/115325207666) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 8 | 0 | — | — | [45s](https://github.com/iree-org/iree/actions/runs/38405811674/job/115325117731) | [2m07s](https://github.com/iree-org/iree/actions/runs/38405847702/job/115325207638) | [2m07s](https://github.com/iree-org/iree/actions/runs/38405847702/job/115325207638) | 8 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 311 | 13% (41/311) |  | 4h37m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 283 | 0% (0/283) |  | 4h43m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
