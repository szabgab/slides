# Introduction
{id: introduction}

## Crystal Language
{id: crystal-language}

* [Crystal lang](https://crystal-lang.org/)
* Similar to Ruby

## Crystal Shards
{id: crystal-shards}

* The 3rd party modules directory
* [Crystal Shards](https://crystalshards.xyz/)
* Use `shards init` to create a file called `shard.yml` and describe the dependencies there.

![](examples/shard.yml)



## Docker on Linux
{id: docker-on-linux}

* [Docker Crystal](https://hub.docker.com/r/crystallang/crystal)
* Install Docker
* Create a file called `crystal` with the following content:

![](crystal)

* Make it executable by running `chmod +x crystal`
* Run `./crystal examples/hello_world.cr`

Alternative:

Start docker container:

```
docker run --rm -it -w/opt -v$(pwd):/opt --name crystal -d crystallang/crystal tail -f /opt/Dockerfile
```

Execute in the running container:

```
docker exec crystal crystal examples/hello_world.cr
```

Later you can stop the container:

```
docker -t0 stop crystal
```


## Hello World (puts)
{id: hello-world}
{i: puts}

![](examples/hello_world.cr)

* `puts` stands for "put string"


## Hello Name (variables)
{id: hello-name}

![](examples/hello_name.cr)

## Hello Name with interpolation
{id: hello-name-interpolation}

![](examples/hello_name_interpolation.cr)

## Escaping - Alternative delimiters
{id: escaping}

![](examples/escaping.cr)


## Add numbers
{id: add-numbers}

![](examples/add_numbers.cr)

## Types
{id: types}
{i: String}
{i: Int32}
{i: Float64}
{i: p!}

![](examples/types.cr)


## Numeric Operators
{id: numeric-operators}


```
+
-
*
** (exponent)
/
// (floor division)
% (modulus)
```

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

## Strings
{id: strings}

![](examples/strings.cr)

## Empty and blank strings
{id: empty-strings}

![](examples/empty_strings.cr)

## Iterate over characters of a atring
{id: strings-iterator}

![](examples/string_iterator.cr)


## Type conversion to float, to int
{id: type-conversion}
{i: to_f}
{i: to_i}

![](examples/type_conversion.cr)

## Converting string to integer or float
{id: converting-string-to-integer-or-float}
{i: to_i}
{i: to_i?}
{i: to_f}
{i: to_f?}

![](examples/convertable.cr)
![](examples/convertable.out)

## Program name
{id: program-name}

![](examples/program_name.cr)
![](examples/program_name.out)

* [toplevel](https://crystal-lang.org/api/toplevel.html)


## Command line arguments - ARGV
{id: command-line-arguments}

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


## Arrays
{id: arrays}

![](examples/array.cr)

## Array iterate over (each, each_with_index)
{id: array-iterate}
{i: each}
{i: each_with_index}

![](examples/array_iterate.cr)

## Array push, append, <<
{id: arrays-push}
{i: push}
{i: append}
{i: <<}

![](examples/array_push.cr)

## Empty array
{id: array-empty}

* Empty array must come with a type definition

![](examples/empty_array.cr)

## Count digitis
{id: count-digits}

![](examples/count_digits.cr)


## Hash
{id: hash}
{i: has_key}
{i: each_key}

![](examples/hash.cr)

## Count words
{id: count-words}

![](examples/count_words.cr)

## Files
{id: files}

* Read from file
* Write to file
* Append to file
* Does file exist? Size of file? Modify date of file?


## Counter
{id: counter}

![](examples/counter.cr)

## Multi Counter
{id: multi-counter}

![](examples/multi_counter.cr)

## True values
{id: true-values}

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

## Other
{id: other}

* Single quotes vs double quotes

No type-checking?

x = "one"
x = 1
p! x
p! typeof(x)


## HTTP Client
{id: http-client}

![](examples/http_client.cr)

## Checking the slides
{id: checking-the-slides}

![](examples/check_slides.cr)

## Crystal mine
{id: crystal-mine}

![](examples/mine.cr)
