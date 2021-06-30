if Random.rand < 0.5
  x = 23
else
  x = "hello"
end

puts x

# puts x.abs # Error: undefined method 'abs' for String (compile-time type is (Int32 | String))
# puts x.size # Error: undefined method 'size' for Int32 (compile-time type is (Int32 | String))

case x
when String
  puts "string"
  puts x.size
when Int32
  puts "int32"
  puts x.abs
end
