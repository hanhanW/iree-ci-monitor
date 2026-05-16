# iree-ci-monitor

_Updated: 2026-05-15 18:11 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 33 | 0 | — | — | 0 | [1h40m](https://github.com/iree-org/iree/actions/runs/25937781487/job/76249098067) | [5h12m](https://github.com/iree-org/iree/actions/runs/25927827699/job/76215193176) | 0% (0/8) | `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 33 | 0 | — | — | 0 | [1h52m](https://github.com/iree-org/iree/actions/runs/25930824449/job/76227257809) | [4h55m](https://github.com/iree-org/iree/actions/runs/25929095028/job/76221241362) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 66 | 0 | — | — | 1 | [1h29m](https://github.com/iree-org/iree/actions/runs/25930825839/job/76231258343) | [4h21m](https://github.com/iree-org/iree/actions/runs/25930437544/job/76224047010) | 0% (0/15) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 33 | 0 | — | — | 0 | [42m58s](https://github.com/iree-org/iree/actions/runs/25937780373/job/76249297464) | [4h17m](https://github.com/iree-org/iree/actions/runs/25929095028/job/76221241326) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 33 | 0 | — | — | 0 | [42m47s](https://github.com/iree-org/iree/actions/runs/25924583203/job/76208222819) | [2h46m](https://github.com/iree-org/iree/actions/runs/25933209813/job/76233311997) | 0% (0/8) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 33 | 0 | — | — | 0 | [1h04m](https://github.com/iree-org/iree/actions/runs/25937662477/job/76248392643) | [2h31m](https://github.com/iree-org/iree/actions/runs/25924583203/job/76208222835) | 0% (0/8) | `shark01-ci`, `shark10-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 66 | 0 | — | — | 0 | [25m21s](https://github.com/iree-org/iree/actions/runs/25937662477/job/76248392725) | [2h25m](https://github.com/iree-org/iree/actions/runs/25930437544/job/76224047016) | 6% (1/16) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 66 | 0 | — | — | 0 | [38m59s](https://github.com/iree-org/iree/actions/runs/25937780373/job/76249297635) | [2h20m](https://github.com/iree-org/iree/actions/runs/25930437544/job/76224047050) | 0% (0/16) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,rdna3` | self-hosted | 66 | 0 | — | — | 0 | [34m01s](https://github.com/iree-org/iree/actions/runs/25930827522/job/76227430760) | [2h16m](https://github.com/iree-org/iree/actions/runs/25927827699/job/76215193195) | 0% (0/16) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-w7900` | self-hosted | 33 | 0 | — | — | 0 | [39m11s](https://github.com/iree-org/iree/actions/runs/25924583203/job/76208222779) | [2h14m](https://github.com/iree-org/iree/actions/runs/25930823348/job/76229143243) | 0% (0/8) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 33 | 0 | — | — | 0 | [28m08s](https://github.com/iree-org/iree/actions/runs/25924583203/job/76208223117) | [1h02m](https://github.com/iree-org/iree/actions/runs/25930824449/job/76227257815) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 33 | 0 | — | — | 0 | [15m04s](https://github.com/iree-org/iree/actions/runs/25937782590/job/76248991374) | [48m33s](https://github.com/iree-org/iree/actions/runs/25927851485/job/76215782703) | 0% (0/8) | `iree-mi308-1` |
| `ubuntu-24.04` | github-hosted | 690 | 2 | [4h53m](https://github.com/iree-org/iree/actions/runs/25907295889/job/76143183087) | 2026-05-15 05:58 PDT | 2 | [1m26s](https://github.com/iree-org/iree/actions/runs/25927827245/job/76213720959) | [18m29s](https://github.com/iree-org/iree/actions/runs/25927854359/job/76216351234) | 8% (11/144) | 677 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 132 | 0 | — | — | 0 | [19s](https://github.com/iree-org/iree/actions/runs/25947076207/job/76277904237) | [18m12s](https://github.com/iree-org/iree/actions/runs/25927851485/job/76215782693) | 3% (1/32) | 132 |
| `ubuntu-24.04-arm` | github-hosted | 111 | 0 | — | — | 0 | [1m16s](https://github.com/iree-org/iree/actions/runs/25937662488/job/76247239814) | [15m00s](https://github.com/iree-org/iree/actions/runs/25930827451/job/76225624013) | 0% (0/24) | 106 |
| `macos-14` | github-hosted | 113 | 0 | — | — | 0 | [1m21s](https://github.com/iree-org/iree/actions/runs/25938905551/job/76252118872) | [13m47s](https://github.com/iree-org/iree/actions/runs/25930822811/job/76225162443) | 0% (0/24) | 107 |
| `windows-2022` | github-hosted | 111 | 0 | — | — | 0 | [1m17s](https://github.com/iree-org/iree/actions/runs/25937662488/job/76247239822) | [12m38s](https://github.com/iree-org/iree/actions/runs/25930827451/job/76225623979) | 0% (0/24) | 110 |
| `ubuntu-latest` | github-hosted | 72 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/25935701372/job/76240461598) | [4m47s](https://github.com/iree-org/iree/actions/runs/25938903407/job/76251278498) | 0% (0/21) | 72 |
| `azure-windows-scale` | ossci | 37 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/25946808975/job/76276467239) | [4m38s](https://github.com/iree-org/iree/actions/runs/25927853528/job/76214542247) | 0% (0/8) | 37 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 33 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/25930823348/job/76229143244) | [2m24s](https://github.com/iree-org/iree/actions/runs/25927857171/job/76215678405) | 0% (0/8) | 33 |
| `azure-linux-scale` | ossci | 195 | 1 | [19m47s](https://github.com/iree-org/iree/actions/runs/25783793136/job/75732425036) | 2026-05-13 00:23 PDT | 1 | [9s](https://github.com/iree-org/iree/actions/runs/25943815981/job/76267452296) | [2m04s](https://github.com/iree-org/iree/actions/runs/25937635101/job/76247036909) | 4% (2/47) | 194 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 2 | 0 | — | — | 0 | [1m34s](https://github.com/iree-org/iree/actions/runs/25941195081/job/76259023177) | [1m37s](https://github.com/iree-org/iree/actions/runs/25927729407/job/76215278111) | — | 2 |
| `macos-15-intel` | github-hosted | 2 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/25941195081/job/76259023128) | [32s](https://github.com/iree-org/iree/actions/runs/25927729407/job/76215278190) | — | 2 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [4h53m](https://github.com/iree-org/iree/actions/runs/25907295889/job/76143183087) | 2026-05-15 05:58 PDT | `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | `users/keshavvinayak01/gpuvectoralloc-swizzle` | pull_request |
| [4h53m](https://github.com/iree-org/iree/actions/runs/25907295886/job/76143196900) | 2026-05-15 05:58 PDT | `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | `users/keshavvinayak01/gpuvectoralloc-swizzle` | pull_request |
| [19m47s](https://github.com/iree-org/iree/actions/runs/25783793136/job/75732425036) | 2026-05-13 00:23 PDT | `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 33 | 0 | — | — | [1h40m](https://github.com/iree-org/iree/actions/runs/25937781487/job/76249098067) | [5h12m](https://github.com/iree-org/iree/actions/runs/25927827699/job/76215193176) | [6h19m](https://github.com/iree-org/iree/actions/runs/25924583203/job/76208223020) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 33 | 0 | — | — | [1h52m](https://github.com/iree-org/iree/actions/runs/25930824449/job/76227257809) | [4h55m](https://github.com/iree-org/iree/actions/runs/25929095028/job/76221241362) | [6h14m](https://github.com/iree-org/iree/actions/runs/25924583203/job/76208222987) | 1 |
| `.github/workflows/lint.yml` | pre-commit | `ubuntu-24.04` | 30 | 1 | [4h53m](https://github.com/iree-org/iree/actions/runs/25907295889/job/76143183087) | 2026-05-15 05:58 PDT | [34s](https://github.com/iree-org/iree/actions/runs/25927856989/job/76213826160) | [5m50s](https://github.com/iree-org/iree/actions/runs/25930824306/job/76223949023) | [12m44s](https://github.com/iree-org/iree/actions/runs/25930823238/job/76223945709) | 29 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 38 | 1 | [4h53m](https://github.com/iree-org/iree/actions/runs/25907295886/job/76143196900) | 2026-05-15 05:58 PDT | [4m53s](https://github.com/iree-org/iree/actions/runs/25927827551/job/76213953396) | [22m14s](https://github.com/iree-org/iree/actions/runs/25927854102/job/76216593979) | [24m58s](https://github.com/iree-org/iree/actions/runs/25937781464/job/76247561242) | 35 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 33 | 0 | — | — | [1h12m](https://github.com/iree-org/iree/actions/runs/25930822823/job/76227335915) | [4h45m](https://github.com/iree-org/iree/actions/runs/25930437544/job/76224047109) | [4h45m](https://github.com/iree-org/iree/actions/runs/25924583203/job/76208223043) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 33 | 0 | — | — | [42m58s](https://github.com/iree-org/iree/actions/runs/25937780373/job/76249297464) | [4h17m](https://github.com/iree-org/iree/actions/runs/25929095028/job/76221241326) | [5h28m](https://github.com/iree-org/iree/actions/runs/25924583203/job/76208222765) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 33 | 0 | — | — | [1h39m](https://github.com/iree-org/iree/actions/runs/25937781487/job/76249097984) | [4h05m](https://github.com/iree-org/iree/actions/runs/25924583203/job/76208222937) | [4h21m](https://github.com/iree-org/iree/actions/runs/25930437544/job/76224047010) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 33 | 0 | — | — | [42m47s](https://github.com/iree-org/iree/actions/runs/25924583203/job/76208222819) | [2h46m](https://github.com/iree-org/iree/actions/runs/25933209813/job/76233311997) | [4h38m](https://github.com/iree-org/iree/actions/runs/25927827699/job/76215193188) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 33 | 0 | — | — | [35m37s](https://github.com/iree-org/iree/actions/runs/25938905649/job/76253308148) | [2h46m](https://github.com/iree-org/iree/actions/runs/25930437544/job/76224047331) | [3h00m](https://github.com/iree-org/iree/actions/runs/25929095028/job/76221241678) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 33 | 0 | — | — | [1h04m](https://github.com/iree-org/iree/actions/runs/25937662477/job/76248392643) | [2h31m](https://github.com/iree-org/iree/actions/runs/25924583203/job/76208222835) | [3h41m](https://github.com/iree-org/iree/actions/runs/25930822823/job/76227335746) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 33 | 0 | — | — | [23m58s](https://github.com/iree-org/iree/actions/runs/25930824449/job/76227257844) | [2h29m](https://github.com/iree-org/iree/actions/runs/25929095028/job/76221241363) | [3h20m](https://github.com/iree-org/iree/actions/runs/25924583203/job/76208223046) | 4 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 33 | 0 | — | — | [38m59s](https://github.com/iree-org/iree/actions/runs/25937780373/job/76249297635) | [2h20m](https://github.com/iree-org/iree/actions/runs/25930437544/job/76224047050) | [2h54m](https://github.com/iree-org/iree/actions/runs/25927827699/job/76215193257) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD W7900 / test_w7900 | `Linux,X64,iree-w7900` | 33 | 0 | — | — | [39m11s](https://github.com/iree-org/iree/actions/runs/25924583203/job/76208222779) | [2h14m](https://github.com/iree-org/iree/actions/runs/25930823348/job/76229143243) | [2h50m](https://github.com/iree-org/iree/actions/runs/25933209813/job/76233311955) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 33 | 0 | — | — | [27m15s](https://github.com/iree-org/iree/actions/runs/25937662477/job/76248392708) | [1h42m](https://github.com/iree-org/iree/actions/runs/25930437544/job/76224046884) | [2h58m](https://github.com/iree-org/iree/actions/runs/25927827699/job/76215193295) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 33 | 0 | — | — | [26m44s](https://github.com/iree-org/iree/actions/runs/25936373194/job/76244610673) | [1h37m](https://github.com/iree-org/iree/actions/runs/25937662477/job/76248392701) | [2h16m](https://github.com/iree-org/iree/actions/runs/25927827699/job/76215193195) | 3 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 33 | 0 | — | — | [40m36s](https://github.com/iree-org/iree/actions/runs/25924583203/job/76208222896) | [1h33m](https://github.com/iree-org/iree/actions/runs/25930827522/job/76227430750) | [3h06m](https://github.com/iree-org/iree/actions/runs/25927729409/job/76216230754) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 33 | 0 | — | — | [28m08s](https://github.com/iree-org/iree/actions/runs/25924583203/job/76208223117) | [1h02m](https://github.com/iree-org/iree/actions/runs/25930824449/job/76227257815) | [1h05m](https://github.com/iree-org/iree/actions/runs/25933372346/job/76233941162) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 33 | 0 | — | — | [15m04s](https://github.com/iree-org/iree/actions/runs/25937782590/job/76248991374) | [48m33s](https://github.com/iree-org/iree/actions/runs/25927851485/job/76215782703) | [1h13m](https://github.com/iree-org/iree/actions/runs/25930827522/job/76227430699) | 1 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 33 | 0 | — | — | [2m12s](https://github.com/iree-org/iree/actions/runs/25930437529/job/76222829745) | [22m11s](https://github.com/iree-org/iree/actions/runs/25927854102/job/76216593957) | [23m21s](https://github.com/iree-org/iree/actions/runs/25937780385/job/76247967442) | 33 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 37 | 0 | — | — | [1m59s](https://github.com/iree-org/iree/actions/runs/25933907033/job/76234399670) | [20m34s](https://github.com/iree-org/iree/actions/runs/25930823415/job/76224428696) | [24m30s](https://github.com/iree-org/iree/actions/runs/25930824478/job/76224404142) | 34 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 1137 | 3% (30/1134) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,shark55-ci`, `self-hosted,persistent-cache,Linux,X64` | 881 | 1% (12/881) |  | 27m42s ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `Linux,X64,rdna3,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 1014 | 7% (66/1014) |  | 33m16s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,iree-w7900`, `Linux,X64,rdna3,persistent-cache`, `Linux,X64,rdna3,shark01-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 931 | 2% (14/931) |  | 35m20s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 309 | 2% (5/309) |  | 55m30s ago |

## Alerts

- **[stale-queued]** `ubuntu-24.04` oldest queued job observed waiting 4h53m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 4h55m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 4h21m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 4h17m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900` p95 queue 2h14m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-w7900x2,persistent-cache` p95 queue 2h46m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 5h12m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h16m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64,threadripper` p95 queue 2h31m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h25m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
