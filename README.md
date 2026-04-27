# iree-ci-monitor

_Updated: 2026-04-27 00:14 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | 0 | [17m20s](https://github.com/iree-org/iree/actions/runs/24977091246/job/73131531103) | [31m47s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696508) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24977091246/job/73131531023) | [24m46s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696285) | — | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 2 | 0 | — | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24977091246/job/73131531113) | [20m31s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696514) | — | `shark10-ci-2` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | 0 | [9m47s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696478) | [20m00s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696530) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24977091246/job/73131531086) | [16m27s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696479) | — | `shark10-ci-2` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 6 | 0 | — | 0 | [5m56s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696483) | [15m13s](https://github.com/iree-org/iree/actions/runs/24977091246/job/73131531108) | — | `shark01-ci`, `shark10-ci-2`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | 0 | [5m54s](https://github.com/iree-org/iree/actions/runs/24977091246/job/73131531114) | [12m56s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696495) | — | `shark01-ci`, `shark10-ci-2`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696402) | [10m44s](https://github.com/iree-org/iree/actions/runs/24977091246/job/73131531041) | — | `shark01-ci`, `shark10-ci-2` |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24977091246/job/73131530990) | [10m26s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696366) | — | `shark01-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | 0 | [8m29s](https://github.com/iree-org/iree/actions/runs/24977091246/job/73131531099) | [10m17s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696569) | — | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 2 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24977091246/job/73131531094) | [4m52s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696502) | — | `shark10-ci-2`, `shark55-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696471) | [2m18s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696566) | — | 8 |
| `azure-linux-scale` | ossci | 10 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/24977091240/job/73131018869) | [11s](https://github.com/iree-org/iree/actions/runs/24977783493/job/73133237280) | — | 10 |
| `windows-2022` | github-hosted | 8 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/24977783493/job/73133237349) | [5s](https://github.com/iree-org/iree/actions/runs/24977783493/job/73133237240) | — | 8 |
| `ubuntu-24.04` | github-hosted | 45 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696367) | [3s](https://github.com/iree-org/iree/actions/runs/24977091246/job/73131531065) | 0% (0/4) | 45 |
| `macos-14` | github-hosted | 8 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/24977783493/job/73133237335) | [3s](https://github.com/iree-org/iree/actions/runs/24979181479/job/73137375619) | — | 8 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/24977783493/job/73133237304) | [2s](https://github.com/iree-org/iree/actions/runs/24979181479/job/73137375629) | — | 9 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 2 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696347) | [2s](https://github.com/iree-org/iree/actions/runs/24977091246/job/73131531013) | — | 2 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696444) | [2s](https://github.com/iree-org/iree/actions/runs/24977091246/job/73131531076) | — | `iree-mi308-1` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696465) | [2s](https://github.com/iree-org/iree/actions/runs/24977091246/job/73131531084) | — | `shark01-ci`, `shark10-ci-2` |
| `azure-windows-scale` | ossci | 2 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24977091240/job/73131018867) | [1s](https://github.com/iree-org/iree/actions/runs/24977783493/job/73133237341) | — | 2 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 384 | 2% (7/380) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 415 | 14% (57/411) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 304 | 0% (0/300) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 320 | 3% (9/315) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 116 | 0% (0/113) | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
