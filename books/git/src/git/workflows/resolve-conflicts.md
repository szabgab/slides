# Resolve conflicts


* A makes changes to the same area where B is making changes.
* B: `git push` rejected
* B: `git pull --rebase`


![](images/more-change-by-a.png)


```
remote: Counting objects: 3, done.
remote: Total 3 (delta 0), reused 0 (delta 0)
Unpacking objects: 100% (3/3), done.
From /Users/gabor/work/git/git-server
   3f6fad3..126d1f8  master     -> origin/master
First, rewinding head to replay your work on top of it...
Applying: add another line by A
Applying: A at the bottom
Using index info to reconstruct a base tree...
M	README
Falling back to patching base and 3-way merge...
Auto-merging README
CONFLICT (content): Merge conflict in README
error: Failed to merge in the changes.
Patch failed at 0002 A at the bottom
Use 'git am --show-current-patch' to see the failed patch

Resolve all conflicts manually, mark them as resolved with
"git add/rm &lt;conflicted_files&gt;", then run "git rebase --continue".
You can instead skip this commit: run "git rebase --skip".
To abort and get back to the state before "git rebase", run "git rebase --abort".
```


