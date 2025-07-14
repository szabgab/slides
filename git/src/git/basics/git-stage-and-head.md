# Stage and HEAD

* diff
* HEAD

```
working copy  ->  (git add) index -> (git commit) -> HEAD
```


```
$ git diff
   # (changes between working copy and staged copy (index, cache))
$ git diff --staged
   # (changes between staged copy and HEAD)
$ git diff HEAD
   # (changes between working copy and HEAD)
```



