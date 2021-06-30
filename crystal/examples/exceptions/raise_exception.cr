puts fibonacci(2)
puts fibonacci(-1)
puts fibonacci(3)

def fibonacci(num)
  if num < 0
    raise "Invalid number"
  end
  # ...
  return num
end
