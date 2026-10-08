# iree-ci-monitor

_Updated: 2026-10-08 06:37 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 20 | 14 | [5h57m](https://github.com/iree-org/iree/actions/runs/37740107264/job/113203432882) | 2026-10-08 06:36 PDT | 0 | [6h18m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869866) | [7h12m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151870328) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 10 | 4 | [4h41m](https://github.com/iree-org/iree/actions/runs/37752052335/job/113230712744) | 2026-10-08 06:36 PDT | 0 | [3h22m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711655) | [6h56m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869658) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 10 | 5 | [4h52m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711769) | 2026-10-08 06:36 PDT | 1 | [3h51m](https://github.com/iree-org/iree/actions/runs/37740107264/job/113203432806) | [6h04m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869951) | 0% (0/1) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 20 | 8 | [2h02m](https://github.com/iree-org/iree/actions/runs/37769967641/job/113290196333) | 2026-10-08 06:36 PDT | 0 | [55m53s](https://github.com/iree-org/iree/actions/runs/37752052335/job/113230713264) | [3h15m](https://github.com/iree-org/iree/actions/runs/37740107264/job/113203432913) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 10 | 3 | [3h26m](https://github.com/iree-org/iree/actions/runs/37760940168/job/113259574815) | 2026-10-08 06:36 PDT | 0 | [37m58s](https://github.com/iree-org/iree/actions/runs/37773779132/job/113303299826) | [3h07m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711764) | 0% (0/2) | `shark55-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 10 | 1 | [2h00m](https://github.com/iree-org/iree/actions/runs/37770076281/job/113290670166) | 2026-10-08 06:36 PDT | 0 | [11m57s](https://github.com/iree-org/iree/actions/runs/37773779132/job/113303300034) | [1h45m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711775) | 100% (2/2) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 20 | 4 | [2h02m](https://github.com/iree-org/iree/actions/runs/37769967641/job/113290196214) | 2026-10-08 06:36 PDT | 0 | [12m01s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869938) | [1h40m](https://github.com/iree-org/iree/actions/runs/37752052335/job/113230713515) | 0% (0/5) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 20 | 5 | [2h02m](https://github.com/iree-org/iree/actions/runs/37769967641/job/113290196343) | 2026-10-08 06:36 PDT | 0 | [28m16s](https://github.com/iree-org/iree/actions/runs/37740107264/job/113203432896) | [1h25m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711690) | 0% (0/6) | `shark55-ci` |
| `ubuntu-24.04` | github-hosted | 221 | 0 | — | — | 4 | [2s](https://github.com/iree-org/iree/actions/runs/37773779206/job/113299561377) | [2m43s](https://github.com/iree-org/iree/actions/runs/37740107272/job/113201150599) | 5% (3/58) | 219 |
| `macos-15` | github-hosted | 34 | 0 | — | — | 1 | [10s](https://github.com/iree-org/iree/actions/runs/37769967519/job/113286924229) | [2m09s](https://github.com/iree-org/iree/actions/runs/37740107272/job/113201150795) | 0% (0/9) | 34 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m59s](https://github.com/iree-org/iree/actions/runs/37757347001/job/113245056666) | [1m59s](https://github.com/iree-org/iree/actions/runs/37757347001/job/113245056666) | 100% (1/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 36 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/37750934922/job/113223755484) | [1m38s](https://github.com/iree-org/iree/actions/runs/37752052327/job/113227489351) | 0% (0/9) | 36 |
| `windows-2022` | github-hosted | 35 | 0 | — | — | 3 | [3s](https://github.com/iree-org/iree/actions/runs/37750934922/job/113223755426) | [1m21s](https://github.com/iree-org/iree/actions/runs/37740107272/job/113201150454) | 11% (1/9) | 35 |
| `azure-linux-scale` | ossci | 71 | 0 | — | — | 7 | [9s](https://github.com/iree-org/iree/actions/runs/37752052327/job/113227489586) | [1m12s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337660728) | 23% (5/22) | 71 |
| `ubuntu-latest` | github-hosted | 30 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/37769959770/job/113286822478) | [39s](https://github.com/iree-org/iree/actions/runs/37770075332/job/113287217431) | 0% (0/9) | 30 |
| `macos-14` | github-hosted | 2 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/37731675631/job/113162040832) | [7s](https://github.com/iree-org/iree/actions/runs/37731675631/job/113162040863) | — | 2 |
| `azure-windows-scale` | ossci | 11 | 0 | — | — | 1 | [1s](https://github.com/iree-org/iree/actions/runs/37785020078/job/113337661028) | [2s](https://github.com/iree-org/iree/actions/runs/37780475189/job/113322113689) | 33% (1/3) | 11 |
| `Linux,X64,iree-w7900` | self-hosted | 10 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [5h57m](https://github.com/iree-org/iree/actions/runs/37740107264/job/113203432882) | 2026-10-08 06:36 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `fix/24955-preserve-shape-cast-ownership` | pull_request |
| [4h52m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711769) | 2026-10-08 06:36 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `main` | push |
| [4h52m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711822) | 2026-10-08 06:36 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `main` | push |
| [4h52m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711901) | 2026-10-08 06:36 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `main` | push |
| [4h41m](https://github.com/iree-org/iree/actions/runs/37752052335/job/113230712741) | 2026-10-08 06:36 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `users/roberto-laudani/qdq-per-channel-group` | pull_request |
| [4h41m](https://github.com/iree-org/iree/actions/runs/37752052335/job/113230712744) | 2026-10-08 06:36 PDT | `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | `users/roberto-laudani/qdq-per-channel-group` | pull_request |
| [4h41m](https://github.com/iree-org/iree/actions/runs/37752052335/job/113230712955) | 2026-10-08 06:36 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `users/roberto-laudani/qdq-per-channel-group` | pull_request |
| [4h41m](https://github.com/iree-org/iree/actions/runs/37752052335/job/113230713451) | 2026-10-08 06:36 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `users/roberto-laudani/qdq-per-channel-group` | pull_request |
| [3h26m](https://github.com/iree-org/iree/actions/runs/37760940168/job/113259574775) | 2026-10-08 06:36 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | `revert-24676-pr-dynamic-size-fix` | pull_request |
| [3h26m](https://github.com/iree-org/iree/actions/runs/37760940168/job/113259574787) | 2026-10-08 06:36 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | `revert-24676-pr-dynamic-size-fix` | pull_request |
| [3h26m](https://github.com/iree-org/iree/actions/runs/37760940168/job/113259574815) | 2026-10-08 06:36 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | `revert-24676-pr-dynamic-size-fix` | pull_request |
| [3h26m](https://github.com/iree-org/iree/actions/runs/37760940168/job/113259574943) | 2026-10-08 06:36 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | `revert-24676-pr-dynamic-size-fix` | pull_request |
| [2h02m](https://github.com/iree-org/iree/actions/runs/37769967641/job/113290196214) | 2026-10-08 06:36 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | `users/ziereis/qdq-reshape-propagation` | pull_request |
| [2h02m](https://github.com/iree-org/iree/actions/runs/37769967641/job/113290196333) | 2026-10-08 06:36 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | `users/ziereis/qdq-reshape-propagation` | pull_request |
| [2h02m](https://github.com/iree-org/iree/actions/runs/37769967641/job/113290196343) | 2026-10-08 06:36 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `users/ziereis/qdq-reshape-propagation` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 10 | 6 | [4h52m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711901) | 2026-10-08 06:36 PDT | [5h40m](https://github.com/iree-org/iree/actions/runs/37740107264/job/113203432973) | [7h12m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151870328) | [7h12m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151870328) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 10 | 4 | [4h41m](https://github.com/iree-org/iree/actions/runs/37752052335/job/113230712744) | 2026-10-08 06:36 PDT | [3h22m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711655) | [6h56m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869658) | [6h56m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869658) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 10 | 8 | [5h57m](https://github.com/iree-org/iree/actions/runs/37740107264/job/113203432882) | 2026-10-08 06:36 PDT | [6h18m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869866) | [6h18m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869866) | [6h18m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869866) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 10 | 5 | [4h52m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711769) | 2026-10-08 06:36 PDT | [3h51m](https://github.com/iree-org/iree/actions/runs/37740107264/job/113203432806) | [6h04m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869951) | [6h04m](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869951) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 10 | 3 | [3h26m](https://github.com/iree-org/iree/actions/runs/37760940168/job/113259574815) | 2026-10-08 06:36 PDT | [37m58s](https://github.com/iree-org/iree/actions/runs/37773779132/job/113303299826) | [3h07m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711764) | [3h07m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711764) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 10 | 4 | [2h02m](https://github.com/iree-org/iree/actions/runs/37769967641/job/113290196333) | 2026-10-08 06:36 PDT | [55m53s](https://github.com/iree-org/iree/actions/runs/37752052335/job/113230713264) | [3h15m](https://github.com/iree-org/iree/actions/runs/37740107264/job/113203432913) | [3h15m](https://github.com/iree-org/iree/actions/runs/37740107264/job/113203432913) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 3 | [2h02m](https://github.com/iree-org/iree/actions/runs/37769967641/job/113290196214) | 2026-10-08 06:36 PDT | [12m01s](https://github.com/iree-org/iree/actions/runs/37727893370/job/113151869938) | [3h05m](https://github.com/iree-org/iree/actions/runs/37740107264/job/113203432805) | [3h05m](https://github.com/iree-org/iree/actions/runs/37740107264/job/113203432805) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 10 | 4 | [2h02m](https://github.com/iree-org/iree/actions/runs/37769967641/job/113290196401) | 2026-10-08 06:36 PDT | [58m59s](https://github.com/iree-org/iree/actions/runs/37760940168/job/113259574742) | [2h54m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711897) | [2h54m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711897) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 10 | 2 | [2h02m](https://github.com/iree-org/iree/actions/runs/37769967641/job/113290196510) | 2026-10-08 06:36 PDT | [21m19s](https://github.com/iree-org/iree/actions/runs/37780046112/job/113323783242) | [2h38m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711752) | [2h38m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711752) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 10 | 3 | [2h02m](https://github.com/iree-org/iree/actions/runs/37769967641/job/113290196343) | 2026-10-08 06:36 PDT | [48m43s](https://github.com/iree-org/iree/actions/runs/37760940168/job/113259575050) | [1h25m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711690) | [1h25m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711690) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 10 | 1 | [2h00m](https://github.com/iree-org/iree/actions/runs/37770076281/job/113290670166) | 2026-10-08 06:36 PDT | [11m57s](https://github.com/iree-org/iree/actions/runs/37773779132/job/113303300034) | [1h45m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711775) | [1h45m](https://github.com/iree-org/iree/actions/runs/37750934856/job/113226711775) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 10 | 1 | [36m30s](https://github.com/iree-org/iree/actions/runs/37780046112/job/113323782925) | 2026-10-08 06:36 PDT | [21m14s](https://github.com/iree-org/iree/actions/runs/37770076281/job/113290670297) | [1h40m](https://github.com/iree-org/iree/actions/runs/37752052335/job/113230713515) | [1h40m](https://github.com/iree-org/iree/actions/runs/37752052335/job/113230713515) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: cpu_task | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37769967641/job/113290196415) | [5m12s](https://github.com/iree-org/iree/actions/runs/37773779132/job/113303300069) | [5m12s](https://github.com/iree-org/iree/actions/runs/37773779132/job/113303300069) | 10 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64 | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37780475316/job/113325345192) | [4m42s](https://github.com/iree-org/iree/actions/runs/37773779132/job/113303299792) | [4m42s](https://github.com/iree-org/iree/actions/runs/37773779132/job/113303299792) | 10 |
| `.github/workflows/pkgci.yml` | Test RISC-V 64 / riscv64-baremetal | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37769967641/job/113290196437) | [3m58s](https://github.com/iree-org/iree/actions/runs/37773779132/job/113303299550) | [3m58s](https://github.com/iree-org/iree/actions/runs/37773779132/job/113303299550) | 10 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O2 | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37780046112/job/113323783294) | [3m50s](https://github.com/iree-org/iree/actions/runs/37773779132/job/113303299864) | [3m50s](https://github.com/iree-org/iree/actions/runs/37773779132/job/113303299864) | 10 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cpu) | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37769967641/job/113290196351) | [3m35s](https://github.com/iree-org/iree/actions/runs/37773779132/job/113303299533) | [3m35s](https://github.com/iree-org/iree/actions/runs/37773779132/job/113303299533) | 10 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: cpu_llvm_sync_O0 | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37769967641/job/113290196411) | [3m24s](https://github.com/iree-org/iree/actions/runs/37773779132/job/113303299570) | [3m24s](https://github.com/iree-org/iree/actions/runs/37773779132/job/113303299570) | 10 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 11 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/37780046153/job/113320638980) | [3m19s](https://github.com/iree-org/iree/actions/runs/37740107272/job/113201150941) | [3m19s](https://github.com/iree-org/iree/actions/runs/37740107272/job/113201150941) | 11 |
| `.github/workflows/pkgci.yml` | Test PJRT plugin / Build and test (ubuntu-24.04, cuda) | `ubuntu-24.04` | 10 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/37780046112/job/113323782957) | [2m55s](https://github.com/iree-org/iree/actions/runs/37773779132/job/113303299415) | [2m55s](https://github.com/iree-org/iree/actions/runs/37773779132/job/113303299415) | 10 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 358 | 0% (1/357) | yes | running |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 139 | 17% (23/139) |  | 5m50s ago |

## Alerts

- **[stale-queued]** `Linux,X64,gfx1100,persistent-cache` oldest queued job observed waiting 3h26m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1100` oldest queued job observed waiting 2h02m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201,persistent-cache` oldest queued job observed waiting 4h52m (> 2h00m)
- **[stale-queued]** `Linux,X64,gfx1201` oldest queued job observed waiting 5h57m (> 2h00m)
- **[stale-queued]** `Linux,X64,iree-r9700` oldest queued job observed waiting 4h41m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3,persistent-cache` oldest queued job observed waiting 2h00m (> 2h00m)
- **[stale-queued]** `Linux,X64,rdna3` oldest queued job observed waiting 2h02m (> 2h00m)
- **[stale-queued]** `self-hosted,persistent-cache,Linux,X64` oldest queued job observed waiting 2h02m (> 2h00m)
- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 3h07m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h25m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 6h04m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 7h12m (> 1h00m)
- **[queue-starved]** `Linux,X64,iree-r9700` p95 queue 6h56m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache` p95 queue 1h45m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 3h15m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h40m (> 1h00m)
- **[high-failure-main]** `azure-linux-scale` main-branch failure rate 23% (5/22)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
