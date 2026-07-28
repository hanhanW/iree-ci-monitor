# iree-ci-monitor

_Updated: 2026-07-28 05:57 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [2m21s](https://github.com/iree-org/iree/actions/runs/30349494988/job/90243373949) | [2m21s](https://github.com/iree-org/iree/actions/runs/30349494988/job/90243373949) | 0% (0/1) | 1 |
| `ubuntu-24.04` | github-hosted | 16 | 0 | — | — | 1 | [2s](https://github.com/iree-org/iree/actions/runs/30349504039/job/90243402861) | [8s](https://github.com/iree-org/iree/actions/runs/30356232018/job/90264967233) | 20% (1/5) | 15 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [3s](https://github.com/iree-org/iree/actions/runs/30356608481/job/90266171467) | [8s](https://github.com/iree-org/iree/actions/runs/30356275247/job/90265108665) | — | 9 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993221) | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993235) | — | 2 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993391) | [3s](https://github.com/iree-org/iree/actions/runs/30349471136/job/90243294763) | — | 3 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [3s](https://github.com/iree-org/iree/actions/runs/30349457314/job/90243249525) | [3s](https://github.com/iree-org/iree/actions/runs/30349457314/job/90243249525) | — | 1 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993250) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993260) | — | 3 |
| `azure-linux-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/30349485701/job/90243342515) | [2s](https://github.com/iree-org/iree/actions/runs/30349405394/job/90243081062) | 0% (0/2) | 2 |

## Longest observed queued jobs (last 3d)

_No queued jobs observed._

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [2m21s](https://github.com/iree-org/iree/actions/runs/30349494988/job/90243373949) | [2m21s](https://github.com/iree-org/iree/actions/runs/30349494988/job/90243373949) | [2m21s](https://github.com/iree-org/iree/actions/runs/30349494988/job/90243373949) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [9s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993236) | [9s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993236) | [9s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993236) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30356608481/job/90266171555) | [8s](https://github.com/iree-org/iree/actions/runs/30356275247/job/90265108559) | [8s](https://github.com/iree-org/iree/actions/runs/30356275247/job/90265108559) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30356608481/job/90266171451) | [8s](https://github.com/iree-org/iree/actions/runs/30356275247/job/90265108665) | [8s](https://github.com/iree-org/iree/actions/runs/30356275247/job/90265108665) | 2 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993206) | [8s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993206) | [8s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993206) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30356232018/job/90264967233) | [8s](https://github.com/iree-org/iree/actions/runs/30356232018/job/90264967233) | [8s](https://github.com/iree-org/iree/actions/runs/30356232018/job/90264967233) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | 1 | 0 | — | — | [8s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90185273679) | [8s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90185273679) | [8s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90185273679) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | 1 | 0 | — | — | [7s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90185273750) | [7s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90185273750) | [7s](https://github.com/iree-org/iree/actions/runs/30330793418/job/90185273750) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/30356607715/job/90266181590) | [5s](https://github.com/iree-org/iree/actions/runs/30356607715/job/90266181590) | [5s](https://github.com/iree-org/iree/actions/runs/30356607715/job/90266181590) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30356275247/job/90265108753) | [3s](https://github.com/iree-org/iree/actions/runs/30356608481/job/90266171467) | [3s](https://github.com/iree-org/iree/actions/runs/30356608481/job/90266171467) | 2 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993391) | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993391) | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993391) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993235) | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993235) | [3s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993235) | 1 |
| `.github/workflows/ci_macos_arm64_clang.yml` | macos_arm64_clang | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30349471136/job/90243294763) | [3s](https://github.com/iree-org/iree/actions/runs/30349471136/job/90243294763) | [3s](https://github.com/iree-org/iree/actions/runs/30349471136/job/90243294763) | 1 |
| `.github/workflows/ci_macos_x64_clang.yml` | macos_x64_clang | `macos-15-intel` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30349457314/job/90243249525) | [3s](https://github.com/iree-org/iree/actions/runs/30349457314/job/90243249525) | [3s](https://github.com/iree-org/iree/actions/runs/30349457314/job/90243249525) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/30356607715/job/90266227764) | [3s](https://github.com/iree-org/iree/actions/runs/30356607715/job/90266227764) | [3s](https://github.com/iree-org/iree/actions/runs/30356607715/job/90266227764) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90264647550) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90264647550) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90264647550) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993245) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993245) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993245) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993260) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993260) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993260) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993250) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993250) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993250) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993293) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993293) | [2s](https://github.com/iree-org/iree/actions/runs/30333338187/job/90192993293) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 328 | 2% (5/328) |  | 1d01h ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 252 | 1% (2/252) |  | 1d01h ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 265 | 5% (14/265) |  | 1d01h ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 238 | 2% (4/238) |  | 1d01h ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 75 | 3% (2/75) |  | 1d01h ago |

## Alerts

_No active alerts._

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
