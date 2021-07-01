# Introduction
{id: introduction}

## Crystal Language
{id: crystal-language}

* [Crystal lang](https://crystal-lang.org/)
* Similar to Ruby
* Statically type checked
* Built-in type inference
* Types are non-nilable (compile time check for lack of assignment)
* Meta-programming with Macro
* Concurrency with green threads called fibers
* C-bindings

## Crystal Shards
{id: crystal-shards}
{i: shards}

* The 3rd party modules directory
* [Crystal Shards](https://crystalshards.xyz/)
* Use `shards init` to create a file called `shard.yml` and describe the dependencies there.

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
