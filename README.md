# iree-ci-monitor

_Updated: 2026-05-04 11:55 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 17 | 4 | [2h32m](https://github.com/iree-org/iree/actions/runs/25329744694/job/74261551089) | 0 | [32m10s](https://github.com/iree-org/iree/actions/runs/25328682699/job/74258123938) | [1h50m](https://github.com/iree-org/iree/actions/runs/25328884382/job/74258529572) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 34 | 7 | [2h51m](https://github.com/iree-org/iree/actions/runs/25328884382/job/74258527321) | 1 | [11m17s](https://github.com/iree-org/iree/actions/runs/25332338190/job/74270444997) | [1h32m](https://github.com/iree-org/iree/actions/runs/25328682699/job/74258085693) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 17 | 5 | [2h43m](https://github.com/iree-org/iree/actions/runs/25329322746/job/74259711994) | 1 | [11m51s](https://github.com/iree-org/iree/actions/runs/25325119939/job/74245610306) | [1h23m](https://github.com/iree-org/iree/actions/runs/25332950994/job/74272033042) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 17 | 0 | — | 0 | [6m17s](https://github.com/iree-org/iree/actions/runs/25332690900/job/74273124087) | [1h17m](https://github.com/iree-org/iree/actions/runs/25329744694/job/74261550904) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 17 | 0 | — | 0 | [10m20s](https://github.com/iree-org/iree/actions/runs/25329744694/job/74261550796) | [1h14m](https://github.com/iree-org/iree/actions/runs/25328884382/job/74258532374) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 17 | 0 | — | 0 | [3m05s](https://github.com/iree-org/iree/actions/runs/25325119939/job/74245610163) | [1h01m](https://github.com/iree-org/iree/actions/runs/25332690900/job/74273124119) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 17 | 1 | [1h08m](https://github.com/iree-org/iree/actions/runs/25333663639/job/74274843880) | 0 | [14m36s](https://github.com/iree-org/iree/actions/runs/25323753014/job/74241163731) | [1h00m](https://github.com/iree-org/iree/actions/runs/25329744694/job/74261550985) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 34 | 0 | — | 0 | [10m13s](https://github.com/iree-org/iree/actions/runs/25331363304/job/74267052202) | [56m15s](https://github.com/iree-org/iree/actions/runs/25332950994/job/74272032940) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 17 | 0 | — | 0 | [10m12s](https://github.com/iree-org/iree/actions/runs/25329744694/job/74261551005) | [40m36s](https://github.com/iree-org/iree/actions/runs/25333663639/job/74274843967) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 34 | 0 | — | 0 | [9m02s](https://github.com/iree-org/iree/actions/runs/25332690900/job/74273124172) | [24m15s](https://github.com/iree-org/iree/actions/runs/25333663639/job/74274843902) | 17% (1/6) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 17 | 0 | — | 0 | [3m06s](https://github.com/iree-org/iree/actions/runs/25332950994/job/74272033020) | [15m49s](https://github.com/iree-org/iree/actions/runs/25328682699/job/74258085754) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 17 | 0 | — | 0 | [3m01s](https://github.com/iree-org/iree/actions/runs/25331158086/job/74266407410) | [12m17s](https://github.com/iree-org/iree/actions/runs/25329322746/job/74259711961) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 17 | 0 | — | 0 | [25s](https://github.com/iree-org/iree/actions/runs/25332950994/job/74272032925) | [9m57s](https://github.com/iree-org/iree/actions/runs/25329744694/job/74261551107) | 0% (0/3) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 68 | 0 | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/25331158086/job/74266407341) | [3m34s](https://github.com/iree-org/iree/actions/runs/25333663639/job/74274844030) | 25% (3/12) | 68 |
| `windows-2022` | github-hosted | 60 | 0 | — | 6 | [4s](https://github.com/iree-org/iree/actions/runs/25331150353/job/74264938020) | [1m56s](https://github.com/iree-org/iree/actions/runs/25334108804/job/74274882066) | 0% (0/9) | 60 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m46s](https://github.com/iree-org/iree/actions/runs/25312820949/job/74203454593) | [1m46s](https://github.com/iree-org/iree/actions/runs/25312820949/job/74203454593) | 0% (0/1) | 1 |
| `macos-14` | github-hosted | 61 | 0 | — | 3 | [3s](https://github.com/iree-org/iree/actions/runs/25331363297/job/74265653029) | [1m33s](https://github.com/iree-org/iree/actions/runs/25329744724/job/74260089027) | 0% (0/10) | 61 |
| `ubuntu-24.04-arm` | github-hosted | 60 | 0 | — | 3 | [3s](https://github.com/iree-org/iree/actions/runs/25332690934/job/74270076767) | [1m26s](https://github.com/iree-org/iree/actions/runs/25332951041/job/74270973012) | 0% (0/9) | 60 |
| `azure-linux-scale` | ossci | 106 | 0 | — | 10 | [13s](https://github.com/iree-org/iree/actions/runs/25333663654/job/74273400454) | [39s](https://github.com/iree-org/iree/actions/runs/25328682086/job/74256605351) | 0% (0/20) | 106 |
| `ubuntu-24.04` | github-hosted | 357 | 0 | — | 4 | [3s](https://github.com/iree-org/iree/actions/runs/25334108776/job/74274851708) | [10s](https://github.com/iree-org/iree/actions/runs/25330573484/job/74264065914) | 6% (3/52) | 351 |
| `ubuntu-latest` | github-hosted | 26 | 0 | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/25325732192/job/74245929300) | [9s](https://github.com/iree-org/iree/actions/runs/25333662525/job/74273351753) | 0% (0/6) | 26 |
| `azure-windows-scale` | ossci | 20 | 1 | [2m38s](https://github.com/iree-org/iree/actions/runs/25337116026/job/74285368069) | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25328682086/job/74256603270) | [9s](https://github.com/iree-org/iree/actions/runs/25332338118/job/74268915374) | 33% (1/3) | 19 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25312806680/job/74203407681) | [3s](https://github.com/iree-org/iree/actions/runs/25312806680/job/74203407681) | 0% (0/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 17 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25328682699/job/74258085619) | [2s](https://github.com/iree-org/iree/actions/runs/25333663639/job/74274843822) | 100% (3/3) | 17 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 695 | 7% (46/694) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 962 | 3% (25/961) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1115 | 5% (55/1112) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 864 | 2% (13/864) |  | 10m36s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 261 | 2% (5/261) |  | 31m22s ago |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 60 | 12% (7/60) |  | 6d21h ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 2h51m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 2h43m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 2h32m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h14m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h17m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h01m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h23m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 1h50m (> 1h00m)
- **[high-failure-main]** `linux-mi325-1gpu-ossci-iree-org` main-branch failure rate 25% (3/12)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
