# iree-ci-monitor

_Updated: 2026-04-28 00:16 PDT_ — `iree-org/iree`, last 10h

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 24 | 13 | [8h31m](https://github.com/iree-org/iree/actions/runs/25023134490/job/73289495756) | 0 | [2h20m](https://github.com/iree-org/iree/actions/runs/25023118334/job/73289097269) | [8h51m](https://github.com/iree-org/iree/actions/runs/25020455344/job/73282046683) | 0% (0/2) | `shark01-ci` |
| `Linux,X64,gfx1201` | self-hosted | 48 | 30 | [9h30m](https://github.com/iree-org/iree/actions/runs/25020455344/job/73282046846) | 0 | [3h26m](https://github.com/iree-org/iree/actions/runs/25023118334/job/73289097253) | [7h59m](https://github.com/iree-org/iree/actions/runs/25021273456/job/73283024422) | 0% (0/1) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 24 | 10 | [7h05m](https://github.com/iree-org/iree/actions/runs/25026229088/job/73298600831) | 0 | [3h58m](https://github.com/iree-org/iree/actions/runs/25019547792/job/73277809131) | [7h22m](https://github.com/iree-org/iree/actions/runs/25020455344/job/73282046816) | 0% (0/3) | `shark01-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 24 | 8 | [3h39m](https://github.com/iree-org/iree/actions/runs/25031463022/job/73317088668) | 0 | [2h55m](https://github.com/iree-org/iree/actions/runs/25027763151/job/73303249569) | [6h34m](https://github.com/iree-org/iree/actions/runs/25022814186/job/73288074560) | 0% (0/5) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 24 | 6 | [2h20m](https://github.com/iree-org/iree/actions/runs/25034506099/job/73323661787) | 0 | [2h10m](https://github.com/iree-org/iree/actions/runs/25023118334/job/73289097192) | [3h39m](https://github.com/iree-org/iree/actions/runs/25025594777/job/73296522791) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 24 | 5 | [1h12m](https://github.com/iree-org/iree/actions/runs/25036437983/job/73330088279) | 1 | [2h04m](https://github.com/iree-org/iree/actions/runs/25031463022/job/73317088593) | [3h19m](https://github.com/iree-org/iree/actions/runs/25026229088/job/73298600670) | 0% (0/6) | `shark01-ci`, `shark10-ci-2` |
| `Linux,X64,rdna3` | self-hosted | 24 | 5 | [1h12m](https://github.com/iree-org/iree/actions/runs/25036437983/job/73330088396) | 1 | [2h03m](https://github.com/iree-org/iree/actions/runs/25022814186/job/73288074556) | [2h48m](https://github.com/iree-org/iree/actions/runs/25033295352/job/73319978561) | 0% (0/6) | `shark01-ci`, `shark10-ci-2`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 72 | 17 | [2h20m](https://github.com/iree-org/iree/actions/runs/25034506099/job/73323661844) | 0 | [2h06m](https://github.com/iree-org/iree/actions/runs/25034506099/job/73323661845) | [2h40m](https://github.com/iree-org/iree/actions/runs/25025594777/job/73296522900) | 0% (0/18) | `shark01-ci`, `shark10-ci-2`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 24 | 5 | [2h20m](https://github.com/iree-org/iree/actions/runs/25034506099/job/73323661843) | 0 | [1h52m](https://github.com/iree-org/iree/actions/runs/25030607027/job/73311802070) | [2h34m](https://github.com/iree-org/iree/actions/runs/25023134490/job/73289495854) | 0% (0/7) | `shark01-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 48 | 12 | [2h20m](https://github.com/iree-org/iree/actions/runs/25034506099/job/73323661836) | 0 | [2h02m](https://github.com/iree-org/iree/actions/runs/25032162739/job/73316989228) | [2h31m](https://github.com/iree-org/iree/actions/runs/25031463022/job/73317088693) | 8% (1/12) | `shark01-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 136 | 0 | — | 2 | [13s](https://github.com/iree-org/iree/actions/runs/25033911198/job/73321427822) | [19m00s](https://github.com/iree-org/iree/actions/runs/25037262482/job/73331746991) | 0% (0/48) | 131 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 24 | 0 | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/25032162739/job/73316989124) | [11m29s](https://github.com/iree-org/iree/actions/runs/25019547792/job/73277809066) | 0% (0/7) | `iree-mi308-1` |
| `windows-2022` | github-hosted | 77 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25025594770/job/73295914856) | [3m53s](https://github.com/iree-org/iree/actions/runs/25037869922/job/73333682584) | 0% (0/24) | 77 |
| `macos-14` | github-hosted | 78 | 0 | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/25034506085/job/73323105894) | [3m01s](https://github.com/iree-org/iree/actions/runs/25023118330/job/73288417134) | 0% (0/24) | 78 |
| `ubuntu-24.04-arm` | github-hosted | 78 | 0 | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/25036522889/job/73329401569) | [2m53s](https://github.com/iree-org/iree/actions/runs/25037869922/job/73333682579) | 0% (0/24) | 78 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 96 | 0 | — | 2 | [8s](https://github.com/iree-org/iree/actions/runs/25032162739/job/73316989158) | [2m50s](https://github.com/iree-org/iree/actions/runs/25019547792/job/73277809196) | 7% (2/30) | 96 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | 0 | [1m50s](https://github.com/iree-org/iree/actions/runs/25030009343/job/73309430370) | [1m50s](https://github.com/iree-org/iree/actions/runs/25030009343/job/73309430370) | — | 1 |
| `ubuntu-24.04` | github-hosted | 416 | 0 | — | 5 | [2s](https://github.com/iree-org/iree/actions/runs/25035264929/job/73326284430) | [1m45s](https://github.com/iree-org/iree/actions/runs/25023118330/job/73288417034) | 1% (1/123) | 416 |
| `ubuntu-latest` | github-hosted | 46 | 0 | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25020454634/job/73279372245) | [13s](https://github.com/iree-org/iree/actions/runs/25025594154/job/73295895843) | 0% (0/17) | 46 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | 1 | [12s](https://github.com/iree-org/iree/actions/runs/25030009343/job/73309430381) | [12s](https://github.com/iree-org/iree/actions/runs/25030009343/job/73309430381) | — | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 24 | 0 | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25021273456/job/73283024121) | [2s](https://github.com/iree-org/iree/actions/runs/25036522879/job/73332603960) | 25% (2/8) | 24 |
| `azure-windows-scale` | ossci | 25 | 0 | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25030607011/job/73311232657) | [1s](https://github.com/iree-org/iree/actions/runs/25037869922/job/73333682647) | 0% (0/8) | 25 |
| `Linux,X64,rdna3,shark10-ci` | self-hosted | 24 | 21 | [9h59m](https://github.com/iree-org/iree/actions/runs/25019547792/job/73277809149) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/25033911199/job/73321958036) | [0s](https://github.com/iree-org/iree/actions/runs/25034982190/job/73325359539) | — | 0 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 24 | 20 | [9h59m](https://github.com/iree-org/iree/actions/runs/25019547792/job/73277809248) | 0 | [0s](https://github.com/iree-org/iree/actions/runs/25033911199/job/73321957973) | [0s](https://github.com/iree-org/iree/actions/runs/25034982190/job/73325359496) | — | `shark10-ci-2` |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 517 | 2% (10/513) | yes | running |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 455 | 3% (14/449) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 435 | 1% (6/430) | yes | running |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 160 | 1% (1/156) | yes | running |
| `shark10-ci-2` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 466 | 14% (63/462) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job waiting 2h20m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job waiting 2h20m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job waiting 3h39m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job waiting 9h30m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job waiting 2h20m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-w7900x2,persistent-cache` oldest queued job waiting 8h31m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache,shark10-ci` oldest queued job waiting 9h59m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,shark10-ci` oldest queued job waiting 9h59m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64,threadripper` oldest queued job waiting 7h05m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job waiting 2h20m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 2h34m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h31m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 6h34m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 7h59m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 3h39m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 3h19m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 8h51m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h48m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 7h22m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h40m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day.
