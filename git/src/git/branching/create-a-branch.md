# Create a branch


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


