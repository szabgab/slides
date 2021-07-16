# Introduction
{id: introduction}

## Crystal Language
{id: crystal-language}

* [Crystal lang](https://crystal-lang.org/)
* Syntax similar to Ruby
* [LLVM](https://llvm.org/) under the hood
* Ideas from Go, Erlang, Rust, Swift
* Statically type checked
* Built-in type inference
* Types are non-nilable (compile time check for lack of assignment)
* Meta-programming with Macro
* Concurrency with green threads called fibers
* C-bindings

## Crystal Shards (3rd party libraries)
{id: crystal-shards}
{i: shards}

* The 3rd party modules directory
* [Shardbox](https://shardbox.org/)
* [Crystal Shards](https://crystalshards.org/)
* Use `shards init` to create a file called `shard.yml` and describe the dependencies there.

## How to install 3rd party shards?
{id: install-shards}

* Create a file called `shard.yml` for your project listing the dependencies of this project
* Run `shards install`

![](shard.yml)

## Install Crystal
{id: install-crystal}

* [Install Crystal](https://crystal-lang.org/install/)

## Crystal in Docker on Linux
{id: docker-on-linux}

* [Docker Crystal](https://hub.docker.com/r/crystallang/crystal)
* Install Docker
* Create a file called `crystal` with the following content:

![](crystal)

* Make it executable by running `chmod +x crystal`
* Run `./crystal examples/intro/hello_world.cr`

Alternative:

Start docker container:

```
docker run --rm -it -w/opt -v$(pwd):/opt --name crystal -d crystallang/crystal tail -f /opt/Dockerfile
```

Execute in the running container:

```
docker exec crystal crystal examples/intro/hello_world.cr
```

Later you can stop the container:

```
docker -t0 stop crystal
```


## Hello World (puts)
{id: hello-world}
{i: puts}

![](examples/intro/hello_world.cr)

* `puts` stands for "put string"
* Adds a newline at the end

## Run Crystal source code
{id: run-crystal-from-source-code}

```
crystal hello_world.cr
```

## Compile Crystal to executable
{id: compile-crystal-to-executable}

```
crystal build hello_world.cr -o hello
./hello
```

## Speed of Crystal
{id: speed-of-crystal}

```
$ time crystal hello_world.cr
Hello World!

real  0m1.108s
user  0m1.268s
sys   0m0.271s
```

```
$ time crystal build hello_world.cr -o hw

real   0m1.108s
user   0m1.323s
sys    0m0.238s
```

```
$ time ./hw
Hello World!

real   0m0.013s
user   0m0.001s
sys    0m0.011s
```

## Hello World (print)
{id: hello-world-print}
{i: print}

* `print` does not add a newline
* You can add one by including `\n`

![](examples/intro/hello_world_print.cr)


## Hello Name (variables)
{id: hello-name}

* `print` will include an empty string between its parameters
* `puts` will include a newline between its parameters

![](examples/intro/hello_name.cr)
![](examples/intro/hello_name.out)


## Hello Name with interpolation
{id: hello-name-interpolation}
{i: #}

* Interpolation is the embedding of variables in strings using `#{}`

![](examples/intro/hello_name_interpolation.cr)
![](examples/intro/hello_name_interpolation.out)


## Interpolation
{id: interpolation}
{i: #}

* Interpolation using `#{}` for strings, integers, floating point numbers
* and even expressions.

![](examples/intro/interpolation.cr)
![](examples/intro/interpolation.out)


## Escaping - Alternative quote as delimiters
{id: escaping}
{i: %}

![](examples/intro/escaping.cr)
![](examples/intro/escaping.out)

## Debugging print p!
{id: debugging-print}
{i: p!}

* `p!` can be useful, especially for debugging prints as it includes the name of the variable.
* Here we see a simple string printed and then a slightly more complex data-structure.

![](examples/intro/debugging_print.cr)
![](examples/intro/debugging_print.out)

## Comments
{id: comments}

![](examples/intro/comments.cr)

## Code formatting
{id: code-formatting}

* 2-space indentation is the norm.

* Use the Crystal tool to format your code:

```
crystal tool format
```

* You can also use it in a CI system to verify code-formatting
* (You can also make the CI format it for you and commit the changes back to the repository)

```
crystal tool format --check
```

## Types - typeof
{id: types}
{i: typeof}
{i: String}
{i: Int32}
{i: Float64}
{i: Bool}
{i: p!}

* [Literals](https://crystal-lang.org/reference/syntax_and_semantics/literals/index.html)

![](examples/intro/types.cr)

## Compound Types - typeof
{id: compound-types}
{i: typeof}
{i: Array}
{i: Tuple}
{i: Hash}
{i: NamedTuple}

![](examples/intro/compound_types.cr)

## Add numbers - concatenate strings
{id: add-numbers}
{i: +}

* Interpolation works on numbers as well
* The `+` operator is numerical addition or string concatenation

![](examples/intro/add_numbers.cr)

## Add mixed strings and Integers
{id: add-mixed-strings-and-integers}

`Error: no overload matches 'Int32#+' with type String`

![](examples/intro/add_mixed.cr)


## Numeric Operators
{id: numeric-operators}


![](examples/intro/numerical_operators.cr)

## Methods of Int32
{id: int-methods}
{i: abs}
{i: round}
{i: even}
{i: gcd}

* [Int32](https://crystal-lang.org/api/Int32.html)

![](examples/intro/int32_methods.cr)

## Methods of Float64
{id: float-methods}
{i: abs}
{i: round}

* [Float64](https://crystal-lang.org/api/Float64.html)

![](examples/intro/float64_methods.cr)

## Program name
{id: program-name}
{i: PROGRAM_NAME}

![](examples/intro/program_name.cr)

* When running with `crystal examples/intro/program_name.cr`:

![](examples/intro/program_name.out)

We can also compile it

```
crystal build examples/intro/program_name.cr
```

* This will generate `program_name` (as that was the name of our source file)
* We can rename it: `mv program_name other`
* We can run it `./other` and it will print the name of the executable file `other`.


* [See other toplevel variables](https://crystal-lang.org/api/toplevel.html)


## Command line arguments - ARGV
{id: command-line-arguments}
{i: ARGV}

* ARGV is an Array of Strings. `Array(String)`

![](examples/intro/cli.cr)


## Early exit
{id: exit}
{i: exit}

![](examples/intro/early_exit.cr)

* Exit code defaults to 0

```
echo $?
echo %ERROR_LEVEL%
```

## Rectangle
{id: rectangle}

![](examples/intro/rectangle.cr)




## True values
{id: true-values}

* `false`, `nil`, and the null pointer are "falsy" everything else, including 0 and "" are `true`

![](examples/intro/true_values.cr)
![](examples/intro/true_values.out)

## Math - PI
{id: math-pi}
{i: PI}
{i: Math}

![](examples/intro/math.cr)
![](examples/intro/math.out)

## Read from STDIN
{id: read-from-stdin}
{i: gets}

![](examples/intro/gets.cr)

## Interactive envrionments
{id: interactive-environments}

* `crystal play`
* [icr](https://github.com/crystal-community/icr)
* [tree](https://github.com/pebauer68/tree)

## Crystal one-liners
{id: crystal-one-liners}
{i: eval}

* `crystal eval`

## Crystal and random numbers
{id: random-numbers}

![](examples/random/random.cr)
![](examples/random/random.out)

## Exercise: Hello World
{id: exercise-hello-world}

* Install Crystal.
* Verify that you can run it on the command line and print the version number `crystal --version`.
* Create a file called `hello_world.cr` that will print out "Hello World"

## Exercise: Hello Name - STDIN
{id: exercise-hello-name-stdin}

* Create a file called `hello_name_stdin.cr` that will ask the user for their name.
* Wait till the user types in their name.
* print "Hello NAME" with their name.

## Exercise: Hello Name - ARGV
{id: exercise-hello-name-argv}

* Create a file called `hello_name_argv.cr` that expects a name on the command line:
* `crystal hello_name_argv.cr FooBar`
* print "Hello FooBar" using whatever name the user provided.

## Exercise: Circle STDIN
{id: exercise-circle-stdin}

* Create a file called `circle_stdin.cr` that will ask the user for a number.
* Then wait till the user types in a number (the radius of a circle).
* Print the area and the circumference of the circle.

## Exercise: Circle ARGV
{id: exercise-circle-argv}

* Create a file called `circle_argv.cr` that will expect a number on the command line, the radius of a circle.
* Print the area and the circumference of the circle.

## Exercise: Calculator STDIN
{id: exercise-calculator-stdin}

* Create a file called `calculator_stdin.cr`
* Ask the user for two numbers and an operator `(+, -, *, /)`
* Compute the result of the operation and print it out.

## Exercise: Calculator ARGV
{id: exercise-calculator-argv}

* Create a file called `calculator_argv.cr` that the user can run with two numbers and an operator `(+, -, *, /)`.
* `crystal calculator_argv.cr 3 + 7`
* Compute the result of the operation and print it out.

## Exercise: Age limit
{id: exercise-age-limit-stdin}

* Create a script called `age_limit_stdin.cr`

* Ask the user what is their age.
* If it is above 18, tell them they can legally drink alcohol.
* If is is above 21, tell them they can also legally drink in the USA.

* Extra: ask the user for thir age and the name of their country and tell them if they can legally drink alcohol.
* See the [Legal drinking age](https://en.wikipedia.org/wiki/Legal_drinking_age) list.
* Don't worry if this seems to be too difficult to solve in a nice way. We'll learn more tools to improve.


