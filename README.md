# iree-ci-monitor

_Updated: 2026-05-08 05:53 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 11 | 3 | [26m44s](https://github.com/iree-org/iree/actions/runs/25555107126/job/75013230321) | 0 | [20m37s](https://github.com/iree-org/iree/actions/runs/25542233917/job/74974769060) | [1h26m](https://github.com/iree-org/iree/actions/runs/25543342736/job/74975607851) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 11 | 2 | [26m15s](https://github.com/iree-org/iree/actions/runs/25555125920/job/75013299416) | 0 | [15m59s](https://github.com/iree-org/iree/actions/runs/25555107126/job/75013230218) | [1h18m](https://github.com/iree-org/iree/actions/runs/25543587944/job/74976004778) | 0% (0/3) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 22 | 5 | [26m44s](https://github.com/iree-org/iree/actions/runs/25555107126/job/75013230258) | 1 | [28m29s](https://github.com/iree-org/iree/actions/runs/25554329769/job/75010506973) | [1h16m](https://github.com/iree-org/iree/actions/runs/25543587944/job/74976004767) | 0% (0/4) | `shark75-ci` |
| `azure-windows-scale` | ossci | 10 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25555107115/job/75012078830) | [1h09m](https://github.com/iree-org/iree/actions/runs/25543587961/job/74974676008) | 0% (0/4) | 10 |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 11 | 3 | [26m44s](https://github.com/iree-org/iree/actions/runs/25555107126/job/75013230276) | 0 | [20m47s](https://github.com/iree-org/iree/actions/runs/25548848326/job/74992583362) | [1h00m](https://github.com/iree-org/iree/actions/runs/25542233917/job/74974768991) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 11 | 1 | [26m15s](https://github.com/iree-org/iree/actions/runs/25555125920/job/75013299353) | 1 | [14m28s](https://github.com/iree-org/iree/actions/runs/25548848326/job/74992583312) | [59m40s](https://github.com/iree-org/iree/actions/runs/25541570373/job/74975110536) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 11 | 2 | [26m15s](https://github.com/iree-org/iree/actions/runs/25555125920/job/75013299562) | 0 | [2m23s](https://github.com/iree-org/iree/actions/runs/25543342736/job/74975607867) | [46m31s](https://github.com/iree-org/iree/actions/runs/25543587944/job/74976004733) | 0% (0/3) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 11 | 2 | [26m15s](https://github.com/iree-org/iree/actions/runs/25555125920/job/75013299385) | 0 | [11m20s](https://github.com/iree-org/iree/actions/runs/25543342736/job/74975607793) | [44m39s](https://github.com/iree-org/iree/actions/runs/25543587944/job/74976004637) | 33% (1/3) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 22 | 3 | [26m44s](https://github.com/iree-org/iree/actions/runs/25555107126/job/75013230172) | 0 | [8m46s](https://github.com/iree-org/iree/actions/runs/25536256872/job/74959512159) | [42m55s](https://github.com/iree-org/iree/actions/runs/25543587944/job/74976004723) | 0% (0/5) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 22 | 5 | [26m44s](https://github.com/iree-org/iree/actions/runs/25555107126/job/75013230324) | 0 | [6m04s](https://github.com/iree-org/iree/actions/runs/25548848326/job/74992583389) | [39m23s](https://github.com/iree-org/iree/actions/runs/25542233917/job/74974769119) | 0% (0/5) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 11 | 0 | — | 2 | [13m16s](https://github.com/iree-org/iree/actions/runs/25555373579/job/75014044664) | [32m21s](https://github.com/iree-org/iree/actions/runs/25543342736/job/74975607833) | 0% (0/3) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 11 | 3 | [26m44s](https://github.com/iree-org/iree/actions/runs/25555107126/job/75013230175) | 0 | [10m01s](https://github.com/iree-org/iree/actions/runs/25554329769/job/75010506862) | [31m38s](https://github.com/iree-org/iree/actions/runs/25543587944/job/74976004674) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `azure-linux-scale` | ossci | 58 | 1 | [6h02m](https://github.com/iree-org/iree/actions/runs/25541570373/job/74968460900) | 3 | [9s](https://github.com/iree-org/iree/actions/runs/25555373565/job/75012974122) | [28m06s](https://github.com/iree-org/iree/actions/runs/25542233931/job/74970476639) | 0% (0/24) | 57 |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 11 | 3 | [26m44s](https://github.com/iree-org/iree/actions/runs/25555107126/job/75013230289) | 0 | [5m29s](https://github.com/iree-org/iree/actions/runs/25542233917/job/74974769000) | [25m24s](https://github.com/iree-org/iree/actions/runs/25543342736/job/74975607819) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 11 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25555107126/job/75013230162) | [15m20s](https://github.com/iree-org/iree/actions/runs/25555373579/job/75014044591) | 0% (0/3) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 44 | 0 | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/25543587944/job/74976004765) | [4m29s](https://github.com/iree-org/iree/actions/runs/25555373579/job/75014044642) | 19% (3/16) | 44 |
| `ubuntu-24.04` | github-hosted | 220 | 0 | — | 2 | [8s](https://github.com/iree-org/iree/actions/runs/25548943214/job/74991871417) | [3m26s](https://github.com/iree-org/iree/actions/runs/25542233917/job/74974769035) | 6% (5/77) | 219 |
| `ubuntu-latest` | github-hosted | 25 | 0 | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/25541569699/job/74968424194) | [3m00s](https://github.com/iree-org/iree/actions/runs/25555605746/job/75013725893) | 0% (0/8) | 25 |
| `ubuntu-24.04-arm` | github-hosted | 33 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25536256863/job/74958704296) | [1m54s](https://github.com/iree-org/iree/actions/runs/25555125925/job/75012290658) | 0% (0/12) | 33 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m30s](https://github.com/iree-org/iree/actions/runs/25548944272/job/74991875074) | [1m30s](https://github.com/iree-org/iree/actions/runs/25548944272/job/74991875074) | 0% (0/1) | 1 |
| `windows-2022` | github-hosted | 32 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25542233931/job/74970476568) | [1m24s](https://github.com/iree-org/iree/actions/runs/25543342739/job/74973884851) | 0% (0/12) | 32 |
| `macos-14` | github-hosted | 33 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25543342739/job/74973884852) | [1m13s](https://github.com/iree-org/iree/actions/runs/25555125925/job/75012290682) | 0% (0/12) | 33 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/25548931396/job/74991832237) | [4s](https://github.com/iree-org/iree/actions/runs/25548931396/job/74991832237) | — | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 11 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25543342736/job/74975607756) | [2s](https://github.com/iree-org/iree/actions/runs/25555373579/job/75014044517) | 0% (0/4) | 11 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 607 | 2% (10/604) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 855 | 7% (60/851) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 230 | 2% (5/228) | yes | running |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 919 | 2% (22/916) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 714 | 2% (12/711) | yes | running |

## Alerts

- **[stale-queued]** `azure-linux-scale` oldest queued job waiting 6h02m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h00m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h16m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h18m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,shark10-ci` p95 queue 1h26m (> 1h00m)
- **[queue-starved]** `azure-windows-scale` p95 queue 1h09m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
