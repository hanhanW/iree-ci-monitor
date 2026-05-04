# iree-ci-monitor

_Updated: 2026-05-04 05:54 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 14 | 1 | [6h04m](https://github.com/iree-org/iree/actions/runs/25304863493/job/74179394357) | 1 | [21m54s](https://github.com/iree-org/iree/actions/runs/25303245167/job/74174737168) | [48m21s](https://github.com/iree-org/iree/actions/runs/25305217616/job/74180522090) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 7 | 0 | — | 0 | [10m54s](https://github.com/iree-org/iree/actions/runs/25304863493/job/74179394203) | [42m59s](https://github.com/iree-org/iree/actions/runs/25305217616/job/74180521921) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 7 | 0 | — | 0 | [18m41s](https://github.com/iree-org/iree/actions/runs/25302005514/job/74171195301) | [30m56s](https://github.com/iree-org/iree/actions/runs/25305217616/job/74180522038) | 0% (0/4) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 7 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25303245167/job/74174737140) | [28m42s](https://github.com/iree-org/iree/actions/runs/25304863493/job/74179394238) | 25% (1/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 7 | 0 | — | 0 | [10m52s](https://github.com/iree-org/iree/actions/runs/25302005514/job/74171195225) | [24m22s](https://github.com/iree-org/iree/actions/runs/25303245167/job/74174737161) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 7 | 0 | — | 0 | [14m42s](https://github.com/iree-org/iree/actions/runs/25302005514/job/74171195287) | [22m22s](https://github.com/iree-org/iree/actions/runs/25305217616/job/74180522133) | 25% (1/4) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 7 | 0 | — | 0 | [5m46s](https://github.com/iree-org/iree/actions/runs/25304863493/job/74179394267) | [21m47s](https://github.com/iree-org/iree/actions/runs/25302005514/job/74171195285) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 7 | 0 | — | 0 | [9m18s](https://github.com/iree-org/iree/actions/runs/25305217616/job/74180522131) | [18m44s](https://github.com/iree-org/iree/actions/runs/25304863493/job/74179394308) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 14 | 0 | — | 0 | [4m55s](https://github.com/iree-org/iree/actions/runs/25303245167/job/74174737151) | [15m42s](https://github.com/iree-org/iree/actions/runs/25303683554/job/74175958503) | 0% (0/8) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 14 | 0 | — | 0 | [5m49s](https://github.com/iree-org/iree/actions/runs/25302005514/job/74171195263) | [13m59s](https://github.com/iree-org/iree/actions/runs/25303683554/job/74175958500) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 7 | 0 | — | 0 | [4m25s](https://github.com/iree-org/iree/actions/runs/25303683554/job/74175958543) | [12m44s](https://github.com/iree-org/iree/actions/runs/25303245167/job/74174737194) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 7 | 0 | — | 0 | [2m19s](https://github.com/iree-org/iree/actions/runs/25305217616/job/74180522068) | [11m56s](https://github.com/iree-org/iree/actions/runs/25303245167/job/74174737122) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m46s](https://github.com/iree-org/iree/actions/runs/25312820949/job/74203454593) | [1m46s](https://github.com/iree-org/iree/actions/runs/25312820949/job/74203454593) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 20 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25303245164/job/74173991502) | [1m28s](https://github.com/iree-org/iree/actions/runs/25305217605/job/74179613441) | 0% (0/9) | 20 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25303751332/job/74175426969) | [1m11s](https://github.com/iree-org/iree/actions/runs/25305217605/job/74179613429) | 0% (0/9) | 21 |
| `azure-linux-scale` | ossci | 36 | 0 | — | 0 | [11s](https://github.com/iree-org/iree/actions/runs/25303245167/job/74173991641) | [24s](https://github.com/iree-org/iree/actions/runs/25301642275/job/74169510722) | 0% (0/21) | 35 |
| `ubuntu-24.04` | github-hosted | 135 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25304863493/job/74179394293) | [20s](https://github.com/iree-org/iree/actions/runs/25303683554/job/74175958525) | 6% (4/65) | 125 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 28 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25305217616/job/74180522009) | [19s](https://github.com/iree-org/iree/actions/runs/25303245167/job/74174737236) | 31% (5/16) | 25 |
| `macos-14` | github-hosted | 21 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25303245164/job/74173991445) | [19s](https://github.com/iree-org/iree/actions/runs/25305217605/job/74179613447) | 0% (0/9) | 21 |
| `ubuntu-latest` | github-hosted | 11 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25316625145/job/74215522058) | [9s](https://github.com/iree-org/iree/actions/runs/25316625145/job/74215547692) | 0% (0/6) | 11 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25312806680/job/74203407681) | [3s](https://github.com/iree-org/iree/actions/runs/25312806680/job/74203407681) | — | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 7 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25304863493/job/74193756362) | [2s](https://github.com/iree-org/iree/actions/runs/25303245167/job/74174737137) | 75% (3/4) | 7 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 7 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25305217616/job/74180522029) | [2s](https://github.com/iree-org/iree/actions/runs/25303683554/job/74175958539) | 0% (0/4) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 6 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25303245164/job/74173991544) | [1s](https://github.com/iree-org/iree/actions/runs/25305217605/job/74179613477) | 0% (0/3) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1056 | 5% (55/1054) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 909 | 3% (24/908) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 645 | 6% (41/645) |  | 4h06m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 819 | 1% (12/819) |  | 5h33m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 245 | 2% (5/245) |  | 5h43m ago |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 60 | 12% (7/60) |  | 6d15h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 6h04m (> 2h00m)
- **[high-failure-main]** `linux-mi325-1gpu-ossci-iree-org` main-branch failure rate 31% (5/16)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
