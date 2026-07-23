# iree-ci-monitor

_Updated: 2026-07-23 11:44 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 9 | 1 | [2h17m](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530616) | 2026-07-23 11:43 PDT | 1 | [1h03m](https://github.com/iree-org/iree/actions/runs/30006927060/job/89207254808) | [2h14m](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444471) | 0% (0/2) | 7 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 9 | 0 | — | — | 0 | [12m57s](https://github.com/iree-org/iree/actions/runs/30006927060/job/89207255069) | [55m25s](https://github.com/iree-org/iree/actions/runs/30010209153/job/89222397303) | 0% (0/2) | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 18 | 0 | — | — | 0 | [14m33s](https://github.com/iree-org/iree/actions/runs/29996688577/job/89176631299) | [54m04s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444355) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 9 | 0 | — | — | 0 | [10m18s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262811943) | [50m12s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444149) | 50% (1/2) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 18 | 0 | — | — | 0 | [8m22s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530797) | [35m40s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444369) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [9m30s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812371) | [30m39s](https://github.com/iree-org/iree/actions/runs/30002106503/job/89193872457) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 9 | 0 | — | — | 0 | [6m43s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812234) | [30m14s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444229) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30006927060/job/89207254819) | [25m01s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444244) | 0% (0/2) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [17m55s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444274) | [23m12s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530732) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 18 | 0 | — | — | 0 | [8m36s](https://github.com/iree-org/iree/actions/runs/29996688577/job/89176631339) | [22m36s](https://github.com/iree-org/iree/actions/runs/30006927060/job/89207255057) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [5m19s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530739) | [13m22s](https://github.com/iree-org/iree/actions/runs/30010209153/job/89222397355) | 0% (0/2) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 18 | 0 | — | — | 0 | [30s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444548) | [6m54s](https://github.com/iree-org/iree/actions/runs/30006927060/job/89207255073) | 25% (1/4) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `azure-linux-scale` | ossci | 44 | 0 | — | — | 0 | [18s](https://github.com/iree-org/iree/actions/runs/30010209153/job/89216101276) | [1m51s](https://github.com/iree-org/iree/actions/runs/30002106611/job/89192144477) | 0% (0/15) | 43 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m28s](https://github.com/iree-org/iree/actions/runs/29997780810/job/89175466408) | [1m28s](https://github.com/iree-org/iree/actions/runs/29997780810/job/89175466408) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 21 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30012453878/job/89223823756) | [52s](https://github.com/iree-org/iree/actions/runs/30006926999/job/89205092445) | 0% (0/6) | 21 |
| `ubuntu-latest` | github-hosted | 30 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30012452956/job/89223781689) | [47s](https://github.com/iree-org/iree/actions/runs/30002974122/job/89192264799) | 0% (0/9) | 30 |
| `windows-2022` | github-hosted | 21 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30010208956/job/89216115020) | [5s](https://github.com/iree-org/iree/actions/runs/30012453878/job/89223823801) | 0% (0/6) | 21 |
| `ubuntu-24.04` | github-hosted | 168 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530772) | [4s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444118) | 7% (3/41) | 156 |
| `macos-14` | github-hosted | 22 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30002106611/job/89192144123) | [4s](https://github.com/iree-org/iree/actions/runs/30023956159/job/89264398844) | 0% (0/7) | 22 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30006927060/job/89207254881) | [3s](https://github.com/iree-org/iree/actions/runs/29996688577/job/89176631126) | 0% (0/2) | `iree-mi308-1` |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/29997758111/job/89175391254) | [3s](https://github.com/iree-org/iree/actions/runs/29997758111/job/89175391254) | 0% (0/1) | 1 |
| `azure-windows-scale` | ossci | 7 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29996688366/job/89171974311) | [2s](https://github.com/iree-org/iree/actions/runs/30023956159/job/89264399225) | 0% (0/2) | 7 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [2h17m](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530616) | 2026-07-23 11:43 PDT | `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | `llvmcpu-stack-check-overflow` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI325 / test_mi325 | `linux-mi325-1gpu-ossci-iree-org` | 9 | 1 | [2h17m](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530616) | 2026-07-23 11:43 PDT | [1h03m](https://github.com/iree-org/iree/actions/runs/30006927060/job/89207254808) | [2h14m](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444471) | [2h14m](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444471) | 7 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [18m39s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530868) | [1h04m](https://github.com/iree-org/iree/actions/runs/30010209153/job/89222397307) | [1h04m](https://github.com/iree-org/iree/actions/runs/30010209153/job/89222397307) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 9 | 0 | — | — | [12m57s](https://github.com/iree-org/iree/actions/runs/30006927060/job/89207255069) | [55m25s](https://github.com/iree-org/iree/actions/runs/30010209153/job/89222397303) | [55m25s](https://github.com/iree-org/iree/actions/runs/30010209153/job/89222397303) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 9 | 0 | — | — | [10m18s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262811943) | [50m12s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444149) | [50m12s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444149) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 9 | 0 | — | — | [14m33s](https://github.com/iree-org/iree/actions/runs/29996688577/job/89176631299) | [39m52s](https://github.com/iree-org/iree/actions/runs/30010209153/job/89222397321) | [39m52s](https://github.com/iree-org/iree/actions/runs/30010209153/job/89222397321) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 9 | 0 | — | — | [9m33s](https://github.com/iree-org/iree/actions/runs/30002106503/job/89193872734) | [37m52s](https://github.com/iree-org/iree/actions/runs/30010209153/job/89222397511) | [37m52s](https://github.com/iree-org/iree/actions/runs/30010209153/job/89222397511) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [7m06s](https://github.com/iree-org/iree/actions/runs/29996688577/job/89176631300) | [33m59s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444377) | [33m59s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444377) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 9 | 0 | — | — | [9m30s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812371) | [30m39s](https://github.com/iree-org/iree/actions/runs/30002106503/job/89193872457) | [30m39s](https://github.com/iree-org/iree/actions/runs/30002106503/job/89193872457) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 9 | 0 | — | — | [6m43s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812234) | [30m14s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444229) | [30m14s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444229) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 9 | 0 | — | — | [8m22s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530797) | [28m35s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444279) | [28m35s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444279) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30006927060/job/89207254819) | [25m01s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444244) | [25m01s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444244) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 9 | 0 | — | — | [17m55s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444274) | [23m12s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530732) | [23m12s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530732) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 9 | 0 | — | — | [9m34s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530792) | [18m00s](https://github.com/iree-org/iree/actions/runs/30002106503/job/89193872626) | [18m00s](https://github.com/iree-org/iree/actions/runs/30002106503/job/89193872626) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 9 | 0 | — | — | [5m19s](https://github.com/iree-org/iree/actions/runs/30023955255/job/89267530739) | [13m22s](https://github.com/iree-org/iree/actions/runs/30010209153/job/89222397355) | [13m22s](https://github.com/iree-org/iree/actions/runs/30010209153/job/89222397355) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [30s](https://github.com/iree-org/iree/actions/runs/30012453834/job/89226444548) | [7m48s](https://github.com/iree-org/iree/actions/runs/30010209153/job/89222397454) | [7m48s](https://github.com/iree-org/iree/actions/runs/30010209153/job/89222397454) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [2m44s](https://github.com/iree-org/iree/actions/runs/30020119572/job/89262812350) | [6m54s](https://github.com/iree-org/iree/actions/runs/30006927060/job/89207255073) | [6m54s](https://github.com/iree-org/iree/actions/runs/30006927060/job/89207255073) | 3 |
| `.github/workflows/ci_linux_x64_clang_tsan.yml` | linux_x64_clang_tsan | `azure-linux-scale` | 1 | 0 | — | — | [2m39s](https://github.com/iree-org/iree/actions/runs/29997780364/job/89175464644) | [2m39s](https://github.com/iree-org/iree/actions/runs/29997780364/job/89175464644) | [2m39s](https://github.com/iree-org/iree/actions/runs/29997780364/job/89175464644) | 1 |
| `.github/workflows/ci_linux_x64_clang_debug.yml` | linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [2m38s](https://github.com/iree-org/iree/actions/runs/29997733810/job/89175310860) | [2m38s](https://github.com/iree-org/iree/actions/runs/29997733810/job/89175310860) | [2m38s](https://github.com/iree-org/iree/actions/runs/29997733810/job/89175310860) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 7 | 0 | — | — | [19s](https://github.com/iree-org/iree/actions/runs/30020118178/job/89260477394) | [1m51s](https://github.com/iree-org/iree/actions/runs/30002106611/job/89192144477) | [1m51s](https://github.com/iree-org/iree/actions/runs/30002106611/job/89192144477) | 7 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 7 | 0 | — | — | [18s](https://github.com/iree-org/iree/actions/runs/30020118178/job/89260477307) | [1m40s](https://github.com/iree-org/iree/actions/runs/30006926999/job/89205092646) | [1m40s](https://github.com/iree-org/iree/actions/runs/30006926999/job/89205092646) | 7 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 413 | 1% (4/413) |  | 1h43m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 311 | 1% (2/311) |  | 1h57m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 328 | 4% (14/328) |  | 1h59m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 320 | 1% (4/320) |  | 1h59m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 95 | 1% (1/95) |  | 2h06m ago |

## Alerts

- **[stale-queued]** `linux-mi325-1gpu-ossci-iree-org` oldest queued job observed waiting 2h17m (> 2h00m)
- **[queue-starved]** `linux-mi325-1gpu-ossci-iree-org` p95 queue 2h14m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
