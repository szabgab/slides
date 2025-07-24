# Shared feature branch

```
A: $ git checkout -b feature
A: $ git push -u origin feature

B: $ git chechkout master
B: $ git pull
B: $ git branch feature origin/feature
```


* Every developer works on the "feature" branch.
* Every developer create a small branch from the "feautre", commits there. pushes it out. Send PR to the feature.


