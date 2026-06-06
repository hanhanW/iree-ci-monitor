# iree-ci-monitor

_Updated: 2026-06-05 18:19 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 40 | 0 | — | — | 0 | [2h23m](https://github.com/iree-org/iree/actions/runs/27023525599/job/79760765654) | [3h33m](https://github.com/iree-org/iree/actions/runs/27033986778/job/79795497465) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 20 | 0 | — | — | 0 | [2h00m](https://github.com/iree-org/iree/actions/runs/27033985659/job/79794854504) | [2h57m](https://github.com/iree-org/iree/actions/runs/27023531359/job/79759327671) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 20 | 0 | — | — | 0 | [53m03s](https://github.com/iree-org/iree/actions/runs/27033983028/job/79795131601) | [2h30m](https://github.com/iree-org/iree/actions/runs/27033985491/job/79794962090) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 20 | 0 | — | — | 0 | [41m27s](https://github.com/iree-org/iree/actions/runs/27033981777/job/79794592875) | [2h28m](https://github.com/iree-org/iree/actions/runs/27033986778/job/79795497338) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 40 | 0 | — | — | 0 | [1h12m](https://github.com/iree-org/iree/actions/runs/27023528986/job/79761680900) | [2h19m](https://github.com/iree-org/iree/actions/runs/27033981777/job/79794592993) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 40 | 0 | — | — | 0 | [58m57s](https://github.com/iree-org/iree/actions/runs/27033985659/job/79794854333) | [2h10m](https://github.com/iree-org/iree/actions/runs/27023528056/job/79761620005) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 20 | 0 | — | — | 0 | [47m26s](https://github.com/iree-org/iree/actions/runs/27023528986/job/79761680748) | [2h07m](https://github.com/iree-org/iree/actions/runs/27033986778/job/79795497441) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 20 | 0 | — | — | 0 | [1h18m](https://github.com/iree-org/iree/actions/runs/27033985491/job/79794962207) | [2h02m](https://github.com/iree-org/iree/actions/runs/27033986778/job/79795497252) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 20 | 0 | — | — | 0 | [1h03m](https://github.com/iree-org/iree/actions/runs/27023525599/job/79760765590) | [1h51m](https://github.com/iree-org/iree/actions/runs/27033986778/job/79795497210) | 0% (0/3) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 40 | 0 | — | — | 0 | [19m59s](https://github.com/iree-org/iree/actions/runs/27033981777/job/79794592992) | [1h18m](https://github.com/iree-org/iree/actions/runs/27023528056/job/79761620006) | 17% (1/6) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 20 | 0 | — | — | 0 | [35m00s](https://github.com/iree-org/iree/actions/runs/27023528056/job/79761620030) | [1h13m](https://github.com/iree-org/iree/actions/runs/27023530674/job/79760843672) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 20 | 0 | — | — | 0 | [16m02s](https://github.com/iree-org/iree/actions/runs/27023528056/job/79761619842) | [57m04s](https://github.com/iree-org/iree/actions/runs/27033985491/job/79794962223) | 0% (0/3) | `iree-mi308-1` |
| `ubuntu-24.04` | github-hosted | 422 | 0 | — | — | 0 | [4m55s](https://github.com/iree-org/iree/actions/runs/27023526973/job/79757498783) | [26m29s](https://github.com/iree-org/iree/actions/runs/27033983037/job/79793620241) | 4% (2/56) | 397 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 80 | 0 | — | — | 0 | [3m44s](https://github.com/iree-org/iree/actions/runs/27023525599/job/79760765539) | [20m03s](https://github.com/iree-org/iree/actions/runs/27033984323/job/79795862181) | 0% (0/12) | 77 |
| `windows-2022` | github-hosted | 54 | 0 | — | — | 0 | [1m19s](https://github.com/iree-org/iree/actions/runs/27023528060/job/79758410567) | [16m50s](https://github.com/iree-org/iree/actions/runs/27033981764/job/79793227819) | 0% (0/9) | 54 |
| `macos-14` | github-hosted | 54 | 0 | — | — | 0 | [1m44s](https://github.com/iree-org/iree/actions/runs/27023528060/job/79758410391) | [13m41s](https://github.com/iree-org/iree/actions/runs/27023528969/job/79762646860) | 0% (0/9) | 54 |
| `ubuntu-24.04-arm` | github-hosted | 54 | 0 | — | — | 0 | [1m23s](https://github.com/iree-org/iree/actions/runs/27023530663/job/79760291355) | [12m59s](https://github.com/iree-org/iree/actions/runs/27023528969/job/79762646955) | 0% (0/9) | 54 |
| `azure-windows-scale` | ossci | 18 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/27028531761/job/79774695313) | [8m59s](https://github.com/iree-org/iree/actions/runs/27033986765/job/79793530186) | 0% (0/3) | 18 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 20 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27028531757/job/79776051237) | [6m30s](https://github.com/iree-org/iree/actions/runs/27033983028/job/79795131575) | 0% (0/3) | 20 |
| `ubuntu-latest` | github-hosted | 30 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27033907341/job/79792943270) | [2m56s](https://github.com/iree-org/iree/actions/runs/27026656337/job/79768299164) | 0% (0/9) | 30 |
| `azure-linux-scale` | ossci | 93 | 0 | — | — | 0 | [13s](https://github.com/iree-org/iree/actions/runs/27028531761/job/79774695326) | [1m44s](https://github.com/iree-org/iree/actions/runs/27033983028/job/79793564509) | 0% (0/18) | 93 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 20 | 0 | — | — | [2h38m](https://github.com/iree-org/iree/actions/runs/27033985491/job/79794962240) | [3h35m](https://github.com/iree-org/iree/actions/runs/27033984323/job/79795862166) | [3h47m](https://github.com/iree-org/iree/actions/runs/27026596957/job/79769864321) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 20 | 0 | — | — | [2h04m](https://github.com/iree-org/iree/actions/runs/27033981777/job/79794592975) | [3h33m](https://github.com/iree-org/iree/actions/runs/27033984323/job/79795862243) | [3h33m](https://github.com/iree-org/iree/actions/runs/27033986778/job/79795497465) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 20 | 0 | — | — | [2h00m](https://github.com/iree-org/iree/actions/runs/27033985659/job/79794854504) | [2h57m](https://github.com/iree-org/iree/actions/runs/27023531359/job/79759327671) | [3h02m](https://github.com/iree-org/iree/actions/runs/27023123683/job/79757793194) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 20 | 0 | — | — | [53m03s](https://github.com/iree-org/iree/actions/runs/27033983028/job/79795131601) | [2h30m](https://github.com/iree-org/iree/actions/runs/27033985491/job/79794962090) | [3h03m](https://github.com/iree-org/iree/actions/runs/27033981777/job/79794592928) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 20 | 0 | — | — | [41m27s](https://github.com/iree-org/iree/actions/runs/27033981777/job/79794592875) | [2h28m](https://github.com/iree-org/iree/actions/runs/27033986778/job/79795497338) | [2h38m](https://github.com/iree-org/iree/actions/runs/27033985659/job/79794854180) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 20 | 0 | — | — | [1h07m](https://github.com/iree-org/iree/actions/runs/27023528986/job/79761680795) | [2h19m](https://github.com/iree-org/iree/actions/runs/27033981777/job/79794592993) | [2h29m](https://github.com/iree-org/iree/actions/runs/27033984323/job/79795862238) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 20 | 0 | — | — | [50m21s](https://github.com/iree-org/iree/actions/runs/27023530674/job/79760843739) | [2h16m](https://github.com/iree-org/iree/actions/runs/27023528986/job/79761680973) | [2h20m](https://github.com/iree-org/iree/actions/runs/27023123683/job/79757793252) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 20 | 0 | — | — | [1h12m](https://github.com/iree-org/iree/actions/runs/27023528986/job/79761680900) | [2h14m](https://github.com/iree-org/iree/actions/runs/27033986778/job/79795497292) | [2h28m](https://github.com/iree-org/iree/actions/runs/27033983028/job/79795131566) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 20 | 0 | — | — | [47m26s](https://github.com/iree-org/iree/actions/runs/27023528986/job/79761680748) | [2h07m](https://github.com/iree-org/iree/actions/runs/27033986778/job/79795497441) | [2h26m](https://github.com/iree-org/iree/actions/runs/27033983028/job/79795131704) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 20 | 0 | — | — | [1h18m](https://github.com/iree-org/iree/actions/runs/27033985491/job/79794962207) | [2h02m](https://github.com/iree-org/iree/actions/runs/27033986778/job/79795497252) | [2h22m](https://github.com/iree-org/iree/actions/runs/27033984323/job/79795862077) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 20 | 0 | — | — | [1h03m](https://github.com/iree-org/iree/actions/runs/27023525599/job/79760765590) | [1h51m](https://github.com/iree-org/iree/actions/runs/27033986778/job/79795497210) | [2h09m](https://github.com/iree-org/iree/actions/runs/27033984323/job/79795862096) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 20 | 0 | — | — | [1h04m](https://github.com/iree-org/iree/actions/runs/27023531359/job/79759327760) | [1h50m](https://github.com/iree-org/iree/actions/runs/27033983028/job/79795131807) | [1h51m](https://github.com/iree-org/iree/actions/runs/27033986778/job/79795497395) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 20 | 0 | — | — | [30m03s](https://github.com/iree-org/iree/actions/runs/27033984323/job/79795862073) | [1h18m](https://github.com/iree-org/iree/actions/runs/27023528056/job/79761620006) | [1h59m](https://github.com/iree-org/iree/actions/runs/27023528986/job/79761680921) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 20 | 0 | — | — | [35m00s](https://github.com/iree-org/iree/actions/runs/27023528056/job/79761620030) | [1h13m](https://github.com/iree-org/iree/actions/runs/27023530674/job/79760843672) | [1h26m](https://github.com/iree-org/iree/actions/runs/27033983028/job/79795131611) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 20 | 0 | — | — | [16m41s](https://github.com/iree-org/iree/actions/runs/27033983028/job/79795131639) | [1h02m](https://github.com/iree-org/iree/actions/runs/27023528986/job/79761680740) | [1h48m](https://github.com/iree-org/iree/actions/runs/27023527223/job/79760147781) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 20 | 0 | — | — | [16m02s](https://github.com/iree-org/iree/actions/runs/27023528056/job/79761619842) | [57m04s](https://github.com/iree-org/iree/actions/runs/27033985491/job/79794962223) | [1h12m](https://github.com/iree-org/iree/actions/runs/27023530674/job/79760843749) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 18 | 0 | — | — | [10m02s](https://github.com/iree-org/iree/actions/runs/27023531383/job/79760529191) | [33m03s](https://github.com/iree-org/iree/actions/runs/27033984206/job/79793464675) | [33m13s](https://github.com/iree-org/iree/actions/runs/27033981764/job/79793227898) | 18 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 27 | 0 | — | — | [9m08s](https://github.com/iree-org/iree/actions/runs/27023530663/job/79760291155) | [32m56s](https://github.com/iree-org/iree/actions/runs/27033984206/job/79793464553) | [34m27s](https://github.com/iree-org/iree/actions/runs/27033981764/job/79793227969) | 18 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 18 | 0 | — | — | [14m57s](https://github.com/iree-org/iree/actions/runs/27023893358/job/79762140750) | [32m48s](https://github.com/iree-org/iree/actions/runs/27033981764/job/79793227833) | [32m48s](https://github.com/iree-org/iree/actions/runs/27033984206/job/79793464644) | 18 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 18 | 0 | — | — | [12m40s](https://github.com/iree-org/iree/actions/runs/27023528969/job/79762646841) | [29m16s](https://github.com/iree-org/iree/actions/runs/27033981764/job/79793227795) | [30m39s](https://github.com/iree-org/iree/actions/runs/27023528060/job/79758410746) | 18 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 310 | 1% (2/310) |  | 2h25m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 262 | 4% (10/262) |  | 3h30m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 238 | 0% (1/238) |  | 3h32m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 222 | 0% (0/222) |  | 3h34m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 71 | 0% (0/71) |  | 5h07m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h13m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h19m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h51m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 3h33m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h30m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h28m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 2h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 2h57m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h10m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 2h07m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h18m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
