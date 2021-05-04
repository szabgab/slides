# This works using Rscript but not inside Rstudio and it installs the package on-the-fly
install.packages("scriptName")
library("scriptName")
current_filename()


species = c("setosa", "versicolor", "virginica")
species
species[1]
species[1] = "qqrq"
species
#colors = c("red", "green", "blue")
#names(species_to_color) = colors
#value(species_to_color["red"])



#args

# 
# barplot(c(2, 3, 7, 1))
# data <- rnorm(100)
# barplot(data)
# 
# fruits = c("apple", "apple", "banana", "peach", "apple", "banana")
# fruits
# class(fruits)
# # A Factor is also a vector?? but with levels (which are the unique values in the original vector)
# ff = as.factor(fruits)
# class(ff)
# length(ff)
# ff


