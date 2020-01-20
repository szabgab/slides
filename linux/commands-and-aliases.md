# Commands and aliases
{id: commands-and-aliases}

## which
{id: which}
{i: which}

{aside}

which shows the path to the given command(s)
{/aside}

```
$ which grep
/usr/bin/grep

$ which echo
/bin/echo

$ which perl
/home/vagrant/localperl/bin/perl

$ which ls
/bin/ls

$ which ll
      (nothing printed)
```


## type
{id: type}
{i: type}

{aside}
type tells us if the command is aliased or not. an external executable.
{/aside}


```
$ type grep
grep is hashed (/usr/bin/grep)

$ type echo
echo is a shell builtin

$ type perl
perl is /home/vagrant/localperl/bin/perl

$ type ls
ls is aliased to `ls --color=auto'

$ type ll
ll is aliased to `ls -alF'
```


## whereis
{id: whereis}
{i: whereis}

{aside}
Show all the places where the given command can be found in the PATH
{/aside}


```
$ whereis perl
perl: /usr/bin/perl /etc/perl /usr/share/perl
  /home/vagrant/localperl/bin/perl /usr/share/man/man1/perl.1.gz
```


## alias
{id: alias}
{i: alias}

```
$ alias
alias cp='cp -i'
alias egrep='egrep --color=auto'
alias fgrep='fgrep --color=auto'
alias grep='grep --color=auto'
alias l='ls -CF'
alias la='ls -A'
alias ll='ls -alF'
alias ls='ls --color=auto'
alias mv='mv -i'
alias rm='rm -i'
```


## Creating alias in bash
{id: creating-alias-bash}
{i: alias}
{i: unalias}

```
alias rm='rm -i'
alias cp='cp -i'
alias ll='ls -lA'

unalias ll
```


## Creating alias in tcsh
{id: creating-alias-tcsh}
{i: alias}

```
alias rm 'rm -i'
alias cp 'cp -i'
alias ll 'ls -lA'

unalias ll
```


## Suppress alias
{id: suppress-alias}

```
alias rm='rm -fr'     # very dangerous!

'rm' thing
\rm  thing
```



## Alias only works in the shell it has been defined in
{id: alias-in-subshell}

{aside}

Aliases only work in the same shell where they were defined. Not even in a subshell
we get when we run a script. (But if we sourced the script then it runs in the same shell.)
{/aside}

```
$ alias tweet=echo
$ tweet hello
hello
```
![](examples/tweet.sh)

```
$ ./examples/tweet.sh 
./examples/tweet.sh: 2: ./examples/tweet.sh: tweet: not found
```


## Exercises: commands and aliases
{id: exercises-commands-and-aliases}

* List all the aliases in your shell
* Add an alias 'hw' that will print 'hello world' to the screen
* Check what is the 'hw' command?
* Remove the 'hw' alias.
* Check that it has been removed.


* Observe what 'ls' and 'ls -l' do and what would be the output of 'ls' if it was not already an alias.
* Create an alias 'll' to do what 'ls -l' does.




