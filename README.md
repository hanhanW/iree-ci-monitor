# iree-ci-monitor

_Updated: 2026-05-19 18:21 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-w7900` | self-hosted | 18 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926441) | 2026-05-19 06:28 PDT | 0 | [11m24s](https://github.com/iree-org/iree/actions/runs/26113983494/job/76800199303) | [1h12m](https://github.com/iree-org/iree/actions/runs/26107445002/job/76776630258) | 25% (1/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 34 | 0 | — | — | 0 | [32m46s](https://github.com/iree-org/iree/actions/runs/26125144668/job/76838052937) | [1h09m](https://github.com/iree-org/iree/actions/runs/26113983494/job/76800199606) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 17 | 0 | — | — | 0 | [44m55s](https://github.com/iree-org/iree/actions/runs/26107952538/job/76778397349) | [1h07m](https://github.com/iree-org/iree/actions/runs/26107445002/job/76776631041) | 0% (0/4) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 34 | 0 | — | — | 0 | [23m46s](https://github.com/iree-org/iree/actions/runs/26125144668/job/76838053030) | [1h01m](https://github.com/iree-org/iree/actions/runs/26107967664/job/76779040236) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 17 | 0 | — | — | 0 | [15m39s](https://github.com/iree-org/iree/actions/runs/26113936149/job/76799907382) | [1h01m](https://github.com/iree-org/iree/actions/runs/26120458110/job/76822309760) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 17 | 0 | — | — | 0 | [28m26s](https://github.com/iree-org/iree/actions/runs/26123500861/job/76832752987) | [58m05s](https://github.com/iree-org/iree/actions/runs/26107445002/job/76776630532) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 34 | 0 | — | — | 0 | [16m45s](https://github.com/iree-org/iree/actions/runs/26125144668/job/76838053019) | [51m47s](https://github.com/iree-org/iree/actions/runs/26119595605/job/76819393694) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 34 | 0 | — | — | 0 | [8m50s](https://github.com/iree-org/iree/actions/runs/26118284133/job/76814670598) | [30m22s](https://github.com/iree-org/iree/actions/runs/26113936149/job/76799907373) | 12% (1/8) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 17 | 0 | — | — | 0 | [12m31s](https://github.com/iree-org/iree/actions/runs/26107952538/job/76778397447) | [28m34s](https://github.com/iree-org/iree/actions/runs/26120458110/job/76822309784) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 17 | 0 | — | — | 0 | [5m45s](https://github.com/iree-org/iree/actions/runs/26118327534/job/76814793624) | [27m00s](https://github.com/iree-org/iree/actions/runs/26107967664/job/76779040032) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 18 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926511) | 2026-05-19 06:28 PDT | 0 | [15m54s](https://github.com/iree-org/iree/actions/runs/26113836080/job/76799318735) | [25m13s](https://github.com/iree-org/iree/actions/runs/26113936149/job/76799907280) | 0% (0/4) | `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 17 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26119595605/job/76819393474) | [15m35s](https://github.com/iree-org/iree/actions/runs/26113936149/job/76799907425) | 0% (0/4) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 68 | 0 | — | — | 0 | [14s](https://github.com/iree-org/iree/actions/runs/26110226769/job/76786400353) | [12m36s](https://github.com/iree-org/iree/actions/runs/26113983494/job/76800199450) | 0% (0/16) | 68 |
| `ubuntu-24.04` | github-hosted | 366 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26119595595/job/76824780885) | [3m10s](https://github.com/iree-org/iree/actions/runs/26113699130/job/76798943401) | 13% (10/75) | 366 |
| `windows-2022` | github-hosted | 60 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/26113699129/job/76797728129) | [2m21s](https://github.com/iree-org/iree/actions/runs/26113936011/job/76799810674) | 0% (0/12) | 60 |
| `ubuntu-24.04-arm` | github-hosted | 60 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/26118257723/job/76813167284) | [2m06s](https://github.com/iree-org/iree/actions/runs/26111587437/job/76790465781) | 0% (0/12) | 60 |
| `macos-14` | github-hosted | 60 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/26120458044/job/76820804815) | [1m53s](https://github.com/iree-org/iree/actions/runs/26113936011/job/76799810614) | 0% (0/12) | 60 |
| `ubuntu-latest` | github-hosted | 69 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26120455911/job/76820766443) | [1m41s](https://github.com/iree-org/iree/actions/runs/26113980327/job/76798281937) | 0% (0/12) | 69 |
| `azure-linux-scale` | ossci | 103 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/26118327443/job/76813697838) | [1m12s](https://github.com/iree-org/iree/actions/runs/26119595595/job/76817781082) | 0% (0/24) | 103 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 17 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26112994086/job/76796896532) | [3s](https://github.com/iree-org/iree/actions/runs/26107967664/job/76779040033) | 0% (0/4) | 17 |
| `azure-windows-scale` | ossci | 20 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26110036693/job/76784544079) | [2s](https://github.com/iree-org/iree/actions/runs/26118284129/job/76813387859) | 25% (1/4) | 20 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926441) | 2026-05-19 06:28 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `new-lds-promotion` | pull_request |
| [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926511) | 2026-05-19 06:28 PDT | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `new-lds-promotion` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 17 | 0 | — | — | [32m46s](https://github.com/iree-org/iree/actions/runs/26125144668/job/76838052937) | [1h35m](https://github.com/iree-org/iree/actions/runs/26107952538/job/76778397381) | [1h36m](https://github.com/iree-org/iree/actions/runs/26107967664/job/76779040341) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 18 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926441) | 2026-05-19 06:28 PDT | [11m24s](https://github.com/iree-org/iree/actions/runs/26113983494/job/76800199303) | [1h12m](https://github.com/iree-org/iree/actions/runs/26107445002/job/76776630258) | [1h22m](https://github.com/iree-org/iree/actions/runs/26107967664/job/76779040143) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 17 | 0 | — | — | [44m55s](https://github.com/iree-org/iree/actions/runs/26107952538/job/76778397349) | [1h07m](https://github.com/iree-org/iree/actions/runs/26107445002/job/76776631041) | [1h19m](https://github.com/iree-org/iree/actions/runs/26107967664/job/76779039996) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 17 | 0 | — | — | [39m45s](https://github.com/iree-org/iree/actions/runs/26107445002/job/76776630741) | [1h05m](https://github.com/iree-org/iree/actions/runs/26119595605/job/76819393365) | [1h09m](https://github.com/iree-org/iree/actions/runs/26113983494/job/76800199606) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 17 | 0 | — | — | [15m39s](https://github.com/iree-org/iree/actions/runs/26113936149/job/76799907382) | [1h01m](https://github.com/iree-org/iree/actions/runs/26120458110/job/76822309760) | [1h14m](https://github.com/iree-org/iree/actions/runs/26107445002/job/76776630930) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 17 | 0 | — | — | [28m26s](https://github.com/iree-org/iree/actions/runs/26123500861/job/76832752987) | [58m05s](https://github.com/iree-org/iree/actions/runs/26107445002/job/76776630532) | [1h17m](https://github.com/iree-org/iree/actions/runs/26107967664/job/76779040464) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 17 | 0 | — | — | [14m18s](https://github.com/iree-org/iree/actions/runs/26110226769/job/76786400572) | [51m47s](https://github.com/iree-org/iree/actions/runs/26119595605/job/76819393694) | [56m38s](https://github.com/iree-org/iree/actions/runs/26107967664/job/76779040224) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 17 | 0 | — | — | [21m38s](https://github.com/iree-org/iree/actions/runs/26113699130/job/76798943459) | [48m55s](https://github.com/iree-org/iree/actions/runs/26118327534/job/76814793595) | [1h15m](https://github.com/iree-org/iree/actions/runs/26107445002/job/76776630803) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 17 | 0 | — | — | [23m46s](https://github.com/iree-org/iree/actions/runs/26125144668/job/76838053030) | [43m51s](https://github.com/iree-org/iree/actions/runs/26119595605/job/76819393450) | [1h01m](https://github.com/iree-org/iree/actions/runs/26107967664/job/76779040236) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 17 | 0 | — | — | [21m24s](https://github.com/iree-org/iree/actions/runs/26107952538/job/76778397497) | [40m56s](https://github.com/iree-org/iree/actions/runs/26113699130/job/76798943438) | [1h07m](https://github.com/iree-org/iree/actions/runs/26107445002/job/76776630703) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 17 | 0 | — | — | [9m29s](https://github.com/iree-org/iree/actions/runs/26111579315/job/76791523801) | [30m22s](https://github.com/iree-org/iree/actions/runs/26113936149/job/76799907373) | [42m32s](https://github.com/iree-org/iree/actions/runs/26113836080/job/76799318834) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 17 | 0 | — | — | [12m31s](https://github.com/iree-org/iree/actions/runs/26107952538/job/76778397447) | [28m34s](https://github.com/iree-org/iree/actions/runs/26120458110/job/76822309784) | [49m56s](https://github.com/iree-org/iree/actions/runs/26107967664/job/76779040244) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 17 | 0 | — | — | [5m45s](https://github.com/iree-org/iree/actions/runs/26118327534/job/76814793624) | [27m00s](https://github.com/iree-org/iree/actions/runs/26107967664/job/76779040032) | [27m22s](https://github.com/iree-org/iree/actions/runs/26113983494/job/76800199540) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 18 | 1 | [21m35s](https://github.com/iree-org/iree/actions/runs/26098633552/job/76744926511) | 2026-05-19 06:28 PDT | [15m54s](https://github.com/iree-org/iree/actions/runs/26113836080/job/76799318735) | [25m13s](https://github.com/iree-org/iree/actions/runs/26113936149/job/76799907280) | [56m04s](https://github.com/iree-org/iree/actions/runs/26107967664/job/76779040192) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 17 | 0 | — | — | [5m32s](https://github.com/iree-org/iree/actions/runs/26107952538/job/76778397321) | [20m33s](https://github.com/iree-org/iree/actions/runs/26118327534/job/76814793575) | [32m51s](https://github.com/iree-org/iree/actions/runs/26107967664/job/76779040222) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 17 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26119595605/job/76819393474) | [15m35s](https://github.com/iree-org/iree/actions/runs/26113936149/job/76799907425) | [29m18s](https://github.com/iree-org/iree/actions/runs/26113836080/job/76799318907) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 17 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/26110226769/job/76786400307) | [8m13s](https://github.com/iree-org/iree/actions/runs/26118327534/job/76814793427) | [13m32s](https://github.com/iree-org/iree/actions/runs/26113836080/job/76799318697) | 17 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 17 | 0 | — | — | [22s](https://github.com/iree-org/iree/actions/runs/26123500861/job/76832753004) | [6m23s](https://github.com/iree-org/iree/actions/runs/26113936149/job/76799907393) | [13m29s](https://github.com/iree-org/iree/actions/runs/26113983494/job/76800199556) | 17 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 17 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/26112994086/job/76796896862) | [6m14s](https://github.com/iree-org/iree/actions/runs/26113936149/job/76799907436) | [12m36s](https://github.com/iree-org/iree/actions/runs/26113983494/job/76800199450) | 17 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 17 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/26125144668/job/76838052769) | [5m02s](https://github.com/iree-org/iree/actions/runs/26113983494/job/76800199449) | [5m35s](https://github.com/iree-org/iree/actions/runs/26113936149/job/76799907408) | 17 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 776 | 2% (13/775) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 681 | 5% (35/680) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 644 | 1% (6/643) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 630 | 0% (1/629) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 215 | 0% (0/215) |  | 4h00m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h12m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h07m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
