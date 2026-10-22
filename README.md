# iree-ci-monitor

_Updated: 2026-10-21 21:56 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 8 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39721566799/job/119635969405) | [3s](https://github.com/iree-org/iree/actions/runs/39652221066/job/119426141956) | 0% (0/4) | 8 |
| `Linux,X64,gfx1100` | self-hosted | 2 | 2 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | 0 | 0s | 0s | — | 0 |
| `Linux,X64,rdna3` | self-hosted | 1 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `fix-spirv-wide-elementwise` | pull_request |
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `fix-spirv-wide-elementwise` | pull_request |
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827580) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `fix-spirv-wide-elementwise` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 1 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827580) | 2026-10-19 06:26 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 1 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 1 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/39652221066/job/119426141956) | [3s](https://github.com/iree-org/iree/actions/runs/39652221066/job/119426141956) | [3s](https://github.com/iree-org/iree/actions/runs/39652221066/job/119426141956) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39622742847/job/119429931071) | [2s](https://github.com/iree-org/iree/actions/runs/39652221089/job/119436477687) | [2s](https://github.com/iree-org/iree/actions/runs/39652221089/job/119436477687) | 2 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39721566799/job/119635969405) | [2s](https://github.com/iree-org/iree/actions/runs/39721566799/job/119635969405) | [2s](https://github.com/iree-org/iree/actions/runs/39721566799/job/119635969405) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39722035529/job/119637471455) | [2s](https://github.com/iree-org/iree/actions/runs/39722035529/job/119637471455) | [2s](https://github.com/iree-org/iree/actions/runs/39722035529/job/119637471455) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39722035529/job/119637471247) | [2s](https://github.com/iree-org/iree/actions/runs/39722035529/job/119637471247) | [2s](https://github.com/iree-org/iree/actions/runs/39722035529/job/119637471247) | 1 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/39720313982/job/119632018910) | [1s](https://github.com/iree-org/iree/actions/runs/39720313982/job/119632018910) | [1s](https://github.com/iree-org/iree/actions/runs/39720313982/job/119632018910) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/39722035529/job/119639625904) | [1s](https://github.com/iree-org/iree/actions/runs/39722035529/job/119639625904) | [1s](https://github.com/iree-org/iree/actions/runs/39722035529/job/119639625904) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 303 | 2% (7/303) |  | 9h48m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 355 | 0% (0/355) |  | 9h52m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
