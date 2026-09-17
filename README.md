# iree-ci-monitor

_Updated: 2026-09-16 21:58 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 8 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35133353625/job/104935797727) | [3s](https://github.com/iree-org/iree/actions/runs/35133351024/job/104939402161) | 0% (0/3) | 8 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 11 | 11 | [22h32m](https://github.com/iree-org/iree/actions/runs/35062939888/job/104689025165) | 2026-09-16 21:57 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [22h32m](https://github.com/iree-org/iree/actions/runs/35062939888/job/104689025165) | 2026-09-16 21:57 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [16h51m](https://github.com/iree-org/iree/actions/runs/35093131570/job/104786295964) | 2026-09-16 21:57 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [15h35m](https://github.com/iree-org/iree/actions/runs/35098403907/job/104811488885) | 2026-09-16 21:57 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `integrates/llvm-20260916` | pull_request |
| [14h36m](https://github.com/iree-org/iree/actions/runs/35106797229/job/104833982219) | 2026-09-16 21:57 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [12h46m](https://github.com/iree-org/iree/actions/runs/35119277314/job/104875991730) | 2026-09-16 21:57 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/ziereis/qdq-integer-contractions` | pull_request |
| [10h30m](https://github.com/iree-org/iree/actions/runs/35133353598/job/104923411056) | 2026-09-16 21:57 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-3` | pull_request |
| [10h29m](https://github.com/iree-org/iree/actions/runs/35133349567/job/104923478700) | 2026-09-16 21:57 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-4` | pull_request |
| [10h28m](https://github.com/iree-org/iree/actions/runs/35133351078/job/104923919050) | 2026-09-16 21:57 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-2` | pull_request |
| [10h27m](https://github.com/iree-org/iree/actions/runs/35133351483/job/104924409806) | 2026-09-16 21:57 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-6` | pull_request |
| [10h26m](https://github.com/iree-org/iree/actions/runs/35133353135/job/104924487535) | 2026-09-16 21:57 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-7` | pull_request |
| [10h26m](https://github.com/iree-org/iree/actions/runs/35133351343/job/104924553868) | 2026-09-16 21:57 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `users/jschuhmacher/dynamic-plugin-support-5` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 11 | 11 | [22h32m](https://github.com/iree-org/iree/actions/runs/35062939888/job/104689025165) | 2026-09-16 21:57 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35133353625/job/104935797727) | [3s](https://github.com/iree-org/iree/actions/runs/35133351024/job/104939402161) | [3s](https://github.com/iree-org/iree/actions/runs/35133351024/job/104939402161) | 4 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35044430244/job/105043577827) | [2s](https://github.com/iree-org/iree/actions/runs/35044430244/job/105043577827) | [2s](https://github.com/iree-org/iree/actions/runs/35044430244/job/105043577827) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35181777529/job/105075283567) | [2s](https://github.com/iree-org/iree/actions/runs/35181777529/job/105075283567) | [2s](https://github.com/iree-org/iree/actions/runs/35181777529/job/105075283567) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35181777529/job/105077106423) | [2s](https://github.com/iree-org/iree/actions/runs/35181777529/job/105077106423) | [2s](https://github.com/iree-org/iree/actions/runs/35181777529/job/105077106423) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/35181777529/job/105075283674) | [1s](https://github.com/iree-org/iree/actions/runs/35181777529/job/105075283674) | [1s](https://github.com/iree-org/iree/actions/runs/35181777529/job/105075283674) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 391 | 2% (6/391) |  | 8h38m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 312 | 2% (6/312) |  | 8h59m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 309 | 1% (3/309) |  | 9h10m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 208 | 9% (18/208) |  | 2d13h ago |

## Alerts

- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job observed waiting 22h32m (> 2h00m)
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
