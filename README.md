# iree-ci-monitor

_Updated: 2026-10-01 06:25 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [1h33m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383144) | [2h00m](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492540) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [17m09s](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492131) | [1h48m](https://github.com/iree-org/iree/actions/runs/36841366234/job/110303522129) | 0% (0/4) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [43m10s](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492315) | [1h35m](https://github.com/iree-org/iree/actions/runs/36838964518/job/110295665922) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [17m13s](https://github.com/iree-org/iree/actions/runs/36843172540/job/110310560170) | [1h28m](https://github.com/iree-org/iree/actions/runs/36841366234/job/110303522201) | 0% (0/4) | `shark75-ci` |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/36838910844/job/110293035638) | [2m54s](https://github.com/iree-org/iree/actions/runs/36838964561/job/110293216691) | 0% (0/12) | 21 |
| `azure-linux-scale` | ossci | 36 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/36860180080/job/110362248533) | [2m04s](https://github.com/iree-org/iree/actions/runs/36843172540/job/110306918963) | 15% (4/26) | 36 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m29s](https://github.com/iree-org/iree/actions/runs/36843274375/job/110307150959) | [1m29s](https://github.com/iree-org/iree/actions/runs/36843274375/job/110307150959) | 100% (1/1) | 1 |
| `macos-14` | github-hosted | 21 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/36841365851/job/110301084834) | [1m16s](https://github.com/iree-org/iree/actions/runs/36838964561/job/110293216442) | 0% (0/12) | 21 |
| `ubuntu-24.04` | github-hosted | 124 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/36843172633/job/110306898304) | [1m10s](https://github.com/iree-org/iree/actions/runs/36838964518/job/110295666095) | 3% (2/76) | 122 |
| `windows-2022` | github-hosted | 20 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/36841365851/job/110301084807) | [54s](https://github.com/iree-org/iree/actions/runs/36838964561/job/110293216646) | 0% (0/12) | 20 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36843170772/job/110306827242) | [12s](https://github.com/iree-org/iree/actions/runs/36838965204/job/110293147199) | 0% (0/12) | 12 |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/36860180080/job/110362248650) | [3s](https://github.com/iree-org/iree/actions/runs/36841365851/job/110301085160) | 0% (0/4) | 6 |
| `Linux,X64,rdna3` | self-hosted | 12 | 12 | [5h04m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383120) | 2026-10-01 06:24 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 12 | 12 | [5h04m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382988) | 2026-10-01 06:24 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 6 | [5h04m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382976) | 2026-10-01 06:24 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 6 | 6 | [5h04m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382936) | 2026-10-01 06:24 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [5h04m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382936) | 2026-10-01 06:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `main` | push |
| [5h04m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382976) | 2026-10-01 06:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |
| [5h04m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382988) | 2026-10-01 06:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [5h04m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383120) | 2026-10-01 06:24 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [5h04m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383211) | 2026-10-01 06:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [5h04m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383216) | 2026-10-01 06:24 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [4h26m](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492369) | 2026-10-01 06:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `main` | push |
| [4h26m](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492455) | 2026-10-01 06:24 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [4h26m](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492528) | 2026-10-01 06:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |
| [4h26m](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492574) | 2026-10-01 06:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [4h26m](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492602) | 2026-10-01 06:24 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [4h26m](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492701) | 2026-10-01 06:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [4h25m](https://github.com/iree-org/iree/actions/runs/36838964518/job/110295665844) | 2026-10-01 06:24 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [4h25m](https://github.com/iree-org/iree/actions/runs/36838964518/job/110295665863) | 2026-10-01 06:24 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [4h25m](https://github.com/iree-org/iree/actions/runs/36838964518/job/110295665868) | 2026-10-01 06:24 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 6 | [5h04m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382976) | 2026-10-01 06:24 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 6 | 6 | [5h04m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382936) | 2026-10-01 06:24 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 6 | [5h04m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382988) | 2026-10-01 06:24 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 6 | [5h04m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383211) | 2026-10-01 06:24 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 6 | [5h04m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383216) | 2026-10-01 06:24 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 6 | [5h04m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383120) | 2026-10-01 06:24 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [1h33m](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282383144) | [2h33m](https://github.com/iree-org/iree/actions/runs/36838964518/job/110295665819) | [2h33m](https://github.com/iree-org/iree/actions/runs/36838964518/job/110295665819) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [35m24s](https://github.com/iree-org/iree/actions/runs/36834861342/job/110282382932) | [2h05m](https://github.com/iree-org/iree/actions/runs/36841366234/job/110303522319) | [2h05m](https://github.com/iree-org/iree/actions/runs/36841366234/job/110303522319) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [17m09s](https://github.com/iree-org/iree/actions/runs/36838910756/job/110295492131) | [1h48m](https://github.com/iree-org/iree/actions/runs/36841366234/job/110303522129) | [1h48m](https://github.com/iree-org/iree/actions/runs/36841366234/job/110303522129) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [22m14s](https://github.com/iree-org/iree/actions/runs/36860180124/job/110364753007) | [1h40m](https://github.com/iree-org/iree/actions/runs/36838964518/job/110295665936) | [1h40m](https://github.com/iree-org/iree/actions/runs/36838964518/job/110295665936) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [17m13s](https://github.com/iree-org/iree/actions/runs/36843172540/job/110310560170) | [1h28m](https://github.com/iree-org/iree/actions/runs/36841366234/job/110303522201) | [1h28m](https://github.com/iree-org/iree/actions/runs/36841366234/job/110303522201) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [32m52s](https://github.com/iree-org/iree/actions/runs/36860180124/job/110364753102) | [1h04m](https://github.com/iree-org/iree/actions/runs/36841366234/job/110303522479) | [1h04m](https://github.com/iree-org/iree/actions/runs/36841366234/job/110303522479) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 6 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/36838910844/job/110293034903) | [3m08s](https://github.com/iree-org/iree/actions/runs/36838964561/job/110293216587) | [3m08s](https://github.com/iree-org/iree/actions/runs/36838964561/job/110293216587) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 6 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/36838910844/job/110293035638) | [2m54s](https://github.com/iree-org/iree/actions/runs/36838964561/job/110293216691) | [2m54s](https://github.com/iree-org/iree/actions/runs/36838964561/job/110293216691) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 6 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/36838910844/job/110293035252) | [2m48s](https://github.com/iree-org/iree/actions/runs/36838964561/job/110293216856) | [2m48s](https://github.com/iree-org/iree/actions/runs/36838964561/job/110293216856) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 6 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36834861188/job/110279794274) | [2m35s](https://github.com/iree-org/iree/actions/runs/36838964561/job/110293216699) | [2m35s](https://github.com/iree-org/iree/actions/runs/36838964561/job/110293216699) | 6 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 6 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36843172633/job/110306898703) | [2m21s](https://github.com/iree-org/iree/actions/runs/36838964561/job/110293217025) | [2m21s](https://github.com/iree-org/iree/actions/runs/36838964561/job/110293217025) | 6 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36843172633/job/110306898500) | [2m06s](https://github.com/iree-org/iree/actions/runs/36838964561/job/110293216869) | [2m06s](https://github.com/iree-org/iree/actions/runs/36838964561/job/110293216869) | 6 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 6 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36834861342/job/110279784388) | [2m04s](https://github.com/iree-org/iree/actions/runs/36843172540/job/110306918963) | [2m04s](https://github.com/iree-org/iree/actions/runs/36843172540/job/110306918963) | 6 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64-baremetal | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/36860180124/job/110364753114) | [2m03s](https://github.com/iree-org/iree/actions/runs/36838964518/job/110295666349) | [2m03s](https://github.com/iree-org/iree/actions/runs/36838964518/job/110295666349) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 280 | 2% (7/280) |  | 23m44s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 329 | 1% (2/329) |  | 16h54m ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 5h04m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 5h04m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 5h04m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 5h04m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h28m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h48m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h35m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
