# iree-ci-monitor

_Updated: 2026-05-07 00:20 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 26 | 0 | — | 0 | [24m21s](https://github.com/iree-org/iree/actions/runs/25473551877/job/74744810935) | [4h02m](https://github.com/iree-org/iree/actions/runs/25461631964/job/74708862174) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 13 | 0 | — | 0 | [28m50s](https://github.com/iree-org/iree/actions/runs/25473551877/job/74744810860) | [3h50m](https://github.com/iree-org/iree/actions/runs/25461631964/job/74708862128) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 13 | 0 | — | 0 | [36m28s](https://github.com/iree-org/iree/actions/runs/25461998416/job/74708734324) | [3h34m](https://github.com/iree-org/iree/actions/runs/25461510340/job/74705979974) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 13 | 0 | — | 0 | [5m24s](https://github.com/iree-org/iree/actions/runs/25476418237/job/74751410990) | [3h04m](https://github.com/iree-org/iree/actions/runs/25464163191/job/74716050502) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 13 | 0 | — | 0 | [21m20s](https://github.com/iree-org/iree/actions/runs/25476418237/job/74751411089) | [3h00m](https://github.com/iree-org/iree/actions/runs/25464163191/job/74716050548) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 13 | 0 | — | 0 | [15m48s](https://github.com/iree-org/iree/actions/runs/25476418237/job/74751411115) | [2h34m](https://github.com/iree-org/iree/actions/runs/25461631964/job/74708862163) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 26 | 0 | — | 0 | [4m38s](https://github.com/iree-org/iree/actions/runs/25473551877/job/74744810915) | [2h30m](https://github.com/iree-org/iree/actions/runs/25461631964/job/74708862145) | 25% (1/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 13 | 0 | — | 0 | [21m49s](https://github.com/iree-org/iree/actions/runs/25473551877/job/74744810882) | [2h09m](https://github.com/iree-org/iree/actions/runs/25462555299/job/74709190317) | 0% (0/2) | `shark01-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 27 | 0 | — | 0 | [11m55s](https://github.com/iree-org/iree/actions/runs/25461631964/job/74708862112) | [2h05m](https://github.com/iree-org/iree/actions/runs/25462555299/job/74709190334) | 25% (1/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 13 | 0 | — | 0 | [1h12m](https://github.com/iree-org/iree/actions/runs/25461510340/job/74705979768) | [1h55m](https://github.com/iree-org/iree/actions/runs/25464163191/job/74716050498) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 13 | 0 | — | 0 | [7m12s](https://github.com/iree-org/iree/actions/runs/25476418237/job/74751411092) | [1h24m](https://github.com/iree-org/iree/actions/runs/25461510340/job/74705979808) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 13 | 0 | — | 0 | [9m42s](https://github.com/iree-org/iree/actions/runs/25465365268/job/74718227501) | [49m13s](https://github.com/iree-org/iree/actions/runs/25464163191/job/74716050620) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 13 | 0 | — | 0 | [18s](https://github.com/iree-org/iree/actions/runs/25461998416/job/74708734130) | [18m09s](https://github.com/iree-org/iree/actions/runs/25462555299/job/74709190207) | 0% (0/2) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 52 | 0 | — | 0 | [7s](https://github.com/iree-org/iree/actions/runs/25475355416/job/74748239731) | [7m01s](https://github.com/iree-org/iree/actions/runs/25462555299/job/74709190096) | 50% (4/8) | 48 |
| `ubuntu-24.04-arm` | github-hosted | 42 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25476307399/job/74750501927) | [2m30s](https://github.com/iree-org/iree/actions/runs/25461998386/job/74706625219) | 0% (0/3) | 42 |
| `windows-2022` | github-hosted | 41 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25476307399/job/74750501953) | [2m07s](https://github.com/iree-org/iree/actions/runs/25461631917/job/74705721164) | 0% (0/3) | 41 |
| `ubuntu-24.04` | github-hosted | 269 | 0 | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/25465365231/job/74717562947) | [1m29s](https://github.com/iree-org/iree/actions/runs/25461998386/job/74706625182) | 8% (3/37) | 259 |
| `macos-14` | github-hosted | 41 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25478838959/job/74758336928) | [1m23s](https://github.com/iree-org/iree/actions/runs/25461631917/job/74705721234) | 0% (0/3) | 41 |
| `azure-linux-scale` | ossci | 71 | 0 | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/25464306004/job/74713863191) | [1m19s](https://github.com/iree-org/iree/actions/runs/25475355423/job/74747567394) | 0% (0/7) | 67 |
| `azure-windows-scale` | ossci | 13 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25476307399/job/74750502034) | [51s](https://github.com/iree-org/iree/actions/runs/25464306004/job/74713863237) | 0% (0/1) | 13 |
| `ubuntu-latest` | github-hosted | 6 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25469615859/job/74730469399) | [9s](https://github.com/iree-org/iree/actions/runs/25464162731/job/74713375987) | 0% (0/2) | 6 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 13 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25465365268/job/74718227328) | [2s](https://github.com/iree-org/iree/actions/runs/25461554615/job/74706063035) | 100% (2/2) | 13 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 969 | 1% (14/966) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 660 | 1% (6/658) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 876 | 6% (55/874) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 755 | 1% (11/753) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 231 | 1% (3/230) | yes | running |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 2h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h30m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 3h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 4h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 3h04m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 1h55m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 2h34m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 3h50m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 3h34m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h24m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h05m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
