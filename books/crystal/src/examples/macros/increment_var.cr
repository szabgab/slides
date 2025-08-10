macro add_one_to(name)
  {{name}} += 1
end

x = 1
y = 1
puts x
puts y
add_one_to(x)
add_one_to(x)
add_one_to(x)
add_one_to(y)
puts x
puts y
