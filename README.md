# iree-ci-monitor

_Updated: 2026-10-20 04:46 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,iree-r9700` | self-hosted | 9 | 0 | — | — | 1 | [58m29s](https://github.com/iree-org/iree/actions/runs/39392893286/job/118531652585) | [2h18m](https://github.com/iree-org/iree/actions/runs/39392991025/job/118539029068) | 17% (1/6) | `shark75-ci` |
| `Linux,X64,gfx1201` | self-hosted | 18 | 2 | [24m06s](https://github.com/iree-org/iree/actions/runs/39410630843/job/118599497129) | 2026-10-20 04:45 PDT | 0 | [35m24s](https://github.com/iree-org/iree/actions/runs/39392991025/job/118539029505) | [2h02m](https://github.com/iree-org/iree/actions/runs/39392991025/job/118539029383) | 0% (0/12) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 18 | 0 | — | — | 1 | [46m44s](https://github.com/iree-org/iree/actions/runs/39392991025/job/118539029352) | [1h54m](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546740167) | 0% (0/13) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 9 | 0 | — | — | 0 | [57m56s](https://github.com/iree-org/iree/actions/runs/39392991025/job/118539029144) | [1h50m](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546739791) | 0% (0/7) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 20 | 7 | [2h37m](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546740121) | 2026-10-20 04:45 PDT | 0 | [45m49s](https://github.com/iree-org/iree/actions/runs/39392991025/job/118539029531) | [1h47m](https://github.com/iree-org/iree/actions/runs/39392893286/job/118531652841) | 0% (0/9) | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 9 | 1 | [24m06s](https://github.com/iree-org/iree/actions/runs/39410630843/job/118599496973) | 2026-10-20 04:45 PDT | 0 | [1h16m](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546739642) | [1h35m](https://github.com/iree-org/iree/actions/runs/39393068980/job/118533301806) | 0% (0/6) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 19 | 6 | [2h37m](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546740103) | 2026-10-20 04:45 PDT | 0 | [41m05s](https://github.com/iree-org/iree/actions/runs/39381119084/job/118499822863) | [1h34m](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546739720) | 0% (0/9) | `shark55-ci` |
| `azure-linux-scale` | ossci | 72 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/39388062744/job/118512692281) | [3m07s](https://github.com/iree-org/iree/actions/runs/39393068981/job/118529103102) | 2% (1/52) | 72 |
| `ubuntu-24.04-arm` | github-hosted | 33 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/39395898363/job/118538515513) | [2m20s](https://github.com/iree-org/iree/actions/runs/39393068981/job/118529101567) | 0% (0/21) | 32 |
| `macos-15` | github-hosted | 33 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/39400796167/job/118554702800) | [1m59s](https://github.com/iree-org/iree/actions/runs/39393068981/job/118529102135) | 0% (0/21) | 32 |
| `ubuntu-24.04` | github-hosted | 202 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/39400870093/job/118554957484) | [1m50s](https://github.com/iree-org/iree/actions/runs/39392991025/job/118539029465) | 1% (1/135) | 198 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m31s](https://github.com/iree-org/iree/actions/runs/39400847977/job/118554881267) | [1m31s](https://github.com/iree-org/iree/actions/runs/39400847977/job/118554881267) | 100% (1/1) | 1 |
| `windows-2022` | github-hosted | 32 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39410630766/job/118587300376) | [1m21s](https://github.com/iree-org/iree/actions/runs/39395898363/job/118538515731) | 0% (0/21) | 31 |
| `azure-windows-scale` | ossci | 10 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/39392991074/job/118561997593) | [1m12s](https://github.com/iree-org/iree/actions/runs/39395898363/job/118538515619) | 0% (0/7) | 10 |
| `ubuntu-latest` | github-hosted | 30 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39395898641/job/118538436712) | [39s](https://github.com/iree-org/iree/actions/runs/39393069362/job/118529022029) | 0% (0/21) | 30 |
| `Linux,X64,iree-w7900` | self-hosted | 9 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [2h37m](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546740103) | 2026-10-20 04:45 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [2h37m](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546740121) | 2026-10-20 04:45 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [1h41m](https://github.com/iree-org/iree/actions/runs/39388062820/job/118569285218) | 2026-10-20 04:45 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `main` | push |
| [1h41m](https://github.com/iree-org/iree/actions/runs/39388062820/job/118569285276) | 2026-10-20 04:45 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [1h41m](https://github.com/iree-org/iree/actions/runs/39388062820/job/118569285316) | 2026-10-20 04:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [1h41m](https://github.com/iree-org/iree/actions/runs/39388062820/job/118569285347) | 2026-10-20 04:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `fix-spirv-wide-elementwise` | pull_request |
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `fix-spirv-wide-elementwise` | pull_request |
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827580) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `fix-spirv-wide-elementwise` | pull_request |
| [24m06s](https://github.com/iree-org/iree/actions/runs/39410630843/job/118599496973) | 2026-10-20 04:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `main` | push |
| [24m06s](https://github.com/iree-org/iree/actions/runs/39410630843/job/118599497129) | 2026-10-20 04:45 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [24m06s](https://github.com/iree-org/iree/actions/runs/39410630843/job/118599497203) | 2026-10-20 04:45 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `main` | push |
| [24m06s](https://github.com/iree-org/iree/actions/runs/39410630843/job/118599497231) | 2026-10-20 04:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |
| [24m06s](https://github.com/iree-org/iree/actions/runs/39410630843/job/118599497316) | 2026-10-20 04:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `main` | push |
| [24m06s](https://github.com/iree-org/iree/actions/runs/39410630843/job/118599497329) | 2026-10-20 04:45 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 10 | 4 | [2h37m](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546740121) | 2026-10-20 04:45 PDT | [45m02s](https://github.com/iree-org/iree/actions/runs/39381119084/job/118499823059) | [2h35m](https://github.com/iree-org/iree/actions/runs/39393068980/job/118533302726) | [2h35m](https://github.com/iree-org/iree/actions/runs/39393068980/job/118533302726) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 9 | 3 | [2h37m](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546740103) | 2026-10-20 04:45 PDT | [32m17s](https://github.com/iree-org/iree/actions/runs/39393068980/job/118533302005) | [42m59s](https://github.com/iree-org/iree/actions/runs/39392991025/job/118539029499) | [42m59s](https://github.com/iree-org/iree/actions/runs/39392991025/job/118539029499) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 9 | 0 | — | — | [58m29s](https://github.com/iree-org/iree/actions/runs/39392893286/job/118531652585) | [2h18m](https://github.com/iree-org/iree/actions/runs/39392991025/job/118539029068) | [2h18m](https://github.com/iree-org/iree/actions/runs/39392991025/job/118539029068) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 9 | 1 | [24m06s](https://github.com/iree-org/iree/actions/runs/39410630843/job/118599497231) | 2026-10-20 04:45 PDT | [58m42s](https://github.com/iree-org/iree/actions/runs/39381119084/job/118499822699) | [2h13m](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546739601) | [2h13m](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546739601) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 10 | 3 | [1h41m](https://github.com/iree-org/iree/actions/runs/39388062820/job/118569285347) | 2026-10-20 04:45 PDT | [44m02s](https://github.com/iree-org/iree/actions/runs/39385170700/job/118505574789) | [1h59m](https://github.com/iree-org/iree/actions/runs/39393068980/job/118533302315) | [1h59m](https://github.com/iree-org/iree/actions/runs/39393068980/job/118533302315) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [58m44s](https://github.com/iree-org/iree/actions/runs/39388062820/job/118569285333) | [1h55m](https://github.com/iree-org/iree/actions/runs/39393068980/job/118533301855) | [1h55m](https://github.com/iree-org/iree/actions/runs/39393068980/job/118533301855) | 2 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 9 | 0 | — | — | [46m44s](https://github.com/iree-org/iree/actions/runs/39392991025/job/118539029352) | [1h54m](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546740167) | [1h54m](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546740167) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 9 | 0 | — | — | [57m56s](https://github.com/iree-org/iree/actions/runs/39392991025/job/118539029144) | [1h50m](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546739791) | [1h50m](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546739791) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 10 | 3 | [1h41m](https://github.com/iree-org/iree/actions/runs/39388062820/job/118569285316) | 2026-10-20 04:45 PDT | [45m49s](https://github.com/iree-org/iree/actions/runs/39392991025/job/118539029531) | [1h42m](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546739728) | [1h42m](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546739728) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 9 | 1 | [24m06s](https://github.com/iree-org/iree/actions/runs/39410630843/job/118599496973) | 2026-10-20 04:45 PDT | [1h16m](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546739642) | [1h35m](https://github.com/iree-org/iree/actions/runs/39393068980/job/118533301806) | [1h35m](https://github.com/iree-org/iree/actions/runs/39393068980/job/118533301806) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 9 | 1 | [24m06s](https://github.com/iree-org/iree/actions/runs/39410630843/job/118599497129) | 2026-10-20 04:45 PDT | [34m23s](https://github.com/iree-org/iree/actions/runs/39393068980/job/118533302290) | [57m24s](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546740304) | [57m24s](https://github.com/iree-org/iree/actions/runs/39395898510/job/118546740304) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39388062820/job/118561101726) | [4m19s](https://github.com/iree-org/iree/actions/runs/39410630843/job/118587301482) | [4m19s](https://github.com/iree-org/iree/actions/runs/39410630843/job/118587301482) | 10 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39410630766/job/118587300207) | [3m38s](https://github.com/iree-org/iree/actions/runs/39395898363/job/118538515571) | [3m38s](https://github.com/iree-org/iree/actions/runs/39395898363/job/118538515571) | 9 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 10 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/39395898363/job/118538515481) | [3m08s](https://github.com/iree-org/iree/actions/runs/39385170748/job/118503234091) | [3m08s](https://github.com/iree-org/iree/actions/runs/39385170748/job/118503234091) | 10 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 10 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/39392893394/job/118528516005) | [3m07s](https://github.com/iree-org/iree/actions/runs/39393068981/job/118529103102) | [3m07s](https://github.com/iree-org/iree/actions/runs/39393068981/job/118529103102) | 10 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 10 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/39388062744/job/118512692096) | [3m06s](https://github.com/iree-org/iree/actions/runs/39381119061/job/118490720322) | [3m06s](https://github.com/iree-org/iree/actions/runs/39381119061/job/118490720322) | 10 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 9 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/39410630766/job/118587300241) | [3m06s](https://github.com/iree-org/iree/actions/runs/39385170748/job/118503234173) | [3m06s](https://github.com/iree-org/iree/actions/runs/39385170748/job/118503234173) | 9 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 9 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39410630843/job/118599497181) | [3m01s](https://github.com/iree-org/iree/actions/runs/39392893286/job/118531652562) | [3m01s](https://github.com/iree-org/iree/actions/runs/39392893286/job/118531652562) | 9 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 10 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/39388062744/job/118512692418) | [2m56s](https://github.com/iree-org/iree/actions/runs/39385170748/job/118503234072) | [2m56s](https://github.com/iree-org/iree/actions/runs/39385170748/job/118503234072) | 10 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 10 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/39385170748/job/118503233963) | [2m55s](https://github.com/iree-org/iree/actions/runs/39393068981/job/118529101835) | [2m55s](https://github.com/iree-org/iree/actions/runs/39393068981/job/118529101835) | 9 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 343 | 1% (3/342) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 401 | 2% (6/400) | yes | running |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 2h37m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 2h37m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h50m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h47m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h35m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 2h18m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 1h34m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h54m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
