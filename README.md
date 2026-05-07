# iree-ci-monitor

_Updated: 2026-05-06 18:13 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 33 | 3 | [6h29m](https://github.com/iree-org/iree/actions/runs/25453930468/job/74679486343) | 0 | [1h00m](https://github.com/iree-org/iree/actions/runs/25444824291/job/74647420029) | [3h40m](https://github.com/iree-org/iree/actions/runs/25459691058/job/74699861471) | 11% (1/9) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 33 | 0 | — | 0 | [49m56s](https://github.com/iree-org/iree/actions/runs/25448473550/job/74660987548) | [3h36m](https://github.com/iree-org/iree/actions/runs/25460700807/job/74703156340) | 0% (0/9) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 66 | 11 | [6h29m](https://github.com/iree-org/iree/actions/runs/25453930468/job/74679486300) | 1 | [44m24s](https://github.com/iree-org/iree/actions/runs/25460700807/job/74703156466) | [3h10m](https://github.com/iree-org/iree/actions/runs/25461510340/job/74705980071) | 0% (0/12) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 33 | 2 | [3h49m](https://github.com/iree-org/iree/actions/runs/25461510340/job/74705979715) | 0 | [42m17s](https://github.com/iree-org/iree/actions/runs/25448786506/job/74661336596) | [3h09m](https://github.com/iree-org/iree/actions/runs/25459572352/job/74699652656) | 0% (0/7) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 33 | 2 | [6h29m](https://github.com/iree-org/iree/actions/runs/25453930468/job/74679486118) | 0 | [29m11s](https://github.com/iree-org/iree/actions/runs/25444824291/job/74647419872) | [3h05m](https://github.com/iree-org/iree/actions/runs/25461238142/job/74704977306) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 66 | 0 | — | 0 | [20m56s](https://github.com/iree-org/iree/actions/runs/25461998416/job/74708734235) | [2h29m](https://github.com/iree-org/iree/actions/runs/25459820642/job/74700443481) | 6% (1/18) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 33 | 7 | [8h19m](https://github.com/iree-org/iree/actions/runs/25448473550/job/74660987369) | 1 | [20m43s](https://github.com/iree-org/iree/actions/runs/25444324780/job/74646531950) | [2h16m](https://github.com/iree-org/iree/actions/runs/25465365268/job/74718227500) | 0% (0/5) | `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 33 | 0 | — | 1 | [33m03s](https://github.com/iree-org/iree/actions/runs/25465365268/job/74718227461) | [2h09m](https://github.com/iree-org/iree/actions/runs/25462555299/job/74709190317) | 0% (0/9) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 66 | 0 | — | 0 | [21m50s](https://github.com/iree-org/iree/actions/runs/25449821789/job/74665152486) | [2h05m](https://github.com/iree-org/iree/actions/runs/25462555299/job/74709190334) | 17% (3/18) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 33 | 0 | — | 1 | [28m48s](https://github.com/iree-org/iree/actions/runs/25444257616/job/74645460861) | [2h00m](https://github.com/iree-org/iree/actions/runs/25464305966/job/74716478145) | 0% (0/9) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 33 | 0 | — | 0 | [44m57s](https://github.com/iree-org/iree/actions/runs/25459418506/job/74699047015) | [1h24m](https://github.com/iree-org/iree/actions/runs/25461510340/job/74705979808) | 0% (0/9) | `shark01-ci`, `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 33 | 0 | — | 0 | [3m59s](https://github.com/iree-org/iree/actions/runs/25444257616/job/74645460949) | [57m22s](https://github.com/iree-org/iree/actions/runs/25461238142/job/74704977273) | 0% (0/9) | `iree-mi308-1` |
| `Linux,X64,rdna3` | self-hosted | 33 | 0 | — | 1 | [9m42s](https://github.com/iree-org/iree/actions/runs/25465365268/job/74718227501) | [57m19s](https://github.com/iree-org/iree/actions/runs/25459691058/job/74699861404) | 0% (0/9) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 132 | 0 | — | 0 | [14s](https://github.com/iree-org/iree/actions/runs/25450051546/job/74665818560) | [13m47s](https://github.com/iree-org/iree/actions/runs/25459691058/job/74699861348) | 22% (8/36) | 123 |
| `azure-linux-scale` | ossci | 181 | 0 | — | 4 | [10s](https://github.com/iree-org/iree/actions/runs/25461238142/job/74703708907) | [4m33s](https://github.com/iree-org/iree/actions/runs/25444324780/job/74644164104) | 0% (0/55) | 176 |
| `ubuntu-24.04` | github-hosted | 605 | 0 | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/25464915080/job/74715841429) | [4m10s](https://github.com/iree-org/iree/actions/runs/25459820553/job/74698959636) | 3% (4/151) | 571 |
| `windows-2022` | github-hosted | 99 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25461510816/job/74704619973) | [2m36s](https://github.com/iree-org/iree/actions/runs/25448786453/job/74660139577) | 0% (0/27) | 96 |
| `ubuntu-24.04-arm` | github-hosted | 99 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25461510816/job/74704619905) | [2m30s](https://github.com/iree-org/iree/actions/runs/25461998386/job/74706625219) | 0% (0/27) | 96 |
| `macos-14` | github-hosted | 99 | 0 | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/25448249008/job/74658217439) | [2m08s](https://github.com/iree-org/iree/actions/runs/25461554705/job/74704819223) | 0% (0/27) | 96 |
| `azure-windows-scale` | ossci | 33 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25448425387/job/74658831278) | [51s](https://github.com/iree-org/iree/actions/runs/25464306004/job/74713863237) | 0% (0/9) | 32 |
| `ubuntu-latest` | github-hosted | 52 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25461237675/job/74703662751) | [40s](https://github.com/iree-org/iree/actions/runs/25459817450/job/74698823689) | 0% (0/18) | 52 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 33 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25448249077/job/74659571992) | [2s](https://github.com/iree-org/iree/actions/runs/25461554615/job/74706063035) | 33% (3/9) | 31 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 859 | 6% (54/856) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 946 | 1% (13/942) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 745 | 1% (11/743) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 650 | 1% (6/648) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 227 | 1% (3/226) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 6h29m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 6h29m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 3h49m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 8h19m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 6h29m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 2h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h29m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 3h05m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 3h10m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 3h09m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 3h36m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 2h16m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 3h40m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 1h24m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h05m (> 1h00m)
- **[high-failure-main]** `linux-mi325-1gpu-ossci-iree-org` main-branch failure rate 22% (8/36)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
