# Git ignore

* .gitignore

The `.gitignore` file in the root of the repository
can describe sets of files that don't need tracking.
This will make sure you don't add the files by mistake
(e.g. while using git add .) and they won't show up in the
output of the `git status` command.



```
config.ini
*.html
*.[oa]
*~
*.swp
```


Add this file to the repository and commit it.
This will ensure that no one in the project will have the extra files problem.

