# Forgetting to rebase


* If you executed a **git pull** and forgot to add **--rebase** it can be still fixed.
* If you have not pushed it out yet: `$ git reset HEAD~1 --hard`
* Then you can `$ git pull --rebase`


