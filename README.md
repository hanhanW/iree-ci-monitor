# iree-ci-monitor

_Updated: 2026-08-02 11:37 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30752431478/job/91508730689) | [8s](https://github.com/iree-org/iree/actions/runs/30752431234/job/91508752188) | 0% (0/3) | 15 |
| `ubuntu-24.04` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30746806255/job/91493679199) | [4s](https://github.com/iree-org/iree/actions/runs/30752191119/job/91508070654) | 0% (0/1) | 5 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30752431234/job/91508730159) | [9s](https://github.com/iree-org/iree/actions/runs/30746997029/job/91494171944) | [9s](https://github.com/iree-org/iree/actions/runs/30746997029/job/91494171944) | 2 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30746997029/job/91494196196) | [8s](https://github.com/iree-org/iree/actions/runs/30752431234/job/91508752188) | [8s](https://github.com/iree-org/iree/actions/runs/30752431234/job/91508752188) | 2 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30746806255/job/91493679199) | [4s](https://github.com/iree-org/iree/actions/runs/30752191119/job/91508070654) | [4s](https://github.com/iree-org/iree/actions/runs/30752191119/job/91508070654) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30752431478/job/91508730689) | [3s](https://github.com/iree-org/iree/actions/runs/30750202415/job/91502773366) | [3s](https://github.com/iree-org/iree/actions/runs/30750202415/job/91502773366) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30750202415/job/91502773383) | [3s](https://github.com/iree-org/iree/actions/runs/30752431478/job/91508730660) | [3s](https://github.com/iree-org/iree/actions/runs/30752431478/job/91508730660) | 3 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30746750485/job/91493537209) | [3s](https://github.com/iree-org/iree/actions/runs/30746750485/job/91493537209) | [3s](https://github.com/iree-org/iree/actions/runs/30746750485/job/91493537209) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30750202415/job/91502773400) | [2s](https://github.com/iree-org/iree/actions/runs/30752431478/job/91508730688) | [2s](https://github.com/iree-org/iree/actions/runs/30752431478/job/91508730688) | 3 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30746997029/job/91494196189) | [2s](https://github.com/iree-org/iree/actions/runs/30752431234/job/91508752190) | [2s](https://github.com/iree-org/iree/actions/runs/30752431234/job/91508752190) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91493529028) | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91493529028) | [2s](https://github.com/iree-org/iree/actions/runs/30735197126/job/91493529028) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30746750485/job/91493668602) | [2s](https://github.com/iree-org/iree/actions/runs/30746750485/job/91493668602) | [2s](https://github.com/iree-org/iree/actions/runs/30746750485/job/91493668602) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 166 | 0% (0/166) |  | 1d22h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 118 | 1% (1/118) |  | 1d22h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 148 | 3% (4/148) |  | 1d22h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 123 | 1% (1/123) |  | 1d22h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 37 | 3% (1/37) |  | 1d22h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
