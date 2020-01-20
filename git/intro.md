# Git intro
{id: git-intro}

## Communication
{id: communication}

No version control system can eliminate the need for developers to talk to each other!



## Version control Systems (VCS)
{id: version-control-systems}

* Local Version Control Systems (LVCS)
* Centralized Version Control Systems (CVCSs)
* Distributed Version Control Systems (DVCS)



## Local Version Control Systems (LVCS)
{id: local-version-control-systems}

* Copy files, dated directories
* [RCS](http://en.wikipedia.org/wiki/Revision_Control_System), short for Revision Control System


* Save a series of patches
* Difficult to collaborate
* Branching is almost impossible



## Centralized Version Control Systems (CVCS)
{id: centralized-version-control-systems}

* [CVS](http://en.wikipedia.org/wiki/Concurrent_Versions_System), or Concurrent Versions System
* [Apache Subversion](http://en.wikipedia.org/wiki/Apache_Subversion) (aka. SVN)
* [Perforce](http://en.wikipedia.org/wiki/Perforce)
* [Rational Clear-Case (IBM)](http://en.wikipedia.org/wiki/Rational_ClearCase)  (Configuration Management)


* Central server holds everything (good/bad)
* Easier administration, better control
* Limited or no off-line work
* Single point of failure.
* Branching is easy in some cases (Subversion)
* Merging is still a pain



## Distributed Version Control Systems (DVCS)
{id: distributed-version-control-systems}

* [Git](http://en.wikipedia.org/wiki/Git_(software))
* [Mercurial (hg)](http://en.wikipedia.org/wiki/Mercurial)
* [GNU Bazaar (bzr)](http://en.wikipedia.org/wiki/GNU_Bazaar)
* [Darcs](http://en.wikipedia.org/wiki/Darcs)


* Full copy of repository
* No central control (good/bad)
* No single point of failure
* Easy branching
* Easy merging
* Fast
* Allow off-line development



## Why Git?
{id: why-git}


It seems to be far the most popular DVCS.




## git services
{id: git-services}


* [GitHub](https://github.com/)
* [GitLab](https://gitlab.com/)
* [Bitbucket](https://bitbucket.org/)
* ...




## Git Overview
{id: git-overview}

* Snapshots of the objects (files) and not diffs. Using pointers eliminate duplications.
* Nearly every operation is local. (Off-line work)
* Integrity using SHA-1 hashes of the files. (40 character string of hexadecimal characters called "object name" or "SHA-1 id".)



## Installation
{id: installation}

* On UNIX/Linux you use your package manger (apt-get, yum, etc...) or install from [git-scm](http://git-scm.com/download).
* On Mac: [git-scm](https://git-scm.com/) or use [Homebrew](https://brew.sh/) to install git.
* On Microsoft Windows install Git from [git-scm](https://git-scm.com/).



* yum install git-core
* apt-get install git-core




## Command line
{id: command-line}
{i: cmd}

Linux: Any terminal or console


Windows:


* Start/cmd  - set the properties!
* CLI: All Programs/Git/Git Bash
* GUI: All Programs/Git/Git GUI



## Why Command line?
{id: why-command-line}

* Many different GUI tools.
* Most of the tutorials are for the command line.
* Most of the people who can provide you help understand the command line, but specific GUI tools.




## Which version do you have?
{id: which-version}
{i: --version}

```
$ git --version
git version 2.17.0
```


## Configure Git
{id: git-configure}
{i: config}

There are three levels of configuration:


* System   (--system)
* User     (--global)
* Project  (--local)


```
$ git config ...
```

On Unix


* /etc/gitconfig
* $HOME/.gitconfig  (/home/foobar/.gitconfig)
* .git/config



On Windows


* "c:\Program Files (x86)\Git\etc\gitconfig"
* %HOMEPATH%\.gitconfig %USERPROFILE%\.gitconfig (C:\Users\Foobar\.gitconfig)
* .git/config



To access them use


* --system
* --global
* --local



## Configure Git - personalize
{id: git-configure-personal}
{i: config}

```
$ git config --global --add user.name "Foo Bar"
$ git config --global --add user.email foo@bar.com

$ git config --list
$ git config --list --global
$ git config user.name      # to see specific value
```


## More configuration
{id: more-git-configuration}
{i: alias}

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
```


## Getting help
{id: git-help}
{i: help}
{i: tutorial}

```
$ git help             # listing the most important commands
$ git help COMMAND     # man page or local web page
$ git COMMAND --help   # the same

$ git help help        # help about the help system
$ git help --all       # list all the git commands
$ git help tutorial    # a simple git tutorial
```


See also the [docs on git-scm](http://git-scm.com/docs), including
[this tutorial](http://git-scm.com/docs/gittutorial).


## Exercises
{id: exercise-intro}

* Check if you already have Git installed (open command line, check the version).
* Install Git.
* Open the command line.
* Check which version do you have?
* List the default configuration.
* Add your name, email to the global configuration.
* Look at the help page of one of the commands.

