# Stash


You are in the middle of a change (some files have changed in your working directory) when you suddenly think about some refactoring to be done.
How to save the local changes easily?



```
# change some files locally
$ git stash        # saves all the changes and leaves the directory clean
Saved working directory and index state WIP on master: 6217360 last-commit
HEAD is now at 6217360 last-commit

$ git stash list
stash@{0}: WIP on master: 6217360 last-commit

# make some other changes, add and commit them

$ git stash pop     # will merge the stashed changes
```



