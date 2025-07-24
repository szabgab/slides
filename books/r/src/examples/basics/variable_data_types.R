x = 23
class(x)     # numeric

x = "George"
class(x)     # character

x = T
class(x)     # logical

isa(2, "numeric")  # TRUE
isa("2", "character")  # TRUE
isa(FALSE, "logical")  # TRUE
