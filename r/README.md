R Notebooks
Bioconductor Project - Bioinformatic R packages

Data types


Numeric
Logical
Character
Factor      factor()

Vectors can only store the same data type


You can use either single quotes or double quotes for string. They mean the same.

base-R Cheatsheet 
R-style Guide by Hadley Whickham


We get a warnng if we try to do an operation on two verctors where their lengthes are not the multiplication of each other.
How can we turn these warnings into errors?
How can we hide these warnings
How can we get an error even if they are multiples but if they are not the exact same size as other languges would do?
When is this repetition feature useful?


Operator precedence in R

Logical operators (boolean operators)  & | !
Conditional operators (??)     > <  == !=    performed on numerical variables

We can use conditional operators on vector - scalar
a = c(2, 3, 4)
a > 3
a == 3

b = c(7, 3 , 2)
a > b
a == b


n can be a single value or a vector:
(n != 3) & (n < 5)

n = c(2, 5, 7)
n[c(2, 3)]  accessing positions by index
names(n) = c("one", "two", "three")
n["two"]


vectors c() have "class"  (type)

data.frames  tables, each column can have a different class (type)
matrix - same idea as a data.frame but all values are the same class (type)
  m = as.matrix(iris[,1:4])
  colnames(m)
  names(data.frame)
  colnames(

Iris database (Petal, Sepal)
http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html

getwd() Get current working directory cwd
setwd("c://.../")   # change directory
setwd("/home/gabor/work/slides/r")

install.packages("here")
library(here)

"rowname" or index of each row in a data.frame


factors are categorized vectors where each element has defiend levels
levels are ordered.

names of levels that might include names that are not currently in the vector.
factor(some_vector, levels=c(

can only add elements to a factor that are listed as levels.

from facto to get back the original numeric values:
char_vec = as.characters(some_factor)
as.numeric(char_vec)


#!/usr/bin/env Rscript
