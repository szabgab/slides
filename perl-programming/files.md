# Files
{id: files}

## die, warn, exit
{id: exit-warn-die}
{i: die}
{i: warn}
{i: exit}
{i: STDERR}

**exit()** -                      exits from the program


**warn()** - writes to STDERR


**die()**  - writes to STDERR and exits from the program (raising exception)



```
warn "This is a warning";
```

```
This is a warning at script.pl line 132.

If no \n at the end of the string both warn and die add the
name of file and line number and possibly the chunk of the input.
```


## while loop
{id: while-loop}


Another tool to create a loop is by using `while`.



```
while (EXPRESSION) { BLOCK }
```

```
my $i = 100;
while ($i > 0) {
    # do something
    $i--;
}
```

```
while (1) {
    # a nice infinite loop
}
```


## Loop controls: next, last
{id: next-last-loop-controls}
{i: next}
{i: last}

* **next** - evaluate the loop condition and if it is true go to the next iteration. (**continue** in other languages)
* **last** - exit the loop. (**break** in other languages)
* **redo** - start the iteration again without evaluating the loop condition.


![](examples/perlarrays/loop_control.txt)

![](examples/files/loop_control.pl)


```
'First line'
'Line after empty line'
'Another text line'
Number of non empty rows: 3 out of a total of 6
```



## Opening file for reading
{id: open-file-for-reading}
{i: open}

```
While working over most of the operating systems today, no program can
access a file directly. This is in order to allow the Operating System
to apply user rights.

Before you can read from a file you have to ask the Operating System to "open"
it for you. When opening a file you provide a variable that will become your
handle to the opened file. It is called a filehandle.
```
![](examples/files/open_file.pl)


[Open and read from text files](https://perlmaven.com/open-and-read-from-files)


## Opening a file
{id: open-file}
{i: append}
{i: write}

![](examples/files/open_file_modes.pl)

[Appending to files](https://perlmaven.com/appending-to-files)


## Opening a file - error handling
{id: open-file-error-handling}
{i: $!}

* $! - error message from the Operating system

![](examples/files/open_with_if.pl)


A more Perlish way to open a file and exit with error message if you could not open the file:


![](examples/files/open_with_die.pl)


## Opening a missing file
{id: open-file-error-message}
![](examples/files/open_missing_file.pl)


The error message we get:



**No such file or directory at examples/files/open_missing_file.pl line 7.**



## Read one line from a file
{id: read-line}
![](examples/files/read_line.pl)




## Process an entire file line by line (while, cat)
{id: cat}
{i: while}

* while - executes as long as there is something in $line, as long as there are lines in the file
* Loop over file (name hard-coded) and print every line (UNIX cat)

![](examples/files/cat.pl)

```
Instead of printing the line you could do anything with it.
```


## Write to a file
{id: write-file}

![](examples/files/write_file.pl)


[Writing to files with Perl](https://perlmaven.com/writing-to-files-with-perl)


## Sum of numbers in a file
{id: sum-of-numbers}

![](examples/files/numbers.txt)
![](examples/files/count_sum.pl)


## Analyze the Apache log file
{id: apache-log-report-hosts}

![](examples/files/apache_access.log)
![](examples/files/apache_log_hosts.pl)


## Encoding and UTF-8
{id: encoding}
![](examples/files/encoding.pl)


## Open files in the old way
{id: old-open}


In old version of perl (before 5.6) we could not use scalar variables as file
handles so we used uppercase letters such as XYZ or INPUT, QQRQ or FILEHANDLE.




Also the function had only 2 parameters.


![](examples/files/open_file_old.pl)

Security problems.

Being global, difficult to pass as parameter to functions.

[Don't Open Files in the old way](https://perlmaven.com/open-files-in-the-old-way)


## Binary mode
{id: binary-mode}

![](examples/files/open_binary_file.pl)


## Reading from file, read, eof
{id: reading-from-file-read-eof}
{i: read}
{i: eof}


In Perl we usually care about lines of input so the above is enough.
Still some like to read files with chunks of arbitrary length.
read puts the read string to the variable passed to the function and
returns the number of characters actually read
READ_LENGTH = read FILEHANDLE,SCALAR,LENGTH


![](examples/files/read_file.pl)

```
# returns TRUE if we are at the end of file.
eof($in)
```

[EOF - End of file in Perl](https://perlmaven.com/end-of-file-in-perl)


## tell, seek
{id: tell-seek}
{i: tell}
{i: seek}


For our purposes a file is a line of characters.
After a bunch of read and/or write operations we need to tell where are we on that line ?


```
LOCATION = tell FILEHANDLE
```

We might also want to move within that file



```
 seek FILEHANDLE, OFFSET, WHENCE
 
 WHENCE:
     0 from beginning of file
     1 from current location
     2 from end of file
 OFFSET: 
     +/- number of bytes to move
```


the important values are:



```
seek $fh, 0,0;    # go to the beginning of the file
seek $fh, 0,2;    # go to the end of the file
```


## truncate
{id: truncate}
{i: truncate}

```
# Sometimes you need to 
truncate FILEHANDLE, LENGTH;
```
![](examples/files/truncate.pl)



## Exercise: Add more statistics
{id: exercise-more-statistics}


Take the script from the previous example (examples/files/count_sum.pl)
and in addition to the sum of the numbers print also



```
minimum
maximum
average
```


median and standard deviation are probably too difficult for now.




## Exercise: Write report to file
{id: exercise-write-report-to-file}


Take the exercise creating statistics of the numbers.txt file and 
write the results to the numbers.out file.



```
minimum: -17
maximum:  98
total:   126
count:     6
average:  21
```


You might need to look up the documentation of the printf command
in order to align the columns.




## Exercise: Analyze Apache - number of successful hits
{id: exercise-analyze-apache-log}


In the Apache log file (examples/files/apache_access.log)
after the "GET something HTTP/1.1" part there is the
result code of the requests. 200 is OK the rest might be some failure.




Please create a report showing how many of the hits were successful (200)
and how many were something else.




Could you put all the lines in either of the categories?




## Solution: Add more statistics
{id: solution-statistics}
![](examples/files/statistics.pl)


## Solution: Write report to file
{id: solution-write-report-to-file}
![](examples/files/write_report_to_file.pl)


## Solution: Analyze Apache - number of successful hits
{id: solution-analyze-apache-log}
![](examples/files/apache_log_result_code.pl)




