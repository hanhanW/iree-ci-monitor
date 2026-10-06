# iree-ci-monitor

_Updated: 2026-10-06 11:27 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 14 | 0 | — | — | 0 | [51m30s](https://github.com/iree-org/iree/actions/runs/37489455050/job/112362466673) | [2h35m](https://github.com/iree-org/iree/actions/runs/37477604292/job/112321051391) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 7 | 0 | — | — | 0 | [37m56s](https://github.com/iree-org/iree/actions/runs/37489455050/job/112362466897) | [1h43m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313677) | 0% (0/3) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 14 | 0 | — | — | 0 | [57m33s](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313744) | [1h37m](https://github.com/iree-org/iree/actions/runs/37477604292/job/112321051193) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 7 | 0 | — | — | 0 | [10m19s](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315312948) | [43m55s](https://github.com/iree-org/iree/actions/runs/37489455050/job/112362466751) | 0% (0/3) | `shark75-ci` |
| `azure-linux-scale` | ossci | 46 | 0 | — | — | 1 | [9s](https://github.com/iree-org/iree/actions/runs/37506869447/job/112417718628) | [2m02s](https://github.com/iree-org/iree/actions/runs/37500140540/job/112394858838) | 0% (0/20) | 46 |
| `windows-2022` | github-hosted | 21 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/37489455158/job/112358171936) | [56s](https://github.com/iree-org/iree/actions/runs/37477604563/job/112317128676) | 0% (0/9) | 21 |
| `ubuntu-24.04` | github-hosted | 142 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/37473437028/job/112307385739) | [21s](https://github.com/iree-org/iree/actions/runs/37477604563/job/112333355479) | 5% (3/59) | 142 |
| `macos-14` | github-hosted | 21 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/37477997235/job/112318512104) | [11s](https://github.com/iree-org/iree/actions/runs/37477604563/job/112317128436) | 0% (0/9) | 21 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/37489455158/job/112358171746) | [8s](https://github.com/iree-org/iree/actions/runs/37477604563/job/112317128593) | 0% (0/9) | 21 |
| `ubuntu-latest` | github-hosted | 24 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/37476524951/job/112313274169) | [3s](https://github.com/iree-org/iree/actions/runs/37507757287/job/112420668390) | 0% (0/9) | 24 |
| `azure-windows-scale` | ossci | 7 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37477604563/job/112317129510) | [2s](https://github.com/iree-org/iree/actions/runs/37506869447/job/112417718689) | 0% (0/3) | 7 |
| `Linux,X64,rdna3` | self-hosted | 16 | 12 | [20h22m](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120988) | 2026-10-06 11:25 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 8 | 6 | [20h22m](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999121376) | 2026-10-06 11:25 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 8 | 6 | [20h22m](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120827) | 2026-10-06 11:25 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 16 | 12 | [20h22m](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120776) | 2026-10-06 11:25 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,iree-w7900` | self-hosted | 7 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [20h22m](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120776) | 2026-10-06 11:25 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `dependabot/github_actions/github-actions-85ecf4c6e7` | pull_request |
| [20h22m](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120827) | 2026-10-06 11:25 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `dependabot/github_actions/github-actions-85ecf4c6e7` | pull_request |
| [20h22m](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120988) | 2026-10-06 11:25 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `dependabot/github_actions/github-actions-85ecf4c6e7` | pull_request |
| [20h22m](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999121210) | 2026-10-06 11:25 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `dependabot/github_actions/github-actions-85ecf4c6e7` | pull_request |
| [20h22m](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999121250) | 2026-10-06 11:25 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `dependabot/github_actions/github-actions-85ecf4c6e7` | pull_request |
| [20h22m](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999121376) | 2026-10-06 11:25 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `dependabot/github_actions/github-actions-85ecf4c6e7` | pull_request |
| [4h12m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313472) | 2026-10-06 11:25 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/maxbartel/layout/propagate-tensor-encodings` | pull_request |
| [4h12m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313612) | 2026-10-06 11:25 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/maxbartel/layout/propagate-tensor-encodings` | pull_request |
| [4h12m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313832) | 2026-10-06 11:25 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `users/maxbartel/layout/propagate-tensor-encodings` | pull_request |
| [4h12m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313855) | 2026-10-06 11:25 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/maxbartel/layout/propagate-tensor-encodings` | pull_request |
| [4h12m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313864) | 2026-10-06 11:25 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/maxbartel/layout/propagate-tensor-encodings` | pull_request |
| [4h12m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313928) | 2026-10-06 11:25 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/maxbartel/layout/propagate-tensor-encodings` | pull_request |
| [4h00m](https://github.com/iree-org/iree/actions/runs/37477604292/job/112321051077) | 2026-10-06 11:25 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |
| [4h00m](https://github.com/iree-org/iree/actions/runs/37477604292/job/112321051248) | 2026-10-06 11:25 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [4h00m](https://github.com/iree-org/iree/actions/runs/37477604292/job/112321051249) | 2026-10-06 11:25 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 8 | 6 | [20h22m](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120827) | 2026-10-06 11:25 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 8 | 6 | [20h22m](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120776) | 2026-10-06 11:25 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 8 | 6 | [20h22m](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999120988) | 2026-10-06 11:25 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 8 | 6 | [20h22m](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999121376) | 2026-10-06 11:25 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 8 | 6 | [20h22m](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999121210) | 2026-10-06 11:25 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 8 | 6 | [20h22m](https://github.com/iree-org/iree/actions/runs/37378873742/job/111999121250) | 2026-10-06 11:25 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 7 | 0 | — | — | [51m30s](https://github.com/iree-org/iree/actions/runs/37489455050/job/112362466673) | [2h36m](https://github.com/iree-org/iree/actions/runs/37477997055/job/112323157683) | [2h36m](https://github.com/iree-org/iree/actions/runs/37477997055/job/112323157683) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 7 | 0 | — | — | [21m03s](https://github.com/iree-org/iree/actions/runs/37500140525/job/112401991824) | [1h56m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313830) | [1h56m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313830) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 7 | 0 | — | — | [57m33s](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313744) | [1h51m](https://github.com/iree-org/iree/actions/runs/37477997055/job/112323157725) | [1h51m](https://github.com/iree-org/iree/actions/runs/37477997055/job/112323157725) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 7 | 0 | — | — | [37m56s](https://github.com/iree-org/iree/actions/runs/37489455050/job/112362466897) | [1h43m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313677) | [1h43m](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313677) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 7 | 0 | — | — | [43m05s](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315313459) | [1h17m](https://github.com/iree-org/iree/actions/runs/37477997055/job/112323157661) | [1h17m](https://github.com/iree-org/iree/actions/runs/37477997055/job/112323157661) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 7 | 0 | — | — | [10m19s](https://github.com/iree-org/iree/actions/runs/37475754186/job/112315312948) | [43m55s](https://github.com/iree-org/iree/actions/runs/37489455050/job/112362466751) | [43m55s](https://github.com/iree-org/iree/actions/runs/37489455050/job/112362466751) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37477604563/job/112317129190) | [2m10s](https://github.com/iree-org/iree/actions/runs/37477997235/job/112318513319) | [2m10s](https://github.com/iree-org/iree/actions/runs/37477997235/job/112318513319) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 7 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37489455158/job/112358172392) | [2m04s](https://github.com/iree-org/iree/actions/runs/37500140540/job/112394858725) | [2m04s](https://github.com/iree-org/iree/actions/runs/37500140540/job/112394858725) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 7 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/37506869447/job/112417718699) | [2m02s](https://github.com/iree-org/iree/actions/runs/37500140540/job/112394858838) | [2m02s](https://github.com/iree-org/iree/actions/runs/37500140540/job/112394858838) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 7 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37489455158/job/112358172715) | [2m02s](https://github.com/iree-org/iree/actions/runs/37500140540/job/112394858769) | [2m02s](https://github.com/iree-org/iree/actions/runs/37500140540/job/112394858769) | 7 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 7 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37477604563/job/112317128638) | [1m41s](https://github.com/iree-org/iree/actions/runs/37477997235/job/112318513440) | [1m41s](https://github.com/iree-org/iree/actions/runs/37477997235/job/112318513440) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang_dynamic_plugins / linux_x64_clang_dynamic_plugins | `azure-linux-scale` | 7 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37477604563/job/112317129038) | [1m41s](https://github.com/iree-org/iree/actions/runs/37500140540/job/112394859935) | [1m41s](https://github.com/iree-org/iree/actions/runs/37500140540/job/112394859935) | 7 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 7 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/37477604292/job/112317142394) | [1m41s](https://github.com/iree-org/iree/actions/runs/37473437028/job/112302691254) | [1m41s](https://github.com/iree-org/iree/actions/runs/37473437028/job/112302691254) | 7 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 7 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/37489455158/job/112358171746) | [1m14s](https://github.com/iree-org/iree/actions/runs/37477997235/job/112318512350) | [1m14s](https://github.com/iree-org/iree/actions/runs/37477997235/job/112318512350) | 7 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 389 | 1% (4/389) |  | 2m04s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 163 | 1% (2/163) |  | 5d21h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 20h22m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 20h22m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 20h22m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 20h22m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h43m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h35m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h37m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
