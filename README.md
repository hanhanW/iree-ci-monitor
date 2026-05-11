# iree-ci-monitor

_Updated: 2026-05-11 00:35 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 10 | 1 | [3m28s](https://github.com/iree-org/iree/actions/runs/25655593466/job/75306399015) | 1 | [8m47s](https://github.com/iree-org/iree/actions/runs/25651548812/job/75294450657) | [30m58s](https://github.com/iree-org/iree/actions/runs/25651548812/job/75294450763) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 5 | 1 | [3m28s](https://github.com/iree-org/iree/actions/runs/25655593466/job/75306399099) | 0 | [19m02s](https://github.com/iree-org/iree/actions/runs/25653961292/job/75299620438) | [24m36s](https://github.com/iree-org/iree/actions/runs/25651548812/job/75294450649) | — | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 5 | 0 | — | 1 | [17m38s](https://github.com/iree-org/iree/actions/runs/25651201814/job/75291283467) | [19m50s](https://github.com/iree-org/iree/actions/runs/25651548812/job/75294450791) | — | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 5 | 1 | [3m28s](https://github.com/iree-org/iree/actions/runs/25655593466/job/75306399030) | 0 | [17m21s](https://github.com/iree-org/iree/actions/runs/25651201814/job/75291283448) | [19m32s](https://github.com/iree-org/iree/actions/runs/25651548812/job/75294450636) | — | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 5 | 1 | [3m28s](https://github.com/iree-org/iree/actions/runs/25655593466/job/75306399057) | 0 | [13m32s](https://github.com/iree-org/iree/actions/runs/25651201814/job/75291283342) | [17m33s](https://github.com/iree-org/iree/actions/runs/25651548812/job/75294450646) | — | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 5 | 0 | — | 1 | [8m56s](https://github.com/iree-org/iree/actions/runs/25651201814/job/75291283460) | [16m51s](https://github.com/iree-org/iree/actions/runs/25653961292/job/75299620427) | — | `shark01-ci`, `shark10-ci` |
| `azure-linux-scale` | ossci | 31 | 5 | [14m02s](https://github.com/iree-org/iree/actions/runs/25656097969/job/75304898021) | 2 | [1m30s](https://github.com/iree-org/iree/actions/runs/25655353116/job/75302662011) | [15m43s](https://github.com/iree-org/iree/actions/runs/25655593438/job/75303177593) | 0% (0/4) | 26 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 5 | 1 | [3m28s](https://github.com/iree-org/iree/actions/runs/25655593466/job/75306399028) | 0 | [4m40s](https://github.com/iree-org/iree/actions/runs/25655353101/job/75303337980) | [13m36s](https://github.com/iree-org/iree/actions/runs/25653961292/job/75299620362) | — | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 10 | 2 | [3m28s](https://github.com/iree-org/iree/actions/runs/25655593466/job/75306399005) | 0 | [5m00s](https://github.com/iree-org/iree/actions/runs/25653961292/job/75299620460) | [9m50s](https://github.com/iree-org/iree/actions/runs/25653961292/job/75299620503) | — | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 10 | 1 | [3m28s](https://github.com/iree-org/iree/actions/runs/25655593466/job/75306399063) | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25655353101/job/75303337918) | [8m57s](https://github.com/iree-org/iree/actions/runs/25651548812/job/75294450653) | — | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 5 | 1 | [3m28s](https://github.com/iree-org/iree/actions/runs/25655593466/job/75306399001) | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25651201814/job/75291283363) | [8m35s](https://github.com/iree-org/iree/actions/runs/25653961292/job/75299620349) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 5 | 1 | [3m28s](https://github.com/iree-org/iree/actions/runs/25655593466/job/75306399073) | 0 | [8m18s](https://github.com/iree-org/iree/actions/runs/25653961292/job/75299620484) | [8m20s](https://github.com/iree-org/iree/actions/runs/25651201814/job/75291283449) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 5 | 1 | [3m28s](https://github.com/iree-org/iree/actions/runs/25655593466/job/75306398998) | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25653961292/job/75299620333) | [3m48s](https://github.com/iree-org/iree/actions/runs/25651548812/job/75294450662) | — | `shark01-ci`, `shark10-ci` |
| `windows-2022` | github-hosted | 20 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25655353116/job/75302661930) | [1m33s](https://github.com/iree-org/iree/actions/runs/25653961304/job/75298036526) | 0% (0/3) | 20 |
| `macos-14` | github-hosted | 20 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25651201822/job/75290651561) | [1m25s](https://github.com/iree-org/iree/actions/runs/25653961304/job/75298036504) | 0% (0/3) | 20 |
| `ubuntu-24.04` | github-hosted | 108 | 0 | — | 7 | [2s](https://github.com/iree-org/iree/actions/runs/25656098055/job/75304813745) | [1m23s](https://github.com/iree-org/iree/actions/runs/25655353101/job/75303337859) | 14% (2/14) | 108 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/25651201822/job/75290651572) | [1m21s](https://github.com/iree-org/iree/actions/runs/25653961304/job/75298036525) | 0% (0/3) | 21 |
| `azure-windows-scale` | ossci | 6 | 1 | [12m27s](https://github.com/iree-org/iree/actions/runs/25656097892/job/75305115644) | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25653961304/job/75298036539) | [1m14s](https://github.com/iree-org/iree/actions/runs/25655593438/job/75303177689) | 0% (0/1) | 5 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 20 | 0 | — | 2 | [8s](https://github.com/iree-org/iree/actions/runs/25655593466/job/75306399048) | [22s](https://github.com/iree-org/iree/actions/runs/25651201814/job/75291283475) | 50% (1/2) | 20 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 5 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25651201814/job/75291283273) | [2s](https://github.com/iree-org/iree/actions/runs/25655353101/job/75303337926) | — | 5 |
| `ubuntu-latest` | github-hosted | 2 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25655592520/job/75303152835) | [2s](https://github.com/iree-org/iree/actions/runs/25655592520/job/75303152867) | 0% (0/2) | 2 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 5 | 0 | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/25653961292/job/75299620514) | [1s](https://github.com/iree-org/iree/actions/runs/25655593466/job/75306399118) | — | `iree-mi308-1` |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 928 | 8% (78/924) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 663 | 2% (12/660) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 982 | 5% (48/979) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 253 | 2% (5/251) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 767 | 3% (24/764) | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
