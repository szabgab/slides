def sum(*numbers : Int32)
  puts typeof(numbers) # Tuple(Int32, Int32, Int32)
  numbers.sum
end

res = sum(2, 3, 4)
puts res # 9
