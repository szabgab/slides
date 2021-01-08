# Introduction to Golang
{id: intro}

## Features
{id: features}

{aside}
I don't plan to give you an "elevator pitch" as to why you would want to use Go, but here are a few items that might help you if you need to justify
the time you spend on it.

In general there are many attributes to every programming language and each language is located somewhere else in relation to those different attributes.

I think there are two central areas where Go has advantages over other languages. One of them is the built-in concurrency that makes it easier to use all the cores that you can find in a modern computer. The other is the cross compilation. Meaning it is easy to write your code on one computer and compile your code
on that computer targeting other operating systems.

If we are already talking about compilation, it is also much faster than that of C or other compiled languages while its run-time is as fast as those other compiled languages. The fast compile time might not sound as a big deal, but if your compilation takes 10 seconds instead of 5 minutes or two hours, your feedback loop is much faster and thus you can develop faster.

Another advantage that Go has is that it manages the memory for you so unlike in C you don't have to deal with memory management. On the other hand by giving up on some of the (usually unnecessary) flexibility of Python it is also not as wasteful with memory allocation.

It provides you control over the types of the variables, but in many cases it does not force you to be precise.
{/aside}

* Built-in concurrency
* Compile to standalone binaries (cross compilation available!)

* Strong and statically typed
* Simplicity
* Fast compile times
* Garbage collected

## Why Golang?
{id: why-golang}

{aside}
The following 2 articles predate the development of Go, but they can illustrate well one of the big challenges of the software development world to which Go provides a good solution.

Comments from companies using it:
Golang is faster and allows easy parallel implementation. Besides, services like swan, bee, rabbit-MQ, etc.
{/aside}


* Concurrency [The Free Lunch Is Over: A Fundamental Turn Toward Concurrency in Software](http://www.gotw.ca/publications/concurrency-ddj.htm) from 2005
* [C10k Problem](https://en.wikipedia.org/wiki/C10k_problem) from 1999


## Go Designed by
{id: go-designed-by}

* [Robert Griesemer](https://github.com/griesemer)
* [Rob Pike](https://en.wikipedia.org/wiki/Rob_Pike)
* [Ken Thompson](https://en.wikipedia.org/wiki/Ken_Thompson)

* At Google

## Open Souce
{id: open-source}

{aside}
To some people, yours truly included, it is important to know that the go compiler is open source. You can find its source code on GitHub.
{/aside}

* [Source code](https://github.com/golang/go)
* [The Go compiler is written in Go](https://blog.golang.org/go1.5)
* [How to compile the Go compiler](https://golang.org/doc/install/source) way beyond our needs.

## Platforms
{id: platforms}

{aside}
Go can be compiled to the 3 major desktop operating systems and to few other, smaller ones. It can be used in mobile environments,
but as far as I know it does not have a good solution for the GUI part.
{/aside}


* Linux
* Mac OSX
* MS Windows
* ...
* [mobile: Android/iOS](https://github.com/golang/go/wiki/Mobile)


## Major Open Source Projects
{id: major-open-source-projects}

{aside}
It might be important for you to know that there are a number of very important and high-profile Open Source projects written in Go.
There are also thousands of other, much smaller Open Source projects that you can find primarily on GitHub.

One of my recommendations for when you are learning Go (or any other programming language) is to find some Open Source projects in areas where you are interested and
start reading their code. Try to make some changes and send them back as contributions. That can be a really nice way to get involved in something real with the pressure you might have when you work on a project in a company.
{/aside}

* [Docker](https://github.com/docker)
* [Kubernetes](https://github.com/kubernetes/kubernetes)
* [Terraform](https://github.com/hashicorp/terraform)

* [Go topic on GitHub](https://github.com/topics/go)
* [Trending Go projects on Github](https://github.com/trending/go?since=monthly)


* [Directory of Open Source Projects in Go](https://github.com/golang/go/wiki/Projects)

## Install Golang
{id: install}

* [Golang home](https://golang.org/)
* [Download](https://golang.org/dl/)
* Install in the standard location offered by the installer!

## Show Installed Version of Golang
{id: version}
{i: version}

{aside}
Once you have installed the Go compiler, let's check that you can run it on the command line.
In MS Windows open a CMD window, or if you use Linux/Mac open a terminal and type:
{/aside}

```
$ go version
```

the output should look something like this:

```
go version go1.12.9 linux/amd64
```

## Editor/IDE for Golang
{id: editor}
{i: editor}
{i: IDE}

{aside}
In order to write some Go program you will need a text editor. You can use Notepad++ on Windows or vim or emacs anywhere, but the recommended editor is the Visual Studio Code of Microsoft using the Go plugins. You can download it from the link bellow.

When you open your first file with a .go extension it will offer you to install the plugins. Let it install everything it wants to.
At the end you might need to restarted the IDE.
{/aside}


* [Visual Studio Code](https://code.visualstudio.com/) (It has plugins for Golang)
* [Other editors and IDEs](https://golang.org/doc/editors.html)
* Any text editor


## Hello World
{id: hello-world}
{i: package}
{i: main}
{i: import}
{i: func}
{i: run}
{i: build}
{i: fmt}

![](examples/hello-go/hello_world.go)

```
go run hello_world.go
```

![](examples/hello-go/hello_world.out)

* main function is the entry point of every program
* [fmt.Print](https://golang.org/pkg/fmt/#Print)

{aside}
Every Go program has a main file that must start with "package main" and it must have a function called `main`.

In order to print something to the screen we first need to import the `fmt` class and then inside the "main" function we can write
`fmt.Println("Hello World")`.

We save this with a .go extension. Then we can run it from the command line by typing `go run` and the name of your file.
This will compile the code into a temporary directory and then run it.
{/aside}


## Build Hello World exe
{id: build-hello-world}

{aside}
If you'd like to crete a distributable version of your code you can type `go build` and the name of your file. That will create an executable
with the same name (just without the extension). This is specific to the Operating System and platform you currently use. Later we'll see how 
{/aside}


```
go build hello_world.go
./hello_world
```

* [Annotated Hello World in Go](https://www.353solutions.com/annotated-go)

## Source of examples
{id: source-of-examples}

{aside}
{/aside}

* [Slides on Github](https://github.com/szabgab/slides)
* Clone or download as a ZIP file.

## Separate directories! - main redeclared in this block
{id: separate-directories}

* Put each example / exercise in a separate directory
* As each package must have only one main() function.

![](examples/same/same_one.go)
![](examples/same/same_two.go)

```
go run .
```

![](examples/same/same.out)



## Exercise: Hello World
{id: exercise-hello-world}

This exercise is "easy" it is here to make sure you managed to set up your development environment
that can be very frustrating if your computer has some special configurations. Which is quite common.

* Install go if you don't have it yet.
* Install an editor/IDE with the appropriate plugin for go.
* Check if `go version` is running.
* Write the Hello World program and run it both from the IDE and from the command line.
 

