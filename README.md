# iree-ci-monitor

_Updated: 2026-04-30 11:50 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 32 | 9 | [3h48m](https://github.com/iree-org/iree/actions/runs/25172324279/job/73796687317) | 0 | [9m49s](https://github.com/iree-org/iree/actions/runs/25165319046/job/73771258716) | [2h25m](https://github.com/iree-org/iree/actions/runs/25174768699/job/73803734702) | — | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 61 | 15 | [2h12m](https://github.com/iree-org/iree/actions/runs/25177015220/job/73813311700) | 0 | [39m33s](https://github.com/iree-org/iree/actions/runs/25177015220/job/73813311538) | [2h06m](https://github.com/iree-org/iree/actions/runs/25172324279/job/73796687391) | — | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 32 | 5 | [6h27m](https://github.com/iree-org/iree/actions/runs/25164786901/job/73769126730) | 0 | [31m47s](https://github.com/iree-org/iree/actions/runs/25166070100/job/73773717611) | [2h01m](https://github.com/iree-org/iree/actions/runs/25172324279/job/73796687318) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 29 | 5 | [2h12m](https://github.com/iree-org/iree/actions/runs/25177015220/job/73813311327) | 0 | [19m34s](https://github.com/iree-org/iree/actions/runs/25163103598/job/73763397946) | [1h33m](https://github.com/iree-org/iree/actions/runs/25173730132/job/73801366668) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 29 | 12 | [6h27m](https://github.com/iree-org/iree/actions/runs/25164786901/job/73769126652) | 0 | [16m57s](https://github.com/iree-org/iree/actions/runs/25172290730/job/73796264660) | [1h19m](https://github.com/iree-org/iree/actions/runs/25157955608/job/73745682985) | — | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 29 | 5 | [6h27m](https://github.com/iree-org/iree/actions/runs/25164786901/job/73769126567) | 1 | [16m45s](https://github.com/iree-org/iree/actions/runs/25159192665/job/73749942516) | [1h18m](https://github.com/iree-org/iree/actions/runs/25156231698/job/73739879875) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 29 | 1 | [42m24s](https://github.com/iree-org/iree/actions/runs/25181157670/job/73827605010) | 0 | [25m05s](https://github.com/iree-org/iree/actions/runs/25157955608/job/73745682982) | [1h12m](https://github.com/iree-org/iree/actions/runs/25170973764/job/73794266364) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 29 | 2 | [26m29s](https://github.com/iree-org/iree/actions/runs/25181924016/job/73830081746) | 0 | [16m41s](https://github.com/iree-org/iree/actions/runs/25166070100/job/73773717417) | [1h05m](https://github.com/iree-org/iree/actions/runs/25157955608/job/73745682831) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 86 | 10 | [44m27s](https://github.com/iree-org/iree/actions/runs/25180977027/job/73827280122) | 1 | [18m36s](https://github.com/iree-org/iree/actions/runs/25165319046/job/73771258690) | [56m40s](https://github.com/iree-org/iree/actions/runs/25156045059/job/73739181931) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 61 | 6 | [56m29s](https://github.com/iree-org/iree/actions/runs/25180529120/job/73825353122) | 2 | [11m58s](https://github.com/iree-org/iree/actions/runs/25166070100/job/73773717694) | [54m05s](https://github.com/iree-org/iree/actions/runs/25180529120/job/73825353116) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 29 | 2 | [32m24s](https://github.com/iree-org/iree/actions/runs/25181554794/job/73829168061) | 1 | [7m15s](https://github.com/iree-org/iree/actions/runs/25175016945/job/73805735253) | [37m04s](https://github.com/iree-org/iree/actions/runs/25172324279/job/73796687251) | — | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 29 | 0 | — | 0 | [4m53s](https://github.com/iree-org/iree/actions/runs/25172324279/job/73796687406) | [20m16s](https://github.com/iree-org/iree/actions/runs/25178803390/job/73819498207) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 29 | 1 | [26m29s](https://github.com/iree-org/iree/actions/runs/25181924016/job/73830081755) | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25177015220/job/73813311428) | [12m56s](https://github.com/iree-org/iree/actions/runs/25181157670/job/73827605197) | — | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 122 | 0 | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/25170867546/job/73789598218) | [3m06s](https://github.com/iree-org/iree/actions/runs/25166070100/job/73773717610) | 25% (2/8) | 119 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [2m16s](https://github.com/iree-org/iree/actions/runs/25159142459/job/73748652065) | [2m16s](https://github.com/iree-org/iree/actions/runs/25159142459/job/73748652065) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 148 | 0 | — | 2 | [11s](https://github.com/iree-org/iree/actions/runs/25178803397/job/73818197224) | [2m01s](https://github.com/iree-org/iree/actions/runs/25165319046/job/73769846379) | 0% (0/13) | 147 |
| `macos-14` | github-hosted | 85 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25181554771/job/73827857066) | [1m34s](https://github.com/iree-org/iree/actions/runs/25163103588/job/73762333052) | 0% (0/7) | 85 |
| `ubuntu-24.04-arm` | github-hosted | 84 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25178269948/job/73816645716) | [1m34s](https://github.com/iree-org/iree/actions/runs/25182050931/job/73829560016) | 0% (0/6) | 84 |
| `windows-2022` | github-hosted | 84 | 0 | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/25181157675/job/73826513638) | [1m25s](https://github.com/iree-org/iree/actions/runs/25181554771/job/73827857013) | 0% (0/6) | 84 |
| `ubuntu-latest` | github-hosted | 29 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25181923131/job/73829088853) | [1m11s](https://github.com/iree-org/iree/actions/runs/25172320294/job/73794879735) | 0% (0/4) | 29 |
| `azure-windows-scale` | ossci | 28 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25173730114/job/73800339501) | [52s](https://github.com/iree-org/iree/actions/runs/25178269948/job/73816645834) | 0% (0/2) | 28 |
| `ubuntu-24.04` | github-hosted | 507 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25159192665/job/73749942585) | [48s](https://github.com/iree-org/iree/actions/runs/25181554794/job/73829168107) | 3% (1/34) | 496 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 29 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25172290730/job/73796264294) | [10s](https://github.com/iree-org/iree/actions/runs/25173730132/job/73801366463) | 0% (0/2) | 28 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/25159119485/job/73748571224) | [4s](https://github.com/iree-org/iree/actions/runs/25159119485/job/73748571224) | 0% (0/1) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 889 | 1% (10/884) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 959 | 3% (26/952) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1084 | 5% (54/1078) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 345 | 7% (24/344) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 282 | 1% (4/278) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 459 | 14% (62/455) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 2h12m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 6h27m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 2h12m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 6h27m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 3h48m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 6h27m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h12m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h06m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h18m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h05m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 1h33m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h19m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 2h25m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 2h01m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
