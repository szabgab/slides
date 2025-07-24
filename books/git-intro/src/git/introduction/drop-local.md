# Drop local changes (restore to HEAD or to index)

* restore
* checkout


```
$ git restore config.pl
$ git checkout config.pl
$ git status
```

**git checkout FILENAME will replace FILENAME in the work tree with the one committed (or if there is a version already staged then to that version). You loose your local work.**

**git checkout . will do it for all the files in the tree.**

```
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

  modified:   README.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

  setup.pl
no changes added to commit (use "git add" and/or "git commit -a")
```


