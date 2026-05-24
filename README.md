# iree-ci-monitor

_Updated: 2026-05-24 11:41 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26360419115/job/77594729214) | [2s](https://github.com/iree-org/iree/actions/runs/26364018813/job/77604536498) | 0% (0/3) | 18 |
| `ubuntu-24.04` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77594350012) | [2s](https://github.com/iree-org/iree/actions/runs/26360303396/job/77594422551) | 0% (0/1) | 5 |
| `azure-linux-scale` | ossci | 1 | 1 | [10m39s](https://github.com/iree-org/iree/actions/runs/26212319110/job/77181582238) | 2026-05-21 06:27 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 1 | 1 | [10m39s](https://github.com/iree-org/iree/actions/runs/26212319110/job/77181582238) | 2026-05-21 06:27 PDT | 0s | 0s | 0s | 0 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26364018553/job/77604545029) | [3s](https://github.com/iree-org/iree/actions/runs/26360419115/job/77594740244) | [3s](https://github.com/iree-org/iree/actions/runs/26360419115/job/77594740244) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26362659917/job/77600806136) | [2s](https://github.com/iree-org/iree/actions/runs/26364018813/job/77604536497) | [2s](https://github.com/iree-org/iree/actions/runs/26364018813/job/77604536497) | 4 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26362659917/job/77600806139) | [2s](https://github.com/iree-org/iree/actions/runs/26364018813/job/77604536496) | [2s](https://github.com/iree-org/iree/actions/runs/26364018813/job/77604536496) | 4 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 4 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26362659917/job/77600806148) | [2s](https://github.com/iree-org/iree/actions/runs/26364018813/job/77604536498) | [2s](https://github.com/iree-org/iree/actions/runs/26364018813/job/77604536498) | 4 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26363904040/job/77604217278) | [2s](https://github.com/iree-org/iree/actions/runs/26360303396/job/77594422551) | [2s](https://github.com/iree-org/iree/actions/runs/26360303396/job/77594422551) | 2 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26364018553/job/77604536253) | [2s](https://github.com/iree-org/iree/actions/runs/26360419115/job/77594729214) | [2s](https://github.com/iree-org/iree/actions/runs/26360419115/job/77594729214) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26364018553/job/77604545008) | [2s](https://github.com/iree-org/iree/actions/runs/26360419115/job/77594740257) | [2s](https://github.com/iree-org/iree/actions/runs/26360419115/job/77594740257) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77594350012) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77594350012) | [2s](https://github.com/iree-org/iree/actions/runs/26353858251/job/77594350012) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/26360277848/job/77594414898) | [2s](https://github.com/iree-org/iree/actions/runs/26360277848/job/77594414898) | [2s](https://github.com/iree-org/iree/actions/runs/26360277848/job/77594414898) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/26360277848/job/77594355377) | [1s](https://github.com/iree-org/iree/actions/runs/26360277848/job/77594355377) | [1s](https://github.com/iree-org/iree/actions/runs/26360277848/job/77594355377) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 300 | 2% (5/299) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 270 | 7% (20/269) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 229 | 3% (7/228) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 224 | 1% (2/223) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 71 | 3% (2/71) |  | 1d23h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
