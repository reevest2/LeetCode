# Git Workflow

This document teaches the git practices used in this repository. These practices are drawn from how major open source projects (Linux kernel, Rust, Git itself) manage contributions, adapted for this project's scope.

Read this guide once, refer back to specific sections as needed.

## Table of Contents

1. [Philosophy](#1-philosophy)
2. [Setup](#2-setup)
3. [The Feature Branch Workflow](#3-the-feature-branch-workflow)
4. [Writing Good Commits](#4-writing-good-commits)
5. [Rebase vs Merge](#5-rebase-vs-merge)
6. [Handling Conflicts](#6-handling-conflicts)
7. [Cherry-Picking](#7-cherry-picking)
8. [Advanced Topics](#8-advanced-topics)
9. [Branch Protection Rules](#9-branch-protection-rules)

---

## 1. Philosophy

### The Log IS the Documentation

`git log` tells the story of the project. A clean log lets anyone understand what changed, why, and when -- without reading the code. A messy log is useless.

Every commit should be:

- **Atomic**: One logical change. Not "implement solution and fix typo and update docs."
- **Compilable**: The project should build and work at every commit. This enables `git bisect`.
- **Explained**: The commit message tells you WHY the change was made, not just WHAT changed.

### Bisectability

If a bug is introduced, `git bisect` performs a binary search through history to find the exact commit that caused it. This only works if every commit in the history represents a working state. Breaking this property wastes everyone's time.

### The Golden Rule

**Never rewrite history that has been shared.** Once you push commits to a shared branch, those commits are public. Rewriting them (force-pushing) causes problems for everyone who has pulled that branch. Rewrite only your own local, unpushed work.

---

## 2. Setup

### Git Identity

Configure your name and email. These appear in every commit you make.

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### Commit Signing with SSH Keys

Signed commits prove that you authored them. SSH signing is the simplest approach.

```bash
# Generate an SSH key if you do not have one
ssh-keygen -t ed25519 -C "your@email.com"

# Configure git to use SSH signing
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true

# Add the public key to your GitHub account:
# GitHub > Settings > SSH and GPG Keys > New SSH Key > Key type: Signing Key
```

Signed commits show "Verified" on GitHub. This is optional for now but will become required as the project matures.

### Useful Aliases

Add these to your `~/.gitconfig`:

```ini
[alias]
    lg = log --oneline --graph --decorate --all
    st = status -sb
    co = checkout
    br = branch -vv
    last = log -1 --stat
    unstage = reset HEAD --
    amend = commit --amend --no-edit
    wip = stash push -m "WIP"
    unwip = stash pop
```

What they do:

- `git lg` -- Pretty, compact log with branch graph
- `git st` -- Short status with branch info
- `git br` -- Branches with tracking info
- `git last` -- Details of the most recent commit
- `git unstage` -- Remove a file from staging without losing changes
- `git wip` / `git unwip` -- Quick stash and restore

### Enable Rerere

Rerere ("reuse recorded resolution") remembers how you resolved merge conflicts. If the same conflict appears again (e.g., during a second rebase), git resolves it automatically.

```bash
git config --global rerere.enabled true
```

### Pull Strategy

Always rebase on pull. This prevents unnecessary merge commits when syncing with the remote.

```bash
git config --global pull.rebase true
```

### Default Branch

Ensure new repositories use `master` (or whichever name your project uses):

```bash
git config --global init.defaultBranch master
```

---

## 3. The Feature Branch Workflow

This is the process for every contribution. Follow it exactly.

### Step 1: Sync Your Local Master

```bash
git checkout master
git pull origin master
```

If you have local changes on master (you should not), stash them first: `git stash`.

### Step 2: Create a Feature Branch

Branch names follow the format: `<type>/<problem-number>-<description>`

```bash
# Implementing a solution
git checkout -b solve/0001-two-sum-python

# Fixing a bug
git checkout -b fix/0042-trapping-rain-water-cpp

# Documentation change
git checkout -b docs/0015-3sum-study-guide
```

Valid types: `solve`, `fix`, `docs`, `feat`, `chore`

### Step 3: Make Your Changes

Work on your branch. Commit early, commit often during development. You will clean up the history before submitting (see Section 5).

```bash
# Stage specific files (preferred over git add .)
git add problems/0001-two-sum/python/solution.py

# Commit with a proper message
git commit -m "solve(0001): implement two sum in python"
```

### Step 4: Rebase onto Master

Before submitting your PR, rebase your branch onto the latest master. This ensures your changes apply cleanly on top of the current state.

```bash
# Fetch the latest master
git fetch origin master

# Rebase your branch onto it
git rebase origin/master
```

If there are conflicts, see [Section 6](#6-handling-conflicts).

### Step 5: Clean Up Your History

If you made multiple small commits during development, squash them into logical units using interactive rebase (see [Section 5](#5-rebase-vs-merge)).

```bash
# Squash the last 3 commits into one
git rebase -i HEAD~3
```

### Step 6: Push

```bash
# First push
git push -u origin solve/0001-two-sum-python

# After rebasing (force push is OK because this is YOUR branch, not shared)
git push --force-with-lease
```

Always use `--force-with-lease` instead of `--force`. It refuses to overwrite the remote if someone else has pushed to your branch since you last fetched.

### Step 7: Open a Pull Request

Open a PR on GitHub targeting `master`. Fill out the PR template completely.

### Step 8: Clean Up After Merge

After your PR is merged, delete your local and remote branches:

```bash
git checkout master
git pull origin master
git branch -d solve/0001-two-sum-python
git push origin --delete solve/0001-two-sum-python
```

Or let GitHub auto-delete the branch on merge (Settings > General > Automatically delete head branches).

---

## 4. Writing Good Commits

### The Format

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Type**: What kind of change (`solve`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`)
**Scope**: What it affects (usually the problem number)
**Description**: What changed, in imperative mood

### The Rules

1. **Imperative mood**: "add solution" not "added solution" or "adds solution"
2. **No capital** on the first letter of the description
3. **No period** at the end
4. **72 characters max** for the subject line
5. **Blank line** between subject and body
6. **Body explains WHY**, not what (the diff shows what)
7. **Footer** references issues: `Closes #42`

### Good Examples

```
solve(0001): implement two sum in python

One-pass hash map approach. O(n) time, O(n) space.
Complement lookup avoids the O(n^2) brute force.

Closes #10
```

```
fix(0042): correct off-by-one in trapping rain water c++

The right pointer was initialized to nums.size() instead of
nums.size() - 1, causing out-of-bounds access on empty input.
```

```
docs(0015): clarify when to sort vs use hash set in 3sum guide

The original guide did not explain why sorting is preferred over
a hash set approach despite both being O(n^2). Added comparison
of constant factors and cache behavior.
```

### Bad Examples

```
# Too vague
fix: fix bug

# Past tense
solved problem 1

# No type/scope
updated the solution for two sum

# Body restates the diff
solve(0001): implement two sum
Added a hash map. Looped through the array. Checked for complement.
```

### The "Future You" Test

Read your commit message and ask: six months from now, with no other context, will I understand WHY this change was made? If no, rewrite it.

### Atomic Commits

Each commit should contain exactly one logical change:

- **YES**: "implement two sum in python" (one solution, one file)
- **YES**: "fix off-by-one in trapping rain water" (one bug, one fix)
- **NO**: "implement two sum and fix typo in readme" (two unrelated changes)
- **NO**: "work in progress" (not a logical unit)

If you realize mid-commit that you have unrelated changes staged, use `git reset HEAD <file>` to unstage them and commit separately.

---

## 5. Rebase vs Merge

### This Repo Uses Rebase

We maintain a **linear history**. Feature branches are rebased onto master before merging. This means `git log --oneline` reads as a clean, chronological list of changes with no merge diamonds.

### Why Rebase Over Merge

```
# Merge creates diamond patterns:
*   Merge branch 'feature'
|\
| * add feature
| * work in progress
|/
* previous commit

# Rebase creates linear history:
* add feature
* previous commit
```

Linear history is:
- Easier to read and navigate
- Required for `git bisect` to work effectively
- What Linux, Git, and most professional projects enforce

### Interactive Rebase

Interactive rebase is the most powerful tool for cleaning up your work before submitting it. It lets you squash, reword, reorder, and split commits.

```bash
# Rebase the last 4 commits interactively
git rebase -i HEAD~4
```

This opens your editor with a list of commits:

```
pick a1b2c3d solve(0001): start implementing two sum
pick e4f5g6h solve(0001): fix edge case
pick i7j8k9l solve(0001): clean up variable names
pick m0n1o2p solve(0001): add type hints
```

Change the commands to reshape history:

```
pick a1b2c3d solve(0001): start implementing two sum
squash e4f5g6h solve(0001): fix edge case
squash i7j8k9l solve(0001): clean up variable names
squash m0n1o2p solve(0001): add type hints
```

This squashes all four commits into one. Git will prompt you to write a new combined message:

```
solve(0001): implement two sum in python

One-pass hash map approach. O(n) time, O(n) space.
```

### Available Commands in Interactive Rebase

| Command | Short | What It Does |
|---------|-------|-------------|
| `pick` | `p` | Keep the commit as-is |
| `reword` | `r` | Keep the commit but edit the message |
| `squash` | `s` | Combine with previous commit, edit combined message |
| `fixup` | `f` | Combine with previous commit, discard this message |
| `drop` | `d` | Delete the commit entirely |

### When to Squash

- Multiple "WIP" or "fix typo" commits during development -- squash into one
- A commit followed by an immediate fix for that commit -- squash
- Keep separate commits for genuinely distinct logical changes

### The Golden Rule (Repeated for Emphasis)

**Never rebase commits that have been pushed to a shared branch.** Your feature branch is yours -- rebase freely. Master is shared -- never rebase master.

---

## 6. Handling Conflicts

### Why Conflicts Happen

Conflicts occur when two branches modify the same lines of the same file. During a rebase, git replays your commits one at a time on top of the target branch. If a commit conflicts with changes already on the target, git pauses and asks you to resolve it.

### Step-by-Step Resolution

```bash
# 1. Start the rebase
git rebase origin/master

# Git will stop and tell you which files have conflicts:
# CONFLICT (content): Merge conflict in problems/0001-two-sum/python/solution.py
# Fix conflicts and then run "git rebase --continue"

# 2. Open the conflicting file. You will see conflict markers:
```

```python
<<<<<<< HEAD
    seen = {}
=======
    lookup = {}
>>>>>>> your-commit
```

The section between `<<<<<<< HEAD` and `=======` is the version on master.
The section between `=======` and `>>>>>>> your-commit` is your version.

```bash
# 3. Edit the file to resolve the conflict. Remove all conflict markers.
#    Choose one version, combine both, or write something new.

# 4. Stage the resolved file
git add problems/0001-two-sum/python/solution.py

# 5. Continue the rebase
git rebase --continue

# 6. If there are more conflicts in subsequent commits, repeat steps 2-5.
```

### Aborting a Rebase

If the conflicts are too complex or you realize you are on the wrong track:

```bash
git rebase --abort
```

This restores your branch to exactly the state it was in before the rebase started. No data is lost.

### Using Rerere

If you have `rerere.enabled true` (see Setup), git remembers your conflict resolutions. The next time the same conflict appears, git resolves it automatically. This is particularly useful when you rebase frequently.

### Tips

- **Resolve the simplest conflicts first.** Build confidence before tackling complex ones.
- **Use a visual merge tool** if you prefer: `git mergetool` (configure with `git config --global merge.tool <tool>`). VS Code's built-in merge editor is excellent.
- **Do not blindly accept "ours" or "theirs."** Understand both versions before choosing.
- **After resolving, verify the solution still works.** Run your solution through LeetCode again if needed.

---

## 7. Cherry-Picking

### What It Is

Cherry-picking copies a single commit from one branch to another. It creates a new commit with the same changes but a different hash.

```bash
# Apply commit abc123 to the current branch
git cherry-pick abc123
```

### When to Use

- **Backporting a bug fix**: A fix on a feature branch needs to be applied to master before the full branch is ready.
- **Extracting a commit**: You made a useful change in the wrong branch and want to move it.

### When NOT to Use

- **As a substitute for branching.** If you need multiple commits from another branch, merge or rebase instead.
- **For regular workflow.** Feature branches should be rebased and merged as a unit, not cherry-picked commit by commit.

### Handling Cherry-Pick Conflicts

Same process as rebase conflicts:

```bash
git cherry-pick abc123
# If conflict:
# Fix the files
git add <resolved-files>
git cherry-pick --continue
# Or abort:
git cherry-pick --abort
```

---

## 8. Advanced Topics

### Git Bisect

Binary search through history to find the commit that introduced a bug.

```bash
# Start bisect
git bisect start

# Mark current state as bad
git bisect bad

# Mark a known-good commit
git bisect good abc123

# Git checks out a commit halfway between. Test it, then:
git bisect good   # if this commit works
git bisect bad    # if this commit has the bug

# Repeat until git identifies the exact commit
# When done:
git bisect reset
```

This is why every commit must compile and work. If commits in the middle of history are broken, bisect cannot function.

### Git Reflog

The reflog is your safety net. It records every change to HEAD, even ones that are not in the normal log (like commits "lost" during a rebase).

```bash
# See the reflog
git reflog

# Output:
# abc123 HEAD@{0}: rebase (finish): ...
# def456 HEAD@{1}: rebase (start): ...
# ghi789 HEAD@{2}: commit: solve(0001): implement two sum

# Recover a "lost" commit
git checkout ghi789
# Or create a branch from it
git branch recovery-branch ghi789
```

**You almost cannot permanently lose work in git** as long as you have committed it. The reflog keeps everything for at least 30 days.

### Git Stash

Stash saves your uncommitted changes temporarily, giving you a clean working directory.

```bash
# Stash current changes with a description
git stash push -m "WIP: two sum solution"

# List stashes
git stash list

# Restore the most recent stash
git stash pop

# Restore a specific stash
git stash pop stash@{2}

# View what is in a stash without applying it
git stash show -p stash@{0}
```

Use stash when you need to switch branches quickly but are not ready to commit.

### Worktrees

Worktrees let you have multiple branches checked out simultaneously in different directories. This is useful when you need to reference one solution while working on another.

```bash
# Create a worktree for a different branch
git worktree add ../leetcode-fix fix/0042-trapping-rain-water

# List active worktrees
git worktree list

# Remove a worktree when done
git worktree remove ../leetcode-fix
```

### Signed Commits Deep Dive

Why sign commits:
- **Authentication**: Proves the commit came from you, not someone impersonating your email
- **Integrity**: Proves the content has not been tampered with
- **Trust chain**: GitHub shows "Verified" badges, increasing community trust

SSH signing (recommended for simplicity):

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
git config --global tag.gpgsign true
```

GPG signing (traditional, more broadly supported):

```bash
# Generate a GPG key
gpg --full-generate-key

# List keys to find your key ID
gpg --list-secret-keys --keyid-format=long

# Configure git
git config --global user.signingkey YOUR_KEY_ID
git config --global commit.gpgsign true

# Add the public key to GitHub
gpg --armor --export YOUR_KEY_ID
# Paste the output into GitHub > Settings > SSH and GPG Keys > New GPG Key
```

---

## 9. Branch Protection Rules

These settings should be configured in GitHub under Settings > Branches > Branch protection rules for `master`.

### Recommended Settings

#### Required Pull Request Reviews

- **Require approvals**: 1 (increase when more maintainers are active)
- **Dismiss stale reviews when new commits are pushed**: Enabled
- **Require review from code owners**: Enable when CODEOWNERS file is added

#### Required Status Checks

The following CI jobs must pass before merge:

- `validate-structure` -- Problem directory follows conventions
- `python-lint` -- Python code passes ruff
- `c-cpp-build` -- C/C++ code compiles without errors
- `commit-lint` -- Commit messages follow format

#### Additional Settings

- **Require linear history**: Enabled (enforces rebase merging, no merge commits)
- **Do not allow force pushes**: Enabled
- **Do not allow deletions**: Enabled
- **Require signed commits**: Aspirational (enable after all contributors set up signing)

### Solo Development Phase

While working alone, start with minimal protection:

1. Require status checks to pass
2. Do not allow force pushes to master

Add the PR requirement when external contributors begin participating.

### Applying These Settings

1. Go to your repository on GitHub
2. Settings > Branches > Add branch protection rule
3. Branch name pattern: `master`
4. Check the boxes as described above
5. Save changes

---

## Quick Reference Card

```
# Daily workflow
git checkout master && git pull
git checkout -b solve/NNNN-problem-name-lang
# ... make changes ...
git add <files>
git commit -m "solve(NNNN): description"
git fetch origin master
git rebase origin/master
git push -u origin solve/NNNN-problem-name-lang
# Open PR on GitHub

# Clean up history before PR
git rebase -i HEAD~N

# After PR is merged
git checkout master && git pull
git branch -d solve/NNNN-problem-name-lang

# Emergency: undo last commit (keep changes)
git reset --soft HEAD~1

# Emergency: recover lost commit
git reflog
git checkout <hash>

# Emergency: abort rebase
git rebase --abort
```
