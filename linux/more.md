# More
{id: more}

## Access modes
{id: access-modes}

* t - Sticky bit - Keep executable in memory after exit
* s - SUID - Set process user ID on execution
* s - SGID - Set process group ID on execution.




## Process CSV file
{id: process-csv-file}
{i: perl}
![](examples/process_csv_file.csv)

```
perl -n -a -F';' -E '$x += $F[2]; END { say $x }' examples/process_csv_file.csv
```


## Shell Pipe ideas
{id: shell-pipe-ideas}

```
sudo find /tmp/* -type d -cmin +30 -print0 | xargs -0 -I{} sudo ls -dl {} | wc -l
sudo find /tmp/* -type d -cmin +30 -print0 | xargs -0 -I{} sudo rm -rf {}

# The first commit of the README file:
git log README | grep ^commit | tail -1 | cut -d ' ' -f 2

Make a 1% sample of a large : separated accounting file
awk -F: 'rand() &lt; 0.01' accounting &gt; 1percent
```


## List and kill processes by username
{id: kill-the-processes-by-user}

List the PIDs of the given user.


```
$ ps aux | awk '$1=="gabor" {print $2}' 
```

```
$ ps aux | awk '$1=="gabor" {print $2}' | kill -9
```


## Compiling software: Perl
{id: compiling-software-perl}
{i: perl}
{i: make}
{i: gcc}

* [Perl Source](http://www.cpan.org/src/README.html)




## Exercise: compile
{id: exercise-compile}

Compile and install a new version of Python and/or Apache http server.






