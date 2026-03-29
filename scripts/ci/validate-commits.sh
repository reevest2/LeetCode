#!/usr/bin/env bash
# Validates that commit messages follow the project's format:
#   <type>(<scope>): <description>
#
# Valid types: solve, fix, docs, style, refactor, test, chore
# Description: imperative mood, no capital, no period, max 72 chars

set -euo pipefail

BASE_REF="${1:-origin/master}"
ERRORS=0

# Regex for valid commit message format
# Type must be one of the allowed values
# Scope is optional (for chore/docs that may not have a problem number)
# Description starts lowercase, no period at end
PATTERN='^(solve|fix|docs|style|refactor|test|chore)(\([^)]+\))?: [a-z].*[^.]$'

# Also allow merge commits
MERGE_PATTERN='^Merge '

# Get commits in this PR/push
COMMITS=$(git log --format='%H' "$BASE_REF"..HEAD 2>/dev/null || true)

if [ -z "$COMMITS" ]; then
    echo "No new commits to validate."
    exit 0
fi

echo "Validating commit messages..."
echo ""

while IFS= read -r hash; do
    subject=$(git log -1 --format='%s' "$hash")
    length=${#subject}

    # Skip merge commits
    if echo "$subject" | grep -qE "$MERGE_PATTERN"; then
        echo "  SKIP (merge): $subject"
        continue
    fi

    # Check format
    if ! echo "$subject" | grep -qE "$PATTERN"; then
        echo "  FAIL: $subject"
        echo "        Expected format: <type>(<scope>): <lowercase description>"
        echo "        Valid types: solve, fix, docs, style, refactor, test, chore"
        ERRORS=$((ERRORS + 1))
        continue
    fi

    # Check length
    if [ "$length" -gt 72 ]; then
        echo "  FAIL: $subject"
        echo "        Subject line is $length characters (max 72)"
        ERRORS=$((ERRORS + 1))
        continue
    fi

    echo "  OK: $subject"
done <<< "$COMMITS"

echo ""

if [ $ERRORS -gt 0 ]; then
    echo "Commit message validation failed with $ERRORS error(s)."
    echo ""
    echo "Format: <type>(<scope>): <description>"
    echo "  - type: solve, fix, docs, style, refactor, test, chore"
    echo "  - description: imperative mood, lowercase start, no period, max 72 chars"
    echo "  - example: solve(0001): implement two sum in python"
    exit 1
fi

echo "All commit messages are valid."
