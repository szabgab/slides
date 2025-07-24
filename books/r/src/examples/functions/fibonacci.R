fibonacci=function(n) {
    if (n == 1) {
        return(1)
    }
    if (n == 2) {
        return(1)
    }
    fibs = c(1, 1)
    for (i in 3:n) {
        last = fibs[length(fibs)] + fibs[length(fibs)-1]
        fibs = append(fibs, last)
    }
    return(fibs)
}

cat(fibonacci(10), end="\n")


