.libPaths(append(.libPaths(), "lib"))
install.packages(setdiff("this.path", rownames(installed.packages())), "lib")
library("this.path")
root = dirname(this.path())
source(file.path(root, "mymath.R"))

if (add(2, 3) != 5) {
    exit(1)
}

if (add(2, -2) != 0) {
    exit(1)
}

