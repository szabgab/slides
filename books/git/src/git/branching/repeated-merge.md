# Repeated merge

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



