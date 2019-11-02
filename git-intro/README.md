
* Merge A to B
* Create a new branch called C from A
* Make a change on C
* Make 2 more changes on A
* Merge A to B again
* Delete branch C
* Delete branch A
* Merge B to master
* delete B


-------------------------- old slides that are probably not needed --------------------------


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

----------------------------------------
