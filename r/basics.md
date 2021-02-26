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


## R and variables
{id: r-variables}

![](examples/variables.R)


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

* It is some_vectpr[n]
* It is 1-based

![](examples/access_vector_element.R)

## Negative index, exclude element
{id: negative-index-exclude-element}

Using a negative index will give you the same vector without that element

![](examples/negative_index.R)

## Access several elements of a vector
{id: access-several-elements-of-a-vector}

We can use a vector as the index of anther vector thereby fetching a new vector of the specific values.

![](examples/several_elements.R)


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

```
distances = c(11, 15, 7, 23, 9)
barplot(distances)
plot(distances)
hist(distances)
boxplot(distances)
pie(distances)


barplot(distances, col="purple")
barplot(distances, col="#2323AA")
barplot(distances, col="#2323AA", ylab="Text on Y", xlab="Text on X")
```

Would create a file called Rplots.pdf.


Random numbers in normal distribution

normal_numbers = rnorm(100)

Histogram of the numbers
hist(normal_numbers)

![](examples/barplot.R)

## Associate name with each value
{id: associate-name-with-each-value}

![](examples/associate_name.R)

barplot this!

## paste (join) strings and numbers together
{id: paste-strings-together}
{i: paste}

paste("abc", "def", "qqrq")
paste("abc", "def", "qqrq", sep="_")


fruits = c("Apple", "Banana", "Apple", "Peach")
f = as.factor()
levels(f)
summary(f)

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


