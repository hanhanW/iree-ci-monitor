# iree-ci-monitor

_Updated: 2026-11-02 17:03 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 20 | 0 | — | — | 0 | [4h20m](https://github.com/iree-org/iree/actions/runs/41479649284/job/125403869343) | [6h19m](https://github.com/iree-org/iree/actions/runs/41465105705/job/125355364869) | 0% (0/10) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 20 | 0 | — | — | 0 | [4h25m](https://github.com/iree-org/iree/actions/runs/41469976758/job/125366482279) | [6h09m](https://github.com/iree-org/iree/actions/runs/41478148803/job/125395173194) | 0% (0/10) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 20 | 0 | — | — | 0 | [1h51m](https://github.com/iree-org/iree/actions/runs/41477608253/job/125392232426) | [5h24m](https://github.com/iree-org/iree/actions/runs/41478148803/job/125395172442) | 0% (0/10) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 10 | 0 | — | — | 0 | [4h06m](https://github.com/iree-org/iree/actions/runs/41477608253/job/125392231941) | [5h19m](https://github.com/iree-org/iree/actions/runs/41465105705/job/125355364488) | 0% (0/5) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [2h05m](https://github.com/iree-org/iree/actions/runs/41476800789/job/125390324506) | [4h13m](https://github.com/iree-org/iree/actions/runs/41478148803/job/125395172939) | 0% (0/5) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 20 | 0 | — | — | 0 | [1h17m](https://github.com/iree-org/iree/actions/runs/41479649284/job/125403868958) | [2h56m](https://github.com/iree-org/iree/actions/runs/41478148803/job/125395174675) | 0% (0/10) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [1h04m](https://github.com/iree-org/iree/actions/runs/41476800789/job/125390324589) | [2h31m](https://github.com/iree-org/iree/actions/runs/41478148803/job/125395172976) | 0% (0/5) | `shark55-ci` |
| `windows-2022` | github-hosted | 33 | 0 | — | — | 0 | [58s](https://github.com/iree-org/iree/actions/runs/41469976909/job/125362263090) | [11m12s](https://github.com/iree-org/iree/actions/runs/41465414920/job/125353362193) | 0% (0/12) | 33 |
| `ubuntu-24.04` | github-hosted | 226 | 0 | — | — | 0 | [12s](https://github.com/iree-org/iree/actions/runs/41532029623/job/125578487800) | [11m03s](https://github.com/iree-org/iree/actions/runs/41465105705/job/125355365253) | 1% (1/92) | 224 |
| `ubuntu-24.04-arm` | github-hosted | 33 | 0 | — | — | 0 | [58s](https://github.com/iree-org/iree/actions/runs/41479649200/job/125398280483) | [7m38s](https://github.com/iree-org/iree/actions/runs/41465414920/job/125353361697) | 0% (0/12) | 33 |
| `macos-15` | github-hosted | 33 | 0 | — | — | 0 | [1m08s](https://github.com/iree-org/iree/actions/runs/41476800913/job/125384621239) | [6m53s](https://github.com/iree-org/iree/actions/runs/41465414920/job/125353361690) | 0% (0/12) | 33 |
| `azure-windows-scale` | ossci | 11 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/41478840413/job/125392092733) | [3m59s](https://github.com/iree-org/iree/actions/runs/41477608292/job/125388596915) | 0% (0/4) | 10 |
| `azure-linux-scale` | ossci | 69 | 0 | — | — | 0 | [14s](https://github.com/iree-org/iree/actions/runs/41479649200/job/125398280491) | [3m00s](https://github.com/iree-org/iree/actions/runs/41478840413/job/125392092271) | 0% (0/28) | 66 |
| `ubuntu-latest` | github-hosted | 22 | 0 | — | — | 0 | [29s](https://github.com/iree-org/iree/actions/runs/41478840745/job/125391483953) | [1m42s](https://github.com/iree-org/iree/actions/runs/41478148340/job/125389064204) | 0% (0/13) | 22 |
| `Linux,X64,iree-w7900` | self-hosted | 10 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 10 | 0 | — | — | [5h01m](https://github.com/iree-org/iree/actions/runs/41476800789/job/125390324979) | [6h35m](https://github.com/iree-org/iree/actions/runs/41478840473/job/125398159595) | [6h35m](https://github.com/iree-org/iree/actions/runs/41478840473/job/125398159595) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 10 | 0 | — | — | [3h00m](https://github.com/iree-org/iree/actions/runs/41477608253/job/125392232585) | [6h19m](https://github.com/iree-org/iree/actions/runs/41465105705/job/125355364869) | [6h19m](https://github.com/iree-org/iree/actions/runs/41465105705/job/125355364869) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [3h23m](https://github.com/iree-org/iree/actions/runs/41477608253/job/125392232128) | [6h15m](https://github.com/iree-org/iree/actions/runs/41478840473/job/125398159307) | [6h15m](https://github.com/iree-org/iree/actions/runs/41478840473/job/125398159307) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [4h14m](https://github.com/iree-org/iree/actions/runs/41469976758/job/125366482835) | [5h55m](https://github.com/iree-org/iree/actions/runs/41465105705/job/125355365094) | [5h55m](https://github.com/iree-org/iree/actions/runs/41465105705/job/125355365094) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [4h31m](https://github.com/iree-org/iree/actions/runs/41477608253/job/125392232230) | [5h53m](https://github.com/iree-org/iree/actions/runs/41478840473/job/125398159081) | [5h53m](https://github.com/iree-org/iree/actions/runs/41478840473/job/125398159081) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [1h38m](https://github.com/iree-org/iree/actions/runs/41477608253/job/125392232492) | [5h24m](https://github.com/iree-org/iree/actions/runs/41478148803/job/125395172442) | [5h24m](https://github.com/iree-org/iree/actions/runs/41478148803/job/125395172442) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 10 | 0 | — | — | [4h06m](https://github.com/iree-org/iree/actions/runs/41477608253/job/125392231941) | [5h19m](https://github.com/iree-org/iree/actions/runs/41465105705/job/125355364488) | [5h19m](https://github.com/iree-org/iree/actions/runs/41465105705/job/125355364488) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 10 | 0 | — | — | [2h05m](https://github.com/iree-org/iree/actions/runs/41476800789/job/125390324506) | [4h13m](https://github.com/iree-org/iree/actions/runs/41478148803/job/125395172939) | [4h13m](https://github.com/iree-org/iree/actions/runs/41478148803/job/125395172939) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [2h18m](https://github.com/iree-org/iree/actions/runs/41476800789/job/125390324642) | [3h30m](https://github.com/iree-org/iree/actions/runs/41478840473/job/125398159335) | [3h30m](https://github.com/iree-org/iree/actions/runs/41478840473/job/125398159335) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 10 | 0 | — | — | [1h04m](https://github.com/iree-org/iree/actions/runs/41476800789/job/125390324589) | [2h31m](https://github.com/iree-org/iree/actions/runs/41478148803/job/125395172976) | [2h31m](https://github.com/iree-org/iree/actions/runs/41478148803/job/125395172976) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [1h03m](https://github.com/iree-org/iree/actions/runs/41469976758/job/125366482353) | [1h42m](https://github.com/iree-org/iree/actions/runs/41478840473/job/125398159029) | [1h42m](https://github.com/iree-org/iree/actions/runs/41478840473/job/125398159029) | 2 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 11 | 0 | — | — | [1m41s](https://github.com/iree-org/iree/actions/runs/41476998110/job/125385674799) | [16m52s](https://github.com/iree-org/iree/actions/runs/41478840413/job/125392091505) | [16m52s](https://github.com/iree-org/iree/actions/runs/41478840413/job/125392091505) | 11 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 11 | 0 | — | — | [1m10s](https://github.com/iree-org/iree/actions/runs/41476800913/job/125384620919) | [16m44s](https://github.com/iree-org/iree/actions/runs/41478840413/job/125392091887) | [16m44s](https://github.com/iree-org/iree/actions/runs/41478840413/job/125392091887) | 11 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 11 | 0 | — | — | [2m04s](https://github.com/iree-org/iree/actions/runs/41469976909/job/125362262783) | [15m46s](https://github.com/iree-org/iree/actions/runs/41478840413/job/125392091654) | [15m46s](https://github.com/iree-org/iree/actions/runs/41478840413/job/125392091654) | 11 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 10 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/41479649284/job/125403868523) | [15m06s](https://github.com/iree-org/iree/actions/runs/41477608253/job/125392232233) | [15m06s](https://github.com/iree-org/iree/actions/runs/41477608253/job/125392232233) | 10 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 11 | 0 | — | — | [1m25s](https://github.com/iree-org/iree/actions/runs/41476998110/job/125385675272) | [14m55s](https://github.com/iree-org/iree/actions/runs/41478840413/job/125392091688) | [14m55s](https://github.com/iree-org/iree/actions/runs/41478840413/job/125392091688) | 11 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 11 | 0 | — | — | [27s](https://github.com/iree-org/iree/actions/runs/41476800913/job/125384620583) | [13m22s](https://github.com/iree-org/iree/actions/runs/41478840413/job/125392091259) | [13m22s](https://github.com/iree-org/iree/actions/runs/41478840413/job/125392091259) | 11 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 10 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/41469976758/job/125366482417) | [11m32s](https://github.com/iree-org/iree/actions/runs/41465105705/job/125355364853) | [11m32s](https://github.com/iree-org/iree/actions/runs/41465105705/job/125355364853) | 10 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 11 | 0 | — | — | [1m39s](https://github.com/iree-org/iree/actions/runs/41476998110/job/125385675048) | [11m28s](https://github.com/iree-org/iree/actions/runs/41465414920/job/125353362200) | [11m28s](https://github.com/iree-org/iree/actions/runs/41465414920/job/125353362200) | 11 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 11 | 0 | — | — | [42s](https://github.com/iree-org/iree/actions/runs/41469976909/job/125362262665) | [11m22s](https://github.com/iree-org/iree/actions/runs/41465414920/job/125353361807) | [11m22s](https://github.com/iree-org/iree/actions/runs/41465414920/job/125353361807) | 11 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 399 | 2% (8/399) |  | 56m15s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 336 | 2% (7/336) |  | 1h00m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 2h31m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 6h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 4h13m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 5h24m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 5h19m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 6h19m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h56m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
