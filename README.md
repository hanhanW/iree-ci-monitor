# iree-ci-monitor

_Updated: 2026-05-12 00:20 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 32 | 2 | [1m31s](https://github.com/iree-org/iree/actions/runs/25719315053/job/75517473276) | 0 | [1h21m](https://github.com/iree-org/iree/actions/runs/25712502971/job/75496494137) | [6h31m](https://github.com/iree-org/iree/actions/runs/25700159906/job/75462059157) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 16 | 1 | [1m31s](https://github.com/iree-org/iree/actions/runs/25719315053/job/75517473031) | 1 | [1h45m](https://github.com/iree-org/iree/actions/runs/25707853907/job/75482545357) | [5h03m](https://github.com/iree-org/iree/actions/runs/25698299550/job/75453350945) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 15 | 1 | [1m31s](https://github.com/iree-org/iree/actions/runs/25719315053/job/75517473274) | 0 | [28m47s](https://github.com/iree-org/iree/actions/runs/25712502971/job/75496494132) | [4h49m](https://github.com/iree-org/iree/actions/runs/25700017452/job/75459332837) | 0% (0/4) | `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 16 | 1 | [1m31s](https://github.com/iree-org/iree/actions/runs/25719315053/job/75517473308) | 0 | [1h26m](https://github.com/iree-org/iree/actions/runs/25702501863/job/75466541524) | [4h42m](https://github.com/iree-org/iree/actions/runs/25700017452/job/75459332743) | 0% (0/4) | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 16 | 1 | [1m31s](https://github.com/iree-org/iree/actions/runs/25719315053/job/75517473325) | 0 | [24m52s](https://github.com/iree-org/iree/actions/runs/25712502971/job/75496494072) | [3h55m](https://github.com/iree-org/iree/actions/runs/25700017452/job/75459332750) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 16 | 1 | [1m31s](https://github.com/iree-org/iree/actions/runs/25719315053/job/75517473158) | 1 | [24m14s](https://github.com/iree-org/iree/actions/runs/25707853907/job/75482545446) | [2h55m](https://github.com/iree-org/iree/actions/runs/25700159906/job/75462058832) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 16 | 1 | [1m31s](https://github.com/iree-org/iree/actions/runs/25719315053/job/75517473171) | 0 | [15m03s](https://github.com/iree-org/iree/actions/runs/25711786487/job/75513949486) | [2h31m](https://github.com/iree-org/iree/actions/runs/25701799400/job/75464305146) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 32 | 2 | [1m31s](https://github.com/iree-org/iree/actions/runs/25719315053/job/75517473269) | 0 | [29m28s](https://github.com/iree-org/iree/actions/runs/25698299550/job/75453351294) | [2h02m](https://github.com/iree-org/iree/actions/runs/25700159906/job/75462059159) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 16 | 1 | [1m31s](https://github.com/iree-org/iree/actions/runs/25719315053/job/75517473352) | 0 | [40m19s](https://github.com/iree-org/iree/actions/runs/25699768786/job/75458479170) | [1h20m](https://github.com/iree-org/iree/actions/runs/25702501863/job/75466541621) | 0% (0/4) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 32 | 1 | [1m31s](https://github.com/iree-org/iree/actions/runs/25719315053/job/75517473291) | 1 | [19m07s](https://github.com/iree-org/iree/actions/runs/25705717803/job/75476265218) | [1h18m](https://github.com/iree-org/iree/actions/runs/25700017452/job/75459332775) | 12% (1/8) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 16 | 1 | [1m31s](https://github.com/iree-org/iree/actions/runs/25719315053/job/75517473331) | 0 | [25m16s](https://github.com/iree-org/iree/actions/runs/25707853907/job/75482545476) | [1h08m](https://github.com/iree-org/iree/actions/runs/25700017452/job/75459332812) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 15 | 0 | — | 1 | [24m28s](https://github.com/iree-org/iree/actions/runs/25705717803/job/75476265268) | [57m25s](https://github.com/iree-org/iree/actions/runs/25700017452/job/75459332782) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,iree-w7900` | self-hosted | 2 | 0 | — | 0 | [33m51s](https://github.com/iree-org/iree/actions/runs/25699916098/job/75458484868) | [54m04s](https://github.com/iree-org/iree/actions/runs/25699916098/job/75458484933) | — | `shark01-ci`, `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 16 | 0 | — | 1 | [1m26s](https://github.com/iree-org/iree/actions/runs/25698299550/job/75453351074) | [8m14s](https://github.com/iree-org/iree/actions/runs/25700159906/job/75462059044) | 0% (0/4) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 64 | 1 | [1m31s](https://github.com/iree-org/iree/actions/runs/25719315053/job/75517473225) | 3 | [8s](https://github.com/iree-org/iree/actions/runs/25701799400/job/75464305138) | [4m54s](https://github.com/iree-org/iree/actions/runs/25700017452/job/75459332784) | 0% (0/16) | 63 |
| `azure-linux-scale` | ossci | 95 | 0 | — | 6 | [8s](https://github.com/iree-org/iree/actions/runs/25707853935/job/75481737715) | [3m32s](https://github.com/iree-org/iree/actions/runs/25712503006/job/75495532769) | 0% (0/25) | 91 |
| `ubuntu-24.04` | github-hosted | 335 | 0 | — | 11 | [3s](https://github.com/iree-org/iree/actions/runs/25711786487/job/75513949405) | [1m55s](https://github.com/iree-org/iree/actions/runs/25699799706/job/75457063779) | 5% (4/76) | 332 |
| `windows-2022` | github-hosted | 56 | 0 | — | 4 | [3s](https://github.com/iree-org/iree/actions/runs/25701799395/job/75463355213) | [1m36s](https://github.com/iree-org/iree/actions/runs/25702501866/job/75465526782) | 0% (0/12) | 56 |
| `ubuntu-24.04-arm` | github-hosted | 57 | 0 | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/25699916077/job/75457645982) | [1m09s](https://github.com/iree-org/iree/actions/runs/25700159898/job/75458228831) | 0% (0/12) | 57 |
| `macos-14` | github-hosted | 56 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25704767499/job/75472429620) | [1m06s](https://github.com/iree-org/iree/actions/runs/25699799706/job/75457063894) | 0% (0/12) | 55 |
| `ubuntu-latest` | github-hosted | 25 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25704766032/job/75472394481) | [26s](https://github.com/iree-org/iree/actions/runs/25699895282/job/75457348863) | 0% (0/9) | 25 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 16 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25698299550/job/75453350907) | [2s](https://github.com/iree-org/iree/actions/runs/25707853907/job/75482545373) | 25% (1/4) | 16 |
| `azure-windows-scale` | ossci | 18 | 0 | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/25702501866/job/75465526848) | [2s](https://github.com/iree-org/iree/actions/runs/25719302020/job/75516389243) | 0% (0/4) | 18 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 974 | 9% (83/970) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,shark55-ci`, `self-hosted,persistent-cache,Linux,X64` | 707 | 2% (11/704) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 268 | 3% (7/266) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1035 | 5% (48/1032) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,shark01-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 810 | 3% (22/807) | yes | running |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h08m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 6h31m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 5h03m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h55m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 2h31m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 4h42m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 4h49m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 3h55m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h18m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
