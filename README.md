# iree-ci-monitor

_Updated: 2026-07-27 06:22 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | — | 0 | [19m16s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952773) | [37m02s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915079) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | — | 0 | [24m44s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914822) | [32m19s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992271) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | — | 0 | [20m50s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992390) | [27m32s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952605) | 0% (0/2) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | — | 0 | [9m10s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992216) | [27m30s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914992) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [5m29s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952423) | [26m08s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914923) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | — | 0 | [13m46s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992231) | [18m38s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914850) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | — | 0 | [7m51s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992462) | [16m51s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952695) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [6m35s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914955) | [16m32s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952585) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | — | 0 | [6m09s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992437) | [16m29s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915124) | 0% (0/4) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | — | 0 | [4m30s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952702) | [11m40s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992405) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | — | 0 | [1m02s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952607) | [6m34s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914977) | 0% (0/2) | `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992409) | [6m33s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914920) | 0% (0/2) | `iree-mi308-1` |
| `azure-linux-scale` | ossci | 24 | 0 | — | — | 0 | [23s](https://github.com/iree-org/iree/actions/runs/30249484800/job/89924030501) | [1m53s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293824) | 0% (0/14) | 24 |
| `macos-14` | github-hosted | 15 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/30258208564/job/89951695826) | [1m22s](https://github.com/iree-org/iree/actions/runs/30258547352/job/89952807997) | 0% (0/6) | 15 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m22s](https://github.com/iree-org/iree/actions/runs/30258212698/job/89951708566) | [1m22s](https://github.com/iree-org/iree/actions/runs/30258212698/job/89951708566) | 0% (0/1) | 1 |
| `ubuntu-24.04` | github-hosted | 94 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/30255672146/job/89952165938) | [1m19s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952698) | 2% (1/43) | 93 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30255672146/job/89952165916) | [1m10s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293450) | 0% (0/6) | 15 |
| `windows-2022` | github-hosted | 14 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293417) | [55s](https://github.com/iree-org/iree/actions/runs/30258547352/job/89952808015) | 0% (0/6) | 14 |
| `ubuntu-latest` | github-hosted | 24 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30264255280/job/89971089332) | [46s](https://github.com/iree-org/iree/actions/runs/30258937531/job/89954024652) | 0% (0/6) | 24 |
| `azure-windows-scale` | ossci | 4 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30255672146/job/89952166110) | [8s](https://github.com/iree-org/iree/actions/runs/30258547352/job/89952808182) | 0% (0/2) | 4 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992171) | [4s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952473) | 0% (0/2) | 4 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/30258205007/job/89951684604) | [2s](https://github.com/iree-org/iree/actions/runs/30258205007/job/89951684604) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [26m38s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992310) | [37m02s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915079) | [37m02s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915079) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 4 | 0 | — | — | [24m44s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914822) | [32m19s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992271) | [32m19s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992271) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 4 | 0 | — | — | [19m16s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952773) | [28m28s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915014) | [28m28s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915014) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 0 | — | — | [20m50s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992390) | [27m32s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952605) | [27m32s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952605) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 4 | 0 | — | — | [9m10s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992216) | [27m30s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914992) | [27m30s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914992) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 4 | 0 | — | — | [5m29s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952423) | [26m08s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914923) | [26m08s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914923) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 4 | 0 | — | — | [13m46s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992231) | [18m38s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914850) | [18m38s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914850) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [9m06s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915020) | [16m51s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952695) | [16m51s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952695) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 4 | 0 | — | — | [7m51s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992462) | [16m44s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915010) | [16m44s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915010) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 4 | 0 | — | — | [6m35s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914955) | [16m32s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952585) | [16m32s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952585) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [8m24s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952602) | [16m29s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915124) | [16m29s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915124) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 4 | 0 | — | — | [9m25s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915037) | [11m40s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992405) | [11m40s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992405) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 4 | 0 | — | — | [6m09s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992437) | [9m27s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914881) | [9m27s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914881) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 4 | 0 | — | — | [1m02s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952607) | [6m34s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914977) | [6m34s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914977) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89911992409) | [6m33s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914920) | [6m33s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914920) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 0 | — | — | [1m32s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915042) | [4m30s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952702) | [4m30s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952702) | 3 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 4 | 0 | — | — | [1m52s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89952809376) | [2m21s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89910298712) | [2m21s](https://github.com/iree-org/iree/actions/runs/30231458809/job/89910298712) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | 4 | 0 | — | — | [46s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915078) | [2m14s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952672) | [2m14s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952672) | 4 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30264254575/job/89971085157) | [2m12s](https://github.com/iree-org/iree/actions/runs/30258937788/job/89954024492) | [2m12s](https://github.com/iree-org/iree/actions/runs/30258937788/job/89954024492) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 4 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30231458802/job/89910293458) | [2m07s](https://github.com/iree-org/iree/actions/runs/30258547352/job/89952808085) | [2m07s](https://github.com/iree-org/iree/actions/runs/30258547352/job/89952808085) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 386 | 1% (5/386) |  | 1h56m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 293 | 1% (2/293) |  | 2h06m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 316 | 5% (15/316) |  | 2h08m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 283 | 1% (4/283) |  | 2h18m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 88 | 2% (2/88) |  | 2h19m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
