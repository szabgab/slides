def f(x, y)
  return x + y
end

def f(args : Array(Int32))
  return f(args[0], args[1])
end

puts f(2, 3)
values = [3, 4]
puts values
puts f(values)
