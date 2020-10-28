fruits = c("Apple", "Banana", "Peach")
nums = c(3, 7, 5)

names(nums) = fruits

print(nums["Peach"])
print(class(nums["Peach"]))
