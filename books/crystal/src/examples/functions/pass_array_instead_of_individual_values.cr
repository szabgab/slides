def f(x, y)
  return x + y
end

puts f(2, 3)
values = [3, 4]
puts values

puts f(values[0], values[1])

# puts f(values)
# Error: wrong number of arguments for 'f' (given 1, expected 2)
