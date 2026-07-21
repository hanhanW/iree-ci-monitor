# iree-ci-monitor

_Updated: 2026-07-21 00:12 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 2 | 0 | — | — | 0 | [18m58s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772425) | [1h05m](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483751) | — | `shark10-ci` |
| `Linux,X64,gfx1201` | self-hosted | 4 | 0 | — | — | 0 | [9m06s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772501) | [34m29s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483799) | — | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772120) | [26m21s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483588) | — | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [19m22s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772429) | [19m30s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483752) | — | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772228) | [18m02s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483783) | — | `shark01-ci` |
| `Linux,X64,gfx1100` | self-hosted | 4 | 0 | — | — | 0 | [5m23s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483809) | [17m28s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772509) | — | `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 4 | 0 | — | — | 0 | [4m01s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772253) | [17m01s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483774) | — | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 4 | 0 | — | — | 0 | [13m19s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772401) | [16m35s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483800) | — | `shark10-ci`, `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 2 | 0 | — | — | 0 | [9m37s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483889) | [12m32s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772399) | — | `shark01-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483672) | [5m08s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772350) | — | `shark10-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 2 | 0 | — | — | 0 | [1m44s](https://github.com/iree-org/iree/actions/runs/29781695181/job/88484238293) | [1m53s](https://github.com/iree-org/iree/actions/runs/29804955576/job/88553560581) | — | 2 |
| `ubuntu-24.04-arm` | github-hosted | 9 | 0 | — | — | 2 | [5s](https://github.com/iree-org/iree/actions/runs/29804955576/job/88553560464) | [1m34s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837256) | — | 9 |
| `macos-14` | github-hosted | 10 | 0 | — | — | 2 | [3s](https://github.com/iree-org/iree/actions/runs/29781695181/job/88484237816) | [1m23s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837086) | — | 10 |
| `windows-2022` | github-hosted | 8 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/29781695181/job/88484237813) | [1m19s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837099) | — | 8 |
| `ubuntu-24.04` | github-hosted | 53 | 0 | — | — | 4 | [2s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483676) | [32s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837020) | 50% (2/4) | 52 |
| `azure-linux-scale` | ossci | 14 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/29804955576/job/88553560595) | [20s](https://github.com/iree-org/iree/actions/runs/29804955576/job/88553560638) | — | 14 |
| `macos-15-intel` | github-hosted | 2 | 0 | — | — | 1 | [4s](https://github.com/iree-org/iree/actions/runs/29781695181/job/88484238263) | [5s](https://github.com/iree-org/iree/actions/runs/29804955576/job/88553560625) | — | 2 |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772130) | [3s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483579) | — | 2 |
| `ubuntu-latest` | github-hosted | 4 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29804953427/job/88553520377) | [3s](https://github.com/iree-org/iree/actions/runs/29804953427/job/88553520354) | 0% (0/1) | 4 |
| `Linux,X64,iree-w7900` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772140) | [2s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483603) | — | `shark01-ci`, `shark10-ci` |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772300) | [2s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483770) | — | `iree-mi308-1` |
| `azure-windows-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/29781695181/job/88484238327) | [2s](https://github.com/iree-org/iree/actions/runs/29804955576/job/88553560556) | — | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 2 | 0 | — | — | [18m58s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772425) | [1h05m](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483751) | [1h05m](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483751) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [5m23s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772481) | [34m29s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483799) | [34m29s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483799) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772120) | [26m21s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483588) | [26m21s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483588) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 2 | 0 | — | — | [19m22s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772429) | [19m30s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483752) | [19m30s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483752) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772228) | [18m02s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483783) | [18m02s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483783) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483742) | [17m28s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772509) | [17m28s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772509) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 2 | 0 | — | — | [4m01s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772253) | [17m01s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483774) | [17m01s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483774) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 2 | 0 | — | — | [13m19s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772401) | [16m35s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483800) | [16m35s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483800) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 2 | 0 | — | — | [9m37s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483889) | [12m32s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772399) | [12m32s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772399) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 2 | 0 | — | — | [6m53s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483838) | [9m52s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772517) | [9m52s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772517) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 2 | 0 | — | — | [6m55s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483840) | [9m06s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772501) | [9m06s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772501) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 2 | 0 | — | — | [5m17s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772512) | [5m23s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483809) | [5m23s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483809) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/29804955596/job/88554483672) | [5m08s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772350) | [5m08s](https://github.com/iree-org/iree/actions/runs/29781695399/job/88485772350) | 1 |
| `.github/workflows/ci.yml` | linux_arm64_clang / linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 2 | 0 | — | — | [1m44s](https://github.com/iree-org/iree/actions/runs/29781695181/job/88484238293) | [1m53s](https://github.com/iree-org/iree/actions/runs/29804955576/job/88553560581) | [1m53s](https://github.com/iree-org/iree/actions/runs/29804955576/job/88553560581) | 2 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1m34s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837256) | [1m34s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837256) | [1m34s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837256) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [1m27s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837068) | [1m27s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837068) | [1m27s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837068) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [1m23s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837086) | [1m23s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837086) | [1m23s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837086) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | 1 | 0 | — | — | [1m19s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837099) | [1m19s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837099) | [1m19s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837099) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [1m15s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837052) | [1m15s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837052) | [1m15s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837052) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [1m09s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837040) | [1m09s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837040) | [1m09s](https://github.com/iree-org/iree/actions/runs/29805747813/job/88555837040) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 161 | 5% (8/161) |  | 8m55s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 191 | 0% (0/191) |  | 38m30s ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 148 | 1% (2/148) |  | 53m54s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 149 | 0% (0/149) |  | 56m35s ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 44 | 0% (0/44) |  | 1h08m ago |

## Alerts

- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h05m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
