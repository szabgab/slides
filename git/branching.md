# Git Branching
{id: git-branching}

## Create a branch
{id: start-a-branch}
{i: branch}

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

make some changes to app.pl, and commit them to the repository

* Alternative way that creates a branch and checks it out:

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
{id: merge-a-branch}

```
$ git checkout master
```

* see that the changes have "disappeared"
* make some other change on the master to README.txt
* see that the two have diverged (use gitk)
* merge the feature into master


```
$ git merge featurex
Merge made by the 'recursive' strategy.
 app.pl |    1 +
 1 file changed, 1 insertion(+)

$ gitk --all
```


## Merge with conflict
{id: merge-with-conflict}

```
$ git branch featurey
$ git co featurey
# edit the app.pl file , add a line, commit the change

$ git co master
# edit the app.pl file, add a line, commit the change

$ git merge featurey
Auto-merging app.pl
CONFLICT (content): Merge conflict in app.pl
Automatic merge failed; fix conflicts and then commit the result.
```
![](examples/out/app_with_conflict.pl)

Edit the app.pl file and resolved the conflict, removing the marks and writing the correct code.


```
$ git add app.pl
$ git ci -m "featurey merged"
```


## Repeated merge
{id: repeated-merge}

```
$ git co featurey
# edit app.pl add another line
$ git add app.pl
$ git ci -m "another line"

$ git co master
$ git merge featurey
```


This time the merge was automatic,
and it only included the changes since the previous merge.


## Delete branch
{id: delete-barnch}

* $ git branch -d featurex


## Force delete branch
{id: force-delete-branch}

If you started to work on a feature but arrived to a dead-end. You can get rid of the whole branch without merging it.

```
git branch -D feature
```

## Delete remote branch
{id: delete-branch-from-remote}

```
git push origin :barnchname
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
$ git lot --follow --name-only FILENAME
```


## Commits that were not merged yet
{id: commits-that-were-not-merged-yet}

```
$ git log fetureX --not master
```


## Git tag
{id: git-tag}
{i: tag}

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


## Exercise
{id: exercise-branch}

* Create two branches A and B
* On A make 2 changes
* On B make one change
* Merge A to B
* Create a new branch called C from A
* Make a change on C
* Make 2 more changes on A
* Merge A to B again
* Delete branch C
* Delete branch A
* Merge B to master
* delete B


## Exercises Session 3
{id: exercises-3}

* Create a tag on the current commit using `git tag -a v1 -m 'this is v1'`
* Use `gitk --all` to see it.
* Use `git log` to see it.


