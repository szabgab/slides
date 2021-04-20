iris = read.table(file="data/iris.txt", sep=" ", header=T)
    # stringsAsFactors=T
head(iris)

# View(iris)  #  did not work for me
#tail(iris)
# iris

#class(iris)
#dim(iris)   # rows, columns

# iris[2, 4]
# iris[1, ]
# iris[, 1]
#iris$Sepal.Length
#iris['Sepal.Length']   # numeric vector
#iris[c('Sepal.Length', 'Petal.Length')]  # data.frame
#iris[,c('Sepal.Length', 'Petal.Length')] # data.frame
#summary(iris)
colnames(iris)

