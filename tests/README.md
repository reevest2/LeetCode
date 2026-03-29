# Tests

This directory contains tests that validate solutions against known inputs and outputs.

Tests are a **secondary** validation. The primary validation is a successful LeetCode submission. Tests here serve to:

1. Catch regressions if a solution is refactored
2. Verify edge cases documented in the study guide
3. Provide a local feedback loop faster than submitting to LeetCode

## Running Tests

### Python

```bash
# Run all Python tests
pytest tests/python/ -v

# Run tests for a specific problem
pytest tests/python/test_0001_two_sum.py -v
```

Requires: `pip install pytest`

### C

```bash
cd tests/c
make test_0001_two_sum
./test_0001_two_sum
```

Requires: `gcc`

### C++

```bash
cd tests/cpp
make test_0001_two_sum
./test_0001_two_sum
```

Requires: `g++`

## Adding Tests

### Naming Convention

```
tests/<language>/test_NNNN_problem_name.<ext>
```

Examples:
- `tests/python/test_0001_two_sum.py`
- `tests/c/test_0001_two_sum.c`
- `tests/cpp/test_0001_two_sum.cpp`

### What to Test

1. **Basic examples** from the LeetCode problem description
2. **Edge cases** from the study guide's "Common Pitfalls" section:
   - Empty input
   - Single element
   - All identical elements
   - Negative numbers
   - Boundary values (INT_MAX, INT_MIN)
3. **The specific case that made you realize your first approach was wrong** (if applicable)

### What NOT to Test

- Performance (LeetCode handles this)
- Random/fuzz testing (keep tests deterministic)
- Implementation details (test behavior, not internal state)

### Test Structure (Python Example)

```python
import sys
import os

# Add the solution's directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../problems/NNNN-problem-name/python'))

from solution import Solution


class TestProblemName:
    def setup_method(self):
        self.solution = Solution()

    def test_basic_example(self):
        assert self.solution.methodName([2, 7, 11, 15], 9) == [0, 1]

    def test_edge_case_description(self):
        assert self.solution.methodName([], 0) == []
```

## Assembly and C# Tests

Assembly tests are not included due to cross-compilation complexity. C# tests via xUnit/NUnit are planned but not yet scaffolded. Contributions welcome -- open an issue to discuss the approach first.
