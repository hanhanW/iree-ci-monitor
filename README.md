# iree-ci-monitor

_Updated: 2026-11-24 01:59 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 2 | 1 | [10m38s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207955) | 2026-11-24 01:59 PST | 1 | [9m33s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357208637) | [9m33s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357208637) | — | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 1 | [10m38s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357208552) | 2026-11-24 01:59 PST | 1 | [7m06s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207828) | [7m06s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207828) | — | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [6m56s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207524) | [6m56s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207524) | — | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [3m26s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207533) | [3m26s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207533) | — | `shark75-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 1 | [1m54s](https://github.com/iree-org/iree/actions/runs/45364072923/job/138341154139) | [1m54s](https://github.com/iree-org/iree/actions/runs/45364072923/job/138341154139) | — | 1 |
| `azure-linux-scale` | ossci | 8 | 0 | — | — | 5 | [8s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353631372) | [1m03s](https://github.com/iree-org/iree/actions/runs/45364071559/job/138341148852) | 50% (1/2) | 8 |
| `macos-15` | github-hosted | 6 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/45364062105/job/138341114398) | [7s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353630461) | — | 6 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/45331522825/job/138233735203) | [5s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353630878) | — | 6 |
| `ubuntu-24.04` | github-hosted | 35 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207407) | [3s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353630776) | 0% (0/4) | 34 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/45366811809/job/138350542265) | [3s](https://github.com/iree-org/iree/actions/runs/45366811809/job/138350542140) | — | 3 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207528) | [2s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207623) | — | `shark55-ci`, `shark75-ci` |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353630407) | [2s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353630801) | — | 5 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353631087) | [1s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353631087) | — | 1 |
| `Linux,X64,gfx1100` | self-hosted | 2 | 2 | [10m38s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207815) | 2026-11-24 01:59 PST | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 1 | [10m38s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207907) | 2026-11-24 01:59 PST | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [10m38s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207815) | 2026-11-24 01:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `docs-ai-tool-use-policy` | pull_request |
| [10m38s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207907) | 2026-11-24 01:59 PST | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `docs-ai-tool-use-policy` | pull_request |
| [10m38s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207955) | 2026-11-24 01:59 PST | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `docs-ai-tool-use-policy` | pull_request |
| [10m38s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357208463) | 2026-11-24 01:59 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `docs-ai-tool-use-policy` | pull_request |
| [10m38s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357208552) | 2026-11-24 01:59 PST | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `docs-ai-tool-use-policy` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 1 | [10m38s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207907) | 2026-11-24 01:59 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 1 | [10m38s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207815) | 2026-11-24 01:59 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 1 | [10m38s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207955) | 2026-11-24 01:59 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 1 | [10m38s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357208463) | 2026-11-24 01:59 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 1 | [10m38s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357208552) | 2026-11-24 01:59 PST | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [9m33s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357208637) | [9m33s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357208637) | [9m33s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357208637) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [7m06s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207828) | [7m06s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207828) | [7m06s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207828) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [6m56s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207524) | [6m56s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207524) | [6m56s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207524) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [3m26s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207533) | [3m26s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207533) | [3m26s](https://github.com/iree-org/iree/actions/runs/45367654995/job/138357207533) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m54s](https://github.com/iree-org/iree/actions/runs/45364072923/job/138341154139) | [1m54s](https://github.com/iree-org/iree/actions/runs/45364072923/job/138341154139) | [1m54s](https://github.com/iree-org/iree/actions/runs/45364072923/job/138341154139) | 1 |
| `.github/workflows/ci_linux_x64_clang_tsan.yml` | linux_x64_clang_tsan | `azure-linux-scale` | 1 | 0 | — | — | [1m03s](https://github.com/iree-org/iree/actions/runs/45364071559/job/138341148852) | [1m03s](https://github.com/iree-org/iree/actions/runs/45364071559/job/138341148852) | [1m03s](https://github.com/iree-org/iree/actions/runs/45364071559/job/138341148852) | 1 |
| `.github/workflows/ci_linux_x64_clang_debug.yml` | linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [22s](https://github.com/iree-org/iree/actions/runs/45363998778/job/138340896702) | [22s](https://github.com/iree-org/iree/actions/runs/45363998778/job/138340896702) | [22s](https://github.com/iree-org/iree/actions/runs/45363998778/job/138340896702) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353633604) | [11s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353633604) | [11s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353633604) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353631176) | [8s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353631176) | [8s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353631176) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353631372) | [8s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353631372) | [8s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353631372) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353630985) | [7s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353630985) | [7s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353630985) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353630461) | [7s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353630461) | [7s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353630461) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353630878) | [5s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353630878) | [5s](https://github.com/iree-org/iree/actions/runs/45367655246/job/138353630878) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/45331522825/job/138233735070) | [4s](https://github.com/iree-org/iree/actions/runs/45331522825/job/138233735070) | [4s](https://github.com/iree-org/iree/actions/runs/45331522825/job/138233735070) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/45331522825/job/138233735203) | [4s](https://github.com/iree-org/iree/actions/runs/45331522825/job/138233735203) | [4s](https://github.com/iree-org/iree/actions/runs/45331522825/job/138233735203) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 124 | 5% (6/123) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 92 | 4% (4/91) | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d
- **[spof]** `ah-ubuntu_22_04-c7g_4x-50` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
