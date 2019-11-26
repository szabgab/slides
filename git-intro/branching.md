# Branching
{id: git-branching}

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
$ git commit -m "featurey merged"
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
$ git commit -m "another line"
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


## Working with remote repository
{id: using-remote-repository}

* fork repository (service of the host)

* git clone
* git push
* git pull   (fetch and merge or fetch and rebase)

* Send Pull-Request (service of the host)

* git remote add upstream ..
* git pull upstream master

## Fork repository
{id: fork-repository}

* Visit [particpants](https://github.com/collab-dev/participants)
* fork

## Clone repository
{id: clone-repository}

```
cd ~/work
$ git clone https://github.com/cm-demo/participants.git
cd participants
```


```
git remote -v

origin	https://github.com/cm-demo/participants (fetch)
origin	https://github.com/cm-demo/participants (push)
```

## Make some local changes
{id: make-some-local-changes}

```
git checkout -b feature
   edit participants.json file
git add participants.json
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
To github.com:collab-dev/participants/
 * [new branch]      feature -> feature
Branch 'feature' set up to track remote branch 'feature' from 'origin'.
```

## Send Pull-Request
{id: send-pull-request}

* Visit [particpants](https://github.com/collab-dev/participants)

## Make more changes and update the pull-request
{id: update-pull-request}

```
git add .
git commit
git push
```

* Visit [particpants](https://github.com/collab-dev/participants)


## Follow the changes in the original repository
{id: follow-changes}


```
git remote add upstream https://github.com/collab-dev/participants.git
git checkout master
git pull upstream master
git push
```

## Remove local branch
{id: remove-local-branch}

```
git checkout maste
git branch -d feature
```

## Remove remote branch
{id: remove-remote-branch}


```
$  git push origin :feature

To github.com:collab-dev/participants/
 - [deleted]         feature
```

## Resources
{id: resources}

* [Our Meetup page](https://www.meetup.com/Code-Mavens/)
* [Slides of Gabor](https://code-maven.com/slides/)

## Thank you
{id: thank-you}

* [Gabor Szabo](https://www.linkedin.com/in/szabgab/)
* Help teams improve their development practices

* [Training Courses](https://hostlocal.com/)
* [Workshops](https://workshops.code-maven.com/)

* [Code Maven Meetup](https://www.meetup.com/Code-Mavens/)


