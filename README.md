# iree-ci-monitor

_Updated: 2026-09-14 21:58 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | — | 0 | [16m34s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736702) | [27m24s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736790) | — | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [18m10s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736794) | [23m15s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736651) | — | `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [21m14s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736777) | [21m14s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736777) | — | `shark01-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [13m22s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736553) | [13m22s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736553) | — | `shark01-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [12m45s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736578) | [12m45s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736578) | — | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [3m59s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736677) | [10m49s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736637) | — | `shark01-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736581) | [7m55s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736726) | — | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [5m48s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736602) | [5m48s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736602) | — | `shark75-ci` |
| `azure-linux-scale` | ossci | 5 | 0 | — | — | 0 | [1m40s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899873) | [3m37s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899831) | — | 5 |
| `ubuntu-24.04` | github-hosted | 24 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736533) | [38s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736585) | 0% (0/3) | 22 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899797) | [7s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899813) | — | 3 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899722) | [5s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899768) | — | 3 |
| `windows-2022` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899704) | [3s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899738) | — | 3 |
| `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/34900304101/job/104164406813) | [3s](https://github.com/iree-org/iree/actions/runs/34900308843/job/104164423077) | 0% (0/2) | 2 |
| `azure-windows-scale` | ossci | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899871) | [2s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899871) | — | 1 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736457) | [1s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736457) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736627) | [1s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736627) | — | `shark01-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 1 | [7h00m](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736563) | 2026-09-14 21:58 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [7h00m](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736563) | 2026-09-14 21:58 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `dependabot/github_actions/github-actions-177be4f125` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 1 | 1 | [7h00m](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736563) | 2026-09-14 21:58 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [27m24s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736790) | [27m24s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736790) | [27m24s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736790) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [23m15s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736651) | [23m15s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736651) | [23m15s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736651) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 1 | 0 | — | — | [21m14s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736777) | [21m14s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736777) | [21m14s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736777) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 1 | 0 | — | — | [18m10s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736794) | [18m10s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736794) | [18m10s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736794) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 1 | 0 | — | — | [16m34s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736702) | [16m34s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736702) | [16m34s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736702) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [13m22s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736553) | [13m22s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736553) | [13m22s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736553) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 1 | 0 | — | — | [12m45s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736578) | [12m45s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736578) | [12m45s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736578) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [10m49s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736637) | [10m49s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736637) | [10m49s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736637) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [7m55s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736726) | [7m55s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736726) | [7m55s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736726) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 1 | 0 | — | — | [5m48s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736602) | [5m48s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736602) | [5m48s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736602) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [3m59s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736677) | [3m59s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736677) | [3m59s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736677) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 1 | 0 | — | — | [3m37s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899831) | [3m37s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899831) | [3m37s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899831) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 1 | 0 | — | — | [2m41s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899784) | [2m41s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899784) | [2m41s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899784) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 0 | — | — | [1m40s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899873) | [1m40s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899873) | [1m40s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899873) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 1 | 0 | — | — | [1m28s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899840) | [1m28s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899840) | [1m28s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899840) | 1 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 1 | 0 | — | — | [38s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736585) | [38s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736585) | [38s](https://github.com/iree-org/iree/actions/runs/34901052587/job/104168736585) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [38s](https://github.com/iree-org/iree/actions/runs/34928672855/job/104252098296) | [38s](https://github.com/iree-org/iree/actions/runs/34928672855/job/104252098296) | [38s](https://github.com/iree-org/iree/actions/runs/34928672855/job/104252098296) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899797) | [7s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899797) | [7s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899797) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899813) | [7s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899813) | [7s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899813) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 294 | 1% (4/294) |  | 6h28m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 220 | 1% (2/220) |  | 6h30m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 224 | 2% (4/224) |  | 6h34m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 263 | 8% (22/263) |  | 13h13m ago |

## Alerts

- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job observed waiting 7h00m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
