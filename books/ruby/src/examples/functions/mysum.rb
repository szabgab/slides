def mysum(*numbers)
  sum = 0
  numbers.each do | number |
    sum += number
  end

  return sum
end

puts mysum()
puts mysum(42)
puts mysum(2, 3)
puts mysum(1, 7, 8)
