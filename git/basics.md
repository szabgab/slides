# Git Basics
{id: git-basics}

## Creating a local repository
{id: git-init}
{i: init}
{i: status}
{i: st}

* $ mkdir app
* $ cd app
* $ git init
* $ git status
* $ git st
* This created a directory called .git and put some files there



```
$ mkdir app
$ cd app
$ git init
Initialized empty Git repository in C:/work/app/.git/
```

```
$ git status
# On branch master
#
# Initial commit
#
nothing to commit (create/copy files and use "git add" to track)
```


## Create first file
{id: git-create-file}
{i: status}

* Create README.txt with one line of text.
* Check the status of the working directory.
* $ git status


```
$ git status
```
![](examples/out/status_01.txt)


## File status
{id: file-status}

Each file can be either


* **untracked**
* **tracked**


* **unmodified**
* **modified**
* **staged**




## Add first file
{id: git-add-file}
{i: index}
{i: staging area}
{i: cache}
{i: add}

* $ git add README.txt
* $ git status



Add the files to the <emp>index</emp> (or staging area, or cache).



```
$ git add README.txt
$ git status
```
![](examples/out/status_02.txt)


## Commit first file
{id: git-commit}
{i: commit}

* $ git commit -m "Add README"
* $ git status


```
$ git commit -m "Add README"
[master (root-commit) 1cd95a6] Add README
 1 file changed, 1 insertion(+)
 create mode 100644 README.txt
```


```
$ git status
# On branch master
nothing to commit, working directory clean
```



## Making some changes
{id: git-make-a-change}
{i: diff}
{i: --cached|diff}

* edit the README.txt file again, adding a new row.
* $ git status
* $ git diff
* $ git add README.txt
* $ git status
* $ git diff
* $ git$ git diff --cached    (or --staged)


```
$ git status
```
![](examples/out/status_03.txt)


What has changed?



```
$ git diff
```

```
WARNING: terminal is not fully functional
diff --git a/README.txt b/README.txt
index e51ca0d..a697828 100644
--- a/README.txt
+++ b/README.txt
@@ -1 +1,2 @@
-Hello Git
+Hello Git
+Second line
```


```
$ git add README.txt
$ git status
```
![](examples/out/status_05.txt)


What did we change?


```
$ git diff
$ git diff --cached    (or --staged)
```


```
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
```


```
$ git commit -m "update README"
```

```
[master 1251a45] update README
 1 file changed, 2 insertions(+), 1 deletion(-)
```



## Untracked and Modified
{id: git-untracked-modified}

Create another file called setup.pl with a single line and also change the README file.


```
$ git status
```
![](examples/out/status_04.txt)


## Untracked/Modified/Staged
{id: git-untracked-modified-staged}

Create another file called config.pl


```
$ git status
```
![](examples/out/status_06.txt)


Stage it


```
$ git add config.pl
```
![](examples/out/status_07.txt)


## Commit the file(s)
{id: commit-one-file}


Only the staged file is committed.




```
$ git commit -m "first version of config.pl"
```

```
[master cdd2c3b] first version of config.pl
 1 file changed, 1 insertion(+)
 create mode 100644 config.pl
```


```
$ git status
```
![](examples/out/status_08.txt)


## See the changes
{id: see-changes}

Make some changes to the config.pl file and stage it.



```
$ notepad config.pl
$ git status
```
![](examples/out/status_09.txt)


```
$ git add config.pl
$ git status
```
![](examples/out/status_10.txt)


So what was changed?


```
$ git diff
```

```
diff --git a/README.txt b/README.txt
index 62567d0..fb89137 100644
--- a/README.txt
+++ b/README.txt
@@ -1,2 +1,4 @@
 Hello Git
 Second line
+Third line
```


Only the changes to the not staged files are shown



```
$ git diff --cached   ( or --staged)
```

```
diff --git a/config.pl b/config.pl
```

```
index f9d55cd..e2b7f47 100644
--- a/config.pl
+++ b/config.pl
@@ -1 +1,2 @@
 # this is the config.pl file
+# second line
```

Only the changed to the staged files are shown




```
$ git diff HEAD
```

