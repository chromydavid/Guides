# Basic Git Commands
## 1. Setup
    # Check installed Git version
    git --version

    # Set global username and email
    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"

    # Set default text editor (e.g., VS Code, nano, vim)
    git config --global core.editor "code --wait"

    # Set default initial branch name to main
    git config --global init.defaultBranch main

    # List all current configurations
    git config --list --show-origin

---

## 2. Repository Initialization & Cloning
Start a new Git repo or download an existing one.

    # Initialize a new local repository in current directory
    git init

    # Initialize a repository inside a new specific folder
    git init my-project

    # Clone a remote repository over HTTPS
    git clone https://github.com/user/repo.git

    # Clone a specific branch directly
    git clone -b <branch-name> --single-branch https://github.com/user/repo.git

---

## 3. Basic Workflow: Stage, Commit & Status
Track changes, stage files, and record snapshots.

    # Check working directory and staging area status
    git status

    # Stage specific file or all changes
    git add filename.ext
    git add .

    # Stage interactive hunks/chunks (allows partial staging)
    git add -p

    # Commit staged changes with an inline message
    git commit -m "feat: implement user authentication"

    # Stage all tracked modified files and commit in one step
    git commit -am "fix: correct typo in header"

    # Amend the most recent commit (modify message or add missed staged files)
    git commit --amend -m "feat: revised commit message"

---

## 4. Inspection & Diffing
Compare changes between working tree, index, and commit history.

    # View unstaged changes (working directory vs. staging area)
    git diff

    # View staged changes (staging area vs. last commit)
    git diff --staged

    # Compare changes between two branches
    git diff main feature-branch

---

## 5. Commit History & Logging
Browse project history with clean formatting.

    # Standard chronological commit log
    git log

    # Compact one-line summary
    git log --oneline

    # Graphical commit hierarchy with branch tips and merges
    git log --graph --oneline --all --decorate

    # Inspect detailed metadata and diff of a specific commit
    git show <commit-hash>

---

## 6. Branching & Context Switching
Create, switch, list, and delete branches.

    # List all branches (local and remote-tracking)
    git branch -a

    # Create a new branch
    git branch feature/login

    # Switch to an existing branch (or switch -c to create and switch)
    git checkout feature/login
    git switch feature/login

    # Safely delete a merged branch
    git branch -d feature/login

    # Force delete an unmerged branch
    git branch -D feature/login

---

## 7. Merging & Rebasing
Integrate changes from one branch into another.

    # Merge feature branch into main
    git switch main
    git merge feature/login

    # Abort an active merge conflict
    git merge --abort

    # Rebase current branch on top of main (linear history)
    git rebase main

    # Continue rebase after resolving conflicts
    git add resolved-file.txt
    git rebase --continue

    # Interactive rebase of last 3 commits
    git rebase -i HEAD~3

---

## 8. Remote Repositories & Collaboration
Sync with GitHub, GitLab, or remote servers.

    # List configured remote aliases with URLs
    git remote -v

    # Fetch updates from remote without modifying local working branch
    git fetch origin

    # Pull remote changes and merge into current branch
    git pull origin main

    # Push branch to remote and set tracking upstream (-u)
    git push -u origin feature/login

    # Delete a remote branch
    git push origin --delete feature/login

---

## 9. Stashing (Temporary Shelving)
Save incomplete working state without committing.

    # Stash tracked working changes
    git stash

    # List all saved stashes
    git stash list

    # Apply most recent stash and remove it from stash list
    git stash pop

    # Clear all stashes
    git stash clear

---

## 10. Undoing & Resetting
Revert mistakes safely or discard changes.

    # Discard unstaged changes in a specific file
    git restore filename.ext

    # Unstage a file keeping changes in working directory
    git restore --staged filename.ext

    # Mixed reset: move HEAD back, keep changes unstaged
    git reset HEAD~1

    # Hard reset: completely discard last commit and working changes (DESTRUCTIVE)
    git reset --hard HEAD~1

    # Revert a published commit by generating an inverse commit (SAFE)
    git revert <commit-hash>

    # View reflog to rescue "lost" commits
    git reflog

---

## 11. Tagging & Releases
Mark specific release versions in history.

    # List all existing tags
    git tag

    # Create an annotated tag (recommended for releases)
    git tag -a v1.0.0 -m "Release version 1.0.0"

    # Create a lightweight tag
    git tag v1.0.0-lw

    # Push a specific tag to remote
    git push origin v1.0.0

    # Push all local tags to remote
    git push origin --tags

    # Delete a local tag
    git tag -d v1.0.0

    # Delete a remote tag
    git push origin --delete v1.0.0

---

## 12. Advanced Troubleshooting & Clean-up
Tools for fixing bugs and removing unwanted files.

    # Find which commit introduced a bug using binary search
    git bisect start
    git bisect bad                 # Current commit has bug
    git bisect good <commit-hash>  # Known working commit
    # Test, then run: git bisect good OR git bisect bad
    git bisect reset               # End bisect session

    # Clean untracked files (dry-run to preview what will be removed)
    git clean -dn

    # Force remove untracked files and directories
    git clean -fd

    # Cherry-pick a specific commit from another branch into current branch
    git cherry-pick <commit-hash>