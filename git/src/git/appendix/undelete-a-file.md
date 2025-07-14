# Undelete a file


After running git rm file, but before committing the change, you suddenly notice you don't need to remove the file.



```
$ git rm file

$ git reset HEAD file
$ git checkout file
```


