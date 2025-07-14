# More configuration - alias

* alias

```
$ git config --global --add alias.st status
$ git config --global --add alias.ci commit
$ git config --global --add alias.co checkout
$ git config --global --add alias.br branch

$ git config --global color.ui true
$ git config --global alias.lol "log --oneline --graph --decorate"
$ git config --global --add core.editor notepad
$ git config --global --add merge.tool vimdiff
$ git config --global --add alias.unstage "reset HEAD"

$ git config --global --unset core.editor

$ git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
```


