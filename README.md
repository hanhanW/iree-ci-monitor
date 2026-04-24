# iree-ci-monitor

_Updated: 2026-04-24 05:41 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 7 | 0 | — | 0 | [9m22s](https://github.com/iree-org/iree/actions/runs/24870706561/job/72817086589) | [34m18s](https://github.com/iree-org/iree/actions/runs/24879277085/job/72844226639) | 0% (0/1) | 1 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 7 | 1 | [5h59m](https://github.com/iree-org/iree/actions/runs/24874178460/job/72833034597) | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24870706561/job/72817086519) | [32m45s](https://github.com/iree-org/iree/actions/runs/24879277085/job/72844226712) | 100% (1/1) | 2 |
| `Linux,X64,iree-w7900` | self-hosted | 7 | 0 | — | 0 | [4m17s](https://github.com/iree-org/iree/actions/runs/24874178460/job/72833034464) | [30m20s](https://github.com/iree-org/iree/actions/runs/24879277085/job/72844226511) | 0% (0/1) | 2 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 7 | 0 | — | 0 | [7m02s](https://github.com/iree-org/iree/actions/runs/24879277085/job/72844226638) | [29m46s](https://github.com/iree-org/iree/actions/runs/24879287212/job/72844568358) | 0% (0/1) | 1 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 21 | 0 | — | 1 | [4m29s](https://github.com/iree-org/iree/actions/runs/24874178460/job/72833034559) | [24m32s](https://github.com/iree-org/iree/actions/runs/24879287212/job/72844568457) | 0% (0/3) | 4 |
| `Linux,X64,iree-r9700` | self-hosted | 7 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24878911921/job/72843160032) | [24m09s](https://github.com/iree-org/iree/actions/runs/24870706561/job/72817086511) | 0% (0/1) | 1 |
| `Linux,X64,gfx1100` | self-hosted | 14 | 0 | — | 0 | [8m58s](https://github.com/iree-org/iree/actions/runs/24874178460/job/72833034553) | [20m39s](https://github.com/iree-org/iree/actions/runs/24879277085/job/72844226714) | 0% (0/2) | 3 |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 7 | 0 | — | 0 | [14m43s](https://github.com/iree-org/iree/actions/runs/24880836113/job/72849408912) | [20m30s](https://github.com/iree-org/iree/actions/runs/24879277085/job/72844226644) | 0% (0/1) | 1 |
| `Linux,X64,gfx1201` | self-hosted | 14 | 0 | — | 1 | [9m59s](https://github.com/iree-org/iree/actions/runs/24874178460/job/72833034509) | [19m22s](https://github.com/iree-org/iree/actions/runs/24879277085/job/72844226667) | 0% (0/2) | 1 |
| `Linux,X64,rdna3` | self-hosted | 7 | 0 | — | 1 | [2m48s](https://github.com/iree-org/iree/actions/runs/24879287212/job/72844568339) | [17m17s](https://github.com/iree-org/iree/actions/runs/24879277085/job/72844226678) | 0% (0/1) | 2 |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 7 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24879277085/job/72844226538) | [15m08s](https://github.com/iree-org/iree/actions/runs/24870706561/job/72817086588) | 0% (0/1) | 2 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 7 | 0 | — | 0 | [4m25s](https://github.com/iree-org/iree/actions/runs/24874178460/job/72833034587) | [13m43s](https://github.com/iree-org/iree/actions/runs/24879277085/job/72844226655) | 0% (0/1) | 3 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 7 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24878911921/job/72843160173) | [7m49s](https://github.com/iree-org/iree/actions/runs/24879287212/job/72844568422) | 0% (0/1) | 1 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 28 | 0 | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/24879287212/job/72844568446) | [6m45s](https://github.com/iree-org/iree/actions/runs/24879287212/job/72844568333) | 0% (0/4) | 25 |
| `azure-windows-scale` | ossci | 12 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24874178459/job/72827158093) | [4m02s](https://github.com/iree-org/iree/actions/runs/24873997941/job/72826543959) | 0% (0/1) | 11 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 2 | 0 | — | 0 | [1m56s](https://github.com/iree-org/iree/actions/runs/24883389184/job/72857245507) | [2m25s](https://github.com/iree-org/iree/actions/runs/24873643813/job/72825431790) | 0% (0/1) | 2 |
| `azure-linux-scale` | ossci | 67 | 3 | [7h00m](https://github.com/iree-org/iree/actions/runs/24874178459/job/72827158113) | 1 | [11s](https://github.com/iree-org/iree/actions/runs/24880836098/job/72848648202) | [2m11s](https://github.com/iree-org/iree/actions/runs/24873441423/job/72824763550) | 0% (0/8) | 60 |
| `macos-14` | github-hosted | 40 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/24880836098/job/72848648132) | [1m42s](https://github.com/iree-org/iree/actions/runs/24879287209/job/72843664135) | 0% (0/3) | 39 |
| `ubuntu-24.04-arm` | github-hosted | 39 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/24874529377/job/72828137980) | [1m24s](https://github.com/iree-org/iree/actions/runs/24879287209/job/72843664102) | 0% (0/3) | 39 |
| `ubuntu-24.04` | github-hosted | 198 | 0 | — | 4 | [2s](https://github.com/iree-org/iree/actions/runs/24878911904/job/72842174640) | [1m09s](https://github.com/iree-org/iree/actions/runs/24873643394/job/72825606187) | 10% (2/21) | 189 |
| `windows-2022` | github-hosted | 38 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/24874529377/job/72828137922) | [58s](https://github.com/iree-org/iree/actions/runs/24879287209/job/72843664105) | 0% (0/3) | 38 |
| `macos-15-intel` | github-hosted | 2 | 0 | — | 1 | [5s](https://github.com/iree-org/iree/actions/runs/24883381503/job/72857218143) | [11s](https://github.com/iree-org/iree/actions/runs/24873643813/job/72825431856) | — | 2 |
| `ubuntu-latest` | github-hosted | 11 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24886932835/job/72869127532) | [4s](https://github.com/iree-org/iree/actions/runs/24873642503/job/72825416805) | 0% (0/2) | 11 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 7 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24880836113/job/72849408765) | [2s](https://github.com/iree-org/iree/actions/runs/24879287212/job/72844568304) | 0% (0/1) | 6 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, +2 more | 167 | 1% (2/163) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +5 more | 160 | 2% (3/155) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +7 more | 185 | 14% (26/181) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +2 more | 138 | 0% (0/134) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 54 | 0% (0/51) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 5h59m (> 2h00m)
- **[stale-queued]** `azure-linux-scale` oldest queued job waiting 7h00m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
