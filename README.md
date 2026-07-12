# iree-ci-monitor

_Updated: 2026-07-12 11:36 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 15 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29196476977/job/86660254753) | [3s](https://github.com/iree-org/iree/actions/runs/29196476977/job/86660254756) | 0% (0/3) | 15 |
| `ubuntu-24.04` | github-hosted | 5 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29190376626/job/86643973793) | [2s](https://github.com/iree-org/iree/actions/runs/29196300805/job/86659773267) | 0% (0/1) | 5 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29190570147/job/86644399511) | [3s](https://github.com/iree-org/iree/actions/runs/29194648427/job/86655348210) | [3s](https://github.com/iree-org/iree/actions/runs/29194648427/job/86655348210) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29194648427/job/86655348214) | [3s](https://github.com/iree-org/iree/actions/runs/29196476977/job/86660254756) | [3s](https://github.com/iree-org/iree/actions/runs/29196476977/job/86660254756) | 3 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 3 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/29194648427/job/86655348213) | [3s](https://github.com/iree-org/iree/actions/runs/29196476977/job/86660254759) | [3s](https://github.com/iree-org/iree/actions/runs/29196476977/job/86660254759) | 3 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29196476813/job/86660264248) | [3s](https://github.com/iree-org/iree/actions/runs/29190569888/job/86644414689) | [3s](https://github.com/iree-org/iree/actions/runs/29190569888/job/86644414689) | 2 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29190416411/job/86643984623) | [2s](https://github.com/iree-org/iree/actions/runs/29196300805/job/86659773267) | [2s](https://github.com/iree-org/iree/actions/runs/29196300805/job/86659773267) | 2 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29190569888/job/86644398529) | [2s](https://github.com/iree-org/iree/actions/runs/29196476813/job/86660254201) | [2s](https://github.com/iree-org/iree/actions/runs/29196476813/job/86660254201) | 2 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29190569888/job/86644414684) | [2s](https://github.com/iree-org/iree/actions/runs/29196476813/job/86660264247) | [2s](https://github.com/iree-org/iree/actions/runs/29196476813/job/86660264247) | 2 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29182078716/job/86643872977) | [2s](https://github.com/iree-org/iree/actions/runs/29182078716/job/86643872977) | [2s](https://github.com/iree-org/iree/actions/runs/29182078716/job/86643872977) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29190376626/job/86643973793) | [2s](https://github.com/iree-org/iree/actions/runs/29190376626/job/86643973793) | [2s](https://github.com/iree-org/iree/actions/runs/29190376626/job/86643973793) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29190376626/job/86643881306) | [2s](https://github.com/iree-org/iree/actions/runs/29190376626/job/86643881306) | [2s](https://github.com/iree-org/iree/actions/runs/29190376626/job/86643881306) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 159 | 7% (11/158) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 202 | 1% (3/201) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 162 | 1% (1/161) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 150 | 1% (1/149) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 47 | 11% (5/47) |  | 2d06h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
