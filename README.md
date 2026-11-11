# iree-ci-monitor

_Updated: 2026-11-11 11:40 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [25m46s](https://github.com/iree-org/iree/actions/runs/43044055649/job/130609072890) | [1h09m](https://github.com/iree-org/iree/actions/runs/43068885344/job/130696589158) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 22 | 0 | — | — | 1 | [11m41s](https://github.com/iree-org/iree/actions/runs/43044055649/job/130609072076) | [1h01m](https://github.com/iree-org/iree/actions/runs/43068885344/job/130696588910) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 22 | 3 | [39m29s](https://github.com/iree-org/iree/actions/runs/43081668474/job/130740413354) | 2026-11-11 11:39 PST | 0 | [27m36s](https://github.com/iree-org/iree/actions/runs/43044055649/job/130609072403) | [55m10s](https://github.com/iree-org/iree/actions/runs/43029517550/job/130556922197) | 0% (0/5) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 11 | 1 | [15m59s](https://github.com/iree-org/iree/actions/runs/43081682833/job/130753230609) | 2026-11-11 11:39 PST | 0 | [12m46s](https://github.com/iree-org/iree/actions/runs/43068994089/job/130696579497) | [48m42s](https://github.com/iree-org/iree/actions/runs/43072655555/job/130708950391) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 22 | 4 | [28m53s](https://github.com/iree-org/iree/actions/runs/43083092285/job/130746190170) | 2026-11-11 11:39 PST | 1 | [16m49s](https://github.com/iree-org/iree/actions/runs/43068885344/job/130696589310) | [44m19s](https://github.com/iree-org/iree/actions/runs/43038605593/job/130589296668) | 0% (0/5) | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 11 | 0 | — | — | 0 | [5m48s](https://github.com/iree-org/iree/actions/runs/43068994089/job/130696579202) | [35m38s](https://github.com/iree-org/iree/actions/runs/43044055649/job/130609072205) | 0% (0/3) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 22 | 0 | — | — | 0 | [8m25s](https://github.com/iree-org/iree/actions/runs/43081682833/job/130753231053) | [34m06s](https://github.com/iree-org/iree/actions/runs/43072655555/job/130708951357) | 0% (0/6) | `shark55-ci`, `shark75-ci` |
| `azure-windows-scale` | ossci | 13 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/43077902009/job/130722596601) | [2m43s](https://github.com/iree-org/iree/actions/runs/43068994196/job/130692746056) | 0% (0/3) | 13 |
| `macos-15` | github-hosted | 39 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/43044055314/job/130603307074) | [2m37s](https://github.com/iree-org/iree/actions/runs/43068885197/job/130691269416) | 0% (0/9) | 39 |
| `ubuntu-24.04-arm` | github-hosted | 39 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/43077902009/job/130722596088) | [2m22s](https://github.com/iree-org/iree/actions/runs/43083092218/job/130740558602) | 33% (3/9) | 39 |
| `azure-linux-scale` | ossci | 83 | 0 | — | — | 3 | [9s](https://github.com/iree-org/iree/actions/runs/43081682981/job/130736674798) | [2m08s](https://github.com/iree-org/iree/actions/runs/43081667586/job/130736925847) | 5% (1/19) | 83 |
| `ubuntu-24.04` | github-hosted | 244 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/43072655555/job/130708950552) | [2m07s](https://github.com/iree-org/iree/actions/runs/43068994089/job/130696579320) | 21% (12/58) | 241 |
| `windows-2022` | github-hosted | 39 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/43077902009/job/130722595501) | [2m05s](https://github.com/iree-org/iree/actions/runs/43068885197/job/130691270668) | 0% (0/9) | 39 |
| `ubuntu-latest` | github-hosted | 21 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/43081665344/job/130735518246) | [1m18s](https://github.com/iree-org/iree/actions/runs/43069444242/job/130693055559) | 0% (0/9) | 21 |
| `Linux,X64,iree-w7900` | self-hosted | 11 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [39m29s](https://github.com/iree-org/iree/actions/runs/43081668474/job/130740413354) | 2026-11-11 11:39 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [28m53s](https://github.com/iree-org/iree/actions/runs/43083092285/job/130746190170) | 2026-11-11 11:39 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `fix-spirv-vector-transfer-alignment` | pull_request |
| [28m53s](https://github.com/iree-org/iree/actions/runs/43083092285/job/130746190461) | 2026-11-11 11:39 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `fix-spirv-vector-transfer-alignment` | pull_request |
| [28m53s](https://github.com/iree-org/iree/actions/runs/43083092285/job/130746190470) | 2026-11-11 11:39 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `fix-spirv-vector-transfer-alignment` | pull_request |
| [15m59s](https://github.com/iree-org/iree/actions/runs/43081682833/job/130753230609) | 2026-11-11 11:39 PST | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `integrates/llvm-20261111` | pull_request |
| [15m59s](https://github.com/iree-org/iree/actions/runs/43081682833/job/130753230995) | 2026-11-11 11:39 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `integrates/llvm-20261111` | pull_request |
| [15m59s](https://github.com/iree-org/iree/actions/runs/43081682833/job/130753231145) | 2026-11-11 11:39 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `integrates/llvm-20261111` | pull_request |
| [15m59s](https://github.com/iree-org/iree/actions/runs/43081682833/job/130753231233) | 2026-11-11 11:39 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `integrates/llvm-20261111` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 11 | 0 | — | — | [25m46s](https://github.com/iree-org/iree/actions/runs/43044055649/job/130609072890) | [1h09m](https://github.com/iree-org/iree/actions/runs/43068885344/job/130696589158) | [1h09m](https://github.com/iree-org/iree/actions/runs/43068885344/job/130696589158) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 11 | 0 | — | — | [11m52s](https://github.com/iree-org/iree/actions/runs/43081668474/job/130740413348) | [1h06m](https://github.com/iree-org/iree/actions/runs/43068994089/job/130696579559) | [1h06m](https://github.com/iree-org/iree/actions/runs/43068994089/job/130696579559) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 11 | 1 | [39m29s](https://github.com/iree-org/iree/actions/runs/43081668474/job/130740413354) | 2026-11-11 11:39 PST | [19m32s](https://github.com/iree-org/iree/actions/runs/43083092285/job/130746190224) | [1h05m](https://github.com/iree-org/iree/actions/runs/43068994089/job/130696579649) | [1h05m](https://github.com/iree-org/iree/actions/runs/43068994089/job/130696579649) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 11 | 2 | [28m53s](https://github.com/iree-org/iree/actions/runs/43083092285/job/130746190470) | 2026-11-11 11:39 PST | [28m57s](https://github.com/iree-org/iree/actions/runs/43068994089/job/130696579447) | [55m10s](https://github.com/iree-org/iree/actions/runs/43029517550/job/130556922197) | [55m10s](https://github.com/iree-org/iree/actions/runs/43029517550/job/130556922197) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 11 | 0 | — | — | [8m25s](https://github.com/iree-org/iree/actions/runs/43081682833/job/130753231053) | [52m08s](https://github.com/iree-org/iree/actions/runs/43068885344/job/130696588942) | [52m08s](https://github.com/iree-org/iree/actions/runs/43068885344/job/130696588942) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 11 | 1 | [15m59s](https://github.com/iree-org/iree/actions/runs/43081682833/job/130753230609) | 2026-11-11 11:39 PST | [12m46s](https://github.com/iree-org/iree/actions/runs/43068994089/job/130696579497) | [48m42s](https://github.com/iree-org/iree/actions/runs/43072655555/job/130708950391) | [48m42s](https://github.com/iree-org/iree/actions/runs/43072655555/job/130708950391) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 11 | 2 | [28m53s](https://github.com/iree-org/iree/actions/runs/43083092285/job/130746190170) | 2026-11-11 11:39 PST | [37m01s](https://github.com/iree-org/iree/actions/runs/43068437282/job/130695274641) | [48m16s](https://github.com/iree-org/iree/actions/runs/43029517550/job/130556922384) | [48m16s](https://github.com/iree-org/iree/actions/runs/43029517550/job/130556922384) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 11 | 0 | — | — | [10m09s](https://github.com/iree-org/iree/actions/runs/43072655555/job/130708951322) | [43m29s](https://github.com/iree-org/iree/actions/runs/43068437282/job/130695274122) | [43m29s](https://github.com/iree-org/iree/actions/runs/43068437282/job/130695274122) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 11 | 0 | — | — | [5m48s](https://github.com/iree-org/iree/actions/runs/43068994089/job/130696579202) | [35m38s](https://github.com/iree-org/iree/actions/runs/43044055649/job/130609072205) | [35m38s](https://github.com/iree-org/iree/actions/runs/43044055649/job/130609072205) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 11 | 2 | [28m53s](https://github.com/iree-org/iree/actions/runs/43083092285/job/130746190461) | 2026-11-11 11:39 PST | [16m23s](https://github.com/iree-org/iree/actions/runs/43057287695/job/130654873570) | [24m44s](https://github.com/iree-org/iree/actions/runs/43068994089/job/130696579483) | [24m44s](https://github.com/iree-org/iree/actions/runs/43068994089/job/130696579483) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 11 | 0 | — | — | [9m28s](https://github.com/iree-org/iree/actions/runs/43068437282/job/130695274161) | [27m58s](https://github.com/iree-org/iree/actions/runs/43072655555/job/130708950937) | [27m58s](https://github.com/iree-org/iree/actions/runs/43072655555/job/130708950937) | 2 |
| `.github/workflows/pkgci.yml` | Unit Test / Linux (x86_64) | `ubuntu-24.04` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43068437282/job/130695273444) | [4m55s](https://github.com/iree-org/iree/actions/runs/43068885344/job/130696588473) | [4m55s](https://github.com/iree-org/iree/actions/runs/43068885344/job/130696588473) | 11 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43068994089/job/130696579469) | [4m46s](https://github.com/iree-org/iree/actions/runs/43068885344/job/130696588772) | [4m46s](https://github.com/iree-org/iree/actions/runs/43068885344/job/130696588772) | 11 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43083092285/job/130746190460) | [4m41s](https://github.com/iree-org/iree/actions/runs/43068885344/job/130696589058) | [4m41s](https://github.com/iree-org/iree/actions/runs/43068885344/job/130696589058) | 11 |
| `.github/workflows/pkgci.yml` | Test TensorFlow / Linux (x86_64) | `ubuntu-24.04` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43083092285/job/130746190379) | [4m18s](https://github.com/iree-org/iree/actions/runs/43068885344/job/130696589172) | [4m18s](https://github.com/iree-org/iree/actions/runs/43068885344/job/130696589172) | 11 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64-baremetal | `ubuntu-24.04` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43072655555/job/130708950552) | [4m10s](https://github.com/iree-org/iree/actions/runs/43068885344/job/130696588755) | [4m10s](https://github.com/iree-org/iree/actions/runs/43068885344/job/130696588755) | 11 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 11 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/43081668474/job/130740413396) | [3m35s](https://github.com/iree-org/iree/actions/runs/43068885344/job/130696589186) | [3m35s](https://github.com/iree-org/iree/actions/runs/43068885344/job/130696589186) | 11 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 13 | 0 | — | — | [14s](https://github.com/iree-org/iree/actions/runs/43072655616/job/130704965306) | [3m02s](https://github.com/iree-org/iree/actions/runs/43029517491/job/130553936343) | [3m03s](https://github.com/iree-org/iree/actions/runs/43068434449/job/130689665316) | 13 |
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 13 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/43077902009/job/130722596601) | [2m43s](https://github.com/iree-org/iree/actions/runs/43068994196/job/130692746056) | [8m53s](https://github.com/iree-org/iree/actions/runs/43068885197/job/130691270091) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 13 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/43068434449/job/130689665359) | [2m37s](https://github.com/iree-org/iree/actions/runs/43068885197/job/130691269416) | [2m39s](https://github.com/iree-org/iree/actions/runs/43083092218/job/130740558692) | 13 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 386 | 1% (2/385) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 309 | 1% (2/308) | yes | running |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h01m (> 1h00m)
- **[high-failure-main]** `ubuntu-24.04` main-branch failure rate 21% (12/58)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
