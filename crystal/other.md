# Other
{id: other}

## Spaceship Operator
{id: spaceship-operator}
{i: <=>}

![](examples/other/spaceship_operator.cr)

## Check if variable is nil?
{id: nil}
{i: nil}
{i: nil?}

![](examples/other/is_nil.cr)

## Single quotes vs double quotes
{id: single-quotes-vs-double-quotes}

* Single quotes are for characters
* Double quotes are for strings


## No type-checking?
{id: no-typechecking}

![](examples/other/assign_to_variable.cr)
![](examples/other/assign_to_variable.out)

## Divide by zero is Infinity
{id: divide-by-zero-is-infinity}
{i: Infinity}

![](examples/other/divide_by_zero.cr)

## Require other files
{id: require-other-files}

* [requiring files](https://crystal-lang.org/reference/syntax_and_semantics/requiring_files.html)

![](examples/one/welcome.cr)
![](examples/one/use_welcome.cr)

## List Methods
{id: list-methods}

![](examples/other/methods.cr)
![](examples/other/methods.out)


## Checking the slides
{id: checking-the-slides}

![](examples/check_slides.cr)

## Crystal mine
{id: crystal-mine}

![](examples/mine.cr)


## Ameba Linter
{id: ameba-linter}


* [Ameba](https://github.com/crystal-ameba/ameba)

![](.ameba.yml)

```
shards install
./bin/ameba
```

## Ternary operator and or to set default value
{id: default-value}
{i:||}
{i: ?:}

![](examples/other/default.cr)

## Gravatar
{id: gravatar}
{i: Digest::MD5.hexdigest}

![](examples/other/gravatar.cr)

## Try Crystal
{id: try}

![](examples/try.cr)

## case / when
{id: case}
{i: case}
{i: switch}
{i: when}

![](examples/other/case.cr)

## STDERR, STDOUT
{id: stderr}
{i: STDERR}
{i: STDOUT}

![](examples/other/stderr.cr)

* Redirection on the command line using > out  and 2> err

## Suffix if
{id: suffix-if}
{i: if}

![](examples/other/suffix_if.cr)

## Suffix unless
{id: suffix-unless}
{i: unless}

![](examples/other/suffix_unless.cr)

## Return Boolean
{id: return-boolean}

![](examples/functions/return_bool.cr)

## Symbols
{id: symbols}

![](examples/other/symbols.cr)

## Macros
{id: macros}

![](examples/macros/function.cr)


![](examples/docspec/shard.yml)

![](examples/docspec/spec/anagram_spec.cr)

![](examples/docspec/spec/doctes_spec.cr)

![](examples/docspec/src/app.cr)

## require
{id: require}

{aside}
require - imports are global. This makes it hard to see in a file where some objects might come from
as they might have been required by some other file.

Similarly requiring a bunch of files in a directory is easy to do, but might make it a bit harder for
someone without an IDE to find the source of each object.
{/aside}

```
require "./directory/file"  # relative path to the cr file
require "./directory/*"     # all the cr files in the directory
require "./directory/**"    # all the cr files in the directory - recursively
require "some_name"         # Find it somewhere (standard library, src directory)
```

* You can put the `require` statements anywhere but you might want to be consistent in your porject.
* Make sure you don't have circular requires.

## Constants
{id: constants}

* Variable names that start with upper-case letter are constants

![](examples/other/constants.cr)

## Multiple assignments
{id: multiple-assignments}

![](examples/other/multiple_assignments.cr)

![](examples/other/assign.cr)

## Int methods: Times
{id: times}

![](examples/other/times.cr)

## case of types
{id: case-of-types}

![](examples/other/case_when_on_type.cr)


## Int64 Zero
{id: int64-zero}

![](examples/other/int64_zero.cr)

## Resources
{id: resources}

* [Crystal Programming](https://www.youtube.com/watch?v=DxFP-Wjqtsc) by Derek Banas from 2018
* [LuckyCast](https://luckycasts.com/)


