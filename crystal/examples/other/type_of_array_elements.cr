values = [1, 2, "three", "four"]
puts typeof(values)
puts typeof(values[0])
puts typeof(values[2])
puts ""

values.each { |val|
  puts typeof(val)
  # puts val.size
  # Error: undefined method 'size' for Int32 (compile-time type is (Int32 | String))

  if val.is_a?(String)
    puts val.size
  end
}
