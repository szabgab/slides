# Remove from stage (unstage) (restore to modified)


```
$ git restore --staged config.pl
$ git reset HEAD config.pl

Unstaged changes after reset:
M       README.txt
M       config.pl

$ git status

On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

      modified:   README.txt
      modified:   config.pl

Untracked files:
  (use "git add <file>..." to include in what will be committed)

      setup.pl
no changes added to commit (use "git add" and/or "git commit -a")
```

**$ git reset HEAD will reset all the files currently staged.
See also the unstage alias we created earlier.**


