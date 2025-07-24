x = "Foo"
y  = "Bar"

# x + y
# Error in x + y : non-numeric argument to binary operator
# Execution halted

z = paste(x, y, sep="")
z     # FooBar
length(z) # 1

# Join elements of a vector
fruits = c("Apple", "Banana")
q = paste(fruits, collapse ="-")
q     # Apple-Banana

# join elements of a numeric vector
numbers = c(2, 3, 4)
class(numbers)  # numeric
nums = paste(numbers, collapse ="-")
nums     # 2-3-4
