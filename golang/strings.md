# Strings
{id: strings}

## Single and double quotes
{id: single-and-double-quotes}

* Double quote is for strings
* Single quote is for Runes

## Runes
{id: runes}

```
rune - any utf-32 character
r := 'a'   // single quotes!
they are actually int32
var r rune = 'a'
```


## Sort
{id: sort}
{i: sort}

![](examples/sort/sort.go)


## Split and join
{id: split}

![](examples/split/split.go)


## Split on whitespaces
{id: split-on-whitespaces}


![](examples/split-on-whitespace/split-ws.go)

```
'  hello    space   world 42 '
[hello space world 42]
4
```

* [strings.Fields](https://golang.org/pkg/strings/#Fields)

