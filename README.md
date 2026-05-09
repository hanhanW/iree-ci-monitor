# iree-ci-monitor

_Updated: 2026-05-09 05:38 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 1 | 0 | — | 0 | [36m44s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661914) | [36m44s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661914) | — | `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 1 | 0 | — | 0 | [22m24s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661892) | [22m24s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661892) | — | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 2 | 0 | — | 0 | [8m29s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661907) | [16m07s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661924) | — | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 2 | 0 | — | 0 | [5m05s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661921) | [14m13s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661919) | — | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 2 | 0 | — | 0 | [4m07s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661891) | [11m53s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661908) | — | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 1 | 0 | — | 0 | [9m31s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661939) | [9m31s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661939) | — | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 1 | 0 | — | 0 | [4m39s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661920) | [4m39s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661920) | — | `shark10-ci` |
| `Linux,X64,rdna3` | self-hosted | 1 | 0 | — | 0 | [4m08s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661938) | [4m08s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661938) | — | `shark55-ci` |
| `azure-linux-scale` | ossci | 15 | 0 | — | 0 | [12s](https://github.com/iree-org/iree/actions/runs/25598787767/job/75149272423) | [2m06s](https://github.com/iree-org/iree/actions/runs/25598663277/job/75148861177) | — | 13 |
| `ubuntu-24.04` | github-hosted | 61 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661910) | [8s](https://github.com/iree-org/iree/actions/runs/25598787767/job/75149272362) | 67% (4/6) | 61 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 4 | 0 | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661884) | [8s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661937) | — | 4 |
| `ubuntu-latest` | github-hosted | 7 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25600094239/job/75152440631) | [7s](https://github.com/iree-org/iree/actions/runs/25599992250/job/75152184401) | — | 7 |
| `ubuntu-24.04-arm` | github-hosted | 12 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25598663269/job/75148958680) | [3s](https://github.com/iree-org/iree/actions/runs/25598663269/job/75148958704) | — | 12 |
| `windows-2022` | github-hosted | 11 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25598663269/job/75148958681) | [3s](https://github.com/iree-org/iree/actions/runs/25598663269/job/75148958711) | — | 11 |
| `macos-14` | github-hosted | 11 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25598663269/job/75148958724) | [3s](https://github.com/iree-org/iree/actions/runs/25598787767/job/75149272334) | — | 11 |
| `Linux,X64,iree-r9700` | self-hosted | 1 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661858) | [2s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661858) | — | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 1 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661870) | [2s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661870) | — | `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 1 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661885) | [2s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661885) | — | `shark01-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 1 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661909) | [2s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661909) | — | `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 1 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661928) | [2s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661928) | — | `iree-mi308-1` |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661809) | [1s](https://github.com/iree-org/iree/actions/runs/25598787761/job/75149661809) | — | 1 |
| `azure-windows-scale` | ossci | 3 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25598663269/job/75148958789) | [1s](https://github.com/iree-org/iree/actions/runs/25598787767/job/75149272422) | — | 3 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 886 | 8% (73/883) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 740 | 3% (24/738) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 943 | 5% (46/941) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 639 | 2% (12/637) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 243 | 2% (5/242) | yes | running |

## Alerts

- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