```
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
 # this is the config.pl file
+# second line
```


changes between working copy and HEAD





## Stage and HEAD
{id: git-stage-and-head}
{i: diff}
{i: HEAD}

```
working copy  ->  (git add) index -> (git commit) -> HEAD
```


```
$ git diff
   # (changes between working copy and staged copy (index, cache))
$ git diff --staged
   # (changes between staged copy and HEAD)
$ git diff HEAD
   # (changes between working copy and HEAD)
```


## Remove from stage (unstage)
{id: git-unstage}
{i: unstage}
{i: reset HEAD}

```
$ git reset HEAD config.pl
```

```
Unstaged changes after reset:
M       README.txt
M       config.pl
```

```
$ git status
```
![](examples/out/status_11.txt)


<command>$ git reset HEAD</command> will reset all the files currently staged.




See also the unstage alias we created earlier.




## Drop local changes (restore to HEAD or to index)
{id: drop-local-changes}

```
$ git checkout config.pl
$ git status
```


<command>git checkout FILENAME</command>
will replace FILENAME in the work tree with the one committed (or if there is a version already staged then to that version).
You loose your local work.




<command>git checkout .</command> will do it for all the files in the tree.


![](examples/out/status_12.txt)



## Add all the files
{id: add-all}

```
$ git add .
$ git status
```
![](examples/out/status_13.txt)

```
$ git commit -m"start writing the setup script"
```

```
[master 887d712] start writing the setup script
 2 files changed, 2 insertions(+)
 create mode 100644 setup.pl
```


## Git ignore
{id: git-gitignore}
{i: .gitignore}


The <command>.gitignore</command> file in the root of the repository
can describe sets of files that don't need tracking.
This will make sure you don't add the files by mistake
(e.g. while using git add .) and they won't show up in the
output of the <command>git status</command> command.



```
config.ini
*.html
*.[oa]
*~
*.swp
```


Add this file to the repository and commit it.
This will ensure that no one in the project will have the extra files problem.




## .gitkeep
{id: gitkeep}


* Git won't track an empty directory, but sometimes you would like to have one in your repository so your code can assume the directory is there (e.g. for temporary files or for caching).
* Not a real feature but a convention is to add an emty file called **.gitkeep** to the directory you'd like to keep and add that file to git. This will make git track the directory.
* If you also want to ignore all the content of that directory you can use .gitignore. In that case you might need to use the force to add the file to git: **git add --force some/directory/.gitkeep**



## add and commit in one step
{id: add-and-commit}

git add and commit at once of the modified files, but not the new files


```
$ git commit -a -m "some message"
```



## Move a file
{id: move-a-file}
{i: mv}

```
$ mv config.pl app.pl
$ git status
$ git add app.pl
$ git rm config.pl
($ git add -u)
```
![](examples/out/status_14.txt)

```
$ git commit -m "rename"
```

**$ git mv old.pl new.pl**



Try also moving a file and changing its content a bit.





## Remove a file
{id: remove-a-file}
{i: rm}

```
$ git rm setup.pl
```
![](examples/out/status_15.txt)

```
$ git commit -m "remove"
```


## Frequency of commits
{id: frequency-of-commits}


Adding files and committing changes to Git is cheap. What happens if you made some great work during the day and,
at 5 pm when you were tired you made some bad changes. How can you go back to the state that was 5 minutes ago?



* Commit after adding a new function.
* Commit after writing a new test case.
* Commit after making any small change.
* Commits are cheap and fast.



## log
{id: git-log}
{i: log}
{i: gitk}

```
$ git log
$ git log -p
$ git log --stat --summary
$ git log --graph

$ gitk --all
```



## Exercise
{id: exercise-basic}

* Create a directory and inside create a new local repository.
* Create a directory and in that directory create a file.  (You can use Visual Studio or Eclipse or your IDE to start a new project.)
* Add the directories and files to the repository.
* Are there any files that should not be tracked?
* Make sure git will ignore them in this project.
* Make some changes. Check what are the changes. Commit some of them.
* Go over the previous chapter and execute all the commands we went through.
* If there is any problem. Ask for help!




