# iree-ci-monitor

_Updated: 2026-05-12 06:03 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 26 | 0 | — | 0 | [51m36s](https://github.com/iree-org/iree/actions/runs/25722860607/job/75533089783) | [1h43m](https://github.com/iree-org/iree/actions/runs/25720109826/job/75523192749) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 13 | 0 | — | 0 | [35m05s](https://github.com/iree-org/iree/actions/runs/25720015534/job/75520451662) | [1h01m](https://github.com/iree-org/iree/actions/runs/25723865211/job/75532766225) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 13 | 0 | — | 0 | [37m05s](https://github.com/iree-org/iree/actions/runs/25726159309/job/75540890071) | [55m11s](https://github.com/iree-org/iree/actions/runs/25721900930/job/75529482810) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 13 | 0 | — | 0 | [18m44s](https://github.com/iree-org/iree/actions/runs/25726159309/job/75540889890) | [52m58s](https://github.com/iree-org/iree/actions/runs/25720109826/job/75523192567) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 13 | 0 | — | 0 | [22m32s](https://github.com/iree-org/iree/actions/runs/25722860607/job/75533089724) | [48m56s](https://github.com/iree-org/iree/actions/runs/25726607433/job/75544392912) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 13 | 0 | — | 0 | [29m13s](https://github.com/iree-org/iree/actions/runs/25723865211/job/75532766489) | [42m12s](https://github.com/iree-org/iree/actions/runs/25726607433/job/75544393028) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 13 | 0 | — | 0 | [17m09s](https://github.com/iree-org/iree/actions/runs/25733921709/job/75567054399) | [28m53s](https://github.com/iree-org/iree/actions/runs/25721900930/job/75529482784) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 26 | 0 | — | 0 | [10m38s](https://github.com/iree-org/iree/actions/runs/25722860607/job/75533089639) | [26m11s](https://github.com/iree-org/iree/actions/runs/25726607433/job/75544393047) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 13 | 0 | — | 0 | [11m56s](https://github.com/iree-org/iree/actions/runs/25733921709/job/75567054269) | [24m52s](https://github.com/iree-org/iree/actions/runs/25712502971/job/75496494072) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 13 | 0 | — | 0 | [14m17s](https://github.com/iree-org/iree/actions/runs/25711786487/job/75513949595) | [24m43s](https://github.com/iree-org/iree/actions/runs/25726607433/job/75544392921) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 26 | 0 | — | 0 | [4m36s](https://github.com/iree-org/iree/actions/runs/25726159309/job/75540889945) | [22m55s](https://github.com/iree-org/iree/actions/runs/25722860607/job/75533089568) | 25% (1/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `azure-linux-scale` | ossci | 84 | 3 | [1m53s](https://github.com/iree-org/iree/actions/runs/25736102654/job/75573498453) | 2 | [1m12s](https://github.com/iree-org/iree/actions/runs/25723865211/job/75531528212) | [21m08s](https://github.com/iree-org/iree/actions/runs/25721900930/job/75524922830) | 0% (0/14) | 78 |
| `Linux,X64,rdna3` | self-hosted | 13 | 0 | — | 0 | [7m40s](https://github.com/iree-org/iree/actions/runs/25723865211/job/75532766391) | [13m14s](https://github.com/iree-org/iree/actions/runs/25726159309/job/75540890022) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 13 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25720966732/job/75539072256) | [10m01s](https://github.com/iree-org/iree/actions/runs/25726159309/job/75540890076) | 0% (0/2) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 52 | 0 | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/25711786487/job/75513949554) | [7m18s](https://github.com/iree-org/iree/actions/runs/25722860607/job/75533089670) | 0% (0/8) | 52 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [7m08s](https://github.com/iree-org/iree/actions/runs/25727680023/job/75544582497) | [7m08s](https://github.com/iree-org/iree/actions/runs/25727680023/job/75544582497) | 0% (0/1) | 1 |
| `azure-windows-scale` | ossci | 16 | 0 | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/25733921759/job/75565844231) | [2m17s](https://github.com/iree-org/iree/actions/runs/25719314987/job/75516602489) | 0% (0/2) | 16 |
| `macos-14` | github-hosted | 51 | 0 | — | 4 | [3s](https://github.com/iree-org/iree/actions/runs/25720015565/job/75519008741) | [1m55s](https://github.com/iree-org/iree/actions/runs/25726607448/job/75541388738) | 0% (0/6) | 50 |
| `windows-2022` | github-hosted | 50 | 0 | — | 3 | [3s](https://github.com/iree-org/iree/actions/runs/25721900987/job/75524921145) | [1m50s](https://github.com/iree-org/iree/actions/runs/25721900987/job/75524921121) | 0% (0/6) | 50 |
| `ubuntu-24.04` | github-hosted | 296 | 0 | — | 8 | [3s](https://github.com/iree-org/iree/actions/runs/25726168960/job/75539604406) | [1m32s](https://github.com/iree-org/iree/actions/runs/25711786544/job/75513125039) | 10% (4/42) | 293 |
| `ubuntu-24.04-arm` | github-hosted | 51 | 0 | — | 3 | [3s](https://github.com/iree-org/iree/actions/runs/25723865199/job/75531538730) | [1m12s](https://github.com/iree-org/iree/actions/runs/25720109827/job/75520713248) | 0% (0/6) | 51 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25732151576/job/75559867407) | [8s](https://github.com/iree-org/iree/actions/runs/25731900895/job/75558980849) | 0% (0/5) | 12 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 1 | [6s](https://github.com/iree-org/iree/actions/runs/25727633237/job/75544419803) | [6s](https://github.com/iree-org/iree/actions/runs/25727633237/job/75544419803) | — | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 13 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25721900930/job/75529482684) | [3s](https://github.com/iree-org/iree/actions/runs/25726168960/job/75540753811) | 0% (0/2) | 13 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 1018 | 8% (85/1015) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1082 | 4% (48/1080) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,shark01-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 846 | 3% (22/844) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,shark55-ci`, `self-hosted,persistent-cache,Linux,X64` | 733 | 2% (11/731) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 278 | 3% (7/277) | yes | running |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h43m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h01m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
