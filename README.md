# iree-ci-monitor

_Updated: 2026-08-17 11:59 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 12 | 0 | — | — | 0 | [30m12s](https://github.com/iree-org/iree/actions/runs/32013688219/job/95344494549) | [1h12m](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347554067) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | — | 0 | [14m29s](https://github.com/iree-org/iree/actions/runs/32030584485/job/95391572692) | [1h03m](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347553697) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 0 | — | — | 0 | [7m54s](https://github.com/iree-org/iree/actions/runs/32032251740/job/95396550866) | [53m22s](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347553796) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 6 | 0 | — | — | 0 | [18m04s](https://github.com/iree-org/iree/actions/runs/32032251740/job/95396550771) | [52m24s](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347554042) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [23m25s](https://github.com/iree-org/iree/actions/runs/32013688219/job/95344494386) | [50m23s](https://github.com/iree-org/iree/actions/runs/32030584485/job/95391572860) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | — | 0 | [8m42s](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347554268) | [33m52s](https://github.com/iree-org/iree/actions/runs/32013688219/job/95344494665) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [12m04s](https://github.com/iree-org/iree/actions/runs/32030584485/job/95391572805) | [27m26s](https://github.com/iree-org/iree/actions/runs/32018753080/job/95355864806) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | — | 0 | [9m42s](https://github.com/iree-org/iree/actions/runs/32013688219/job/95344494504) | [26m58s](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347554140) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 0 | — | — | 0 | [4m04s](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347554048) | [24m06s](https://github.com/iree-org/iree/actions/runs/32018753080/job/95355864662) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 12 | 0 | — | — | 0 | [4m51s](https://github.com/iree-org/iree/actions/runs/32030584485/job/95391572787) | [22m24s](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347554181) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 6 | 0 | — | — | 0 | [4m40s](https://github.com/iree-org/iree/actions/runs/32030584485/job/95391572911) | [22m19s](https://github.com/iree-org/iree/actions/runs/32032251740/job/95396551080) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m29s](https://github.com/iree-org/iree/actions/runs/32015151779/job/95342932036) | [1m29s](https://github.com/iree-org/iree/actions/runs/32015151779/job/95342932036) | 0% (0/1) | 1 |
| `ubuntu-24.04` | github-hosted | 128 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32032251723/job/95394721558) | [1m12s](https://github.com/iree-org/iree/actions/runs/32014244935/job/95342421552) | 5% (1/22) | 126 |
| `macos-14` | github-hosted | 19 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/32014244668/job/95340245310) | [1m07s](https://github.com/iree-org/iree/actions/runs/32018752993/job/95353784657) | 0% (0/4) | 19 |
| `azure-linux-scale` | ossci | 33 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/32015897578/job/95345667987) | [1m05s](https://github.com/iree-org/iree/actions/runs/32014244668/job/95340245362) | 0% (0/8) | 33 |
| `windows-2022` | github-hosted | 18 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/32013688305/job/95342336193) | [6s](https://github.com/iree-org/iree/actions/runs/32015897578/job/95345667904) | 0% (0/3) | 18 |
| `ubuntu-24.04-arm` | github-hosted | 18 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/32015897578/job/95345667907) | [5s](https://github.com/iree-org/iree/actions/runs/32032251723/job/95394721786) | 0% (0/3) | 18 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32024557768/job/95371116078) | [3s](https://github.com/iree-org/iree/actions/runs/32030582808/job/95389461651) | 0% (0/3) | 12 |
| `azure-windows-scale` | ossci | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/32014244668/job/95340245410) | [2s](https://github.com/iree-org/iree/actions/runs/32032251723/job/95394721883) | 0% (0/1) | 6 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [42m22s](https://github.com/iree-org/iree/actions/runs/32032251740/job/95396550856) | [1h12m](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347554067) | [1h12m](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347554067) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 6 | 0 | — | — | [15m35s](https://github.com/iree-org/iree/actions/runs/32032251740/job/95396551199) | [1h08m](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347554128) | [1h08m](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347554128) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 6 | 0 | — | — | [14m29s](https://github.com/iree-org/iree/actions/runs/32030584485/job/95391572692) | [1h03m](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347553697) | [1h03m](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347553697) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 6 | 0 | — | — | [7m54s](https://github.com/iree-org/iree/actions/runs/32032251740/job/95396550866) | [53m22s](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347553796) | [53m22s](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347553796) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 6 | 0 | — | — | [18m04s](https://github.com/iree-org/iree/actions/runs/32032251740/job/95396550771) | [52m24s](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347554042) | [52m24s](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347554042) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 6 | 0 | — | — | [23m25s](https://github.com/iree-org/iree/actions/runs/32013688219/job/95344494386) | [50m23s](https://github.com/iree-org/iree/actions/runs/32030584485/job/95391572860) | [50m23s](https://github.com/iree-org/iree/actions/runs/32030584485/job/95391572860) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [10m02s](https://github.com/iree-org/iree/actions/runs/32032251740/job/95396551253) | [33m52s](https://github.com/iree-org/iree/actions/runs/32013688219/job/95344494665) | [33m52s](https://github.com/iree-org/iree/actions/runs/32013688219/job/95344494665) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 6 | 0 | — | — | [12m04s](https://github.com/iree-org/iree/actions/runs/32030584485/job/95391572805) | [27m26s](https://github.com/iree-org/iree/actions/runs/32018753080/job/95355864806) | [27m26s](https://github.com/iree-org/iree/actions/runs/32018753080/job/95355864806) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 0 | — | — | [9m42s](https://github.com/iree-org/iree/actions/runs/32013688219/job/95344494504) | [26m58s](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347554140) | [26m58s](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347554140) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 0 | — | — | [4m04s](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347554048) | [24m06s](https://github.com/iree-org/iree/actions/runs/32018753080/job/95355864662) | [24m06s](https://github.com/iree-org/iree/actions/runs/32018753080/job/95355864662) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 0 | — | — | [6m44s](https://github.com/iree-org/iree/actions/runs/32014244935/job/95342421685) | [23m14s](https://github.com/iree-org/iree/actions/runs/32013688219/job/95344494686) | [23m14s](https://github.com/iree-org/iree/actions/runs/32013688219/job/95344494686) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [2m45s](https://github.com/iree-org/iree/actions/runs/32013688219/job/95344494459) | [22m24s](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347554181) | [22m24s](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347554181) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 6 | 0 | — | — | [4m40s](https://github.com/iree-org/iree/actions/runs/32030584485/job/95391572911) | [22m19s](https://github.com/iree-org/iree/actions/runs/32032251740/job/95396551080) | [22m19s](https://github.com/iree-org/iree/actions/runs/32032251740/job/95396551080) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 6 | 0 | — | — | [5m55s](https://github.com/iree-org/iree/actions/runs/32013688219/job/95344494556) | [17m10s](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347554001) | [17m10s](https://github.com/iree-org/iree/actions/runs/32015897607/job/95347554001) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 0 | — | — | [7m48s](https://github.com/iree-org/iree/actions/runs/32013688219/job/95344494445) | [13m41s](https://github.com/iree-org/iree/actions/runs/32018753080/job/95355864636) | [13m41s](https://github.com/iree-org/iree/actions/runs/32018753080/job/95355864636) | 2 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32032251740/job/95396550960) | [2m21s](https://github.com/iree-org/iree/actions/runs/32014244935/job/95342421614) | [2m21s](https://github.com/iree-org/iree/actions/runs/32014244935/job/95342421614) | 6 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32018753080/job/95355864716) | [1m50s](https://github.com/iree-org/iree/actions/runs/32014244935/job/95342421586) | [1m50s](https://github.com/iree-org/iree/actions/runs/32014244935/job/95342421586) | 6 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 6 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/32018753080/job/95355864607) | [1m45s](https://github.com/iree-org/iree/actions/runs/32014244935/job/95342421663) | [1m45s](https://github.com/iree-org/iree/actions/runs/32014244935/job/95342421663) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 6 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/32032251723/job/95394721925) | [1m35s](https://github.com/iree-org/iree/actions/runs/32030584672/job/95389528056) | [1m35s](https://github.com/iree-org/iree/actions/runs/32030584672/job/95389528056) | 6 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m29s](https://github.com/iree-org/iree/actions/runs/32015151779/job/95342932036) | [1m29s](https://github.com/iree-org/iree/actions/runs/32015151779/job/95342932036) | [1m29s](https://github.com/iree-org/iree/actions/runs/32015151779/job/95342932036) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 233 | 0% (1/233) |  | 5h05m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 188 | 3% (6/188) |  | 5h30m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 160 | 8% (12/160) |  | 5h33m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 196 | 6% (12/196) |  | 5h35m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h12m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h03m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
