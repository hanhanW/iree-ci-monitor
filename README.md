# iree-ci-monitor

_Updated: 2026-07-26 11:38 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30206371003/job/89805056200) | [4s](https://github.com/iree-org/iree/actions/runs/30204298806/job/89799571987) | 0% (0/3) | 15 |
| `ubuntu-24.04` | github-hosted | 6 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30200932816/job/89790742626) | [2s](https://github.com/iree-org/iree/actions/runs/30207899234/job/89809054928) | 0% (0/2) | 6 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30206371003/job/89805056262) | [4s](https://github.com/iree-org/iree/actions/runs/30204298806/job/89799571987) | [4s](https://github.com/iree-org/iree/actions/runs/30204298806/job/89799571987) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30204298806/job/89799571962) | [4s](https://github.com/iree-org/iree/actions/runs/30206371003/job/89805056206) | [4s](https://github.com/iree-org/iree/actions/runs/30206371003/job/89805056206) | 3 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791231661) | [3s](https://github.com/iree-org/iree/actions/runs/30206370713/job/89805055256) | [3s](https://github.com/iree-org/iree/actions/runs/30206370713/job/89805055256) | 2 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791246729) | [3s](https://github.com/iree-org/iree/actions/runs/30206370713/job/89805077372) | [3s](https://github.com/iree-org/iree/actions/runs/30206370713/job/89805077372) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30206370713/job/89805077371) | [3s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791246703) | [3s](https://github.com/iree-org/iree/actions/runs/30201165630/job/89791246703) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30204298806/job/89799571951) | [2s](https://github.com/iree-org/iree/actions/runs/30206371003/job/89805056200) | [2s](https://github.com/iree-org/iree/actions/runs/30206371003/job/89805056200) | 3 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30200981179/job/89790751679) | [2s](https://github.com/iree-org/iree/actions/runs/30206170740/job/89804510918) | [2s](https://github.com/iree-org/iree/actions/runs/30206170740/job/89804510918) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89790618255) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89790618255) | [2s](https://github.com/iree-org/iree/actions/runs/30190405648/job/89790618255) | 1 |
| `.github/workflows/issue_greeter.yml` | issue-greeter | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30207899234/job/89809054928) | [2s](https://github.com/iree-org/iree/actions/runs/30207899234/job/89809054928) | [2s](https://github.com/iree-org/iree/actions/runs/30207899234/job/89809054928) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30200932816/job/89790742626) | [2s](https://github.com/iree-org/iree/actions/runs/30200932816/job/89790742626) | [2s](https://github.com/iree-org/iree/actions/runs/30200932816/job/89790742626) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30200932816/job/89790627825) | [2s](https://github.com/iree-org/iree/actions/runs/30200932816/job/89790627825) | [2s](https://github.com/iree-org/iree/actions/runs/30200932816/job/89790627825) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 269 | 1% (3/269) |  | 2d02h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 368 | 1% (5/368) |  | 2d02h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 300 | 5% (14/300) |  | 2d02h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 281 | 1% (2/281) |  | 2d02h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 84 | 1% (1/84) |  | 2d02h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
