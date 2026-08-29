# iree-ci-monitor

_Updated: 2026-08-29 09:45 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 24 | 9 | [4h29m](https://github.com/iree-org/iree/actions/runs/32985518412/job/98231028102) | 2026-08-26 13:05 PDT | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33256827657/job/99111922773) | [3s](https://github.com/iree-org/iree/actions/runs/33256828849/job/99111926770) | — | 15 |
| `ubuntu-24.04` | github-hosted | 12 | 7 | [4h28m](https://github.com/iree-org/iree/actions/runs/32985622770/job/98231128361) | 2026-08-26 13:05 PDT | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33249242019/job/99091929241) | [3s](https://github.com/iree-org/iree/actions/runs/33256563579/job/99111222721) | 0% (0/1) | 5 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 6 | 3 | [4h29m](https://github.com/iree-org/iree/actions/runs/32985518412/job/98231028148) | 2026-08-26 13:05 PDT | [3s](https://github.com/iree-org/iree/actions/runs/33249265874/job/99091988912) | [3s](https://github.com/iree-org/iree/actions/runs/33256828849/job/99111926770) | [3s](https://github.com/iree-org/iree/actions/runs/33256828849/job/99111926770) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 6 | 3 | [4h29m](https://github.com/iree-org/iree/actions/runs/32985518412/job/98231028102) | 2026-08-26 13:05 PDT | [2s](https://github.com/iree-org/iree/actions/runs/33256828849/job/99111926637) | [3s](https://github.com/iree-org/iree/actions/runs/33249265874/job/99091988962) | [3s](https://github.com/iree-org/iree/actions/runs/33249265874/job/99091988962) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 6 | 3 | [4h29m](https://github.com/iree-org/iree/actions/runs/32985518412/job/98231028155) | 2026-08-26 13:05 PDT | [2s](https://github.com/iree-org/iree/actions/runs/33249461888/job/99092501601) | [2s](https://github.com/iree-org/iree/actions/runs/33256828849/job/99111926816) | [2s](https://github.com/iree-org/iree/actions/runs/33256828849/job/99111926816) | 3 |
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 1 | [4h28m](https://github.com/iree-org/iree/actions/runs/32985622770/job/98231128361) | 2026-08-26 13:05 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | 2 | 2 | [4h27m](https://github.com/iree-org/iree/actions/runs/32985674221/job/98231234420) | 2026-08-26 13:05 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 2 | 2 | [4h27m](https://github.com/iree-org/iree/actions/runs/32985674146/job/98231288233) | 2026-08-26 13:05 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/clang_tidy.yml` | clang-tidy | `ubuntu-24.04` | 1 | 1 | [4h26m](https://github.com/iree-org/iree/actions/runs/32985715581/job/98231323412) | 2026-08-26 13:05 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | 1 | 1 | [4h26m](https://github.com/iree-org/iree/actions/runs/32985698522/job/98231380998) | 2026-08-26 13:05 PDT | 0s | 0s | 0s | 0 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33256827657/job/99111945353) | [4s](https://github.com/iree-org/iree/actions/runs/33249461730/job/99092520727) | [4s](https://github.com/iree-org/iree/actions/runs/33249461730/job/99092520727) | 2 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33249242019/job/99091929241) | [3s](https://github.com/iree-org/iree/actions/runs/33256563579/job/99111222721) | [3s](https://github.com/iree-org/iree/actions/runs/33256563579/job/99111222721) | 2 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33249186564/job/99091918231) | [3s](https://github.com/iree-org/iree/actions/runs/33249186564/job/99091918231) | [3s](https://github.com/iree-org/iree/actions/runs/33249186564/job/99091918231) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33249461730/job/99092501323) | [2s](https://github.com/iree-org/iree/actions/runs/33256827657/job/99111922773) | [2s](https://github.com/iree-org/iree/actions/runs/33256827657/job/99111922773) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/33256827657/job/99111945375) | [2s](https://github.com/iree-org/iree/actions/runs/33249461730/job/99092520638) | [2s](https://github.com/iree-org/iree/actions/runs/33249461730/job/99092520638) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99091769508) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99091769508) | [2s](https://github.com/iree-org/iree/actions/runs/33235656716/job/99091769508) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33249186564/job/99091784169) | [2s](https://github.com/iree-org/iree/actions/runs/33249186564/job/99091784169) | [2s](https://github.com/iree-org/iree/actions/runs/33249186564/job/99091784169) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 307 | 1% (2/307) |  | 22h13m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 265 | 3% (8/265) |  | 23h55m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 219 | 0% (1/219) |  | 23h56m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 215 | 0% (0/215) |  | 1d00h ago |

## Alerts

- **[stale-queued]** `ubuntu-24.04` oldest queued job observed waiting 4h28m (> 2h00m)
- **[stale-queued]** `ubuntu-latest` oldest queued job observed waiting 4h29m (> 2h00m)

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
