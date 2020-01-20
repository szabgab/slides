# Bash script
{id: bash-script}

## sh-bang
{id: sh-bang}
{i: #!}
{i: echo}

{aside}

A bash script is just a text file with commands in it. Command like the ones we can give on the command line.
It does not have to have any particular extension, but often people use the .sh extension.
For example foobar.sh

In order to be able to run it we need to make it executable   **chmod u+x foobar.sh**
or to make it exacutable for all the users on the system use   **chmod +x foobar.sh**.

To ensure the script always executes as a bash script, and not as the "current shell of the user"
we need to add ad a **sh-bang** line.
{/aside}

```
#!/bin/bash
```

![](examples/script/hello_world.sh)

```
$ ./examples/script/hello_world.sh 
Hello
World
```

![](examples/script/hello_world_more.sh)

```
$ ./examples/script/hello_world_more.sh 
Hello World
```

![](examples/script/hello_world_n.sh)

```
$ ./examples/script/hello_world_n.sh 
HelloWorld
```

![](examples/script/hello_world_space.sh)

```
$ ./examples/script/hello_world_space.sh 
Hello World
```


## Comments in a Shell script
{id: comments}
{i: #}
![](examples/script/comments.sh)

```
$ ./examples/script/comments.sh 
Hello
World
```


## cd in subshell
{id: cd-in-subshell}
![](examples/script/change_dir.sh)

{aside}

When a shell script is executed ./foobar.sh it is executed in a subshell.
This means certain changes made in the script don't apply in the original (parent) shell. 
For example if we change the current working directory using cd, when the script ends, we are back in the
same directory where we started.
{/aside}

```
$ pwd
/home/gabor

$ ./examples/script/change_dir.sh 
/home/gabor
/etc

$ pwd
/home/gabor
```


## Set a variable in a subshell
{id: set-variable-in-subshell}
![](examples/script/change_term.sh)

```
$ echo $TERM
xterm-256color

$ ./examples/script/change_term.sh 
xterm-256color
xterm

$ echo $TERM
xterm-256color
```


## . (dot command)
{id: dot}
{i: source}
{i: .}

{aside}

The **source** and the . command will execute the script in the current shell. Which means the above changes are now persistant even after the script finishes running.
{/aside}

```
$ pwd
/home/gabor
$ . examples/script/change_dir.sh 
/home/gabor
/etc
$ pwd
/etc
```


```
$ echo $TERM
xterm-256color
$ . examples/script/change_term.sh 
xterm-256color
xterm
$ echo $TERM
xterm
```


## Input
{id: input}

* Command line parameters in $1, $2, ..., $#, $*, $@, shift
* Read from STDIN (read)



## Command line parameters
{id: command-line-parameters}
{i: $0}
{i: $1}

{aside}

The shell puts the space separated values from the command line in variables $0 .. $9 where
$0 is the name of the current script. Can handle up to 9 parameters (excluding the script itself)

$10 would be $1 followed by a 0, but we can write ${10} in our script which will be the 10th command line parameter.
{/aside}
![](examples/script/command_line.sh)

```
$ ./examples/script/command_line.sh Foo Bar wins
0: ./examples/script/command_line.sh
1: Foo
2: Bar
```


```
$ ./examples/script/command_line.sh "Foo Bar" wins
0: ./examples/script/command_line.sh
1: Foo Bar
2: wins
```


```
$ ./examples/script/command_line.sh Foo 
0: ./examples/script/command_line.sh
1: Foo
2:
```


## Wildcards on the command line
{id: wildcards-on-the-command-line}

{aside}

If possible, wildcards are expanded before the script is executed:
{/aside}

```
$ ./examples/script/command_line.sh *
0: ./examples/script/command_line.sh
1: README
2: build
```

{aside}
README and build are files in the current directory.
{/aside}



```
$ ./examples/script/command_line.sh *x
0: ./examples/script/command_line.sh
1: *x
2:
```

{aside}
In this case the wildcard does not match anything and thus it is passed to the script as it is.
{/aside}



{aside}

If you want to pass a parameter that contains a wildcard character, we need to quote the parameter or escape the wildcard.
If we try this on the current script, we won't be able to really see the impact:
{/aside}

```
$ ./examples/script/command_line.sh '*'
0: ./examples/script/command_line.sh
1: README build examples intro.xml linux.yml scripts.xml variables.xml
2:
$ ./examples/script/command_line.sh \*
0: ./examples/script/command_line.sh
1: README build examples intro.xml linux.yml scripts.xml variables.xml
2:
```

{aside}
That's because echo itself expands the wildcard when it prints *.
{/aside}



## Command line and wildcard
{id: command-line-and-wildcard}

{aside}

A little script to show that escaping matters.
{/aside}
![](examples/script/command_line_wild.sh)

```
$ ./examples/script/command_line_wild.sh 
0: ./examples/script/command_line_wild.sh
1:

$ ./examples/script/command_line_wild.sh *
0: ./examples/script/command_line_wild.sh
1: README

$ ./examples/script/command_line_wild.sh '*'
0: ./examples/script/command_line_wild.sh
1: README build examples intro.xml linux.yml scripts.xml variables.xml
star

$ ./examples/script/command_line_wild.sh "*"
0: ./examples/script/command_line_wild.sh
1: README build examples intro.xml linux.yml scripts.xml variables.xml
star

$ ./examples/script/command_line_wild.sh \*
0: ./examples/script/command_line_wild.sh
1: README build examples intro.xml linux.yml scripts.xml variables.xml
star
```


## Command line $#, $*, $@
{id: command-line}
{i: $#}
{i: $*}
{i: $@}
![](examples/script/command_line_params.sh)

```
"$*" = "$1 $2 $3 $4 ... $n"
"$@" = "$1" "$2" "$3" "$4" ... "$n"
```

```
$ ./examples/script/command_line_params.sh foo bar
2
foo bar
foo bar

$ ./examples/script/command_line_params.sh "foo bar"
1
foo bar
foo bar
```

{aside}

When put in double quotes "$*" and "$@" are slightly different. (See man bash)
{/aside}


## shift
{id: shift}
{i: shift}
![](examples/script/shift.sh)

```
$ ./examples/script/shift.sh foo bar moo qux zorg
foo bar moo qux zorg
bar moo qux zorg
qux zorg
```

{aside}
shift can move the content of $* to the left by N elements (defaults to 1)
Mostly to avoid dealing with ${10}.
{/aside}



## read
{id: read}
{i: read}
![](examples/script/read.sh)

{aside}
read one line from the standard input
{/aside}


```
$ ./examples/script/read.sh 
What's your name?
Foo
Hello Foo, how are you?
```


## prompte (read -p)
{id: read-p}
![](examples/script/read_p.sh)

```
$ ./examples/script/read_p.sh 
What's your name? Foo
Hello Foo, how are you?
```


## Read several values from one line
{id: read-several-values}
![](examples/script/read_more.sh)

```
$ ./examples/script/read_more.sh 
Please enter two strings: one two
You typed in one and two
```


## Process ID
{id: process-id}
{i: $$}
{i: $PPID}

```
$$      - current process ID
$PPID   - process ID of the parent process
```


## Background process ID $!
{id: background-process-id}
{i: $!}

```
$!   PID of the most recently started background process

$ perl -e 'print $$' &amp;
$ echo $!
```



## Exit from a script
{id: exit-from-a-script}
{i: exit}
{i: $?}

{aside}

Calling exit  will stop the running of the script and set the exit status to 0. Calling exit N with any number of N
will set the exit status to that N.
{/aside}

```
exit   - on the command line to close the window (or the most recent shell)
exit   - in a script to end the script (exit code = most recent statement)
exit n - exit code n
```



## Exit status in $?
{id: exit-status}
{i: $?}

{aside}
Every command has a so-called exit status. A number between 0-255. 0 indicates success. Other numbers indicate some failure.
The exit status of the last command is always saved in $?
{/aside}

```
$ ls
README      build       examples
$ echo $?
0

$ ls /nosuch
ls: /nosuch: No such file or directory
$ echo $?
1
```



## if
{id: if}
{i: if}
{i: else}
![](examples/script/testing_variables.sh)

```
$ ./examples/script/testing_variables.sh 
The number of parameters is 0

$ ./examples/script/testing_variables.sh one
The number of parameters is 1

$ ./examples/script/testing_variables.sh one two
there are 2 parameters

$ ./examples/script/testing_variables.sh one two three
The number of parameters is 3
```



## elif
{id: elif}
{i: elif}
![](examples/script/elif.sh)


## file tests
{id: file-tests}
{i: -e}
{i: -f}
{i: -d}
{i: -e}
![](examples/script/file_tests.sh)

```
$ ./examples/script/file_tests.sh 
Usage ./examples/script/file_tests.sh FILE

$ ./examples/script/file_tests.sh abc
abc does NOT exist

$ ./examples/script/file_tests.sh .
. if a directory

$ ./examples/script/file_tests.sh examples/script/file_tests.sh 
examples/script/file_tests.sh if a file
```

{aside}
The spaces inside the square brackets are significant.
{/aside}


```
-e    thing exists
-f    thing is a file
-d    thing is a directory
-L    thing is a symbolic link
-s    thing is not empty
...
-r    thing is readable by current user
-w    thing is writable by current user
-x    thing is executable by current user
```


## File comparision tests
{id: file-comparision-tests}
{i: -nt}
{i: -ot}
{i: -ef}

```
[ file1 -nt file1 ]   file1 is newer than file2
[ file1 -ot file2 ]   file1 is older than file2
[ file1 -ef file2 ]   file1 and file2 point to the same file (e.g. symbolic link)
```


## Empty string
{id: empty-string}
{i: ""}
![](examples/script/empty_string.sh)

```
$ ./examples/script/empty_string.sh 
Please type in your name: Foo

$ ./examples/script/empty_string.sh 
Please type in your name: 
Name was missing
```


## Boolean tests
{id: boolean-tests}
{i: &amp;&amp;}
{i: ||}
{i: !}
![](examples/script/boolean.sh)


## Boolean expressions
{id: boolean-expressions}
![](examples/script/boolean_expressions.sh)


## Testing strings - comparing their values
{id: testing-strings}
![](examples/script/testing_strings.sh)


## case
{id: case}
{i: case}
{i: esac}
![](examples/script/case.sh)

```
$ ./examples/script/case.sh foo
it is foo

$ ./examples/script/case.sh abc
letters

$ ./examples/script/case.sh 123
digits

$ ./examples/script/case.sh 42
digits

$ ./examples/script/case.sh 
default

$ ./examples/script/case.sh abc123
letters
```

* ;;      - no subsequent cases are checked
* ;&amp;  - execute the subsequent blocks until ;; is found or till the esac.
* ;;&amp; - check the subsequent condition till you find a match.



## Debugging
{id: debugging}
{i: -v}
{i: -x}

```
bash -v script.sh   - echos commands before variable substitution
bash -x script.sh   - echos commands after varaiable substitution
```


## while-loop
{id: while-loop}
{i: while}
{i: do}
{i: done}
![](examples/script/while.sh)


## for loop
{id: for-loop}
{i: for}

```
for var [ in word... ]
do
   statements
done
```
![](examples/script/for_loop.sh)


## Iterate over commend line arguments
{id: iterate-command-line-arguments}

{aside}

By omitting the list of values the for-loop needs to go over, it will default to the 
list of values supplied on the command line.
{/aside}
![](examples/script/for_argv.sh)

```
$ ./examples/script/for_argv.sh 
$ ./examples/script/for_argv.sh one two
one
two
```


## break
{id: break}
{i: break}

{aside}
break exits the smallest enclosing for, while, until or select loop
break n  exits the nth enclosing loop
{/aside}




## continue
{id: continue}
{i: continue}

{aside}

Goes to the next iteration of the loop, skipping the rest of the code in the current iteration.
{/aside}


## Testing commands
{id: testing-commands}
![](examples/script/testing_command.sh)

```
$ ./examples/script/testing_command.sh Gate
_taskgated:*:13:13:Task Gate Daemon:/var/empty:/usr/bin/false
found Gate in /etc/passwd
```

{aside}

We can check the exit value of a command directly as the command is executed.
The problem is that in many cases we are not interested in the output of the command, just if it was successful or not.
Redirection to /dev/null can solve the problem by hiding the extra output.
{/aside}


## Testing commands while redirecting output
{id: testing-command-while-redirecting}
![](examples/script/testing_command_redirect.sh)



## Shell arithmetic
{id: shell-arithmetic}
{i: expr}

```
$ expr 2 + 3
5


declare variable using 
declare -i variable_name
(typeset -i obsolete way?)

Opeartors
+
-
*
/
% modulo
&lt;&lt; - left shift
&gt;&gt; - right shift
&amp; | ^ ~  - bitwise and, or, not, one's complement
```
![](examples/script/math.sh)

```
Arithmetic tests
&lt;=
&lt;
&gt;=
&gt;
==
!=
!
&amp;&amp;
||
```


## Arrays
{id: arrays}
![](examples/script/array.sh)


## Create array
{id: create-array}
![](examples/script/array_creation.sh)

```
$ ./examples/script/array_creation.sh 
Mon
-----
Mon
Tue
Wed
Thu
Fri
Sat
Sun
```




