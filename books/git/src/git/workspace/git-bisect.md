# git bisect - finding bugs

* Notice a bug that you recall was working earlier. (but apparently there were no automated tests checking it)
* Task: find the change that broke it



* Find an old commit where it was still working.
* Binary search the commit since then to locate the breaking change.

Preferably write an automated test that can verify the feature. Put it in a separate test file in the workspace.


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


