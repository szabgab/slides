iris = read.table(file="data/iris.txt", sep=" ", header=T, stringsAsFactors=T)
head(iris)

# hist(iris$Sepal.Length)
hist(iris$Petal.Width)

mean_petal_width = mean(iris$Petal.Width)
hist(
    x=iris$Petal.Width,
    breaks=10,
    col="light blue",
    main="Distribution of Petal Width",
    xlab="Width of Petal (cm)",
    #ylab="",
    sub=paste("Mean", mean_petal_width), # paste concatentes values
    )

#help(hist)
#View(iris)
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


plot(iris$Petal.Length, iris$Sepal.Length)
help(plot)  # or ?plot

plot(
  x=iris$Petal.Length,
  y=iris$Sepal.Length,
  #type="l",  # or p for points
  #pch=20,  # change how the points look like

  # col (short for color)
  #col="purple red",

  col=iris$Species,
  #pch=19

  xlab="X Title",
  ylab="Y Title",
  main="Main heading",
  sub="Sub heading",
)

# In the iris dataset when we draw a histogram how does it pick colors when we only have names?
# Because it is a factor (beacise of the stringsAsFactors)
class(iris$Species) # "factor"
# Each "level" in the factor has a numerical value (1, 2, 3) and in R each color also a number (1 = black 2 = red, etc)


plot(
  x=iris$Petal.Length,
  y=iris$Sepal.Length,
  pch=as.numeric(iris$Species),
)

# TODO: how to pick the specific colors?

# how to color the point accorind to some other condition? e.g. iris$Sepal.width > 2
plot(
  x=iris$Petal.Length,
  y=iris$Sepal.Length,
  col=as.numeric(iris$Sepal.Width > 3)+1
)
# iris$Sepal.Width > 2   is a boolean vector
# as.numeric(iris$Sepal.Width > 2) is a numerical vector of 0 and 1 values
# careful: color 0 is white so we won't see it, that's why we add 1 so instead of 0 and 1 we will get 1 and 2 values.


levels(iris$Species) # "setosa" "versicolor" "virginica"

help(data.frame)


pairs(iris[,1:4])  # pairwise relation graphs
pairs(iris[,1:4], col=as.numeric(iris$Species))
pairs(iris[,1:4], col=as.numeric(iris$Species), upper.panel=NULL)
