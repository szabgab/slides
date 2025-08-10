numbers = [2, -3, 4, -5]
puts numbers
puts ""

doubles = numbers.map do |num|
  num*2
end
puts doubles
puts numbers
puts ""

triples = numbers.map { |num| num*3 }
puts triples
puts numbers
puts ""

abs = numbers.map &.abs
puts abs
puts numbers
puts ""

abs = numbers.map! &.abs
puts abs
puts numbers
