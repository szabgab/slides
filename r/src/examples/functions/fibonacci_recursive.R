fibonacci=function(n) {
    if (n == 1) {
        return(1)
    }
    if (n == 2) {
        return(1)
    }
    return(fibonacci(n-1) + fibonacci(n-2))
}

for (n in 1:10) {
    cat(fibonacci(n), end="\n")
}


