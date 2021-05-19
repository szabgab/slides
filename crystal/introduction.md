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


## Interpolation
{id: interpolation}
{i: #}

* Interpolation using `#{}` for strings, integers, floating point numbers
* and even expressions.

![](examples/intro/interpolation.cr)


## Escaping - Alternative delimiters
{id: escaping}

![](examples/intro/escaping.cr)

## Types
{id: types}
{i: String}
{i: Int32}
{i: Float64}
{i: p!}

![](examples/intro/types.cr)


## Add numbers
{id: add-numbers}
{i: +}

* Interpolation works on numbers as well
* The `+` operator is numerical addition or string concatenation

![](examples/add_numbers.cr)

## Add mixed strings and Integers
{id: add-mixed-strings-and-integers}

`Error: no overload matches 'Int32#+' with type String`

![](examples/add_mixed.cr)


## Numeric Operators
{id: numeric-operators}


![](examples/numerical_operators.cr)

## Methods of int
{id: int-methods}

![](examples/number_methods.cr)

## if statement
{id: if}
{i: if}
{i: else}
{i: end}

![](examples/if.cr)

## elsif
{id: elsif}
{i: elsif}

![](examples/deep_if.cr)

![](examples/elsif.cr)


## Comparision Operators
{id: comparision-operators}

* ==, <, > <=, >=

* Spaceship operator <=> returns -1, 0, or 1


## Program name
{id: program-name}

![](examples/program_name.cr)
![](examples/program_name.out)

* [toplevel](https://crystal-lang.org/api/toplevel.html)


## Command line arguments - ARGV
{id: command-line-arguments}
{i: ARGV}

* ARGV is an Array of Strings. `Array(String)`

![](examples/cli.cr)


## Early exit
{id: exit}
{i: exit}

![](examples/early_exit.cr)

* Exit code defaults to 0

```
echo $?
echo %ERROR_LEVEL%
```

## Rectangle
{id: rectangle}

![](examples/rectangle.cr)




## True values
{id: true-values}

* `false`, `nil`, and the null pointer are "falsy" everything else, including 0 and "" are `true`

![](examples/true_values.cr)

## Math
{id: math}

![](examples/math.cr)
![](examples/math.out)


