.libPaths(append(.libPaths(), "lib"))
install.packages("jsonlite", "lib")
library("jsonlite")

filename = "r.json"
data = read_json(filename)


