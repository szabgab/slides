# Tools

* [WinMerge](http://winmerge.org/)
* [Kdiff3](http://kdiff3.sourceforge.net/)
* [Beyond Compare](http://www.scootersoftware.com/)

In the Git-Bash you can run Notepad++ like the first command. You can set a Bash alias to it (second line)
and then use that alias to launch Notepad++.

```
$ /c/Program\ Files\ \(x86\)/Notepad++/notepad++.exe
$ alias np="/c/Program\ Files\ \(x86\)/Notepad++/notepad++.exe"
$ np
```

To make this permanent, `cd` to switch the to home directory and there create a file called `.bashrc`
containing the following:



```
alias np="/c/Program\ Files\ \(x86\)/Notepad++/notepad++.exe"
alias ll="ls -al"
```


(On my system this file is located in c:\Users\Gabor, so if you are not familiar with linux, it is probably easier to create the file while using Windows.)



