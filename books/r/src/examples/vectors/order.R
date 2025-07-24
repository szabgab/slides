numbers = c(7, 3, 9, 11, 2)
order(numbers)   # 5 2 1 3 4
numbers[order(numbers)]  # 2  3  7  9 11

fruits = c("apple", "peach", "lemon", "banana", "ananas")
order(fruits)                 #  5 1 4 3 2
fruits[ order(fruits) ]       # "ananas" "apple"  "banana" "lemon"  "peach"
fruits[ order(fruits, decreasing = T) ]  # "peach"  "lemon"  "banana" "apple"  "ananas"
