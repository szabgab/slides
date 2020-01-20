# Variables
{id: variables}

## Legal variables
{id: rules}

* Variable names must consist of letters, digits, and the underscore
* The first character must be a letter or an underscore
* Any length
* All the existing variables in the current shell are called the "environment" and the are called "environment variables"
* Usually predefined (or system) variables are all upper case letters.
* Some manuals call these variables "Named parameters".



## Setting and getting variables
{id: setting-getting-variables}
{i: $}

* Assignment using = without spaces on either side of =
* All the variables are strings. If there are spaces in the value, the whole value mus be in quotes
* When using a variable we must prefix it with a $ sign

![](examples/script/variables.sh)

```
$ ./examples/script/variables.sh 
foobar
./examples/script/variables.sh: line 5: programmer: command not found

Hello foobar

foobarit
```

{aside}

There are empty lines printing the content of 'occupation' and that of the variable 'nameit'.
{/aside}


## Backtick or back quote
{id: backtick-or-backquote}
{i: `}
![](examples/script/backtick.txt)


## Command substitution
{id: command-substitution}
{i: $()}

{aside}

Bash provides alternative syntax for command substitution. $().
{/aside}


## Exporting variables
{id: export}
{i: export}

{aside}

The following command may be used to examine and remove things from the environment.
env, set, unset, export
{/aside}

{aside}

If we set a variable using    name=foobar   this variable won't be visible in scripts
we launch because those scripts run in a subshell and the variable is local.

If we would like to make sure the variable is visible in the subshell we have to export
the variable.
{/aside}

```
$ name=foobar
$ echo $name
foobar
$ ./show_name.sh 

$ export name=FooBar
$ echo $name
FooBar
$ ./show_name.sh 
FooBar
```

![](examples/script/show_name.sh)


## env
{id: env}
{i: env}

{aside}
Shows all the exported variables.
{/aside}



## set
{id: set}
{i: set}

{aside}

set - shows all the variables (exported and local)
{/aside}


## unset
{id: unset}

{aside}
unset remove variable
{/aside}

{i: unset}

```
$ echo $username

$ username="foo bar"
$ echo $username
foo bar

$ unset username
$ echo $username

```


## Predefined variables
{id: predefined-variables}

```
DISPLAY
HISTFILE
HISTSIZE
HOME
LANGUAGE
MANPATH
OLDPWD
PATH
SHELL
TERM
USER
```


## Change PATH
{id: change-path}

```
$ echo $PATH
...

$ export PATH=/home/foobar/bin:$PATH
```


## PATH environment variable
{id: path-environment-variable}
{i: PATH}
{i: set}
{i: export}
{i: which}

Setting the PATH environment variable


```
each $PATH
export PATH=/some/new/path:$PATH
set
which command
```







