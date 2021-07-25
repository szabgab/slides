# Other
{id: other}

## Sequence
{id: sequence-generation}

![](examples/other/sequence.cr)

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

## Gravatar
{id: gravatar}
{i: Digest::MD5.hexdigest}

![](examples/other/gravatar.cr)

## Try Crystal
{id: try}

![](examples/try.cr)

## STDERR, STDOUT
{id: stderr}
{i: STDERR}
{i: STDOUT}

![](examples/other/stderr.cr)

* Redirection on the command line using > out  and 2> err

## Return Boolean
{id: return-boolean}

![](examples/functions/return_bool.cr)

## Symbols
{id: symbols}

![](examples/other/symbols.cr)

## Docspec
{id: docspec}

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

* You can put the `require` statements anywhere but you might want to be consistent in your project.
* Make sure you don't have circular requires.

## Constants
{id: constants}

* Variable names that start with upper-case letter are constants

![](examples/other/constants.cr)

## Multiple assignment
{id: multiple-assignment}

* [Multiple assignment](https://crystal-lang.org/reference/syntax_and_semantics/assignment.html#multiple-assignment)

![](examples/other/multiple_assignment.cr)

## Chained assignment
{id: chained-assignment}

* [Chained assignment](https://crystal-lang.org/reference/syntax_and_semantics/assignment.html#chained-assignment)

![](examples/other/chained_assignment.cr)

## Int methods: Times
{id: times}

![](examples/other/times.cr)

## Int64 Zero
{id: int64-zero}

![](examples/other/int64_zero.cr)

## Question mark: ?
{id: question-mark}
{i: ?}

* meaning "or nil" in type definitions `String?` is the same as `String | Nil`
* Methods ending with `?` usually return a boolean (true, false) - there is no enforcement of this in Crystal
* If a construct might raise an exception adding a question mark can convert that into returning nil
* It is also part of the conditional operator `?:`

![](examples/other/questionmark.cr)

## Exclamation mark: !
{id: exclamation-mark}
{i: !}

* Methods ending with `!` usually modify the underlying object.
* Logical not (before an expression)

## Ampersand: &
{id: ampersand}
{i: &}

* [short syntax](https://crystal-lang.org/reference/syntax_and_semantics/blocks_and_procs.html#short-one-parameter-syntax)

## STDIN don't accept nil
{id: stdin-dont-accept-nil}

* `gets` will retun `nil` if we press Ctrl-D
* `gets.not_nil!` will raise an exception

![](examples/other/gets_not_nil.cr)


## Math
{id: math}

* [Math](https://crystal-lang.org/api/Math.html)

![](examples/other/math.cr)

## Proc
{id: proc}
{i: Proc}

* [Proc](https://crystal-lang.org/api/Proc.html)

![](examples/other/proc.cr)

## Enums
{id: enums}
{i: enum}

![](examples/other/enums.cr)

## Type of array elements
{id: type-of-array-elements}

![](examples/other/type_of_array_elements.cr)

All the elements of an array "inherit" the type from the array

## Environment variables
{id: environment-variables}
{i: ENV}

![](examples/other/env.cr)


## Int32 or Nil
{id: int32-or-nil}

![](examples/other/int_or_nil.cr)

## Resources
{id: resources}

* [Crystal Programming](https://www.youtube.com/watch?v=DxFP-Wjqtsc) by Derek Banas from 2018
* [Crystal: Fast as C, Slick as Ruby](https://www.youtube.com/watch?v=m8bYqfrGjGo) by [Tom Richards](https://github.com/t-richards) from [Delegator](https://www.delegator.com/) form 2017
* [LuckyCast](https://luckycasts.com/)

* [Crystal for Rubyists](https://www.crystalforrubyists.com/)
* [Crystal Weekly](https://crystalweekly.com/) by Serdar Doğruyol
* [Friends of Crystal](https://friendsofcrystal.com/) by Serdar Doğruyol
* [Programming Crystal book](https://www.pragprog.com/titles/crystal/programming-crystal/)

* [Facebook page](https://www.facebook.com/Crystallang-1457045254320264/)
* [Facebook group](https://www.facebook.com/groups/crystallang/)
* [LinkedIn page](https://www.linkedin.com/company/crystal-language/)

