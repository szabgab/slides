iris = read.table(file="data/iris.txt", sep=" ", header=T, stringsAsFactors=T)
head(iris)
ord = order(iris$Sepal.Length)
head(iris[ord,])
