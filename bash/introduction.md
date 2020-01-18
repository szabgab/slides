# Introduction
{id: introduction}


## Echo
{id: bash-echo}
{i: echo}
{i: pwd}
{i: man}

```
echo Hello World
echo $BASH_VERSION
bash --version

echo and pwd  are external programs that we can run using the shell

man bash

man cd    (does not exist)
help cd
```


## First Shell script
{id: bash-hello-world}
{i: echo}
{i: chmod}
{i: #!}

```
chmod +x hello_world.sh
```
![](examples/hello_world.sh)


## Bash command line parameters
{id: bash-command-line-parameters}
{i: $1}
![](examples/hello_foo.sh)

```
$1 $2 $3
$*      which is $1 $2 $3 ...   but that splits up the spaces that might be inside $1 or $2 ..
"$*"    is the same
$@      is the same but
"$@"    is "$1" "$2" "$3" ...
```



## Bash if parameter
{id: bash-if-parameter}
{i: if}
![](examples/if_parameter.sh)



## Bash while-loop
{id: bash-while-loop}
{i: while}
![](examples/while.sh)


## Bash for-loop
{id: bash-for-loop}
{i: for}
![](examples/for_items.sh)


## Bash for loop on files
{id: bash-for-on-files}
{i: for}
![](examples/for_files.sh)


## Bash for loop on command-line arguments
{id: bash-for-on-arguments}
{i: $@}

```
If there is no list to go over (there is no "in something" part) then by default it will go over
the values on the command line as if this was written:

for a in "$@"
```
![](examples/for_arguments.sh)



## Arithmetic in Bash
{id: arithmetic-in-bash}

```
$ x=2
$ echo $x
2

$ (( x = x + 3 ))
$ echo $x
5

$ ((x=x+3))
$ echo $x
8

$ ((x+=1))
$ echo $x
9

$ ((x++))
$ echo $x
10

$ ((x*=2))
$ echo $x
20
```


## Conditionals in Bash
{id: conditionals-in-bash}


Insted of real conditionals in Bash we only have a way to some command was successful or not and
the if will execute code based on this condition.

What does it mean a program is successful or not?  Exit code 0 or anything else.  $?



{i: [[ ]]}
{i: -e}
![](examples/if_file_exists.sh)


## Bash exit code
{id: bash-exit-code}
![](examples/echo_exit_code.sh)


## Bash exit code
{id: bash-condition-on-exit-code}
![](examples/cond_exit_code.sh)


Make sure you save the exit code immediaely after the execution of some code if you'd like to use it later,
as it always contains the exit code of the most recent statement.




## Echo multiline string
{id: bash-echo-multiline-string}
![](examples/echo_multilne_string.sh)


## Redirect multiline string
{id: bash-redirect-multiline-string}
![](examples/redirect_multilne_string.sh)



## User Input (read)
{id: bash-read-input}
![](examples/user_input.sh)

* [Catching user input](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_08_02.html)







