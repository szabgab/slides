# R
{id: r}

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


## Running Rscript on the command line
{id: running-r-scripts-on-the-command-line}

![](examples/hello_world.R)


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

x = 23
class(x)     # numeric
x = "George"
class(x)     # character
x = True
class(x)   # logical

y = c(2, 7, 3)
class(y)


the_truth = c(TRUE, FALSE, TRUE, TRUE, FALSE)
class(the_truth)       # logical
sum(the_truth)         # 3
length(logical_vector) # 5

sum(TRUE)   # 1
sum(FALSE)  # 0


## Repeate the same number
{id: repeate-the-same-number}
{i: rep}

same_number = rep(2, 10)
print(same_number)

## Range of numbers
{id: range-of-numbers}
{i: :}

range_of_numbers = 1:10
print(range_of_numbers)


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

