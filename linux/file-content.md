# File content
{id: file-content}

## Text editors
{id: text-editors}
{i: vim}
{i: emacs}
{i: gedit}
{i: pico}
{i: nano}

* vim
* emacs
* gedit - notepad like editor on the desktop
* pico - notepad like editor on the command line
* nano - 



## nano - a small editor
{id: nano}

```
nano file.txt
```


## Displaying file content
{id: displaying-file-content}
{i: cat}
{i: more}
{i: less}
{i: head}
{i: tail}

* **cat**  - show the content of the whole file.
* **more**- an old pager (not really used any more).
* **less**- a new pager (h for help; q for quit).
* **head**- show first 10 lines of a file.
* **head -42** - show first 42 lines of a file.
* **tail**  - show last 10 lines.
* **tail -42** - show last 42 lines.
* **tail -f** - follow as the file growth.



## cut
{id: cut}
{i: cut}

{aside}

Extract fields or charcters from strings.
{/aside}

```
cut -c 3,2,10    files (characters)
cut -f 1,3       files (fields separated by tab)
cut -f 1,3 -d' ' files (fields separated by space)
cut -f 1,3 -d':' files (fields separated by :)

cut -b   files   (bytes)
```

* -c N      charcter
* -f N      field
* -d ':'    delimeter (defaults to TAB)


```
$ who
foo      console  Apr  8 18:57
bar      ttys000  Apr  9 07:42
moose    ttys001  Apr  8 18:57
```


```
$ who | cut -f1 -d' '
foo
bar
moose
```


## sort
{id: sort}
{i: sort}

![](examples/intro/sort.txt)

{aside}

-k -select field to use for sorting
-n -numerical sorting
{/aside}


## uniq
{id: uniq}
{i: uniq}

{aside}

Despite its name, **uniq** will not necessarly provide a unique list of values.
It will collapse the adjacent equal values.
If all the equal values are adjacent then it will really create a unique list.
Sorting will reorder the original list so that the equal values will be next to each other.
{/aside}

![](examples/intro/uniq.txt)


## Finding text in a file
{id: grep}
{i: grep}
{i: egrep}
{i: ack-grep}

* grep regex FILEs
* egrep regex FILEs
* ack-grep


```
-v lines that did not match
-i ignore case
-n show line numbers
-r look into the files recursively

-w match exact words only
-l print names of the files matched
-c count of lines matched

-B n   show n lines before the match.
-A n   show n lines after the match.
-C n   show n lines both before and after the match (up to 2*n+1 lines) (context).
```

![](examples/intro/grep.txt)


## word count with wc
{id: word-count}
{i: passwd}

```
$ wc README
     220     516    3270 README
$ wc *.xml
     750    2020   19797 intro.xml
     593    1568   14953 scripts.xml
     145     366    3338 variables.xml
    1488    3954   38088 total

$ wc -l README 
     220 README
$ wc -w README 
     516 README
$ wc -c README 
    3270 README
```

{aside}
Counting lines, words, characters
{/aside}



## tr - transcribe
{id: tr}
{i: tr}

![](examples/intro/tr.txt)


## sed - the stream editor
{id: sed}
{i: sed}

```
sed 's/old/new/' &lt; ORIGINAL_FILE &gt; NEW_FILE
sed 's/old/new/' ORIGINAL_FILE &gt; NEW_FILE
cat ORIGINAL_FILE | sed 's/old/new/' &gt; NEW_FILE

s/REGEX/STRING/
s:REGEX:STRING:

s/c./(&amp;)/     &amp; represent the whole match

echo fool | sed -r 's/(.)/(&amp;)/'           (f)ool
echo fool | sed -r 's/(.)\1/(&amp;)/'         f(oo)l
echo fool | sed -r 's/(.)\1/(double \1)/'     f(double o)l
```

[Sed tutorial](http://www.grymoire.com/Unix/Sed.html)



## Compression and archiving
{id: compression-and-archiving}
{i: tar}
{i: gzip}
{i: gunzip}
{i: zip}
{i: unzip}
{i: bzip2}
{i: bunzip2}
{i: zcat}
{i: zgrep}
{i: xz}

* tar
* zip unzip
* gzip gunzip zcat zgrep
* bzip2 bunzip2 bzcat bzgrep
* xz unxz xzcat xzgrep


```
tar xzf file.tar.gz
tar czf file.tar.gz  dir/
```


## Generate random output
{id: generate-random-output}
{i: $RANDOM}

{aside}

A Bash script that will generate a random number.
If it is bigger that 10 then print the number.
{/aside}

![](examples/linux/generate_random_output.sh)


## Generate random log
{id: generate-random-log}

{aside}

Change the script to print one of these every tenth of a second.
{/aside}
![](examples/linux/generate_random_log.sh)

```
$ ./generate_random_log.sh

Pressing Ctrl-C will stop the execution.
```


## Exercise: log file
{id: exercise-log-file}

* Run the script in a way that only the lines with "Error" in them will show.
* Then run the script and redirect the output to a file.
* Run it in the background.
* Display the content of the log-file as it is growing.
* Now display only the lines with the word "Error"




## Exercise: File content
{id: exercise-file-content}

1. grep through  /etc/password showing the line of your username
1. Then show the shell of every user in the system.
1. Count how many times each shell is used.
1. Count how many users are in the system.
1. Archive the content of your home directory in a tar.gz and then also ina tar.bz2 file.
1. How do they compare in size to each other and to the real content of your home directory?
1. Find your name in the zipped file without opening it to the disk.
1. Open the whole directory tree in /tmp.
1. Remove a file from that new tree and compare it to original directory tree.



## Exercise: File content round 2
{id: exercise-file-content2}


Use the following script to create a subdirectory called 'file_conent' and in it a file
called 'data.txt'. Once we have the file, replace the numbers with their duplication so 1 will become 11.


![](examples/linux/file_content.sh)



