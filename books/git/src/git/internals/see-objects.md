# See Objects


```
$ mkdir test
$ cd test
$ git init
$ ls -al
$ ls -al .git
$ find .git
$ echo "first version" > README
$ git add README
$ find

# observe the creation of .git/objects/22/de8d69c9026be2a49f540fda12f3e755a33e6c
$ git cat-file -t 22de8d69c9026be2a49f540fda12f3e755a33e6c
blob
$ git cat-file -p 22de8d69c9026be2a49f540fda12f3e755a33e6c
first version

$ git ci -m "commit first ver"

$ .git/COMMIT_MESSAGE   (always the last commit message)

Two more objects appeared:
  a tree object and a commit object

.git/refs/heads/master  was created with the SHA1 of commit object in it

$ echo "second version" >> README
$ git add README

   new blob object created
   .git/index file updated
```



