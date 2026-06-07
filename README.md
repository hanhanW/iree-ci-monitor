# iree-ci-monitor

_Updated: 2026-06-07 11:45 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27091905853/job/79956997652) | [3s](https://github.com/iree-org/iree/actions/runs/27091948133/job/79957004749) | 0% (0/1) | 5 |
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27092075769/job/79957363883) | [2s](https://github.com/iree-org/iree/actions/runs/27095578166/job/79967017640) | 0% (0/3) | 15 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27095460182/job/79966679889) | [3s](https://github.com/iree-org/iree/actions/runs/27091948133/job/79957004749) | [3s](https://github.com/iree-org/iree/actions/runs/27091948133/job/79957004749) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27092075769/job/79957363876) | [3s](https://github.com/iree-org/iree/actions/runs/27095577903/job/79967025582) | [3s](https://github.com/iree-org/iree/actions/runs/27095577903/job/79967025582) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79956889167) | [3s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79956889167) | [3s](https://github.com/iree-org/iree/actions/runs/27085027703/job/79956889167) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27094026694/job/79962741227) | [2s](https://github.com/iree-org/iree/actions/runs/27095578166/job/79967017638) | [2s](https://github.com/iree-org/iree/actions/runs/27095578166/job/79967017638) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27094026694/job/79962741219) | [2s](https://github.com/iree-org/iree/actions/runs/27095578166/job/79967017639) | [2s](https://github.com/iree-org/iree/actions/runs/27095578166/job/79967017639) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27094026694/job/79962741224) | [2s](https://github.com/iree-org/iree/actions/runs/27095578166/job/79967017640) | [2s](https://github.com/iree-org/iree/actions/runs/27095578166/job/79967017640) | 3 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/27095577903/job/79967017367) | [2s](https://github.com/iree-org/iree/actions/runs/27092075769/job/79957355776) | [2s](https://github.com/iree-org/iree/actions/runs/27092075769/job/79957355776) | 2 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27092075769/job/79957363883) | [2s](https://github.com/iree-org/iree/actions/runs/27095577903/job/79967025584) | [2s](https://github.com/iree-org/iree/actions/runs/27095577903/job/79967025584) | 2 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27091905853/job/79956997652) | [2s](https://github.com/iree-org/iree/actions/runs/27091905853/job/79956997652) | [2s](https://github.com/iree-org/iree/actions/runs/27091905853/job/79956997652) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/27091905853/job/79956895377) | [2s](https://github.com/iree-org/iree/actions/runs/27091905853/job/79956895377) | [2s](https://github.com/iree-org/iree/actions/runs/27091905853/job/79956895377) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 301 | 1% (2/301) |  | 1d19h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 256 | 3% (8/256) |  | 1d20h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 230 | 0% (1/230) |  | 1d20h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 215 | 0% (0/215) |  | 1d21h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 69 | 0% (0/69) |  | 1d22h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
