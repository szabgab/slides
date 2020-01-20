# Extra
{id: git-extra}

## Stage hunk-by-hunk
{id: stage-hunk-by-hunk}
{i: hunk}

```
$ git add -p
```


## Edit last commit message
{id: edit-last-commit-message}
{i: amend}

```
$ git commit --amend -m "New commit message"
```


## Push to remote branch
{id: push-to-remote-branch}

```
Mary:
git push -u origin local_branch_name_of_mary

Joe:
$ git fetch
$ git co -b local_for_joe
$ git merge origin/local_branch_name_of_mary
# make changed
$ git push origin HEAD:local_branch_name_of_mary
$ git push -u origin HEAD:local_branch_name_of_mary
```


## Detached HEAD
{id: detached-head}

```
$ git co master
```



## Change last commit message
{id: change-last-commit-message}

```
$ git commit --amend -m "new message"
$ git commit --amend
```


Only do this if the specific commit has not been shared by the public. (Has not been pushed to a remote).
Otherwise it will break the history and merging for everyone.





## How to see the content of the staged version of a file?
{id: show-staged-version}
{i: show}

```
$ git show :FILE
```


## How to see an older version of a file?
{id: show-earlier-content}
{i: show}

```
$ git show HEAD:FILE
$ git show HEAD~2:FILE
$ git show 8931:FILE    (The SHA of the relevant commit)
```


short SHA1 (at least 4 but usually not more than 7)





## Setup git subtree
{id: setup-git-subtree}
{i: subtree}

```
$ cd parent-repo
$ git remote add some-library URL-TO-LIBRARY-REPO
$ git subtree add --prefix lib/ some-library master
$ git log
```


## git subtree change parent
{id: git-subtree-change-parent}

```
$ echo "add to parent" >> README.md
$ git add README.md
$ git commit -m "added to parent"
$ git push
$ git log
```



## git subtree change in subtre
{id: git-subtree-change-subtree}

```
$ echo "add to library" >> lib/README.md
$ git add lib/README.md
$ git commit -m "added to library"
$ git push
```

Pushes out to parent






