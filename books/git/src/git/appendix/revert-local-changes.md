# Revert local changes

Changes that were made to the working copy:

```
$ git checkout file-name
```

Changes that were already staged using git add:


```
$ git reset HEAD file-name
```

Last change that was already committed:


```
$ git reset --hard HEAD~1
```

Do NOT do this if the change was already made public.


