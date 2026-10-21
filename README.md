# iree-ci-monitor

_Updated: 2026-10-21 10:17 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `Linux,X64,rdna3` | self-hosted | 27 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | 0 | [51m47s](https://github.com/iree-org/iree/actions/runs/39595459103/job/119210108761) | [3h02m](https://github.com/iree-org/iree/actions/runs/39570078803/job/119125355587) | 0% (0/8) | `shark55-ci` |
| `Linux,X64,gfx1201` | self-hosted | 26 | 0 | — | — | 0 | [1h12m](https://github.com/iree-org/iree/actions/runs/39560004172/job/119091888914) | [2h21m](https://github.com/iree-org/iree/actions/runs/39572067963/job/119131600849) | 0% (0/8) | `shark75-ci` |
| `Linux,X64,gfx1100` | self-hosted | 28 | 2 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | 0 | [39m04s](https://github.com/iree-org/iree/actions/runs/39580992961/job/119161704876) | [1h50m](https://github.com/iree-org/iree/actions/runs/39570078803/job/119125355739) | 0% (0/8) | `shark55-ci` |
| `self-hosted,persistent-cache,Linux,X64` | self-hosted | 26 | 0 | — | — | 0 | [30m20s](https://github.com/iree-org/iree/actions/runs/39572112203/job/119133130767) | [1h41m](https://github.com/iree-org/iree/actions/runs/39572067963/job/119131600580) | 0% (0/8) | `shark55-ci`, `shark75-ci` |
| `Linux,X64,gfx1100,persistent-cache` | self-hosted | 13 | 0 | — | — | 0 | [14m32s](https://github.com/iree-org/iree/actions/runs/39570078803/job/119125355225) | [1h20m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615579) | 0% (0/4) | `shark55-ci` |
| `Linux,X64,gfx1201,persistent-cache` | self-hosted | 13 | 0 | — | — | 0 | [42m59s](https://github.com/iree-org/iree/actions/runs/39572067963/job/119131600698) | [1h03m](https://github.com/iree-org/iree/actions/runs/39570087898/job/119125295223) | 0% (0/4) | `shark75-ci` |
| `Linux,X64,iree-r9700` | self-hosted | 13 | 0 | — | — | 0 | [17m00s](https://github.com/iree-org/iree/actions/runs/39558502683/job/119094850099) | [45m45s](https://github.com/iree-org/iree/actions/runs/39580992961/job/119161704783) | 25% (1/4) | `shark75-ci` |
| `ubuntu-24.04-arm` | github-hosted | 39 | 0 | — | — | 0 | [6s](https://github.com/iree-org/iree/actions/runs/39572068017/job/119128533150) | [3m28s](https://github.com/iree-org/iree/actions/runs/39572112058/job/119129335843) | 0% (0/9) | 39 |
| `macos-15` | github-hosted | 40 | 0 | — | — | 0 | [10s](https://github.com/iree-org/iree/actions/runs/39590033759/job/119188474694) | [3m20s](https://github.com/iree-org/iree/actions/runs/39558502614/job/119092528721) | 0% (0/10) | 40 |
| `ubuntu-24.04` | github-hosted | 285 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39607316670/job/119279735446) | [2m54s](https://github.com/iree-org/iree/actions/runs/39570078784/job/119121853308) | 7% (5/72) | 275 |
| `windows-2022` | github-hosted | 39 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/39607316851/job/119246859735) | [2m20s](https://github.com/iree-org/iree/actions/runs/39558502614/job/119092528683) | 0% (0/9) | 39 |
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m35s](https://github.com/iree-org/iree/actions/runs/39577194480/job/119145546938) | [1m35s](https://github.com/iree-org/iree/actions/runs/39577194480/job/119145546938) | 100% (1/1) | 1 |
| `azure-linux-scale` | ossci | 84 | 0 | — | — | 1 | [8s](https://github.com/iree-org/iree/actions/runs/39572068017/job/119128533582) | [1m24s](https://github.com/iree-org/iree/actions/runs/39595459157/job/119206962294) | 5% (1/22) | 84 |
| `ubuntu-latest` | github-hosted | 42 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/39626276009/job/119312254010) | [1m15s](https://github.com/iree-org/iree/actions/runs/39572105377/job/119128578409) | 0% (0/9) | 42 |
| `azure-windows-scale` | ossci | 13 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/39595459157/job/119206962407) | [4s](https://github.com/iree-org/iree/actions/runs/39570087459/job/119121877993) | 33% (1/3) | 13 |
| `Linux,X64,iree-w7900` | self-hosted | 13 | 0 | — | — | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | `fix-spirv-wide-elementwise` | pull_request |
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | `fix-spirv-wide-elementwise` | pull_request |
| [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827580) | 2026-10-19 06:26 PDT | `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | `fix-spirv-wide-elementwise` | pull_request |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_vulkan_rdna3_O3 | `Linux,X64,rdna3` | 13 | 0 | — | — | [40m23s](https://github.com/iree-org/iree/actions/runs/39595459103/job/119210108995) | [3h02m](https://github.com/iree-org/iree/actions/runs/39570078803/job/119125355587) | [3h35m](https://github.com/iree-org/iree/actions/runs/39558502683/job/119094850624) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_vulkan_rdna3_O0 | `Linux,X64,rdna3` | 14 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827420) | 2026-10-19 06:26 PDT | [1h07m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615660) | [2h32m](https://github.com/iree-org/iree/actions/runs/39560004172/job/119091888867) | [2h32m](https://github.com/iree-org/iree/actions/runs/39560004172/job/119091888867) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna4_O3 | `Linux,X64,gfx1201` | 13 | 0 | — | — | [1h12m](https://github.com/iree-org/iree/actions/runs/39560004172/job/119091888914) | [2h21m](https://github.com/iree-org/iree/actions/runs/39572067963/job/119131600849) | [2h21m](https://github.com/iree-org/iree/actions/runs/39572067963/job/119131600849) | 1 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1201_O3 | `Linux,X64,gfx1201` | 13 | 0 | — | — | [1h13m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615692) | [2h16m](https://github.com/iree-org/iree/actions/runs/39572067963/job/119131600812) | [2h26m](https://github.com/iree-org/iree/actions/runs/39570078803/job/119125355616) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: cpu_llvm_task | `self-hosted,persistent-cache,Linux,X64` | 13 | 0 | — | — | [20m49s](https://github.com/iree-org/iree/actions/runs/39580992961/job/119161704944) | [1h51m](https://github.com/iree-org/iree/actions/runs/39570087898/job/119125295877) | [1h51m](https://github.com/iree-org/iree/actions/runs/39570087898/job/119125295877) | 2 |
| `.github/workflows/pkgci.yml` | Test Torch / test_torch_ops :: amdgpu_hip_gfx1100_O3 | `Linux,X64,gfx1100` | 14 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827336) | 2026-10-19 06:26 PDT | [46m26s](https://github.com/iree-org/iree/actions/runs/39572112203/job/119133130664) | [1h50m](https://github.com/iree-org/iree/actions/runs/39570078803/job/119125355739) | [2h39m](https://github.com/iree-org/iree/actions/runs/39572067963/job/119131600711) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_ops :: amdgpu_hip_rdna3_O3 | `Linux,X64,gfx1100` | 14 | 1 | [53m29s](https://github.com/iree-org/iree/actions/runs/39246616119/job/118060827580) | 2026-10-19 06:26 PDT | [38m41s](https://github.com/iree-org/iree/actions/runs/39572112203/job/119133130655) | [1h39m](https://github.com/iree-org/iree/actions/runs/39572067963/job/119131600622) | [1h41m](https://github.com/iree-org/iree/actions/runs/39570078803/job/119125355613) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna3 | `Linux,X64,gfx1100,persistent-cache` | 13 | 0 | — | — | [14m32s](https://github.com/iree-org/iree/actions/runs/39570078803/job/119125355225) | [1h20m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615579) | [1h33m](https://github.com/iree-org/iree/actions/runs/39570087898/job/119125295371) | 1 |
| `.github/workflows/pkgci.yml` | Test ONNX / test_onnx_models :: amdgpu_hip_rdna4 | `Linux,X64,gfx1201,persistent-cache` | 13 | 0 | — | — | [42m59s](https://github.com/iree-org/iree/actions/runs/39572067963/job/119131600698) | [1h03m](https://github.com/iree-org/iree/actions/runs/39570087898/job/119125295223) | [1h07m](https://github.com/iree-org/iree/actions/runs/39596897988/job/119214615750) | 1 |
| `.github/workflows/pkgci.yml` | Test AMD R9700 / test_r9700 | `Linux,X64,iree-r9700` | 13 | 0 | — | — | [17m00s](https://github.com/iree-org/iree/actions/runs/39558502683/job/119094850099) | [45m45s](https://github.com/iree-org/iree/actions/runs/39580992961/job/119161704783) | [1h23m](https://github.com/iree-org/iree/actions/runs/39572067963/job/119131600660) | 1 |
| `.github/workflows/pkgci.yml` | Test Sharktank / sharktank_tests :: cpu_task | `self-hosted,persistent-cache,Linux,X64` | 13 | 0 | — | — | [35m49s](https://github.com/iree-org/iree/actions/runs/39580992961/job/119161705088) | [44m27s](https://github.com/iree-org/iree/actions/runs/39595459103/job/119210108857) | [58m01s](https://github.com/iree-org/iree/actions/runs/39593998836/job/119205283281) | 2 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: tracy | `ubuntu-24.04-arm` | 13 | 0 | — | — | [36s](https://github.com/iree-org/iree/actions/runs/39572068017/job/119128533505) | [4m58s](https://github.com/iree-org/iree/actions/runs/39570087459/job/119121879353) | [4m58s](https://github.com/iree-org/iree/actions/runs/39570087459/job/119121879353) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04-arm :: console | `ubuntu-24.04-arm` | 13 | 0 | — | — | [6s](https://github.com/iree-org/iree/actions/runs/39572068017/job/119128533260) | [4m34s](https://github.com/iree-org/iree/actions/runs/39570087459/job/119121879236) | [4m34s](https://github.com/iree-org/iree/actions/runs/39570087459/job/119121879236) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: console | `ubuntu-24.04` | 13 | 0 | — | — | [1m44s](https://github.com/iree-org/iree/actions/runs/39596898107/job/119211419199) | [4m32s](https://github.com/iree-org/iree/actions/runs/39570087459/job/119121879459) | [4m32s](https://github.com/iree-org/iree/actions/runs/39570087459/job/119121879459) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: ubuntu-24.04 :: tracy | `ubuntu-24.04` | 13 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/39607316851/job/119246860003) | [4m24s](https://github.com/iree-org/iree/actions/runs/39570087459/job/119121879391) | [4m24s](https://github.com/iree-org/iree/actions/runs/39570087459/job/119121879391) | 13 |
| `.github/workflows/ci.yml` | runtime :: macos-15 | `macos-15` | 13 | 0 | — | — | [10s](https://github.com/iree-org/iree/actions/runs/39570078784/job/119121853075) | [4m18s](https://github.com/iree-org/iree/actions/runs/39572112058/job/119129336333) | [4m18s](https://github.com/iree-org/iree/actions/runs/39572112058/job/119129336333) | 13 |
| `.github/workflows/ci.yml` | runtime_wasm :: wasm32 | `ubuntu-24.04` | 14 | 0 | — | — | [51s](https://github.com/iree-org/iree/actions/runs/39570078784/job/119121853149) | [3m59s](https://github.com/iree-org/iree/actions/runs/39570087459/job/119121876717) | [3m59s](https://github.com/iree-org/iree/actions/runs/39570087459/job/119121876717) | 13 |
| `.github/workflows/ci.yml` | runtime_tracing :: macos-15 :: console | `macos-15` | 13 | 0 | — | — | [1m24s](https://github.com/iree-org/iree/actions/runs/39595459157/job/119206961793) | [3m30s](https://github.com/iree-org/iree/actions/runs/39572112058/job/119129335972) | [3m30s](https://github.com/iree-org/iree/actions/runs/39572112058/job/119129335972) | 13 |
| `.github/workflows/ci.yml` | runtime :: ubuntu-24.04-arm | `ubuntu-24.04-arm` | 13 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/39607316851/job/119246859815) | [3m28s](https://github.com/iree-org/iree/actions/runs/39572112058/job/119129335843) | [3m28s](https://github.com/iree-org/iree/actions/runs/39572112058/job/119129335843) | 13 |
| `.github/workflows/ci.yml` | runtime_small | `ubuntu-24.04` | 14 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/39631204737/job/119329680830) | [3m07s](https://github.com/iree-org/iree/actions/runs/39572068017/job/119128533382) | [3m07s](https://github.com/iree-org/iree/actions/runs/39572068017/job/119128533382) | 13 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 401 | 2% (9/401) |  | 1h18m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 473 | 1% (3/473) |  | 1h23m ago |

## Alerts

- **[queue-starved]** `Linux,X64,gfx1100,persistent-cache` p95 queue 1h20m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1100` p95 queue 1h50m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201,persistent-cache` p95 queue 1h03m (> 1h00m)
- **[queue-starved]** `Linux,X64,gfx1201` p95 queue 2h21m (> 1h00m)
- **[queue-starved]** `Linux,X64,rdna3` p95 queue 3h02m (> 1h00m)
- **[queue-starved]** `self-hosted,persistent-cache,Linux,X64` p95 queue 1h41m (> 1h00m)
- **[spof]** `Linux,X64,gfx1100,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1100` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201,persistent-cache` single runner observed in last 7d
- **[spof]** `Linux,X64,gfx1201` single runner observed in last 7d
- **[spof]** `Linux,X64,iree-r9700` single runner observed in last 7d
- **[spof]** `Linux,X64,rdna3` single runner observed in last 7d

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
