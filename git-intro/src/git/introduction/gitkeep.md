# .gitkeep


* Git won't track an empty directory, but sometimes you would like to have one in your repository so your code can assume the directory is there (e.g. for temporary files or for caching).

* Not a real feature but a convention is to add an emty file called `.gitkeep` to the directory you'd like to keep and add that file to git. This will make git track the directory.

* If you also want to ignore all the content of that directory you can use .gitignore. In that case you might need to use the force to add the file to git: `git add --force some/directory/.gitkeep`


