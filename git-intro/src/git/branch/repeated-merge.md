# Repeated merge

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


