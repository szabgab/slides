# File comparision tests

* -nt
* -ot
* -ef

```
[ file1 -nt file1 ]   file1 is newer than file2
[ file1 -ot file2 ]   file1 is older than file2
[ file1 -ef file2 ]   file1 and file2 point to the same file (e.g. symbolic link)
```



