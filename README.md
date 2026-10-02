# iree-ci-monitor

_Updated: 2026-10-02 05:43 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 1 | [22m32s](https://github.com/iree-org/iree/actions/runs/37005242492/job/110834612021) | 2026-10-02 05:42 PDT | 0 | [38m34s](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654349) | [38m34s](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654349) | — | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 1 | [22m32s](https://github.com/iree-org/iree/actions/runs/37005242492/job/110834612118) | 2026-10-02 05:42 PDT | 0 | [12m14s](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654368) | [32m53s](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654131) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 1 | [22m22s](https://github.com/iree-org/iree/actions/runs/37005242492/job/110834611957) | [23m20s](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654130) | — | `shark75-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m35s](https://github.com/iree-org/iree/actions/runs/36990074123/job/110783975134) | [1m35s](https://github.com/iree-org/iree/actions/runs/36990074123/job/110783975134) | 100% (1/1) | 1 |
| `azure-linux-scale` | ossci | 12 | 0 | — | — | 2 | [8s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831928139) | [1m29s](https://github.com/iree-org/iree/actions/runs/37005242492/job/110831930143) | 50% (1/2) | 12 |
| `macos-14` | github-hosted | 9 | 0 | — | — | 1 | [7s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831927862) | [9s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831927705) | — | 9 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/36968248175/job/110716624021) | [5s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831927815) | — | 9 |
| `windows-2022` | github-hosted | 8 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831927736) | [4s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831927913) | — | 8 |
| `ubuntu-24.04` | github-hosted | 57 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654344) | [3s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831927846) | 56% (5/9) | 55 |
| `ubuntu-latest` | github-hosted | 3 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/36990430520/job/110785105495) | [3s](https://github.com/iree-org/iree/actions/runs/36990430520/job/110785105855) | — | 3 |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654137) | [2s](https://github.com/iree-org/iree/actions/runs/37005242492/job/110834611732) | — | `shark75-ci` |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/36990435254/job/110803251718) | [1s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831928537) | — | 2 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 6 | [19h50m](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464282) | 2026-10-02 05:42 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 12 | 12 | [19h50m](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464313) | 2026-10-02 05:42 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 12 | 12 | [19h50m](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464341) | 2026-10-02 05:42 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 6 | 6 | [19h50m](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464546) | 2026-10-02 05:42 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [19h50m](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464282) | 2026-10-02 05:42 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |
| [19h50m](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464313) | 2026-10-02 05:42 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [19h50m](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464341) | 2026-10-02 05:42 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [19h50m](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464413) | 2026-10-02 05:42 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [19h50m](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464458) | 2026-10-02 05:42 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [19h50m](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464546) | 2026-10-02 05:42 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `main` | push |
| [17h41m](https://github.com/iree-org/iree/actions/runs/36908228839/job/110534196439) | 2026-10-02 05:42 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `integrates/llvm-20261001` | pull_request |
| [17h41m](https://github.com/iree-org/iree/actions/runs/36908228839/job/110534196554) | 2026-10-02 05:42 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `integrates/llvm-20261001` | pull_request |
| [17h41m](https://github.com/iree-org/iree/actions/runs/36908228839/job/110534196620) | 2026-10-02 05:42 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `integrates/llvm-20261001` | pull_request |
| [17h41m](https://github.com/iree-org/iree/actions/runs/36908228839/job/110534196654) | 2026-10-02 05:42 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `integrates/llvm-20261001` | pull_request |
| [17h41m](https://github.com/iree-org/iree/actions/runs/36908228839/job/110534196959) | 2026-10-02 05:42 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `integrates/llvm-20261001` | pull_request |
| [17h41m](https://github.com/iree-org/iree/actions/runs/36908228839/job/110534196973) | 2026-10-02 05:42 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `integrates/llvm-20261001` | pull_request |
| [16h26m](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700507) | 2026-10-02 05:42 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `main` | push |
| [16h26m](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700524) | 2026-10-02 05:42 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [16h26m](https://github.com/iree-org/iree/actions/runs/36916799758/job/110564700530) | 2026-10-02 05:42 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 6 | 6 | [19h50m](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464282) | 2026-10-02 05:42 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 6 | 6 | [19h50m](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464546) | 2026-10-02 05:42 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 6 | 6 | [19h50m](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464313) | 2026-10-02 05:42 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 6 | 6 | [19h50m](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464341) | 2026-10-02 05:42 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 6 | 6 | [19h50m](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464458) | 2026-10-02 05:42 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 6 | 6 | [19h50m](https://github.com/iree-org/iree/actions/runs/36894148757/job/110480464413) | 2026-10-02 05:42 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 1 | [22m32s](https://github.com/iree-org/iree/actions/runs/37005242492/job/110834612021) | 2026-10-02 05:42 PDT | [38m34s](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654349) | [38m34s](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654349) | [38m34s](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654349) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [7m02s](https://github.com/iree-org/iree/actions/runs/37005242492/job/110834612261) | [32m53s](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654131) | [32m53s](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654131) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [12m31s](https://github.com/iree-org/iree/actions/runs/37005242492/job/110834611909) | [23m20s](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654130) | [23m20s](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654130) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 1 | [22m32s](https://github.com/iree-org/iree/actions/runs/37005242492/job/110834612118) | 2026-10-02 05:42 PDT | [12m14s](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654368) | [12m14s](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654368) | [12m14s](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654368) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [6m33s](https://github.com/iree-org/iree/actions/runs/36990435268/job/110787654354) | [22m22s](https://github.com/iree-org/iree/actions/runs/37005242492/job/110834611957) | [22m22s](https://github.com/iree-org/iree/actions/runs/37005242492/job/110834611957) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m35s](https://github.com/iree-org/iree/actions/runs/36990074123/job/110783975134) | [1m35s](https://github.com/iree-org/iree/actions/runs/36990074123/job/110783975134) | [1m35s](https://github.com/iree-org/iree/actions/runs/36990074123/job/110783975134) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 2 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/36990435268/job/110785182754) | [1m29s](https://github.com/iree-org/iree/actions/runs/37005242492/job/110831930143) | [1m29s](https://github.com/iree-org/iree/actions/runs/37005242492/job/110831930143) | 2 |
| `.github/workflows/ci.yml` | runtime :: macos-14 | `macos-14` | 2 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831927705) | [9s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831927705) | [9s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831927705) | 2 |
| `.github/workflows/ci_macos_arm64_clang.yml` | macos_arm64_clang | `macos-14` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/36990053067/job/110783908309) | [9s](https://github.com/iree-org/iree/actions/runs/36990053067/job/110783908309) | [9s](https://github.com/iree-org/iree/actions/runs/36990053067/job/110783908309) | 1 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831928151) | [8s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831928151) | [8s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831928151) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831928139) | [8s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831928139) | [8s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831928139) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831928360) | [8s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831928360) | [8s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831928360) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: tracy | `macos-14` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831927904) | [8s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831927904) | [8s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831927904) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-14 :: console | `macos-14` | 2 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831927862) | [7s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831927862) | [7s](https://github.com/iree-org/iree/actions/runs/37005242784/job/110831927862) | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 247 | 2% (4/246) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 228 | 1% (2/228) |  | 1d16h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 19h50m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 19h50m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 19h50m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 19h50m (> 2h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
