# iree-ci-monitor

_Updated: 2026-06-26 06:04 PDT_ — `iree-org/iree`, queue samples last 10h; queued observations up to 3d

Automated tracker of GitHub Actions runner health for the IREE project. 
Each tick, the collector pulls new run+job metadata via the GitHub REST API and the reporter regenerates this page.
The static benchmark dashboard is generated under [`docs/`](docs/) from PkgCI benchmark summary artifacts and can be published with GitHub Pages.

## Top of queue (sorted by p95, last 10h)

| label | type | jobs | queued | oldest queued | seen | running | p50 queue | p95 queue | main fail rate | runners |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | [1m25s](https://github.com/iree-org/iree/actions/runs/28232150756/job/83638239393) | [1m25s](https://github.com/iree-org/iree/actions/runs/28232150756/job/83638239393) | 0% (0/1) | 1 |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051276) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051316) | — | 3 |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [5s](https://github.com/iree-org/iree/actions/runs/28232118098/job/83638137400) | [5s](https://github.com/iree-org/iree/actions/runs/28232118098/job/83638137400) | — | 1 |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28237862968/job/83657015153) | [4s](https://github.com/iree-org/iree/actions/runs/28237632624/job/83656254835) | — | 9 |
| `ubuntu-24.04` | github-hosted | 15 | 0 | — | — | 2 | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051304) | [3s](https://github.com/iree-org/iree/actions/runs/28237532199/job/83656118243) | 50% (2/4) | 15 |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28232128133/job/83638169145) | [3s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051301) | 0% (0/1) | 3 |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051291) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051295) | — | 2 |
| `azure-linux-scale` | ossci | 2 | 0 | — | — | 0 | [1s](https://github.com/iree-org/iree/actions/runs/28232151910/job/83638243023) | [2s](https://github.com/iree-org/iree/actions/runs/28232090631/job/83638047714) | 50% (1/2) | 2 |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 1 | [23h26m](https://github.com/iree-org/iree/actions/runs/28172319267/job/83446011596) | 2026-06-26 06:03 PDT | 0 | 0s | 0s | — | 0 |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [23h26m](https://github.com/iree-org/iree/actions/runs/28172319267/job/83446011596) | 2026-06-26 06:03 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time (samples last 10h, queued observations up to 3d)

| workflow | job | labels | jobs | queued | oldest queued | seen | p50 queue | p95 queue | max queue | runners |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | 1 | 1 | [23h26m](https://github.com/iree-org/iree/actions/runs/28172319267/job/83446011596) | 2026-06-26 06:03 PDT | 0s | 0s | 0s | 0 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | 1 | 0 | — | — | [1m25s](https://github.com/iree-org/iree/actions/runs/28232150756/job/83638239393) | [1m25s](https://github.com/iree-org/iree/actions/runs/28232150756/job/83638239393) | [1m25s](https://github.com/iree-org/iree/actions/runs/28232150756/job/83638239393) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051316) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051316) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051316) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051276) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051276) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051276) | 1 |
| `.github/workflows/ci_macos_x64_clang.yml` | macos_x64_clang | `macos-15-intel` | 1 | 0 | — | — | [5s](https://github.com/iree-org/iree/actions/runs/28232118098/job/83638137400) | [5s](https://github.com/iree-org/iree/actions/runs/28232118098/job/83638137400) | [5s](https://github.com/iree-org/iree/actions/runs/28232118098/job/83638137400) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | 2 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28237863555/job/83656991185) | [4s](https://github.com/iree-org/iree/actions/runs/28237632624/job/83656254835) | [4s](https://github.com/iree-org/iree/actions/runs/28237632624/job/83656254835) | 2 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | 1 | 0 | — | — | [4s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051279) | [4s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051279) | [4s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051279) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28237632624/job/83656254871) | [3s](https://github.com/iree-org/iree/actions/runs/28237863555/job/83656991218) | [3s](https://github.com/iree-org/iree/actions/runs/28237863555/job/83656991218) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | 2 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28237632624/job/83656254822) | [3s](https://github.com/iree-org/iree/actions/runs/28237863555/job/83656991195) | [3s](https://github.com/iree-org/iree/actions/runs/28237863555/job/83656991195) | 2 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051301) | [3s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051301) | [3s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051301) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28237597529/job/83656139911) | [3s](https://github.com/iree-org/iree/actions/runs/28237597529/job/83656139911) | [3s](https://github.com/iree-org/iree/actions/runs/28237597529/job/83656139911) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | 1 | 0 | — | — | [3s](https://github.com/iree-org/iree/actions/runs/28237532199/job/83656118243) | [3s](https://github.com/iree-org/iree/actions/runs/28237532199/job/83656118243) | [3s](https://github.com/iree-org/iree/actions/runs/28237532199/job/83656118243) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83655910793) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83655910793) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83655910793) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051300) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051300) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051300) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051304) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051304) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051304) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051305) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051305) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051305) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051332) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051332) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051332) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051325) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051325) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051325) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603031487) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603031487) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603031487) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | 1 | 0 | — | — | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051291) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051291) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051291) | 1 |

## Self-hosted runners (last 7d)

| runner | labels | jobs | fail rate | running | last seen |
|---|---|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 123 | 0% (0/123) |  | 22h56m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 94 | 0% (0/94) |  | 23h00m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 102 | 6% (6/102) |  | 23h01m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 86 | 0% (0/86) |  | 23h01m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 27 | 0% (0/27) |  | 23h13m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 23h26m (> 2h00m)

See [`status.md`](status.md) for the full per-label breakdown including all-jobs failure rates, methodology, and thresholds. See [`daily.md`](daily.md) for a snapshot of the most recently completed Pacific calendar day. See [`docs/README.md`](docs/README.md) for dashboard generation, local viewing, and chart interaction notes.
