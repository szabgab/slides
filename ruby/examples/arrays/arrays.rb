names = ["Anna", "Bea", "Cecil", "David"]
puts names.class # Array
puts ''

puts names
puts ''

puts names[0]
puts ''

puts names[-1]
puts ''

puts names[0,3] # range
puts ''

names.each do |name|
  puts name
end

[1, 2, 3].each do |number|
  puts number
end
