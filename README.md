# iree-ci-monitor

_Updated: 2026-08-11 06:45 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [1h10m](https://github.com/iree-org/iree/actions/runs/31451216453/job/93702455937) | [1h15m](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699361959) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 10 | 0 | — | — | 0 | [35m08s](https://github.com/iree-org/iree/actions/runs/31477208607/job/93735648533) | [1h08m](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699362098) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 10 | 0 | — | — | 0 | [25m03s](https://github.com/iree-org/iree/actions/runs/31471877714/job/93734311884) | [1h01m](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699362132) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [31m32s](https://github.com/iree-org/iree/actions/runs/31477208607/job/93735648158) | [51m49s](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699361945) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 5 | 0 | — | — | 0 | [38m19s](https://github.com/iree-org/iree/actions/runs/31477208607/job/93735648186) | [47m27s](https://github.com/iree-org/iree/actions/runs/31471877714/job/93734311793) | 0% (0/1) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 10 | 0 | — | — | 0 | [29m23s](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699361937) | [47m22s](https://github.com/iree-org/iree/actions/runs/31451216453/job/93702455999) | 0% (0/2) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 5 | 0 | — | — | 0 | [39m02s](https://github.com/iree-org/iree/actions/runs/31471877714/job/93734312020) | [40m37s](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699361970) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [4m46s](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699361938) | [38m38s](https://github.com/iree-org/iree/actions/runs/31451216453/job/93702455962) | 100% (1/1) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 5 | 0 | — | — | 0 | [10m35s](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699361943) | [38m27s](https://github.com/iree-org/iree/actions/runs/31451216453/job/93702455891) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 5 | 0 | — | — | 0 | [16m58s](https://github.com/iree-org/iree/actions/runs/31451216453/job/93702455940) | [31m55s](https://github.com/iree-org/iree/actions/runs/31471877714/job/93734311825) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 10 | 0 | — | — | 0 | [10m35s](https://github.com/iree-org/iree/actions/runs/31477208607/job/93735648282) | [29m28s](https://github.com/iree-org/iree/actions/runs/31477208607/job/93735648284) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31477208591/job/93733628403) | [5m45s](https://github.com/iree-org/iree/actions/runs/31451216529/job/93699980620) | 0% (0/3) | 18 |
| `ubuntu-24.04` | github-hosted | 115 | 0 | — | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/31477208607/job/93735648534) | [4m02s](https://github.com/iree-org/iree/actions/runs/31451216360/job/93699403021) | 5% (1/22) | 114 |
| `windows-2022` | github-hosted | 17 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31465090879/job/93697758811) | [3m38s](https://github.com/iree-org/iree/actions/runs/31451216529/job/93699980639) | 0% (0/3) | 17 |
| `macos-14` | github-hosted | 18 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31477208591/job/93733628307) | [1m47s](https://github.com/iree-org/iree/actions/runs/31477208591/job/93733628442) | 0% (0/4) | 18 |
| `azure-linux-scale` | ossci | 28 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/31480340510/job/93743642914) | [1m39s](https://github.com/iree-org/iree/actions/runs/31477208591/job/93733628579) | 0% (0/8) | 28 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m28s](https://github.com/iree-org/iree/actions/runs/31478323730/job/93737202823) | [1m28s](https://github.com/iree-org/iree/actions/runs/31478323730/job/93737202823) | 0% (0/1) | 1 |
| `azure-windows-scale` | ossci | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31477208591/job/93733628661) | [33s](https://github.com/iree-org/iree/actions/runs/31451216529/job/93699980598) | 0% (0/1) | 5 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31483090262/job/93752251173) | [8s](https://github.com/iree-org/iree/actions/runs/31483472860/job/93753482868) | 0% (0/3) | 12 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 5 | 0 | — | — | [1h10m](https://github.com/iree-org/iree/actions/runs/31451216453/job/93702455937) | [1h15m](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699361959) | [1h15m](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699361959) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 5 | 0 | — | — | [39m20s](https://github.com/iree-org/iree/actions/runs/31471877714/job/93734312040) | [1h08m](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699362098) | [1h08m](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699362098) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [59m27s](https://github.com/iree-org/iree/actions/runs/31477208607/job/93735648371) | [1h01m](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699362132) | [1h01m](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699362132) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 5 | 0 | — | — | [31m32s](https://github.com/iree-org/iree/actions/runs/31477208607/job/93735648158) | [51m49s](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699361945) | [51m49s](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699361945) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 5 | 0 | — | — | [38m19s](https://github.com/iree-org/iree/actions/runs/31477208607/job/93735648186) | [47m27s](https://github.com/iree-org/iree/actions/runs/31471877714/job/93734311793) | [47m27s](https://github.com/iree-org/iree/actions/runs/31471877714/job/93734311793) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [46m18s](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699361939) | [47m22s](https://github.com/iree-org/iree/actions/runs/31451216453/job/93702455999) | [47m22s](https://github.com/iree-org/iree/actions/runs/31451216453/job/93702455999) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 5 | 0 | — | — | [39m02s](https://github.com/iree-org/iree/actions/runs/31471877714/job/93734312020) | [40m37s](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699361970) | [40m37s](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699361970) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 5 | 0 | — | — | [4m46s](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699361938) | [38m38s](https://github.com/iree-org/iree/actions/runs/31451216453/job/93702455962) | [38m38s](https://github.com/iree-org/iree/actions/runs/31451216453/job/93702455962) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 5 | 0 | — | — | [10m35s](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699361943) | [38m27s](https://github.com/iree-org/iree/actions/runs/31451216453/job/93702455891) | [38m27s](https://github.com/iree-org/iree/actions/runs/31451216453/job/93702455891) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 5 | 0 | — | — | [23m23s](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699361944) | [38m10s](https://github.com/iree-org/iree/actions/runs/31451216453/job/93702456014) | [38m10s](https://github.com/iree-org/iree/actions/runs/31451216453/job/93702456014) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [25m03s](https://github.com/iree-org/iree/actions/runs/31471877714/job/93734311884) | [37m36s](https://github.com/iree-org/iree/actions/runs/31477208607/job/93735648206) | [37m36s](https://github.com/iree-org/iree/actions/runs/31477208607/job/93735648206) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [29m23s](https://github.com/iree-org/iree/actions/runs/31465090853/job/93699361937) | [34m34s](https://github.com/iree-org/iree/actions/runs/31477208607/job/93735648135) | [34m34s](https://github.com/iree-org/iree/actions/runs/31477208607/job/93735648135) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 5 | 0 | — | — | [16m58s](https://github.com/iree-org/iree/actions/runs/31451216453/job/93702455940) | [31m55s](https://github.com/iree-org/iree/actions/runs/31471877714/job/93734311825) | [31m55s](https://github.com/iree-org/iree/actions/runs/31471877714/job/93734311825) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [25m12s](https://github.com/iree-org/iree/actions/runs/31451216453/job/93702456049) | [29m28s](https://github.com/iree-org/iree/actions/runs/31477208607/job/93735648284) | [29m28s](https://github.com/iree-org/iree/actions/runs/31477208607/job/93735648284) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [10m35s](https://github.com/iree-org/iree/actions/runs/31477208607/job/93735648282) | [14m07s](https://github.com/iree-org/iree/actions/runs/31451216453/job/93702455991) | [14m07s](https://github.com/iree-org/iree/actions/runs/31451216453/job/93702455991) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 5 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/31477208591/job/93733628372) | [8m13s](https://github.com/iree-org/iree/actions/runs/31451216529/job/93699980595) | [8m13s](https://github.com/iree-org/iree/actions/runs/31451216529/job/93699980595) | 5 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31477208607/job/93733567469) | [7m23s](https://github.com/iree-org/iree/actions/runs/31451216453/job/93699404218) | [7m23s](https://github.com/iree-org/iree/actions/runs/31451216453/job/93699404218) | 5 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 5 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31480340510/job/93743642771) | [6m03s](https://github.com/iree-org/iree/actions/runs/31451216529/job/93699980682) | [6m03s](https://github.com/iree-org/iree/actions/runs/31451216529/job/93699980682) | 5 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 5 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31480340510/job/93743642704) | [5m45s](https://github.com/iree-org/iree/actions/runs/31451216529/job/93699980620) | [5m45s](https://github.com/iree-org/iree/actions/runs/31451216529/job/93699980620) | 5 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 5 | 0 | — | — | [50s](https://github.com/iree-org/iree/actions/runs/31480340510/job/93743642716) | [4m55s](https://github.com/iree-org/iree/actions/runs/31451216529/job/93699980571) | [4m55s](https://github.com/iree-org/iree/actions/runs/31451216529/job/93699980571) | 5 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 115 | 10% (11/115) |  | 2h37m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 152 | 0% (0/152) |  | 3h12m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 134 | 4% (5/134) |  | 3h14m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 123 | 3% (4/123) |  | 3h16m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h15m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h08m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
