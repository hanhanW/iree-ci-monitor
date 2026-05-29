# iree-ci-monitor

_Updated: 2026-05-28 18:22 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 57 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26611837895/job/78419230975) | [3s](https://github.com/iree-org/iree/actions/runs/26611837711/job/78419230555) | 0% (0/22) | 47 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26611835316/job/78419225966) | [3s](https://github.com/iree-org/iree/actions/runs/26611835316/job/78419225977) | — | 15 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26572863141/job/78338994615) | [2s](https://github.com/iree-org/iree/actions/runs/26572863141/job/78338994615) | 0% (0/8) | 8 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78339031087) | [2s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78339031087) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark75-ci` |
| `azure-linux-scale` | ossci | 2 | 0 | — | — | 0 | 0s | 0s | 0% (0/2) | 2 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 3 | 1 | [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293013979) | 2026-05-28 06:38 PDT | 0 | 0s | 0s | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 6 | 2 | [1h17m](https://github.com/iree-org/iree/actions/runs/26572863141/job/78289296086) | 2026-05-28 06:38 PDT | 0 | 0s | 0s | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | 0% (0/2) | `iree-mi308-1` |
| `Linux,X64,gfx1100` | self-hosted | 5 | 1 | [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014224) | 2026-05-28 06:38 PDT | 0 | 0s | 0s | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 2 | 0 | — | — | 0 | 0s | 0s | 0% (0/2) | 2 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | 0s | 0s | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 6 | 2 | [1h17m](https://github.com/iree-org/iree/actions/runs/26572863141/job/78289296040) | 2026-05-28 06:38 PDT | 0 | 0s | 0s | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 3 | 1 | [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014243) | 2026-05-28 06:38 PDT | 0 | 0s | 0s | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 3 | 1 | [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014052) | 2026-05-28 06:38 PDT | 0 | 0s | 0s | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 2 | [1h17m](https://github.com/iree-org/iree/actions/runs/26572863141/job/78289296402) | 2026-05-28 06:38 PDT | 0 | 0s | 0s | 0% (0/2) | `shark10-ci` |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [1h17m](https://github.com/iree-org/iree/actions/runs/26572863141/job/78289296040) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [1h17m](https://github.com/iree-org/iree/actions/runs/26572863141/job/78289296086) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [1h17m](https://github.com/iree-org/iree/actions/runs/26572863141/job/78289296402) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293013979) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `main` | push |
| [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014052) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `main` | push |
| [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014176) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | `main` | push |
| [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014210) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014224) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014243) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | `main` | push |
| [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014246) | 2026-05-28 06:38 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 4 | 2 | [1h17m](https://github.com/iree-org/iree/actions/runs/26572863141/job/78289296402) | 2026-05-28 06:38 PDT | 0s | 0s | 0s | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 4 | 2 | [1h17m](https://github.com/iree-org/iree/actions/runs/26572863141/job/78289296040) | 2026-05-28 06:38 PDT | 0s | 0s | 0s | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 4 | 2 | [1h17m](https://github.com/iree-org/iree/actions/runs/26572863141/job/78289296086) | 2026-05-28 06:38 PDT | 0s | 0s | 0s | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 3 | 1 | [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293013979) | 2026-05-28 06:38 PDT | 0s | 0s | 0s | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 3 | 1 | [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014243) | 2026-05-28 06:38 PDT | 0s | 0s | 0s | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 3 | 1 | [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014052) | 2026-05-28 06:38 PDT | 0s | 0s | 0s | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 3 | 1 | [55m25s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78293014224) | 2026-05-28 06:38 PDT | 0s | 0s | 0s | 2 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 7 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26611454943/job/78418069687) | [3s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78340230769) | [3s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78340230769) | 7 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | 7 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26611890967/job/78419392984) | [3s](https://github.com/iree-org/iree/actions/runs/26611837711/job/78419230555) | [3s](https://github.com/iree-org/iree/actions/runs/26611837711/job/78419230555) | 7 |
| `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26611890891/job/78419392425) | [3s](https://github.com/iree-org/iree/actions/runs/26612030446/job/78419811520) | [3s](https://github.com/iree-org/iree/actions/runs/26612030446/job/78419811520) | 5 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26612028667/job/78419809323) | [3s](https://github.com/iree-org/iree/actions/runs/26611889286/job/78419389761) | [3s](https://github.com/iree-org/iree/actions/runs/26611889286/job/78419389761) | 5 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26611453273/job/78418050366) | [3s](https://github.com/iree-org/iree/actions/runs/26611835316/job/78419225915) | [3s](https://github.com/iree-org/iree/actions/runs/26611835316/job/78419225915) | 5 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26611837895/job/78419248209) | [2s](https://github.com/iree-org/iree/actions/runs/26612030594/job/78419835848) | [2s](https://github.com/iree-org/iree/actions/runs/26612030594/job/78419835848) | 5 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26611837895/job/78419230975) | [2s](https://github.com/iree-org/iree/actions/runs/26612030594/job/78419811972) | [2s](https://github.com/iree-org/iree/actions/runs/26612030594/job/78419811972) | 5 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 5 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26611835316/job/78419225966) | [2s](https://github.com/iree-org/iree/actions/runs/26612028667/job/78419809319) | [2s](https://github.com/iree-org/iree/actions/runs/26612028667/job/78419809319) | 5 |
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26572863141/job/78338994615) | [2s](https://github.com/iree-org/iree/actions/runs/26572863141/job/78338994615) | [2s](https://github.com/iree-org/iree/actions/runs/26572863141/job/78338994615) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78339031087) | [2s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78339031087) | [2s](https://github.com/iree-org/iree/actions/runs/26573925134/job/78339031087) | 2 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 5 | 0 | — | — | 0s | 0s | 0s | 0 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 5 | 0 | — | — | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 2 | 0 | — | — | 0s | 0s | 0s | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 218 | 4% (9/217) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 185 | 2% (4/185) |  | 8h43m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 245 | 1% (3/245) |  | 10h35m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 170 | 0% (0/170) |  | 11h40m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 58 | 2% (1/58) |  | 12h29m ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
