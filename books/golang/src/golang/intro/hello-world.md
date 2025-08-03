# Hello World

* package
* main
* import
* func
* run
* build
* fmt

{% embed include file="src/examples/hello-go/hello_world.go" %}

```
go run hello_world.go
```

{% embed include file="src/examples/hello-go/hello_world.out" %}

* main function is the entry point of every program
* [fmt.Print](https://golang.org/pkg/fmt/#Print)


Every Go program has a main file that must start with "package main" and it must have a function called `main`.

In order to print something to the screen we first need to import the `fmt` class and then inside the "main" function we can write
`fmt.Println("Hello World")`.

We save this with a .go extension. Then we can run it from the command line by typing `go run` and the name of your file.
This will compile the code into a temporary directory and then run it.



