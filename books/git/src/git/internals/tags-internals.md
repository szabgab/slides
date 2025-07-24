# tags


A light weight tag that was created using `git tag NAME`
is a simple file saved as `.git/refs/tags/NAME`
that contains the SHA1 of the current commit when the tag was created.



An annotated tag created using `git tag -a NAME` is
a simple file saved as  `.git/refs/tags/NAME`
holding the SHA1 of a newly created object of type "tag"
that was saved in `.git/objects`.



```
$ git cat-file -p SHA1

$ git push --tags
```


