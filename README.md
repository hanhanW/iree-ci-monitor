# iree-ci-monitor

_Updated: 2026-05-01 11:42 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 21 | 14 | [3h29m](https://github.com/iree-org/iree/actions/runs/25219461262/job/73948748152) | 0 | [1h02m](https://github.com/iree-org/iree/actions/runs/25218004726/job/73943911837) | [3h25m](https://github.com/iree-org/iree/actions/runs/25218447012/job/73945460616) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 21 | 8 | [2h49m](https://github.com/iree-org/iree/actions/runs/25220983125/job/73953960242) | 0 | [1h00m](https://github.com/iree-org/iree/actions/runs/25222174334/job/73958116141) | [3h07m](https://github.com/iree-org/iree/actions/runs/25219461262/job/73948747907) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 21 | 10 | [3h23m](https://github.com/iree-org/iree/actions/runs/25219713733/job/73949635506) | 0 | [1h22m](https://github.com/iree-org/iree/actions/runs/25220729478/job/73953067899) | [3h04m](https://github.com/iree-org/iree/actions/runs/25219461262/job/73948748069) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 42 | 23 | [3h56m](https://github.com/iree-org/iree/actions/runs/25218447012/job/73945460646) | 0 | [1h15m](https://github.com/iree-org/iree/actions/runs/25219918076/job/73950951612) | [3h03m](https://github.com/iree-org/iree/actions/runs/25218447012/job/73945460573) | 0% (0/3) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 42 | 8 | [2h49m](https://github.com/iree-org/iree/actions/runs/25220983125/job/73953960254) | 1 | [1h06m](https://github.com/iree-org/iree/actions/runs/25223228674/job/73962225010) | [2h50m](https://github.com/iree-org/iree/actions/runs/25219713733/job/73949635480) | 0% (0/12) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 42 | 1 | [1h01m](https://github.com/iree-org/iree/actions/runs/25225063841/job/73967595303) | 1 | [1h18m](https://github.com/iree-org/iree/actions/runs/25222502218/job/73960658274) | [2h22m](https://github.com/iree-org/iree/actions/runs/25219012438/job/73948755210) | 0% (0/16) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 21 | 6 | [2h32m](https://github.com/iree-org/iree/actions/runs/25221679391/job/73956141618) | 0 | [1h08m](https://github.com/iree-org/iree/actions/runs/25220983125/job/73953960313) | [2h11m](https://github.com/iree-org/iree/actions/runs/25219461262/job/73948748071) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 21 | 8 | [3h29m](https://github.com/iree-org/iree/actions/runs/25219461262/job/73948748089) | 0 | [1h16m](https://github.com/iree-org/iree/actions/runs/25219012438/job/73948755176) | [2h10m](https://github.com/iree-org/iree/actions/runs/25219713733/job/73949635373) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 21 | 9 | [3h29m](https://github.com/iree-org/iree/actions/runs/25219461262/job/73948747922) | 1 | [44m40s](https://github.com/iree-org/iree/actions/runs/25219574262/job/73949207946) | [1h53m](https://github.com/iree-org/iree/actions/runs/25218447012/job/73945460314) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 21 | 0 | — | 1 | [39m01s](https://github.com/iree-org/iree/actions/runs/25225063841/job/73967595277) | [1h36m](https://github.com/iree-org/iree/actions/runs/25222154447/job/73957861096) | 0% (0/9) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 21 | 1 | [1h01m](https://github.com/iree-org/iree/actions/runs/25225063841/job/73967595325) | 0 | [45m41s](https://github.com/iree-org/iree/actions/runs/25223228674/job/73962225071) | [1h22m](https://github.com/iree-org/iree/actions/runs/25223791601/job/73963630232) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 21 | 0 | — | 0 | [38m09s](https://github.com/iree-org/iree/actions/runs/25222154447/job/73957861173) | [1h06m](https://github.com/iree-org/iree/actions/runs/25220478946/job/73952149373) | 0% (0/9) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 21 | 0 | — | 0 | [15m33s](https://github.com/iree-org/iree/actions/runs/25225209635/job/73968256014) | [45m33s](https://github.com/iree-org/iree/actions/runs/25219012438/job/73948755167) | 0% (0/9) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 84 | 0 | — | 0 | [19s](https://github.com/iree-org/iree/actions/runs/25217658538/job/73943032110) | [7m09s](https://github.com/iree-org/iree/actions/runs/25219574262/job/73949208153) | 8% (3/36) | 84 |
| `ubuntu-24.04` | github-hosted | 394 | 0 | — | 1 | [7s](https://github.com/iree-org/iree/actions/runs/25222154447/job/73957861027) | [2m55s](https://github.com/iree-org/iree/actions/runs/25219012438/job/73948755182) | 1% (1/157) | 394 |
| `windows-2022` | github-hosted | 69 | 0 | — | 3 | [6s](https://github.com/iree-org/iree/actions/runs/25219012407/job/73946316898) | [2m23s](https://github.com/iree-org/iree/actions/runs/25219918057/job/73949658349) | 0% (0/27) | 69 |
| `ubuntu-24.04-arm` | github-hosted | 69 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25219574256/job/73948202188) | [2m16s](https://github.com/iree-org/iree/actions/runs/25222502488/job/73957968741) | 0% (0/30) | 69 |
| `macos-14` | github-hosted | 70 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25227359246/job/73974143617) | [2m10s](https://github.com/iree-org/iree/actions/runs/25220502760/job/73951535010) | 0% (0/31) | 68 |
| `azure-windows-scale` | ossci | 23 | 0 | — | 2 | [1s](https://github.com/iree-org/iree/actions/runs/25222502488/job/73957968982) | [2m07s](https://github.com/iree-org/iree/actions/runs/25220729477/job/73952252488) | 0% (0/9) | 23 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m44s](https://github.com/iree-org/iree/actions/runs/25210238746/job/73919140136) | [1m44s](https://github.com/iree-org/iree/actions/runs/25210238746/job/73919140136) | 0% (0/1) | 1 |
| `ubuntu-latest` | github-hosted | 57 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25212905391/job/73927072214) | [1m01s](https://github.com/iree-org/iree/actions/runs/25219916151/job/73949308601) | 0% (0/20) | 57 |
| `azure-linux-scale` | ossci | 129 | 0 | — | 4 | [10s](https://github.com/iree-org/iree/actions/runs/25220983132/job/73952883031) | [58s](https://github.com/iree-org/iree/actions/runs/25219574262/job/73948206988) | 0% (0/59) | 125 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25210218261/job/73919079681) | [2s](https://github.com/iree-org/iree/actions/runs/25210218261/job/73919079681) | 0% (0/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 21 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25218429597/job/73945130609) | [2s](https://github.com/iree-org/iree/actions/runs/25225209635/job/73968255999) | 11% (1/9) | 21 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 540 | 6% (34/539) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1180 | 5% (58/1176) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 1020 | 3% (27/1016) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 953 | 1% (11/951) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 296 | 2% (5/295) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 323 | 13% (42/321) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 2h32m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 3h56m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 2h49m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 3h29m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 3h29m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 3h23m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 3h29m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job waiting 2h49m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h22m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h11m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 3h03m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 3h07m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h53m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 2h10m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 3h04m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 3h25m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h22m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h36m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h50m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
