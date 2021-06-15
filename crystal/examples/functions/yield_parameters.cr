def run(number, &block)
  puts "before"
  yield number
  puts "after"
end

run(10) {|value|
  puts "in block #{value}"
}
puts "----"

run(20) do |value|
  puts "in do-end #{value}"
end

