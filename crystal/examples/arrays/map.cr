
numbers = [2, -3, 4, -5]
puts numbers

doubles = numbers.map do |num| num*2 end
puts doubles

triples = numbers.map { |num| num*3 }
puts triples

abs = numbers.map &.abs
puts abs
