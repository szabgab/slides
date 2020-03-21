# Files
{id: python-files}

## Open and read file
{id: open-and-read-with}
{i: open}
{i: close}
{i: with}

![](examples/files/open_and_read_with.py)


## Filename on the command line
{id: filename-on-the-command-line}

![](examples/files/single.py)

```
$ python single.py
Usage: single.py FILENAME

$ python single.py numbers.txt
Working on the file numbers.txt
```


## Filehandle with and without
{id: filehandle-with-and-without}
{i: open}
{i: close}
{i: with}
![](examples/files/open_with.py)


## Filehandle with return
{id: filehandle-with-return}
![](examples/files/with_returns.py)


## Read file remove newlines
{id: read-file-remove-newlines}
{i: trim}
{i: rstrip}
{i: chomp}
![](examples/files/read_file_remove_newlines.py)


## Read all the lines into a list
{id: read-all-the-lines}
{i: readlines}
![](examples/files/read_full_file.py)


## Read all the characters into a string (slurp)
{id: slurp}
{i: read}
![](examples/files/slurp.py)

{aside}

read(20) will read 20 bytes.
{/aside}


## Not existing file
{id: not-existing-file}
{i: IOError}
![](examples/files/open_file.py)


## Open file exception handling
{id: open-file-exception-handling}
{i: try}
{i: except}

Exception handling

![](examples/files/open_file_handle.py)


## Open many files - exception handling
{id: open-many-files-exception-handling}
![](examples/files/average_from_files.py)
![](examples/files/number_per_line.txt)
![](examples/files/empty.txt)

```
python average_from_files.pyt number_per_line.txt empty.txt number_per_line2.txt
```

```
Average:  58.25
trouble with empty.txt
Average:  3.5
```


## Writing to file
{id: writing-to-file}
{i: open}
{i: write}
![](examples/files/write.py)


## Append to file
{id: append-to-file}
{i: append}
![](examples/files/append.py)



## Binary mode
{id: binary-mode}
![](examples/files/read_binary.py)


## Does file exist? Is it a file?
{id: file-exists}
{i: os.path.exists}
{i: os.path.isfile}
{i: os.path.isdir}

* [os.path.exists](https://docs.python.org/library/os.path.html#os.path.exists)
* [os.path.isfile](https://docs.python.org/library/os.path.html#os.path.isfile)
* [os.path.isdir](https://docs.python.org/library/os.path.html#os.path.isdir)


## Exercise: count numbers
{id: exercise-count-numbers}
![](examples/files/numbers.txt)

1. Given the file **examples/files/numbers.txt** (or a similar file), count how many times each digit appears? The output will look like this. Just different values.
1. Save the results in a file called **report.txt**.


```
0 0
1 3
2 3
3 4
4 2
5 2
6 1
7 2
8 1
9 1
```


## Exercise: strip newlines
{id: exercise-strip-newlines}


How to read all the lines of a file into a list
and remove trailing newlines?





## Exercise: color selector
{id: exercise-file-color-selector}

Create a file similar to the colors.txt file
and use it as the list of colors in the earlier example where we prompted for a color.


![](examples/files/colors.txt)

Extend the previous example by letting the user provide the name of the file on the command line:
`python color.py examples/files/color.txt`


## Exercise: ROT13
{id: exercise-rot13}

Implement [ROT13](https://en.wikipedia.org/wiki/ROT13):
* Create a function that given a string return the rot13 of it.
* Create a script that given a file it will replace with the rot13 of it.

How to check if it works properly:

```
txt = "any text"
encrypted = rot13(txt)
decrypted = rot13(encrypted)
assert decrypted == text
```


## Exercise: Combine lists
{id: exercise-combine-lists}

![](examples/files/a.txt)
![](examples/files/b.txt)

Write a script that takes the two files and combines them adding the values for each vegetable. The expected result is:

![](examples/files/c.txt)


## Solution: count numbers
{id: solution-count-numbers}

![](examples/files/count_numbers.py)


## Solution: strip newlines
{id: solution-strip-newlines}

![](examples/files/strip_newlines.py)


## Solution: color selector
{id: solution-file-color-selector}

![](examples/files/colors.py)


## Solution: Combine lists
{id: solution-combine-lists}

![](examples/files/combine_lists.py)


## Read text file
{id: read-file}

![](examples/files/read_file.py)


## Open and read file
{id: open-and-read}

{aside}
In some code you will encounter the following way of opening files.
This was used before "with" was added to the language.
It is not a recommended way of opening a file as you might easily forget
to call "close" and that might cause trouble. For example you might loose data.
Don't do that.
{/aside}

![](examples/files/open_and_read.py)


## Direct access of a line in a file
{id: direct-access-of-a-line}

![](examples/files/fh_access.py)
![](examples/files/fh_access.err)

{aside}
This does NOT work because files can only be accessed sequentially.
{/aside}

## Example
{id: example-with-files}


![](examples/files/sample.txt)
![](examples/files/example.py)

