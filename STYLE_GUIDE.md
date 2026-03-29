# Style Guide

This document defines the formatting and structural conventions for every language in this repository. Consistency across solutions is mandatory -- a reader should never have to re-calibrate their expectations when moving between solutions.

## Table of Contents

- [Universal Conventions](#universal-conventions)
- [File Structure](#file-structure)
- [Python](#python)
- [C#](#c-sharp)
- [C](#c)
- [C++](#cpp)
- [x86-64 Assembly](#x86-64-assembly)
- [ARM64 Assembly](#arm64-assembly)
- [RISC-V Assembly](#risc-v-assembly)

## Universal Conventions

### File Headers

Every solution file begins with a standard header. Do not remove, reorder, or modify the structure:

```
<comment> <problem-number>. <problem-name>
<comment> <leetcode-url>
<comment> Pattern: <pattern-name>
<comment>
<comment> Hints:
<comment>   1. <hint>
<comment>   2. <hint>
<comment>   3. <hint>
<comment>
<comment> Brute Force: <description>
<comment> Optimal: <description>
```

### Whitespace

- No trailing whitespace on any line
- Files end with a single newline
- No more than two consecutive blank lines
- One blank line between logical sections within a function
- Two blank lines between top-level definitions (functions, classes)

### Line Length

| Language | Max Line Length |
|----------|----------------|
| Python | 100 characters |
| C# | 120 characters |
| C | 100 characters |
| C++ | 100 characters |
| Assembly | 100 characters (excluding comments) |

### Braces and Blocks

Languages with braces (C, C++, C#) use **same-line opening braces** (K&R / "One True Brace Style"):

```c
if (condition) {
    // body
} else {
    // body
}
```

Not:

```c
if (condition)
{
    // body
}
```

## File Structure

### Solution File Layout

1. Header block (problem info, hints, approach summary)
2. Imports / includes
3. Solution class or function
4. No main function, no test code, no driver code

### What Does NOT Go in Solution Files

- Test cases or example usage
- Main functions
- Multiple solution approaches in the same file (use the optimal one)
- Benchmarking code

## Python

### Formatting

- **Indentation:** 4 spaces (no tabs)
- **Quotes:** Single quotes for strings unless the string contains a single quote
- **Type hints:** Required on all function parameters and return types
- **Docstrings:** Not required in solution files (the header serves this purpose)

### Conventions

```python
# Imports at the top, grouped: stdlib first, then collections/typing
from collections import defaultdict, deque

class Solution:
    def methodName(self, nums: list[int], target: int) -> list[int]:
        # Use modern type hints: list[int], dict[str, int], etc.
        # NOT List[int], Dict[str, int]

        n = len(nums)
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

        return []
```

### Naming

| Element | Style | Example |
|---------|-------|---------|
| Variables | snake_case | `max_length`, `left_bound` |
| Functions/methods | camelCase (LeetCode convention) | `twoSum`, `maxProfit` |
| Constants | UPPER_SNAKE | `MOD = 10**9 + 7` |
| Classes | PascalCase | `Solution`, `ListNode` |

Note: Method names follow LeetCode's camelCase convention to match the expected interface.

## C Sharp

### Formatting

- **Indentation:** 4 spaces
- **Braces:** Same-line opening (not Allman style, despite C# convention -- we prioritize consistency across the repo)
- **Namespace:** Not used in solution files

### Conventions

```csharp
using System;
using System.Collections.Generic;

public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var seen = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++) {
            int complement = target - nums[i];

            if (seen.ContainsKey(complement)) {
                return new int[] { seen[complement], i };
            }

            seen[nums[i]] = i;
        }

        return Array.Empty<int>();
    }
}
```

### Naming

| Element | Style | Example |
|---------|-------|---------|
| Variables | camelCase | `maxLength`, `leftBound` |
| Methods | PascalCase | `TwoSum`, `MaxProfit` |
| Properties | PascalCase | `Val`, `Next` |
| Constants | PascalCase | `MaxValue` |

## C

### Formatting

- **Indentation:** 4 spaces
- **Braces:** Same-line opening (K&R style)
- **Pointer declaration:** `int *ptr` not `int* ptr`

### Conventions

```c
#include <stdlib.h>
#include <string.h>

int *twoSum(int *nums, int numsSize, int target, int *returnSize) {
    // Allocate result
    int *result = (int *)malloc(2 * sizeof(int));
    *returnSize = 2;

    // Hash map implementation or nested loop
    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                result[0] = i;
                result[1] = j;
                return result;
            }
        }
    }

    *returnSize = 0;
    free(result);
    return NULL;
}
```

### Naming

| Element | Style | Example |
|---------|-------|---------|
| Variables | snake_case | `max_length`, `left_bound` |
| Functions | camelCase (LeetCode) | `twoSum`, `maxProfit` |
| Macros | UPPER_SNAKE | `MAX_SIZE`, `MOD` |
| Struct members | snake_case | `tree_node.left` |

## CPP

### Formatting

- **Indentation:** 4 spaces
- **Braces:** Same-line opening
- **Includes:** Standard library first, then problem-specific

### Conventions

```cpp
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            if (seen.count(complement)) {
                return {seen[complement], i};
            }

            seen[nums[i]] = i;
        }

        return {};
    }
};
```

### Naming

| Element | Style | Example |
|---------|-------|---------|
| Variables | snake_case | `max_length`, `left_bound` |
| Methods | camelCase (LeetCode) | `twoSum`, `maxProfit` |
| Classes | PascalCase | `Solution`, `ListNode` |
| Constants | kPascalCase or UPPER_SNAKE | `kMaxSize`, `MOD` |

## x86-64 Assembly

### Formatting

- **Indentation:** 4 spaces for instructions, no indent for labels
- **Comments:** `;` for inline comments, aligned when possible
- **Sections:** Clearly labeled with `.section` or `.text` / `.data`

### Conventions

```asm
; 1. Two Sum
; https://leetcode.com/problems/two-sum/
; Pattern: Hash Table
;
; Register usage:
;   rdi - nums array pointer
;   rsi - nums size
;   rdx - target value
;   rcx - loop counter i
;   r8  - loop counter j

section .text
global twoSum

twoSum:
    push    rbp
    mov     rbp, rsp

    ; Setup
    xor     rcx, rcx                ; i = 0

outer_loop:
    cmp     rcx, rsi
    jge     not_found

    lea     r8, [rcx + 1]           ; j = i + 1

inner_loop:
    cmp     r8, rsi
    jge     next_outer

    ; Check if nums[i] + nums[j] == target
    mov     eax, [rdi + rcx * 4]    ; nums[i]
    add     eax, [rdi + r8 * 4]     ; nums[i] + nums[j]
    cmp     eax, edx
    je      found

    inc     r8
    jmp     inner_loop

next_outer:
    inc     rcx
    jmp     outer_loop

found:
    ; Return result
    mov     eax, ecx                ; result[0] = i
    mov     edx, r8d                ; result[1] = j
    pop     rbp
    ret

not_found:
    mov     eax, -1
    pop     rbp
    ret
```

### Label Naming

- Use descriptive names: `outer_loop`, `found`, `not_found`
- Prefix helper labels with function name for clarity: `twoSum_inner_loop`
- No numeric-only labels: `.L1` is not acceptable

## ARM64 Assembly

### Formatting

- **Indentation:** 4 spaces for instructions
- **Comments:** `//` for inline comments
- **Register documentation:** Required at function entry

### Conventions

```asm
// 1. Two Sum
// https://leetcode.com/problems/two-sum/
// Pattern: Hash Table
//
// Register usage:
//   x0 - nums array pointer
//   x1 - nums size
//   x2 - target value
//   x3 - loop counter i
//   x4 - loop counter j
//   w5 - nums[i]
//   w6 - nums[j]

    .text
    .global twoSum

twoSum:
    stp     x29, x30, [sp, #-16]!
    mov     x29, sp

    mov     x3, #0                  // i = 0

outer_loop:
    cmp     x3, x1
    b.ge    not_found

    add     x4, x3, #1              // j = i + 1

inner_loop:
    cmp     x4, x1
    b.ge    next_outer

    ldr     w5, [x0, x3, lsl #2]    // nums[i]
    ldr     w6, [x0, x4, lsl #2]    // nums[j]
    add     w5, w5, w6              // nums[i] + nums[j]
    cmp     w5, w2
    b.eq    found

    add     x4, x4, #1
    b       inner_loop

next_outer:
    add     x3, x3, #1
    b       outer_loop

found:
    mov     x0, x3                  // result[0] = i
    mov     x1, x4                  // result[1] = j
    ldp     x29, x30, [sp], #16
    ret

not_found:
    mov     x0, #-1
    ldp     x29, x30, [sp], #16
    ret
```

## RISC-V Assembly

### Formatting

- **Indentation:** 4 spaces for instructions
- **Comments:** `#` for inline comments
- **Pseudo-instructions:** Use when they improve readability

### Conventions

```asm
# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Pattern: Hash Table
#
# Register usage:
#   a0 - nums array pointer
#   a1 - nums size
#   a2 - target value
#   t0 - loop counter i
#   t1 - loop counter j
#   t2 - nums[i]
#   t3 - nums[j]

    .text
    .global twoSum

twoSum:
    addi    sp, sp, -16
    sd      ra, 8(sp)
    sd      s0, 0(sp)

    li      t0, 0                   # i = 0

outer_loop:
    bge     t0, a1, not_found

    addi    t1, t0, 1               # j = i + 1

inner_loop:
    bge     t1, a1, next_outer

    slli    t4, t0, 2               # offset for nums[i]
    add     t4, a0, t4
    lw      t2, 0(t4)               # nums[i]

    slli    t5, t1, 2               # offset for nums[j]
    add     t5, a0, t5
    lw      t3, 0(t5)               # nums[j]

    add     t2, t2, t3              # nums[i] + nums[j]
    beq     t2, a2, found

    addi    t1, t1, 1
    j       inner_loop

next_outer:
    addi    t0, t0, 1
    j       outer_loop

found:
    mv      a0, t0                  # result[0] = i
    mv      a1, t1                  # result[1] = j
    ld      ra, 8(sp)
    ld      s0, 0(sp)
    addi    sp, sp, 16
    ret

not_found:
    li      a0, -1
    ld      ra, 8(sp)
    ld      s0, 0(sp)
    addi    sp, sp, 16
    ret
```

---

**Consistency is the priority.** When in doubt, look at existing solutions for precedent. If no precedent exists, open an issue to discuss before establishing a new pattern.
