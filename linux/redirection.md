# Redirection and Pipes
{id: redirection}

## Open Channels
{id: open-channels}

* STDIN   (keyboard) 0
* STDOUT  (screen) 1
* STDERR  (screen) 2



## Redirection
{id: redirection-in-general}
{i: &gt;}
{i: &gt;&gt;}
{i: &lt;}
{i: 2&gt;}
{i: 2&gt;&amp;1}
![](examples/intro/redirection.txt)


## Redirection bash
{id: redirection-bash}
![](examples/intro/redirection_bash.txt)


## Redirection bash append
{id: redirection-bash-append}
![](examples/intro/redirection_bash_append.txt)


## Redirection bash merge
{id: redirection-bash-merge}
![](examples/intro/redirection_bash_merge.txt)


## Redirection tcsh
{id: redirection-tcsh}
![](examples/intro/redirection_tcsh.txt)

{aside}

tcsh cannot directly redirect stderr but we can use a subshell with the parentheses.
{/aside}


## Redirect to /dev/null
{id: dev-null}
{i: /dev/null}
![](examples/intro/redirect_to_dev_null.txt)


## Pipes
{id: pipes}
{i: |}
![](examples/intro/pipes.txt)


## Filters
{id: filters}

A filter is a command that can either act on a filename it sees on the command line or on the stream on STDIN.


```
$ filter INPUT_FILE
$ filter &lt; INPUT_FILE
$ cat INPUT_FILE | filter
```

* grep
* cut
* uniq
* sort
* ...
* sed
* awk
* perl



## tee
{id: tee}
{i: tee}

{aside}

Both redirects the output to a file and let's it through to the screen or to a pipe.
**tee -a** would append to the file.
{/aside}
![](examples/intro/tee.txt)


## Exercises: redirection
{id: exercises-redirection}

* How many files are in the current directory?
* How many files are in the current directory tree?
* Given the Apache log file in examples/apache_access.log
* How many hits came from 127.0.0.1 ?
* How many hits came from other than 127.0.0.1 ?



## Exercise: HTML content
{id: exercise-conten}

* Find a package that can strip the html tags from an html file and install it.
* If you found the HTML::Strip perl module, then the script bellow will do the work using that module.
* Save the home page of IMDB, strip the html and then count how many numbers are in the file.

![](examples/htmlstrip.pl)





