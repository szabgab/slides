def run
  puts "before"
  yield
  puts "middle"
  yield
  puts "after"
end

run {
  puts "in block"
}
puts "----"
run do
  puts "in do-end"
end
