# Git Branching
{id: git-branching}

## Create a branch
{id: start-a-branch}
{i: branch}


You might work on a feature or a bug-fix, sometimes you will need
to stop working and implement some other changes. There might be several people
working on different features at the same time. Git allows and encourages frequent commits



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


Check using gitk



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

```
$ git tag v1.10
$ git tag -a v1.10 -m "commit message"
```


Marks a specific commit. The former is a "light weight tag", the latter is an "annotated tag".




The light weight tag is just like a branch that does not move. A pointer to a commit.




An annotated tag is a full object.




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





