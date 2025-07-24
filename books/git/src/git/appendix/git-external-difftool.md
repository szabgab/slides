# External difftool WinMerge


```
git config --replace --global diff.tool winmerge
git config --replace --global difftool.winmerge.cmd
   "winmerge.sh \"\$LOCAL\" \"\$REMOTE\""
git config --replace --global difftool.prompt false
```

Save the following in c:\Users\Gabor\bin\winmerge.sh


```
#!/bin/sh
echo Launching WinMergeU.exe: $1 $2
"$PROGRAMFILES/WinMerge/WinMergeU.exe" -e -ub -dl "Base" -dr "Mine" "$1" "$2"
```

```
$ git difftool
```


