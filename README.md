# iree-ci-monitor

_Updated: 2026-08-12 06:50 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [33m17s](https://github.com/iree-org/iree/actions/runs/31589330007/job/94092226308) | [33m22s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070809814) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [15m48s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531327) | [29m54s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070809883) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [15m45s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531389) | [29m38s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070810119) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [12m39s](https://github.com/iree-org/iree/actions/runs/31589330007/job/94092226500) | [24m53s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070810011) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [17m36s](https://github.com/iree-org/iree/actions/runs/31583219282/job/94079019336) | [21m34s](https://github.com/iree-org/iree/actions/runs/31589330007/job/94092226321) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [9m02s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070809881) | [19m30s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070810069) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [3m23s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531356) | [13m59s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070809930) | 100% (1/1) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [8m57s](https://github.com/iree-org/iree/actions/runs/31583219282/job/94079019316) | [11m58s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070809847) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [4m10s](https://github.com/iree-org/iree/actions/runs/31589330007/job/94092226392) | [10m50s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531399) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [3m17s](https://github.com/iree-org/iree/actions/runs/31583219282/job/94079019128) | [8m28s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531615) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [2m11s](https://github.com/iree-org/iree/actions/runs/31583219282/job/94079019241) | [3m34s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531416) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m28s](https://github.com/iree-org/iree/actions/runs/31583860263/job/94073002035) | [1m28s](https://github.com/iree-org/iree/actions/runs/31583860263/job/94073002035) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 28 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/31589329864/job/94090452320) | [1m14s](https://github.com/iree-org/iree/actions/runs/31589329864/job/94090452219) | 0% (0/8) | 24 |
| `ubuntu-24.04` | github-hosted | 105 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531346) | [9s](https://github.com/iree-org/iree/actions/runs/31582379397/job/94068218969) | 5% (1/22) | 98 |
| `macos-14` | github-hosted | 18 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31582427580/job/94068459729) | [6s](https://github.com/iree-org/iree/actions/runs/31585530982/job/94093586483) | 0% (0/4) | 15 |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31585530982/job/94093586149) | [4s](https://github.com/iree-org/iree/actions/runs/31566985657/job/94020761396) | 0% (0/3) | 15 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31589329377/job/94090405505) | [4s](https://github.com/iree-org/iree/actions/runs/31586758961/job/94082267509) | 0% (0/3) | 12 |
| `windows-2022` | github-hosted | 17 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31583219161/job/94077093104) | [3s](https://github.com/iree-org/iree/actions/runs/31585530982/job/94093586094) | 0% (0/3) | 14 |
| `azure-windows-scale` | ossci | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31582427580/job/94068459788) | [2s](https://github.com/iree-org/iree/actions/runs/31583219161/job/94077093243) | 0% (0/1) | 4 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [33m17s](https://github.com/iree-org/iree/actions/runs/31589330007/job/94092226308) | [33m22s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070809814) | [33m22s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070809814) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [15m48s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531327) | [29m54s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070809883) | [29m54s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070809883) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [15m45s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531389) | [29m38s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070810119) | [29m38s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070810119) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [12m39s](https://github.com/iree-org/iree/actions/runs/31589330007/job/94092226500) | [24m53s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070810011) | [24m53s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070810011) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [20m56s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531483) | [21m34s](https://github.com/iree-org/iree/actions/runs/31589330007/job/94092226321) | [21m34s](https://github.com/iree-org/iree/actions/runs/31589330007/job/94092226321) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [10m34s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531524) | [19m30s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070810069) | [19m30s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070810069) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [12m35s](https://github.com/iree-org/iree/actions/runs/31589330007/job/94092226300) | [17m36s](https://github.com/iree-org/iree/actions/runs/31583219282/job/94079019336) | [17m36s](https://github.com/iree-org/iree/actions/runs/31583219282/job/94079019336) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [3m23s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531356) | [13m59s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070809930) | [13m59s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070809930) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [9m02s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070809881) | [13m23s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531407) | [13m23s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531407) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [8m57s](https://github.com/iree-org/iree/actions/runs/31583219282/job/94079019316) | [11m58s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070809847) | [11m58s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070809847) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [4m10s](https://github.com/iree-org/iree/actions/runs/31589330007/job/94092226392) | [10m50s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531399) | [10m50s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531399) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [3m17s](https://github.com/iree-org/iree/actions/runs/31583219282/job/94079019128) | [8m28s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531615) | [8m28s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531615) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [4m47s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531380) | [8m15s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070810063) | [8m15s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070810063) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [5m33s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94070809925) | [6m45s](https://github.com/iree-org/iree/actions/runs/31583219282/job/94079019333) | [6m45s](https://github.com/iree-org/iree/actions/runs/31583219282/job/94079019333) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 4 | 0 | — | — | [2m11s](https://github.com/iree-org/iree/actions/runs/31583219282/job/94079019241) | [3m34s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531416) | [3m34s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94095531416) | 2 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m28s](https://github.com/iree-org/iree/actions/runs/31583860263/job/94073002035) | [1m28s](https://github.com/iree-org/iree/actions/runs/31583860263/job/94073002035) | [1m28s](https://github.com/iree-org/iree/actions/runs/31583860263/job/94073002035) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 5 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/31585531036/job/94093607956) | [1m23s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94068460977) | [1m23s](https://github.com/iree-org/iree/actions/runs/31582427540/job/94068460977) | 5 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 5 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31585530982/job/94093586094) | [1m15s](https://github.com/iree-org/iree/actions/runs/31583219161/job/94077093005) | [1m15s](https://github.com/iree-org/iree/actions/runs/31583219161/job/94077093005) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 5 | 0 | — | — | [1m03s](https://github.com/iree-org/iree/actions/runs/31582427580/job/94068459784) | [1m14s](https://github.com/iree-org/iree/actions/runs/31589329864/job/94090452219) | [1m14s](https://github.com/iree-org/iree/actions/runs/31589329864/job/94090452219) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 5 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/31589329864/job/94090452320) | [1m05s](https://github.com/iree-org/iree/actions/runs/31582427580/job/94068459826) | [1m05s](https://github.com/iree-org/iree/actions/runs/31582427580/job/94068459826) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 192 | 0% (0/192) |  | 2h05m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 162 | 6% (10/162) |  | 2h13m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 135 | 13% (17/135) |  | 2h15m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 155 | 5% (7/155) |  | 2h17m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
