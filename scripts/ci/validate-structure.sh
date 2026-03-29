#!/usr/bin/env bash
# Validates that changed problem directories follow the expected structure.
# Each problem directory must contain:
#   - README.md
#   - python/solution.py
#   - csharp/Solution.cs
#   - c/solution.c
#   - cpp/solution.cpp
#   - x86_64/solution.asm
#   - arm64/solution.s
#   - riscv/solution.s

set -euo pipefail

BASE_REF="${1:-origin/master}"
ERRORS=0

# Get changed problem directories
CHANGED_DIRS=$(git diff --name-only "$BASE_REF"...HEAD \
    | grep '^problems/' \
    | cut -d'/' -f1-2 \
    | sort -u)

if [ -z "$CHANGED_DIRS" ]; then
    echo "No problem directories changed."
    exit 0
fi

REQUIRED_FILES=(
    "README.md"
    "python/solution.py"
    "csharp/Solution.cs"
    "c/solution.c"
    "cpp/solution.cpp"
    "x86_64/solution.asm"
    "arm64/solution.s"
    "riscv/solution.s"
)

for dir in $CHANGED_DIRS; do
    if [ ! -d "$dir" ]; then
        continue
    fi

    echo "Checking $dir..."

    # Validate directory name format: NNNN-problem-name
    dirname=$(basename "$dir")
    if ! echo "$dirname" | grep -qE '^[0-9]{4}-[a-z0-9-]+$'; then
        echo "  ERROR: Directory name '$dirname' does not match format NNNN-problem-name"
        ERRORS=$((ERRORS + 1))
    fi

    # Check all required files exist
    for file in "${REQUIRED_FILES[@]}"; do
        if [ ! -f "$dir/$file" ]; then
            echo "  ERROR: Missing required file: $dir/$file"
            ERRORS=$((ERRORS + 1))
        fi
    done
done

if [ $ERRORS -gt 0 ]; then
    echo ""
    echo "Structure validation failed with $ERRORS error(s)."
    exit 1
fi

echo "Structure validation passed."
