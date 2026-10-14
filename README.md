# iree-ci-monitor

_Updated: 2026-10-14 05:00 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 16 | 0 | — | — | 0 | [58m17s](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742875446) | [1h52m](https://github.com/iree-org/iree/actions/runs/38522002606/job/115722985127) | 0% (0/6) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 16 | 0 | — | — | 0 | [52m55s](https://github.com/iree-org/iree/actions/runs/38527942546/job/115735218163) | [1h41m](https://github.com/iree-org/iree/actions/runs/38522002606/job/115722985068) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 16 | 0 | — | — | 0 | [24m14s](https://github.com/iree-org/iree/actions/runs/38523581553/job/115721079023) | [1h33m](https://github.com/iree-org/iree/actions/runs/38527942546/job/115735218477) | 0% (0/6) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 8 | 0 | — | — | 0 | [21m10s](https://github.com/iree-org/iree/actions/runs/38522002606/job/115722984917) | [1h04m](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742875262) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [24m42s](https://github.com/iree-org/iree/actions/runs/38529169306/job/115739584160) | [47m36s](https://github.com/iree-org/iree/actions/runs/38525482782/job/115727101512) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [29m22s](https://github.com/iree-org/iree/actions/runs/38523581553/job/115721078889) | [44m31s](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742875670) | 0% (0/3) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 16 | 0 | — | — | 0 | [9m54s](https://github.com/iree-org/iree/actions/runs/38514940142/job/115693837865) | [40m23s](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742875736) | 0% (0/6) | `shark55-ci`, `shark75-ci` |
| `windows-2022` | github-hosted | 29 | 0 | — | — | 0 | [1m06s](https://github.com/iree-org/iree/actions/runs/38515699622/job/115693931763) | [3m12s](https://github.com/iree-org/iree/actions/runs/38530100758/job/115740105162) | 0% (0/9) | 29 |
| `ubuntu-24.04-arm` | github-hosted | 30 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/38522002640/job/115719921827) | [2m25s](https://github.com/iree-org/iree/actions/runs/38515699622/job/115693931786) | 11% (1/9) | 29 |
| `macos-15` | github-hosted | 30 | 0 | — | — | 1 | [10s](https://github.com/iree-org/iree/actions/runs/38522002640/job/115719921890) | [1m56s](https://github.com/iree-org/iree/actions/runs/38530100758/job/115740105160) | 0% (0/9) | 30 |
| `ubuntu-latest` | github-hosted | 31 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/38523572518/job/115718622058) | [1m28s](https://github.com/iree-org/iree/actions/runs/38530094390/job/115739645021) | 0% (0/10) | 31 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m26s](https://github.com/iree-org/iree/actions/runs/38542595656/job/115780762052) | [1m26s](https://github.com/iree-org/iree/actions/runs/38542595656/job/115780762052) | 100% (1/1) | 1 |
| `ubuntu-24.04` | github-hosted | 193 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/38527942464/job/115733264424) | [1m18s](https://github.com/iree-org/iree/actions/runs/38522002606/job/115722984960) | 2% (1/62) | 187 |
| `azure-linux-scale` | ossci | 59 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/38529169445/job/115736670092) | [9s](https://github.com/iree-org/iree/actions/runs/38522002640/job/115719922241) | 0% (0/23) | 59 |
| `azure-windows-scale` | ossci | 9 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/38527836035/job/115732377764) | [1s](https://github.com/iree-org/iree/actions/runs/38530100758/job/115740105306) | 0% (0/3) | 9 |
| `Linux,X64,iree-w7900` | self-hosted | 8 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 8 | 0 | — | — | [56m00s](https://github.com/iree-org/iree/actions/runs/38529169306/job/115739584229) | [2h00m](https://github.com/iree-org/iree/actions/runs/38522002606/job/115722984956) | [2h00m](https://github.com/iree-org/iree/actions/runs/38522002606/job/115722984956) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [1h17m](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742875484) | [1h54m](https://github.com/iree-org/iree/actions/runs/38525482782/job/115727101932) | [1h54m](https://github.com/iree-org/iree/actions/runs/38525482782/job/115727101932) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 8 | 0 | — | — | [1h09m](https://github.com/iree-org/iree/actions/runs/38529169306/job/115739584234) | [1h52m](https://github.com/iree-org/iree/actions/runs/38522002606/job/115722985127) | [1h52m](https://github.com/iree-org/iree/actions/runs/38522002606/job/115722985127) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 8 | 0 | — | — | [53m16s](https://github.com/iree-org/iree/actions/runs/38525482782/job/115727101976) | [1h46m](https://github.com/iree-org/iree/actions/runs/38527942546/job/115735218542) | [1h46m](https://github.com/iree-org/iree/actions/runs/38527942546/job/115735218542) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 8 | 0 | — | — | [13m27s](https://github.com/iree-org/iree/actions/runs/38519841686/job/115710005310) | [1h33m](https://github.com/iree-org/iree/actions/runs/38527942546/job/115735218477) | [1h33m](https://github.com/iree-org/iree/actions/runs/38527942546/job/115735218477) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 8 | 0 | — | — | [21m10s](https://github.com/iree-org/iree/actions/runs/38522002606/job/115722984917) | [1h04m](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742875262) | [1h04m](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742875262) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [28m16s](https://github.com/iree-org/iree/actions/runs/38529169306/job/115739584348) | [55m50s](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742875775) | [55m50s](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742875775) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [17m51s](https://github.com/iree-org/iree/actions/runs/38522002606/job/115722984885) | [49m06s](https://github.com/iree-org/iree/actions/runs/38527942546/job/115735218221) | [49m06s](https://github.com/iree-org/iree/actions/runs/38527942546/job/115735218221) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 8 | 0 | — | — | [24m42s](https://github.com/iree-org/iree/actions/runs/38529169306/job/115739584160) | [47m36s](https://github.com/iree-org/iree/actions/runs/38525482782/job/115727101512) | [47m36s](https://github.com/iree-org/iree/actions/runs/38525482782/job/115727101512) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 8 | 0 | — | — | [29m22s](https://github.com/iree-org/iree/actions/runs/38523581553/job/115721078889) | [44m31s](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742875670) | [44m31s](https://github.com/iree-org/iree/actions/runs/38530100825/job/115742875670) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [9m08s](https://github.com/iree-org/iree/actions/runs/38529169306/job/115739584082) | [31m12s](https://github.com/iree-org/iree/actions/runs/38525482782/job/115727101923) | [31m12s](https://github.com/iree-org/iree/actions/runs/38525482782/job/115727101923) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 9 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/38523572518/job/115718622058) | [3m43s](https://github.com/iree-org/iree/actions/runs/38530094390/job/115739645401) | [3m43s](https://github.com/iree-org/iree/actions/runs/38530094390/job/115739645401) | 9 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 9 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/38522002640/job/115719921827) | [3m19s](https://github.com/iree-org/iree/actions/runs/38530100758/job/115740105271) | [3m19s](https://github.com/iree-org/iree/actions/runs/38530100758/job/115740105271) | 9 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 9 | 0 | — | — | [39s](https://github.com/iree-org/iree/actions/runs/38529169445/job/115736669312) | [3m19s](https://github.com/iree-org/iree/actions/runs/38530100758/job/115740105276) | [3m19s](https://github.com/iree-org/iree/actions/runs/38530100758/job/115740105276) | 9 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: tracy | `windows-2022` | 9 | 0 | — | — | [37s](https://github.com/iree-org/iree/actions/runs/38527836035/job/115732377797) | [3m12s](https://github.com/iree-org/iree/actions/runs/38530100758/job/115740105162) | [3m12s](https://github.com/iree-org/iree/actions/runs/38530100758/job/115740105162) | 9 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 9 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/38530100825/job/115740167969) | [3m01s](https://github.com/iree-org/iree/actions/runs/38519841686/job/115706847702) | [3m01s](https://github.com/iree-org/iree/actions/runs/38519841686/job/115706847702) | 9 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 9 | 0 | — | — | [1m23s](https://github.com/iree-org/iree/actions/runs/38525482930/job/115724780594) | [2m56s](https://github.com/iree-org/iree/actions/runs/38530100758/job/115740105130) | [2m56s](https://github.com/iree-org/iree/actions/runs/38530100758/job/115740105130) | 9 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 9 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/38527832171/job/115732299630) | [2m52s](https://github.com/iree-org/iree/actions/runs/38530094390/job/115739645288) | [2m52s](https://github.com/iree-org/iree/actions/runs/38530094390/job/115739645288) | 9 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/38527942464/job/115733264590) | [2m32s](https://github.com/iree-org/iree/actions/runs/38530100758/job/115740105176) | [2m32s](https://github.com/iree-org/iree/actions/runs/38530100758/job/115740105176) | 9 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 9 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38525482930/job/115724780387) | [2m28s](https://github.com/iree-org/iree/actions/runs/38529169445/job/115736669455) | [2m28s](https://github.com/iree-org/iree/actions/runs/38529169445/job/115736669455) | 9 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 360 | 12% (42/360) |  | 2h34m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 277 | 0% (0/277) |  | 2h47m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h33m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h41m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h04m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h52m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
