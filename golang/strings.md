# Strings
{id: strings}


## Single and double quotes
{id: single-and-double-quotes}

* Double quote is for strings - a series of bytes (uint8)
* Single quote is for runes (alias for int32 signed integer) - a character value


## Runes
{id: runes}

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


