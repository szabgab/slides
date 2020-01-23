# Git Internals
{id: git-internals}

## Plumbing and Porcelan
{id: plumbing-and-porcelan}
{i: branch}


Porcelan refers to the regular commands people use.




Plumbing refers to the low-level system commands of Git



```
```



## The .git directory
{id: git-directory}
{i: .git}

git init


* branches/
* index
* config
* description
* HEAD
* hooks/
* info/
* objects/
* refs/


* **config** holds your project specific configuration.
* **objects/** holds the objects (blob, tree, commit)
* **refs/** holds references to objects
* **hooks/** the local and remote hooks.



## Git Objects (Files)
{id: git-objects}
{i: .git}

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



## See Objects
{id: see-objects}

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



## tags
{id: tags-internals}

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




