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

## Key Documents

| Document | Owns |
|----------|------|
| [CODE_QUALITY.md](CODE_QUALITY.md) | Correctness, complexity, readability, naming philosophy, forbidden names, prohibited practices, edge cases, language-specific quality rules |
| [STYLE_GUIDE.md](STYLE_GUIDE.md) | Formatting, indentation, line length, naming conventions (snake_case vs camelCase), braces, file headers, annotated examples per language |
| [CONTRIBUTING.md](CONTRIBUTING.md) | What we accept/reject, PR process, review process, solution requirements, study guide requirements |
| [GIT_WORKFLOW.md](GIT_WORKFLOW.md) | Branch naming, commit format, rebase workflow, conflict resolution, signing, advanced git |

When in doubt about a rule, check the document that owns it. Do not duplicate rules across documents.

## Quick Reference

### When Implementing a Solution

1. Read the study guide (`README.md`) first
2. Understand the optimal approach before coding
3. Preserve the file header comments
4. Follow the optimal approach from the study guide
5. Use meaningful variable names per [CODE_QUALITY.md](CODE_QUALITY.md#naming)
6. Handle all edge cases listed in the study guide
7. Verify it compiles without warnings
8. Remove all debug output and TODOs

### Critical Rules (see source docs for full details)

- **No debug output, commented-out code, or TODOs** in submitted solutions
- **Preserve file headers** (problem link, pattern, hints)
- **One problem per PR**
- **Rebase-only workflow** (no merge commits on feature branches)
- **Commit format**: `<type>(<scope>): <description>` -- see [GIT_WORKFLOW.md](GIT_WORKFLOW.md#4-writing-good-commits)
- **Branch format**: `<type>/<problem-number>-<description>` -- see [GIT_WORKFLOW.md](GIT_WORKFLOW.md#3-the-feature-branch-workflow)

### Style Essentials

- Line endings: LF everywhere
- Indentation: 4 spaces (2 for YAML/JSON)
- Line length: Python 100, C# 120, C/C++ 100, Assembly 100
- Braces: K&R style (same-line opening) for C, C++, and C#
- Files end with a single newline, no trailing whitespace
