# iree-ci-monitor

_Updated: 2026-07-27 11:49 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [28m28s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915014) | [37m02s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915079) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 3 | 0 | — | — | 0 | [15m05s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914993) | [27m32s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952605) | 0% (0/2) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952663) | [27m30s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914992) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [5m29s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952423) | [26m08s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914923) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [7m51s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952493) | [24m44s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914822) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952484) | [18m38s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914850) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [16m44s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915010) | [16m51s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952695) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [6m35s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914955) | [16m32s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952585) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [8m24s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952602) | [16m29s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915124) | 0% (0/4) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [6m58s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952704) | [9m25s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915037) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [1m02s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952607) | [6m34s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914977) | 0% (0/2) | `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952455) | [6m33s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914920) | 0% (0/2) | `iree-mi308-1` |
| `macos-14` | github-hosted | 7 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30258208564/job/89951695826) | [2m07s](https://github.com/iree-org/iree/actions/runs/30258547352/job/89952808085) | 0% (0/4) | 7 |
| `azure-linux-scale` | ossci | 14 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/30255672146/job/89952166198) | [1m42s](https://github.com/iree-org/iree/actions/runs/30258547352/job/89952808096) | 0% (0/9) | 14 |
| `ubuntu-24.04` | github-hosted | 61 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914843) | [1m39s](https://github.com/iree-org/iree/actions/runs/30249484790/job/89954158309) | 3% (1/35) | 60 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30258547352/job/89952807933) | [1m30s](https://github.com/iree-org/iree/actions/runs/30258547352/job/89952808041) | 0% (0/3) | 6 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m22s](https://github.com/iree-org/iree/actions/runs/30258212698/job/89951708566) | [1m22s](https://github.com/iree-org/iree/actions/runs/30258212698/job/89951708566) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/30255672146/job/89952165967) | [1m19s](https://github.com/iree-org/iree/actions/runs/30258547352/job/89952808019) | 0% (0/3) | 6 |
| `ubuntu-latest` | github-hosted | 27 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30278079298/job/90017141314) | [46s](https://github.com/iree-org/iree/actions/runs/30258937531/job/89954024652) | 0% (0/3) | 27 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30255672146/job/89952166110) | [8s](https://github.com/iree-org/iree/actions/runs/30258547352/job/89952808182) | 0% (0/1) | 2 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914780) | [4s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952473) | 0% (0/2) | 3 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30258205007/job/89951684604) | [2s](https://github.com/iree-org/iree/actions/runs/30258205007/job/89951684604) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [14m24s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952722) | [37m02s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915079) | [37m02s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915079) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [19m16s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952773) | [28m28s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915014) | [28m28s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915014) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 3 | 0 | — | — | [15m05s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914993) | [27m32s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952605) | [27m32s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952605) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952663) | [27m30s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914992) | [27m30s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914992) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 3 | 0 | — | — | [5m29s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952423) | [26m08s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914923) | [26m08s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914923) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [7m51s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952493) | [24m44s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914822) | [24m44s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914822) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952484) | [18m38s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914850) | [18m38s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914850) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [9m06s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915020) | [16m51s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952695) | [16m51s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952695) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [4m24s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952719) | [16m44s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915010) | [16m44s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915010) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [6m35s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914955) | [16m32s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952585) | [16m32s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952585) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [8m24s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952602) | [16m29s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915124) | [16m29s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915124) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952491) | [9m27s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914881) | [9m27s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914881) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [6m58s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952704) | [9m25s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915037) | [9m25s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915037) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [1m02s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952607) | [6m34s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914977) | [6m34s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914977) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952455) | [6m33s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914920) | [6m33s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954914920) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [1m32s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915042) | [4m30s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952702) | [4m30s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952702) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | 3 | 0 | — | — | [46s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89954915078) | [2m14s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952672) | [2m14s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89953952672) | 3 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 4 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30278078427/job/90017135820) | [2m12s](https://github.com/iree-org/iree/actions/runs/30258937788/job/89954024492) | [2m12s](https://github.com/iree-org/iree/actions/runs/30258937788/job/89954024492) | 4 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30255672146/job/89952165961) | [2m07s](https://github.com/iree-org/iree/actions/runs/30258547352/job/89952808085) | [2m07s](https://github.com/iree-org/iree/actions/runs/30258547352/job/89952808085) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 3 | 0 | — | — | [27s](https://github.com/iree-org/iree/actions/runs/30255671766/job/89952167224) | [1m52s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89952809376) | [1m52s](https://github.com/iree-org/iree/actions/runs/30258547422/job/89952809376) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 386 | 1% (5/386) |  | 7h23m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 293 | 1% (2/293) |  | 7h33m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 316 | 5% (15/316) |  | 7h35m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 283 | 1% (4/283) |  | 7h45m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 88 | 2% (2/88) |  | 7h46m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
