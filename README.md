# iree-ci-monitor

_Updated: 2026-04-27 05:52 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 12 | 1 | [15m35s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954068) | 1 | [10m59s](https://github.com/iree-org/iree/actions/runs/24982797665/job/73149528880) | [46m44s](https://github.com/iree-org/iree/actions/runs/24982244020/job/73147828069) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 6 | 1 | [15m35s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954043) | 0 | [24m46s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696285) | [34m22s](https://github.com/iree-org/iree/actions/runs/24982244020/job/73147827981) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 6 | 1 | [15m35s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954081) | 0 | [14m29s](https://github.com/iree-org/iree/actions/runs/24982244020/job/73147827982) | [31m47s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696508) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 6 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193521) | [24m57s](https://github.com/iree-org/iree/actions/runs/24982797665/job/73149528780) | 0% (0/2) | `shark01-ci`, `shark10-ci-2` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 6 | 1 | [15m35s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954193) | 0 | [8m46s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193619) | [23m48s](https://github.com/iree-org/iree/actions/runs/24982797665/job/73149528837) | 0% (0/2) | `shark10-ci-2` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 6 | 1 | [15m35s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954027) | 0 | [10m17s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696569) | [19m40s](https://github.com/iree-org/iree/actions/runs/24982797665/job/73149528843) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 6 | 1 | [15m35s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954273) | 0 | [5m44s](https://github.com/iree-org/iree/actions/runs/24982244020/job/73147828054) | [18m09s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193610) | 100% (2/2) | `shark01-ci`, `shark10-ci-2` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 6 | 1 | [15m35s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954035) | 0 | [4m01s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193629) | [16m27s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696479) | 0% (0/2) | `shark10-ci-2` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 18 | 0 | — | 2 | [5m56s](https://github.com/iree-org/iree/actions/runs/24977783490/job/73133696483) | [15m13s](https://github.com/iree-org/iree/actions/runs/24977091246/job/73131531108) | 0% (0/6) | `shark01-ci`, `shark10-ci-2`, `shark55-ci`, `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 6 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193582) | [14m12s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954034) | 0% (0/2) | `shark01-ci`, `shark10-ci-2` |
| `Linux,X64,rdna3` | self-hosted | 6 | 0 | — | 0 | [5m22s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954091) | [14m05s](https://github.com/iree-org/iree/actions/runs/24982797665/job/73149528859) | 0% (0/2) | `shark01-ci`, `shark10-ci-2`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 12 | 0 | — | 0 | [6m39s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193625) | [12m52s](https://github.com/iree-org/iree/actions/runs/24985668908/job/73159193646) | 0% (0/4) | `shark01-ci`, `shark10-ci-2`, `shark55-ci` |
| `azure-windows-scale` | ossci | 7 | 0 | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/24984135475/job/73153126424) | [6m10s](https://github.com/iree-org/iree/actions/runs/24985668927/job/73158235168) | 0% (0/2) | 7 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 24 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/24982797665/job/73149528857) | [2m08s](https://github.com/iree-org/iree/actions/runs/24977091246/job/73131531116) | 0% (0/8) | 24 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m52s](https://github.com/iree-org/iree/actions/runs/24988571683/job/73168031432) | [1m52s](https://github.com/iree-org/iree/actions/runs/24988571683/job/73168031432) | 0% (0/1) | 1 |
| `azure-linux-scale` | ossci | 39 | 0 | — | 2 | [10s](https://github.com/iree-org/iree/actions/runs/24984135475/job/73153126410) | [1m46s](https://github.com/iree-org/iree/actions/runs/24982244024/job/73146988827) | 0% (0/14) | 39 |
| `windows-2022` | github-hosted | 23 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24995028438/job/73189692615) | [50s](https://github.com/iree-org/iree/actions/runs/24982797659/job/73148756941) | 0% (0/6) | 23 |
| `ubuntu-24.04` | github-hosted | 126 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/24982797665/job/73149528847) | [4s](https://github.com/iree-org/iree/actions/runs/24982244024/job/73146988680) | 6% (2/36) | 125 |
| `macos-14` | github-hosted | 24 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/24995028438/job/73189692647) | [3s](https://github.com/iree-org/iree/actions/runs/24995028438/job/73189692582) | 0% (0/6) | 24 |
| `ubuntu-24.04-arm` | github-hosted | 24 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24984135475/job/73153126391) | [3s](https://github.com/iree-org/iree/actions/runs/24982797659/job/73148756991) | 0% (0/6) | 24 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/24988562703/job/73168001571) | [3s](https://github.com/iree-org/iree/actions/runs/24988562703/job/73168001571) | — | 1 |
| `ubuntu-latest` | github-hosted | 4 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/24982243413/job/73146966147) | [3s](https://github.com/iree-org/iree/actions/runs/24982797016/job/73148733232) | 0% (0/4) | 4 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 6 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/24982797665/job/73149528729) | [2s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954032) | 0% (0/2) | 6 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 6 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/24977091246/job/73131531076) | [2s](https://github.com/iree-org/iree/actions/runs/24995028433/job/73190954386) | 0% (0/2) | `iree-mi308-1` |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 432 | 14% (60/427) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 317 | 0% (0/312) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 120 | 0% (0/117) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 331 | 3% (9/325) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 400 | 2% (7/395) | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
