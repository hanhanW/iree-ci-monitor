# iree-ci-monitor

_Updated: 2026-07-10 17:52 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29101868470/job/86392561624) | [3s](https://github.com/iree-org/iree/actions/runs/29101868470/job/86392527073) | — | 6 |
| `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29083604717/job/86400988587) | [2s](https://github.com/iree-org/iree/actions/runs/29083604717/job/86400988587) | — | 1 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 8 | 8 | [15h07m](https://github.com/iree-org/iree/actions/runs/29083604698/job/86333510684) | 2026-07-10 17:52 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [15h07m](https://github.com/iree-org/iree/actions/runs/29083604698/job/86333510684) | 2026-07-10 17:52 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `dependabot/github_actions/github-actions-bda1fe1b4d` | pull_request |
| [15h07m](https://github.com/iree-org/iree/actions/runs/29083604698/job/86333510732) | 2026-07-10 17:52 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | `dependabot/github_actions/github-actions-bda1fe1b4d` | pull_request |
| [15h07m](https://github.com/iree-org/iree/actions/runs/29083604698/job/86333510802) | 2026-07-10 17:52 PDT | `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | `dependabot/github_actions/github-actions-bda1fe1b4d` | pull_request |
| [15h07m](https://github.com/iree-org/iree/actions/runs/29083604698/job/86333510822) | 2026-07-10 17:52 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | `dependabot/github_actions/github-actions-bda1fe1b4d` | pull_request |
| [13h19m](https://github.com/iree-org/iree/actions/runs/29089345918/job/86352075842) | 2026-07-10 17:52 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [13h19m](https://github.com/iree-org/iree/actions/runs/29089345918/job/86352075870) | 2026-07-10 17:52 PDT | `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [13h19m](https://github.com/iree-org/iree/actions/runs/29089345918/job/86352075886) | 2026-07-10 17:52 PDT | `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |
| [13h19m](https://github.com/iree-org/iree/actions/runs/29089345918/job/86352075970) | 2026-07-10 17:52 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 2 | [15h07m](https://github.com/iree-org/iree/actions/runs/29083604698/job/86333510684) | 2026-07-10 17:52 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi300_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 2 | [15h07m](https://github.com/iree-org/iree/actions/runs/29083604698/job/86333510732) | 2026-07-10 17:52 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_rocm_mi300_gfx942_O3 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 2 | [15h07m](https://github.com/iree-org/iree/actions/runs/29083604698/job/86333510822) | 2026-07-10 17:52 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: amdgpu_mi325_gfx942 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 2 | [15h07m](https://github.com/iree-org/iree/actions/runs/29083604698/job/86333510802) | 2026-07-10 17:52 PDT | 0s | 0s | 0s | 0 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29101868470/job/86392527073) | [3s](https://github.com/iree-org/iree/actions/runs/29101868470/job/86392527073) | [3s](https://github.com/iree-org/iree/actions/runs/29101868470/job/86392527073) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29083604717/job/86400988587) | [2s](https://github.com/iree-org/iree/actions/runs/29083604717/job/86400988587) | [2s](https://github.com/iree-org/iree/actions/runs/29083604717/job/86400988587) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29101869665/job/86392531143) | [2s](https://github.com/iree-org/iree/actions/runs/29101869665/job/86392531143) | [2s](https://github.com/iree-org/iree/actions/runs/29101869665/job/86392531143) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29101868470/job/86392561629) | [2s](https://github.com/iree-org/iree/actions/runs/29101868470/job/86392561629) | [2s](https://github.com/iree-org/iree/actions/runs/29101868470/job/86392561629) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29101868470/job/86392561624) | [2s](https://github.com/iree-org/iree/actions/runs/29101868470/job/86392561624) | [2s](https://github.com/iree-org/iree/actions/runs/29101868470/job/86392561624) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29101869665/job/86392531169) | [1s](https://github.com/iree-org/iree/actions/runs/29101869665/job/86392531169) | [1s](https://github.com/iree-org/iree/actions/runs/29101869665/job/86392531169) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/29101869665/job/86392531172) | [1s](https://github.com/iree-org/iree/actions/runs/29101869665/job/86392531172) | [1s](https://github.com/iree-org/iree/actions/runs/29101869665/job/86392531172) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 159 | 7% (11/158) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 202 | 1% (3/201) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 162 | 1% (1/161) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 150 | 1% (1/149) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 47 | 11% (5/47) |  | 13h09m ago |

## Alerts

- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job observed waiting 15h07m (> 2h00m)

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
