# bisect - find broken commit

```
git bisect start

# test fails
git bisect bad

git checkout old-sha
# test passes
git bisect good

# test passes / fails
git bisect good / bad
```


