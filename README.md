# iree-ci-monitor

_Updated: 2026-04-28 05:58 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 24 | 5 | [8h45m](https://github.com/iree-org/iree/actions/runs/25033295352/job/73319978532) | 1 | [3h36m](https://github.com/iree-org/iree/actions/runs/25036878947/job/73333392682) | [6h25m](https://github.com/iree-org/iree/actions/runs/25032162739/job/73316989188) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 12 | 0 | — | 0 | [3h31m](https://github.com/iree-org/iree/actions/runs/25036878947/job/73333392519) | [6h13m](https://github.com/iree-org/iree/actions/runs/25033295352/job/73319978539) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 12 | 0 | — | 0 | [3h29m](https://github.com/iree-org/iree/actions/runs/25037262481/job/73334325071) | [4h43m](https://github.com/iree-org/iree/actions/runs/25034506099/job/73323661848) | 0% (0/3) | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 12 | 0 | — | 0 | [3h25m](https://github.com/iree-org/iree/actions/runs/25034506099/job/73323661792) | [4h13m](https://github.com/iree-org/iree/actions/runs/25036522879/job/73332604004) | 0% (0/3) | `shark01-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 12 | 0 | — | 0 | [2h14m](https://github.com/iree-org/iree/actions/runs/25034506099/job/73323661799) | [3h38m](https://github.com/iree-org/iree/actions/runs/25037869894/job/73337283859) | 0% (0/3) | `shark01-ci` |
| `Linux,X64,gfx1100` | self-hosted | 24 | 0 | — | 0 | [2h17m](https://github.com/iree-org/iree/actions/runs/25036522879/job/73332604138) | [3h24m](https://github.com/iree-org/iree/actions/runs/25037262481/job/73334325138) | 0% (0/6) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 12 | 0 | — | 0 | [2h12m](https://github.com/iree-org/iree/actions/runs/25031463022/job/73317088684) | [3h12m](https://github.com/iree-org/iree/actions/runs/25037262481/job/73334325141) | 0% (0/3) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 12 | 0 | — | 0 | [2h09m](https://github.com/iree-org/iree/actions/runs/25036522879/job/73332603918) | [3h12m](https://github.com/iree-org/iree/actions/runs/25037262481/job/73334324988) | 0% (0/3) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 36 | 0 | — | 0 | [2h10m](https://github.com/iree-org/iree/actions/runs/25031463022/job/73317088707) | [3h12m](https://github.com/iree-org/iree/actions/runs/25037869894/job/73337283800) | 0% (0/9) | `shark01-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 12 | 0 | — | 0 | [1h56m](https://github.com/iree-org/iree/actions/runs/25031463022/job/73317088679) | [2h32m](https://github.com/iree-org/iree/actions/runs/25036878947/job/73333392539) | 0% (0/3) | `shark01-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 81 | 3 | [1m53s](https://github.com/iree-org/iree/actions/runs/25054099963/job/73389514389) | 3 | [59s](https://github.com/iree-org/iree/actions/runs/25034506085/job/73323106027) | [23m11s](https://github.com/iree-org/iree/actions/runs/25036522889/job/73329401706) | 0% (0/20) | 73 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 12 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25034506099/job/73323661915) | [6m01s](https://github.com/iree-org/iree/actions/runs/25037262481/job/73334325042) | 0% (0/3) | `iree-mi308-1` |
| `windows-2022` | github-hosted | 47 | 0 | — | 3 | [3s](https://github.com/iree-org/iree/actions/runs/25034506085/job/73323105900) | [3m53s](https://github.com/iree-org/iree/actions/runs/25037869922/job/73333682584) | 0% (0/9) | 47 |
| `macos-14` | github-hosted | 48 | 0 | — | 4 | [4s](https://github.com/iree-org/iree/actions/runs/25046436311/job/73362627042) | [3m38s](https://github.com/iree-org/iree/actions/runs/25036878943/job/73330640407) | 0% (0/9) | 48 |
| `ubuntu-24.04-arm` | github-hosted | 48 | 0 | — | 3 | [2s](https://github.com/iree-org/iree/actions/runs/25036522889/job/73329401541) | [2m09s](https://github.com/iree-org/iree/actions/runs/25036878943/job/73330640410) | 0% (0/9) | 48 |
| `ubuntu-24.04` | github-hosted | 243 | 0 | — | 7 | [2s](https://github.com/iree-org/iree/actions/runs/25037262407/job/73331723566) | [1m46s](https://github.com/iree-org/iree/actions/runs/25033514284/job/73320093409) | 0% (0/53) | 243 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m41s](https://github.com/iree-org/iree/actions/runs/25046449719/job/73362674548) | [1m41s](https://github.com/iree-org/iree/actions/runs/25046449719/job/73362674548) | 0% (0/1) | 1 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 48 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25034982190/job/73325359521) | [1m18s](https://github.com/iree-org/iree/actions/runs/25031463022/job/73317088579) | 8% (1/12) | 48 |
| `ubuntu-latest` | github-hosted | 40 | 0 | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/25037261513/job/73331723583) | [4s](https://github.com/iree-org/iree/actions/runs/25054098634/job/73389478775) | 0% (0/6) | 40 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25046431930/job/73362613190) | [3s](https://github.com/iree-org/iree/actions/runs/25046431930/job/73362613190) | — | 1 |
| `azure-windows-scale` | ossci | 15 | 0 | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/25036362687/job/73328917648) | [2s](https://github.com/iree-org/iree/actions/runs/25054099963/job/73389514564) | 0% (0/3) | 15 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 12 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25037869894/job/73337283814) | [2s](https://github.com/iree-org/iree/actions/runs/25036522879/job/73332603960) | 0% (0/3) | 12 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 12 | 9 | [9h22m](https://github.com/iree-org/iree/actions/runs/25032162739/job/73316989167) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/25033911199/job/73321957973) | [0s](https://github.com/iree-org/iree/actions/runs/25034982190/job/73325359496) | — | 0 |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 12 | 9 | [9h22m](https://github.com/iree-org/iree/actions/runs/25032162739/job/73316989223) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/25033911199/job/73321958036) | [0s](https://github.com/iree-org/iree/actions/runs/25034982190/job/73325359539) | — | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 558 | 2% (10/553) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 490 | 3% (14/485) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 463 | 1% (6/459) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 160 | 1% (1/157) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 466 | 14% (63/462) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 8h45m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 9h22m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 9h22m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 2h32m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 3h24m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 6h13m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 6h25m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 3h12m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 3h38m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 4h43m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 3h12m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 4h13m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 3h12m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
