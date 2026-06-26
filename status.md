# Status detail

_Updated: 2026-06-26 06:04 PDT_ — watching `iree-org/iree`, queue samples = last 10h, queued observations = up to 3d

## Per-label metrics

| label | type | jobs | queued | oldest queued | seen | running | oldest running | avg | p50 | p95 | max | all-jobs fail | main-only fail | runners | SPOF |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | — | 1m25s | [1m25s](https://github.com/iree-org/iree/actions/runs/28232150756/job/83638239393) | [1m25s](https://github.com/iree-org/iree/actions/runs/28232150756/job/83638239393) | [1m25s](https://github.com/iree-org/iree/actions/runs/28232150756/job/83638239393) | 0% (0/1) | 0% (0/1) | 1 |  |
| `ubuntu-24.04-arm` | github-hosted | 3 | 0 | — | — | 0 | — | 4s | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051276) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051316) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051316) | 0% (0/3) | — | 3 |  |
| `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | [2h41m](https://github.com/iree-org/iree/actions/runs/28232118098/job/83638137400) | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28232118098/job/83638137400) | [5s](https://github.com/iree-org/iree/actions/runs/28232118098/job/83638137400) | [5s](https://github.com/iree-org/iree/actions/runs/28232118098/job/83638137400) | — | — | 1 |  |
| `ubuntu-latest` | github-hosted | 9 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28237862968/job/83657015153) | [4s](https://github.com/iree-org/iree/actions/runs/28237632624/job/83656254835) | [4s](https://github.com/iree-org/iree/actions/runs/28237632624/job/83656254835) | 22% (2/9) | — | 9 |  |
| `ubuntu-24.04` | github-hosted | 15 | 0 | — | — | 2 | [2h41m](https://github.com/iree-org/iree/actions/runs/28232152114/job/83638243948) | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051304) | [3s](https://github.com/iree-org/iree/actions/runs/28237532199/job/83656118243) | [3s](https://github.com/iree-org/iree/actions/runs/28237597529/job/83656139911) | 15% (2/13) | 50% (2/4) | 15 |  |
| `macos-14` | github-hosted | 3 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28232128133/job/83638169145) | [3s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051301) | [3s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051301) | 0% (0/3) | 0% (0/1) | 3 |  |
| `windows-2022` | github-hosted | 2 | 0 | — | — | 0 | — | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051291) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051295) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051295) | 0% (0/2) | — | 2 |  |
| `azure-linux-scale` | ossci | 2 | 0 | — | — | 0 | — | 1s | [1s](https://github.com/iree-org/iree/actions/runs/28232151910/job/83638243023) | [2s](https://github.com/iree-org/iree/actions/runs/28232090631/job/83638047714) | [2s](https://github.com/iree-org/iree/actions/runs/28232090631/job/83638047714) | 50% (1/2) | 50% (1/2) | 2 |  |
| `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 1 | [23h26m](https://github.com/iree-org/iree/actions/runs/28172319267/job/83446011596) | 2026-06-26 06:03 PDT | 0 | — | 0s | 0s | 0s | 0s | — | — | 0 |  |

## Longest observed queued jobs (last 3d)

| wait | observed | workflow | job | labels | branch | event |
|---:|---:|---|---|---|---|---|
| [23h26m](https://github.com/iree-org/iree/actions/runs/28172319267/job/83446011596) | 2026-06-26 06:03 PDT | `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | `main` | push |

## Workflow/job waiting time

Aggregated by workflow file/name, job name, and exact `runs-on` label set. This exposes cases where one CI job is constrained more tightly than the broader label pool.

| workflow | job | labels | type | jobs | queued | oldest queued | seen | running | avg | p50 | p95 | max | runners |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `.github/workflows/pkgci.yml` | Test AMD MI355 / test_mi355 | `linux-mi35x-1gpu-ossci-iree-org` | ossci | 1 | 1 | [23h26m](https://github.com/iree-org/iree/actions/runs/28172319267/job/83446011596) | 2026-06-26 06:03 PDT | 0 | 0s | 0s | 0s | 0s | 0 |
| `.github/workflows/ci_linux_arm64_clang.yml` | linux_arm64_clang | `ah-ubuntu_22_04-c7g_4x-50` | github-hosted | 1 | 0 | — | — | 0 | 1m25s | [1m25s](https://github.com/iree-org/iree/actions/runs/28232150756/job/83638239393) | [1m25s](https://github.com/iree-org/iree/actions/runs/28232150756/job/83638239393) | [1m25s](https://github.com/iree-org/iree/actions/runs/28232150756/job/83638239393) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build main-dist-linux Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051316) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051316) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051316) | 1 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-runtime-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051276) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051276) | [5s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051276) | 1 |
| `.github/workflows/ci_macos_x64_clang.yml` | macos_x64_clang | `macos-15-intel` | github-hosted | 1 | 0 | — | — | 1 | 5s | [5s](https://github.com/iree-org/iree/actions/runs/28232118098/job/83638137400) | [5s](https://github.com/iree-org/iree/actions/runs/28232118098/job/83638137400) | [5s](https://github.com/iree-org/iree/actions/runs/28232118098/job/83638137400) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (actions) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/28237863555/job/83656991185) | [4s](https://github.com/iree-org/iree/actions/runs/28237632624/job/83656254835) | [4s](https://github.com/iree-org/iree/actions/runs/28237632624/job/83656254835) | 2 |
| `.github/workflows/build_package.yml` | linux-aarch64 :: Build py-compiler-pkg Package | `ubuntu-24.04-arm` | github-hosted | 1 | 0 | — | — | 0 | 4s | [4s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051279) | [4s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051279) | [4s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051279) | 1 |
| `dynamic/github-code-scanning/codeql` | Analyze (javascript) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28237632624/job/83656254871) | [3s](https://github.com/iree-org/iree/actions/runs/28237863555/job/83656991218) | [3s](https://github.com/iree-org/iree/actions/runs/28237863555/job/83656991218) | 2 |
| `dynamic/github-code-scanning/codeql` | Analyze (python) | `ubuntu-latest` | github-hosted | 2 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28237632624/job/83656254822) | [3s](https://github.com/iree-org/iree/actions/runs/28237863555/job/83656991195) | [3s](https://github.com/iree-org/iree/actions/runs/28237863555/job/83656991195) | 2 |
| `.github/workflows/build_package.yml` | macos :: Build py-compiler-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051301) | [3s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051301) | [3s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051301) | 1 |
| `.github/workflows/publish_website.yml` | publish_website | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/28237597529/job/83656139911) | [3s](https://github.com/iree-org/iree/actions/runs/28237597529/job/83656139911) | [3s](https://github.com/iree-org/iree/actions/runs/28237597529/job/83656139911) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 3s | [3s](https://github.com/iree-org/iree/actions/runs/28237532199/job/83656118243) | [3s](https://github.com/iree-org/iree/actions/runs/28237532199/job/83656118243) | [3s](https://github.com/iree-org/iree/actions/runs/28237532199/job/83656118243) | 1 |
| `.github/workflows/build_package.yml` | Trigger validate and publish release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83655910793) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83655910793) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83655910793) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build main-dist-linux Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051300) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051300) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051300) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-compiler-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051304) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051304) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051304) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-runtime-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051305) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051305) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051305) | 1 |
| `.github/workflows/build_package.yml` | linux-x86_64 :: Build py-tf-compiler-tools-pkg Package | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051332) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051332) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051332) | 1 |
| `.github/workflows/build_package.yml` | macos :: Build py-runtime-pkg Package | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051325) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051325) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051325) | 1 |
| `.github/workflows/build_package.yml` | setup_metadata | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603031487) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603031487) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603031487) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-compiler-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051291) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051291) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051291) | 1 |
| `.github/workflows/build_package.yml` | windows :: Build py-runtime-pkg Package | `windows-2022` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051295) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051295) | [2s](https://github.com/iree-org/iree/actions/runs/28221312301/job/83603051295) | 1 |
| `.github/workflows/ci_linux_x64_clang_debug.yml` | linux_x64_clang_debug | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28232090631/job/83638047714) | [2s](https://github.com/iree-org/iree/actions/runs/28232090631/job/83638047714) | [2s](https://github.com/iree-org/iree/actions/runs/28232090631/job/83638047714) | 1 |
| `.github/workflows/ci_linux_x64_gcc.yml` | linux_x64_gcc | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28232162673/job/83638276214) | [2s](https://github.com/iree-org/iree/actions/runs/28232162673/job/83638276214) | [2s](https://github.com/iree-org/iree/actions/runs/28232162673/job/83638276214) | 1 |
| `.github/workflows/ci_macos_arm64_clang.yml` | macos_arm64_clang | `macos-14` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28232128133/job/83638169145) | [2s](https://github.com/iree-org/iree/actions/runs/28232128133/job/83638169145) | [2s](https://github.com/iree-org/iree/actions/runs/28232128133/job/83638169145) | 1 |
| `.github/workflows/samples.yml` | colab | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83597228962) | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83597228962) | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83597228962) | 1 |
| `.github/workflows/samples.yml` | samples | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83597228950) | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83597228950) | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83597228950) | 1 |
| `.github/workflows/samples.yml` | samples_summary / summary | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83598184239) | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83598184239) | [2s](https://github.com/iree-org/iree/actions/runs/28219425687/job/83598184239) | 1 |
| `.github/workflows/schedule_candidate_release.yml` | Tag candidate release | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28221278784/job/83602925806) | [2s](https://github.com/iree-org/iree/actions/runs/28221278784/job/83602925806) | [2s](https://github.com/iree-org/iree/actions/runs/28221278784/job/83602925806) | 1 |
| `.github/workflows/validate_and_publish_release.yml` | Validate packages | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28237532199/job/83655926688) | [2s](https://github.com/iree-org/iree/actions/runs/28237532199/job/83655926688) | [2s](https://github.com/iree-org/iree/actions/runs/28237532199/job/83655926688) | 1 |
| `dynamic/pages/pages-build-deployment` | build | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28237862968/job/83656990138) | [2s](https://github.com/iree-org/iree/actions/runs/28237862968/job/83656990138) | [2s](https://github.com/iree-org/iree/actions/runs/28237862968/job/83656990138) | 1 |
| `dynamic/pages/pages-build-deployment` | deploy | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28237862968/job/83657015148) | [2s](https://github.com/iree-org/iree/actions/runs/28237862968/job/83657015148) | [2s](https://github.com/iree-org/iree/actions/runs/28237862968/job/83657015148) | 1 |
| `dynamic/pages/pages-build-deployment` | report-build-status | `ubuntu-latest` | github-hosted | 1 | 0 | — | — | 0 | 2s | [2s](https://github.com/iree-org/iree/actions/runs/28237862968/job/83657015153) | [2s](https://github.com/iree-org/iree/actions/runs/28237862968/job/83657015153) | [2s](https://github.com/iree-org/iree/actions/runs/28237862968/job/83657015153) | 1 |
| `.github/workflows/ci_linux_x64_clang_byollvm.yml` | linux_x64_clang_byollvm | `ubuntu-24.04` | github-hosted | 1 | 0 | — | — | 1 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/28232152114/job/83638243948) | [1s](https://github.com/iree-org/iree/actions/runs/28232152114/job/83638243948) | [1s](https://github.com/iree-org/iree/actions/runs/28232152114/job/83638243948) | 1 |
| `.github/workflows/ci_linux_x64_clang_tsan.yml` | linux_x64_clang_tsan | `azure-linux-scale` | ossci | 1 | 0 | — | — | 0 | 1s | [1s](https://github.com/iree-org/iree/actions/runs/28232151910/job/83638243023) | [1s](https://github.com/iree-org/iree/actions/runs/28232151910/job/83638243023) | [1s](https://github.com/iree-org/iree/actions/runs/28232151910/job/83638243023) | 1 |

## Per-runner metrics (self-hosted, last 7d)

Only runners that served at least one label with ≤ 15 distinct runners in the lookback window are listed. Ephemeral auto-scaler workers (ubuntu-*, azure-*, macos-*, mi325, etc.) are summarized by label above.

| runner | labels | jobs | ok | fail | cancelled | fail rate | running | last seen |
|---|---|---:|---:|---:|---:|---:|:---:|---:|
| `shark75-ci` | `Linux,X64,gfx1201`, `Linux,X64,gfx1201,persistent-cache`, `Linux,X64,iree-r9700`, `self-hosted,persistent-cache,Linux,X64` | 123 | 122 | 0 | 1 | 0% |  | 22h56m ago |
| `shark01-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 94 | 93 | 0 | 1 | 0% |  | 23h00m ago |
| `shark10-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,iree-w7900`, `Linux,X64,iree-w7900x2,persistent-cache`, `Linux,X64,rdna3`, `Linux,X64,rdna3,persistent-cache,shark10-ci`, `self-hosted,persistent-cache,Linux,X64`, `self-hosted,persistent-cache,Linux,X64,threadripper` | 102 | 96 | 6 | 0 | 6% |  | 23h01m ago |
| `shark55-ci` | `Linux,X64,gfx1100`, `Linux,X64,gfx1100,persistent-cache`, `Linux,X64,rdna3`, `self-hosted,persistent-cache,Linux,X64` | 86 | 86 | 0 | 0 | 0% |  | 23h01m ago |
| `iree-mi308-1` | `nodai-amdgpu-mi308-x86-64` | 27 | 27 | 0 | 0 | 0% |  | 23h13m ago |

## Alerts

- **[stale-queued]** `linux-mi35x-1gpu-ossci-iree-org` oldest queued job observed waiting 23h26m (> 2h00m)

## Methodology

- Window: last 10 hours of job records for queue-time percentiles and failure metrics; queued observations are scanned for 3 days; last 7 days for runner metrics and SPOF.
- Timestamps rendered in `America/Los_Angeles` local time; underlying records are UTC.
- Queue time: `started_at - created_at`. Skipped jobs excluded.
- Queued: jobs with `status == queued` or `waiting` (not yet assigned a runner).
- Running: jobs with `status == in_progress` (runner assigned, executing).
- Oldest queued: `collected_at - created_at` for the oldest job observed with `status == queued` or `waiting`. This is only updated by collection; rerunning the reporter does not inflate stale queued snapshots.
- Workflow/job waiting time: same queue-time definition, grouped by stable workflow id/name + job name + exact label set. Older records collected before `workflow_path` was stored fall back to `workflow_name`.
- All-jobs fail rate: over every completed job (PR + push + schedule).
- Main-only fail rate: subset where `head_branch == main` and `event != pull_request` — post-merge, scheduled, and workflow_dispatch runs. PR noise excluded.
- Runner type:
  - `self-hosted`: persistent physical hosts managed by the IREE infra team (shark fleet, `iree-mi308-1`, etc.). The `runners` count is the number of physical boxes.
  - `github-hosted`: GitHub's standard runner pool (`ubuntu-*`, `macos-*`, `windows-*`) and Actions Hosting partners (`ah-*`). Ephemeral — one worker per job.
  - `ossci`: org-managed autoscaler pools (`azure-*`, `*-ossci-iree-org`). Ephemeral — one worker per job, so the `runners` count here is really "pod spawns in the window" not physical capacity.
- SPOF: label has seen only one distinct `runner_name` in the last 7 days.
- Persistent runner: ran ≥ 5 jobs in the lookback window AND served at least one label with ≤ 15 distinct runners. Ephemeral auto-scaler worker names (which appear once per spawn) are excluded.
- Re-runs: `(job_id, run_attempt)` tuples are distinct; a re-run counts as a new job.

## Alert thresholds

- `queue-starved`: p95 queue > 1h00m
- `stale-queued`: oldest observed queued job (not yet started) > 2h00m
- `high-failure-main`: main-only failure rate > 20% with ≥ 10 completed main-only jobs
- `spof`: only one distinct runner in last 7d
