
fruits = c("apple", "apple", "banana", "peach", "apple", "banana")
fruits
class(fruits)
length(fruits)
# A Factor is also a vector?? but with levels (which are the unique values in the original vector)
fruit_factor = as.factor(fruits)
class(fruit_factor)
length(fruit_factor)
fruit_factor
summary(fruits)
summary(fruit_factor)
# hist(fruits)       # must be numeric
# hist(fruit_factor) # must be numeric
levels(fruits) # NULL
levels(fruit_factor) # "apple" "banana" "peach"
labels(fruit_factor)
?factor
