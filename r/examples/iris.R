filename = "/home/gabor/Dropbox/Weizmann/R/iris_dataset.txt"

# setwd - set working directory
# getcwd - get working directory
ir = read.table(filename, sep="\t", header=T)
head(ir, 3)
tail(ir, 3)
View(ir)   # Capital V !!! (opens a separate view of the data)
class(ir)  # data.frame
dim(ir)  # 150 5  dimensions: (rows, columns)
ir[2, 3]
head(ir)
# The indexes on the left hand side are also called "row-names"

ir[,1]     # access a column by its location
ir$seplen  # access a column by its name 

ir1 = ir[, c("seplen", "sepwid")]  # dataframe
head(ir1)

column = ir[, c("seplen")] # numberic vector

summary(ir)
