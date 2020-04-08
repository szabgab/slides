# Strings
{id: strings}


## Single and double quotes
{id: single-and-double-quotes}

* Double quote is for strings - a series of bytes (uint8)
* Single quote is for runes (alias for int32 signed integer) - a character value


## Runes
{id: runes}
{i: rune}
{i: int32}

* alias for int32

![](examples/rune/rune.go)
![](examples/rune/rune.out)

## Strings
{id: strings-intro}

![](examples/strings/strings.go)
![](examples/strings/strings.out)

## Strings and Runes
{id: strings-and-runes}

![](examples/string-rune/string_rune.go)
![](examples/string-rune/string_rune.out)


## Length of string
{id: length-of-string}
{i: len}

![](examples/string-length/string_length.go)

## iterate over characters in a string
{id: for-loop-string}
{i: range}

![](examples/loop-string/loop_string.go)

## String Contains, HasPrefix, HasSuffix
{id: string-contains}
{i: Contains}
{i: HasPrefix}
{i: HasSuffix}


![](examples/suffix-prefix/suffix_prefix.go)



## Sort
{id: sort}
{i: sort}

![](examples/sort/sort.go)


## Split and join
{id: split}

![](examples/split/split.go)


## Split on whitespaces
{id: split-on-whitespaces}


![](examples/split-on-whitespace/split_on_whitespace.go)

```
'  hello    space   world 42 '
[hello space world 42]
4
```

* [strings.Fields](https://golang.org/pkg/strings/#Fields)


## Read line from stdin (keyboard)
{id: read-line-from-stdin}

Read from the stdin (standard input) Get input from the keyboard in golang

![](examples/read-from-stdin/read_from_stdin.go)

## Read line from stdin (keyboard) with error handling
{id: read-line-from-stdin-with-error-handling}

![](examples/read-from-stdin-with-error-handling/read_from_stdin_with_error_handling.go)


## Exercise: how long is this string?
{id: exercise-how-long-is-this-string}

* The code will ask the user to type in a string and will print out the length of the string

## Exercise: which string is longer?
{id: exercise-which-string-is-longer}

* The code will prompt the user for two strings and then print out which string is longer


## Solution: how long is this string?
{id: solution-how-long-is-this-string}




## Solution: which string is longer?
{id: solution-which-string-is-longer}
{i: len}

![](examples/which-string-is-longer/which_string_is_longer.go)
