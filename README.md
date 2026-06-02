# iree-ci-monitor

_Updated: 2026-06-02 12:33 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 12 | 0 | — | — | 0 | [34m24s](https://github.com/iree-org/iree/actions/runs/26825289730/job/79092425263) | [1h09m](https://github.com/iree-org/iree/actions/runs/26825566002/job/79094083986) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 24 | 0 | — | — | 0 | [29m23s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969068) | [1h03m](https://github.com/iree-org/iree/actions/runs/26822992004/job/79093377200) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 12 | 0 | — | — | 0 | [20m32s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969126) | [46m56s](https://github.com/iree-org/iree/actions/runs/26816473996/job/79064221275) | 0% (0/4) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 12 | 0 | — | — | 0 | [10m09s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617472) | [42m58s](https://github.com/iree-org/iree/actions/runs/26822992004/job/79093376827) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 12 | 0 | — | — | 0 | [5m45s](https://github.com/iree-org/iree/actions/runs/26825289730/job/79092425284) | [42m06s](https://github.com/iree-org/iree/actions/runs/26816473996/job/79064221297) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 12 | 0 | — | — | 0 | [9m06s](https://github.com/iree-org/iree/actions/runs/26828447910/job/79104328040) | [41m59s](https://github.com/iree-org/iree/actions/runs/26825566002/job/79094083674) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 24 | 0 | — | — | 0 | [16m33s](https://github.com/iree-org/iree/actions/runs/26822811722/job/79083569447) | [41m41s](https://github.com/iree-org/iree/actions/runs/26816141532/job/79063396809) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 24 | 0 | — | — | 0 | [16m22s](https://github.com/iree-org/iree/actions/runs/26822992004/job/79093377401) | [32m04s](https://github.com/iree-org/iree/actions/runs/26816473996/job/79064221280) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 12 | 0 | — | — | 0 | [11m00s](https://github.com/iree-org/iree/actions/runs/26822811722/job/79083569243) | [25m35s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118968894) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 12 | 0 | — | — | 0 | [8m42s](https://github.com/iree-org/iree/actions/runs/26816473996/job/79064221205) | [24m57s](https://github.com/iree-org/iree/actions/runs/26822992004/job/79093376762) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 24 | 0 | — | — | 0 | [12m30s](https://github.com/iree-org/iree/actions/runs/26816141532/job/79063396818) | [24m37s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969121) | 12% (1/8) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617478) | [16m12s](https://github.com/iree-org/iree/actions/runs/26825566002/job/79094084331) | 0% (0/4) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 48 | 0 | — | — | 0 | [18s](https://github.com/iree-org/iree/actions/runs/26822992004/job/79093376749) | [6m02s](https://github.com/iree-org/iree/actions/runs/26816473996/job/79064221383) | 6% (1/16) | 48 |
| `ubuntu-24.04-arm` | github-hosted | 36 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/26828449200/job/79102615920) | [2m00s](https://github.com/iree-org/iree/actions/runs/26815331609/job/79055578190) | 0% (0/12) | 36 |
| `ubuntu-24.04` | github-hosted | 235 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/26822811722/job/79083569191) | [1m55s](https://github.com/iree-org/iree/actions/runs/26825565815/job/79091999993) | 3% (2/75) | 235 |
| `azure-linux-scale` | ossci | 69 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/26828449200/job/79102616062) | [1m48s](https://github.com/iree-org/iree/actions/runs/26832422199/job/79117196679) | 4% (1/27) | 69 |
| `macos-14` | github-hosted | 37 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26825288728/job/79090953682) | [1m43s](https://github.com/iree-org/iree/actions/runs/26816473925/job/79059449893) | 0% (0/13) | 37 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m36s](https://github.com/iree-org/iree/actions/runs/26814985354/job/79054373745) | [1m36s](https://github.com/iree-org/iree/actions/runs/26814985354/job/79054373745) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 36 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/26825288728/job/79090954354) | [1m30s](https://github.com/iree-org/iree/actions/runs/26832422199/job/79117196039) | 0% (0/12) | 36 |
| `ubuntu-latest` | github-hosted | 33 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26829823362/job/79107633138) | [22s](https://github.com/iree-org/iree/actions/runs/26832416022/job/79117124909) | 0% (0/12) | 33 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26825289730/job/79092424812) | [3s](https://github.com/iree-org/iree/actions/runs/26822811722/job/79083569105) | 25% (1/4) | 12 |
| `azure-windows-scale` | ossci | 12 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/26828449200/job/79102616128) | [2s](https://github.com/iree-org/iree/actions/runs/26825288728/job/79090955065) | 0% (0/4) | 12 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26814968832/job/79054317297) | [2s](https://github.com/iree-org/iree/actions/runs/26814968832/job/79054317297) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 12 | 0 | — | — | [34m24s](https://github.com/iree-org/iree/actions/runs/26825289730/job/79092425263) | [1h09m](https://github.com/iree-org/iree/actions/runs/26825566002/job/79094083986) | [1h09m](https://github.com/iree-org/iree/actions/runs/26825566002/job/79094083986) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 12 | 0 | — | — | [26m02s](https://github.com/iree-org/iree/actions/runs/26825289730/job/79092424832) | [1h05m](https://github.com/iree-org/iree/actions/runs/26828447910/job/79104328943) | [1h05m](https://github.com/iree-org/iree/actions/runs/26828447910/job/79104328943) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 12 | 0 | — | — | [29m23s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969068) | [1h03m](https://github.com/iree-org/iree/actions/runs/26822992004/job/79093377200) | [1h03m](https://github.com/iree-org/iree/actions/runs/26822992004/job/79093377200) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 12 | 0 | — | — | [20m32s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969126) | [46m56s](https://github.com/iree-org/iree/actions/runs/26816473996/job/79064221275) | [46m56s](https://github.com/iree-org/iree/actions/runs/26816473996/job/79064221275) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 12 | 0 | — | — | [15m02s](https://github.com/iree-org/iree/actions/runs/26815331653/job/79056969779) | [44m18s](https://github.com/iree-org/iree/actions/runs/26825289730/job/79092425120) | [44m18s](https://github.com/iree-org/iree/actions/runs/26825289730/job/79092425120) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 12 | 0 | — | — | [10m09s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617472) | [42m58s](https://github.com/iree-org/iree/actions/runs/26822992004/job/79093376827) | [42m58s](https://github.com/iree-org/iree/actions/runs/26822992004/job/79093376827) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 12 | 0 | — | — | [5m45s](https://github.com/iree-org/iree/actions/runs/26825289730/job/79092425284) | [42m06s](https://github.com/iree-org/iree/actions/runs/26816473996/job/79064221297) | [42m06s](https://github.com/iree-org/iree/actions/runs/26816473996/job/79064221297) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 12 | 0 | — | — | [9m06s](https://github.com/iree-org/iree/actions/runs/26828447910/job/79104328040) | [41m59s](https://github.com/iree-org/iree/actions/runs/26825566002/job/79094083674) | [41m59s](https://github.com/iree-org/iree/actions/runs/26825566002/job/79094083674) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 12 | 0 | — | — | [5m21s](https://github.com/iree-org/iree/actions/runs/26815331653/job/79056969899) | [41m41s](https://github.com/iree-org/iree/actions/runs/26816141532/job/79063396809) | [41m41s](https://github.com/iree-org/iree/actions/runs/26816141532/job/79063396809) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 12 | 0 | — | — | [14m11s](https://github.com/iree-org/iree/actions/runs/26822992004/job/79093377450) | [39m47s](https://github.com/iree-org/iree/actions/runs/26816473996/job/79064221373) | [39m47s](https://github.com/iree-org/iree/actions/runs/26816473996/job/79064221373) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 12 | 0 | — | — | [16m22s](https://github.com/iree-org/iree/actions/runs/26822992004/job/79093377401) | [32m04s](https://github.com/iree-org/iree/actions/runs/26816473996/job/79064221280) | [32m04s](https://github.com/iree-org/iree/actions/runs/26816473996/job/79064221280) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 12 | 0 | — | — | [11m00s](https://github.com/iree-org/iree/actions/runs/26822811722/job/79083569243) | [25m35s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118968894) | [25m35s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118968894) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 12 | 0 | — | — | [8m42s](https://github.com/iree-org/iree/actions/runs/26816473996/job/79064221205) | [24m57s](https://github.com/iree-org/iree/actions/runs/26822992004/job/79093376762) | [24m57s](https://github.com/iree-org/iree/actions/runs/26822992004/job/79093376762) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 12 | 0 | — | — | [13m42s](https://github.com/iree-org/iree/actions/runs/26822811722/job/79083569269) | [24m57s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969039) | [24m57s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969039) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 12 | 0 | — | — | [6m33s](https://github.com/iree-org/iree/actions/runs/26822811722/job/79083569319) | [24m37s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969121) | [24m37s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969121) | 4 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 12 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26832406098/job/79118617478) | [16m12s](https://github.com/iree-org/iree/actions/runs/26825566002/job/79094084331) | [16m12s](https://github.com/iree-org/iree/actions/runs/26825566002/job/79094084331) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 12 | 0 | — | — | [1m21s](https://github.com/iree-org/iree/actions/runs/26832421673/job/79118969101) | [15m08s](https://github.com/iree-org/iree/actions/runs/26822811722/job/79083569497) | [15m08s](https://github.com/iree-org/iree/actions/runs/26822811722/job/79083569497) | 12 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 12 | 0 | — | — | [1m10s](https://github.com/iree-org/iree/actions/runs/26828447910/job/79104328615) | [6m07s](https://github.com/iree-org/iree/actions/runs/26822811722/job/79083569246) | [6m07s](https://github.com/iree-org/iree/actions/runs/26822811722/job/79083569246) | 12 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 12 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/26828447910/job/79104328411) | [4m15s](https://github.com/iree-org/iree/actions/runs/26825566002/job/79094083916) | [4m15s](https://github.com/iree-org/iree/actions/runs/26825566002/job/79094083916) | 12 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 12 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/26825289730/job/79092424799) | [3m56s](https://github.com/iree-org/iree/actions/runs/26816473996/job/79064221265) | [3m56s](https://github.com/iree-org/iree/actions/runs/26816473996/job/79064221265) | 12 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 299 | 4% (13/298) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 336 | 0% (1/336) |  | 2h40m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 232 | 0% (1/232) |  | 2h44m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 241 | 0% (0/241) |  | 2h48m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 76 | 1% (1/76) |  | 2h55m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h03m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
