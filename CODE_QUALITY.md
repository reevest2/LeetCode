# Code Quality Standards

This document defines the quality bar for all code in this repository. These are not guidelines -- they are requirements. Code that does not meet these standards will not be merged.

## Table of Contents

- [Universal Standards](#universal-standards)
- [Correctness](#correctness)
- [Complexity Requirements](#complexity-requirements)
- [Readability](#readability)
- [Naming](#naming)
- [Comments](#comments)
- [Prohibited Practices](#prohibited-practices)
- [Language-Specific Standards](#language-specific-standards)
- [Assembly Standards](#assembly-standards)
- [Edge Case Handling](#edge-case-handling)
- [Submission Verification](#submission-verification)

## Universal Standards

These apply to every solution in every language without exception.

### The Three Questions

Before submitting any code, you must be able to answer YES to all three:

1. **Does it work?** Accepted on LeetCode with all test cases passing.
2. **Is it clear?** A competent programmer unfamiliar with the problem can read your solution and understand the algorithm without external references.
3. **Is it honest?** You understand every line. You can explain why each decision was made. You did not copy-paste without comprehension.

## Correctness

### Requirements

- The solution MUST be accepted on LeetCode. "Works on my machine" is not sufficient.
- The solution MUST handle all edge cases defined by the problem constraints.
- The solution MUST NOT rely on undefined behavior in any language.
- The solution MUST NOT rely on LeetCode-specific environmental assumptions (e.g., global state between test cases) unless the problem explicitly requires it.

### What "Correct" Means

```
Correct = passes all test cases
        + handles edge cases explicitly
        + no undefined behavior
        + no memory leaks (C/C++)
        + no integer overflow (unless handled intentionally)
```

## Complexity Requirements

Every solution must meet the optimal time and space complexity described in the problem's study guide unless there is a documented reason for deviation.

### Acceptable Deviations

- Using O(n) space instead of O(1) space when the O(1) version sacrifices significant readability
- Using O(n log n) instead of O(n) when the linear solution requires obscure techniques not suitable for learning

All deviations must be documented in a comment at the top of the solution explaining the tradeoff.

### Unacceptable

- Brute force solutions submitted as the primary solution when an optimal approach exists
- Solutions that exceed the problem's time or memory limits
- Solutions with unnecessary extra passes over the data

## Readability

Code is read far more often than it is written. In an educational repository, readability is paramount.

### Structure

- **One logical operation per line.** Do not chain multiple operations to save lines.
- **Consistent indentation.** Use the language's standard (see Style Guide).
- **Blank lines separate logical blocks.** Group related statements. Separate setup, core logic, and return.
- **Short functions.** If a helper function clarifies the algorithm, use one. If it obscures it, do not.

### Bad Example (Python)

```python
def twoSum(self, nums, target):
    d = {}
    for i, v in enumerate(nums):
        if target - v in d: return [d[target - v], i]
        d[v] = i
```

### Good Example (Python)

```python
def twoSum(self, nums: list[int], target: int) -> list[int]:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i
```

### Why the Second is Better

- `seen` tells you what the dict represents; `d` tells you nothing
- `num` is clearer than `v`
- `complement` names the concept; `target - v` forces the reader to derive it
- Blank lines separate the check from the store
- Type hints document the contract
- The `if` and `return` are on separate lines -- debuggable, readable

## Naming

### Rules

| Element | Convention | Example |
|---------|-----------|---------|
| Variables | Descriptive, lowercase | `left_bound`, `max_profit`, `seen` |
| Loop counters | Single letter OK | `i`, `j`, `k` |
| Size/length | `n`, `m` OK when obvious | `n = len(nums)` |
| Pointers | `left`, `right`, `slow`, `fast` | Not `l`, `r`, `s`, `f` |
| Hash maps | Name describes content | `char_count`, `index_map` | Not `d`, `mp`, `m` |
| Booleans | Reads as a question | `is_valid`, `has_cycle` | Not `flag`, `check` |
| Results | Name describes what it holds | `max_length`, `result` | Not `ans`, `res`, `ret` |

### Forbidden Names

These names are banned in all solutions:

- `tmp`, `temp` -- name what it actually holds
- `data`, `info`, `stuff` -- meaningless
- `flag`, `check` -- name the condition
- `val` (when `num`, `char`, `node` etc. are more specific)
- `arr` (when `nums`, `heights`, `prices` etc. are more specific)
- `d`, `m`, `mp` for hash maps
- `l` (ambiguous with `1` in many fonts)

### Assembly Exception

Assembly languages have register-based naming. Use comments to document what each register holds at the top of each logical section.

## Comments

### When to Comment

- **Algorithm choice**: Why this approach over alternatives (one line, top of solution)
- **Non-obvious logic**: Anything a reader might pause on
- **Edge case handling**: Why a specific check exists
- **Assembly**: What each register holds, what each block does

### When NOT to Comment

- Do not restate what the code does: `// increment i` above `i++`
- Do not leave TODO comments in submitted solutions
- Do not leave commented-out alternative approaches
- Do not write journal-style comments: `// I tried X but it didn't work`

### Comment Style

```python
# Good: explains WHY
# Track the maximum ending here to handle the case where all numbers are negative
max_ending_here = max(num, max_ending_here + num)

# Bad: restates WHAT
# Update max_ending_here
max_ending_here = max(num, max_ending_here + num)
```

## Prohibited Practices

The following will result in immediate rejection during review:

### Code Smells

- [ ] **Magic numbers** -- all numeric constants must be named or obvious from context
- [ ] **God functions** -- solutions should not exceed ~50 lines of logic (language-dependent)
- [ ] **Dead code** -- no commented-out blocks, no unreachable code
- [ ] **Debug output** -- no print, cout, Console.WriteLine, printf left in the solution
- [ ] **Unused imports/includes** -- import only what you use
- [ ] **Premature optimization** -- do not micro-optimize at the cost of readability
- [ ] **Copy-paste code** -- if you repeat yourself, extract a helper

### Architectural Smells

- [ ] **Global state** -- no module-level mutable variables
- [ ] **Side effects in the Solution class** -- solutions must be stateless between calls
- [ ] **Platform-dependent code** -- must work on any system LeetCode supports

## Language-Specific Standards

### Python

- Use type hints on all function signatures
- Use `list[int]` not `List[int]` (modern syntax)
- Use `collections` and `itertools` only when they genuinely simplify
- Do not use walrus operator (`:=`) unless it significantly improves readability
- Prefer `for` loops over comprehensions when the logic has multiple steps
- No bare `except` clauses

### C#

- Use `PascalCase` for methods, `camelCase` for locals
- Use `var` only when the type is obvious from the right side
- Prefer `Array` and `Dictionary` over LINQ for algorithmic code -- the algorithm should be visible
- No `dynamic` typing
- No `unsafe` blocks unless the problem specifically requires pointer manipulation

### C

- All variables declared at the top of their scope
- No VLAs (variable-length arrays) -- use `malloc`/`calloc`
- Free all allocated memory -- no leaks
- Use `int` for return codes, not magic numbers
- Use `const` for parameters that are not modified
- Check all pointer dereferences for NULL where applicable

### C++

- Use `const` and `const&` for parameters that are not modified
- Prefer `unordered_map` over `map` unless ordering is required
- No `using namespace std;` in headers (acceptable in solution files since they are self-contained)
- Use range-based for loops when iterating over containers
- No raw `new`/`delete` -- use stack allocation or smart pointers
- No `goto`

## Assembly Standards

Assembly solutions have unique requirements due to the nature of the languages.

### All Assembly Languages

- **Register documentation**: Comment block at the top of each function listing which registers hold which values
- **Section labels**: Use descriptive labels, not `.L1`, `.L2`
- **Stack frame documentation**: Document the stack layout when using the stack
- **Calling convention compliance**: Follow the platform's standard calling convention exactly
- **No self-modifying code**

### x86-64 (NASM/GAS)

- Follow System V AMD64 ABI for function calls
- Document register clobber lists
- Use meaningful label names: `find_complement:` not `.loop1:`

### ARM64

- Follow AAPCS64 calling convention
- Document register usage at function entry
- Use conditional execution where it improves clarity

### RISC-V

- Follow standard RISC-V calling convention
- Document which registers are callee-saved vs caller-saved
- Use pseudo-instructions where they improve readability (e.g., `li`, `mv`, `j`)

## Edge Case Handling

Every solution must explicitly handle edge cases relevant to the problem. Common edge cases by category:

### Arrays

- Empty array
- Single element
- All identical elements
- Already sorted / reverse sorted
- Contains negatives, zeros, or INT_MAX/INT_MIN

### Strings

- Empty string
- Single character
- All identical characters
- Unicode considerations (if applicable)

### Linked Lists

- NULL/empty list
- Single node
- Cycle detection (if applicable)

### Trees

- NULL/empty tree
- Single node
- Skewed tree (all left or all right children)

### Numbers

- Zero
- Negative numbers
- Integer overflow / underflow
- Powers of 2, boundary values

## Submission Verification

Before submitting a PR, run through this verification checklist:

### Mandatory

1. [ ] Submitted to LeetCode and accepted
2. [ ] Runtime is within the expected complexity class
3. [ ] Memory usage is within the expected complexity class
4. [ ] All variable names follow naming standards
5. [ ] No prohibited practices present
6. [ ] File header preserved (problem link, pattern, hints)
7. [ ] No extraneous files in the PR

### Recommended

1. [ ] Tested with edge cases locally before LeetCode submission
2. [ ] Reviewed the diff yourself as if you were the reviewer
3. [ ] Read your solution after a break -- is it still clear?
4. [ ] Compared your approach with the study guide -- does it match?

---

**Remember:** This is an educational repository. Every solution teaches someone. Write code you would be proud to present in a technical interview or a classroom.
