
.libPaths(append(.libPaths(), "lib"))
install.packages("csv", "lib")
library("csv")

filename = "a.csv"
table = read.table(filename)

