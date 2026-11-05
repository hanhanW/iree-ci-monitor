# iree-ci-monitor

_Updated: 2026-11-05 12:01 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 18 | 0 | — | — | 0 | [59m23s](https://github.com/iree-org/iree/actions/runs/42066427083/job/127387084738) | [2h23m](https://github.com/iree-org/iree/actions/runs/42049182733/job/127325131104) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 9 | 0 | — | — | 0 | [22m38s](https://github.com/iree-org/iree/actions/runs/42057296414/job/127353601830) | [2h06m](https://github.com/iree-org/iree/actions/runs/42049182733/job/127325131683) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 18 | 0 | — | — | 0 | [1h29m](https://github.com/iree-org/iree/actions/runs/42032451511/job/127374085890) | [1h52m](https://github.com/iree-org/iree/actions/runs/42057536171/job/127357525394) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [35m47s](https://github.com/iree-org/iree/actions/runs/42066427083/job/127387085385) | [1h32m](https://github.com/iree-org/iree/actions/runs/42040605148/job/127294911387) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 18 | 0 | — | — | 0 | [17m57s](https://github.com/iree-org/iree/actions/runs/42049182733/job/127325131441) | [1h27m](https://github.com/iree-org/iree/actions/runs/42057296414/job/127353602390) | 0% (0/4) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 18 | 0 | — | — | 0 | [38m20s](https://github.com/iree-org/iree/actions/runs/42046565918/job/127315737987) | [1h27m](https://github.com/iree-org/iree/actions/runs/42057536171/job/127357525355) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [21m28s](https://github.com/iree-org/iree/actions/runs/42040603121/job/127294629508) | [36m26s](https://github.com/iree-org/iree/actions/runs/42066427083/job/127387084532) | 0% (0/2) | `shark55-ci` |
| `azure-windows-scale` | ossci | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/42032451692/job/127369066960) | [10m02s](https://github.com/iree-org/iree/actions/runs/42057536342/job/127350328050) | 0% (0/2) | 9 |
| `azure-linux-scale` | ossci | 64 | 0 | — | — | 0 | [50s](https://github.com/iree-org/iree/actions/runs/42032451692/job/127369066170) | [7m14s](https://github.com/iree-org/iree/actions/runs/42057296224/job/127349189772) | 7% (1/14) | 64 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [38s](https://github.com/iree-org/iree/actions/runs/42042366719/job/127296805719) | [3m23s](https://github.com/iree-org/iree/actions/runs/42042367409/job/127296226629) | 0% (0/6) | 12 |
| `ubuntu-24.04` | github-hosted | 209 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/42066427083/job/127387084380) | [2m25s](https://github.com/iree-org/iree/actions/runs/42040605139/job/127291741507) | 3% (1/39) | 204 |
| `macos-15` | github-hosted | 35 | 0 | — | — | 2 | [8s](https://github.com/iree-org/iree/actions/runs/42032451692/job/127369065768) | [2m23s](https://github.com/iree-org/iree/actions/runs/42068458902/job/127389381326) | 0% (0/6) | 35 |
| `ubuntu-24.04-arm` | github-hosted | 33 | 0 | — | — | 1 | [5s](https://github.com/iree-org/iree/actions/runs/42057296224/job/127349188992) | [1m56s](https://github.com/iree-org/iree/actions/runs/42032530364/job/127262432029) | 0% (0/6) | 33 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 4 | 0 | — | — | 0 | [1m38s](https://github.com/iree-org/iree/actions/runs/42040602987/job/127290653085) | [1m38s](https://github.com/iree-org/iree/actions/runs/42040605139/job/127291741857) | — | 4 |
| `windows-2022` | github-hosted | 31 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/42046565902/job/127311119917) | [1m34s](https://github.com/iree-org/iree/actions/runs/42032530364/job/127262431794) | 17% (1/6) | 31 |
| `Linux,X64,iree-w7900` | self-hosted | 9 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 9 | 0 | — | — | [1h29m](https://github.com/iree-org/iree/actions/runs/42032451511/job/127374085890) | [2h55m](https://github.com/iree-org/iree/actions/runs/42040605148/job/127294911149) | [2h55m](https://github.com/iree-org/iree/actions/runs/42040605148/job/127294911149) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [1h21m](https://github.com/iree-org/iree/actions/runs/42032451511/job/127374085446) | [2h48m](https://github.com/iree-org/iree/actions/runs/42040605148/job/127294911258) | [2h48m](https://github.com/iree-org/iree/actions/runs/42040605148/job/127294911258) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [46m13s](https://github.com/iree-org/iree/actions/runs/42032530416/job/127266112426) | [2h23m](https://github.com/iree-org/iree/actions/runs/42049182733/job/127325131104) | [2h23m](https://github.com/iree-org/iree/actions/runs/42049182733/job/127325131104) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 9 | 0 | — | — | [22m38s](https://github.com/iree-org/iree/actions/runs/42057296414/job/127353601830) | [2h06m](https://github.com/iree-org/iree/actions/runs/42049182733/job/127325131683) | [2h06m](https://github.com/iree-org/iree/actions/runs/42049182733/job/127325131683) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 9 | 0 | — | — | [1h48m](https://github.com/iree-org/iree/actions/runs/42040605148/job/127294911632) | [1h52m](https://github.com/iree-org/iree/actions/runs/42057536171/job/127357525394) | [1h52m](https://github.com/iree-org/iree/actions/runs/42057536171/job/127357525394) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [21m37s](https://github.com/iree-org/iree/actions/runs/42046565918/job/127315737757) | [1h41m](https://github.com/iree-org/iree/actions/runs/42057536171/job/127357525801) | [1h41m](https://github.com/iree-org/iree/actions/runs/42057536171/job/127357525801) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [29m39s](https://github.com/iree-org/iree/actions/runs/42057296414/job/127353602345) | [1h35m](https://github.com/iree-org/iree/actions/runs/42057536171/job/127357525398) | [1h35m](https://github.com/iree-org/iree/actions/runs/42057536171/job/127357525398) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 9 | 0 | — | — | [35m47s](https://github.com/iree-org/iree/actions/runs/42066427083/job/127387085385) | [1h32m](https://github.com/iree-org/iree/actions/runs/42040605148/job/127294911387) | [1h32m](https://github.com/iree-org/iree/actions/runs/42040605148/job/127294911387) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [48m08s](https://github.com/iree-org/iree/actions/runs/42046565918/job/127315738258) | [1h27m](https://github.com/iree-org/iree/actions/runs/42057536171/job/127357525355) | [1h27m](https://github.com/iree-org/iree/actions/runs/42057536171/job/127357525355) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [17m57s](https://github.com/iree-org/iree/actions/runs/42049182733/job/127325131441) | [1h02m](https://github.com/iree-org/iree/actions/runs/42032451511/job/127374085872) | [1h02m](https://github.com/iree-org/iree/actions/runs/42032451511/job/127374085872) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 9 | 0 | — | — | [21m28s](https://github.com/iree-org/iree/actions/runs/42040603121/job/127294629508) | [36m26s](https://github.com/iree-org/iree/actions/runs/42066427083/job/127387084532) | [36m26s](https://github.com/iree-org/iree/actions/runs/42066427083/job/127387084532) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 9 | 0 | — | — | [1m24s](https://github.com/iree-org/iree/actions/runs/42040602987/job/127290652425) | [33m58s](https://github.com/iree-org/iree/actions/runs/42057536342/job/127350327996) | [33m58s](https://github.com/iree-org/iree/actions/runs/42057536342/job/127350327996) | 9 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 9 | 0 | — | — | [58s](https://github.com/iree-org/iree/actions/runs/42032451692/job/127369067798) | [33m06s](https://github.com/iree-org/iree/actions/runs/42057536342/job/127350327723) | [33m06s](https://github.com/iree-org/iree/actions/runs/42057536342/job/127350327723) | 9 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 9 | 0 | — | — | [49s](https://github.com/iree-org/iree/actions/runs/42032451692/job/127369067104) | [12m42s](https://github.com/iree-org/iree/actions/runs/42057536342/job/127350327844) | [12m42s](https://github.com/iree-org/iree/actions/runs/42057536342/job/127350327844) | 9 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42032451692/job/127369066960) | [10m02s](https://github.com/iree-org/iree/actions/runs/42057536342/job/127350328050) | [10m02s](https://github.com/iree-org/iree/actions/runs/42057536342/job/127350328050) | 9 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64-baremetal | `ubuntu-24.04` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42057536171/job/127357525696) | [7m14s](https://github.com/iree-org/iree/actions/runs/42040603121/job/127294628990) | [7m14s](https://github.com/iree-org/iree/actions/runs/42040603121/job/127294628990) | 9 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 9 | 0 | — | — | [50s](https://github.com/iree-org/iree/actions/runs/42032451692/job/127369066170) | [7m13s](https://github.com/iree-org/iree/actions/runs/42057296224/job/127349189694) | [7m13s](https://github.com/iree-org/iree/actions/runs/42057296224/job/127349189694) | 9 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 9 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/42032451511/job/127374085499) | [5m23s](https://github.com/iree-org/iree/actions/runs/42040603121/job/127294628730) | [5m23s](https://github.com/iree-org/iree/actions/runs/42040603121/job/127294628730) | 9 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42057536171/job/127357525911) | [4m55s](https://github.com/iree-org/iree/actions/runs/42040603121/job/127294629179) | [4m55s](https://github.com/iree-org/iree/actions/runs/42040603121/job/127294629179) | 9 |
| `.github/workflows/pkgci.yml` | Unit Test / Linux (x86_64) | `ubuntu-24.04` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/42057536171/job/127357525618) | [4m28s](https://github.com/iree-org/iree/actions/runs/42040605148/job/127294911045) | [4m28s](https://github.com/iree-org/iree/actions/runs/42040605148/job/127294911045) | 9 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 544 | 1% (8/544) |  | 2h02m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 430 | 1% (5/430) |  | 2h09m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h23m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h27m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h52m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h27m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
