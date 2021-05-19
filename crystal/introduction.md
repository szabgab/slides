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

![](examples/shard.yml)

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

* Interpolation is the embedding of variables in strings using `#{}`

![](examples/intro/hello_name_interpolation.cr)

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

## List Methods
{id: list-methods}

![](examples/methods.cr)
![](examples/methods.out)


## List directory content
{id: list-directory}
{i: Dir}

![](examples/list_dir.cr)

## List directory tree
{id: directory-tree}
{i: Dir}
{i: glob}
![](examples/traverse_tree.cr)

## Get Current workding directory (cwd, pwd)
{id: current-working-directory}

![](examples/cwd.cr)


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

## Checking the slides
{id: checking-the-slides}

![](examples/check_slides.cr)

## Crystal mine
{id: crystal-mine}

![](examples/mine.cr)


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


## Testing
{id: testing-1}

![](examples/test1/mymath.cr)
![](examples/test1/use_mymath.cr)
![](examples/test1/mymath_spec.cr)


```
crystal spec .
```

## Other
{id: other}

* Single quotes vs double quotes

No type-checking?

x = "one"
x = 1
p! x
p! typeof(x)



