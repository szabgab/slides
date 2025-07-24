# Try Git Flow


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

