# Appendix
{id: git-appendix}


## Setup remote repository
{id: setup-another-remote-repository}


On the "remote machine"



```
$ mkdir git/repo
$ cd git/repo
$ git init --bare
```


```
$ git remote add origin /home/gabor/work/test_remote/
git push -u origin master
```


## Revert local changes
{id: revert-local-changes}

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




## Undelete a file
{id: undelete-a-file}


After running git rm file, but before committing the change, you suddenly notice you don't need to remove the file.



```
$ git rm file

$ git reset HEAD file
$ git checkout file
```


## Edit config files
{id: git-config-editing}

Open the respective configuration files for editing


* git config --edit --local
* git config --edit --global
* git config --edit --system



## Common Git commands
{id: common-commands}

```
$ git init
$ git status

$ git add FILENAMEs
$ git add .
$ git commit -m "Text"

$ git diff
$ git diff --cached       (aka. --staged)
$ git diff HEAD

$ git log
$ git checkout
$ git checkout branch_n ame


$ git branch
$ git merge  name_of_branch_to_merge_from

$ git tag

$ git clone

$ git remote
$ git remote add

$ git push
$ git push REMOTE  BRANCH_NAME
$ git push REMOTE  LOCAL_BRANCH_NAME:REMOTE_BRANCH_NAME
$ git push REMOTE  HEAD:REMOTE_BRANCH_NAME
$ git push -u REMOTE  branchname    # set up tracking as well

$ git fetch
$ git pull

$ git stash
$ git stash list
$ git stash pop
```


## Tools
{id: tools}

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




## External difftool WinMerge
{id: git-external-difftool}

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



## Resources
{id: git-resources}

* [SourceTree](http://www.sourcetreeapp.com/) a free Git and Mercurical client for Windows and Mac
* [The home of Git](http://git-scm.com/)
* [Pro Git book](http://git-scm.com/book) 
* [Git Guys](http://www.gitguys.com/)
* [Tutorial of Ralf Ebert](http://www.ralfebert.de/tutorials/git/)
* [Git reference site](http://gitref.org/)
* [Leran Git branching](http://pcottle.github.com/learnGitBranching/) interactive tutorial.
* [Why aren't you using git-flow?](http://jeffkreeftmeijer.com/2010/why-arent-you-using-git-flow/)
* [git-flow, a successful Git branching model](http://nvie.com/posts/a-successful-git-branching-model/)
* [What git branching models actually work?](http://stackoverflow.com/questions/2621610/what-git-branching-models-actually-work)
* [How to use a scalable Git branching model called Gitflow (video)](http://buildamodule.com/video/change-management-and-version-control-deploying-releases-features-and-fixes-with-git-how-to-use-a-scalable-git-branching-model-called-gitflow)




