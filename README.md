# iree-ci-monitor

_Updated: 2026-10-19 15:25 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 16 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | 0 | [22m53s](https://github.com/iree-org/iree/actions/runs/39253754977/job/118067817567) | [1h47m](https://github.com/iree-org/iree/actions/runs/39260013822/job/118089165989) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 16 | 2 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | 0 | [21m45s](https://github.com/iree-org/iree/actions/runs/39302642894/job/118234895997) | [1h36m](https://github.com/iree-org/iree/actions/runs/39260013822/job/118089166490) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [12m34s](https://github.com/iree-org/iree/actions/runs/39302642894/job/118234896003) | [1h26m](https://github.com/iree-org/iree/actions/runs/39260013822/job/118089166161) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [42m26s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827326) | [1h15m](https://github.com/iree-org/iree/actions/runs/39253754977/job/118067817423) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 16 | 0 | — | — | 0 | [23m30s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827365) | [1h15m](https://github.com/iree-org/iree/actions/runs/39260013822/job/118089166456) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 8 | 0 | — | — | 0 | [16m58s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827134) | [36m26s](https://github.com/iree-org/iree/actions/runs/39255369599/job/118078931891) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 16 | 0 | — | — | 0 | [7m01s](https://github.com/iree-org/iree/actions/runs/39318807637/job/118290601023) | [17m48s](https://github.com/iree-org/iree/actions/runs/39253754977/job/118067817350) | 0% (0/4) | `shark55-ci`, `shark75-ci` |
| `azure-linux-scale` | ossci | 47 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/39252995745/job/118062211853) | [1m28s](https://github.com/iree-org/iree/actions/runs/39260013733/job/118085009380) | 0% (0/14) | 47 |
| `windows-2022` | github-hosted | 21 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287308927) | [1m17s](https://github.com/iree-org/iree/actions/runs/39252995745/job/118062211437) | 0% (0/6) | 21 |
| `macos-15` | github-hosted | 21 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287308999) | [55s](https://github.com/iree-org/iree/actions/runs/39252995745/job/118062211410) | 0% (0/6) | 21 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/39287569653/job/118179138569) | [48s](https://github.com/iree-org/iree/actions/runs/39252995745/job/118062211114) | 0% (0/6) | 21 |
| `ubuntu-latest` | github-hosted | 25 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/39253750862/job/118063744218) | [8s](https://github.com/iree-org/iree/actions/runs/39318806867/job/118287181358) | 0% (0/7) | 25 |
| `ubuntu-24.04` | github-hosted | 169 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39287569726/job/118184226011) | [6s](https://github.com/iree-org/iree/actions/runs/39260013822/job/118147566282) | 2% (1/40) | 155 |
| `azure-windows-scale` | ossci | 7 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/39260013733/job/118085009610) | [2s](https://github.com/iree-org/iree/actions/runs/39302642238/job/118231646227) | 50% (1/2) | 7 |
| `Linux,X64,iree-w7900` | self-hosted | 8 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `fix-spirv-wide-elementwise` | pull_request |
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `fix-spirv-wide-elementwise` | pull_request |
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827580) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `fix-spirv-wide-elementwise` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 8 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | [17m00s](https://github.com/iree-org/iree/actions/runs/39302642894/job/118234896132) | [2h55m](https://github.com/iree-org/iree/actions/runs/39253754977/job/118067817460) | [2h55m](https://github.com/iree-org/iree/actions/runs/39253754977/job/118067817460) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [3m22s](https://github.com/iree-org/iree/actions/runs/39302642894/job/118234896225) | [1h57m](https://github.com/iree-org/iree/actions/runs/39253754977/job/118067817536) | [1h57m](https://github.com/iree-org/iree/actions/runs/39253754977/job/118067817536) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 8 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | [23m04s](https://github.com/iree-org/iree/actions/runs/39287569726/job/118184226287) | [1h36m](https://github.com/iree-org/iree/actions/runs/39260013822/job/118089166490) | [1h36m](https://github.com/iree-org/iree/actions/runs/39260013822/job/118089166490) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 8 | 0 | — | — | [12m34s](https://github.com/iree-org/iree/actions/runs/39302642894/job/118234896003) | [1h26m](https://github.com/iree-org/iree/actions/runs/39260013822/job/118089166161) | [1h26m](https://github.com/iree-org/iree/actions/runs/39260013822/job/118089166161) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 8 | 0 | — | — | [42m26s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827326) | [1h15m](https://github.com/iree-org/iree/actions/runs/39253754977/job/118067817423) | [1h15m](https://github.com/iree-org/iree/actions/runs/39253754977/job/118067817423) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [26m01s](https://github.com/iree-org/iree/actions/runs/39255369599/job/118078932288) | [1h07m](https://github.com/iree-org/iree/actions/runs/39253754977/job/118067817686) | [1h07m](https://github.com/iree-org/iree/actions/runs/39253754977/job/118067817686) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 8 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827580) | 2026-10-19 06:26 PDT | [14m39s](https://github.com/iree-org/iree/actions/runs/39287569726/job/118184226243) | [1h07m](https://github.com/iree-org/iree/actions/runs/39253754977/job/118067817362) | [1h07m](https://github.com/iree-org/iree/actions/runs/39253754977/job/118067817362) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 8 | 0 | — | — | [16m58s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827134) | [36m26s](https://github.com/iree-org/iree/actions/runs/39255369599/job/118078931891) | [36m26s](https://github.com/iree-org/iree/actions/runs/39255369599/job/118078931891) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 8 | 0 | — | — | [22m53s](https://github.com/iree-org/iree/actions/runs/39253754977/job/118067817567) | [30m46s](https://github.com/iree-org/iree/actions/runs/39255369599/job/118078932063) | [30m46s](https://github.com/iree-org/iree/actions/runs/39255369599/job/118078932063) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [15m19s](https://github.com/iree-org/iree/actions/runs/39302642894/job/118234895972) | [28m15s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827466) | [28m15s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827466) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [3m08s](https://github.com/iree-org/iree/actions/runs/39302642894/job/118234895923) | [8m02s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827294) | [8m02s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827294) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 7 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/39287569653/job/118179139421) | [1m49s](https://github.com/iree-org/iree/actions/runs/39260013733/job/118085009952) | [1m49s](https://github.com/iree-org/iree/actions/runs/39260013733/job/118085009952) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 7 | 0 | — | — | [26s](https://github.com/iree-org/iree/actions/runs/39255369397/job/118070125691) | [1m48s](https://github.com/iree-org/iree/actions/runs/39260013733/job/118085009579) | [1m48s](https://github.com/iree-org/iree/actions/runs/39260013733/job/118085009579) | 7 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 7 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39287569653/job/118179138532) | [1m32s](https://github.com/iree-org/iree/actions/runs/39253755266/job/118063837589) | [1m32s](https://github.com/iree-org/iree/actions/runs/39253755266/job/118063837589) | 7 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 7 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/39252995745/job/118062211367) | [1m31s](https://github.com/iree-org/iree/actions/runs/39253755266/job/118063837737) | [1m31s](https://github.com/iree-org/iree/actions/runs/39253755266/job/118063837737) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 7 | 0 | — | — | [27s](https://github.com/iree-org/iree/actions/runs/39255369397/job/118070125677) | [1m28s](https://github.com/iree-org/iree/actions/runs/39260013733/job/118085009380) | [1m28s](https://github.com/iree-org/iree/actions/runs/39260013733/job/118085009380) | 7 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 7 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/39287569653/job/118179138909) | [1m26s](https://github.com/iree-org/iree/actions/runs/39253755266/job/118063837626) | [1m26s](https://github.com/iree-org/iree/actions/runs/39253755266/job/118063837626) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 4 | 0 | — | — | [44s](https://github.com/iree-org/iree/actions/runs/39255369397/job/118070125847) | [1m25s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309214) | [1m25s](https://github.com/iree-org/iree/actions/runs/39318807596/job/118287309214) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 7 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/39287569653/job/118179138328) | [1m24s](https://github.com/iree-org/iree/actions/runs/39253755266/job/118063837696) | [1m24s](https://github.com/iree-org/iree/actions/runs/39253755266/job/118063837696) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 7 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/39302642238/job/118231646468) | [1m23s](https://github.com/iree-org/iree/actions/runs/39255369397/job/118070125744) | [1m23s](https://github.com/iree-org/iree/actions/runs/39255369397/job/118070125744) | 7 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 390 | 3% (11/390) |  | 1h32m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 328 | 1% (2/328) |  | 1h34m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h15m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h36m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h26m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h15m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h47m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
