# iree-ci-monitor

_Updated: 2026-10-30 06:03 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [10m53s](https://github.com/iree-org/iree/actions/runs/41043326734/job/124025229394) | [25m16s](https://github.com/iree-org/iree/actions/runs/41037238786/job/124004429542) | 0% (0/3) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 8 | 0 | — | — | 0 | [8m11s](https://github.com/iree-org/iree/actions/runs/41046100908/job/124034251828) | [22m10s](https://github.com/iree-org/iree/actions/runs/41014175939/job/123929183637) | 0% (0/3) | `shark75-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 16 | 0 | — | — | 0 | [6m25s](https://github.com/iree-org/iree/actions/runs/41043326734/job/124025229260) | [21m36s](https://github.com/iree-org/iree/actions/runs/41036360404/job/124000769652) | 0% (0/6) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,rdna3` | self-hosted | 16 | 0 | — | — | 0 | [8m25s](https://github.com/iree-org/iree/actions/runs/41014175939/job/123929183761) | [20m48s](https://github.com/iree-org/iree/actions/runs/41046100908/job/124034251922) | 17% (1/6) | `shark55-ci` |
| `Linux,X64,gfx1100` | self-hosted | 16 | 0 | — | — | 0 | [13m59s](https://github.com/iree-org/iree/actions/runs/41014175939/job/123929183671) | [19m52s](https://github.com/iree-org/iree/actions/runs/41037238786/job/124004429614) | 17% (1/6) | `shark55-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 8 | 0 | — | — | 0 | [5m26s](https://github.com/iree-org/iree/actions/runs/41036360404/job/124000769632) | [15m54s](https://github.com/iree-org/iree/actions/runs/41021907634/job/123978730627) | 0% (0/3) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 16 | 0 | — | — | 0 | [6m57s](https://github.com/iree-org/iree/actions/runs/41014175939/job/123929183691) | [14m25s](https://github.com/iree-org/iree/actions/runs/41046100908/job/124034252008) | 17% (1/6) | `shark75-ci` |
| `ubuntu-24.04-arm` | github-hosted | 27 | 0 | — | — | 0 | [4s](https://github.com/iree-org/iree/actions/runs/41050722968/job/124045871258) | [2m23s](https://github.com/iree-org/iree/actions/runs/41037238942/job/124001063601) | 0% (0/9) | 27 |
| `azure-linux-scale` | ossci | 53 | 0 | — | — | 0 | [8s](https://github.com/iree-org/iree/actions/runs/41046100942/job/124031568257) | [1m42s](https://github.com/iree-org/iree/actions/runs/41021907701/job/123975720676) | 4% (1/23) | 53 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m33s](https://github.com/iree-org/iree/actions/runs/41032787171/job/123986288821) | [1m33s](https://github.com/iree-org/iree/actions/runs/41032787171/job/123986288821) | 100% (1/1) | 1 |
| `macos-15` | github-hosted | 27 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/41021907701/job/123975720486) | [1m27s](https://github.com/iree-org/iree/actions/runs/41037238942/job/124001063578) | 0% (0/9) | 27 |
| `windows-2022` | github-hosted | 26 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/41043326789/job/124021274066) | [37s](https://github.com/iree-org/iree/actions/runs/41037238942/job/124001063804) | 11% (1/9) | 26 |
| `azure-windows-scale` | ossci | 8 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/41046100942/job/124031568260) | [7s](https://github.com/iree-org/iree/actions/runs/41037238942/job/124001063822) | 33% (1/3) | 8 |
| `ubuntu-24.04` | github-hosted | 179 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/41037238786/job/124015477446) | [3s](https://github.com/iree-org/iree/actions/runs/41050722968/job/124045871129) | 6% (4/62) | 176 |
| `ubuntu-latest` | github-hosted | 12 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/41045982420/job/124030071802) | [3s](https://github.com/iree-org/iree/actions/runs/41014174876/job/123926614681) | 0% (0/9) | 12 |
| `Linux,X64,iree-w7900` | self-hosted | 8 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 8 | 0 | — | — | [10m53s](https://github.com/iree-org/iree/actions/runs/41043326734/job/124025229394) | [25m16s](https://github.com/iree-org/iree/actions/runs/41037238786/job/124004429542) | [25m16s](https://github.com/iree-org/iree/actions/runs/41037238786/job/124004429542) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [9m17s](https://github.com/iree-org/iree/actions/runs/41050722999/job/124048557595) | [23m13s](https://github.com/iree-org/iree/actions/runs/41037238786/job/124004429549) | [23m13s](https://github.com/iree-org/iree/actions/runs/41037238786/job/124004429549) | 2 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 8 | 0 | — | — | [8m11s](https://github.com/iree-org/iree/actions/runs/41046100908/job/124034251828) | [22m10s](https://github.com/iree-org/iree/actions/runs/41014175939/job/123929183637) | [22m10s](https://github.com/iree-org/iree/actions/runs/41014175939/job/123929183637) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 8 | 0 | — | — | [12m16s](https://github.com/iree-org/iree/actions/runs/41043326734/job/124025229619) | [21m26s](https://github.com/iree-org/iree/actions/runs/41014175939/job/123929183834) | [21m26s](https://github.com/iree-org/iree/actions/runs/41014175939/job/123929183834) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 8 | 0 | — | — | [8m25s](https://github.com/iree-org/iree/actions/runs/41014175939/job/123929183761) | [20m48s](https://github.com/iree-org/iree/actions/runs/41046100908/job/124034251922) | [20m48s](https://github.com/iree-org/iree/actions/runs/41046100908/job/124034251922) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 8 | 0 | — | — | [17m26s](https://github.com/iree-org/iree/actions/runs/41007454007/job/123915236771) | [20m24s](https://github.com/iree-org/iree/actions/runs/41050722999/job/124048557704) | [20m24s](https://github.com/iree-org/iree/actions/runs/41050722999/job/124048557704) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 8 | 0 | — | — | [8m40s](https://github.com/iree-org/iree/actions/runs/41043326734/job/124025229667) | [18m43s](https://github.com/iree-org/iree/actions/runs/41050722999/job/124048557487) | [18m43s](https://github.com/iree-org/iree/actions/runs/41050722999/job/124048557487) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [6m57s](https://github.com/iree-org/iree/actions/runs/41014175939/job/123929183691) | [17m57s](https://github.com/iree-org/iree/actions/runs/41021907634/job/123978730561) | [17m57s](https://github.com/iree-org/iree/actions/runs/41021907634/job/123978730561) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 8 | 0 | — | — | [5m26s](https://github.com/iree-org/iree/actions/runs/41036360404/job/124000769632) | [15m54s](https://github.com/iree-org/iree/actions/runs/41021907634/job/123978730627) | [15m54s](https://github.com/iree-org/iree/actions/runs/41021907634/job/123978730627) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 8 | 0 | — | — | [3m43s](https://github.com/iree-org/iree/actions/runs/41021907634/job/123978730417) | [14m39s](https://github.com/iree-org/iree/actions/runs/41037238786/job/124004429603) | [14m39s](https://github.com/iree-org/iree/actions/runs/41037238786/job/124004429603) | 2 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 8 | 0 | — | — | [8m14s](https://github.com/iree-org/iree/actions/runs/41050722999/job/124048557640) | [13m34s](https://github.com/iree-org/iree/actions/runs/41014175939/job/123929183686) | [13m34s](https://github.com/iree-org/iree/actions/runs/41014175939/job/123929183686) | 1 |
| `.github/workflows/ci.yml` | runtime_tracing :: windows-2022 :: console | `windows-2022` | 8 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41046100942/job/124031568010) | [2m55s](https://github.com/iree-org/iree/actions/runs/41037238942/job/124001063884) | [2m55s](https://github.com/iree-org/iree/actions/runs/41037238942/job/124001063884) | 8 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 8 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41050722968/job/124045870860) | [2m47s](https://github.com/iree-org/iree/actions/runs/41037238942/job/124001063657) | [2m47s](https://github.com/iree-org/iree/actions/runs/41037238942/job/124001063657) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 8 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/41036360544/job/123998116965) | [2m41s](https://github.com/iree-org/iree/actions/runs/41037238942/job/124001063821) | [2m41s](https://github.com/iree-org/iree/actions/runs/41037238942/job/124001063821) | 8 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04 | `ubuntu-24.04` | 8 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41043326789/job/124021274042) | [2m34s](https://github.com/iree-org/iree/actions/runs/41037238942/job/124001063692) | [2m34s](https://github.com/iree-org/iree/actions/runs/41037238942/job/124001063692) | 8 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 8 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/41046100942/job/124031568053) | [2m25s](https://github.com/iree-org/iree/actions/runs/41037238942/job/124001063725) | [2m25s](https://github.com/iree-org/iree/actions/runs/41037238942/job/124001063725) | 8 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 8 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/41046100942/job/124031568239) | [2m23s](https://github.com/iree-org/iree/actions/runs/41037238942/job/124001063601) | [2m23s](https://github.com/iree-org/iree/actions/runs/41037238942/job/124001063601) | 8 |
| `.github/workflows/ci.yml` | linux_x64_clang_debug / linux_x64_clang_debug | `azure-linux-scale` | 3 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/41014176073/job/123926671275) | [2m18s](https://github.com/iree-org/iree/actions/runs/41036360544/job/123998117217) | [2m18s](https://github.com/iree-org/iree/actions/runs/41036360544/job/123998117217) | 3 |
| `.github/workflows/pkgci.yml` | Build Packages / Linux Release (x86_64) | `azure-linux-scale` | 8 | 0 | — | — | [1s](https://github.com/iree-org/iree/actions/runs/41046100908/job/124030853080) | [2m06s](https://github.com/iree-org/iree/actions/runs/41021907634/job/123975727889) | [2m06s](https://github.com/iree-org/iree/actions/runs/41021907634/job/123975727889) | 8 |
| `.github/workflows/ci.yml` | linux_x64_bazel / linux_x64_bazel | `azure-linux-scale` | 8 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/41050722968/job/124045871218) | [2m02s](https://github.com/iree-org/iree/actions/runs/41021907701/job/123975720528) | [2m02s](https://github.com/iree-org/iree/actions/runs/41021907701/job/123975720528) | 8 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 325 | 2% (8/325) |  | 41m41s ago |
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 268 | 3% (7/268) |  | 52m07s ago |

## Alerts

- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
