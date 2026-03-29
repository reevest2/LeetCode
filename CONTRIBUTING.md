# Contributing

Thank you for your interest in contributing. This project holds contributions to a high standard -- every solution is a teaching tool, and every piece of code should be something a learner can study with confidence.

Read this entire document before submitting your first contribution.

## Table of Contents

- [Before You Start](#before-you-start)
- [What We Accept](#what-we-accept)
- [What We Do NOT Accept](#what-we-do-not-accept)
- [Contribution Workflow](#contribution-workflow)
- [Commit Standards](#commit-standards)
- [Pull Request Process](#pull-request-process)
- [Review Process](#review-process)
- [Solution Requirements](#solution-requirements)
- [Study Guide Requirements](#study-guide-requirements)
- [Getting Help](#getting-help)

## Before You Start

1. **Read the [Code of Conduct](CODE_OF_CONDUCT.md).** We enforce it.
2. **Read the [Code Quality Standards](CODE_QUALITY.md).** Every solution must meet them.
3. **Read the [Style Guide](STYLE_GUIDE.md).** Consistency is non-negotiable.
4. **Check existing issues and PRs** to avoid duplicate work.
5. **Open an issue first** for new problems or significant changes. Do not start work without alignment.

## What We Accept

- **Implemented solutions** replacing `TODO: implement` stubs in any of the 7 supported languages
- **Bug fixes** to existing solutions (with proof: describe the failing case)
- **Study guide improvements** that add clarity without adding fluff
- **New problem additions** that follow the existing structure exactly
- **Test cases** that validate solutions
- **Documentation fixes** (typos, broken links, factual errors)

## What We Do NOT Accept

- Solutions that do not compile or pass all LeetCode test cases
- "Alternative" solutions without clear justification of why they belong alongside the primary one
- Solutions that prioritize cleverness over readability
- Code golf or obfuscated solutions
- Solutions copied from other repositories or websites without attribution and original understanding
- Changes to project structure without prior discussion and approval
- Unrelated files, IDE configs, or build artifacts
- AI-generated solutions submitted without review, testing, and genuine understanding

## Contribution Workflow

### 1. Fork and Clone

```bash
git clone https://github.com/<your-username>/LeetCode.git
cd LeetCode
```

### 2. Create a Branch

Branch names must follow this format:

```
<type>/<problem-number>-<short-description>

# Examples:
solve/0001-two-sum-python
fix/0042-trapping-rain-water-cpp
docs/0015-3sum-study-guide
```

Valid types: `solve`, `fix`, `docs`, `feat`, `chore`

### 3. Make Your Changes

- One problem per pull request. No exceptions.
- Follow all standards in [CODE_QUALITY.md](CODE_QUALITY.md) and [STYLE_GUIDE.md](STYLE_GUIDE.md).
- Test your solution against LeetCode before submitting.

### 4. Submit a Pull Request

- Fill out the PR template completely. Incomplete PRs will be closed.
- Link the relevant issue if one exists.
- Mark your PR as draft if it is not ready for review.

## Commit Standards

### Message Format

```
<type>(<scope>): <description>

[optional body]
[optional footer]
```

### Types

| Type | Usage |
|------|-------|
| `solve` | Implementing a solution |
| `fix` | Fixing a bug in an existing solution |
| `docs` | Documentation changes only |
| `style` | Formatting, whitespace (no logic changes) |
| `refactor` | Restructuring without changing behavior |
| `test` | Adding or modifying tests |
| `chore` | Build scripts, CI, tooling |

### Rules

- Use the imperative mood: "add solution" not "added solution" or "adds solution"
- Do not capitalize the first letter of the description
- No period at the end
- Limit the subject line to 72 characters
- Separate subject from body with a blank line
- Reference issue numbers in the footer: `Closes #42`

### Examples

```
solve(0001): implement two sum in python

One-pass hash map approach. O(n) time, O(n) space.

Closes #10
```

```
fix(0042): correct off-by-one in trapping rain water c++ solution

The right pointer was initialized to nums.size() instead of
nums.size() - 1, causing out-of-bounds access on empty input.
```

## Pull Request Process

1. **One problem, one PR.** Multi-problem PRs will be rejected without review.
2. **Complete the PR template.** Every field. No exceptions.
3. **Ensure your solution compiles and passes all LeetCode test cases.** State the runtime and memory percentile in your PR.
4. **Self-review your diff before requesting review.** If you would not approve it, do not submit it.
5. **Respond to review feedback within 7 days** or your PR will be closed.
6. **Do not force-push after review has started** unless asked by a reviewer.
7. **Squash trivial fixup commits** before requesting re-review.

### PR Checklist

Before submitting, verify:

- [ ] Solution compiles without warnings in the target language
- [ ] Solution passes all LeetCode test cases
- [ ] Code follows [CODE_QUALITY.md](CODE_QUALITY.md) standards
- [ ] Code follows [STYLE_GUIDE.md](STYLE_GUIDE.md) conventions
- [ ] Existing header comments (problem link, pattern, hints) are preserved
- [ ] No debug output, commented-out code, or TODOs left behind
- [ ] Commit messages follow the format specified above
- [ ] PR description is complete and accurate

## Review Process

Every PR requires at least one maintainer approval. Reviewers will evaluate:

1. **Correctness** -- Does it solve the problem? Does it handle edge cases?
2. **Complexity** -- Does it meet or beat the expected time/space complexity?
3. **Readability** -- Can a learner understand this without external context?
4. **Standards compliance** -- Does it follow CODE_QUALITY.md and STYLE_GUIDE.md?
5. **Consistency** -- Does it match the patterns used in existing solutions?

### Review Outcomes

- **Approved** -- Merges after CI passes.
- **Changes requested** -- Address every comment. Do not resolve conversations yourself; let the reviewer resolve them.
- **Rejected** -- Fundamentally misaligned with project standards. The rejection comment will explain why.

Reviewers are volunteers. Be patient, be respectful, and make their job easy by submitting clean work.

## Solution Requirements

### Every solution MUST:

1. **Solve the problem correctly** on LeetCode (accepted submission required)
2. **Use the optimal or near-optimal approach** described in the study guide
3. **Preserve the existing file header** (problem link, pattern, hints)
4. **Use meaningful variable names** -- no single letters except loop counters (`i`, `j`, `k`) and well-known conventions (`n` for size, `m` for rows/cols)
5. **Include no debug output** -- no print statements, console.log, or cout left in the code
6. **Include no commented-out code** -- dead code is deleted, not commented
7. **Handle edge cases** -- empty input, single element, negative numbers, overflow, etc.

### Every solution MUST NOT:

1. Use language features that obscure the algorithm (no regex for string problems unless the problem is about regex)
2. Rely on platform-specific behavior
3. Import unnecessary libraries
4. Exceed the memory/time constraints of the problem

## Study Guide Requirements

Study guides follow a strict structure. Do not deviate from it:

1. **Problem Statement** -- One-sentence summary. Not a copy of the LeetCode description.
2. **Key Insight** -- The single conceptual breakthrough needed to solve optimally.
3. **Pattern** -- Which algorithmic pattern applies and why.
4. **When to Use / When NOT to Use** -- Concrete guidance, not vague generalities.
5. **Approach** -- Brute force first, then optimal. Include complexity for both.
6. **Common Pitfalls** -- Real mistakes people make, not hypothetical ones.
7. **Related Problems** -- Cross-references to problems that use the same pattern.

## Getting Help

- **Stuck on a problem?** Open a discussion, not an issue.
- **Unclear about standards?** Read the docs first, then ask.
- **Found a bug?** Open an issue with a minimal reproduction case.
- **Want to add a new language?** Open an issue to discuss feasibility and maintenance burden first.

We want contributors to succeed. Ask questions early rather than submitting work that does not meet standards.
