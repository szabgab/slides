# How to stash only part of the files

Let's say we have made changes to two files (X and Y) and we would like to stash one of them (X)

```
$ git add Y
$ git stash --keep-index
$ git reset HEAD Y
```



