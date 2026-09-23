# iree-ci-monitor

_Updated: 2026-09-23 10:08 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 20 | 0 | — | — | 0 | [56m25s](https://github.com/iree-org/iree/actions/runs/35860367806/job/107184134694) | [2h41m](https://github.com/iree-org/iree/actions/runs/35841023154/job/107119219083) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 20 | 0 | — | — | 0 | [1h44m](https://github.com/iree-org/iree/actions/runs/35860366221/job/107190663836) | [2h29m](https://github.com/iree-org/iree/actions/runs/35860367806/job/107184134766) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 20 | 0 | — | — | 0 | [1h29m](https://github.com/iree-org/iree/actions/runs/35860367806/job/107184135305) | [2h26m](https://github.com/iree-org/iree/actions/runs/35841023657/job/107120086147) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [1h40m](https://github.com/iree-org/iree/actions/runs/35841024182/job/107118911353) | [2h20m](https://github.com/iree-org/iree/actions/runs/35860366459/job/107190315493) | 0% (0/1) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 20 | 0 | — | — | 0 | [1h15m](https://github.com/iree-org/iree/actions/runs/35841024182/job/107118911343) | [2h00m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888461) | 0% (0/2) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [39m54s](https://github.com/iree-org/iree/actions/runs/35841023120/job/107119197648) | [1h48m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888732) | 0% (0/1) | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 10 | 0 | — | — | 0 | [22m03s](https://github.com/iree-org/iree/actions/runs/35830803214/job/107085796876) | [1h29m](https://github.com/iree-org/iree/actions/runs/35841023120/job/107119197581) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 10 | 0 | — | — | 0 | [17m46s](https://github.com/iree-org/iree/actions/runs/35841023120/job/107119197182) | [1h19m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888553) | 0% (0/1) | `shark75-ci` |
| `azure-linux-scale` | ossci | 53 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/35830803202/job/107082743442) | [26m54s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180221047) | 12% (1/8) | 53 |
| `azure-windows-scale` | ossci | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35841023545/job/107116212114) | [8m36s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180221080) | 0% (0/1) | 10 |
| `ubuntu-24.04-arm` | github-hosted | 30 | 0 | — | — | 0 | [1m52s](https://github.com/iree-org/iree/actions/runs/35841023545/job/107116211464) | [8m29s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180220888) | 0% (0/3) | 30 |
| `macos-14` | github-hosted | 31 | 0 | — | — | 0 | [2m30s](https://github.com/iree-org/iree/actions/runs/35841023545/job/107116211335) | [7m18s](https://github.com/iree-org/iree/actions/runs/35841023084/job/107116210830) | 0% (0/4) | 31 |
| `windows-2022` | github-hosted | 30 | 0 | — | — | 0 | [1m58s](https://github.com/iree-org/iree/actions/runs/35860366367/job/107179220012) | [7m07s](https://github.com/iree-org/iree/actions/runs/35841023545/job/107116211416) | 0% (0/3) | 30 |
| `ubuntu-24.04` | github-hosted | 260 | 0 | — | — | 0 | [29s](https://github.com/iree-org/iree/actions/runs/35860366221/job/107190663670) | [6m56s](https://github.com/iree-org/iree/actions/runs/35860366207/job/107180014288) | 0% (0/23) | 232 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m31s](https://github.com/iree-org/iree/actions/runs/35843042550/job/107122453793) | [1m31s](https://github.com/iree-org/iree/actions/runs/35843042550/job/107122453793) | 100% (1/1) | 1 |
| `ubuntu-latest` | github-hosted | 54 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/35860361318/job/107178791849) | [1m05s](https://github.com/iree-org/iree/actions/runs/35860362399/job/107178794627) | 0% (0/3) | 54 |
| `Linux,X64,iree-w7900` | self-hosted | 10 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 10 | 0 | — | — | [1h12m](https://github.com/iree-org/iree/actions/runs/35829786411/job/107155742966) | [3h06m](https://github.com/iree-org/iree/actions/runs/35841023120/job/107119197636) | [3h06m](https://github.com/iree-org/iree/actions/runs/35841023120/job/107119197636) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [59m49s](https://github.com/iree-org/iree/actions/runs/35841023154/job/107119218992) | [2h56m](https://github.com/iree-org/iree/actions/runs/35841023120/job/107119197444) | [2h56m](https://github.com/iree-org/iree/actions/runs/35841023120/job/107119197444) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [1h55m](https://github.com/iree-org/iree/actions/runs/35860366221/job/107190663565) | [2h33m](https://github.com/iree-org/iree/actions/runs/35841023154/job/107119218886) | [2h33m](https://github.com/iree-org/iree/actions/runs/35841023154/job/107119218886) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 10 | 0 | — | — | [1h15m](https://github.com/iree-org/iree/actions/runs/35860366459/job/107190315310) | [2h29m](https://github.com/iree-org/iree/actions/runs/35860367806/job/107184134766) | [2h29m](https://github.com/iree-org/iree/actions/runs/35860367806/job/107184134766) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [1h03m](https://github.com/iree-org/iree/actions/runs/35829786411/job/107155742724) | [2h28m](https://github.com/iree-org/iree/actions/runs/35841023154/job/107119219162) | [2h28m](https://github.com/iree-org/iree/actions/runs/35841023154/job/107119219162) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 10 | 0 | — | — | [1h40m](https://github.com/iree-org/iree/actions/runs/35841024182/job/107118911353) | [2h20m](https://github.com/iree-org/iree/actions/runs/35860366459/job/107190315493) | [2h20m](https://github.com/iree-org/iree/actions/runs/35860366459/job/107190315493) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 10 | 0 | — | — | [1h45m](https://github.com/iree-org/iree/actions/runs/35841023120/job/107119197378) | [2h16m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888880) | [2h16m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888880) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 10 | 0 | — | — | [46m21s](https://github.com/iree-org/iree/actions/runs/35841024182/job/107118911374) | [2h06m](https://github.com/iree-org/iree/actions/runs/35860366459/job/107190315280) | [2h06m](https://github.com/iree-org/iree/actions/runs/35860366459/job/107190315280) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 0 | — | — | [1h08m](https://github.com/iree-org/iree/actions/runs/35829786411/job/107155742757) | [2h00m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888461) | [2h00m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888461) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 10 | 0 | — | — | [39m54s](https://github.com/iree-org/iree/actions/runs/35841023120/job/107119197648) | [1h48m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888732) | [1h48m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888732) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 10 | 0 | — | — | [22m03s](https://github.com/iree-org/iree/actions/runs/35830803214/job/107085796876) | [1h29m](https://github.com/iree-org/iree/actions/runs/35841023120/job/107119197581) | [1h29m](https://github.com/iree-org/iree/actions/runs/35841023120/job/107119197581) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 10 | 0 | — | — | [17m46s](https://github.com/iree-org/iree/actions/runs/35841023120/job/107119197182) | [1h19m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888553) | [1h19m](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888553) | 1 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 10 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/35841023365/job/107116188433) | [28m22s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180221070) | [28m22s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180221070) | 10 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 10 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/35830803202/job/107082743442) | [28m15s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180220833) | [28m15s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180220833) | 10 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 10 | 0 | — | — | [1m33s](https://github.com/iree-org/iree/actions/runs/35841023154/job/107116214623) | [27m41s](https://github.com/iree-org/iree/actions/runs/35860367805/job/107180504989) | [27m41s](https://github.com/iree-org/iree/actions/runs/35860367805/job/107180504989) | 10 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 10 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35841024215/job/107116167723) | [26m54s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180221047) | [26m54s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180221047) | 10 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 10 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/35841023365/job/107116188046) | [26m41s](https://github.com/iree-org/iree/actions/runs/35860366207/job/107180014491) | [26m41s](https://github.com/iree-org/iree/actions/runs/35860366207/job/107180014491) | 10 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 10 | 0 | — | — | [2m44s](https://github.com/iree-org/iree/actions/runs/35841023084/job/107116210647) | [10m04s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180221061) | [10m04s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180221061) | 10 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 10 | 0 | — | — | [3m43s](https://github.com/iree-org/iree/actions/runs/35841023084/job/107116210751) | [10m01s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180220915) | [10m01s](https://github.com/iree-org/iree/actions/runs/35860367746/job/107180220915) | 10 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64-baremetal | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/35860367805/job/107192888635) | [9m09s](https://github.com/iree-org/iree/actions/runs/35841024182/job/107118911575) | [9m09s](https://github.com/iree-org/iree/actions/runs/35841024182/job/107118911575) | 10 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 367 | 1% (5/367) |  | 1h42m ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 357 | 2% (6/357) |  | 1h50m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 134 | 1% (2/134) |  | 5d19h ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 2h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 2h26m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h29m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h29m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 1h19m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache` p95 queue 1h48m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 2h41m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 2h00m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-w7900` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
