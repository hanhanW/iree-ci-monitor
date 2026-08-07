# iree-ci-monitor

_Updated: 2026-08-07 12:18 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 12 | 0 | — | — | 0 | [18m54s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196270) | [1h12m](https://github.com/iree-org/iree/actions/runs/31188713140/job/92912380334) | 0% (0/5) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 12 | 0 | — | — | 0 | [21m35s](https://github.com/iree-org/iree/actions/runs/31188713140/job/92912380187) | [41m50s](https://github.com/iree-org/iree/actions/runs/31193504174/job/92918099718) | 0% (0/5) | `shark75-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 12 | 0 | — | — | 0 | [10m51s](https://github.com/iree-org/iree/actions/runs/31188713140/job/92912379758) | [33m57s](https://github.com/iree-org/iree/actions/runs/31183205110/job/92889731516) | 20% (1/5) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 12 | 0 | — | — | 0 | [8m29s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622253) | [26m23s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196312) | 0% (0/5) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 12 | 0 | — | — | 0 | [17m17s](https://github.com/iree-org/iree/actions/runs/31191826101/job/92913470538) | [26m10s](https://github.com/iree-org/iree/actions/runs/31193504174/job/92918099359) | 0% (0/5) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 24 | 0 | — | — | 1 | [9m54s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622203) | [23m32s](https://github.com/iree-org/iree/actions/runs/31186595156/job/92894868200) | 11% (1/9) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 24 | 0 | — | — | 0 | [11m51s](https://github.com/iree-org/iree/actions/runs/31195612648/job/92925376551) | [22m42s](https://github.com/iree-org/iree/actions/runs/31186595156/job/92894868109) | 0% (0/10) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 24 | 0 | — | — | 0 | [13m01s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511465) | [22m26s](https://github.com/iree-org/iree/actions/runs/31193504174/job/92918099660) | 0% (0/10) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 12 | 0 | — | — | 0 | [8m07s](https://github.com/iree-org/iree/actions/runs/31195612648/job/92925376414) | [21m56s](https://github.com/iree-org/iree/actions/runs/31186595156/job/92894868030) | 80% (4/5) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 24 | 0 | — | — | 0 | [4m59s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622316) | [20m14s](https://github.com/iree-org/iree/actions/runs/31186595156/job/92894868151) | 0% (0/10) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 12 | 0 | — | — | 0 | [2m58s](https://github.com/iree-org/iree/actions/runs/31193504174/job/92918099576) | [19m50s](https://github.com/iree-org/iree/actions/runs/31186595156/job/92894867973) | 0% (0/5) | `shark75-ci` |
| `azure-linux-scale` | ossci | 71 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/31178720584/job/92867099910) | [2m49s](https://github.com/iree-org/iree/actions/runs/31188310499/job/92898449227) | 0% (0/33) | 70 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m23s](https://github.com/iree-org/iree/actions/runs/31166488477/job/92828382266) | [1m23s](https://github.com/iree-org/iree/actions/runs/31166488477/job/92828382266) | 0% (0/1) | 1 |
| `macos-14` | github-hosted | 37 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31191826872/job/92910311239) | [11s](https://github.com/iree-org/iree/actions/runs/31193501181/job/92916052911) | 0% (0/16) | 37 |
| `ubuntu-24.04` | github-hosted | 246 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31188310499/job/92898448705) | [9s](https://github.com/iree-org/iree/actions/runs/31193501181/job/92915948599) | 3% (3/93) | 232 |
| `ubuntu-latest` | github-hosted | 42 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31183201205/job/92881277612) | [9s](https://github.com/iree-org/iree/actions/runs/31200171742/job/92938023758) | 0% (0/15) | 42 |
| `ubuntu-24.04-arm` | github-hosted | 36 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31200173451/job/92938111302) | [6s](https://github.com/iree-org/iree/actions/runs/31176929305/job/92860922877) | 0% (0/15) | 36 |
| `windows-2022` | github-hosted | 36 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31188310499/job/92898448864) | [4s](https://github.com/iree-org/iree/actions/runs/31198986139/job/92934155393) | 0% (0/15) | 36 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/31166457150/job/92828289146) | [3s](https://github.com/iree-org/iree/actions/runs/31166457150/job/92828289146) | 0% (0/1) | 1 |
| `azure-windows-scale` | ossci | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/31186595035/job/92892641399) | [2s](https://github.com/iree-org/iree/actions/runs/31198986139/job/92934155917) | 0% (0/5) | 12 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 12 | 0 | — | — | [18m54s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196270) | [1h12m](https://github.com/iree-org/iree/actions/runs/31188713140/job/92912380334) | [1h12m](https://github.com/iree-org/iree/actions/runs/31188713140/job/92912380334) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 12 | 0 | — | — | [21m35s](https://github.com/iree-org/iree/actions/runs/31188713140/job/92912380187) | [41m50s](https://github.com/iree-org/iree/actions/runs/31193504174/job/92918099718) | [41m50s](https://github.com/iree-org/iree/actions/runs/31193504174/job/92918099718) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 12 | 0 | — | — | [15m53s](https://github.com/iree-org/iree/actions/runs/31188311359/job/92907309043) | [34m28s](https://github.com/iree-org/iree/actions/runs/31183205110/job/92889731697) | [34m28s](https://github.com/iree-org/iree/actions/runs/31183205110/job/92889731697) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 12 | 0 | — | — | [10m51s](https://github.com/iree-org/iree/actions/runs/31188713140/job/92912379758) | [33m57s](https://github.com/iree-org/iree/actions/runs/31183205110/job/92889731516) | [33m57s](https://github.com/iree-org/iree/actions/runs/31183205110/job/92889731516) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 12 | 0 | — | — | [8m13s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511456) | [31m41s](https://github.com/iree-org/iree/actions/runs/31183205110/job/92889731776) | [31m41s](https://github.com/iree-org/iree/actions/runs/31183205110/job/92889731776) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 12 | 0 | — | — | [15m36s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196496) | [28m06s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511507) | [28m06s](https://github.com/iree-org/iree/actions/runs/31198986031/job/92936511507) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 12 | 0 | — | — | [6m08s](https://github.com/iree-org/iree/actions/runs/31183205110/job/92889731602) | [27m53s](https://github.com/iree-org/iree/actions/runs/31188713140/job/92912380169) | [27m53s](https://github.com/iree-org/iree/actions/runs/31188713140/job/92912380169) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 12 | 0 | — | — | [8m29s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622253) | [26m23s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196312) | [26m23s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92940196312) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 12 | 0 | — | — | [17m17s](https://github.com/iree-org/iree/actions/runs/31191826101/job/92913470538) | [26m10s](https://github.com/iree-org/iree/actions/runs/31193504174/job/92918099359) | [26m10s](https://github.com/iree-org/iree/actions/runs/31193504174/job/92918099359) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 12 | 0 | — | — | [8m23s](https://github.com/iree-org/iree/actions/runs/31188311359/job/92907308871) | [22m42s](https://github.com/iree-org/iree/actions/runs/31186595156/job/92894868109) | [22m42s](https://github.com/iree-org/iree/actions/runs/31186595156/job/92894868109) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 12 | 0 | — | — | [11m02s](https://github.com/iree-org/iree/actions/runs/31176927766/job/92862625339) | [22m16s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622297) | [22m16s](https://github.com/iree-org/iree/actions/runs/31178720794/job/92868622297) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 12 | 0 | — | — | [8m07s](https://github.com/iree-org/iree/actions/runs/31195612648/job/92925376414) | [21m56s](https://github.com/iree-org/iree/actions/runs/31186595156/job/92894868030) | [21m56s](https://github.com/iree-org/iree/actions/runs/31186595156/job/92894868030) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 12 | 0 | — | — | [2m58s](https://github.com/iree-org/iree/actions/runs/31193504174/job/92918099576) | [19m50s](https://github.com/iree-org/iree/actions/runs/31186595156/job/92894867973) | [19m50s](https://github.com/iree-org/iree/actions/runs/31186595156/job/92894867973) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 12 | 0 | — | — | [1m51s](https://github.com/iree-org/iree/actions/runs/31193504174/job/92918099749) | [15m45s](https://github.com/iree-org/iree/actions/runs/31183205110/job/92889731821) | [15m45s](https://github.com/iree-org/iree/actions/runs/31183205110/job/92889731821) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 12 | 0 | — | — | [11m56s](https://github.com/iree-org/iree/actions/runs/31188713140/job/92912380142) | [14m46s](https://github.com/iree-org/iree/actions/runs/31191826101/job/92913470715) | [23m32s](https://github.com/iree-org/iree/actions/runs/31186595156/job/92894868200) | 4 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 13 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/31200173112/job/92938078471) | [3m00s](https://github.com/iree-org/iree/actions/runs/31180795081/job/92873391235) | [4m09s](https://github.com/iree-org/iree/actions/runs/31191826101/job/92910325091) | 12 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 12 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/31186595035/job/92892641174) | [2m29s](https://github.com/iree-org/iree/actions/runs/31188310499/job/92898449332) | [4m10s](https://github.com/iree-org/iree/actions/runs/31191826872/job/92910311308) | 12 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 7 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/31200173451/job/92938111350) | [1m56s](https://github.com/iree-org/iree/actions/runs/31180795090/job/92873380408) | [1m56s](https://github.com/iree-org/iree/actions/runs/31180795090/job/92873380408) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 12 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/31188713531/job/92903116904) | [1m44s](https://github.com/iree-org/iree/actions/runs/31180795090/job/92873380406) | [2m49s](https://github.com/iree-org/iree/actions/runs/31188310499/job/92898449227) | 12 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 12 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/31186595035/job/92892641377) | [1m42s](https://github.com/iree-org/iree/actions/runs/31188310499/job/92898449140) | [2m47s](https://github.com/iree-org/iree/actions/runs/31180795090/job/92873380303) | 12 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 143 | 3% (4/142) | yes | running |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 153 | 4% (6/153) |  | 1h39m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 181 | 0% (0/181) |  | 1h49m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 137 | 4% (5/137) |  | 1h53m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 13 | 0% (0/13) |  | 4d06h ago |

## Alerts

- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h12m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
