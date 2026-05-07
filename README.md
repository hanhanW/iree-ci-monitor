# iree-ci-monitor

_Updated: 2026-05-07 05:59 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 8 | 0 | — | 1 | [8m55s](https://github.com/iree-org/iree/actions/runs/25495012547/job/74813441574) | [41m38s](https://github.com/iree-org/iree/actions/runs/25494600410/job/74812568456) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 8 | 0 | — | 0 | [19m32s](https://github.com/iree-org/iree/actions/runs/25476418237/job/74751411100) | [34m47s](https://github.com/iree-org/iree/actions/runs/25495012547/job/74813441637) | — | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 8 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25473551877/job/74744810822) | [34m33s](https://github.com/iree-org/iree/actions/runs/25494600410/job/74812568369) | — | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 8 | 0 | — | 0 | [10m39s](https://github.com/iree-org/iree/actions/runs/25476418237/job/74751411045) | [33m36s](https://github.com/iree-org/iree/actions/runs/25473551877/job/74744810947) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 8 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25494600410/job/74812568547) | [32m41s](https://github.com/iree-org/iree/actions/runs/25473551877/job/74744810892) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 8 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25473551877/job/74744810813) | [29m45s](https://github.com/iree-org/iree/actions/runs/25494600410/job/74812568587) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 16 | 3 | [45m26s](https://github.com/iree-org/iree/actions/runs/25494600410/job/74812568576) | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25476418237/job/74751411060) | [26m41s](https://github.com/iree-org/iree/actions/runs/25476418237/job/74751411118) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 8 | 0 | — | 0 | [4m30s](https://github.com/iree-org/iree/actions/runs/25494600410/job/74812568410) | [24m33s](https://github.com/iree-org/iree/actions/runs/25473551877/job/74744810817) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 8 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25475711162/job/74749358540) | [21m49s](https://github.com/iree-org/iree/actions/runs/25473551877/job/74744810882) | — | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 8 | 0 | — | 0 | [6m32s](https://github.com/iree-org/iree/actions/runs/25476418237/job/74751411123) | [16m56s](https://github.com/iree-org/iree/actions/runs/25494600410/job/74812568575) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 17 | 0 | — | 0 | [5m12s](https://github.com/iree-org/iree/actions/runs/25495012547/job/74813441570) | [16m30s](https://github.com/iree-org/iree/actions/runs/25476418237/job/74751411128) | — | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 16 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25475355416/job/74748239713) | [11m42s](https://github.com/iree-org/iree/actions/runs/25495012547/job/74813441381) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 8 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25476418237/job/74751411135) | [4m59s](https://github.com/iree-org/iree/actions/runs/25495012547/job/74813441678) | — | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 32 | 0 | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/25476418237/job/74751411024) | [2m18s](https://github.com/iree-org/iree/actions/runs/25495012547/job/74813441454) | — | 32 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m42s](https://github.com/iree-org/iree/actions/runs/25489252129/job/74792730081) | [1m42s](https://github.com/iree-org/iree/actions/runs/25489252129/job/74792730081) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 68 | 0 | — | 6 | [8s](https://github.com/iree-org/iree/actions/runs/25475711154/job/74748793147) | [1m37s](https://github.com/iree-org/iree/actions/runs/25494769773/job/74811561391) | 0% (0/2) | 64 |
| `macos-14` | github-hosted | 42 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25475355423/job/74747567357) | [1m31s](https://github.com/iree-org/iree/actions/runs/25494769773/job/74811561399) | 0% (0/3) | 42 |
| `windows-2022` | github-hosted | 41 | 0 | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/25494600372/job/74811071191) | [1m24s](https://github.com/iree-org/iree/actions/runs/25494769773/job/74811561415) | — | 41 |
| `ubuntu-24.04-arm` | github-hosted | 42 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25476244779/job/74750358060) | [31s](https://github.com/iree-org/iree/actions/runs/25494769773/job/74811561355) | 0% (0/3) | 42 |
| `ubuntu-24.04` | github-hosted | 211 | 0 | — | 4 | [3s](https://github.com/iree-org/iree/actions/runs/25497024641/job/74819453583) | [10s](https://github.com/iree-org/iree/actions/runs/25490669675/job/74797773653) | 0% (0/8) | 211 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25497023026/job/74819393714) | [9s](https://github.com/iree-org/iree/actions/runs/25497023026/job/74819393668) | 0% (0/2) | 9 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25489233190/job/74792665775) | [3s](https://github.com/iree-org/iree/actions/runs/25489233190/job/74792665775) | — | 1 |
| `azure-windows-scale` | ossci | 13 | 0 | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/25490513094/job/74797392226) | [2s](https://github.com/iree-org/iree/actions/runs/25494769773/job/74811561469) | — | 13 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 8 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25476418237/job/74751411038) | [2s](https://github.com/iree-org/iree/actions/runs/25495012547/job/74813441303) | — | 8 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 892 | 6% (56/890) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 769 | 2% (12/767) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 984 | 2% (16/980) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 672 | 1% (6/670) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 235 | 2% (4/234) | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
