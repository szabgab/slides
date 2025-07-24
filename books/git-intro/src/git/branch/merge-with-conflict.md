# Merge with conflict


```
$ git branch featurey
$ git checkout featurey
```

edit the README file, add a line, commit the change.

```
$ git checkout master
```

edit the README file, add a line, commit the change.

```
$ git merge featurey

Auto-merging README
CONFLICT (content): Merge conflict in README
Automatic merge failed; fix conflicts and then commit the result.
```

```
Line before changes
<<<<<<< HEAD
# add fix on master
=======
# line added in featurey
>>>>>>> featurey
```

Edit the README file and resolved the conflict, removing the marks and writing the correct code.

```
$ git add README
$ git commit -m "featurey merged"
```

