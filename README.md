# iree-ci-monitor

_Updated: 2026-05-03 18:11 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | 0 | [20m03s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721713) | [25m06s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721730) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | 0 | [18m38s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721734) | [18m38s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721734) | — | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | 0 | [13m30s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721731) | [15m13s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721727) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | 0 | [13m29s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721691) | [13m29s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721691) | — | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 1 | 0 | — | 0 | [9m42s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721722) | [9m42s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721722) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | 0 | [7m09s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721729) | [9m19s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721742) | — | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | 0 | [7m28s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721723) | [7m28s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721723) | — | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | 0 | [4m38s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721677) | [4m38s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721677) | — | `shark10-ci` |
| `azure-linux-scale` | ossci | 10 | 0 | — | 0 | [11s](https://github.com/iree-org/iree/actions/runs/25286743834/job/74132344070) | [2m17s](https://github.com/iree-org/iree/actions/runs/25286598725/job/74131872593) | — | 10 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | 0 | [18s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721666) | [19s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721737) | — | 4 |
| `ubuntu-24.04` | github-hosted | 29 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721642) | [8s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74134706935) | — | 29 |
| `azure-windows-scale` | ossci | 2 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25286598709/job/74131870302) | [6s](https://github.com/iree-org/iree/actions/runs/25286743834/job/74132344123) | — | 2 |
| `windows-2022` | github-hosted | 6 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25286743834/job/74132344023) | [4s](https://github.com/iree-org/iree/actions/runs/25286598709/job/74131870232) | — | 6 |
| `macos-14` | github-hosted | 6 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25286598709/job/74131870298) | [3s](https://github.com/iree-org/iree/actions/runs/25286743834/job/74132344031) | — | 6 |
| `ubuntu-24.04-arm` | github-hosted | 6 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25286598709/job/74131870241) | [2s](https://github.com/iree-org/iree/actions/runs/25286743834/job/74132344062) | — | 6 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721654) | [2s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721654) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721663) | [2s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721663) | — | `shark01-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721698) | [2s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721698) | — | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 1 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721716) | [2s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721716) | — | `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721718) | [2s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721718) | — | `iree-mi308-1` |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721638) | [1s](https://github.com/iree-org/iree/actions/runs/25286743841/job/74132721638) | — | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1023 | 5% (53/1022) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 884 | 3% (23/883) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 615 | 6% (38/615) |  | 6h31m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 799 | 1% (11/799) |  | 6h36m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 237 | 2% (5/237) |  | 6h45m ago |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 60 | 12% (7/60) |  | 6d03h ago |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
