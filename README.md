# iree-ci-monitor

_Updated: 2026-10-15 04:36 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [15m03s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015364) | [23m16s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015437) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [14m18s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015385) | [18m15s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015367) | — | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [6m49s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015381) | [16m04s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015391) | — | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [11m34s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015282) | [11m34s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015282) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015253) | [4m21s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015341) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [3m16s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015435) | [3m16s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015435) | — | `shark55-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m27s](https://github.com/iree-org/iree/actions/runs/38713201392/job/116349449223) | [1m27s](https://github.com/iree-org/iree/actions/runs/38713201392/job/116349449223) | 100% (1/1) | 1 |
| `azure-linux-scale` | ossci | 8 | 0 | — | — | 0 | [13s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796619) | [17s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796904) | 50% (1/2) | 8 |
| `macos-15` | github-hosted | 6 | 0 | — | — | 1 | [7s](https://github.com/iree-org/iree/actions/runs/38685825787/job/116260347708) | [9s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796710) | — | 6 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/38685825787/job/116260347582) | [5s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796695) | — | 6 |
| `ubuntu-24.04` | github-hosted | 40 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/38678272679/job/116236741402) | [3s](https://github.com/iree-org/iree/actions/runs/38663624196/job/116203457254) | 0% (0/4) | 38 |
| `windows-2022` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796705) | [2s](https://github.com/iree-org/iree/actions/runs/38685825787/job/116260347592) | — | 5 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38725029583/job/116388636536) | [2s](https://github.com/iree-org/iree/actions/runs/38725029583/job/116388636751) | — | 3 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015164) | [1s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015164) | — | `shark75-ci` |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796853) | [1s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796853) | — | 1 |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [23m16s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015437) | [23m16s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015437) | [23m16s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015437) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [18m15s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015367) | [18m15s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015367) | [18m15s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015367) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [16m04s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015391) | [16m04s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015391) | [16m04s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015391) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [15m03s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015364) | [15m03s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015364) | [15m03s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015364) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [14m18s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015385) | [14m18s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015385) | [14m18s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015385) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [11m34s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015282) | [11m34s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015282) | [11m34s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015282) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [6m49s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015381) | [6m49s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015381) | [6m49s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015381) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [4m21s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015341) | [4m21s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015341) | [4m21s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015341) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [3m16s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015435) | [3m16s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015435) | [3m16s](https://github.com/iree-org/iree/actions/runs/38678272646/job/116239015435) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m27s](https://github.com/iree-org/iree/actions/runs/38713201392/job/116349449223) | [1m27s](https://github.com/iree-org/iree/actions/runs/38713201392/job/116349449223) | [1m27s](https://github.com/iree-org/iree/actions/runs/38713201392/job/116349449223) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [17s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796904) | [17s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796904) | [17s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796904) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [14s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796844) | [14s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796844) | [14s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796844) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 1 | 0 | — | — | [14s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796810) | [14s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796810) | [14s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796810) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [13s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796619) | [13s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796619) | [13s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796619) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796561) | [12s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796561) | [12s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796561) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796710) | [9s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796710) | [9s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796710) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796743) | [8s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796743) | [8s](https://github.com/iree-org/iree/actions/runs/38678272834/job/116236796743) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/38724743630/job/116388307790) | [8s](https://github.com/iree-org/iree/actions/runs/38724743630/job/116388307790) | [8s](https://github.com/iree-org/iree/actions/runs/38724743630/job/116388307790) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-15` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/38685825787/job/116260347708) | [7s](https://github.com/iree-org/iree/actions/runs/38685825787/job/116260347708) | [7s](https://github.com/iree-org/iree/actions/runs/38685825787/job/116260347708) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-15` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/38685825787/job/116260347768) | [7s](https://github.com/iree-org/iree/actions/runs/38685825787/job/116260347768) | [7s](https://github.com/iree-org/iree/actions/runs/38685825787/job/116260347768) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 281 | 1% (2/281) |  | 7h12m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 365 | 8% (30/365) |  | 7h14m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
