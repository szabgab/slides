chars = c("1", "2", "3")
nums = as.numeric(chars)

print(class(chars))
print(class(nums))

print(summary(chars))
print(summary(nums))
print(sum(nums))   # 6 
print(sum(chars))  # invalid 'type' (character) of argument
