# Shell
{id: shell}

## cal - calendar
{id: cal}
{i: cal}

```
$ cal
$ cal 2015
$ cal 1 2015
```


## bc - calculator
{id: bc}
{i: bc}

```
$ bc
3/2
1
Ctrl-d
```


```
bc -l
3/2
1.50000000000000
Ctrl-d
```


## time commands
{id: time}
{i: time}

```
time find .
```


Will do all the work find does and at the end it will print how long did it take to run the given command.



```
real    0m0.757s
user    0m0.002s
sys     0m0.005s
```


## Separating commands
{id: separating-commands}
{i: ;}

```
cd /home; pwd
```

{aside}

Commands are executed in sequence, from left to right.
{/aside}



## Combining commands
{id: combinding-commands}

* The commnad **perldoc -lm Module::Name** will print the full path to the source code of a Perl Module.
* We can take that path and open with vim using:  **vim `perldoc -lm Module::Name`**.
* Maybe better this way: **vim $(perldoc -lm Module::Name)**.



## Bash functions
{id: bash-functions}

Creating an alias for this might be difficult because of the parameter passing but we can create a function.


Add the following to ~/.bashrc and then type **source ~/.bashrc**


Then we can write **epm Module::Name**.


```
function epm(){
    vim $(perldoc -lm $*);
}
```


## Execute shell file
{id: execute-shell-file}
{i: source}
{i: .}
{i: ./}

```
./script_name         Spawn new shell
script_name           Spawn new shell

source script_name    Run in current shell
. script_name         Run in current shell
```



## Grouping commands
{id: grouping-command}
![](examples/intro/grouping_commands.txt)

{aside}

Without the parantheses, the pipe is only applied to the output of the second command.
With the paranetheses, the output of both ls commands are combined and the pipe is applied to that.
A subshell is spawned to execute the commands.
{/aside}
![](examples/intro/grouping_commands_cd.txt)


## Quotes
{id: quotes}
{i: '}
{i: "}
{i: \}
{i: `}
{i: $()}

{aside}

{/aside}

* '' - no special meaning for any character except '
* "" - no special meaning for any character except ", $, \ and `
* \ - escape next character (disable special meaning of next character)
* `` - (backtick) command substitution
* $() - command subsitutions.

![](examples/intro/quotes.txt)


## Spell checking
{id: spell-checking}

* ispell
* aspell



## hostname
{id: hostname}
{i: hostname}
{i: /etc/hostname}

```
$ cat /etc/hostname

$ hostname
```


## date
{id: date}
{i: date}

```
$ date
Wed Jul  6 08:53:10 UTC 2016

$ date +"%d %H:%M"
06 08:55

$ TZ=EST date +"%d %H:%M"
06 03:56
```


## First day of the month
{id: date-in-script}

![](examples/linux/first_day.sh)


## exit and exit code
{id: exit-code}
{i: exit}
{i: $?}
{i: Ctrl-D}

```
$?     - contains the most recent exit code in the parent shell
```

{aside}
Typing 'exit' in a login shell will log out the user.
If it is typed in a terminal, that terminal will be closed.
Ctrl-D has the same effect in a terminal.
{/aside}


## locale
{id: locale}
{i: locale}

```
$ locale

/etc/default/locale
```



## Setting the prompt
{id: prompt}
{i: PS1}

```
echo $PS1

PS1='$(hostname) $'
```


## Secondary prompt
{id: secondary-prompt}
{i: PS2}

```
ls \
&gt;

PS2=':)'
```


## set -o
{id: set-o}
{i: set -o}

```
set -o     listing the status

set -o vi
set -o emacs
```


## Start up files (Login shells)
{id: startup-files-for-login-shells}
{i: profile}
{i: .bash_profile}

```
/etc/profile     - systemwide startup file for every user, only after login
/etc/profile.d/*
~.profile

~/.bash_profile  - user specific startup file, only after login
~/.bash_login
```


## Start up file (Noninteractive shells too)
{id: startup-files-for-noninteractive-shells-too}
{i: .bashrc}

```
/etc/bashrc  - all users, every new shell and subshell

~/.bashrc -  user specific, every new shell and subshell
```


## Startup files
{id: startup-files}
![](examples/intro/startup_files.txt)


## logout script
{id: logout-script}
{i: .bash_logout}

```
~/.bash_logout  - when exiting the shell
```



## Exercise: Prompt
{id: exercise-prompt}

* Set the prompt to be the current hour (or the number of seconds till the end of the day).
* Include the current username in the prompt.
* Include the current directory in the prompt.
* Any other ideas?





