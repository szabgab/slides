# R
{id: r}

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

[Download R Studio](https://rstudio.com/products/rstudio/download/)


## Launch interactive R and quit
{id: launch-interactive}
{i: R}
{i: q}


```
$ R
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


## Variable types are deducted
{id: variable-types-are-deducted}
{i: class}
{i: numeric}
{i: character}
{i: logical}

![](examples/basics/data_types.R)

## Repeate the same number
{id: repeate-the-same-number}
{i: rep}

![](examples/repeat_number.R)

## Range of numbers
{id: range-of-numbers}
{i: :}

![](examples/range_of_numbers.R)


## paste (join) strings and numbers together
{id: paste-strings-together}
{i: paste}

![](examples/paste_examples.R)

## Comments
{id: comments}

* Lines starting at a "#" character are comments

## Operator preference order and parentheses
{id: operator-peference-order-and-parentheses}

## Operators comparing values
{id: operators-comparing-values}

![](examples/conditional_operators.R)

## Convert between types using as.
{id: converting-between-types-using-as}

* as.numeric
* as.factor


## Convert string to numeric
{id: convert-string-to-numeric}

![](examples/convert_string_to_numeric.R)



## Boolean (logical) operations
{id: boolean-operations}

![](examples/boolean_vectors_truth_table.R)

![](examples/logical_boolean.R)

![](examples/boolean.R)

![](examples/boolean_operations_on_numbers.R)

## Concatenate strings
{id: concatenate-strings}

![](examples/concatenate_strings.R)

## Filesystem pathes
{id: filesystem-pathes}

![](examples/pathes.R)

