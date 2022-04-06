# Strings
{id: strings}


## Single quoted and double quoted strings
{id: single-quote-double-quote}

{aside}
In Python, just as in most of the programming languages you must put any free text inside a pair of quote characters.
Otherwise Python will try to find meaning in the text.

These pieces of texts are called "strings".

In Python you can put string between two single quotes: '' or between two double quotes: "". Which one, does not matter.
{/aside}

![](examples/strings/quotes.py)
![](examples/strings/quotes.out)

## Long lines
{id: long-lines}

![](examples/strings/other.py)
![](examples/strings/other.out)


## Multiline strings
{id: multiline-strings}

* We would like to print the number one under the other

![](examples/strings/multiline_string.py)
![](examples/strings/multiline_string.out)


## Triple quoted strings (multiline)
{id: triple-quoted-strings}
{i: """}
{i: '''}

{aside}
If you would like to create a string that spreads on multiple lines,
there is a possibility to put the text between 3 quotes on both sides. Either 2*3 single-quotes
or 2*3 double-quotes.
{/aside}

![](examples/strings/triple_quotes.py)
![](examples/strings/triple_quotes.org)

Can spread multiple lines.

```
first row
second row
third row
```

## Triple quoted comments - documentation
{id: triple-quoted-comments}

![](examples/strings/triple_comments.py)

## String length (len)
{id: string-length}
{i: len}

{aside}
The `len` function returns the length of the string in number of characters.
{/aside}

![](examples/strings/length.py)


## String repetition and concatenation
{id: string-repetition}
{i: *}
{i: +}

{aside}
You might be used to the fact that you can only multiply numbers, but in python you can also "multiply" a string by a number.
It is called repetition. In this example we have a string "Jar " that we repeat twice.

We can also add two strings to concatenate them together.

I don't think the repetition operator is used very often, but in one case it could come in very handy.
When you are writing some text report and you'd like to add a long line of dashes that would be exactly the same length
as your title.
{/aside}

![](examples/strings/repetition.py)

## A character in a string
{id: character--in-string}
{i: []}

![](examples/strings/string_char.py)


## String slice (instead of substr)
{id: string-slice}
{i: slice}
{i: substr}
{i: [:]}
{i: :}

![](examples/strings/string_slice.py)


## Change a string
{id: string-change}
{i: immutable}

{aside}
In Python strings are "immutable", meaning you cannot change them. You can replace a whole string in a variable,
but you cannot change it.

In the following example we wanted to replace the 3rd character (index 2), and put "Y" in place. This raised an exception
{/aside}

![](examples/strings/string_change.py)

![](examples/strings/string_change.out)

{aside}
Replace part of a string
{/aside}


* Strings in Python are **immutable** - they never change.


## How to change a string
{id: how-to-change-a-string}

![](examples/strings/change_a_string.py)


## String copy
{id: string-copy}

![](examples/strings/string_copy.py)

{aside}
When assigning a variable pointing to a string, the new variable is pointing to the same string..
If we then assign some other string to either of the variables, then they will point to two different strings.
{/aside}


## String functions and methods (len, upper, lower)
{id: string-functions}
{i: len}
{i: upper}
{i: lower}

![](examples/strings/functions.py)

* Type **dir("")** in the REPL to get the list of string methods.
* List of [built-in functions](https://docs.python.org/library/functions.html).
* List of [string methods](https://docs.python.org/library/stdtypes.html#string-methods).


## index in string
{id: index-in-string}
{i: index}
{i: ValueError}

![](examples/strings/index.py)
![](examples/strings/index.out)


## index in string with range
{id: index-in-string-range}
{i: index}

![](examples/strings/index2.py)
![](examples/strings/index2.out)


## rindex in string with range
{id: rindex-in-string-range}
{i: rindex}

![](examples/strings/rindex.py)
![](examples/strings/rindex.out)


## find in string
{id: find-in-string}
{i: find}
{i: rfind}

Alternatively use find and rfind that will return -1 instead of raising an exception.

![](examples/strings/find.py)


## Find all in the string
{id: find-all-in-the-string}

Later, when we learned loops.


## in string
{id: in-syntax-on-string}
{i: in}

Check if a substring is **in** the string?

![](examples/strings/in.py)
![](examples/strings/in.out)


## index if in string
{id: location-if-in-string}
{i: index}
{i: in}

![](examples/strings/location_if_in.py)


## Encodings: ASCII, Windows-1255, Unicode
{id: ascii-unicode}

* [ASCII](https://en.wikipedia.org/wiki/ASCII)
* [Hebrew Character](https://en.wikipedia.org/wiki/Hebrew_character)
* [Windows-1255](https://en.wikipedia.org/wiki/Windows-1255)
* [Unicode (UTF-8)](https://en.wikipedia.org/wiki/Unicode)



## raw strings
{id: raw-strings}
{i: r}

![](examples/strings/raw.py)

Escape sequences are kept intact and not escaped. Used in regexes.

## ord
{id: ord}
{i: ord}

* [ord](https://docs.python.org/library/functions.html#ord)

![](examples/strings/ord_chars.py)


## chr - number to character
{id: chr}
{i: chr}

* [chr](https://docs.python.org/library/functions.html#chr)

![](examples/strings/chr.py)

## Exercise: one string in another string
{id: exercise-one-string-in-another-string}

* Write script called **string_in_another_string.py** that accepts two strings and tells if one of them can be found in the other and where?


## Exercise: Character to ASCII - CLI
{id: exercise-to-ascii-cli}

Write script called **char_to_ascii.py** that gets a character on the command line and prints out the ascii code of it.

Maybe even:

Write script that gets a string on the command line and prints out the ascii code of each character.


## Exercise: from ASCII to character - CLI
{id: exercise-from-ascii-cli}

Write script called **ascii_to_char.py** that accepts a number on the command line and prints the character represented by that number.

## Exercise: ROT13
{id: exercise-rot13}
{i: rot13}

* Implement [ROT13](https://en.wikipedia.org/wiki/ROT13):
* Create a script called **rot13.py** that given a string on the command line will print the ROT13 version of the string.
* It should work like this:

```
$ python rot13.py "Hello world!"
Uryyb Jbeyq!

$ python rot13.py "Uryyb Jbeyq!"
Hello world!
```

## Solution: one string in another string
{id: solution-one-string-in-another-string}

![](examples/strings/in_string.py)

## Solution: compare strings
{id: solution-compare-string}

![](examples/strings/compare_strings.py)

## Solution: to ASCII CLI
{id: solution-to-ascii-cli}


![](examples/strings/to_ascii_char.py)
![](examples/strings/to_ascii.py)

## Solution: from ASCII CLI
{id: solution-from-ascii-cli}

![](examples/strings/from_ascii.py)

## Solution: Show characters based on Unicode code-points
{id: solution-show-characters-based-on-code-points}

![](examples/strings/show_chars.py)

## Solution: ROT13
{id: solution-rot13}
{i: rot13}
{i: codecs}
{i: encoding}

![](examples/strings/rot13.py)

Of course instead of implementing all the calculations by yourself you can also rely on a module that comes with Python:

* [codecs library](https://docs.python.org/library/codecs.html)

![](examples/strings/rot13_codecs.py)

