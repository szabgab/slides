# Push to remote branch

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


