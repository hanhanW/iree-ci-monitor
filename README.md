# iree-ci-monitor

_Updated: 2026-06-10 12:13 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 12 | 0 | — | — | 0 | [21m43s](https://github.com/iree-org/iree/actions/runs/27277786359/job/80565805615) | [1h50m](https://github.com/iree-org/iree/actions/runs/27267001030/job/80528756803) | 25% (1/4) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 24 | 0 | — | — | 0 | [34m13s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764776) | [1h39m](https://github.com/iree-org/iree/actions/runs/27267001030/job/80528756859) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 12 | 0 | — | — | 0 | [25m21s](https://github.com/iree-org/iree/actions/runs/27268836032/job/80534488495) | [1h33m](https://github.com/iree-org/iree/actions/runs/27267001030/job/80528756775) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 12 | 0 | — | — | 0 | [17m48s](https://github.com/iree-org/iree/actions/runs/27277786359/job/80565805648) | [1h20m](https://github.com/iree-org/iree/actions/runs/27264226761/job/80525708271) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 12 | 0 | — | — | 0 | [19m22s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737278) | [58m33s](https://github.com/iree-org/iree/actions/runs/27267001030/job/80528756805) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 24 | 0 | — | — | 0 | [17m44s](https://github.com/iree-org/iree/actions/runs/27277786359/job/80565805758) | [56m28s](https://github.com/iree-org/iree/actions/runs/27267001030/job/80528756914) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 12 | 0 | — | — | 0 | [34m21s](https://github.com/iree-org/iree/actions/runs/27267001030/job/80528757117) | [53m08s](https://github.com/iree-org/iree/actions/runs/27268836032/job/80534488540) | 0% (0/4) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 12 | 0 | — | — | 0 | [18m27s](https://github.com/iree-org/iree/actions/runs/27287978538/job/80602310752) | [50m23s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943619) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 24 | 0 | — | — | 0 | [14m01s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943483) | [47m32s](https://github.com/iree-org/iree/actions/runs/27268836032/job/80534488429) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 24 | 0 | — | — | 0 | [17m12s](https://github.com/iree-org/iree/actions/runs/27267001030/job/80528756892) | [45m52s](https://github.com/iree-org/iree/actions/runs/27264226761/job/80525708167) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 60 | 0 | — | — | 0 | [1m11s](https://github.com/iree-org/iree/actions/runs/27287978502/job/80600434847) | [28m50s](https://github.com/iree-org/iree/actions/runs/27269163544/job/80533925600) | 0% (0/14) | 60 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 12 | 0 | — | — | 0 | [9m57s](https://github.com/iree-org/iree/actions/runs/27287978538/job/80602311156) | [21m03s](https://github.com/iree-org/iree/actions/runs/27268836032/job/80534488457) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27287978538/job/80602311221) | [8m20s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736833) | 0% (0/4) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 48 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/27277125245/job/80563160300) | [3m09s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737021) | 6% (1/16) | 48 |
| `windows-2022` | github-hosted | 33 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27278899197/job/80578176859) | [3m00s](https://github.com/iree-org/iree/actions/runs/27277786523/job/80564055062) | 0% (0/6) | 33 |
| `macos-14` | github-hosted | 34 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27289866882/job/80607579290) | [2m41s](https://github.com/iree-org/iree/actions/runs/27277786523/job/80564055123) | 0% (0/7) | 34 |
| `ubuntu-24.04-arm` | github-hosted | 33 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27268836507/job/80532808843) | [1m53s](https://github.com/iree-org/iree/actions/runs/27277387329/job/80562231503) | 0% (0/6) | 33 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m19s](https://github.com/iree-org/iree/actions/runs/27270524680/job/80538532157) | [1m19s](https://github.com/iree-org/iree/actions/runs/27270524680/job/80538532157) | 0% (0/1) | 1 |
| `ubuntu-24.04` | github-hosted | 236 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27287271492/job/80597827019) | [1m08s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943531) | 3% (2/61) | 236 |
| `ubuntu-latest` | github-hosted | 24 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27287267195/job/80597824730) | [3s](https://github.com/iree-org/iree/actions/runs/27285844176/job/80592714999) | 0% (0/6) | 24 |
| `azure-windows-scale` | ossci | 11 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27278899197/job/80578176965) | [2s](https://github.com/iree-org/iree/actions/runs/27289866882/job/80607579568) | 0% (0/2) | 11 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27268836032/job/80534488532) | [2s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602736816) | 25% (1/4) | 12 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27270493944/job/80538430456) | [2s](https://github.com/iree-org/iree/actions/runs/27270493944/job/80538430456) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 12 | 0 | — | — | [21m43s](https://github.com/iree-org/iree/actions/runs/27277786359/job/80565805615) | [1h50m](https://github.com/iree-org/iree/actions/runs/27267001030/job/80528756803) | [1h50m](https://github.com/iree-org/iree/actions/runs/27267001030/job/80528756803) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 12 | 0 | — | — | [52m40s](https://github.com/iree-org/iree/actions/runs/27277387490/job/80563738783) | [1h39m](https://github.com/iree-org/iree/actions/runs/27267001030/job/80528756859) | [1h39m](https://github.com/iree-org/iree/actions/runs/27267001030/job/80528756859) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 12 | 0 | — | — | [25m21s](https://github.com/iree-org/iree/actions/runs/27268836032/job/80534488495) | [1h33m](https://github.com/iree-org/iree/actions/runs/27267001030/job/80528756775) | [1h33m](https://github.com/iree-org/iree/actions/runs/27267001030/job/80528756775) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 12 | 0 | — | — | [17m48s](https://github.com/iree-org/iree/actions/runs/27277786359/job/80565805648) | [1h20m](https://github.com/iree-org/iree/actions/runs/27264226761/job/80525708271) | [1h23m](https://github.com/iree-org/iree/actions/runs/27264904091/job/80526015571) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 12 | 0 | — | — | [9m12s](https://github.com/iree-org/iree/actions/runs/27289866809/job/80608764812) | [1h16m](https://github.com/iree-org/iree/actions/runs/27264904091/job/80526015574) | [1h16m](https://github.com/iree-org/iree/actions/runs/27264904091/job/80526015574) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 12 | 0 | — | — | [29m49s](https://github.com/iree-org/iree/actions/runs/27264226761/job/80525708048) | [1h16m](https://github.com/iree-org/iree/actions/runs/27269163381/job/80540350102) | [2h10m](https://github.com/iree-org/iree/actions/runs/27267001030/job/80528756772) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 12 | 0 | — | — | [11m43s](https://github.com/iree-org/iree/actions/runs/27277786359/job/80565805719) | [1h03m](https://github.com/iree-org/iree/actions/runs/27264904091/job/80526015506) | [1h03m](https://github.com/iree-org/iree/actions/runs/27264904091/job/80526015506) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 12 | 0 | — | — | [19m22s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737278) | [58m33s](https://github.com/iree-org/iree/actions/runs/27267001030/job/80528756805) | [58m33s](https://github.com/iree-org/iree/actions/runs/27267001030/job/80528756805) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 12 | 0 | — | — | [22m38s](https://github.com/iree-org/iree/actions/runs/27264226761/job/80525708247) | [56m28s](https://github.com/iree-org/iree/actions/runs/27267001030/job/80528756914) | [56m28s](https://github.com/iree-org/iree/actions/runs/27267001030/job/80528756914) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 12 | 0 | — | — | [9m51s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943610) | [55m05s](https://github.com/iree-org/iree/actions/runs/27268836032/job/80534488668) | [55m05s](https://github.com/iree-org/iree/actions/runs/27268836032/job/80534488668) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 12 | 0 | — | — | [34m21s](https://github.com/iree-org/iree/actions/runs/27267001030/job/80528757117) | [53m08s](https://github.com/iree-org/iree/actions/runs/27268836032/job/80534488540) | [53m08s](https://github.com/iree-org/iree/actions/runs/27268836032/job/80534488540) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 12 | 0 | — | — | [18m27s](https://github.com/iree-org/iree/actions/runs/27287978538/job/80602310752) | [50m23s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943619) | [50m23s](https://github.com/iree-org/iree/actions/runs/27284594156/job/80597943619) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 12 | 0 | — | — | [18m56s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737088) | [47m32s](https://github.com/iree-org/iree/actions/runs/27268836032/job/80534488429) | [47m32s](https://github.com/iree-org/iree/actions/runs/27268836032/job/80534488429) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 11 | 0 | — | — | [47s](https://github.com/iree-org/iree/actions/runs/27268836507/job/80532808918) | [38m42s](https://github.com/iree-org/iree/actions/runs/27269163544/job/80533925856) | [38m42s](https://github.com/iree-org/iree/actions/runs/27269163544/job/80533925856) | 11 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 11 | 0 | — | — | [54s](https://github.com/iree-org/iree/actions/runs/27287271492/job/80597867338) | [38m40s](https://github.com/iree-org/iree/actions/runs/27269163544/job/80533925640) | [38m40s](https://github.com/iree-org/iree/actions/runs/27269163544/job/80533925640) | 11 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 12 | 0 | — | — | [23m05s](https://github.com/iree-org/iree/actions/runs/27287272236/job/80602737030) | [38m24s](https://github.com/iree-org/iree/actions/runs/27277387490/job/80563738767) | [38m24s](https://github.com/iree-org/iree/actions/runs/27277387490/job/80563738767) | 3 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 11 | 0 | — | — | [29s](https://github.com/iree-org/iree/actions/runs/27284593347/job/80596342251) | [37m31s](https://github.com/iree-org/iree/actions/runs/27269163544/job/80533925494) | [37m31s](https://github.com/iree-org/iree/actions/runs/27269163544/job/80533925494) | 11 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 11 | 0 | — | — | [1m19s](https://github.com/iree-org/iree/actions/runs/27268836507/job/80532809096) | [28m50s](https://github.com/iree-org/iree/actions/runs/27269163544/job/80533925600) | [28m50s](https://github.com/iree-org/iree/actions/runs/27269163544/job/80533925600) | 11 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 3 | 0 | — | — | [9m25s](https://github.com/iree-org/iree/actions/runs/27277387329/job/80562231819) | [25m19s](https://github.com/iree-org/iree/actions/runs/27269163544/job/80533925513) | [25m19s](https://github.com/iree-org/iree/actions/runs/27269163544/job/80533925513) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 12 | 0 | — | — | [9m57s](https://github.com/iree-org/iree/actions/runs/27287978538/job/80602311156) | [21m03s](https://github.com/iree-org/iree/actions/runs/27268836032/job/80534488457) | [28m00s](https://github.com/iree-org/iree/actions/runs/27277786359/job/80565805606) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 369 | 2% (9/369) |  | 2h01m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 322 | 7% (21/322) |  | 2h18m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 278 | 2% (5/278) |  | 2h19m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 272 | 2% (5/272) |  | 2h32m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 87 | 1% (1/87) |  | 2h35m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h33m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h39m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h50m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h20m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
