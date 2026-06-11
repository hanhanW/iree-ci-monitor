# iree-ci-monitor

_Updated: 2026-06-11 12:18 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201` | self-hosted | 36 | 0 | — | — | 0 | [31m30s](https://github.com/iree-org/iree/actions/runs/27353226389/job/80822499319) | [1h34m](https://github.com/iree-org/iree/actions/runs/27361767449/job/80853471769) | 0% (0/8) | `shark75-ci` |
| `azure-windows-scale` | ossci | 18 | 0 | — | — | 0 | [12s](https://github.com/iree-org/iree/actions/runs/27350469698/job/80810694766) | [1h30m](https://github.com/iree-org/iree/actions/runs/27339548473/job/80772524889) | 0% (0/3) | 18 |
| `Linux,X64,rdna3,persistent-cache,shark10-ci` | self-hosted | 18 | 0 | — | — | 0 | [32m44s](https://github.com/iree-org/iree/actions/runs/27341035739/job/80781841325) | [1h15m](https://github.com/iree-org/iree/actions/runs/27361767449/job/80853471915) | 0% (0/4) | `shark10-ci` |
| `Linux,X64,gfx1100` | self-hosted | 36 | 0 | — | — | 0 | [22m25s](https://github.com/iree-org/iree/actions/runs/27339548574/job/80781626196) | [1h02m](https://github.com/iree-org/iree/actions/runs/27361765800/job/80853262707) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 36 | 0 | — | — | 0 | [8m27s](https://github.com/iree-org/iree/actions/runs/27350778119/job/80818921965) | [57m28s](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931910) | 12% (1/8) | `shark01-ci`, `shark10-ci`, `shark55-ci`, `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64,threadripper` | self-hosted | 18 | 0 | — | — | 0 | [17m49s](https://github.com/iree-org/iree/actions/runs/27339548574/job/80781626192) | [54m30s](https://github.com/iree-org/iree/actions/runs/27361767449/job/80853471684) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 18 | 0 | — | — | 0 | [13m41s](https://github.com/iree-org/iree/actions/runs/27357464421/job/80837682439) | [49m28s](https://github.com/iree-org/iree/actions/runs/27361768667/job/80853784755) | 0% (0/4) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 18 | 0 | — | — | 0 | [28m26s](https://github.com/iree-org/iree/actions/runs/27361765800/job/80853262409) | [48m18s](https://github.com/iree-org/iree/actions/runs/27353226389/job/80822498876) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-w7900x2,persistent-cache` | self-hosted | 18 | 0 | — | — | 0 | [9m12s](https://github.com/iree-org/iree/actions/runs/27339548574/job/80781626092) | [47m22s](https://github.com/iree-org/iree/actions/runs/27360626370/job/80852592426) | 0% (0/4) | `shark01-ci`, `shark10-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 18 | 0 | — | — | 0 | [35m52s](https://github.com/iree-org/iree/actions/runs/27357719153/job/80838683396) | [46m40s](https://github.com/iree-org/iree/actions/runs/27361765800/job/80853262490) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 36 | 0 | — | — | 0 | [8m25s](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931958) | [42m58s](https://github.com/iree-org/iree/actions/runs/27357722610/job/80840142029) | 0% (0/8) | `shark01-ci`, `shark10-ci`, `shark55-ci` |
| `azure-linux-scale` | ossci | 96 | 0 | — | — | 0 | [12s](https://github.com/iree-org/iree/actions/runs/27350761897/job/80812009728) | [41m46s](https://github.com/iree-org/iree/actions/runs/27339548473/job/80772524860) | 0% (0/20) | 96 |
| `nodai-amdgpu-mi308-x86-64` | self-hosted | 18 | 0 | — | — | 0 | [6m09s](https://github.com/iree-org/iree/actions/runs/27357719153/job/80838683165) | [38m46s](https://github.com/iree-org/iree/actions/runs/27361768667/job/80853784726) | 0% (0/4) | `iree-mi308-1` |
| `linux-mi325-1gpu-ossci-iree-org` | ossci | 72 | 0 | — | — | 0 | [1m53s](https://github.com/iree-org/iree/actions/runs/27357722610/job/80840142076) | [21m01s](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852932036) | 6% (1/16) | 72 |
| `ubuntu-24.04` | github-hosted | 442 | 0 | — | — | 0 | [54s](https://github.com/iree-org/iree/actions/runs/27350777806/job/80812763632) | [14m10s](https://github.com/iree-org/iree/actions/runs/27357722610/job/80840142178) | 4% (3/69) | 399 |
| `Linux,X64,iree-w7900` | self-hosted | 18 | 0 | — | — | 0 | [8m01s](https://github.com/iree-org/iree/actions/runs/27353226389/job/80822498897) | [12m33s](https://github.com/iree-org/iree/actions/runs/27357723771/job/80840176021) | 25% (1/4) | `shark01-ci`, `shark10-ci` |
| `windows-2022` | github-hosted | 54 | 0 | — | — | 0 | [1m32s](https://github.com/iree-org/iree/actions/runs/27353225947/job/80820495515) | [6m20s](https://github.com/iree-org/iree/actions/runs/27357722611/job/80837890464) | 0% (0/9) | 54 |
| `macos-14` | github-hosted | 55 | 0 | — | — | 0 | [42s](https://github.com/iree-org/iree/actions/runs/27350726446/job/80811624670) | [5m12s](https://github.com/iree-org/iree/actions/runs/27361767227/job/80850734545) | 0% (0/10) | 55 |
| `ubuntu-24.04-arm` | github-hosted | 54 | 0 | — | — | 0 | [26s](https://github.com/iree-org/iree/actions/runs/27357722611/job/80837890401) | [4m29s](https://github.com/iree-org/iree/actions/runs/27357720650/job/80840077736) | 0% (0/9) | 54 |
| `ubuntu-latest` | github-hosted | 39 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27350721858/job/80811570480) | [3m21s](https://github.com/iree-org/iree/actions/runs/27357787090/job/80836704158) | 0% (0/9) | 39 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m17s](https://github.com/iree-org/iree/actions/runs/27341743240/job/80780044223) | [1m17s](https://github.com/iree-org/iree/actions/runs/27341743240/job/80780044223) | 0% (0/1) | 1 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 18 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/27341035739/job/80781841302) | [36s](https://github.com/iree-org/iree/actions/runs/27361768667/job/80853784703) | 0% (0/4) | 18 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/27341694492/job/80779880911) | [3s](https://github.com/iree-org/iree/actions/runs/27341694492/job/80779880911) | 0% (0/1) | 1 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci.yml` | windows_x64_msvc / windows_x64_msvc | `azure-windows-scale` | 18 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/27350469698/job/80810694766) | [1h30m](https://github.com/iree-org/iree/actions/runs/27339548473/job/80772524889) | [2h37m](https://github.com/iree-org/iree/actions/runs/27341035726/job/80777656092) | 18 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 18 | 0 | — | — | [34m31s](https://github.com/iree-org/iree/actions/runs/27360626370/job/80852592318) | [1h27m](https://github.com/iree-org/iree/actions/runs/27361767449/job/80853471685) | [2h31m](https://github.com/iree-org/iree/actions/runs/27357464421/job/80837682438) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache,shark10-ci` | 18 | 0 | — | — | [32m44s](https://github.com/iree-org/iree/actions/runs/27341035739/job/80781841325) | [1h15m](https://github.com/iree-org/iree/actions/runs/27361767449/job/80853471915) | [1h19m](https://github.com/iree-org/iree/actions/runs/27361768667/job/80853784740) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 18 | 0 | — | — | [31m30s](https://github.com/iree-org/iree/actions/runs/27353226389/job/80822499319) | [1h03m](https://github.com/iree-org/iree/actions/runs/27360626370/job/80852592690) | [1h34m](https://github.com/iree-org/iree/actions/runs/27361767449/job/80853471769) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 18 | 0 | — | — | [18m37s](https://github.com/iree-org/iree/actions/runs/27357464421/job/80837682552) | [1h02m](https://github.com/iree-org/iree/actions/runs/27361765800/job/80853262707) | [1h04m](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931901) | 3 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 18 | 0 | — | — | [26m33s](https://github.com/iree-org/iree/actions/runs/27361765800/job/80853262685) | [59m48s](https://github.com/iree-org/iree/actions/runs/27357464421/job/80837682541) | [1h04m](https://github.com/iree-org/iree/actions/runs/27361768667/job/80853784749) | 3 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 18 | 0 | — | — | [10m44s](https://github.com/iree-org/iree/actions/runs/27339548574/job/80781626171) | [55m20s](https://github.com/iree-org/iree/actions/runs/27357719153/job/80838683188) | [57m28s](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931910) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / torch_models tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64,threadripper` | 18 | 0 | — | — | [17m49s](https://github.com/iree-org/iree/actions/runs/27339548574/job/80781626192) | [54m30s](https://github.com/iree-org/iree/actions/runs/27361767449/job/80853471684) | [1h01m](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931922) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 18 | 0 | — | — | [13m41s](https://github.com/iree-org/iree/actions/runs/27357464421/job/80837682439) | [49m28s](https://github.com/iree-org/iree/actions/runs/27361768667/job/80853784755) | [51m49s](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931957) | 3 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 18 | 0 | — | — | [28m26s](https://github.com/iree-org/iree/actions/runs/27361765800/job/80853262409) | [48m18s](https://github.com/iree-org/iree/actions/runs/27353226389/job/80822498876) | [1h01m](https://github.com/iree-org/iree/actions/runs/27357719153/job/80838683194) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_model_tests :: rocm_hip_w7900 | `Linux,X64,iree-w7900x2,persistent-cache` | 18 | 0 | — | — | [9m12s](https://github.com/iree-org/iree/actions/runs/27339548574/job/80781626092) | [47m22s](https://github.com/iree-org/iree/actions/runs/27360626370/job/80852592426) | [1h01m](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931862) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 18 | 0 | — | — | [35m52s](https://github.com/iree-org/iree/actions/runs/27357719153/job/80838683396) | [46m40s](https://github.com/iree-org/iree/actions/runs/27361765800/job/80853262490) | [50m33s](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852932097) | 1 |
| `.github/workflows/ci_linux_x64_clang_tsan.yml` | linux_x64_clang_tsan | `azure-linux-scale` | 1 | 0 | — | — | [45m51s](https://github.com/iree-org/iree/actions/runs/27341722911/job/80779977908) | [45m51s](https://github.com/iree-org/iree/actions/runs/27341722911/job/80779977908) | [45m51s](https://github.com/iree-org/iree/actions/runs/27341722911/job/80779977908) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 18 | 0 | — | — | [7m30s](https://github.com/iree-org/iree/actions/runs/27357464421/job/80837682508) | [42m58s](https://github.com/iree-org/iree/actions/runs/27357722610/job/80840142029) | [45m25s](https://github.com/iree-org/iree/actions/runs/27361765800/job/80853262852) | 3 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 4 | 0 | — | — | [12s](https://github.com/iree-org/iree/actions/runs/27360629385/job/80846777702) | [42m43s](https://github.com/iree-org/iree/actions/runs/27339548473/job/80772524934) | [42m43s](https://github.com/iree-org/iree/actions/runs/27339548473/job/80772524934) | 4 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 18 | 0 | — | — | [11m20s](https://github.com/iree-org/iree/actions/runs/27350778119/job/80818921972) | [42m40s](https://github.com/iree-org/iree/actions/runs/27361765800/job/80853262596) | [44m20s](https://github.com/iree-org/iree/actions/runs/27357719153/job/80838683552) | 3 |
| `.github/workflows/ci_linux_x64_clang_debug.yml` | linux_x64_clang_debug | `azure-linux-scale` | 1 | 0 | — | — | [39m43s](https://github.com/iree-org/iree/actions/runs/27341654524/job/80779743665) | [39m43s](https://github.com/iree-org/iree/actions/runs/27341654524/job/80779743665) | [39m43s](https://github.com/iree-org/iree/actions/runs/27341654524/job/80779743665) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: amdgpu_rocm_mi308_gfx942 | `nodai-amdgpu-mi308-x86-64` | 18 | 0 | — | — | [6m09s](https://github.com/iree-org/iree/actions/runs/27357719153/job/80838683165) | [38m46s](https://github.com/iree-org/iree/actions/runs/27361768667/job/80853784726) | [41m15s](https://github.com/iree-org/iree/actions/runs/27357723771/job/80840176418) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 18 | 0 | — | — | [8m27s](https://github.com/iree-org/iree/actions/runs/27350778119/job/80818921965) | [36m45s](https://github.com/iree-org/iree/actions/runs/27361767021/job/80852931959) | [59m40s](https://github.com/iree-org/iree/actions/runs/27357464421/job/80837682494) | 4 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 18 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/27357718762/job/80836484603) | [32m37s](https://github.com/iree-org/iree/actions/runs/27339548473/job/80772524768) | [42m20s](https://github.com/iree-org/iree/actions/runs/27341035726/job/80777656052) | 18 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 387 | 2% (9/387) |  | 1h02m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 327 | 7% (22/327) |  | 1h13m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 291 | 2% (5/291) |  | 1h23m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 281 | 1% (4/281) |  | 1h31m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 92 | 1% (1/92) |  | 1h46m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h02m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 1h34m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3,persistent-cache,shark10-ci` p95 queue 1h15m (> 1h00m)
- **[queue-starved]** `azure-windows-scale` p95 queue 1h30m (> 1h00m)
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache,shark10-ci` single runner observed in last 7d
- **[spof]** `nodai-amdgpu-mi308-x86-64` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
