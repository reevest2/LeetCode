# CLAUDE.md

## Project Overview

Educational LeetCode solutions repository. 394 problems with study guides and solution templates in 7 languages: Python, C#, C, C++, x86-64 Assembly, ARM64 Assembly, RISC-V Assembly.

Most solutions are currently stubs (`TODO: implement`). The goal is to learn good programming holistically.

## Repository Structure

```
problems/NNNN-problem-name/
  README.md          # Study guide (problem statement, pattern, approach, pitfalls)
  python/solution.py
  csharp/Solution.cs
  c/solution.c
  cpp/solution.cpp
  x86_64/solution.asm
  arm64/solution.s
  riscv/solution.s
scripts/
  generate.py        # Generates problem scaffolding from Excel
  ci/                # CI validation scripts
tests/               # Test infrastructure (pytest, gcc, g++)
.github/
  workflows/ci.yml   # GitHub Actions CI pipeline
  PULL_REQUEST_TEMPLATE.md
  ISSUE_TEMPLATE/    # Bug, feature, solution request templates
```

## Conventions

### Branch Naming

```
<type>/<problem-number>-<short-description>
```

Types: `solve`, `fix`, `docs`, `feat`, `chore`

Examples: `solve/0001-two-sum-python`, `fix/0042-trapping-rain-water-cpp`

### Commit Messages

```
<type>(<scope>): <description>
```

- Types: `solve`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- Imperative mood, no capital, no period, max 72 chars
- Example: `solve(0001): implement two sum in python`

### Pull Requests

- One problem per PR, no exceptions
- Must be accepted on LeetCode before submitting
- Fill out the PR template completely

## Code Quality Rules

Read CODE_QUALITY.md for full details. Key rules:

### Banned Variable Names

`tmp`, `temp`, `data`, `info`, `stuff`, `flag`, `check`, `val`, `arr`, `d`, `m`, `mp`, `l`, `ans`, `res`, `ret`

### Per-Language Rules

- **Python**: Type hints required, `list[int]` not `List[int]`, no bare `except`
- **C#**: K&R braces (not Allman), `var` only when type is obvious, no `dynamic`
- **C**: No VLAs, free all allocations, `const` for unmodified params, check NULL pointers
- **C++**: `const&` for unmodified params, `unordered_map` over `map` unless ordering needed, no raw `new`/`delete`, no `goto`
- **Assembly**: Register documentation required at function entry, descriptive labels (not `.L1`), calling convention compliance

### Universal

- No debug output in submitted solutions
- No commented-out code
- No TODO comments in submitted solutions
- Preserve file headers (problem link, pattern, hints)
- Handle edge cases explicitly
- Meaningful variable names (loop counters `i`/`j`/`k` and `n`/`m` for sizes are OK)

## When Implementing a Solution

1. Read the study guide (`README.md`) first
2. Understand the optimal approach before coding
3. Preserve the file header comments
4. Follow the optimal approach from the study guide
5. Use meaningful variable names per CODE_QUALITY.md
6. Handle all edge cases listed in the study guide
7. Verify it compiles without warnings
8. Remove all debug output and TODOs

## Style

- Line endings: LF everywhere
- Indentation: 4 spaces (2 for YAML/JSON)
- Line length: Python 100, C# 120, C/C++ 100, Assembly 100
- Braces: K&R style (same-line opening) for C, C++, and C#
- Files end with a single newline
- No trailing whitespace

## Git Workflow

- Rebase-only workflow (no merge commits on feature branches)
- See GIT_WORKFLOW.md for comprehensive guide
- See CONTRIBUTING.md for contribution process
