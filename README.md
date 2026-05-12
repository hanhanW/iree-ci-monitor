# iree-ci-monitor

_Updated: 2026-05-11 18:12 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 78 | 25 | [8h01m](https://github.com/iree-org/iree/actions/runs/25684915768/job/75407346143) | 1 | [19m18s](https://github.com/iree-org/iree/actions/runs/25682694876/job/75400084493) | [3h48m](https://github.com/iree-org/iree/actions/runs/25692451768/job/75433260104) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 39 | 10 | [5h36m](https://github.com/iree-org/iree/actions/runs/25692451768/job/75433260122) | 1 | [4m42s](https://github.com/iree-org/iree/actions/runs/25680866201/job/75393915291) | [3h29m](https://github.com/iree-org/iree/actions/runs/25698299550/job/75453351357) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 39 | 2 | [2h36m](https://github.com/iree-org/iree/actions/runs/25700159906/job/75462058957) | 0 | [8m52s](https://github.com/iree-org/iree/actions/runs/25692451768/job/75433260102) | [3h14m](https://github.com/iree-org/iree/actions/runs/25696910931/job/75448966372) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 39 | 10 | [4h05m](https://github.com/iree-org/iree/actions/runs/25696910931/job/75448966451) | 0 | [17m39s](https://github.com/iree-org/iree/actions/runs/25690896533/job/75428077387) | [3h08m](https://github.com/iree-org/iree/actions/runs/25693984229/job/75438794025) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 39 | 8 | [5h36m](https://github.com/iree-org/iree/actions/runs/25692451768/job/75433260133) | 0 | [26m46s](https://github.com/iree-org/iree/actions/runs/25682694876/job/75400084313) | [3h02m](https://github.com/iree-org/iree/actions/runs/25696111638/job/75446466321) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 36 | 18 | [9h12m](https://github.com/iree-org/iree/actions/runs/25680866201/job/75393915357) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/25704767504/job/75473330601) | [2h40m](https://github.com/iree-org/iree/actions/runs/25690896533/job/75428077399) | — | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 39 | 4 | [5h04m](https://github.com/iree-org/iree/actions/runs/25693984229/job/75438794109) | 0 | [15m16s](https://github.com/iree-org/iree/actions/runs/25705717803/job/75476265078) | [2h29m](https://github.com/iree-org/iree/actions/runs/25697051993/job/75449184060) | 33% (1/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 78 | 1 | [30m20s](https://github.com/iree-org/iree/actions/runs/25705717803/job/75476265403) | 1 | [23m38s](https://github.com/iree-org/iree/actions/runs/25684915768/job/75407346160) | [2h15m](https://github.com/iree-org/iree/actions/runs/25692702297/job/75437590345) | 0% (0/12) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 39 | 1 | [30m20s](https://github.com/iree-org/iree/actions/runs/25705717803/job/75476265189) | 1 | [39m07s](https://github.com/iree-org/iree/actions/runs/25696910931/job/75448966388) | [2h02m](https://github.com/iree-org/iree/actions/runs/25682993130/job/75404013715) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,rdna3,shark01-ci` | self-hosted | 1 | 0 | — | 0 | [1h41m](https://github.com/iree-org/iree/actions/runs/25687967528/job/75417907634) | [1h41m](https://github.com/iree-org/iree/actions/runs/25687967528/job/75417907634) | — | `shark01-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 39 | 0 | — | 0 | [20m41s](https://github.com/iree-org/iree/actions/runs/25687840553/job/75417642841) | [1h19m](https://github.com/iree-org/iree/actions/runs/25697051993/job/75449184408) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 78 | 0 | — | 0 | [21m47s](https://github.com/iree-org/iree/actions/runs/25680865848/job/75393910513) | [1h18m](https://github.com/iree-org/iree/actions/runs/25700017452/job/75459332775) | 0% (0/12) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3,shark55-ci` | self-hosted | 1 | 0 | — | 0 | [1h11m](https://github.com/iree-org/iree/actions/runs/25694027929/job/75439462550) | [1h11m](https://github.com/iree-org/iree/actions/runs/25694027929/job/75439462550) | — | `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 38 | 0 | — | 1 | [13m07s](https://github.com/iree-org/iree/actions/runs/25684915768/job/75407346363) | [57m25s](https://github.com/iree-org/iree/actions/runs/25700017452/job/75459332782) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,iree-w7900` | self-hosted | 2 | 0 | — | 0 | [33m51s](https://github.com/iree-org/iree/actions/runs/25699916098/job/75458484868) | [54m04s](https://github.com/iree-org/iree/actions/runs/25699916098/job/75458484933) | — | `shark01-ci`, `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 39 | 0 | — | 0 | [2m44s](https://github.com/iree-org/iree/actions/runs/25698886106/job/75455209209) | [17m55s](https://github.com/iree-org/iree/actions/runs/25696910931/job/75448966466) | 0% (0/6) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 156 | 0 | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/25696051946/job/75445936073) | [7m45s](https://github.com/iree-org/iree/actions/runs/25687967528/job/75417907363) | 0% (0/24) | 151 |
| `ubuntu-24.04` | github-hosted | 702 | 0 | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/25678715582/job/75385464633) | [2m30s](https://github.com/iree-org/iree/actions/runs/25680866492/job/75391722322) | 0% (0/97) | 692 |
| `azure-linux-scale` | ossci | 193 | 0 | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/25687967545/job/75416585527) | [2m10s](https://github.com/iree-org/iree/actions/runs/25700159898/job/75458228732) | 0% (0/37) | 192 |
| `ubuntu-24.04-arm` | github-hosted | 108 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25699916077/job/75457645982) | [1m52s](https://github.com/iree-org/iree/actions/runs/25680866492/job/75391722348) | 0% (0/18) | 108 |
| `macos-14` | github-hosted | 108 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25698299540/job/75452159745) | [1m48s](https://github.com/iree-org/iree/actions/runs/25680866492/job/75391722253) | 0% (0/18) | 108 |
| `azure-windows-scale` | ossci | 36 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25699916077/job/75457646102) | [1m39s](https://github.com/iree-org/iree/actions/runs/25680866492/job/75391722548) | 0% (0/6) | 36 |
| `windows-2022` | github-hosted | 108 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25698299540/job/75452159690) | [1m36s](https://github.com/iree-org/iree/actions/runs/25702501866/job/75465526782) | 0% (0/18) | 108 |
| `ubuntu-latest` | github-hosted | 58 | 0 | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/25693982592/job/75437369071) | [15s](https://github.com/iree-org/iree/actions/runs/25694025830/job/75437517802) | 0% (0/12) | 58 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 39 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25674889092/job/75394469513) | [7s](https://github.com/iree-org/iree/actions/runs/25699916098/job/75458484759) | 67% (4/6) | 39 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 984 | 5% (47/981) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 927 | 9% (79/923) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,shark55-ci`, `self-hosted,persistent-cache,Linux,X64` | 691 | 2% (11/688) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,shark01-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 787 | 3% (22/784) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 263 | 3% (7/262) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 8h01m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 4h05m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900` oldest queued job waiting 5h04m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 2h36m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 5h36m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 9h12m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 5h36m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h19m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h15m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 3h48m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 3h08m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h29m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 3h14m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 3h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark01-ci` p95 queue 1h41m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 2h40m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark55-ci` p95 queue 1h11m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 3h29m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h18m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark01-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark55-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
