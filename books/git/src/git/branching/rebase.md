# rebase


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



