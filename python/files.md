# Files
{id: files}

## File types: Text vs Binary
{id: file-types-text-vs-binary}

{aside}
You probably know many file types such as Images (png, jpg, ...), Word, Excel, mp3, mp4, csv, and now also .py files. Internally there are two big categories.
Text and Binary files. Text files are the ones that look readable if you open them with a plain text editor such as Notepad. Binary files will
look like a mess if you opened them in Noetpad.

For Binary files you need a special application to "look" at their content. For example
the Excel and Word programs for the appropriate files. Some image viewer application to view all the images.
VLC to look at an mp4. Some application to hear the content of mp3 files.
{/aside}

* Text: .txt, csv, .py, .pl, ..., HTML , XML, YAML, JSON
* Binary: Images, Zip files, Word, Excel, .exe, mp3, mp4

{aside}
In Python you have specialized modules for each well-knonw binary type to handle the files of that format. Text files on the other
hand can be handled by low level file-reading functions, however even for those we usually have modules that know how to read
and interpret the specific formats. (e.g. CSV, HTML, XML, YAML, JSON parsers)
{/aside}

## Open vs. Read vs. Load
{id: open-vs-read}

{aside}
The expression "open a file" has two distinct meanings for programmers and users of software. For a user of Word, for example,
"open the file" would mean to be able to see its content in a formatted way inside the editor.

When a programmer - now acting as a regular user - opens a Python file in an editor such as Notepad++ or Pycharm,
the expectation is to see the content of that program with nice colors.

However in order to provide this the programmer behind these applications had to do several things.
{/aside}

* Connect to a file on the disk (aka. "opening the file" in programmer speak).
* Read the content of the file from the disk to memory.
* Format the content read from the file as expected by the user of that application.


## Binary files: Images
{id: binary-file-images}

{aside}
This is just a quick example how to use the Pillow module to handle images. There is a whole chapter on dealing with images.
{/aside}

