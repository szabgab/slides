numbers = [10, 20, 7, 21, 5]
puts numbers
small = numbers.select do |num|
  num > 10
end
puts small
puts numbers.select { |num| num > 10 }
puts numbers
puts ""

big = numbers.select! do |num|
  num < 10
end
puts big
puts numbers
