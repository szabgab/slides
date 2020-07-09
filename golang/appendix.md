# Appendix
{id: appendix}


## Some advanced topics
{id: advanced-topics}

* closures
* pointers
* go-routines
* classes (there are no classes)
* interfaces
* Stringers - stringification
* many standard packages
* many external packages

## Resources
{id: resources}

* [Golang tour](https://tour.golang.org/welcome/1)
* [7-hours Video of freeCodeCamp](https://www.youtube.com/watch?v=YS4e4q9oBaU)
* [Video](https://youtu.be/YS4e4q9oBaU?t=6927)
* [Practical intro to Go](https://www.youtube.com/playlist?list=PLQVvvaa0QuDeF3hP0wQoSxpkqgRcgxMqX)
* [GoDoc](https://godoc.org/)
* [Concurrency in Go](https://www.youtube.com/watch?v=LvgVSSpwND8)
* [Golang REST API With Mux](https://www.youtube.com/watch?v=SonwZ6MF5BE)


## Caller filename
{id: caller-filename}
{i: caller}
{i: runtime}

![](examples/caller-filename/caller_filename.go)


## os.Executable
{id: os-executable}
{i: Eecutable}

![](examples/os-executable/os_executable.go)


## Solution: rectangular (STDIN) Reader
{id: solution-rectangular-stdin-reader}

![](examples/rectangular-stdin-reader/rectangular_stdin_reader.go)


## Scan int
{id: scan-int}

![](examples/scan-int/scan_int.go)

* Accepts an integer
* Accepts a single character (and gives 0) but the second character is left on the SDTIN buffer
* TODO: try also with int8 type

## Function assignment
{id: function-assignment}

![](examples/function-alias/function_alias.go)

## Overwriting built-in functions
{id: overwriting-built-in-functions}

![](examples/overwriting-builtin-functions/overwriting_builtin_functions.go)

* TODO: Why does Go allow for this without any complaint? 

## TODO: stack
{id: stack}

* see [lists](https://golang.org/pkg/container/list/)

## queue
{id: queue}
{i: PushBack}
{i: Front}
{i: Remove}

* see [lists](https://golang.org/pkg/container/list/)

![](examples/queue/queue.go)
![](examples/queue/queue.out)

## Left over
{id: left-over}

![](examples/bytes/bytes.go)


## Open Web browser
{id: open-web-browser}
{i: runtime}

![](examples/open-browser/open_browser.go)

## Unicode
{id: unicode}

![](examples/unicode/unicode.go)


## golang create io.reader from string
{id: create-io-reader-from-string}
{i: NewReader}
{i: Read}
{i: EOF}

{aside}
Many tools in Golang expect an io.reader object as an input parameter
What happens if you have a string and you'd like to pass that to such a function?
You need to create an io.reader object that can read from that string:
{/aside}

![](examples/create-io-reader/create_io_reader.go)
![](examples/create-io-reader/create_io_reader.out)

## Parse HTML Token by token
{id: parse-html-token-by-token}

* [HTML Parser](https://godoc.org/golang.org/x/net/html)

![](examples/parse-html-token/parse_html_token.go)
![](examples/parse-html-token/parse_html_token.out)

## Parse HTML extract tags and attributes
{id: parse-html-extract-tags-and-attributes}
{i: TagName}
{i: TagAttr}

![](examples/parse-html/parse_html.go)
![](examples/parse-html/parse_html.out)
