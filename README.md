# iree-ci-monitor

_Updated: 2026-04-30 05:53 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 14 | 1 | [30m41s](https://github.com/iree-org/iree/actions/runs/25164786901/job/73769126652) | 0 | [19m09s](https://github.com/iree-org/iree/actions/runs/25159192665/job/73749942716) | [2h22m](https://github.com/iree-org/iree/actions/runs/25155043255/job/73735813988) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 28 | 2 | [16m35s](https://github.com/iree-org/iree/actions/runs/25165319046/job/73771258760) | 0 | [31m08s](https://github.com/iree-org/iree/actions/runs/25150066715/job/73722186160) | [2h15m](https://github.com/iree-org/iree/actions/runs/25156231698/job/73739880116) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 14 | 1 | [16m35s](https://github.com/iree-org/iree/actions/runs/25165319046/job/73771258386) | 0 | [36m04s](https://github.com/iree-org/iree/actions/runs/25156045059/job/73739181852) | [1h28m](https://github.com/iree-org/iree/actions/runs/25155043255/job/73735813706) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 14 | 0 | — | 0 | [27m48s](https://github.com/iree-org/iree/actions/runs/25159192665/job/73749942714) | [1h25m](https://github.com/iree-org/iree/actions/runs/25155043255/job/73735813973) | 0% (0/3) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 14 | 2 | [30m41s](https://github.com/iree-org/iree/actions/runs/25164786901/job/73769126730) | 0 | [8m05s](https://github.com/iree-org/iree/actions/runs/25159192665/job/73749942691) | [1h21m](https://github.com/iree-org/iree/actions/runs/25157955608/job/73745682979) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 14 | 2 | [30m41s](https://github.com/iree-org/iree/actions/runs/25164786901/job/73769126567) | 0 | [11m06s](https://github.com/iree-org/iree/actions/runs/25150066715/job/73722186047) | [1h18m](https://github.com/iree-org/iree/actions/runs/25156231698/job/73739879875) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 28 | 1 | [16m35s](https://github.com/iree-org/iree/actions/runs/25165319046/job/73771258634) | 1 | [15m32s](https://github.com/iree-org/iree/actions/runs/25165319046/job/73771258666) | [1h08m](https://github.com/iree-org/iree/actions/runs/25156231698/job/73739880153) | 0% (0/6) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 42 | 2 | [16m35s](https://github.com/iree-org/iree/actions/runs/25165319046/job/73771258456) | 1 | [15m13s](https://github.com/iree-org/iree/actions/runs/25149748717/job/73719652752) | [56m40s](https://github.com/iree-org/iree/actions/runs/25156045059/job/73739181931) | 0% (0/9) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 14 | 0 | — | 1 | [12m01s](https://github.com/iree-org/iree/actions/runs/25148831047/job/73715160612) | [35m01s](https://github.com/iree-org/iree/actions/runs/25155043255/job/73735813850) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 14 | 0 | — | 1 | [12m35s](https://github.com/iree-org/iree/actions/runs/25165319046/job/73771258472) | [31m55s](https://github.com/iree-org/iree/actions/runs/25148831047/job/73715160574) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 14 | 1 | [16m35s](https://github.com/iree-org/iree/actions/runs/25165319046/job/73771258774) | 0 | [10m02s](https://github.com/iree-org/iree/actions/runs/25156231698/job/73739880098) | [25m18s](https://github.com/iree-org/iree/actions/runs/25163103598/job/73763398035) | 0% (0/3) | `shark75-ci` |
| `azure-linux-scale` | ossci | 91 | 0 | — | 7 | [12s](https://github.com/iree-org/iree/actions/runs/25164786910/job/73768443099) | [15m08s](https://github.com/iree-org/iree/actions/runs/25149748717/job/73717423715) | 0% (0/20) | 91 |
| `Linux,X64,rdna3` | self-hosted | 14 | 0 | — | 0 | [6m55s](https://github.com/iree-org/iree/actions/runs/25164786901/job/73769126840) | [13m37s](https://github.com/iree-org/iree/actions/runs/25157955608/job/73745682987) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 14 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25157955608/job/73745682795) | [5m36s](https://github.com/iree-org/iree/actions/runs/25155043255/job/73735813797) | 0% (0/3) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 17 | 0 | — | 2 | [1s](https://github.com/iree-org/iree/actions/runs/25163103588/job/73762333091) | [3m51s](https://github.com/iree-org/iree/actions/runs/25156045056/job/73738059809) | 0% (0/3) | 16 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [2m16s](https://github.com/iree-org/iree/actions/runs/25159142459/job/73748652065) | [2m16s](https://github.com/iree-org/iree/actions/runs/25159142459/job/73748652065) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 54 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25154866354/job/73734055638) | [1m34s](https://github.com/iree-org/iree/actions/runs/25165319052/job/73769844059) | 0% (0/9) | 52 |
| `macos-14` | github-hosted | 54 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25157955569/job/73744621901) | [1m31s](https://github.com/iree-org/iree/actions/runs/25159192646/job/73749031942) | 0% (0/9) | 53 |
| `windows-2022` | github-hosted | 53 | 0 | — | 3 | [3s](https://github.com/iree-org/iree/actions/runs/25159192646/job/73749031934) | [1m25s](https://github.com/iree-org/iree/actions/runs/25156231638/job/73738800582) | 0% (0/9) | 53 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 56 | 0 | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/25155043255/job/73735813890) | [1m17s](https://github.com/iree-org/iree/actions/runs/25155043255/job/73735813861) | 0% (0/12) | 56 |
| `ubuntu-latest` | github-hosted | 22 | 0 | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/25149748003/job/73717404377) | [42s](https://github.com/iree-org/iree/actions/runs/25155280403/job/73735419687) | 0% (0/6) | 22 |
| `ubuntu-24.04` | github-hosted | 302 | 0 | — | 2 | [4s](https://github.com/iree-org/iree/actions/runs/25149748717/job/73719652606) | [10s](https://github.com/iree-org/iree/actions/runs/25163103588/job/73762333053) | 5% (3/57) | 300 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/25159119485/job/73748571224) | [4s](https://github.com/iree-org/iree/actions/runs/25159119485/job/73748571224) | — | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 14 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25156231698/job/73739879872) | [2s](https://github.com/iree-org/iree/actions/runs/25165319046/job/73771258357) | 33% (1/3) | 14 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 830 | 1% (10/825) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 295 | 7% (20/294) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 897 | 3% (26/890) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 262 | 2% (4/259) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1011 | 5% (54/1006) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 459 | 14% (62/455) | yes | running |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h08m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h15m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h18m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h28m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 2h22m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 1h25m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h21m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
