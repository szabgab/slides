# R
{id: r}

## Background
{id: background}

* Open Source
* Relatively Slow

## Alternatives
{id: alternatives}

* Excel ????
* Matlab
* Python / Perl

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

![](examples/hello_world.R)

```
Rscript hello_world.R
```

## R and simple math operations
{id: r-and-simple-math-operations}

![](examples/calc.R)


## R variables
{id: r-variables}

![](examples/variables.R)

## R assignment (left-assignment, right-assignment)
{id: r-assignment}

* Both = and <- can be used for left-assignment
* -> Can be used for right-assignment

![](examples/assignment.R)


## R vectors
{id: r-vectors}
{i: c}

* c stands for concatenate

![](examples/vector.R)

![](examples/vector.out)


## Variable types are deducted
{id: variable-types-are-deducted}

![](examples/data_types.R)

## Repeate the same number
{id: repeate-the-same-number}
{i: rep}

![](examples/repeat_number.R)

## Range of numbers
{id: range-of-numbers}
{i: :}

![](examples/range_of_numbers.R)

## Access the n-the element of a vector
{id: access-the-n-the-element-of-a-vector}

* It is `some_vector[n]`
* It is 1-based

![](examples/access_vector_element.R)

## R Vector: Negative index, exclude element
{id: negative-index-exclude-element}

Using a negative index will give you the same vector without that element

![](examples/negative_index.R)

## R vector: Access several elements
{id: access-several-elements-of-a-vector}

* We can use a vector as the index of anther vector thereby fetching a new vector of the specific values.
* We can also select a range of elements using :

![](examples/several_elements.R)

## R vector: Exclude several elements
{id: exclude-several-elements-of-a-vector}

![](examples/exclude_elements.R)

## Some basic statistical functions
{id: some-basic-statistical-functions}
{i: median}
{i: sum}
{i: mean}
{i: min}
{i: max}

![](examples/statistics.R)

## Quick graphs
{id: quick-grapsh}

![](examples/quick_graph.R)

* Will create a file called Rplots.pdf.


## Random numbers in normal distribution
{id: random-numbers-in-normal-distribution}

```
normal_numbers = rnorm(100)
```

Histogram of the numbers

```
hist(normal_numbers)
```

## 3 ways to create vectors
{id: 3-ways-to-create-vectors}

![](examples/create_vectors.R)

## Bar plot
{id: bar-plot}

![](examples/barplot.R)

## Associate name with each value
{id: associate-name-with-each-value}

![](examples/associate_name.R)
![](examples/associate_name.out)

barplot this!

## paste (join) strings and numbers together
{id: paste-strings-together}
{i: paste}

![](examples/paste_examples.R)

## Comments
{id: comments}

* Lines starting at a "#" character are comments

## Operator preference order and parentheses
{id: operator-peference-order-and-parentheses}

## Data Frames
{id: data-frames}


![](examples/boolean_vectors_truth_table.R)

![](examples/conditional_operators.R)

![](examples/convert_string_to_numeric.R)

![](examples/different_length_of_arrays.R)

![](examples/factors.R)

![](examples/filter_values.R)

![](examples/index_of_true_elements.R)

![](examples/iris.R)

![](examples/logical_boolean.R)

![](examples/matrix.R)

![](examples/reuse_short_array_exact_multiple.R)

## R - sequences and ranges
{id: r-sequences-and-ranges}
{i: seq}

![](examples/seq.R)


