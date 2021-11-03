# Git Intro
{id: git-intro}

## Updated slides
{id: updated-slides}

These slides are not maintained any more. Check out our other [Git slides](https://code-maven.com/slides/git/).

## Self intro
{id: self-intro}

* [Gabor Szabo](https://www.linkedin.com/in/szabgab/)
* Help teams improve their development practices

* [Training Courses](https://hostlocal.com/)
* [Workshops](https://workshops.code-maven.com/)

* [Code Maven Meetup](https://www.meetup.com/Code-Mavens/)

## Why use a version control?
{id: why-use-version-control}

* Fearless experimentations
* Fearless deletition
* Easier (smoother) collaboration
* History
* git, mercurial, subversion, cvs, rcs, ...

## Git Installation
{id: getting-git}


On **Linux** you use your package manger (apt-get, yum, etc...) or install from [git-scm](https://git-scm.com/)

* `yum install git-core`
* `apt-get install git-core`

On **Microsoft Windows** install Git from [git-scm](https://git-scm.com/).

On **Mac OSX** use [Homebrew](https://brew.sh/) or [git-scm](https://git-scm.com/).

* `brew install git`

## Which version do you have?
{id: version}

Windows: use the Git Cmd

```
$ git --version

git version 2.20.1
```

## Configure Git
{id: configure-git}
{i: config}

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
* `youruser+github@gmail.com`

* [eBook](https://leanpub.com/collab-dev-git)


## Getting help
{id: getting-help}
{i: help}

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

* Check if you already have Git installed (open command line, check the version) On MS Windows start the git-bash.
* If you don't have it installed yet, then install git.
* Open the command line.
* Check which version do you have?
* List the default configuration.
* Add your name, email to the global configuration.
* Look at the help page of one of the commands.

## 4 Ways to get started
{id: 4-ways-to-get-started}

* [Create empty local repository](local-rep.html)
* Create repository in local directory where we already have files of the project
* Clone remote repository
* [Fork and then clone remote repository of someone else](using-remote-repository.html)


## Creating a local empty repository
{id: local-rep}
{i: status}

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

**This will create a directory called .git and put some files there.**

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

## Add first file
{id: add-first-file}
{i: add}

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
{i: commit}

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

## File status
{id: file-status}

**Each file can be either**
* untracked
* tracked

**Tracked files can be**
* unmodified
* modified
* staged

## Drop local changes (restore to HEAD or to index)
{id: drop-local}
{i: restore}
{i: checkout}


```
$ git restore config.pl
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

## Remove from stage (unstage) (restore to modified)
{id: unstage}

```
$ git restore --staged config.pl
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

## .git/info/exclude
{id: git-info-exclude}

You can have a file called `.git/info/exclude` with similar format to the `.gitignore` file where you would list
the files that should be ignored only on your computer. I don't think it is a good practice to use this.

* Others might have the same files that need to be excluded.
* You might move to a different computer and need to set that up manually.



## .gitkeep
{id: gitkeep}

* Git won't track an empty directory, but sometimes you would like to have one in your repository so your code can assume the directory is there (e.g. for temporary files or for caching).

* Not a real feature but a convention is to add an emty file called `.gitkeep` to the directory you'd like to keep and add that file to git. This will make git track the directory.

* If you also want to ignore all the content of that directory you can use .gitignore. In that case you might need to use the force to add the file to git: `git add --force some/directory/.gitkeep`

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



## log and
{id: log}

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
* An annotated tag is a full object with owner and message (annotation).
* `git push --follow-tags` only pushes annotated tags

## Remove tags
{id: remove-tags}

Locally:

```
git tag -d TAGNAME
```

Remotely:

```
git push --delete origin TAGNAME
```


## Exercises Session 3
{id: exercises-3}

* Create a tag on the current commit using `git tag -a v1 -m 'this is v1'`
* Use `gitk --all` to see it.
* Use `git log` to see it.

