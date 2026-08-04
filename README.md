# iree-ci-monitor

_Updated: 2026-08-03 17:55 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | [20s](https://github.com/iree-org/iree/actions/runs/30825248877/job/91725182586) | [20s](https://github.com/iree-org/iree/actions/runs/30825248877/job/91725182586) | 0% (0/1) | 1 |
| `ubuntu-latest` | github-hosted | 7 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/30826032709/job/91727777172) | [8s](https://github.com/iree-org/iree/actions/runs/30855766296/job/91826294535) | 0% (0/1) | 7 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 2 | 2 | [15h36m](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715262) | 2026-08-03 17:55 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [15h36m](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715262) | 2026-08-03 17:55 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `conv-dt-lower-to-ukernel` | pull_request |
| [11h52m](https://github.com/iree-org/iree/actions/runs/30815414228/job/91694209322) | 2026-08-03 17:55 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `integrates/llvm-20260731-cleanup` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 2 | 2 | [15h36m](https://github.com/iree-org/iree/actions/runs/30798185758/job/91644715262) | 2026-08-03 17:55 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [20s](https://github.com/iree-org/iree/actions/runs/30825248877/job/91725182586) | [20s](https://github.com/iree-org/iree/actions/runs/30825248877/job/91725182586) | [20s](https://github.com/iree-org/iree/actions/runs/30825248877/job/91725182586) | 1 |
| `dynamic/dependabot/dependabot-updates` | Dependabot | `ubuntu-latest` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30855766296/job/91826294535) | [8s](https://github.com/iree-org/iree/actions/runs/30855766296/job/91826294535) | [8s](https://github.com/iree-org/iree/actions/runs/30855766296/job/91826294535) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30826033761/job/91727777226) | [8s](https://github.com/iree-org/iree/actions/runs/30826033761/job/91727777226) | [8s](https://github.com/iree-org/iree/actions/runs/30826033761/job/91727777226) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30826032709/job/91727777172) | [8s](https://github.com/iree-org/iree/actions/runs/30826032709/job/91727777172) | [8s](https://github.com/iree-org/iree/actions/runs/30826032709/job/91727777172) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30826032709/job/91727853468) | [8s](https://github.com/iree-org/iree/actions/runs/30826032709/job/91727853468) | [8s](https://github.com/iree-org/iree/actions/runs/30826032709/job/91727853468) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30826033761/job/91727777314) | [2s](https://github.com/iree-org/iree/actions/runs/30826033761/job/91727777314) | [2s](https://github.com/iree-org/iree/actions/runs/30826033761/job/91727777314) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30826033761/job/91727777310) | [2s](https://github.com/iree-org/iree/actions/runs/30826033761/job/91727777310) | [2s](https://github.com/iree-org/iree/actions/runs/30826033761/job/91727777310) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30826032709/job/91727853517) | [2s](https://github.com/iree-org/iree/actions/runs/30826032709/job/91727853517) | [2s](https://github.com/iree-org/iree/actions/runs/30826032709/job/91727853517) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 157 | 0% (0/157) |  | 11h19m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 111 | 0% (0/111) |  | 11h20m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 118 | 1% (1/118) |  | 11h22m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 139 | 2% (3/139) |  | 11h28m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 35 | 0% (0/35) |  | 11h41m ago |

## Alerts

- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job observed waiting 15h36m (> 2h00m)

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
