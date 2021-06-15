def run
  puts "before"
  yield
  puts "after"
end

run {
  puts "in block"
}

run do
  puts "in do-end"
end
