I am using this repo to understand about Git
Basic Git Setup
Check Git Version → git --version
Set Global Username & Email → git config --global user.name "Your Name" & git config --global user.email "your.email@example.com"
View Git Configurations → git config --list
Repository Initialization & Cloning
Initialize a Git Repository → git init
Clone an Existing Repository → git clone <repo-url>
Staging & Committing Changes
Check Repository Status → git status
Add All Changes to Staging → git add .
Add Specific File to Staging → git add <filename>
Commit Changes with a Message → git commit -m "Your commit message"
Commit with All Staged Changes → git commit -a -m "Your commit message"
Branching & Merging
Create a New Branch → git branch <branch-name>
Switch to Another Branch → git checkout <branch-name> or git switch <branch-name>
Create & Switch to a New Branch → git checkout -b <branch-name> or git switch -c <branch-name>
Merge a Branch into Current Branch → git merge <branch-name>
Delete a Branch → git branch -d <branch-name>
Pushing & Pulling Changes
Push Changes to Remote Repository → git push origin <branch-name>
Pull Latest Changes from Remote → git pull origin <branch-name>
Remote Repository Management
View Remote Repositories → git remote -v
Add a Remote Repository → git remote add origin <repo-url>
Change Remote Repository URL → git remote set-url origin <new-repo-url>
Undoing Changes
Undo Last Commit (Keep Changes in Staging) → git reset --soft HEAD~1
Undo Last Commit (Discard Changes) → git reset --hard HEAD~1
Unstage a File → git reset HEAD <filename>
Viewing History & Logs
View Commit History → git log
View One-Line History → git log --oneline
View Changes in Last Commit → git show
Tagging Releases
Create a Tag → git tag -a v1.0 -m "Version 1.0"
List All Tags → git tag
Push Tags to Remote → git push origin --tags
Stashing Changes
Stash Current Changes → git stash
View Stashed Changes → git stash list
Apply Last Stash → git stash apply
Drop a Stash → git stash drop
Other Useful Commands
Check Differences Between Commits → git diff
Revert a Specific Commit → git revert <commit-hash>
Clean Untracked Files → git clean -f
