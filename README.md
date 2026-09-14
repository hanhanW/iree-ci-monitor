# iree-ci-monitor

_Updated: 2026-09-14 14:52 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | — | 0 | [13m28s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938484) | [13m28s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938484) | 100% (1/1) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | — | 0 | [13m24s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938220) | [13m24s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938220) | 0% (0/1) | `shark01-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | — | 0 | [12m57s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938670) | [12m57s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938670) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | — | 0 | [9m42s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938867) | [9m42s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938867) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 3 | 1 | [2h00m](https://github.com/iree-org/iree/actions/runs/34581758865/job/103214541971) | 2026-09-11 04:27 PDT | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938330) | [8m26s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938520) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | — | 0 | [4m43s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938478) | [5m03s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938319) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938387) | [4m03s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938403) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `azure-linux-scale` | ossci | 11 | 4 | [1m01s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899784) | 2026-09-14 14:52 PDT | 1 | [10s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037594) | [1m14s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035038355) | 0% (0/6) | 7 |
| `macos-14` | github-hosted | 6 | 0 | — | — | 3 | [7s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899813) | [12s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037296) | 0% (0/3) | 6 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | — | 3 | [5s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037610) | [6s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037623) | 0% (0/3) | 6 |
| `ubuntu-24.04` | github-hosted | 29 | 0 | — | — | 6 | [2s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899654) | [4s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037384) | 5% (1/19) | 27 |
| `windows-2022` | github-hosted | 6 | 0 | — | — | 3 | [3s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037504) | [3s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899738) | 0% (0/3) | 6 |
| `ubuntu-latest` | github-hosted | 5 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/34861603041/job/104034968821) | [3s](https://github.com/iree-org/iree/actions/runs/34900308843/job/104164423077) | 0% (0/5) | 5 |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035038210) | [2s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899871) | 0% (0/1) | 2 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938314) | [2s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938314) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938562) | [2s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938562) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0% (0/1) | 0 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | — | 0 | 0s | 0s | 0% (0/1) | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [1m01s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899784) | 2026-09-14 14:52 PDT | `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | `dependabot/github_actions/github-actions-177be4f125` | pull_request |
| [1m01s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899831) | 2026-09-14 14:52 PDT | `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | `dependabot/github_actions/github-actions-177be4f125` | pull_request |
| [1m01s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899840) | 2026-09-14 14:52 PDT | `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | `dependabot/github_actions/github-actions-177be4f125` | pull_request |
| [1m01s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899873) | 2026-09-14 14:52 PDT | `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | `dependabot/github_actions/github-actions-177be4f125` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 1 | [2h00m](https://github.com/iree-org/iree/actions/runs/34581758865/job/103214541971) | 2026-09-11 04:27 PDT | [8m26s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938520) | [8m26s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938520) | [8m26s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938520) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 1 | 0 | — | — | [13m28s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938484) | [13m28s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938484) | [13m28s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938484) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 1 | 0 | — | — | [13m24s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938220) | [13m24s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938220) | [13m24s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938220) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 1 | 0 | — | — | [12m57s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938670) | [12m57s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938670) | [12m57s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938670) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 0 | — | — | [9m42s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938867) | [9m42s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938867) | [9m42s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938867) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [5m03s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938319) | [5m03s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938319) | [5m03s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938319) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 1 | 0 | — | — | [4m43s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938478) | [4m43s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938478) | [4m43s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938478) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 0 | — | — | [4m03s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938403) | [4m03s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938403) | [4m03s](https://github.com/iree-org/iree/actions/runs/34861604351/job/104037938403) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 1 | [1m01s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899784) | 2026-09-14 14:52 PDT | [1m14s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035038355) | [1m14s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035038355) | [1m14s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035038355) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 1 | [1m01s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899873) | 2026-09-14 14:52 PDT | [1m14s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035038029) | [1m14s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035038029) | [1m14s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035038029) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 2 | 1 | [1m01s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899840) | 2026-09-14 14:52 PDT | [9s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037560) | [9s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037560) | [9s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037560) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 1 | [1m01s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899831) | 2026-09-14 14:52 PDT | [10s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037594) | [10s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037594) | [10s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037594) | 1 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 2 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899797) | [12s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037296) | [12s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037296) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 2 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899741) | [11s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037660) | [11s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037660) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037604) | [10s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037604) | [10s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037604) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 2 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899813) | [9s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037463) | [9s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037463) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 2 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899722) | [6s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037623) | [6s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037623) | 2 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 2 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899635) | [5s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037266) | [5s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037266) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 2 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037610) | [5s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899768) | [5s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899768) | 2 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34901052562/job/104166899654) | [4s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037384) | [4s](https://github.com/iree-org/iree/actions/runs/34861604296/job/104035037384) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 294 | 1% (4/294) |  | 6h04m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 223 | 2% (4/223) |  | 6h04m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 218 | 1% (2/218) |  | 6h05m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 267 | 8% (22/267) |  | 6h07m ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 2h00m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
