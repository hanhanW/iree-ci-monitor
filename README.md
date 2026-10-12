# iree-ci-monitor

_Updated: 2026-10-12 08:36 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 10 | 0 | — | — | 0 | [8m49s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874646309) | [53m14s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611860) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 10 | 0 | — | — | 0 | [11m36s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645885) | [43m45s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611743) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,rdna3,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [13m35s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645909) | [35m49s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611933) | 100% (2/2) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 10 | 0 | — | — | 0 | [15m06s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874646313) | [28m03s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611856) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [16m32s](https://github.com/iree-org/iree/actions/runs/38225214928/job/114734415286) | [22m21s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611880) | 0% (0/2) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 10 | 0 | — | — | 0 | [8m56s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611763) | [22m05s](https://github.com/iree-org/iree/actions/runs/38232943298/job/114759451582) | 0% (0/4) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 5 | 0 | — | — | 0 | [12m45s](https://github.com/iree-org/iree/actions/runs/38225214928/job/114734415220) | [15m37s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611689) | 0% (0/2) | `shark75-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 5 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645967) | [2m37s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611949) | 0% (0/2) | `shark75-ci` |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [2m16s](https://github.com/iree-org/iree/actions/runs/38231829455/job/114752913970) | [2m16s](https://github.com/iree-org/iree/actions/runs/38231829455/job/114752913970) | 100% (1/1) | 1 |
| `azure-linux-scale` | ossci | 68 | 0 | — | — | 0 | [9s](https://github.com/iree-org/iree/actions/runs/38238500139/job/114775042228) | [1m46s](https://github.com/iree-org/iree/actions/runs/38241137017/job/114783824069) | 12% (2/17) | 64 |
| `ubuntu-24.04-arm` | github-hosted | 30 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866046745) | [1m26s](https://github.com/iree-org/iree/actions/runs/38226308982/job/114735230789) | 0% (0/6) | 30 |
| `ubuntu-24.04` | github-hosted | 165 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38239648593/job/114832548790) | [51s](https://github.com/iree-org/iree/actions/runs/38241137017/job/114783823779) | 10% (4/42) | 163 |
| `macos-15` | github-hosted | 31 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/38229979741/job/114748058639) | [28s](https://github.com/iree-org/iree/actions/runs/38238624404/job/114775895827) | 0% (0/6) | 30 |
| `windows-2022` | github-hosted | 30 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/38229979741/job/114748058503) | [20s](https://github.com/iree-org/iree/actions/runs/38238624404/job/114775895809) | 0% (0/6) | 30 |
| `azure-windows-scale` | ossci | 10 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38238500139/job/114775042253) | [18s](https://github.com/iree-org/iree/actions/runs/38238624404/job/114775896214) | 0% (0/2) | 10 |
| `ubuntu-latest` | github-hosted | 33 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/38241134611/job/114783737288) | [16s](https://github.com/iree-org/iree/actions/runs/38238623939/job/114775397093) | 0% (0/6) | 33 |
| `Linux,X64,iree-w7900` | self-hosted | 5 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 5 | 0 | — | — | [19m26s](https://github.com/iree-org/iree/actions/runs/38225214928/job/114734415414) | [53m14s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611860) | [53m14s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611860) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [11m36s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645885) | [43m45s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611743) | [43m45s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611743) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_vulkan_rdna3 | `Linux,X64,rdna3,persistent-cache` | 5 | 0 | — | — | [13m35s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645909) | [35m49s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611933) | [35m49s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611933) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [25m19s](https://github.com/iree-org/iree/actions/runs/38225214928/job/114734415377) | [28m03s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611856) | [28m03s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611856) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 5 | 0 | — | — | [16m32s](https://github.com/iree-org/iree/actions/runs/38225214928/job/114734415286) | [22m21s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611880) | [22m21s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611880) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [8m56s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611763) | [22m05s](https://github.com/iree-org/iree/actions/runs/38232943298/job/114759451582) | [22m05s](https://github.com/iree-org/iree/actions/runs/38232943298/job/114759451582) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 5 | 0 | — | — | [15m06s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874646313) | [19m31s](https://github.com/iree-org/iree/actions/runs/38232943298/job/114759451659) | [19m31s](https://github.com/iree-org/iree/actions/runs/38232943298/job/114759451659) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 5 | 0 | — | — | [14m54s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645914) | [18m43s](https://github.com/iree-org/iree/actions/runs/38232943298/job/114759451494) | [18m43s](https://github.com/iree-org/iree/actions/runs/38232943298/job/114759451494) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 5 | 0 | — | — | [12m45s](https://github.com/iree-org/iree/actions/runs/38225214928/job/114734415220) | [15m37s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611689) | [15m37s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611689) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 5 | 0 | — | — | [11m23s](https://github.com/iree-org/iree/actions/runs/38232943298/job/114759451522) | [12m29s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787612212) | [12m29s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787612212) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 5 | 0 | — | — | [8m42s](https://github.com/iree-org/iree/actions/runs/38232943298/job/114759451725) | [9m33s](https://github.com/iree-org/iree/actions/runs/38225214928/job/114734415658) | [9m33s](https://github.com/iree-org/iree/actions/runs/38225214928/job/114734415658) | 1 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 10 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/38229979778/job/114746868416) | [3m11s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114783825572) | [3m11s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114783825572) | 9 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 5 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/38265336218/job/114874645967) | [2m37s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611949) | [2m37s](https://github.com/iree-org/iree/actions/runs/38241137079/job/114787611949) | 1 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [2m16s](https://github.com/iree-org/iree/actions/runs/38231829455/job/114752913970) | [2m16s](https://github.com/iree-org/iree/actions/runs/38231829455/job/114752913970) | [2m16s](https://github.com/iree-org/iree/actions/runs/38231829455/job/114752913970) | 1 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 10 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/38238500139/job/114775041898) | [2m11s](https://github.com/iree-org/iree/actions/runs/38226308982/job/114735230679) | [2m11s](https://github.com/iree-org/iree/actions/runs/38226308982/job/114735230679) | 10 |
| `.github/workflows/ci.yml` | linux_x64_clang / linux_x64_clang | `azure-linux-scale` | 10 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/38232943249/job/114756653656) | [1m48s](https://github.com/iree-org/iree/actions/runs/38229979741/job/114748058696) | [1m48s](https://github.com/iree-org/iree/actions/runs/38229979741/job/114748058696) | 9 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 10 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/38232943249/job/114756653528) | [1m46s](https://github.com/iree-org/iree/actions/runs/38241137017/job/114783824069) | [1m46s](https://github.com/iree-org/iree/actions/runs/38241137017/job/114783824069) | 10 |
| `.github/workflows/ci.yml` | linux_x64_clang_ubsan / linux_x64_clang_ubsan | `azure-linux-scale` | 10 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/38265336751/job/114866047741) | [1m46s](https://github.com/iree-org/iree/actions/runs/38241137017/job/114783824265) | [1m46s](https://github.com/iree-org/iree/actions/runs/38241137017/job/114783824265) | 9 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 10 | 0 | — | — | [19s](https://github.com/iree-org/iree/actions/runs/38238624404/job/114775895779) | [1m45s](https://github.com/iree-org/iree/actions/runs/38226308982/job/114735230809) | [1m45s](https://github.com/iree-org/iree/actions/runs/38226308982/job/114735230809) | 10 |
| `.github/workflows/ci.yml` | linux_x64_clang_asan / linux_x64_clang_asan | `azure-linux-scale` | 10 | 0 | — | — | [11s](https://github.com/iree-org/iree/actions/runs/38232943249/job/114756653902) | [1m41s](https://github.com/iree-org/iree/actions/runs/38241137017/job/114783824223) | [1m41s](https://github.com/iree-org/iree/actions/runs/38241137017/job/114783824223) | 10 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 322 | 0% (0/322) |  | 7m12s ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache`, `self-hosted,persistent-cache,Linux,X64` | 254 | 15% (38/254) |  | 12m33s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
