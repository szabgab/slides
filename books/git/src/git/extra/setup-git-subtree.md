# Setup git subtree

* subtree

```
$ cd parent-repo
$ git remote add some-library URL-TO-LIBRARY-REPO
$ git subtree add --prefix lib/ some-library master
$ git log
```


