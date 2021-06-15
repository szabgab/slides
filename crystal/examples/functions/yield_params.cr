def run
  puts "before"
  yield 42
  puts "after"
end

run {|value|
  puts "in block #{value}"
}
puts "----"

run do |value|
  puts "in do-end #{value}"
end
puts "----"


run {
  puts "in block"
}
puts "----"

run do
  puts "in do-end"
end

