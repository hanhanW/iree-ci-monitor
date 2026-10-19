# iree-ci-monitor

_Updated: 2026-10-18 21:48 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 6 | 0 | — | — | 0 | [34m50s](https://github.com/iree-org/iree/actions/runs/39161488320/job/117777441154) | [55m02s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778175015) | — | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | — | 0 | [27m45s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981427) | [54m33s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981408) | — | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [27m13s](https://github.com/iree-org/iree/actions/runs/39161488320/job/117777441133) | [51m26s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778174905) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 0 | — | — | 0 | [26m39s](https://github.com/iree-org/iree/actions/runs/39161488320/job/117777441381) | [41m26s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778175032) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 0 | — | — | 0 | [22m30s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981294) | [39m23s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778174949) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | — | 0 | [3m24s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981281) | [37m14s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778174868) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 0 | — | — | 0 | [18m08s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981202) | [24m55s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778175020) | — | `shark75-ci` |
| `macos-15` | github-hosted | 9 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/39161488353/job/117775590714) | [2m12s](https://github.com/iree-org/iree/actions/runs/39161698626/job/117776396152) | — | 9 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/39161698626/job/117776395975) | [2m04s](https://github.com/iree-org/iree/actions/runs/39161698626/job/117776396155) | — | 9 |
| `ubuntu-24.04` | github-hosted | 74 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39161620156/job/117775976866) | [1m53s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981413) | 0% (0/5) | 69 |
| `windows-2022` | github-hosted | 9 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/39161698626/job/117776395983) | [1m30s](https://github.com/iree-org/iree/actions/runs/39161620156/job/117775976975) | — | 9 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [46s](https://github.com/iree-org/iree/actions/runs/39161696096/job/117776152413) | [52s](https://github.com/iree-org/iree/actions/runs/39161696096/job/117776152435) | — | 3 |
| `azure-linux-scale` | ossci | 18 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/39161620156/job/117775977046) | [9s](https://github.com/iree-org/iree/actions/runs/39161488353/job/117775590766) | — | 18 |
| `azure-windows-scale` | ossci | 3 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/39161488353/job/117775590786) | [1s](https://github.com/iree-org/iree/actions/runs/39161620156/job/117775977098) | — | 3 |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [39m55s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981446) | [55m02s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778175015) | [55m02s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778175015) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 0 | — | — | [37m54s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778175014) | [54m33s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981408) | [54m33s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981408) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 0 | — | — | [27m13s](https://github.com/iree-org/iree/actions/runs/39161488320/job/117777441133) | [51m26s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778174905) | [51m26s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778174905) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 0 | — | — | [34m50s](https://github.com/iree-org/iree/actions/runs/39161488320/job/117777441154) | [46m13s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981323) | [46m13s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981323) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 0 | — | — | [27m45s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981427) | [43m36s](https://github.com/iree-org/iree/actions/runs/39161488320/job/117777441252) | [43m36s](https://github.com/iree-org/iree/actions/runs/39161488320/job/117777441252) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [30m37s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981335) | [41m26s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778175032) | [41m26s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778175032) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 0 | — | — | [22m30s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981294) | [39m23s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778174949) | [39m23s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778174949) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [3m24s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981281) | [37m14s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778174868) | [37m14s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778174868) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 3 | 0 | — | — | [26m39s](https://github.com/iree-org/iree/actions/runs/39161488320/job/117777441381) | [28m15s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778175037) | [28m15s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778175037) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 0 | — | — | [18m08s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981202) | [24m55s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778175020) | [24m55s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778175020) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 3 | 0 | — | — | [7m11s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981295) | [8m47s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778174835) | [8m47s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778174835) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: tracy | `macos-15` | 3 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/39161620156/job/117775976887) | [2m12s](https://github.com/iree-org/iree/actions/runs/39161698626/job/117776396152) | [2m12s](https://github.com/iree-org/iree/actions/runs/39161698626/job/117776396152) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 3 | 0 | — | — | [18s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981343) | [2m12s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778174951) | [2m12s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778174951) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39161620156/job/117775976877) | [2m07s](https://github.com/iree-org/iree/actions/runs/39161698626/job/117776396147) | [2m07s](https://github.com/iree-org/iree/actions/runs/39161698626/job/117776396147) | 3 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 3 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/39161620156/job/117775976964) | [2m04s](https://github.com/iree-org/iree/actions/runs/39161698626/job/117776396155) | [2m04s](https://github.com/iree-org/iree/actions/runs/39161698626/job/117776396155) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39161488320/job/117777441249) | [1m59s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778174891) | [1m59s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778174891) | 3 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 3 | 0 | — | — | [1m10s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778175065) | [1m53s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981413) | [1m53s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981413) | 3 |
| `.github/workflows/pkgci.yml` | Test Android / android_arm64 | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981347) | [1m41s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778175006) | [1m41s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778175006) | 3 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 3 | 0 | — | — | [52s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981438) | [1m35s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778174925) | [1m35s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778174925) | 3 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/39161619357/job/117777981228) | [1m33s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778175068) | [1m33s](https://github.com/iree-org/iree/actions/runs/39161698611/job/117778175068) | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 320 | 3% (11/320) |  | 7h37m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 263 | 1% (2/263) |  | 7h45m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
