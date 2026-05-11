# iree-ci-monitor

_Updated: 2026-05-11 06:21 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 14 | 0 | — | 0 | [17m21s](https://github.com/iree-org/iree/actions/runs/25651201814/job/75291283448) | [1h23m](https://github.com/iree-org/iree/actions/runs/25657840679/job/75311861586) | 0% (0/1) | `shark75-ci` |
| `azure-windows-scale` | ossci | 18 | 0 | — | 0 | [1m14s](https://github.com/iree-org/iree/actions/runs/25655593438/job/75303177689) | [1h19m](https://github.com/iree-org/iree/actions/runs/25660883101/job/75321265346) | 0% (0/1) | 14 |
| `Linux,X64,gfx1201` | self-hosted | 28 | 0 | — | 0 | [10m59s](https://github.com/iree-org/iree/actions/runs/25667829692/job/75346179085) | [1h05m](https://github.com/iree-org/iree/actions/runs/25656097969/job/75309375300) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 14 | 0 | — | 0 | [17m38s](https://github.com/iree-org/iree/actions/runs/25651201814/job/75291283467) | [48m09s](https://github.com/iree-org/iree/actions/runs/25664812496/job/75335555776) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 14 | 0 | — | 0 | [3m42s](https://github.com/iree-org/iree/actions/runs/25664812496/job/75335555507) | [46m52s](https://github.com/iree-org/iree/actions/runs/25657981746/job/75313489196) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 14 | 0 | — | 0 | [13m32s](https://github.com/iree-org/iree/actions/runs/25651201814/job/75291283342) | [31m23s](https://github.com/iree-org/iree/actions/runs/25657840679/job/75311861394) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 14 | 0 | — | 0 | [12m52s](https://github.com/iree-org/iree/actions/runs/25668777375/job/75349230611) | [25m58s](https://github.com/iree-org/iree/actions/runs/25660883155/job/75322507310) | 0% (0/1) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 28 | 0 | — | 0 | [5m18s](https://github.com/iree-org/iree/actions/runs/25660985947/job/75322894498) | [25m57s](https://github.com/iree-org/iree/actions/runs/25657981746/job/75313489394) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 14 | 0 | — | 0 | [8m58s](https://github.com/iree-org/iree/actions/runs/25655593466/job/75306399099) | [24m36s](https://github.com/iree-org/iree/actions/runs/25651548812/job/75294450649) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 14 | 0 | — | 0 | [8m56s](https://github.com/iree-org/iree/actions/runs/25651201814/job/75291283460) | [23m16s](https://github.com/iree-org/iree/actions/runs/25660883155/job/75322507311) | 0% (0/1) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 28 | 0 | — | 0 | [3m56s](https://github.com/iree-org/iree/actions/runs/25668777375/job/75349230634) | [18m32s](https://github.com/iree-org/iree/actions/runs/25664812496/job/75335555522) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 14 | 0 | — | 0 | [8m35s](https://github.com/iree-org/iree/actions/runs/25653961292/job/75299620349) | [18m17s](https://github.com/iree-org/iree/actions/runs/25660883155/job/75322507261) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 93 | 0 | — | 0 | [41s](https://github.com/iree-org/iree/actions/runs/25660883101/job/75321265411) | [16m13s](https://github.com/iree-org/iree/actions/runs/25655593466/job/75303180002) | 0% (0/8) | 88 |
| `Linux,X64,rdna3` | self-hosted | 14 | 0 | — | 0 | [8m20s](https://github.com/iree-org/iree/actions/runs/25651201814/job/75291283449) | [9m42s](https://github.com/iree-org/iree/actions/runs/25660985947/job/75322893974) | 0% (0/1) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `windows-2022` | github-hosted | 56 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25656097892/job/75305115586) | [1m47s](https://github.com/iree-org/iree/actions/runs/25657679209/job/75310022648) | 0% (0/3) | 53 |
| `macos-14` | github-hosted | 57 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25660883101/job/75321265481) | [1m45s](https://github.com/iree-org/iree/actions/runs/25655593438/job/75303177586) | 0% (0/3) | 54 |
| `ubuntu-24.04-arm` | github-hosted | 57 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25660986003/job/75321622440) | [1m41s](https://github.com/iree-org/iree/actions/runs/25657981780/job/75311179244) | 0% (0/3) | 54 |
| `ubuntu-24.04` | github-hosted | 319 | 0 | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/25660986003/job/75321622454) | [1m16s](https://github.com/iree-org/iree/actions/runs/25657840679/job/75311861416) | 10% (2/21) | 315 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 56 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25668777375/job/75349230557) | [1m10s](https://github.com/iree-org/iree/actions/runs/25668777375/job/75349230971) | 25% (1/4) | 56 |
| `ubuntu-latest` | github-hosted | 11 | 0 | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/25657676912/job/75309994146) | [8s](https://github.com/iree-org/iree/actions/runs/25668427375/job/75346981465) | 0% (0/2) | 11 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 14 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25657981746/job/75313489332) | [4s](https://github.com/iree-org/iree/actions/runs/25660883155/job/75322507318) | 0% (0/1) | `iree-mi308-1` |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/25664519709/job/75333431199) | [4s](https://github.com/iree-org/iree/actions/runs/25664519709/job/75333431199) | — | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 14 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25651201814/job/75291283273) | [2s](https://github.com/iree-org/iree/actions/runs/25657981746/job/75313489302) | 100% (1/1) | 14 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 1 | [2h56m](https://github.com/iree-org/iree/actions/runs/25664551860/job/75333540077) | 0 | 0s | 0s | — | 0 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1027 | 5% (48/1025) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 967 | 8% (80/964) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 802 | 3% (24/800) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 690 | 2% (13/688) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 262 | 2% (6/261) | yes | running |

## Alerts

- **[stale-queued]** `ah-ubuntu_22_04-c7g_4x-50` oldest queued job waiting 2h56m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h23m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h05m (> 1h00m)
- **[queue-starved]** `azure-windows-scale` p95 queue 1h19m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
