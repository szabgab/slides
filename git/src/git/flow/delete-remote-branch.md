# Delete remote branch

* delete

Mary


```
$ git co develop
$ git branch -d feature/A

$ git push origin --delete feature/A

# older version:
$ git push origin :feature/A
```


Joe


```
$ git pull
$ git branch -d feature/A
$ git remote prune origin
```


