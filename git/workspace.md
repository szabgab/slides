# Git Workspace
{id: git-workspace}

## tags
{id: tags}

A light weight tag can be created using `git tag NAME`.

An annotated tag can be created using `git tag -a NAME`.

```
$ git tag v3.0
$ git tag v3.0 SHA1

$ git tag -a v3.0

$ git push --tags
```


## Stash
{id: git-stash}


You are in the middle of a change (some files have changed in your working directory) when you suddenly think about some refactoring to be done.
How to save the local changes easily?



```
# change some files locally
$ git stash        # saves all the changes and leaves the directory clean
Saved working directory and index state WIP on master: 6217360 last-commit
HEAD is now at 6217360 last-commit

$ git stash list
stash@{0}: WIP on master: 6217360 last-commit

# make some other changes, add and commit them

$ git stash pop     # will merge the stashed changes
```


## Stash untracked files as well
{id: stash-untracked-files}

```
$ stash --include-untracked
$ stash -u
```

## Stash selected files
{id: stash-selected-files}

```
git stash push filename
```

## How to stash only part of the files
{id: stash-some-files}


Let's say we have made changes to two files (X and Y) and we would like to stash one of them (X)



```
$ git add Y
$ git stash --keep-index
$ git reset HEAD Y
```


## Clear stash
{id: stash-clear}


Remove everything from stash



```
$ git stash clear
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




## Undo last commit
{id: undo-last-commit}
{i: undo}

```
$ git reset --soft HEAD~


$ git commit ...
$ git reset --soft HEAD^
$ edit
$ git add ....
$ git commit -c ORIG_HEAD     (
```


## Undo git reset
{id: undo-git-reset}

```
$ git reset HEAD~

$ git reset HEAD@{1}

$ git reflog    # to list the history of HEAD
```



## git bisect - finding bugs
{id: git-bisect}

* Notice a bug that you recall was working earlier. (but apparently there were no automated tests checking it)
* Task: find the change that broke it



* Find an old commit where it was still working.
* Binary search the commit since then to locate the breaking change.

Preferably write an automated test that can verify the feature. Put it in a separate test file in the workspace.


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

![](examples/git/add.sh)

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



## git rebase
{id: git-rebase}



