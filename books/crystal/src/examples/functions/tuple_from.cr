def f(x, y)
  return x + y
end

puts f(2, 3)
values = [3, 4]
puts values

puts f(*{Int32, Int32}.from(values))
