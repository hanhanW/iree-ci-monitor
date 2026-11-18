# iree-ci-monitor

_Updated: 2026-11-18 12:38 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [11m22s](https://github.com/iree-org/iree/actions/runs/44351058823/job/134971579686) | [31m17s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134889593821) | — | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 5 | 3 | [4h33m](https://github.com/iree-org/iree/actions/runs/44341029469/job/134937500612) | 2026-11-18 12:37 PST | 0 | [2s](https://github.com/iree-org/iree/actions/runs/44329483333/job/134915612928) | [28m04s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134889593446) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 10 | 0 | — | — | 0 | [8m54s](https://github.com/iree-org/iree/actions/runs/44329483333/job/134915613988) | [25m28s](https://github.com/iree-org/iree/actions/runs/44341029469/job/134937501112) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 10 | 0 | — | — | 1 | [10m27s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134889593579) | [23m09s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134889593415) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 10 | 0 | — | — | 0 | [7m44s](https://github.com/iree-org/iree/actions/runs/44341029469/job/134937501111) | [20m53s](https://github.com/iree-org/iree/actions/runs/44364834103/job/135020464492) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 10 | 6 | [4h33m](https://github.com/iree-org/iree/actions/runs/44341029469/job/134937501195) | 2026-11-18 12:37 PST | 0 | [10m56s](https://github.com/iree-org/iree/actions/runs/44329483333/job/134915614414) | [16m25s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134889593589) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 5 | 3 | [4h33m](https://github.com/iree-org/iree/actions/runs/44341029469/job/134937501361) | 2026-11-18 12:37 PST | 0 | [4m40s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134889593620) | [9m23s](https://github.com/iree-org/iree/actions/runs/44329483333/job/134915613652) | — | `shark75-ci` |
| `azure-linux-scale` | ossci | 36 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/44329483926/job/134910013100) | [1m25s](https://github.com/iree-org/iree/actions/runs/44329483926/job/134910013524) | — | 34 |
| `macos-15` | github-hosted | 18 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/44351058756/job/134966795820) | [21s](https://github.com/iree-org/iree/actions/runs/44341029612/job/134931236480) | — | 18 |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/44364833963/job/135015941019) | [7s](https://github.com/iree-org/iree/actions/runs/44341029612/job/134931237231) | — | 6 |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/44364833963/job/135015939055) | [5s](https://github.com/iree-org/iree/actions/runs/44351058756/job/134966796052) | — | 18 |
| `ubuntu-24.04` | github-hosted | 113 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/44351058823/job/134971580173) | [3s](https://github.com/iree-org/iree/actions/runs/44364834103/job/135020464046) | 0% (0/1) | 111 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/44340860961/job/134930124399) | [3s](https://github.com/iree-org/iree/actions/runs/44321024825/job/134859689822) | — | 12 |
| `windows-2022` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/44341029612/job/134931236604) | [2s](https://github.com/iree-org/iree/actions/runs/44364833963/job/135015939370) | — | 18 |
| `Linux,X64,iree-w7900` | self-hosted | 5 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [4h33m](https://github.com/iree-org/iree/actions/runs/44341029469/job/134937500612) | 2026-11-18 12:37 PST | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `users/roberto-laudani/update-torch-mlir` | pull_request |
| [4h33m](https://github.com/iree-org/iree/actions/runs/44341029469/job/134937501195) | 2026-11-18 12:37 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `users/roberto-laudani/update-torch-mlir` | pull_request |
| [4h33m](https://github.com/iree-org/iree/actions/runs/44341029469/job/134937501361) | 2026-11-18 12:37 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `users/roberto-laudani/update-torch-mlir` | pull_request |
| [4h33m](https://github.com/iree-org/iree/actions/runs/44341029469/job/134937501424) | 2026-11-18 12:37 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `users/roberto-laudani/update-torch-mlir` | pull_request |
| [3h43m](https://github.com/iree-org/iree/actions/runs/44351058823/job/134971579491) | 2026-11-18 12:37 PST | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `openssf-scorecard` | pull_request |
| [3h43m](https://github.com/iree-org/iree/actions/runs/44351058823/job/134971579748) | 2026-11-18 12:37 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `openssf-scorecard` | pull_request |
| [3h43m](https://github.com/iree-org/iree/actions/runs/44351058823/job/134971579934) | 2026-11-18 12:37 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `openssf-scorecard` | pull_request |
| [3h43m](https://github.com/iree-org/iree/actions/runs/44351058823/job/134971580340) | 2026-11-18 12:37 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `openssf-scorecard` | pull_request |
| [2h30m](https://github.com/iree-org/iree/actions/runs/44364834103/job/135020463823) | 2026-11-18 12:37 PST | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `L-roro/extend_tracy_supported_functions` | pull_request |
| [2h30m](https://github.com/iree-org/iree/actions/runs/44364834103/job/135020464118) | 2026-11-18 12:37 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `L-roro/extend_tracy_supported_functions` | pull_request |
| [2h30m](https://github.com/iree-org/iree/actions/runs/44364834103/job/135020464258) | 2026-11-18 12:37 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `L-roro/extend_tracy_supported_functions` | pull_request |
| [2h30m](https://github.com/iree-org/iree/actions/runs/44364834103/job/135020464349) | 2026-11-18 12:37 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `L-roro/extend_tracy_supported_functions` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 5 | 3 | [4h33m](https://github.com/iree-org/iree/actions/runs/44341029469/job/134937500612) | 2026-11-18 12:37 PST | [2s](https://github.com/iree-org/iree/actions/runs/44329483333/job/134915612928) | [28m04s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134889593446) | [28m04s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134889593446) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 5 | 3 | [4h33m](https://github.com/iree-org/iree/actions/runs/44341029469/job/134937501361) | 2026-11-18 12:37 PST | [4m40s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134889593620) | [9m23s](https://github.com/iree-org/iree/actions/runs/44329483333/job/134915613652) | [9m23s](https://github.com/iree-org/iree/actions/runs/44329483333/job/134915613652) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 5 | 3 | [4h33m](https://github.com/iree-org/iree/actions/runs/44341029469/job/134937501424) | 2026-11-18 12:37 PST | [2m34s](https://github.com/iree-org/iree/actions/runs/44329483333/job/134915614109) | [16m25s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134889593589) | [16m25s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134889593589) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 5 | 3 | [4h33m](https://github.com/iree-org/iree/actions/runs/44341029469/job/134937501195) | 2026-11-18 12:37 PST | [2s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134889593584) | [10m56s](https://github.com/iree-org/iree/actions/runs/44329483333/job/134915614414) | [10m56s](https://github.com/iree-org/iree/actions/runs/44329483333/job/134915614414) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 5 | 0 | — | — | [11m22s](https://github.com/iree-org/iree/actions/runs/44351058823/job/134971579686) | [31m17s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134889593821) | [31m17s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134889593821) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 5 | 0 | — | — | [12m43s](https://github.com/iree-org/iree/actions/runs/44364834103/job/135020464350) | [25m28s](https://github.com/iree-org/iree/actions/runs/44341029469/job/134937501112) | [25m28s](https://github.com/iree-org/iree/actions/runs/44341029469/job/134937501112) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [13m18s](https://github.com/iree-org/iree/actions/runs/44364834103/job/135020464114) | [23m09s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134889593415) | [23m09s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134889593415) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [14m19s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134889593583) | [20m53s](https://github.com/iree-org/iree/actions/runs/44364834103/job/135020464492) | [20m53s](https://github.com/iree-org/iree/actions/runs/44364834103/job/135020464492) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 5 | 0 | — | — | [4m03s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134889594241) | [20m05s](https://github.com/iree-org/iree/actions/runs/44351058823/job/134971579789) | [20m05s](https://github.com/iree-org/iree/actions/runs/44351058823/job/134971579789) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [7m44s](https://github.com/iree-org/iree/actions/runs/44341029469/job/134937501111) | [19m58s](https://github.com/iree-org/iree/actions/runs/44364834103/job/135020464237) | [19m58s](https://github.com/iree-org/iree/actions/runs/44364834103/job/135020464237) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/44351058823/job/134971579781) | [18m19s](https://github.com/iree-org/iree/actions/runs/44364834103/job/135020464102) | [18m19s](https://github.com/iree-org/iree/actions/runs/44364834103/job/135020464102) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 6 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/44351058823/job/134966730107) | [1m29s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134884112700) | [1m29s](https://github.com/iree-org/iree/actions/runs/44327844712/job/134884112700) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 6 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/44341029612/job/134931237306) | [1m25s](https://github.com/iree-org/iree/actions/runs/44329483926/job/134910013524) | [1m25s](https://github.com/iree-org/iree/actions/runs/44329483926/job/134910013524) | 5 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 6 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/44329483926/job/134910013369) | [27s](https://github.com/iree-org/iree/actions/runs/44351058756/job/134966797312) | [27s](https://github.com/iree-org/iree/actions/runs/44351058756/job/134966797312) | 6 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 6 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/44351058756/job/134966795820) | [21s](https://github.com/iree-org/iree/actions/runs/44341029612/job/134931236480) | [21s](https://github.com/iree-org/iree/actions/runs/44341029612/job/134931236480) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 6 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/44351058756/job/134966796273) | [21s](https://github.com/iree-org/iree/actions/runs/44341029612/job/134931236600) | [21s](https://github.com/iree-org/iree/actions/runs/44341029612/job/134931236600) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 6 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/44364833963/job/135015939416) | [20s](https://github.com/iree-org/iree/actions/runs/44341029612/job/134931236497) | [20s](https://github.com/iree-org/iree/actions/runs/44341029612/job/134931236497) | 6 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 6 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/44351058756/job/134966796686) | [9s](https://github.com/iree-org/iree/actions/runs/44364833963/job/135015940582) | [9s](https://github.com/iree-org/iree/actions/runs/44364833963/job/135015940582) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 6 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/44329483926/job/134910013100) | [9s](https://github.com/iree-org/iree/actions/runs/44351058756/job/134966796468) | [9s](https://github.com/iree-org/iree/actions/runs/44351058756/job/134966796468) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 6 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/44364833963/job/135015940421) | [9s](https://github.com/iree-org/iree/actions/runs/44351058756/job/134966796856) | [9s](https://github.com/iree-org/iree/actions/runs/44351058756/job/134966796856) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 321 | 1% (2/320) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 396 | 0% (1/396) |  | 2h04m ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job observed waiting 4h33m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 4h33m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job observed waiting 4h33m (> 2h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
