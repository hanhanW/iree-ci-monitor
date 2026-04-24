# iree-ci-monitor

_Updated: 2026-04-24 00:01 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 26 | 20 | [9h46m](https://github.com/iree-org/iree/actions/runs/24858194412/job/72780172445) | 1 | [0s](https://github.com/iree-org/iree/actions/runs/24862703064/job/72792565113) | [29m52s](https://github.com/iree-org/iree/actions/runs/24866931477/job/72805571843) | 0% (0/2) | 1 |
| `Linux,X64,gfx1100` | self-hosted | 26 | 11 | [9h46m](https://github.com/iree-org/iree/actions/runs/24858194412/job/72780172498) | 2 | [2s](https://github.com/iree-org/iree/actions/runs/24870706561/job/72817086595) | [22m11s](https://github.com/iree-org/iree/actions/runs/24861650625/job/72791150360) | 0% (0/6) | 3 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 13 | 9 | [9h46m](https://github.com/iree-org/iree/actions/runs/24858194412/job/72780172450) | 1 | [0s](https://github.com/iree-org/iree/actions/runs/24866300244/job/72803732728) | [19m19s](https://github.com/iree-org/iree/actions/runs/24870706561/job/72817086538) | 0% (0/1) | 1 |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 13 | 9 | [9h46m](https://github.com/iree-org/iree/actions/runs/24858194412/job/72780172578) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24862703064/job/72792565237) | [17m43s](https://github.com/iree-org/iree/actions/runs/24870706561/job/72817086610) | 0% (0/2) | 1 |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 35 | 11 | [9h46m](https://github.com/iree-org/iree/actions/runs/24858194412/job/72780172460) | 5 | [25s](https://github.com/iree-org/iree/actions/runs/24861650625/job/72791150306) | [17m40s](https://github.com/iree-org/iree/actions/runs/24874178460/job/72833034591) | 0% (0/9) | 4 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 13 | 9 | [9h46m](https://github.com/iree-org/iree/actions/runs/24858194412/job/72780172520) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24862703064/job/72792565206) | [13m31s](https://github.com/iree-org/iree/actions/runs/24874178460/job/72833034582) | 0% (0/2) | 1 |
| `Linux,X64,iree-r9700` | self-hosted | 13 | 7 | [9h46m](https://github.com/iree-org/iree/actions/runs/24858194412/job/72780172397) | 1 | [0s](https://github.com/iree-org/iree/actions/runs/24867333949/job/72806909906) | [13m00s](https://github.com/iree-org/iree/actions/runs/24866931477/job/72805571748) | 0% (0/1) | 1 |
| `Linux,X64,rdna3` | self-hosted | 13 | 6 | [9h46m](https://github.com/iree-org/iree/actions/runs/24858194412/job/72780172455) | 1 | [1s](https://github.com/iree-org/iree/actions/runs/24867333949/job/72806909994) | [12m40s](https://github.com/iree-org/iree/actions/runs/24860904417/job/72786810885) | 0% (0/4) | 3 |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 17 | 11 | [9h46m](https://github.com/iree-org/iree/actions/runs/24858194412/job/72780172548) | 1 | [0s](https://github.com/iree-org/iree/actions/runs/24861685549/job/72791988765) | [11m01s](https://github.com/iree-org/iree/actions/runs/24866931477/job/72805571817) | 0% (0/2) | 2 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 13 | 2 | [8h06m](https://github.com/iree-org/iree/actions/runs/24862703064/job/72792565453) | 2 | [1s](https://github.com/iree-org/iree/actions/runs/24874178460/job/72833034556) | [7m48s](https://github.com/iree-org/iree/actions/runs/24861766292/job/72791715798) | 0% (0/5) | 1 |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 13 | 8 | [9h46m](https://github.com/iree-org/iree/actions/runs/24858194412/job/72780172468) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24866704561/job/72804850730) | [5m19s](https://github.com/iree-org/iree/actions/runs/24860364298/job/72785009733) | 67% (2/3) | 2 |
| `Linux,X64,iree-w7900` | self-hosted | 13 | 8 | [9h46m](https://github.com/iree-org/iree/actions/runs/24858194412/job/72780172414) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/24862703064/job/72792565107) | [5m14s](https://github.com/iree-org/iree/actions/runs/24867333949/job/72806909936) | 0% (0/2) | 2 |
| `macos-14` | github-hosted | 60 | 2 | [8h43m](https://github.com/iree-org/iree/actions/runs/24861685535/job/72788483216) | 6 | [3s](https://github.com/iree-org/iree/actions/runs/24873997941/job/72826543876) | [5m07s](https://github.com/iree-org/iree/actions/runs/24861766248/job/72788945891) | 0% (0/17) | 57 |
| `macos-15-intel` | github-hosted | 5 | 0 | — | 4 | [11s](https://github.com/iree-org/iree/actions/runs/24873643813/job/72825431856) | [4m30s](https://github.com/iree-org/iree/actions/runs/24861766248/job/72788945917) | — | 5 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 13 | 2 | [8h11m](https://github.com/iree-org/iree/actions/runs/24861685549/job/72791988728) | 1 | [50s](https://github.com/iree-org/iree/actions/runs/24861766292/job/72791715732) | [4m25s](https://github.com/iree-org/iree/actions/runs/24874178460/job/72833034587) | 0% (0/5) | 3 |
| `azure-windows-scale` | ossci | 18 | 0 | — | 5 | [1s](https://github.com/iree-org/iree/actions/runs/24870706605/job/72816449105) | [3m58s](https://github.com/iree-org/iree/actions/runs/24861766248/job/72788945915) | 0% (0/4) | 17 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 52 | 0 | — | 4 | [8s](https://github.com/iree-org/iree/actions/runs/24867333949/job/72806909943) | [3m39s](https://github.com/iree-org/iree/actions/runs/24862703064/job/72792565215) | 8% (2/24) | 52 |
| `windows-2022` | github-hosted | 56 | 0 | — | 8 | [3s](https://github.com/iree-org/iree/actions/runs/24860904345/job/72785866211) | [3m36s](https://github.com/iree-org/iree/actions/runs/24862703062/job/72791770684) | 6% (1/17) | 56 |
| `ubuntu-24.04-arm` | github-hosted | 57 | 0 | — | 4 | [2s](https://github.com/iree-org/iree/actions/runs/24873997941/job/72826543899) | [3m26s](https://github.com/iree-org/iree/actions/runs/24862703062/job/72791770712) | 0% (0/18) | 57 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 4 | 0 | — | 3 | [2m06s](https://github.com/iree-org/iree/actions/runs/24866704514/job/72804322146) | [2m25s](https://github.com/iree-org/iree/actions/runs/24873643813/job/72825431790) | — | 4 |
| `ubuntu-24.04` | github-hosted | 309 | 0 | — | 20 | [2s](https://github.com/iree-org/iree/actions/runs/24873441423/job/72824763326) | [2m01s](https://github.com/iree-org/iree/actions/runs/24861685535/job/72788483209) | 6% (6/103) | 309 |
| `ubuntu-latest` | github-hosted | 27 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24867466329/job/72806569537) | [1m20s](https://github.com/iree-org/iree/actions/runs/24867333495/job/72806180921) | 0% (0/12) | 27 |
| `azure-linux-scale` | ossci | 106 | 3 | [1h20m](https://github.com/iree-org/iree/actions/runs/24874178459/job/72827158113) | 24 | [8s](https://github.com/iree-org/iree/actions/runs/24861685535/job/72788483308) | [1m12s](https://github.com/iree-org/iree/actions/runs/24870706561/job/72816450677) | 0% (0/29) | 100 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 13 | 0 | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/24866300244/job/72803732671) | [2s](https://github.com/iree-org/iree/actions/runs/24860904417/job/72786810626) | 17% (1/6) | 13 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +2 more | 124 | 0% (0/120) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +7 more | 164 | 16% (25/160) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, +2 more | 151 | 1% (2/147) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, +5 more | 145 | 2% (3/140) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 49 | 0% (0/46) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job waiting 8h11m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 9h46m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 9h46m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 9h46m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 9h46m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 9h46m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 9h46m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 9h46m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 9h46m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job waiting 9h46m (> 2h00m)
- **[stale-queued]** `macos-14` oldest queued job waiting 8h43m (> 2h00m)
- **[stale-queued]** `nodai-amdgpu-mi308-x86-64` oldest queued job waiting 8h06m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 9h46m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job waiting 9h46m (> 2h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
