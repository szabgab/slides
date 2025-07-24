all_nums = c(3, 7, 2, 40, 8)
mean(all_nums)   # 12

missing_nums = c(3, 7, 2, NA, 8)
mean(missing_nums)  # NA

mean(missing_nums, na.rm = TRUE)  # 5
