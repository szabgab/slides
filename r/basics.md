# R - basics
{id: basics}

## Background
{id: background}

* Open Source
* Relatively Slow

## Alternatives
{id: alternatives}

* Excel - Not really, but people use it anyway.
* Matlab
* Python, Perl, ...

## Install R
{id: install-r}


* [Install R](https://cran.r-project.org/)

Ubuntu:

```
sudo apt-get install r-base
```

## Install R Studio
{id: install-r-studio}

[Download R Studio](https://rstudio.com/products/rstudio/download/) the IDE used to write and execute R code.


## Launch interactive R, get help, and quit
{id: launch-interactive}
{i: R}
{i: help}
{i: q}


```
$ R
> help()
> help(class)
...
> q()
```

## Running R on the command line using Rscript
{id: running-r-scripts-on-the-command-line}
{i: Rscript}
{i: print}

![](examples/basics/hello_world.R)

```
Rscript hello_world.R
```

## Comments
{id: comments}

* Lines starting at a "#" character are comments

![](examples/basics/comments.R)


## R and simple math operations
{id: r-and-simple-math-operations}

![](examples/basics/calc.R)


## R variables
{id: r-variables}

![](examples/basics/variables.R)

## R assignment (left-assignment, right-assignment)
{id: r-assignment}

* Both = and <- can be used for left-assignment
* -> Can be used for right-assignment

![](examples/basics/assignment.R)

## Variable types (numeric, character, logical, function)
{id: variable-types}
{i: class}
{i: isa}
{i: numeric}
{i: character}
{i: logical}
{i: function}

* numeric:     1   34  2.7
* character:   "hello"   "23"
* logical:     TRUE  FALSE
* function:    class print

![](examples/basics/data_types.R)

![](examples/basics/data_types_isa.R)

## Variable types are deducted
{id: variable-types-are-deducted}
{i: class}
{i: isa}
{i: numeric}
{i: character}
{i: logical}

![](examples/basics/variable_data_types.R)

## paste (join) strings and numbers together
{id: paste-strings-together}
{i: paste}

![](examples/basics/paste_examples.R)

## Operator preference order and parentheses
{id: operator-peference-order-and-parentheses}

## Operators comparing numbers
{id: operators-comparing-numbers}

![](examples/basics/compare_numbers.R)

## Operators comparing strings (characters)
{id: operators-comparing-strings}

* characters are compared in ABC order (but not ASCII order!)

![](examples/basics/compare_strings.R)

## Convert string (character) to numeric
{id: convert-string-to-numeric}
{i: as.numeric}

* as.numeric

![](examples/basics/convert_string_to_numeric.R)

## Boolean (logical) operations
{id: boolean-operations}

![](examples/basics/logical_boolean.R)

![](examples/basics/boolean_operations_on_numbers.R)

## Concatenate strings
{id: concatenate-strings}

![](examples/basics/concatenate_strings.R)

## Convert between types using as.
{id: converting-between-types-using-as}

* as.factor

## Printing with cat
{id: printing-with-cat}

![](examples/basics/cat.R)

