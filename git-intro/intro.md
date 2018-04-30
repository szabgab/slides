# DevOps Workshops: Git
{id: introduction-to-git}

## About us
{id: about-us}

* [Yonit Gruber-Hazani](https://www.linkedin.com/in/yonitgruber/)
* [Gabor Szabo](https://www.linkedin.com/in/szabgab/)
* DevOps Workshops http://devops-workshops.code-maven.com/

## About you
{id: about-you}

* Name
* Company
* What do you do
* Something interesting about you

## Version control Systems (VCS)
{id: vcs}

* Local Version Control Systems (LVCS)
* Centralized Version Control Systems (CVCSs)
* Distributed Version Control Systems (DVCS)

## Local Version Control Systems (LVCS)
{id: lvcs}

* Copy files, dated directories
* RCS, short for Revision Control System
* Save a series of patches
* Difficult to collaborate
* Branching is almost impossible

## Centralized Version Control Systems (CVCS)
{id: cvcs}

**Samples:**
* CVS, or Concurrent Versions System
* Apache Subversion (aka. SVN)
* Perforce
* Rational Clear-Case (IBM) (Configuration Management)

**Details:** 
* Central server holds everything (good/bad)
* Easier administration, better control
* Limited or no off-line work
* Single point of failure.
* Branching is easy in some cases (Subversion)
* Merging is still a pain

## Distributed Version Control Systems (DVCS)
{id: dvcs}

**Samples:**
* Git
* Mercurial (hg)
* GNU Bazaar (bzr)
* Darcs

**Details:** 
* Full copy of repository
* No central control (good/bad)
* No single point of failure
* Easy branching
* Easy merging
* Fast
* Allow off-line development

## Git Overview
{id: git-overview}

* Snapshots of the objects (files) and not diffs. Using pointers eliminate duplications.
* Nearly every operation is local. (Off-line work)
* Integrity using SHA-1 hashes of the files. (40 character string of hexadecimal characters called "object name" or "SHA-1 id".)

## Git Installation
{id: getting-git}

[git-scm](https://git-scm.com/)

On **Linux** you use your package manger (apt-get, yum, etc...) or install from git-scm.

* yum install git-core
* apt-get install git-core

On **Microsoft Windows** install Git from git-scm.

On **Mac OSX** use [Homebrew](https://brew.sh/) or git-scm.

## Which version do you have?
{id: version}

Windows: use the Git Cmd

```
$ git --version

git version 2.15.0
```

## Configure Git
{id: configure-git}

**There are three levels of configuration:**
System (--system)
User (--global)
Project (--local)

$ git config ...

**On Unix**
* /etc/gitconfig
* $HOME/.gitconfig (/home/foobar/.gitconfig)
* .git/config

**On Windows**
* "c:\Program Files (x86)\Git\etc\gitconfig"
* %HOMEPATH%\.gitconfig %USERPROFILE%\.gitconfig (C:\Users\Foobar\.gitconfig)
* .git/config

To access them use

```
--system
--global
--local
```

**Samples:**

```
$ git config --global --add user.name "Foo Bar"
$ git config --global --add user.email foo@bar.com

$ git config --list
$ git config --list --global
$ git config user.name      # to see specific value
```

## Configure and Privacy
{id: privacy}

* Your name
* Your e-mail address

* [eBook](https://leanpub.com/collab-dev-git/c/code-maven-ws3): https://leanpub.com/collab-dev-git/c/code-maven-ws3


## Getting help
{id: getting-help}

```
$ git help             # listing the most important commands
$ git help COMMAND     # man page or local web page
$ git COMMAND --help   # the same

$ git help help        # help about the help system
$ git help --all       # list all the git commands
$ git help tutorial    # a simple git tutorial
```

## Exercises Session 1
{id: exercises-1}

* Check if you already have Git installed (open command line, check the version)
* Install git
* Open the command line
* Check which version do you have?
* List the default configuration
* Add your name, email to the global configuration.
* Look at the help page of one of the commands.

## Creating a local repository
{id: local-rep}

```
$ mkdir app
$ cd app
$ git init
Initialized empty Git repository in /c/work/app/.git/

$ git status
On branch master

Initial commit

nothing to commit (create/copy files and use "git add" to track)
```

**This will create a directory called .git and put some files there**

## Create first file
{id: create-first-file}

Create README.txt with one line of text.
Check the status of the working directory.

```
$ git status

On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

      README.txt
nothing added to commit but untracked files present (use "git add" to track)
```

## File status
{id: file-status}

**Each file can be either**
* untracked
* tracked

**tracked files can be**
* unmodified
* modified
* staged

## Add first file
{id: add-first-file}

* git add README.txt
* git status

**Add the files to the index (or staging area, or cache).**

```
$ git add README.txt
$ git status

On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

      new file:   README.txt

```

## Commit first file
{id: commit-first-file}

* git commit -m "Add README"
* git status

```
$ git commit -m "Add README"

[master (root-commit) 1cd95a6] Add README
 1 file changed, 1 insertion(+)
 create mode 100644 README.txt

$ git status

On branch master
nothing to commit, working directory clean
```

## Untracked and Modified
{id: untracked-and-modified}

**Create another file called setup.pl with a single line and also change the README file.**

```
$ git status

On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

      modified:   README.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

      setup.pl
no changes added to commit (use "git add" and/or "git commit -a")
```

## Making some changes
{id: making-some-changes}

edit the README.txt file again, adding a new row.

* git status
* git diff
* git add README.txt
* git status
* git diff
* git diff --cached 
* git diff --staged

```
$ git status

On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

      modified:   README.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

**What has changed?**

```
$ git diff

diff --git a/README.txt b/README.txt
index e51ca0d..a697828 100644
--- a/README.txt
+++ b/README.txt
-Hello Git
+Hello Git
+Second line

$ git add README.txt
$ git status

On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

      modified:   README.txt

```

**What did we change?**

```
$ git diff
$ git diff --cached    (or --staged)

diff --git a/README.txt b/README.txt
index e51ca0d..62567d0 100644
--- a/README.txt
+++ b/README.txt
-Hello Git
 No newline at end of file
+Hello Git
+Second line

$ git commit -m "update README"

[master 1251a45] update README
 1 file changed, 2 insertions(+), 1 deletion(-)
```

## Untracked - Modified - Staged
{id: untracked-modified-staged}

**Create another file called config.pl**

```
$ git status

On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

      modified:   README.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

      config.pl
      setup.pl
no changes added to commit (use "git add" and/or "git commit -a")
```

## Stage it
{id: stage-it}

```
$ git add config.pl

On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

      new file:   config.pl

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

      modified:   README.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

      setup.pl
```

## See the changes
{id: see-the-changes}

**Make some changes to the config.pl file and stage it.**

```
$ notepad config.pl
$ git status

 On branch master
 Changes not staged for commit:
   (use "git add <file>..." to update what will be committed)
   (use "git checkout -- <file>..." to discard changes in working directory)

       modified:   README.txt
       modified:   config.pl

 Untracked files:
   (use "git add <file>..." to include in what will be committed)

       setup.pl
no changes added to commit (use "git add" and/or "git commit -a")

$ git add config.pl
$ git status

 On branch master
 Changes to be committed:
   (use "git reset HEAD <file>..." to unstage)

       modified:   config.pl

 Changes not staged for commit:
   (use "git add <file>..." to update what will be committed)
   (use "git checkout -- <file>..." to discard changes in working directory)

       modified:   README.txt

 Untracked files:
   (use "git add <file>..." to include in what will be committed)

       setup.pl
```

## So what was changed?
{id: so-what-has-changed}

* git diff
* git diff --cached
* git diff HEAD

```
$ git diff

diff --git a/README.txt b/README.txt
index 62567d0..fb89137 100644
--- a/README.txt
+++ b/README.txt
@@ -1,2 +1,4 @@
 Hello Git
 Second line
+Third line
```

**Only the changes to the not staged files are shown**

```
$ git diff --cached
diff --git a/config.pl b/config.pl
index f9d55cd..e2b7f47 100644
--- a/config.pl
+++ b/config.pl
@@ -1 +1,2 @@
  this is the config.pl file
+ second line
```

**Only the changed to the staged files are shown**

```
$ git diff HEAD
diff --git a/README.txt b/README.txt
index 62567d0..fb89137 100644
--- a/README.txt
+++ b/README.txt
@@ -1,2 +1,4 @@
 Hello Git
 Second line
+Third line
+
diff --git a/config.pl b/config.pl
index f9d55cd..e2b7f47 100644
--- a/config.pl
+++ b/config.pl
@@ -1 +1,2 @@
  this is the config.pl file
+ second line
```

**changes between working copy and HEAD**

## Stage and HEAD
{id: stage-and-head}

**working copy  ->  (git add) index -> (git commit) -> HEAD**

$ git diff
* (changes between working copy and staged copy (index, cache))

$ git diff --staged
* (changes between staged copy and HEAD)

$ git diff HEAD
* (changes between working copy and HEAD)
   
## Remove from stage (unstage)
{id: unstage}

```
$ git reset HEAD config.pl

Unstaged changes after reset:
M       README.txt
M       config.pl

$ git status

On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

      modified:   README.txt
      modified:   config.pl

Untracked files:
  (use "git add <file>..." to include in what will be committed)

      setup.pl
no changes added to commit (use "git add" and/or "git commit -a")
```

**$ git reset HEAD will reset all the files currently staged.
See also the unstage alias we created earlier.**

## Drop local changes (restore to HEAD or to index)
{id: drop-local}

```
$ git checkout config.pl
$ git status
```

**git checkout FILENAME will replace FILENAME in the work tree with the one committed (or if there is a version already staged then to that version). You loose your local work.**

**git checkout . will do it for all the files in the tree.**

```
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

  modified:   README.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

  setup.pl
no changes added to commit (use "git add" and/or "git commit -a")
```

## Add all the files
{id: add-all-files}

* $ git add .
* $ git status


```
On branch master
 Changes to be committed:
   (use "git reset HEAD <file>..." to unstage)

   modified:   README.txt
   new file:   setup.pl

$ git commit -m"start writing the setup script"
[master 887d712] start writing the setup script
 2 files changed, 2 insertions(+)
 create mode 100644 setup.pl
```

## Git ignore
{id: ignore}

The **.gitignore** file in the root of the repository can describe sets of files that don't need tracking. 

This will make sure you don't add the files by mistake (e.g. while using git add .) and they won't show up in the output of the git status command.

```
config.ini
.html
.[oa]
~
.swp
```

Add this file to the repository and commit it. This will ensure that no one in the project will have the extra files problem.

## add and commit in one step
{id: one-step}

git add and commit at once of the modified files, but not the new files

* git commit -a -m "some message"

## Move a file
{id: move-file}

* git mv old.txt new.txt


## Remove a file
{id: remove-file}

* git rm setup.pl

```
 On branch master
 Changes to be committed:
   (use "git reset HEAD <file>..." to unstage)

   deleted:    setup.pl

$ git commit -m "remove"
```

## Frequency of commits
{id: frequency-of-commits}



Adding files and committing changes to Git is cheap. What happens if you made some great work during the day and, at 5 pm when you were tired you made some bad changes. How can you go back to the state that was 5 minutes ago?

* Commit after adding a new function.
* Commit after writing a new test case.
* Commit after making any small change.
* Commits are cheap and fast.



## log and blame
{id: log-blame}

* git log
* git log -p
* git log --stat --summary
* git log --graph

## gitk
{id: gitk}

* gitk --all

## blame
{id: git-blame}

* git blame [filename]

![git blame1](git_blame_1.jpg)

![git blame2](git_blame_2.png)

## Exercises Session 2
{id: exercises-2}

* Create a directory and inside create a new local repository.
* Create a directory and in that directory create a file. (You can use Visual Studio or Eclipse or your IDE to start a new project.)
* Add the directories and files to the repository.
* Are there any files that should not be tracked?
* Make sure git will ignore them in this project.
* Make some changes. Check what are the changes. Commit some of them.
* Go over the previous chapter and execute all the commands we went through.
* If there is any problem. Ask for help!


## Alias
{id: alias}

```
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.ci commit
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```

## Git tag
{id: git-tag}

* You release a new version of your software.
* What if later you'll need to come back to the same commit and make some changes?
* How to remember which SHA-1 was this release?
 
```
$ git tag v1.10
$ git tag -a v1.10 -m "commit message"
```

* A tag marks a specific commit. The former is a "light weight tag", the latter is an "annotated tag".
* The light weight tag is just like a branch that does not move. A pointer to a commit.
* An annotated tag is a full object.


## Exercises Session 3
{id: exercises-3}

* Create a tag on the current commit using `git tag -a v1 -m 'this is v1'`
* Use `gitk --all` to see it.
* Use `git log` to see it.

## Branching in Git
{id: branching-in-git}

* You might work on several features and bug-fixes at the same time.
* Sometimes you will need to stop working and implement some other changes.
* There might be several people working on different features at the same time.
* Git allows and encourages frequent commits.

## Create a branch
{id: create-a-branch}

```
$ git branch
* master

$ git branch featurex
$ git branch
  featurex
* master

$ git checkout featurex
Switched to branch 'featurex'
$ git branch
* featurex
  master
```

* Alternative that creates a branch and checks it out:

```
git checkout -b featurex
```

* Make some changes to file, and commit it to the repository.
* Use `gitk --all` to see the branch.

## Switch between branches
{id: switch-between-branches}

```
git checkout master
```

* This will switch to the `master` branch.

* See that the changes have "disappeared".
* Make some other change on the master to README.txt.
* See that the two have diverged (use `gitk --all`).

## Exercises Session 4
{id: exercises-4}

* While still on the master branch create 2 new files A.txt and B.txt with the content "a file" and "b file" respevtively.
* Commit the changes.
* As you make the changes, keep using `gitk --all` to observe the changes.

* Create three new branches featureA, featureB, and featureC. (or any other names)
* On `master` make a commit to `README`. (Add a line 'this is master')
* On `featureA` make a few commits to a file called `A.txt`.
* On `featureB` make a few commits to a file called `B.txt`.  
* On `featureC` make a commit to `README` changing (Add a line 'this is feaure C').

## Simple automatic merge
{id: simple-automatic-merge}

```
$ git checkout master
```

* Merge the feature into master.

```
$ git merge featurex
Merge made by the 'recursive' strategy.
 A.txt |    1 +
 1 file changed, 1 insertion(+)
```

```
$ gitk --all
```


## Merge with conflict
{id: merge-with-conflict}

```
$ git branch featurey
$ git checkout featurey
```

edit the README file, add a line, commit the change.

```
$ git checkout master
```

edit the README file, add a line, commit the change.

```
$ git merge featurey

Auto-merging README
CONFLICT (content): Merge conflict in README
Automatic merge failed; fix conflicts and then commit the result.
```

```
Line before changes
<<<<<<< HEAD
# add fix on master
=======
# line added in featurey
>>>>>>> featurey
```

Edit the README file and resolved the conflict, removing the marks and writing the correct code.

```
$ git add README
$ git ci -m "featurey merged"
```

## Exercises Session 5
{id: exercises-5}

* Merge featureA into the master branch.
* Observe the results with `gitk --all`.

* Then merge featureC into the master branch

## Repeated merge
{id: repeated-merge}

```
$ git checkout featurey
```

edit README add another line

```
$ git add README
$ git ci -m "another line"
```

```
$ git checkout master
$ git merge featurey
```

This time the merge was automatic, and it only included the changes since the previous merge. 

## Delete branch
{id: delete-branch}

```
$ git branch -d featurex
```

## Force delete branch
{id: force-delete-branch}

If you started to work on a feature but arrived to a dead-end. You can get rid of the whole branch without merging it.

```
git branch -D feature
```

## Exercises Session 6
{id: exercises-6}

* Check out featureC, make some changes, commit
* Merge fetureC into master again - it should be without conflict

* Check out featureA, make some changes, commit
* Check out master and run `gitk --all`. featureC should be fully merged and featureA should have commit on it.

* Remove (delete) both featureA and featureC branches.

## rebase
{id: rebase}

* Have straight line of history.
* Make it easier for the maintainer of the application to merge changes.
* Resolve conflicts before the merge.

Create a branch and make some changes

```
git checkout -b feature
...
git add .
git commit -m "some changes"
```

Make some progress on the `master` branch:

```
git checkout master
...
git add .
git commit -m "progress"
```

Observe the situation using `gitk --all &`

```
$  git checkout feature
Switched to branch 'feature'

$  git rebase master
First, rewinding head to replay your work on top of it...
Applying: feature
```

Observe the situation again using `gitk --all &`

## Exercises Session 7
{id: exercises-7}

* featureC has some changes that started a while ago. Since then master made some progress.
* Rebase featureC onto master.
* Observe the state before and after.

## Various ways to list changes
{id: ways-to-list-changes}

* `gitk --all`
* `git log`


## log between commits
{id: log-between-commits}

```
$ git log SHA1..SHA2
```

## log show filenames
{id: log-show-filenames}

```
$ git log --name-only
```

## Show history of renamed file
{id: show-history-of-renamed-file}

```
$ git log --follow --name-only FILENAME
```

## Commits that were not merged yet
{id: commits-that-were-not-merged-yet}

* commits on one branch but not on the other branch

```
$ git log fetureX --not master
```

## Stash
{id: stash}

* You are in the middle of a change (some files have changed in your working directory) when you suddenly think about some refactoring to be done.
* How to save the local changes easily?

* Change some files locally

```
$ git stash        # saves all the changes and leaves the directory clean
Saved working directory and index state WIP on master: 6217360 last-commit
HEAD is now at 6217360 last-commit
```

```
$ git stash list
stash@{0}: WIP on master: 6217360 last-commit
```

* Make some other changes, add and commit them.

```
$ git stash pop     # will merge the stashed changes
```

## Exercises Session 8
{id: exercises-8}

* Make some local changes
* Create a new file
* Stash them away using `git stash -u`
* Observe that the working directory is clean and back to the previous state
* Observe the content of the stash.

* Make some other changes
* Commit them.

* `git stash pop`
* See the previous partial changes are in the working directory. Including the new file.
* Commit the changes.

## bisect - find broken commit
{id: bisect}

```
git bisect start

# test fails
git bisect bad

git checkout old-sha
# test passes
git bisect good

# test passes / fails
git bisect good / bad
```

## Exercises Session 9
{id: exercises-9}

* Create a file called 'add.sh' with the following content:

![](add.sh)

* Make it executable.
* Test it: `./add 23 19` should print 42
* Commit it.

* Create a file called NUMBER and put a 1 in it.
* Commit it.
* Then create 5 more commit changing the file to some other number. (This might help)

```
echo 7 > NUMBER
git commit -am "7"
```

* Then change the `add.sh` file replacing the + by a -.
* Create another 5 commits chaning the NUMBER file.

* No check if the `add.sh` script works
* `./add.sh 23 19` will now prin 4 instead of 42.

* Using bisect find the commit that broke it.


## Using remote repository
{id: using-remote-repository}

* git clone
* git push
* git pull   (fetch and merge)

## Clone repository
{id: clone-repository}

```
cd ~/work
$ git clone ws@git.code-maven.com:demo/
cd demo
```


```
git remote -v

origin	ws@git.code-maven.com:demo/ (fetch)
origin	ws@git.code-maven.com:demo/ (push)
```

## Make some local changes
{id: make-some-local-changes}

```
git checkout -b feature
   edit file
git add .
git commit -m "some change"
```

## push out local changes to branch
{id: pus-out-local-changes-to-branch}

```
git push

fatal: The current branch feature has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin feature
```

```
$  git push -u origin feature

Total 0 (delta 0), reused 0 (delta 0)
To git.code-maven.com:demo/
 * [new branch]      feature -> feature
Branch 'feature' set up to track remote branch 'feature' from 'origin'.
```

## Remove remote branch
{id: remove-remote-branch}


```
$  git push origin :feature

To git.code-maven.com:demo/
 - [deleted]         feature
```

## Resources
{id: resources}

* [Our Meetup page](https://www.meetup.com/Code-Mavens/)
* [Our Facebook page](https://www.facebook.com/Devops.Workshops)
* [Facebook group](https://www.facebook.com/groups/188753948553382/)
* [Slides of Gabor](https://code-maven.com/slides/git/)

## Finding jobs
{id: finding-jobs}

* Send us contact request via LinkedIn (mention the DevOps Workshops in your message).
* Google is hiring - contact Yonit about it.
* Connect to each other via LinkedIn.

* [Yonit Gruber-Hazani](https://www.linkedin.com/in/yonitgruber/)
* [Gabor Szabo](https://www.linkedin.com/in/szabgab/)

