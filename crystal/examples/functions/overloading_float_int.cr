def add(x : Int32, y : Int32)
  puts "handling two integers"
end

def add(x : Float64, y : Float64)
  puts "handling two floats"
end

add(2, 3)
add(2.1, 3.1)
add(2.1, 3)
