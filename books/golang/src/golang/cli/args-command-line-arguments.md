# Args - (argv) command line arguments

* Args
* os.Args


os.Args is a slice of strings (we'll talk about slices in later in detail) that contains the values on the command line.

The first element of this slice (index 0) is the path to the executable. If we run this using `go run` then it
will be some strange-looking temporary location.

`len` gives us the number of elements on the command line that will be 1 if there are no parameters on the command line.

Using a square-bracket after the name `os.Args` allows us to access the specific elements in the slice.

Later we'll learn higher level abstractions to read command line parameters, but for now this will be enough.


{% embed include file="src/examples/cli/cli.go" %}

```
go run examples/cli/cli.go  hello world
```

{% embed include file="src/examples/cli/cli.out" %}

