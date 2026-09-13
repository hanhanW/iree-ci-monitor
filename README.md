# iree-ci-monitor

_Updated: 2026-09-13 09:22 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735931895) | [3s](https://github.com/iree-org/iree/actions/runs/34761829563/job/103735908124) | 0% (0/3) | 9 |
| `ubuntu-24.04` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/34761556655/job/103735181276) | [2s](https://github.com/iree-org/iree/actions/runs/34761556655/job/103735181276) | 0% (0/1) | 1 |
| `Linux,X64,gfx1201` | self-hosted | 1 | 1 | [2h00m](https://github.com/iree-org/iree/actions/runs/34581758865/job/103214541971) | 2026-09-11 04:27 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [2h00m](https://github.com/iree-org/iree/actions/runs/34581758865/job/103214541971) | 2026-09-11 04:27 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 1 | 1 | [2h00m](https://github.com/iree-org/iree/actions/runs/34581758865/job/103214541971) | 2026-09-11 04:27 PDT | 0s | 0s | 0s | 0 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34760657622/job/103732802833) | [3s](https://github.com/iree-org/iree/actions/runs/34761829563/job/103735908124) | [3s](https://github.com/iree-org/iree/actions/runs/34761829563/job/103735908124) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34760657622/job/103732802919) | [2s](https://github.com/iree-org/iree/actions/runs/34761829563/job/103735907933) | [2s](https://github.com/iree-org/iree/actions/runs/34761829563/job/103735907933) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34760657622/job/103732802905) | [2s](https://github.com/iree-org/iree/actions/runs/34761829563/job/103735908098) | [2s](https://github.com/iree-org/iree/actions/runs/34761829563/job/103735908098) | 2 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34761556655/job/103735181276) | [2s](https://github.com/iree-org/iree/actions/runs/34761556655/job/103735181276) | [2s](https://github.com/iree-org/iree/actions/runs/34761556655/job/103735181276) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735908426) | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735908426) | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735908426) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735931895) | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735931895) | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735931895) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735931978) | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735931978) | [2s](https://github.com/iree-org/iree/actions/runs/34761829494/job/103735931978) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | 0s | 0s | 0s | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 254 | 8% (20/254) |  | 1d16h ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 284 | 1% (4/284) |  | 1d16h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 214 | 1% (3/214) |  | 1d16h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 208 | 1% (2/208) |  | 1d16h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 2h00m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
