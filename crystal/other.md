# Other
{id: other}

## Single quotes vs double quotes 
{id: single-quotes-vs-double-quotes}

* Single quotes are for characters
* Double quotes are for strings


## No type-checking?
{id: no-typechecking}

```
x = "one"
x = 1
p! x
p! typeof(x)
```

## JSON (to_json, parse)
{id: json}
{i: json}
{i: to_json}
{i: parse}

* Round trip with JSON
* Have to `require "json"` for the method to be added.

![](examples/json.cr)

## HTTP Client
{id: http-client}

![](examples/http_client.cr)


## Divide by zero is Infinity
{id: divide-by-zero-is-infinity}
{i: Infinity}

![](examples/divide_by_zero.cr)

## Catch exception - begin, rescue
{id: catch-exception}
{i: begin}
{i: rescue}

![](examples/catch_exception.cr)

## Raise exception
{id: raise-exception}

![](examples/raise_exception.cr)

## Require other files
{id: require-other-files}

* [requiring files](https://crystal-lang.org/reference/syntax_and_semantics/requiring_files.html)

![](examples/one/welcome.cr)
![](examples/one/use_welcome.cr)

## List Methods
{id: list-methods}

![](examples/methods.cr)
![](examples/methods.out)


## Checking the slides
{id: checking-the-slides}

![](examples/check_slides.cr)

## Crystal mine
{id: crystal-mine}

![](examples/mine.cr)

## Ameba Linter
{id: ameba-linter}


* [Ameba](https://github.com/crystal-ameba/ameba)

![](.ameba.yml)

```
shards install
./bin/ameba
```
