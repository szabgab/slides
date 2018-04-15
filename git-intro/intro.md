# DevOps Workshops: Git
{id: introduction-to-git}

## About us
{id: about-us}

* Yonit Gruber-Hazani
* Gabor Szabo
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

On UNIX/Linux you use your package manger (apt-get, yum, etc...) or install from git-scm.

* yum install git-core
* apt-get install git-core

On Microsoft Windows install Git from msysgit (Git and not msysGit)
On Mac: Git OSX installer

## Which version do you have?
{id: version}

Windows

```
c:\> git --version
git version 1.8.1.msysgit.1
```

OSX

```
$ git --version
git version 2.1.3
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
Initialized empty Git repository in C:/work/app/.git/
$ git status
# On branch master
#
# Initial commit
#
nothing to commit (create/copy files and use "git add" to track)
```

**This will create a directory called .git and put some files there**

## Create first file
{id: create-first-file}

Create README.txt with one line of text.
Check the status of the working directory.

```
$ git status
examples/out/status_01.txt
# On branch master
#
# Initial commit
#
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#
#       README.txt
nothing added to commit but untracked files present (use "git add" to track)
```

## File status
{id: file-status}

**Each file can be either**
* untracked
* tracked
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
examples/out/status_02.txt
# On branch master
#
# Initial commit
#
# Changes to be committed:
#   (use "git rm --cached <file>..." to unstage)
#
#       new file:   README.txt
#
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
# On branch master
nothing to commit, working directory clean
```

## Making some changes
{id: making-some-changes}

edit the README.txt file again, adding a new row.
* git status
* git diff
* git add README.txt
* git status
* git diff
* git$ git diff --cached (or --staged)

```
$ git status
# On branch master
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#       modified:   README.txt
#
no changes added to commit (use "git add" and/or "git commit -a")
```

**What has changed?**

```
$ git diff
WARNING: terminal is not fully functional
diff --git a/README.txt b/README.txt
index e51ca0d..a697828 100644
--- a/README.txt
+++ b/README.txt
@@ -1 +1,2 @@
-Hello Git
+Hello Git
+Second line

$ git add README.txt
$ git status
examples/out/status_05.txt
# On branch master
# Changes to be committed:
#   (use "git reset HEAD <file>..." to unstage)
#
#       modified:   README.txt
#
```

**What did we change?**

```
$ git diff
$ git diff --cached    (or --staged)
WARNING: terminal is not fully functional
diff --git a/README.txt b/README.txt
index e51ca0d..62567d0 100644
--- a/README.txt
+++ b/README.txt
@@ -1 +1,2 @@
-Hello Git
\ No newline at end of file
+Hello Git
+Second line
$ git commit -m "update README"
[master 1251a45] update README
 1 file changed, 2 insertions(+), 1 deletion(-)
 ```

## title
{id: title}


## Resources
{id: resources}
* [Our Meetup page](https://www.meetup.com/Code-Mavens/)
* [Our Facebook page](https://www.facebook.com/Devops.Workshops)
* [Facebook group](https://www.facebook.com/groups/188753948553382/)
* [Slides of Gabor](https://code-maven.com/slides/git/)


