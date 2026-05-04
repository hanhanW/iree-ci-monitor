# iree-ci-monitor

_Updated: 2026-05-04 10:36 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 14 | 3 | [1h24m](https://github.com/iree-org/iree/actions/runs/25329322746/job/74259711753) | 0 | [8m33s](https://github.com/iree-org/iree/actions/runs/25331158086/job/74266407023) | [1h14m](https://github.com/iree-org/iree/actions/runs/25328884382/job/74258532374) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 14 | 6 | [1h32m](https://github.com/iree-org/iree/actions/runs/25328884382/job/74258532104) | 0 | [8m02s](https://github.com/iree-org/iree/actions/runs/25323753014/job/74241163772) | [1h09m](https://github.com/iree-org/iree/actions/runs/25328682699/job/74258089582) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 14 | 2 | [42m51s](https://github.com/iree-org/iree/actions/runs/25331158086/job/74266407403) | 0 | [14m35s](https://github.com/iree-org/iree/actions/runs/25322352615/job/74236073400) | [1h00m](https://github.com/iree-org/iree/actions/runs/25329744694/job/74261550985) | 0% (0/2) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 14 | 2 | [17m23s](https://github.com/iree-org/iree/actions/runs/25332338190/job/74270444922) | 0 | [8m40s](https://github.com/iree-org/iree/actions/runs/25322352615/job/74236073195) | [51m22s](https://github.com/iree-org/iree/actions/runs/25329322746/job/74259711930) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 28 | 2 | [7m16s](https://github.com/iree-org/iree/actions/runs/25332950994/job/74272032940) | 1 | [7m20s](https://github.com/iree-org/iree/actions/runs/25322352615/job/74236073248) | [48m49s](https://github.com/iree-org/iree/actions/runs/25329322746/job/74259711936) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 28 | 8 | [1h32m](https://github.com/iree-org/iree/actions/runs/25328884382/job/74258527321) | 1 | [11m17s](https://github.com/iree-org/iree/actions/runs/25332338190/job/74270444997) | [45m24s](https://github.com/iree-org/iree/actions/runs/25329322746/job/74259712006) | 0% (0/5) | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 14 | 6 | [1h32m](https://github.com/iree-org/iree/actions/runs/25328884382/job/74258529572) | 1 | [10m07s](https://github.com/iree-org/iree/actions/runs/25323753014/job/74241163921) | [42m15s](https://github.com/iree-org/iree/actions/runs/25330573484/job/74264066015) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 14 | 4 | [1h13m](https://github.com/iree-org/iree/actions/runs/25329744694/job/74261550904) | 0 | [4m15s](https://github.com/iree-org/iree/actions/runs/25328884382/job/74258576271) | [27m18s](https://github.com/iree-org/iree/actions/runs/25331363304/job/74267051962) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 14 | 3 | [38m53s](https://github.com/iree-org/iree/actions/runs/25331363304/job/74267052150) | 0 | [1m01s](https://github.com/iree-org/iree/actions/runs/25330573484/job/74264065924) | [24m44s](https://github.com/iree-org/iree/actions/runs/25329744694/job/74261550971) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 28 | 0 | — | 1 | [4m20s](https://github.com/iree-org/iree/actions/runs/25325119939/job/74245610235) | [23m14s](https://github.com/iree-org/iree/actions/runs/25331158086/job/74266407084) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 14 | 0 | — | 0 | [3m06s](https://github.com/iree-org/iree/actions/runs/25332950994/job/74272033020) | [15m49s](https://github.com/iree-org/iree/actions/runs/25328682699/job/74258085754) | 0% (0/3) | `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 14 | 1 | [7m15s](https://github.com/iree-org/iree/actions/runs/25332950994/job/74272033094) | 0 | [3m01s](https://github.com/iree-org/iree/actions/runs/25331158086/job/74266407410) | [12m17s](https://github.com/iree-org/iree/actions/runs/25329322746/job/74259711961) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 14 | 0 | — | 1 | [25s](https://github.com/iree-org/iree/actions/runs/25332950994/job/74272032925) | [9m57s](https://github.com/iree-org/iree/actions/runs/25329744694/job/74261551107) | 0% (0/3) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 56 | 0 | — | 1 | [10s](https://github.com/iree-org/iree/actions/runs/25322352615/job/74236073322) | [2m24s](https://github.com/iree-org/iree/actions/runs/25332338190/job/74270444908) | 25% (3/12) | 56 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m46s](https://github.com/iree-org/iree/actions/runs/25312820949/job/74203454593) | [1m46s](https://github.com/iree-org/iree/actions/runs/25312820949/job/74203454593) | 0% (0/1) | 1 |
| `macos-14` | github-hosted | 43 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25330573506/job/74262954707) | [1m33s](https://github.com/iree-org/iree/actions/runs/25329744724/job/74260089027) | 0% (0/7) | 43 |
| `ubuntu-24.04-arm` | github-hosted | 42 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25331363297/job/74265653038) | [1m03s](https://github.com/iree-org/iree/actions/runs/25329322736/job/74258593105) | 0% (0/6) | 42 |
| `windows-2022` | github-hosted | 42 | 0 | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/25328682086/job/74256602242) | [49s](https://github.com/iree-org/iree/actions/runs/25332690934/job/74270076749) | 0% (0/6) | 42 |
| `azure-linux-scale` | ossci | 75 | 0 | — | 9 | [13s](https://github.com/iree-org/iree/actions/runs/25329744724/job/74260089070) | [39s](https://github.com/iree-org/iree/actions/runs/25328884297/job/74257019395) | 0% (0/15) | 75 |
| `ubuntu-24.04` | github-hosted | 272 | 0 | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/25332338190/job/74270445150) | [10s](https://github.com/iree-org/iree/actions/runs/25328279532/job/74254781014) | 8% (4/48) | 266 |
| `ubuntu-latest` | github-hosted | 24 | 0 | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/25325732192/job/74245929300) | [9s](https://github.com/iree-org/iree/actions/runs/25332948202/job/74270924530) | 0% (0/4) | 24 |
| `azure-windows-scale` | ossci | 14 | 0 | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/25328279649/job/74254831565) | [9s](https://github.com/iree-org/iree/actions/runs/25332338118/job/74268915374) | 50% (1/2) | 14 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25312806680/job/74203407681) | [3s](https://github.com/iree-org/iree/actions/runs/25312806680/job/74203407681) | 0% (0/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 14 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25325119939/job/74245610154) | [2s](https://github.com/iree-org/iree/actions/runs/25331158086/job/74266407008) | 100% (3/3) | 14 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 681 | 6% (44/680) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 851 | 2% (13/850) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1100 | 5% (55/1097) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 943 | 3% (24/941) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 258 | 2% (5/257) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 60 | 12% (7/60) |  | 6d20h ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h14m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h09m (> 1h00m)
- **[high-failure-main]** `linux-mi325-1gpu-ossci-iree-org` main-branch failure rate 25% (3/12)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
