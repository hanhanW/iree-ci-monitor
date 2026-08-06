# iree-ci-monitor

_Updated: 2026-08-06 07:37 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [23m01s](https://github.com/iree-org/iree/actions/runs/31093507966/job/92591753015) | [1h10m](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158769) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [11m02s](https://github.com/iree-org/iree/actions/runs/31093507966/job/92591753201) | [29m58s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500306) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [17m27s](https://github.com/iree-org/iree/actions/runs/31090288803/job/92581332500) | [25m59s](https://github.com/iree-org/iree/actions/runs/31093507966/job/92591753031) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [8m09s](https://github.com/iree-org/iree/actions/runs/31087664594/job/92572996747) | [23m47s](https://github.com/iree-org/iree/actions/runs/31087664594/job/92572996652) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [11m22s](https://github.com/iree-org/iree/actions/runs/31093507966/job/92591753156) | [22m46s](https://github.com/iree-org/iree/actions/runs/31087664594/job/92572996622) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 6 | 0 | — | — | 0 | [17m02s](https://github.com/iree-org/iree/actions/runs/31093507966/job/92591753117) | [22m06s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158689) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | [19m41s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500330) | [22m06s](https://github.com/iree-org/iree/actions/runs/31090288803/job/92581332638) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [7m43s](https://github.com/iree-org/iree/actions/runs/31090288803/job/92581332559) | [22m03s](https://github.com/iree-org/iree/actions/runs/31087664594/job/92572996681) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | — | 0 | [5m55s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158766) | [17m20s](https://github.com/iree-org/iree/actions/runs/31090288803/job/92581332622) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 6 | 0 | — | — | 0 | [15m26s](https://github.com/iree-org/iree/actions/runs/31090288803/job/92581332607) | [17m10s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158835) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [7m34s](https://github.com/iree-org/iree/actions/runs/31087664594/job/92572996741) | [11m41s](https://github.com/iree-org/iree/actions/runs/31090288803/job/92581332595) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `azure-linux-scale` | ossci | 43 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/31093508505/job/92589940612) | [1m43s](https://github.com/iree-org/iree/actions/runs/31097069200/job/92601553441) | 0% (0/15) | 43 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m35s](https://github.com/iree-org/iree/actions/runs/31092008899/job/92584985396) | [1m35s](https://github.com/iree-org/iree/actions/runs/31092008899/job/92584985396) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 23 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31093508505/job/92589940402) | [1m31s](https://github.com/iree-org/iree/actions/runs/31076637886/job/92536030297) | 0% (0/6) | 23 |
| `ubuntu-24.04` | github-hosted | 144 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/31090288803/job/92581332526) | [1m27s](https://github.com/iree-org/iree/actions/runs/31076637886/job/92536030291) | 0% (0/42) | 143 |
| `macos-14` | github-hosted | 24 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/31090289397/job/92579880652) | [1m26s](https://github.com/iree-org/iree/actions/runs/31076637886/job/92536030389) | 0% (0/7) | 24 |
| `ubuntu-24.04-arm` | github-hosted | 24 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31087665143/job/92570912690) | [58s](https://github.com/iree-org/iree/actions/runs/31097388078/job/92602806370) | 0% (0/6) | 24 |
| `azure-windows-scale` | ossci | 7 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31076637886/job/92536030466) | [34s](https://github.com/iree-org/iree/actions/runs/31097069200/job/92601553444) | 0% (0/2) | 7 |
| `ubuntu-latest` | github-hosted | 24 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31099006809/job/92607777222) | [9s](https://github.com/iree-org/iree/actions/runs/31099006809/job/92607777313) | 0% (0/6) | 24 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/31091980282/job/92584891896) | [2s](https://github.com/iree-org/iree/actions/runs/31091980282/job/92584891896) | — | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [24m49s](https://github.com/iree-org/iree/actions/runs/31090288803/job/92581332653) | [1h10m](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158769) | [1h10m](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158769) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [6m04s](https://github.com/iree-org/iree/actions/runs/31090288803/job/92581332584) | [48m09s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500333) | [48m09s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500333) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [11m02s](https://github.com/iree-org/iree/actions/runs/31093507966/job/92591753201) | [29m58s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500306) | [29m58s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500306) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [17m27s](https://github.com/iree-org/iree/actions/runs/31090288803/job/92581332500) | [25m59s](https://github.com/iree-org/iree/actions/runs/31093507966/job/92591753031) | [25m59s](https://github.com/iree-org/iree/actions/runs/31093507966/job/92591753031) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [6m58s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500435) | [23m47s](https://github.com/iree-org/iree/actions/runs/31087664594/job/92572996652) | [23m47s](https://github.com/iree-org/iree/actions/runs/31087664594/job/92572996652) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [11m22s](https://github.com/iree-org/iree/actions/runs/31093507966/job/92591753156) | [22m46s](https://github.com/iree-org/iree/actions/runs/31087664594/job/92572996622) | [22m46s](https://github.com/iree-org/iree/actions/runs/31087664594/job/92572996622) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 6 | 0 | — | — | [19m41s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500330) | [22m06s](https://github.com/iree-org/iree/actions/runs/31090288803/job/92581332638) | [22m06s](https://github.com/iree-org/iree/actions/runs/31090288803/job/92581332638) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 6 | 0 | — | — | [17m02s](https://github.com/iree-org/iree/actions/runs/31093507966/job/92591753117) | [22m06s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158689) | [22m06s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158689) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [8m53s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500276) | [22m03s](https://github.com/iree-org/iree/actions/runs/31087664594/job/92572996681) | [22m03s](https://github.com/iree-org/iree/actions/runs/31087664594/job/92572996681) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [11m03s](https://github.com/iree-org/iree/actions/runs/31093507966/job/92591753133) | [20m57s](https://github.com/iree-org/iree/actions/runs/31090288803/job/92581332588) | [20m57s](https://github.com/iree-org/iree/actions/runs/31090288803/job/92581332588) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [9m31s](https://github.com/iree-org/iree/actions/runs/31079151613/job/92545500447) | [17m20s](https://github.com/iree-org/iree/actions/runs/31090288803/job/92581332622) | [17m20s](https://github.com/iree-org/iree/actions/runs/31090288803/job/92581332622) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 6 | 0 | — | — | [15m26s](https://github.com/iree-org/iree/actions/runs/31090288803/job/92581332607) | [17m10s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158835) | [17m10s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158835) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [6m51s](https://github.com/iree-org/iree/actions/runs/31087664594/job/92572996650) | [16m48s](https://github.com/iree-org/iree/actions/runs/31093507966/job/92591753169) | [16m48s](https://github.com/iree-org/iree/actions/runs/31093507966/job/92591753169) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [5m55s](https://github.com/iree-org/iree/actions/runs/31076637887/job/92537158766) | [11m59s](https://github.com/iree-org/iree/actions/runs/31087664594/job/92572996884) | [11m59s](https://github.com/iree-org/iree/actions/runs/31087664594/job/92572996884) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 6 | 0 | — | — | [7m34s](https://github.com/iree-org/iree/actions/runs/31087664594/job/92572996741) | [11m41s](https://github.com/iree-org/iree/actions/runs/31090288803/job/92581332595) | [11m41s](https://github.com/iree-org/iree/actions/runs/31090288803/job/92581332595) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 7 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/31076637886/job/92536030273) | [2m37s](https://github.com/iree-org/iree/actions/runs/31097388078/job/92602806533) | [2m37s](https://github.com/iree-org/iree/actions/runs/31097388078/job/92602806533) | 7 |
| `.github/workflows/ci.yml` | runtime :: windows-2022 | `windows-2022` | 7 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31093508505/job/92589940402) | [2m11s](https://github.com/iree-org/iree/actions/runs/31097388078/job/92602806398) | [2m11s](https://github.com/iree-org/iree/actions/runs/31097388078/job/92602806398) | 7 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 7 | 0 | — | — | [1m07s](https://github.com/iree-org/iree/actions/runs/31087665143/job/92570912765) | [2m08s](https://github.com/iree-org/iree/actions/runs/31097388078/job/92602806493) | [2m08s](https://github.com/iree-org/iree/actions/runs/31097388078/job/92602806493) | 7 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 7 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/31079151663/job/92543793328) | [2m04s](https://github.com/iree-org/iree/actions/runs/31097388078/job/92602806323) | [2m04s](https://github.com/iree-org/iree/actions/runs/31097388078/job/92602806323) | 7 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 7 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31093507966/job/92589928726) | [1m54s](https://github.com/iree-org/iree/actions/runs/31097069594/job/92601566034) | [1m54s](https://github.com/iree-org/iree/actions/runs/31097069594/job/92601566034) | 7 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 125 | 2% (3/125) |  | 32m28s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 142 | 0% (0/142) |  | 2h25m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 112 | 1% (1/112) |  | 2h26m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 110 | 0% (0/110) |  | 2h28m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 17 | 0% (0/17) |  | 3d01h ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h10m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
