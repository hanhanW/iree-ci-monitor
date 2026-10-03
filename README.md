# iree-ci-monitor

_Updated: 2026-10-03 09:26 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37131310269/job/111226822511) | [37s](https://github.com/iree-org/iree/actions/runs/37118820192/job/111190745789) | — | 9 |
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37114473273/job/111178474146) | [3s](https://github.com/iree-org/iree/actions/runs/37099241046/job/111190462734) | 33% (1/3) | 11 |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 3 | 3 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257364) | 2026-10-03 09:26 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 3 | 3 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257394) | 2026-10-03 09:26 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 6 | 6 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257428) | 2026-10-03 09:26 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,gfx1100` | self-hosted | 6 | 6 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257509) | 2026-10-03 09:26 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257364) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `main` | push |
| [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257394) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `main` | push |
| [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257428) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257509) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257562) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257835) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [15h58m](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943478) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `users/kuhar/vulkan-rocjitsu-ci` | pull_request |
| [15h58m](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943507) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/kuhar/vulkan-rocjitsu-ci` | pull_request |
| [15h58m](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943522) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/kuhar/vulkan-rocjitsu-ci` | pull_request |
| [15h58m](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943553) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `users/kuhar/vulkan-rocjitsu-ci` | pull_request |
| [15h58m](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943557) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `users/kuhar/vulkan-rocjitsu-ci` | pull_request |
| [15h58m](https://github.com/iree-org/iree/actions/runs/37081552964/job/111084943578) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `users/kuhar/vulkan-rocjitsu-ci` | pull_request |
| [10h13m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173088) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | `feat-python-async-parameter-files` | pull_request |
| [10h13m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173141) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `feat-python-async-parameter-files` | pull_request |
| [10h13m](https://github.com/iree-org/iree/actions/runs/37101946689/job/111144173202) | 2026-10-03 09:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `feat-python-async-parameter-files` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 3 | 3 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257394) | 2026-10-03 09:26 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 3 | 3 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257364) | 2026-10-03 09:26 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 3 | 3 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257835) | 2026-10-03 09:26 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 3 | 3 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257428) | 2026-10-03 09:26 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 3 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257509) | 2026-10-03 09:26 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 3 | 3 | [18h42m](https://github.com/iree-org/iree/actions/runs/37067818568/job/111042257562) | 2026-10-03 09:26 PDT | 0s | 0s | 0s | 0 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37131310269/job/111226822511) | [37s](https://github.com/iree-org/iree/actions/runs/37118820192/job/111190745789) | [37s](https://github.com/iree-org/iree/actions/runs/37118820192/job/111190745789) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37099241046/job/111190462734) | [3s](https://github.com/iree-org/iree/actions/runs/37099241046/job/111190462734) | [3s](https://github.com/iree-org/iree/actions/runs/37099241046/job/111190462734) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37131309474/job/111226847576) | [3s](https://github.com/iree-org/iree/actions/runs/37131309474/job/111226847576) | [3s](https://github.com/iree-org/iree/actions/runs/37131309474/job/111226847576) | 1 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37031842464/job/111241668141) | [2s](https://github.com/iree-org/iree/actions/runs/37031857001/job/111242297080) | [2s](https://github.com/iree-org/iree/actions/runs/37031857001/job/111242297080) | 3 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/37118783602/job/111190645881) | [2s](https://github.com/iree-org/iree/actions/runs/37130994553/job/111225902561) | [2s](https://github.com/iree-org/iree/actions/runs/37130994553/job/111225902561) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37118820192/job/111190745605) | [2s](https://github.com/iree-org/iree/actions/runs/37131310269/job/111226822556) | [2s](https://github.com/iree-org/iree/actions/runs/37131310269/job/111226822556) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/37118820192/job/111190745778) | [2s](https://github.com/iree-org/iree/actions/runs/37131310269/job/111226822544) | [2s](https://github.com/iree-org/iree/actions/runs/37131310269/job/111226822544) | 2 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111148940685) | [2s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111148940685) | [2s](https://github.com/iree-org/iree/actions/runs/37101946668/job/111148940685) | 1 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37114473273/job/111178474146) | [2s](https://github.com/iree-org/iree/actions/runs/37114473273/job/111178474146) | [2s](https://github.com/iree-org/iree/actions/runs/37114473273/job/111178474146) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37135538489/job/111239206710) | [2s](https://github.com/iree-org/iree/actions/runs/37135538489/job/111239206710) | [2s](https://github.com/iree-org/iree/actions/runs/37135538489/job/111239206710) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37118726945/job/111190628501) | [2s](https://github.com/iree-org/iree/actions/runs/37118726945/job/111190628501) | [2s](https://github.com/iree-org/iree/actions/runs/37118726945/job/111190628501) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37118726945/job/111190485527) | [2s](https://github.com/iree-org/iree/actions/runs/37118726945/job/111190485527) | [2s](https://github.com/iree-org/iree/actions/runs/37118726945/job/111190485527) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37131309474/job/111226820308) | [2s](https://github.com/iree-org/iree/actions/runs/37131309474/job/111226820308) | [2s](https://github.com/iree-org/iree/actions/runs/37131309474/job/111226820308) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37131309474/job/111226847685) | [2s](https://github.com/iree-org/iree/actions/runs/37131309474/job/111226847685) | [2s](https://github.com/iree-org/iree/actions/runs/37131309474/job/111226847685) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 280 | 1% (4/280) |  | 9h29m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 206 | 1% (2/206) |  | 2d19h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 18h42m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 18h42m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 18h42m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 18h42m (> 2h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
