# iree-ci-monitor

_Updated: 2026-10-29 15:49 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1100` | self-hosted | 18 | 0 | — | — | 0 | [2h24m](https://github.com/iree-org/iree/actions/runs/40919957091/job/123641249494) | [2h59m](https://github.com/iree-org/iree/actions/runs/40905257165/job/123564265041) | 0% (0/10) | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 18 | 0 | — | — | 0 | [2h06m](https://github.com/iree-org/iree/actions/runs/40906269591/job/123587713179) | [2h54m](https://github.com/iree-org/iree/actions/runs/40919047452/job/123613804801) | 0% (0/10) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 18 | 0 | — | — | 0 | [1h31m](https://github.com/iree-org/iree/actions/runs/40919047452/job/123613804785) | [2h44m](https://github.com/iree-org/iree/actions/runs/40906269591/job/123587713352) | 0% (0/10) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [1h25m](https://github.com/iree-org/iree/actions/runs/40919047452/job/123613804688) | [2h17m](https://github.com/iree-org/iree/actions/runs/40905257165/job/123564264936) | 0% (0/5) | `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 9 | 0 | — | — | 0 | [1h05m](https://github.com/iree-org/iree/actions/runs/40919047452/job/123613804544) | [2h05m](https://github.com/iree-org/iree/actions/runs/40906221380/job/123572854484) | 0% (0/5) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [1h09m](https://github.com/iree-org/iree/actions/runs/40919047452/job/123613804860) | [1h19m](https://github.com/iree-org/iree/actions/runs/40911293108/job/123587586199) | 0% (0/5) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 18 | 0 | — | — | 0 | [18m37s](https://github.com/iree-org/iree/actions/runs/40906221380/job/123572854686) | [56m08s](https://github.com/iree-org/iree/actions/runs/40914921696/job/123598551173) | 0% (0/10) | `shark55-ci`, `shark75-ci` |
| `azure-linux-scale` | ossci | 67 | 0 | — | — | 0 | [2m35s](https://github.com/iree-org/iree/actions/runs/40905257142/job/123558268553) | [21m11s](https://github.com/iree-org/iree/actions/runs/40920454672/job/123612040467) | 6% (2/36) | 67 |
| `ubuntu-24.04` | github-hosted | 204 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/40911293108/job/123587586463) | [7m12s](https://github.com/iree-org/iree/actions/runs/40905257165/job/123564265148) | 2% (2/104) | 201 |
| `ubuntu-24.04-arm` | github-hosted | 30 | 0 | — | — | 0 | [17s](https://github.com/iree-org/iree/actions/runs/40911293022/job/123582089681) | [4m12s](https://github.com/iree-org/iree/actions/runs/40905257142/job/123558268461) | 0% (0/15) | 30 |
| `macos-15` | github-hosted | 30 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/40920454672/job/123612039694) | [4m11s](https://github.com/iree-org/iree/actions/runs/40905257142/job/123558268248) | 0% (0/15) | 30 |
| `windows-2022` | github-hosted | 30 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/40914921682/job/123592587922) | [3m50s](https://github.com/iree-org/iree/actions/runs/40905257142/job/123558268281) | 0% (0/15) | 30 |
| `ubuntu-latest` | github-hosted | 27 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/40921276567/job/123614848596) | [2m07s](https://github.com/iree-org/iree/actions/runs/40906211160/job/123561561848) | 0% (0/15) | 27 |
| `azure-windows-scale` | ossci | 10 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/40911293022/job/123582090710) | [8s](https://github.com/iree-org/iree/actions/runs/40919957218/job/123610288025) | 0% (0/5) | 10 |
| `Linux,X64,iree-w7900` | self-hosted | 9 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 9 | 0 | — | — | [2h15m](https://github.com/iree-org/iree/actions/runs/40920454541/job/123653360254) | [3h13m](https://github.com/iree-org/iree/actions/runs/40914921696/job/123598551308) | [3h13m](https://github.com/iree-org/iree/actions/runs/40914921696/job/123598551308) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [2h07m](https://github.com/iree-org/iree/actions/runs/40919047452/job/123613804962) | [3h05m](https://github.com/iree-org/iree/actions/runs/40905257165/job/123564265097) | [3h05m](https://github.com/iree-org/iree/actions/runs/40905257165/job/123564265097) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [2h40m](https://github.com/iree-org/iree/actions/runs/40906269591/job/123587713355) | [3h03m](https://github.com/iree-org/iree/actions/runs/40919047452/job/123613804807) | [3h03m](https://github.com/iree-org/iree/actions/runs/40919047452/job/123613804807) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 9 | 0 | — | — | [1h55m](https://github.com/iree-org/iree/actions/runs/40914921696/job/123598551164) | [2h53m](https://github.com/iree-org/iree/actions/runs/40906221380/job/123572854866) | [2h53m](https://github.com/iree-org/iree/actions/runs/40906221380/job/123572854866) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [1h51m](https://github.com/iree-org/iree/actions/runs/40911293108/job/123587586772) | [2h51m](https://github.com/iree-org/iree/actions/runs/40914921696/job/123598551177) | [2h51m](https://github.com/iree-org/iree/actions/runs/40914921696/job/123598551177) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 9 | 0 | — | — | [1h25m](https://github.com/iree-org/iree/actions/runs/40919047452/job/123613804688) | [2h17m](https://github.com/iree-org/iree/actions/runs/40905257165/job/123564264936) | [2h17m](https://github.com/iree-org/iree/actions/runs/40905257165/job/123564264936) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 9 | 0 | — | — | [1h05m](https://github.com/iree-org/iree/actions/runs/40919047452/job/123613804544) | [2h05m](https://github.com/iree-org/iree/actions/runs/40906221380/job/123572854484) | [2h05m](https://github.com/iree-org/iree/actions/runs/40906221380/job/123572854484) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [1h24m](https://github.com/iree-org/iree/actions/runs/40911293108/job/123587586308) | [1h40m](https://github.com/iree-org/iree/actions/runs/40914921696/job/123598551441) | [1h40m](https://github.com/iree-org/iree/actions/runs/40914921696/job/123598551441) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 9 | 0 | — | — | [1h09m](https://github.com/iree-org/iree/actions/runs/40919047452/job/123613804860) | [1h19m](https://github.com/iree-org/iree/actions/runs/40911293108/job/123587586199) | [1h19m](https://github.com/iree-org/iree/actions/runs/40911293108/job/123587586199) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [39m29s](https://github.com/iree-org/iree/actions/runs/40906221380/job/123572854723) | [59m13s](https://github.com/iree-org/iree/actions/runs/40911293108/job/123587586292) | [59m13s](https://github.com/iree-org/iree/actions/runs/40911293108/job/123587586292) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [18m37s](https://github.com/iree-org/iree/actions/runs/40906221380/job/123572854686) | [44m19s](https://github.com/iree-org/iree/actions/runs/40914921696/job/123598551239) | [44m19s](https://github.com/iree-org/iree/actions/runs/40914921696/job/123598551239) | 2 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 10 | 0 | — | — | [2m03s](https://github.com/iree-org/iree/actions/runs/40905257165/job/123558245334) | [41m46s](https://github.com/iree-org/iree/actions/runs/40920454541/job/123612042613) | [41m46s](https://github.com/iree-org/iree/actions/runs/40920454541/job/123612042613) | 10 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 6 | 0 | — | — | [2m17s](https://github.com/iree-org/iree/actions/runs/40905257142/job/123558268683) | [41m30s](https://github.com/iree-org/iree/actions/runs/40920454672/job/123612040211) | [41m30s](https://github.com/iree-org/iree/actions/runs/40920454672/job/123612040211) | 6 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 10 | 0 | — | — | [1m18s](https://github.com/iree-org/iree/actions/runs/40905742360/job/123561681905) | [21m11s](https://github.com/iree-org/iree/actions/runs/40920454672/job/123612040467) | [21m11s](https://github.com/iree-org/iree/actions/runs/40920454672/job/123612040467) | 10 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 10 | 0 | — | — | [3m26s](https://github.com/iree-org/iree/actions/runs/40919047541/job/123607102328) | [19m53s](https://github.com/iree-org/iree/actions/runs/40920454672/job/123612040295) | [19m53s](https://github.com/iree-org/iree/actions/runs/40920454672/job/123612040295) | 10 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 11 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40919957218/job/123610287552) | [13m20s](https://github.com/iree-org/iree/actions/runs/40905742360/job/123561679378) | [13m20s](https://github.com/iree-org/iree/actions/runs/40905742360/job/123561679378) | 10 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 11 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40914921682/job/123592587331) | [10m51s](https://github.com/iree-org/iree/actions/runs/40905742360/job/123561678937) | [10m51s](https://github.com/iree-org/iree/actions/runs/40905742360/job/123561678937) | 10 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 10 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/40910077922/job/123577221445) | [10m41s](https://github.com/iree-org/iree/actions/runs/40905742360/job/123561679382) | [10m41s](https://github.com/iree-org/iree/actions/runs/40905742360/job/123561679382) | 10 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 9 | 0 | — | — | [44s](https://github.com/iree-org/iree/actions/runs/40919047452/job/123613804972) | [9m27s](https://github.com/iree-org/iree/actions/runs/40905257165/job/123564265290) | [9m27s](https://github.com/iree-org/iree/actions/runs/40905257165/job/123564265290) | 9 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 10 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/40914921682/job/123592587522) | [9m24s](https://github.com/iree-org/iree/actions/runs/40905257142/job/123558268457) | [9m24s](https://github.com/iree-org/iree/actions/runs/40905257142/job/123558268457) | 10 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 303 | 1% (4/303) |  | 1h54m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 248 | 2% (5/248) |  | 2h46m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 2h17m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h59m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h19m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h44m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h05m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h54m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
