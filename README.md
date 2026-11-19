# iree-ci-monitor

_Updated: 2026-11-19 12:43 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [10m17s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767343) | [10m57s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767799) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [3m33s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767554) | [9m21s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767450) | 0% (0/2) | `shark55-ci` |
| `azure-linux-scale` | ossci | 28 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/44557367933/job/135677147991) | [6m31s](https://github.com/iree-org/iree/actions/runs/44544100442/job/135630170517) | 12% (1/8) | 28 |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [2m33s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767498) | [5m00s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767622) | 50% (1/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [3m38s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767369) | [3m38s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767369) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [1m27s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767549) | [1m53s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767946) | 50% (1/2) | `shark55-ci` |
| `macos-15` | github-hosted | 12 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/44549399134/job/135648991117) | [14s](https://github.com/iree-org/iree/actions/runs/44557367933/job/135677146999) | 0% (0/3) | 12 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/44576495814/job/135745392221) | [5s](https://github.com/iree-org/iree/actions/runs/44549399134/job/135648991250) | 0% (0/3) | 12 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/44557349980/job/135676914633) | [4s](https://github.com/iree-org/iree/actions/runs/44544085888/job/135629870743) | 0% (0/3) | 12 |
| `ubuntu-24.04` | github-hosted | 73 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767512) | [3s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767392) | 15% (3/20) | 72 |
| `windows-2022` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/44549399134/job/135648991040) | [3s](https://github.com/iree-org/iree/actions/runs/44549399134/job/135648991169) | 0% (0/3) | 12 |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767321) | [1s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767321) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767400) | [1s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767400) | 0% (0/1) | `shark55-ci` |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/44557367933/job/135677148329) | [1s](https://github.com/iree-org/iree/actions/runs/44576495814/job/135745392700) | 0% (0/1) | 4 |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [10m57s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767799) | [10m57s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767799) | [10m57s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767799) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [10m17s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767343) | [10m17s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767343) | [10m17s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767343) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [9m21s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767450) | [9m21s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767450) | [9m21s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767450) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 3 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/44557367933/job/135677147991) | [7m23s](https://github.com/iree-org/iree/actions/runs/44544100442/job/135630170653) | [7m23s](https://github.com/iree-org/iree/actions/runs/44544100442/job/135630170653) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 4 | 0 | — | — | [25s](https://github.com/iree-org/iree/actions/runs/44557367933/job/135677148277) | [6m31s](https://github.com/iree-org/iree/actions/runs/44544100442/job/135630170517) | [6m31s](https://github.com/iree-org/iree/actions/runs/44544100442/job/135630170517) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 4 | 0 | — | — | [45s](https://github.com/iree-org/iree/actions/runs/44557367933/job/135677148294) | [6m30s](https://github.com/iree-org/iree/actions/runs/44544100442/job/135630170450) | [6m30s](https://github.com/iree-org/iree/actions/runs/44544100442/job/135630170450) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 4 | 0 | — | — | [45s](https://github.com/iree-org/iree/actions/runs/44557367933/job/135677148560) | [5m47s](https://github.com/iree-org/iree/actions/runs/44544100442/job/135630170974) | [5m47s](https://github.com/iree-org/iree/actions/runs/44544100442/job/135630170974) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [5m00s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767622) | [5m00s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767622) | [5m00s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767622) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 4 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/44576495814/job/135745392033) | [4m56s](https://github.com/iree-org/iree/actions/runs/44544100442/job/135630170302) | [4m56s](https://github.com/iree-org/iree/actions/runs/44544100442/job/135630170302) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 4 | 0 | — | — | [25s](https://github.com/iree-org/iree/actions/runs/44557367933/job/135677148230) | [4m06s](https://github.com/iree-org/iree/actions/runs/44544100442/job/135630170655) | [4m06s](https://github.com/iree-org/iree/actions/runs/44544100442/job/135630170655) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [3m38s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767369) | [3m38s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767369) | [3m38s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767369) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [3m33s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767554) | [3m33s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767554) | [3m33s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767554) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44549399273/job/135686228601) | [2m33s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767498) | [2m33s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767498) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [1m53s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767946) | [1m53s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767946) | [1m53s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767946) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 4 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135745374519) | [1m28s](https://github.com/iree-org/iree/actions/runs/44544100360/job/135630145395) | [1m28s](https://github.com/iree-org/iree/actions/runs/44544100360/job/135630145395) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44557367976/job/135742179114) | [1m27s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767549) | [1m27s](https://github.com/iree-org/iree/actions/runs/44576496550/job/135758767549) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 4 | 0 | — | — | [13s](https://github.com/iree-org/iree/actions/runs/44557367933/job/135677147352) | [32s](https://github.com/iree-org/iree/actions/runs/44544100442/job/135630170818) | [32s](https://github.com/iree-org/iree/actions/runs/44544100442/job/135630170818) | 4 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 4 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/44544100442/job/135630170337) | [14s](https://github.com/iree-org/iree/actions/runs/44557367933/job/135677146999) | [14s](https://github.com/iree-org/iree/actions/runs/44557367933/job/135677146999) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 4 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/44549399134/job/135648991117) | [13s](https://github.com/iree-org/iree/actions/runs/44557367933/job/135677147597) | [13s](https://github.com/iree-org/iree/actions/runs/44557367933/job/135677147597) | 4 |
| `.github/workflows/build_clang_tidy.yml` | build_clang_tidy | `azure-linux-scale` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/44576495568/job/135745267558) | [10s](https://github.com/iree-org/iree/actions/runs/44576495568/job/135745267558) | [10s](https://github.com/iree-org/iree/actions/runs/44576495568/job/135745267558) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 353 | 1% (4/353) |  | 2h44m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 288 | 1% (3/288) |  | 2h48m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
