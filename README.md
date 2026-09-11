# iree-ci-monitor

_Updated: 2026-09-11 14:01 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 28 | 2 | [2h00m](https://github.com/iree-org/iree/actions/runs/34581758865/job/103214541971) | 2026-09-11 04:27 PDT | 0 | [2h05m](https://github.com/iree-org/iree/actions/runs/34600457106/job/103268686685) | [4h40m](https://github.com/iree-org/iree/actions/runs/34600458124/job/103271388651) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 14 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077064) | 2026-09-08 04:24 PDT | 0 | [1h35m](https://github.com/iree-org/iree/actions/runs/34600457228/job/103269590177) | [3h01m](https://github.com/iree-org/iree/actions/runs/34600452293/job/103268473324) | 0% (0/4) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 14 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077123) | 2026-09-08 04:24 PDT | 0 | [22m46s](https://github.com/iree-org/iree/actions/runs/34614704603/job/103320823417) | [2h52m](https://github.com/iree-org/iree/actions/runs/34600452293/job/103268473346) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 26 | 0 | — | — | 0 | [15m53s](https://github.com/iree-org/iree/actions/runs/34632536823/job/103374904499) | [2h25m](https://github.com/iree-org/iree/actions/runs/34600457106/job/103268686911) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 27 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076982) | 2026-09-08 04:24 PDT | 0 | [16m47s](https://github.com/iree-org/iree/actions/runs/34637491886/job/103391182343) | [2h20m](https://github.com/iree-org/iree/actions/runs/34600458124/job/103271388690) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 14 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076911) | 2026-09-08 04:24 PDT | 0 | [16m04s](https://github.com/iree-org/iree/actions/runs/34599870179/job/103266393297) | [2h18m](https://github.com/iree-org/iree/actions/runs/34600457106/job/103268686619) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 13 | 0 | — | — | 0 | [28m20s](https://github.com/iree-org/iree/actions/runs/34614704603/job/103320822996) | [2h02m](https://github.com/iree-org/iree/actions/runs/34600458852/job/103271494348) | 0% (0/4) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 26 | 0 | — | — | 0 | [9m42s](https://github.com/iree-org/iree/actions/runs/34599870179/job/103266393637) | [1h33m](https://github.com/iree-org/iree/actions/runs/34600457228/job/103269590352) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 13 | 0 | — | — | 0 | [16m24s](https://github.com/iree-org/iree/actions/runs/34600458124/job/103271388526) | [1h20m](https://github.com/iree-org/iree/actions/runs/34600452293/job/103268473289) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 13 | 0 | — | — | 0 | [25m40s](https://github.com/iree-org/iree/actions/runs/34632536823/job/103374904338) | [1h15m](https://github.com/iree-org/iree/actions/runs/34600458852/job/103271494609) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 13 | 0 | — | — | 0 | [24m18s](https://github.com/iree-org/iree/actions/runs/34584167104/job/103241696846) | [1h12m](https://github.com/iree-org/iree/actions/runs/34599870179/job/103266393517) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `ubuntu-24.04` | github-hosted | 277 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/34637491616/job/103388843613) | [19m27s](https://github.com/iree-org/iree/actions/runs/34600458852/job/103271494825) | 4% (3/73) | 270 |
| `ubuntu-24.04-arm` | github-hosted | 36 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/34632536779/job/103372646842) | [15m55s](https://github.com/iree-org/iree/actions/runs/34600458834/job/103267748209) | 0% (0/9) | 36 |
| `macos-14` | github-hosted | 36 | 0 | — | — | 0 | [13s](https://github.com/iree-org/iree/actions/runs/34614704614/job/103313672049) | [12m36s](https://github.com/iree-org/iree/actions/runs/34600457814/job/103272268426) | 0% (0/9) | 36 |
| `windows-2022` | github-hosted | 36 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/34621526530/job/103336486709) | [10m01s](https://github.com/iree-org/iree/actions/runs/34600457814/job/103272268034) | 0% (0/9) | 36 |
| `ubuntu-latest` | github-hosted | 36 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/34615343789/job/103315753963) | [7m44s](https://github.com/iree-org/iree/actions/runs/34600454721/job/103266188476) | 0% (0/9) | 36 |
| `azure-linux-scale` | ossci | 64 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/34637491884/job/103388906585) | [1m22s](https://github.com/iree-org/iree/actions/runs/34637491884/job/103388906563) | 16% (3/19) | 64 |
| `azure-windows-scale` | ossci | 12 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/34637491884/job/103388906592) | [2s](https://github.com/iree-org/iree/actions/runs/34621526530/job/103336487035) | 33% (1/3) | 12 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [2h00m](https://github.com/iree-org/iree/actions/runs/34581758865/job/103214541971) | 2026-09-11 04:27 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 14 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076980) | 2026-09-08 04:24 PDT | [2h31m](https://github.com/iree-org/iree/actions/runs/34614704603/job/103320823358) | [4h34m](https://github.com/iree-org/iree/actions/runs/34600457228/job/103269590256) | [4h44m](https://github.com/iree-org/iree/actions/runs/34600458852/job/103271494846) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 14 | 1 | [2h00m](https://github.com/iree-org/iree/actions/runs/34581758865/job/103214541971) | 2026-09-11 04:27 PDT | [2h05m](https://github.com/iree-org/iree/actions/runs/34600457106/job/103268686685) | [3h59m](https://github.com/iree-org/iree/actions/runs/34600458852/job/103271494827) | [4h40m](https://github.com/iree-org/iree/actions/runs/34600458124/job/103271388651) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 14 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077064) | 2026-09-08 04:24 PDT | [1h35m](https://github.com/iree-org/iree/actions/runs/34600457228/job/103269590177) | [3h01m](https://github.com/iree-org/iree/actions/runs/34600452293/job/103268473324) | [3h14m](https://github.com/iree-org/iree/actions/runs/34600457106/job/103268686500) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 14 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010077123) | 2026-09-08 04:24 PDT | [22m46s](https://github.com/iree-org/iree/actions/runs/34614704603/job/103320823417) | [2h52m](https://github.com/iree-org/iree/actions/runs/34600452293/job/103268473346) | [2h52m](https://github.com/iree-org/iree/actions/runs/34600452293/job/103268473346) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 13 | 0 | — | — | [15m53s](https://github.com/iree-org/iree/actions/runs/34632536823/job/103374904499) | [2h25m](https://github.com/iree-org/iree/actions/runs/34600457106/job/103268686911) | [2h31m](https://github.com/iree-org/iree/actions/runs/34600458124/job/103271388536) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 13 | 0 | — | — | [19m34s](https://github.com/iree-org/iree/actions/runs/34621526374/job/103338775178) | [2h20m](https://github.com/iree-org/iree/actions/runs/34600458124/job/103271388690) | [2h32m](https://github.com/iree-org/iree/actions/runs/34600457106/job/103268686551) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 14 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076911) | 2026-09-08 04:24 PDT | [16m04s](https://github.com/iree-org/iree/actions/runs/34599870179/job/103266393297) | [2h18m](https://github.com/iree-org/iree/actions/runs/34600457106/job/103268686619) | [2h19m](https://github.com/iree-org/iree/actions/runs/34600458124/job/103271388341) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 13 | 0 | — | — | [24m55s](https://github.com/iree-org/iree/actions/runs/34584167104/job/103241696831) | [2h15m](https://github.com/iree-org/iree/actions/runs/34600457106/job/103268686587) | [2h22m](https://github.com/iree-org/iree/actions/runs/34600458124/job/103271388604) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 13 | 0 | — | — | [28m20s](https://github.com/iree-org/iree/actions/runs/34614704603/job/103320822996) | [2h02m](https://github.com/iree-org/iree/actions/runs/34600458852/job/103271494348) | [2h16m](https://github.com/iree-org/iree/actions/runs/34600457228/job/103269590192) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 14 | 1 | [1h52m](https://github.com/iree-org/iree/actions/runs/34209494698/job/102010076982) | 2026-09-08 04:24 PDT | [15m21s](https://github.com/iree-org/iree/actions/runs/34621526374/job/103338775190) | [1h27m](https://github.com/iree-org/iree/actions/runs/34600457228/job/103269590393) | [2h09m](https://github.com/iree-org/iree/actions/runs/34600457106/job/103268686832) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 13 | 0 | — | — | [9m42s](https://github.com/iree-org/iree/actions/runs/34599870179/job/103266393637) | [1h33m](https://github.com/iree-org/iree/actions/runs/34600457228/job/103269590352) | [1h41m](https://github.com/iree-org/iree/actions/runs/34600458124/job/103271388614) | 4 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 13 | 0 | — | — | [16m24s](https://github.com/iree-org/iree/actions/runs/34600458124/job/103271388526) | [1h20m](https://github.com/iree-org/iree/actions/runs/34600452293/job/103268473289) | [2h01m](https://github.com/iree-org/iree/actions/runs/34600457106/job/103268686652) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 13 | 0 | — | — | [25m40s](https://github.com/iree-org/iree/actions/runs/34632536823/job/103374904338) | [1h15m](https://github.com/iree-org/iree/actions/runs/34600458852/job/103271494609) | [1h35m](https://github.com/iree-org/iree/actions/runs/34600458124/job/103271388665) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 13 | 0 | — | — | [24m18s](https://github.com/iree-org/iree/actions/runs/34584167104/job/103241696846) | [1h12m](https://github.com/iree-org/iree/actions/runs/34599870179/job/103266393517) | [1h14m](https://github.com/iree-org/iree/actions/runs/34600458852/job/103271494752) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 13 | 0 | — | — | [10m06s](https://github.com/iree-org/iree/actions/runs/34632536823/job/103374904153) | [1h06m](https://github.com/iree-org/iree/actions/runs/34600457228/job/103269590147) | [1h19m](https://github.com/iree-org/iree/actions/runs/34600452293/job/103268473335) | 4 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 13 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/34621526530/job/103336486408) | [27m35s](https://github.com/iree-org/iree/actions/runs/34600452261/job/103266754180) | [27m55s](https://github.com/iree-org/iree/actions/runs/34600458834/job/103267748238) | 12 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 12 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/34621526530/job/103336486743) | [26m36s](https://github.com/iree-org/iree/actions/runs/34600458834/job/103267748128) | [29m12s](https://github.com/iree-org/iree/actions/runs/34600452261/job/103266754362) | 12 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 12 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/34599870138/job/103264330238) | [24m16s](https://github.com/iree-org/iree/actions/runs/34600458834/job/103267748134) | [33m56s](https://github.com/iree-org/iree/actions/runs/34600452261/job/103266754292) | 12 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 12 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/34632536779/job/103372646799) | [24m06s](https://github.com/iree-org/iree/actions/runs/34600457305/job/103267418252) | [35m23s](https://github.com/iree-org/iree/actions/runs/34600452261/job/103266754310) | 12 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64-baremetal | `ubuntu-24.04` | 13 | 0 | — | — | [8m11s](https://github.com/iree-org/iree/actions/runs/34600458852/job/103271494481) | [19m32s](https://github.com/iree-org/iree/actions/runs/34600457228/job/103269590304) | [19m53s](https://github.com/iree-org/iree/actions/runs/34600457106/job/103268686552) | 13 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 292 | 1% (4/292) |  | 49m04s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 261 | 7% (18/261) |  | 49m07s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 214 | 1% (2/214) |  | 49m22s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 223 | 1% (3/223) |  | 51m14s ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 2h00m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h12m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h25m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h52m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 4h40m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h15m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 3h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h20m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 2h18m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h33m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
