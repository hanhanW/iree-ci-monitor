# iree-ci-monitor

_Updated: 2026-09-03 21:38 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-24.04` | github-hosted | 11 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/33815837578/job/100847738270) | [7s](https://github.com/iree-org/iree/actions/runs/33815837509/job/100847723842) | 0% (0/3) | 8 |
| `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/33815511473/job/100846675730) | [2s](https://github.com/iree-org/iree/actions/runs/33815511473/job/100846675730) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | pkgci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/33815837509/job/100847723842) | [7s](https://github.com/iree-org/iree/actions/runs/33815837509/job/100847723842) | [7s](https://github.com/iree-org/iree/actions/runs/33815837509/job/100847723842) | 1 |
| `.github/workflows/ci.yml` | ci_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33815837578/job/100847738270) | [3s](https://github.com/iree-org/iree/actions/runs/33815837578/job/100847738270) | [3s](https://github.com/iree-org/iree/actions/runs/33815837578/job/100847738270) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33836636161/job/100910396397) | [3s](https://github.com/iree-org/iree/actions/runs/33836636161/job/100910396397) | [3s](https://github.com/iree-org/iree/actions/runs/33836636161/job/100910396397) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/33836636161/job/100912148219) | [3s](https://github.com/iree-org/iree/actions/runs/33836636161/job/100912148219) | [3s](https://github.com/iree-org/iree/actions/runs/33836636161/job/100912148219) | 1 |
| `.github/workflows/ci.yml` | setup / setup | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33815837578/job/100847675591) | [2s](https://github.com/iree-org/iree/actions/runs/33815837578/job/100847675591) | [2s](https://github.com/iree-org/iree/actions/runs/33815837578/job/100847675591) | 1 |
| `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33815837369/job/100847673565) | [2s](https://github.com/iree-org/iree/actions/runs/33815837369/job/100847673565) | [2s](https://github.com/iree-org/iree/actions/runs/33815837369/job/100847673565) | 1 |
| `.github/workflows/pkgci.yml` | setup / setup | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33815837509/job/100847675017) | [2s](https://github.com/iree-org/iree/actions/runs/33815837509/job/100847675017) | [2s](https://github.com/iree-org/iree/actions/runs/33815837509/job/100847675017) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33836636161/job/100910396272) | [2s](https://github.com/iree-org/iree/actions/runs/33836636161/job/100910396272) | [2s](https://github.com/iree-org/iree/actions/runs/33836636161/job/100910396272) | 1 |
| `dynamic/dependabot/dependabot-updates` | Dependabot | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/33815511473/job/100846675730) | [2s](https://github.com/iree-org/iree/actions/runs/33815511473/job/100846675730) | [2s](https://github.com/iree-org/iree/actions/runs/33815511473/job/100846675730) | 1 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 1 | 0 | — | — | 0s | 0s | 0s | 0 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 1 | 0 | — | — | 0s | 0s | 0s | 0 |
| `.github/workflows/pull_request_greeter.yml` | pr-greeter | `ubuntu-24.04` | 1 | 0 | — | — | 0s | 0s | 0s | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 143 | 1% (1/143) |  | 13h40m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 200 | 1% (2/200) |  | 13h42m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 132 | 0% (0/132) |  | 13h43m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 166 | 4% (7/166) |  | 13h45m ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
