# iree-ci-monitor

_Updated: 2026-05-01 23:59 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 8 | 0 | — | 0 | [12m54s](https://github.com/iree-org/iree/actions/runs/25237508696/job/74007461147) | [3h23m](https://github.com/iree-org/iree/actions/runs/25234638883/job/73998842539) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 4 | 0 | — | 0 | [33m17s](https://github.com/iree-org/iree/actions/runs/25237508696/job/74007461104) | [2h52m](https://github.com/iree-org/iree/actions/runs/25234638883/job/73998842596) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 4 | 0 | — | 0 | [19m52s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989378) | [1h15m](https://github.com/iree-org/iree/actions/runs/25234638883/job/73998842550) | 50% (1/2) | `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 4 | 0 | — | 0 | [25m17s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989402) | [1h13m](https://github.com/iree-org/iree/actions/runs/25234638883/job/73998842597) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 4 | 0 | — | 0 | [8m05s](https://github.com/iree-org/iree/actions/runs/25237508696/job/74007461043) | [54m04s](https://github.com/iree-org/iree/actions/runs/25234638883/job/73998842404) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 8 | 0 | — | 0 | [6m25s](https://github.com/iree-org/iree/actions/runs/25234638883/job/73998842537) | [19m52s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989392) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 8 | 0 | — | 0 | [4m45s](https://github.com/iree-org/iree/actions/runs/25237508696/job/74007461108) | [14m31s](https://github.com/iree-org/iree/actions/runs/25234638883/job/73998842599) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 4 | 0 | — | 0 | [8m22s](https://github.com/iree-org/iree/actions/runs/25234638883/job/73998842507) | [14m25s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989522) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 4 | 0 | — | 0 | [9m14s](https://github.com/iree-org/iree/actions/runs/25237508696/job/74007461110) | [11m10s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989397) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | 0 | [9m04s](https://github.com/iree-org/iree/actions/runs/25234638883/job/73998842551) | [10m58s](https://github.com/iree-org/iree/actions/runs/25237508696/job/74007461133) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 4 | 0 | — | 0 | [1m36s](https://github.com/iree-org/iree/actions/runs/25234638883/job/73998842508) | [5m32s](https://github.com/iree-org/iree/actions/runs/25237508696/job/74007461075) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `azure-linux-scale` | ossci | 22 | 0 | — | 0 | [11s](https://github.com/iree-org/iree/actions/runs/25234638886/job/73998007142) | [36s](https://github.com/iree-org/iree/actions/runs/25235327560/job/74000154117) | 0% (0/12) | 22 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989405) | [19s](https://github.com/iree-org/iree/actions/runs/25237508696/job/74007461079) | 25% (2/8) | 16 |
| `ubuntu-24.04` | github-hosted | 95 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25237508709/job/74006743753) | [8s](https://github.com/iree-org/iree/actions/runs/25237508709/job/74006722424) | 7% (3/45) | 95 |
| `windows-2022` | github-hosted | 14 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25235327560/job/74000154019) | [5s](https://github.com/iree-org/iree/actions/runs/25237508709/job/74006743684) | 0% (0/6) | 14 |
| `macos-14` | github-hosted | 14 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25237508709/job/74006743673) | [3s](https://github.com/iree-org/iree/actions/runs/25243903940/job/74024588132) | 0% (0/6) | 14 |
| `ubuntu-24.04-arm` | github-hosted | 15 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25243903940/job/74024588172) | [3s](https://github.com/iree-org/iree/actions/runs/25243903940/job/74024588139) | 0% (0/6) | 15 |
| `ubuntu-latest` | github-hosted | 11 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25243903653/job/74024578930) | [3s](https://github.com/iree-org/iree/actions/runs/25234822818/job/73998560924) | 0% (0/4) | 11 |
| `Linux,X64,iree-w7900` | self-hosted | 4 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989347) | [2s](https://github.com/iree-org/iree/actions/runs/25237508696/job/74007461050) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989330) | [2s](https://github.com/iree-org/iree/actions/runs/25237508696/job/74007461071) | 0% (0/2) | 4 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 4 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25243903937/job/74024989393) | [2s](https://github.com/iree-org/iree/actions/runs/25237508696/job/74007461084) | 0% (0/2) | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 4 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25235327560/job/74000154182) | [1s](https://github.com/iree-org/iree/actions/runs/25237508709/job/74006743809) | 0% (0/2) | 4 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1044 | 5% (56/1043) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 905 | 3% (28/904) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 822 | 1% (11/822) |  | 1h41m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 610 | 6% (38/610) |  | 1h41m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 245 | 2% (5/245) |  | 2h01m ago |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 94 | 14% (13/94) |  | 4d09h ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 2h52m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 3h23m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h13m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 1h15m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
