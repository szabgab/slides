# Appendix
{id: appendix}


## Some advanced topics
{id: advanced-topics}

* closures
* pointers
* go-routines
* classes (there are no classes)
* methods (attached to types), but no classes
* interfaces
* Stringers - stringification
* Cross compilation
* many standard packages
* many external packages

## Resources
{id: resources}

* [Golang tour](https://tour.golang.org/welcome/1)
* [7-hours Video of freeCodeCamp](https://www.youtube.com/watch?v=YS4e4q9oBaU)
* [Video](https://youtu.be/YS4e4q9oBaU?t=6927)




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

## TODO: queue
{id: queue}

* see [lists](https://golang.org/pkg/container/list/)

## Find executable (which where)
{id: find-executable}
{i: which}
{i: where}
{i: exec}
{i: LookPath}

* Unix: `which`
* Windows: `where`
* Go:

![](examples/find-executable/find_executable.go)
![](examples/find-executable/find_executable.out)

## Run external programs
{id: run-external-programs}

![](examples/run-external/run_external.go)

