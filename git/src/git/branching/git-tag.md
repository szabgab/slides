# Git tag

* tag

* You release a new version of your software.
* What if later you'll need to come back to the same commit and make some changes?
* How to remember which SHA-1 was this release?

```
$ git tag v1.10
$ git tag -a v1.10 -m "commit message"
```

* A tag marks a specific commit. The former is a "light weight tag", the latter is an "annotated tag".
* The light weight tag is just like a branch that does not move. A pointer to a commit.
* An annotated tag is a full object with owner and message (annotation).
* `git push --follow-tags` only pushes annotated tags


