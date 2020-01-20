# Git Remote
{id: git-remote}


## Setup remote repository
{id: setup-remote-repository}


On the "remote machine"



```
$ mkdir git/repo
$ cd git/repo
$ git init --bare
```


## Clone a repository
{id: clone}
{i: clone}

```
$ cd ~/work
$ git clone /path/to/git/repo
```


## List remote repositories
{id: git-remote-v}

```
$ git remote
$ git remote -v
```


## push
{id: git-push}

Do some work, make some changes, commit several times


```
$ git push
```


## fetch
{id: git-fetch}

```
$ git fetch
$ git co master
$ git merge origin/master
```


## pull
{id: git-pull}

```
$ git pull
```

pull is the same as fetch+merge, but it is probably better to do it in two step. First fetch and then try to merge.



## Simple Centralized workflow
{id: simple-centralized-workflow}


One central git repository where everyone has read/write access.
You can work off-line without caring what the others do making changes, commiting to your repository.
Before you try to push you will first have to fetch and merge to integrate all the changes others did.
Then you can push your own changes.




## incoming, outgoing
{id: git-logs}

git incoming - After a fetch it will show what is on the remote master barnch that I have not merged into my own master.


```
$ git log origin/master ^master
```


git outgoing - What is on my master that has not been pushed to the remote master


```
$ git log master ^origin/master
```



## Remote branch
{id: remote-branch}

```
$ git branch
$ git branch --remote
$ git branch --all

$ git config --global push.default  simple

$ git co -b feature

$ git push -u origin feature

$ git fetch
$ git co feature
$ git merge origin/feature
$ git push

$ git push origin --delete feature

# older version:
$ git push origin :feature
```


## Remote branch created by others
{id: other-remote-branch}

```
$ git clone URL
$ git branch --remote      # listing the remote branches

$ git checkout origin/feature
(detached HEAD)
$ git co master

$ git co -b feature origin/feature
$ git push     # will push the the remote feature branch

$ git fetch     # syncs the remote repository to the local one
$ git co feature
$ git merge origin/feature
```


## Exercise
{id: exercise-remote}

* Create a directory and in it create a --bare repository, or if you have a remote sandbox repository use that.
* Clone it to 'local' directory (joe)
* Add 2 files
* Push them to the main repository.
* Clone the repository to another location on the hard-disk (mary)
* Make some changes: create a file your_git_user.txt
* push the changes to the server


* Clone a reposiotry
* Create local develop branch tracking the remote develop branch
* Create local branch feature/USERNAME
* Make some changes
* Push the changes to the remote feature/USERNAME  branch
* Fetch the remote to see if other have been doing anything


Some  commands you might need


```
$ git clone URL
$ git checkout -b local_name
$ git checkout -b local_name origin/remote_name
$ git fetch
$ git push
$ git merge origin/remote_name
```






