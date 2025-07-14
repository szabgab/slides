# Git Objects (Files)

* .git

```
git init
ls -l .git
find .git/objects
find .git/objects -type f

$ git hash-object -w test.txt
$ git cat-file -p  SHA1
$ git cat-file -t SHA1
blob
```

the type of these object is called blob


