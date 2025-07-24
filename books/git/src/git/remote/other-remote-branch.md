# Remote branch created by others

```
$ git clone URL
$ git branch --remote      # listing the remote branches

$ git checkout origin/feature
(detached HEAD)
$ git co master

$ git co -b feature origin/feature
$ git push     # will push the the remote feature branch

$ git fetch     # syncs the remote repository to the local one
$ git co feature
$ git merge origin/feature
```


