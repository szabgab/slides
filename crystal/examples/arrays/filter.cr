numbers = [10, 20, 7, 21, 5]
puts numbers
small = numbers.reject do |num| num > 10 end
puts small

big = numbers.reject! do |num| num < 10 end
puts big