* [Pillow](https://pillow.readthedocs.io/en/stable/)

![](examples/pil/get_image_size.py)

## Reading an Excel file
{id: binary-reading-an-excel-file}

{aside}
There are many ways to deal with Excel files as well.
{/aside}

* [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

![](examples/excel/read_any_excel.py)


## Open and read file (easy but not recommended)
{id: open-and-read}

{aside}
In some code you will encounter the following way of opening files.
This was used before "with" was added to the language.
It is not a recommended way of opening a file as you might easily forget
to call "close" and that might cause trouble. For example you might loose data.
Don't do that.

I am showing this as the first example, because it is easuer to understand.
{/aside}

![](examples/files/open_and_read.py)


## Open and read file using with (recommended)
{id: open-and-read-with}
{i: open}
{i: close}
{i: with}

![](examples/files/open_and_read_with.py)

## Read file remove newlines
{id: read-file-remove-newlines}
{i: trim}
{i: rstrip}
{i: chomp}

![](examples/files/read_file_remove_newlines.py)


## Filename on the command line
{id: filename-on-the-command-line}

![](examples/files/single.py)

```
$ python single.py
Usage: single.py FILENAME

$ python single.py numbers.txt
Working on the file numbers.txt
```

## Filehandle with return
{id: filehandle-with-return}

![](examples/files/with_returns.py)



## Read all the lines into a list
{id: read-all-the-lines}
{i: readlines}

{aside}
There are rare cases when you need the whole content of a file in the memory and you cannot process it line by line.
In those rare cases we have several options. `readlines` will read the whole content into a list converting each line
from the file to be an element in the list.

Beware though, if the file is too big, it might not fit in the free memory of the computer.
{/aside}

![](examples/files/read_full_file.py)
![](examples/files/read_full_file.out)


## Read all the characters into a string (slurp)
{id: slurp}
{i: read}

{aside}
In some other cases, especially if you are looknig for some pattern that starts on one line but ends on another line.
you'd be better off having the whole file as a single string in a variable. This is where the `read` method comes in handy.

It can also be used to read in chunks of the file.
{/aside}

![](examples/files/slurp.py)
![](examples/files/slurp.out)

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
![](examples/files/open_file_handle.out)


## Open many files - exception handling
{id: open-many-files-exception-handling}

![](examples/files/average_from_files.py)
![](examples/files/number_per_line.txt)
![](examples/files/empty.txt)

```
$ python average_from_files.py number_per_line.txt empty.txt number_per_line2.txt

Average:  58.25
trouble with 'empty.txt': Error: division by zero
Average:  3.5
```

```
$ python average_from_files.py numbers.txt

trouble with 'numbers.txt': Error: could not convert string to float: '23 345 12345\n'
```

```
$ python average_from_files.py more_numbers.txt

trouble with 'more_numbers.txt': Error: [Errno 2] No such file or directory: 'more_numbers.txt'
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
{i: rb}

![](examples/files/read_binary.py)


```
python examples/files/read_binary.py examples/pil/first.png

1000
1000
1000
1000
1000
775
0

```

## Does file exist? Is it a file?
{id: file-exists}
{i: os.path.exists}
{i: os.path.isfile}
{i: os.path.isdir}

* [os.path.exists](https://docs.python.org/library/os.path.html#os.path.exists)
* [os.path.isfile](https://docs.python.org/library/os.path.html#os.path.isfile)
* [os.path.isdir](https://docs.python.org/library/os.path.html#os.path.isdir)

## Direct access of a line in a file
{id: direct-access-of-a-line}


![](examples/files/access_list_element.py)
![](examples/files/access_list_element.out)

![](examples/files/fh_access.py)
![](examples/files/fh_access.err)

{aside}
This does NOT work because files can only be accessed sequentially.
{/aside}

![](examples/files/read_all_lines.py)

![](examples/files/count_lines.py)

## Exercise: count digits
{id: exercise-count-digits-in-file}

![](examples/files/numbers.txt)

1. Given the file **examples/files/numbers.txt** (or a similar file), create a file called **count_digits_in_file.py** that will count how many times each digit appears? The output will look like this. Just different values.
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


## Exercise: remove newlines
{id: exercise-remove-newlines}

* Create a file called **remove_newlines.py** that will be able to read all the lines of a given file into a list and remove trailing newlines.

## Exercise: print lines with Report:
{id: exercise-print-lines-with-report}


In many cases you get some text report in some free form of text (and not in a CSV file or an Excel file.) You need to extract the information
from such a file after recognizing the patterns. This exercise tries to provide such a case.

* Create a script called **text_report.py**

Given a file that looks like this:

![](examples/files/text_report.txt)

* Print out the first line that starts with `Report:`.
* Print out all the lines that have the string `Report:` in it.
* Print out all the lines that start with the string `Report:`.
* Print out the numbers that are after `Report:`. (e.g. `Report: 42` print out 42)
* Add the numbers that after after the string `Report:`. So in the above example the result is expected to be 204.

* Do the same, but only take account lines between the `Begin report` and `End report` section. (sum expected to be 58)


## Exercise: color selector
{id: exercise-file-color-selector}

* Create a file similar to the colors.txt file and use it as the list of colors in the earlier example where we prompted for a color.
* Call the new script **color_selector_file.py**

![](examples/files/colors.txt)

Extend the previous example by letting the user provide the name of the file on the command line:
`python color.py examples/files/color.txt`


## Exercise: ROT13
{id: exercise-rot13-files}
{i: rot13}

* Implement [ROT13](https://en.wikipedia.org/wiki/ROT13):
* Create a script called **rot13_file.py** that given a file on the command line it will replace the content with the rot13 of it of it.


## Exercise: Combine lists
{id: exercise-combine-lists}

![](examples/files/a.txt)
![](examples/files/b.txt)

Write a script called **combine_lists.py** that takes the two files and combines them adding the values for each vegetable. The expected result is:

![](examples/files/c.txt)

## Exercise: Number guessing game - save to file
{id: exercise-number-guessing-game-save-to-file}

Level 7

* Create a file called **number_guessing_game_7.py**
* Based on the previous solutions.
* When starting a new game ask the user for their name and save the game information in the file.
* The hidden number and the guesses.
* Have an option to show the previously played games.


## Solution: count numbers
{id: solution-count-numbers}

![](examples/files/count_numbers.py)


## Solution: remove newlines
{id: solution-remove-newlines}

![](examples/files/remove_newlines.py)

## Solution: print lines with Report:
{id: solution-print-lines-with-report}

![](examples/files/text_report.py)


## Solution: color selector
{id: solution-file-color-selector}

![](examples/files/colors.py)

## Solution: ROT13
{id: solution-rot13-files}
{i: rot13}

![](examples/files/rot13_file.py)



## Solution: Combine lists
{id: solution-combine-lists}

![](examples/files/combine_lists.py)


## Solution: Combine lists with tuple
{id: solution-combine-lists-with-tuple}
{i: zip}
{i: tuple}

![](examples/files/combine_lists_tuple.py)


## Filehandle using with and not using it
{id: filehandle-with-and-without}
{i: open}
{i: close}
{i: with}

![](examples/files/open_with.py)



