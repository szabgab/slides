# Git Flow
{id: git-flow}


## About Git Flow
{id: git-flow-about}

Best for web applications or if you only need to handle single version.



## Git Flow branches
{id: git-flow-branches}
{i: flow}

* master        (or deployment)
* hotfixes      (several small branches)
* release       (to prepare for release)
* develop       (or integration)
* feature       (several branches)



## Git flow chart
{id: git-flow-chart}
![](Screen-shot-2009-12-24-at-11.32.03.png)


## Try Git Flow
{id: try-git-flow}


Joe creates a branch called feature/a  and pushes it to the central repository
Mary also wants to work on the same feature, so she pulls it down.



Joe:


```
$ git co master
$ git co -b develop
$ git co -b feature/A
# create file A.txt
$ git add A.txt
$ git ci -m "start A"
```



```
$ git push -u origin feature/A

Counting objects: 4, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 327 bytes, done.
Total 3 (delta 0), reused 0 (delta 0)
Unpacking objects: 100% (3/3), done.
To /home/gabor/work/test_remote/
 * [new branch]      feature/A -> feature/A
Branch feature/A set up to track remote branch feature/A from origin.
```


Mary


```
$ git fetch origin

remote: Counting objects: 4, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0)
Unpacking objects: 100% (3/3), done.
From /home/gabor/work/test_remote
```


```
$ git checkout --track origin/feature/A

Branch feature/A set up to track remote branch feature/A from origin.
Switched to a new branch 'feature/A'
```



## Merge to develop
{id: merge-to-develop}

```
$ git co develop
$ git merge feature/A
$ git push
```


## Delete remote branch
{id: delete-remote-branch}
{i: delete}

Mary


```
$ git co develop
$ git branch -d feature/A

$ git push origin --delete feature/A

# older version:
$ git push origin :feature/A
```


Joe


```
$ git pull
$ git branch -d feature/A
$ git remote prune origin
```


## Gitflow with Fast Forward merges
{id: gitflow-with-ff-merges}

Set up the develop branch on the central server. Needs to be done only once.


```
git clone  URL
git checkout -b develop
git push -u origin develop
```


Developer sets up a local version of the develop branch. Each developer (in each clone) needs to do once.


```
git clone  URL
git checkout -b develop origin/develop
```

When a developer starts to work on feature X, she needs to create a local branch and push ot to the server.


```
git checkout -b feature/X
git push -u origin feature/X
```

Other developer who also wants to work on feature X, needs to create local branch for it tracking the respecive remote branch.


```
git fetch
# Using git branch --remote  make sure origin/feature/X  already exists
git checkout feature/X origin/feature/X
```


Developers do they work on the feature/x branch and push it out to remote.
Sometimes they fetch from remote and integrate the changes the other developer(s) of feature/x
have done.



```
git add ....
git commit ...
git fetch
git merger origin/feature/X
git push
```


When the feature is finished one of the developers needs
to integrate the changes in develop since the start of featoure/X and feature/X itself.
In order to keep feature/X intact we do this integration in a separate branch:



```
# first update develop
git fetch
git checkout develop
git merge --ff-only origin/develop    # fast-forward

# create the integration branch
git checkout feature/X
git checkout -b integrate/X
git merge develop                     # there might be conflicts!
```


The branch integrate/X can be tested. If something is broken, the developers can
fix it on feature/X and merge it again into integrate/X. Once the integration is done
and the integrate/X was pused to the central server,



```
git checkout integrate/X
git push -u origin integrate/X
```


At this point the branch integrate/X contains all the changes in develop and all the changes in feature/X and the developers have tested it.
Now we can allow a tester to test this on her own machine:



```
git fetch
git checkout -b integrate/X   origin/integrate/X
# Testing, if it failed, complain to the developers and then later:

git fetch
git checkout integrate/X
git merge --ff-only origin/integrate/X   # fast-forward
```


Once the Tester accepts the version, the Chief Integrator (CI) - who is not necessarily a developer
- can now integrate this branch into develop using fast forward:



```
git fetch
git checkout develop

# Check if there are any changes on develop that are not yet in feature/X
# the next log should be empty
git log develop --not origin/integrate/X

git merge --ff-only origin/integrate/X  # only if it is fast-forward
```



There is a separate command set for release and for hotfixes:



```
git checkout develop
git checkout -b release/v1.00
git push -u origin release/v1.00
# do some last minute work on the relaase branch. Once it is done
git checkout master
git merge --ff-only release/v1.00    # fast forward
git tag v1.00                        # tag is placed on the master
git checkout release/v1.00
git merge develop                    # resolve conflicts if necessary
# Test
git checkout develop
git merge --ff-only release/v1.00    # fast forward
```


hotfix is the same as release except it stars from 'master' and not from 'develop'
and the branch is called hotfix/v1.01.







