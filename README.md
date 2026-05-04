# iree-ci-monitor

_Updated: 2026-05-04 00:23 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 14 | 3 | [33m47s](https://github.com/iree-org/iree/actions/runs/25304863493/job/74179394357) | 1 | [12m26s](https://github.com/iree-org/iree/actions/runs/25302005514/job/74171195335) | [36m07s](https://github.com/iree-org/iree/actions/runs/25303245167/job/74174737230) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 7 | 1 | [23m09s](https://github.com/iree-org/iree/actions/runs/25305217616/job/74180522038) | 0 | [18m41s](https://github.com/iree-org/iree/actions/runs/25302005514/job/74171195301) | [32m17s](https://github.com/iree-org/iree/actions/runs/25297812877/job/74160026431) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 7 | 1 | [23m09s](https://github.com/iree-org/iree/actions/runs/25305217616/job/74180521966) | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25302005514/job/74171195193) | [28m42s](https://github.com/iree-org/iree/actions/runs/25304863493/job/74179394238) | 50% (1/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 7 | 0 | — | 1 | [15m24s](https://github.com/iree-org/iree/actions/runs/25304863493/job/74179394334) | [28m12s](https://github.com/iree-org/iree/actions/runs/25297812877/job/74160026406) | 50% (1/2) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 7 | 0 | — | 0 | [11m40s](https://github.com/iree-org/iree/actions/runs/25303683554/job/74175958510) | [24m22s](https://github.com/iree-org/iree/actions/runs/25303245167/job/74174737161) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 7 | 0 | — | 0 | [6m00s](https://github.com/iree-org/iree/actions/runs/25305217616/job/74180522078) | [21m47s](https://github.com/iree-org/iree/actions/runs/25302005514/job/74171195285) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 14 | 0 | — | 1 | [5m49s](https://github.com/iree-org/iree/actions/runs/25302005514/job/74171195263) | [19m08s](https://github.com/iree-org/iree/actions/runs/25297812877/job/74160026421) | 0% (0/5) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 7 | 0 | — | 0 | [9m18s](https://github.com/iree-org/iree/actions/runs/25305217616/job/74180522131) | [18m44s](https://github.com/iree-org/iree/actions/runs/25304863493/job/74179394308) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 7 | 1 | [23m09s](https://github.com/iree-org/iree/actions/runs/25305217616/job/74180521921) | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25302005514/job/74171195221) | [17m26s](https://github.com/iree-org/iree/actions/runs/25303683554/job/74175958456) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 14 | 0 | — | 0 | [4m15s](https://github.com/iree-org/iree/actions/runs/25302005514/job/74171195279) | [15m42s](https://github.com/iree-org/iree/actions/runs/25303683554/job/74175958503) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 7 | 0 | — | 0 | [9m23s](https://github.com/iree-org/iree/actions/runs/25304863493/job/74179394302) | [15m28s](https://github.com/iree-org/iree/actions/runs/25297812877/job/74160026401) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 7 | 0 | — | 0 | [2m19s](https://github.com/iree-org/iree/actions/runs/25305217616/job/74180522068) | [11m56s](https://github.com/iree-org/iree/actions/runs/25303245167/job/74174737122) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `windows-2022` | github-hosted | 23 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25304863494/job/74178616306) | [1m28s](https://github.com/iree-org/iree/actions/runs/25305217605/job/74179613441) | 0% (0/9) | 23 |
| `ubuntu-24.04-arm` | github-hosted | 24 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25303751332/job/74175426951) | [1m11s](https://github.com/iree-org/iree/actions/runs/25305217605/job/74179613429) | 0% (0/9) | 24 |
| `azure-linux-scale` | ossci | 38 | 0 | — | 1 | [11s](https://github.com/iree-org/iree/actions/runs/25305217605/job/74179613505) | [24s](https://github.com/iree-org/iree/actions/runs/25301642275/job/74169510722) | 0% (0/17) | 38 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 28 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25303245167/job/74174737216) | [19s](https://github.com/iree-org/iree/actions/runs/25303245167/job/74174737236) | 25% (3/12) | 28 |
| `macos-14` | github-hosted | 23 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25303751332/job/74175426975) | [19s](https://github.com/iree-org/iree/actions/runs/25305217605/job/74179613447) | 0% (0/9) | 23 |
| `ubuntu-24.04` | github-hosted | 133 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25303683556/job/74175228543) | [16s](https://github.com/iree-org/iree/actions/runs/25305217605/job/74179613459) | 6% (3/52) | 133 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25304862646/job/74178591774) | [7s](https://github.com/iree-org/iree/actions/runs/25305217100/job/74179595849) | 0% (0/6) | 6 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 7 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25304863493/job/74179394235) | [2s](https://github.com/iree-org/iree/actions/runs/25303245167/job/74174737137) | 67% (2/3) | 7 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 7 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25305217616/job/74180522029) | [2s](https://github.com/iree-org/iree/actions/runs/25303683554/job/74175958539) | 0% (0/3) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 7 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25303245164/job/74173991544) | [1s](https://github.com/iree-org/iree/actions/runs/25305217605/job/74179613477) | 0% (0/3) | 7 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 639 | 6% (41/638) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1048 | 5% (55/1046) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 906 | 3% (24/904) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 816 | 1% (12/816) |  | 2m54s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 244 | 2% (5/244) |  | 12m44s ago |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 60 | 12% (7/60) |  | 6d10h ago |

## Alerts

- **[high-failure-main]** `linux-mi325-1gpu-ossci-iree-org` main-branch failure rate 25% (3/12)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
