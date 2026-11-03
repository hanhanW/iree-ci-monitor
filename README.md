# iree-ci-monitor

_Updated: 2026-11-03 15:28 PST_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 18 | 0 | — | — | 0 | [1h58m](https://github.com/iree-org/iree/actions/runs/41683259826/job/126090725823) | [3h54m](https://github.com/iree-org/iree/actions/runs/41644460192/job/125950505795) | 0% (0/8) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 18 | 0 | — | — | 0 | [2h03m](https://github.com/iree-org/iree/actions/runs/41683259826/job/126090725844) | [3h42m](https://github.com/iree-org/iree/actions/runs/41644460192/job/125950505712) | 0% (0/8) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 18 | 0 | — | — | 0 | [1h45m](https://github.com/iree-org/iree/actions/runs/41652530758/job/125979237343) | [3h08m](https://github.com/iree-org/iree/actions/runs/41644460192/job/125950505728) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 9 | 0 | — | — | 0 | [24m02s](https://github.com/iree-org/iree/actions/runs/41645995117/job/125955353386) | [2h04m](https://github.com/iree-org/iree/actions/runs/41644460192/job/125950505627) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [1h02m](https://github.com/iree-org/iree/actions/runs/41645995117/job/125955353346) | [1h15m](https://github.com/iree-org/iree/actions/runs/41677356641/job/126068129277) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [18m08s](https://github.com/iree-org/iree/actions/runs/41683259826/job/126090725689) | [1h08m](https://github.com/iree-org/iree/actions/runs/41648098980/job/125963970768) | 0% (0/4) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 18 | 0 | — | — | 0 | [28m17s](https://github.com/iree-org/iree/actions/runs/41677356641/job/126068129212) | [1h02m](https://github.com/iree-org/iree/actions/runs/41652530758/job/125979237087) | 0% (0/8) | `shark55-ci`, `shark75-ci` |
| `ubuntu-24.04-arm` | github-hosted | 27 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/41652530962/job/125974277765) | [3m35s](https://github.com/iree-org/iree/actions/runs/41677324988/job/126063085919) | 0% (0/9) | 27 |
| `macos-15` | github-hosted | 27 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/41680997773/job/126074453256) | [2m23s](https://github.com/iree-org/iree/actions/runs/41677324988/job/126063085870) | 11% (1/9) | 27 |
| `windows-2022` | github-hosted | 27 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/41683259933/job/126082411333) | [2m12s](https://github.com/iree-org/iree/actions/runs/41683259933/job/126082411334) | 0% (0/9) | 27 |
| `azure-linux-scale` | ossci | 57 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/41677356683/job/126061606342) | [1m34s](https://github.com/iree-org/iree/actions/runs/41683259933/job/126082412000) | 0% (0/21) | 54 |
| `ubuntu-24.04` | github-hosted | 232 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/41677356683/job/126093489974) | [1m10s](https://github.com/iree-org/iree/actions/runs/41683259933/job/126082411053) | 1% (1/73) | 219 |
| `azure-windows-scale` | ossci | 9 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/41677356683/job/126061606297) | [12s](https://github.com/iree-org/iree/actions/runs/41648098977/job/125958797089) | 0% (0/3) | 9 |
| `ubuntu-latest` | github-hosted | 27 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/41683258141/job/126082193941) | [9s](https://github.com/iree-org/iree/actions/runs/41675132456/job/126053602936) | 0% (0/9) | 27 |
| `Linux,X64,iree-w7900` | self-hosted | 9 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 9 | 0 | — | — | [1h57m](https://github.com/iree-org/iree/actions/runs/41683259826/job/126090725647) | [4h04m](https://github.com/iree-org/iree/actions/runs/41648098980/job/125963971178) | [4h04m](https://github.com/iree-org/iree/actions/runs/41648098980/job/125963971178) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [2h03m](https://github.com/iree-org/iree/actions/runs/41683259826/job/126090725844) | [4h02m](https://github.com/iree-org/iree/actions/runs/41652530758/job/125979237587) | [4h02m](https://github.com/iree-org/iree/actions/runs/41652530758/job/125979237587) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 9 | 0 | — | — | [2h13m](https://github.com/iree-org/iree/actions/runs/41677356641/job/126068129411) | [3h54m](https://github.com/iree-org/iree/actions/runs/41644460192/job/125950505795) | [3h54m](https://github.com/iree-org/iree/actions/runs/41644460192/job/125950505795) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [1h49m](https://github.com/iree-org/iree/actions/runs/41677324958/job/126066577884) | [3h46m](https://github.com/iree-org/iree/actions/runs/41652530758/job/125979237273) | [3h46m](https://github.com/iree-org/iree/actions/runs/41652530758/job/125979237273) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [2h18m](https://github.com/iree-org/iree/actions/runs/41677356641/job/126068129439) | [3h42m](https://github.com/iree-org/iree/actions/runs/41644460192/job/125950505712) | [3h42m](https://github.com/iree-org/iree/actions/runs/41644460192/job/125950505712) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [1h45m](https://github.com/iree-org/iree/actions/runs/41652530758/job/125979237343) | [2h23m](https://github.com/iree-org/iree/actions/runs/41644460192/job/125950505735) | [2h23m](https://github.com/iree-org/iree/actions/runs/41644460192/job/125950505735) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 9 | 0 | — | — | [24m02s](https://github.com/iree-org/iree/actions/runs/41645995117/job/125955353386) | [2h04m](https://github.com/iree-org/iree/actions/runs/41644460192/job/125950505627) | [2h04m](https://github.com/iree-org/iree/actions/runs/41644460192/job/125950505627) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [31m55s](https://github.com/iree-org/iree/actions/runs/41648098980/job/125963970642) | [1h53m](https://github.com/iree-org/iree/actions/runs/41645995117/job/125955353294) | [1h53m](https://github.com/iree-org/iree/actions/runs/41645995117/job/125955353294) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 9 | 0 | — | — | [1h02m](https://github.com/iree-org/iree/actions/runs/41645995117/job/125955353346) | [1h15m](https://github.com/iree-org/iree/actions/runs/41677356641/job/126068129277) | [1h15m](https://github.com/iree-org/iree/actions/runs/41677356641/job/126068129277) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 9 | 0 | — | — | [18m08s](https://github.com/iree-org/iree/actions/runs/41683259826/job/126090725689) | [1h08m](https://github.com/iree-org/iree/actions/runs/41648098980/job/125963970768) | [1h08m](https://github.com/iree-org/iree/actions/runs/41648098980/job/125963970768) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [24m08s](https://github.com/iree-org/iree/actions/runs/41681070475/job/126081328566) | [37m48s](https://github.com/iree-org/iree/actions/runs/41645995117/job/125955353573) | [37m48s](https://github.com/iree-org/iree/actions/runs/41645995117/job/125955353573) | 2 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 9 | 0 | — | — | [57s](https://github.com/iree-org/iree/actions/runs/41645995401/job/125951462808) | [7m24s](https://github.com/iree-org/iree/actions/runs/41648098977/job/125958796557) | [7m24s](https://github.com/iree-org/iree/actions/runs/41648098977/job/125958796557) | 8 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41683259933/job/126082411060) | [4m32s](https://github.com/iree-org/iree/actions/runs/41677324988/job/126063085866) | [4m32s](https://github.com/iree-org/iree/actions/runs/41677324988/job/126063085866) | 9 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 13 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/41652530962/job/125974277266) | [4m18s](https://github.com/iree-org/iree/actions/runs/41677324988/job/126063086014) | [4m18s](https://github.com/iree-org/iree/actions/runs/41677324988/job/126063086014) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 9 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/41677356683/job/126061605561) | [4m17s](https://github.com/iree-org/iree/actions/runs/41677324988/job/126063085962) | [4m17s](https://github.com/iree-org/iree/actions/runs/41677324988/job/126063085962) | 9 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 9 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/41652530962/job/125974277765) | [4m02s](https://github.com/iree-org/iree/actions/runs/41677324988/job/126063085912) | [4m02s](https://github.com/iree-org/iree/actions/runs/41677324988/job/126063085912) | 9 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 9 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/41648098977/job/125958796531) | [3m53s](https://github.com/iree-org/iree/actions/runs/41677324988/job/126063085910) | [3m53s](https://github.com/iree-org/iree/actions/runs/41677324988/job/126063085910) | 9 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 9 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/41675137130/job/126053829171) | [3m35s](https://github.com/iree-org/iree/actions/runs/41677324988/job/126063085919) | [3m35s](https://github.com/iree-org/iree/actions/runs/41677324988/job/126063085919) | 9 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41681070469/job/126075616662) | [2m59s](https://github.com/iree-org/iree/actions/runs/41677324988/job/126063085991) | [2m59s](https://github.com/iree-org/iree/actions/runs/41677324988/job/126063085991) | 9 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 9 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/41652530962/job/125974278264) | [2m53s](https://github.com/iree-org/iree/actions/runs/41683259933/job/126082412304) | [2m53s](https://github.com/iree-org/iree/actions/runs/41683259933/job/126082412304) | 9 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 532 | 2% (12/532) |  | 3h48m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 442 | 2% (10/442) |  | 4h43m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h08m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 3h42m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h15m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 3h08m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h04m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 3h54m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h02m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
