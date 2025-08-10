def welcome(name : String)
  return "Hello #{name}"
end

puts welcome "Foo"

# puts welcome 42
# Error: no overload matches 'welcome' with type Int32

def add(x, y : Int32)
  puts "#{x} #{y}"
end

add(2, 3)

# add(2, 3.1)
# Error: no overload matches 'add' with types Int32, Float64

add(2.1, 3) # this works
