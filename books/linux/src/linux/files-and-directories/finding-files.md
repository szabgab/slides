# Finding files (find)

* find

```
find .

find . -name \*.xml

-name NAME         wilde card for name of the thing
-iname NAME        like name but ignores case
-user  NAME        things owned by the user
-type [fdlcb]      f = file, d = directory, ...
-size [+/-]n[ck]   min or max size
-inum number       inode numbe of the thing (to find hard links)
-mtime [+/-]n      modified time in days.
```


Actions:



```
-exec command {} \;
-ok command {} \;
```

A little warning. If we run find . -name *.xml (without escaping the wildcard), the shell will try to expand it in the current working
directory. If it is successful that result will be used as the search term.



